# Copyright (c) 2026 ADBC Drivers Contributors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Render cached ADBC quickstart examples and their source listings.

The `quickstarts` directive renders the examples available for a driver from
https://github.com/columnar-tech/adbc-quickstarts.

The extension clones the repository lazily into the Sphinx doctree directory
and refreshes an existing checkout after one hour. If a refresh fails, it uses
the stale checkout and emits a warning. The repository, ref, and refresh period
can be changed with the `quickstarts_repository`, `quickstarts_ref`, and
`quickstarts_cache_ttl` Sphinx configuration values.

Examples are grouped into vendor and language tabs and rendered inline. Each
listing links to its example directory at the exact commit displayed by the
documentation build.
"""

from __future__ import annotations

import json
import shutil
import subprocess
import tempfile
import time
from pathlib import Path
from urllib.parse import quote

from docutils import nodes
from docutils.parsers.rst import directives
from sphinx.application import Sphinx
from sphinx.errors import ExtensionError
from sphinx.util.docutils import SphinxDirective
from sphinx.util.logging import getLogger
from sphinx.util.typing import ExtensionMetadata
from sphinx_design.shared import create_component

LOGGER = getLogger(__name__)
CLIENT_LIBRARIES_URL = "https://arrow.apache.org/adbc/current/client_libraries.html"
INTEGRATIONS_URL = "https://arrow.apache.org/adbc/current/integrations.html"
LANGUAGE_ENTRYPOINTS = {
    "cpp": ("main.cpp", "cpp"),
    "csharp": ("Program.cs", "csharp"),
    "go": ("main.go", "go"),
    "java": ("src/main/java/tech/columnar/Example.java", "java"),
    "javascript": ("main.js", "javascript"),
    "kotlin": ("src/main/kotlin/Main.kt", "kotlin"),
    "python": ("main.py", "python"),
    "r": ("main.R", "r"),
    "ruby": ("main.rb", "ruby"),
    "rust": ("src/main.rs", "rust"),
}
_CACHE_TIMESTAMP = ".adbc-quickstarts-refreshed"


def _run_git(*args: str, cwd: Path | None = None) -> str:
    try:
        result = subprocess.run(
            ["git", *args],
            cwd=cwd,
            check=True,
            capture_output=True,
            text=True,
            timeout=60,
        )
    except (OSError, subprocess.CalledProcessError, subprocess.TimeoutExpired) as exc:
        detail = getattr(exc, "stderr", None) or str(exc)
        raise ExtensionError(
            f"could not update ADBC quickstarts cache: {detail}"
        ) from exc
    return result.stdout.strip()


def _is_valid_checkout(path: Path) -> bool:
    return all(
        candidate.is_file()
        for candidate in (
            path / ".github" / "data" / "languages.json",
            path / ".github" / "data" / "databases.json",
        )
    )


def _cache_is_fresh(path: Path, ttl: int, now: float | None = None) -> bool:
    timestamp = path / _CACHE_TIMESTAMP
    if not timestamp.is_file():
        return False
    return (now if now is not None else time.time()) - timestamp.stat().st_mtime < ttl


def _clone_checkout(cache: Path, repository: str, ref: str) -> None:
    cache.parent.mkdir(parents=True, exist_ok=True)
    temporary = Path(
        tempfile.mkdtemp(prefix="temp_adbc_quickstarts_", dir=cache.parent)
    )
    try:
        _run_git(
            "clone",
            "--depth",
            "1",
            "--branch",
            ref,
            "--single-branch",
            repository,
            str(temporary),
        )
        if cache.exists():
            shutil.rmtree(cache)
        temporary.replace(cache)
    finally:
        if temporary.exists():
            shutil.rmtree(temporary)


def ensure_checkout(app: Sphinx, now: float | None = None) -> tuple[Path, str]:
    """Return a usable checkout and its exact commit SHA."""
    cache = Path(app.doctreedir) / "adbc-quickstarts"
    repository = app.config.quickstarts_repository
    ref = app.config.quickstarts_ref
    ttl = app.config.quickstarts_cache_ttl

    if not _is_valid_checkout(cache):
        _clone_checkout(cache, repository, ref)
        (cache / _CACHE_TIMESTAMP).touch()
    elif not _cache_is_fresh(cache, ttl, now):
        try:
            _run_git("fetch", "--depth", "1", "origin", ref, cwd=cache)
            _run_git("reset", "--hard", "FETCH_HEAD", cwd=cache)
            _run_git("clean", "-fdx", cwd=cache)
            (cache / _CACHE_TIMESTAMP).touch()
        except ExtensionError as exc:
            LOGGER.warning("%s; using the existing cached checkout", exc)

    if not _is_valid_checkout(cache):
        raise ExtensionError("ADBC quickstarts cache is incomplete")
    return cache, _run_git("rev-parse", "HEAD", cwd=cache)


def _load_metadata(checkout: Path) -> tuple[dict[str, str], dict[str, dict]]:
    data = checkout / ".github" / "data"
    try:
        languages = json.loads((data / "languages.json").read_text(encoding="utf-8"))
        databases = json.loads((data / "databases.json").read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ExtensionError(
            f"could not read ADBC quickstarts metadata: {exc}"
        ) from exc
    return languages, databases


def _vendors(driver: str, databases: dict[str, dict]) -> list[str]:
    info = databases.get(driver)
    if info is None:
        raise ExtensionError(f"unknown ADBC quickstarts driver: {driver}")
    if info.get("display_name_when_parent") is None:
        return [driver]
    return sorted(
        (slug for slug, vendor in databases.items() if vendor.get("parent") == driver),
        key=lambda slug: databases[slug]["name"].casefold(),
    )


def _example_directory(checkout: Path, language: str, driver: str, vendor: str) -> Path:
    nested = checkout / language / driver / vendor
    if nested.is_dir():
        return nested
    return checkout / language / vendor


def discover_examples(
    checkout: Path,
    driver: str,
    languages: dict[str, str],
    databases: dict[str, dict],
) -> list[dict]:
    """Discover source entrypoints grouped by vendor."""
    groups = []
    for vendor in _vendors(driver, databases):
        examples = []
        for language, display_name in languages.items():
            entrypoint = LANGUAGE_ENTRYPOINTS.get(language)
            if entrypoint is None:
                LOGGER.warning(
                    "no quickstarts entrypoint is configured for %s", language
                )
                continue
            directory = _example_directory(checkout, language, driver, vendor)
            if not directory.is_dir():
                continue
            source = directory / entrypoint[0]
            if not source.is_file():
                LOGGER.warning(
                    "quickstart directory %s has no expected entrypoint %s",
                    directory,
                    entrypoint[0],
                )
                continue
            examples.append(
                {
                    "language": language,
                    "language_name": display_name,
                    "source": source,
                    "directory": directory,
                    "lexer": entrypoint[1],
                }
            )
        examples.sort(key=lambda item: item["language_name"].casefold())
        if examples:
            groups.append(
                {
                    "vendor": vendor,
                    "vendor_name": databases[vendor]["name"],
                    "examples": examples,
                }
            )
    return groups


def _strip_copyright_header(source: str) -> str:
    """Remove a recognized leading Apache copyright header."""
    lines = source.splitlines(keepends=True)
    if not lines:
        return source

    end = None
    first = lines[0].lstrip()
    if first.startswith(("# Copyright", "// Copyright")):
        for index, line in enumerate(lines):
            if "limitations under the License." in line:
                end = index + 1
                break
    elif first.strip() == "/*" or first.startswith("/* Copyright"):
        for index, line in enumerate(lines):
            if "*/" in line:
                end = index + 1
                break

    if end is None:
        return source
    header = "".join(lines[:end])
    if "Copyright" not in header or "Licensed under the Apache License" not in header:
        return source
    while end < len(lines) and not lines[end].strip():
        end += 1
    return "".join(lines[end:])


def _default_language(examples: list[dict]) -> str:
    if any(example["language"] == "python" for example in examples):
        return "python"
    return examples[0]["language"]


def _language_tabs(
    checkout: Path,
    repository: str,
    commit: str,
    group: dict,
) -> nodes.container:
    tabs = create_component("tab-set", classes=["sd-tab-set"])
    default_language = _default_language(group["examples"])
    for example in group["examples"]:
        item = create_component(
            "tab-item",
            classes=["sd-tab-item"],
            selected=example["language"] == default_language,
        )
        item += nodes.rubric(
            example["language_name"],
            example["language_name"],
            classes=["sd-tab-label"],
        )
        content = create_component("tab-content", classes=["sd-tab-content"])
        source = _strip_copyright_header(example["source"].read_text(encoding="utf-8"))
        listing = nodes.literal_block(source, source)
        listing["language"] = example["lexer"]
        listing["classes"].append("quickstart-source")
        content += listing

        relative_directory = example["directory"].relative_to(checkout).as_posix()
        github_url = (
            f"{repository}/tree/{quote(commit, safe='')}/"
            f"{quote(relative_directory, safe='/')}"
        )
        link_text = (
            f"View the full {group['vendor_name']} quickstart for "
            f"{example['language_name']} on the columnar-tech/adbc-quickstarts repo"
        )
        link = nodes.paragraph()
        link += nodes.reference("", link_text, refuri=github_url)
        content += link
        item += content
        tabs += item
    return tabs


def _default_vendor(driver: str, groups: list[dict]) -> str:
    if any(group["vendor"] == driver for group in groups):
        return driver
    return groups[0]["vendor"]


def _vendor_tabs(
    driver: str, groups: list[dict], language_tabs: list[nodes.Node]
) -> nodes.container:
    tabs = create_component("tab-set", classes=["sd-tab-set"])
    default_vendor = _default_vendor(driver, groups)
    for group, languages in zip(groups, language_tabs, strict=True):
        item = create_component(
            "tab-item",
            classes=["sd-tab-item"],
            selected=group["vendor"] == default_vendor,
        )
        item += nodes.rubric(
            group["vendor_name"],
            group["vendor_name"],
            classes=["sd-tab-label"],
        )
        content = create_component("tab-content", classes=["sd-tab-content"])
        content += languages
        item += content
        tabs += item
    return tabs


class QuickstartsDirective(SphinxDirective):
    """Render all cached quickstart examples for one driver."""

    required_arguments = 1
    final_argument_whitespace = False
    has_content = False
    option_spec: dict = {}

    def run(self) -> list[nodes.Node]:
        driver = directives.unchanged_required(self.arguments[0]).strip().lower()
        checkout, commit = ensure_checkout(self.env.app)
        languages, databases = _load_metadata(checkout)
        groups = discover_examples(checkout, driver, languages, databases)
        if not groups:
            raise self.error(f"no quickstarts found for driver {driver!r}")

        repository = self.env.config.quickstarts_repository.removesuffix(".git")
        multiple_vendors = len(groups) > 1
        output = nodes.container(classes=["quickstarts"])
        language_tabs = [
            _language_tabs(checkout, repository, commit, group) for group in groups
        ]
        if multiple_vendors:
            output += _vendor_tabs(driver, groups, language_tabs)
        else:
            output += language_tabs[0]

        footer = nodes.paragraph()
        footer += nodes.Text("More languages are supported! Find an ")
        footer += nodes.reference(
            "",
            "ADBC client library",
            refuri=CLIENT_LIBRARIES_URL,
        )
        footer += nodes.Text(" for your language, or find an ")
        footer += nodes.reference(
            "",
            "integration",
            refuri=INTEGRATIONS_URL,
        )
        footer += nodes.Text(" for your data stack.")
        output += footer
        return [output]


def setup(app: Sphinx) -> ExtensionMetadata:
    app.add_config_value(
        "quickstarts_repository",
        "https://github.com/columnar-tech/adbc-quickstarts.git",
        "env",
    )
    app.add_config_value("quickstarts_ref", "main", "env")
    app.add_config_value("quickstarts_cache_ttl", 3600, "env", types={int})
    app.add_directive("quickstarts", QuickstartsDirective)
    return {
        "version": "0.1.0",
        "parallel_read_safe": False,
        "parallel_write_safe": True,
    }
