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
import re
import shutil
import subprocess
import tempfile
import time
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import quote

from docutils import nodes
from docutils.parsers.rst import directives
from highlight_text import apply_highlight_text, parse_highlight_text
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
_REVISION = re.compile(r"[0-9a-fA-F]{40}")


def _run_git_raw(*args: str, cwd: Path | None = None) -> str:
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
    return result.stdout


def _run_git(*args: str, cwd: Path | None = None) -> str:
    return _run_git_raw(*args, cwd=cwd).strip()


def parse_revision(argument: str) -> str:
    """Require a full, unambiguous Git commit SHA."""
    revision = directives.unchanged_required(argument).strip().lower()
    if _REVISION.fullmatch(revision) is None:
        raise ValueError("revision must be a full 40-character Git SHA")
    return revision


@dataclass(frozen=True)
class GitSnapshot:
    """Read files and directory structure from one commit without checkout."""

    checkout: Path
    revision: str
    files: frozenset[str]

    @classmethod
    def load(cls, checkout: Path, revision: str) -> GitSnapshot:
        listing = _run_git("ls-tree", "-r", "--name-only", revision, cwd=checkout)
        return cls(checkout, revision, frozenset(listing.splitlines()))

    def is_dir(self, path: str) -> bool:
        prefix = path.rstrip("/") + "/"
        return any(candidate.startswith(prefix) for candidate in self.files)

    def is_file(self, path: str) -> bool:
        return path in self.files

    def read_text(self, path: str) -> str:
        if not self.is_file(path):
            raise ExtensionError(
                f"quickstarts file {path!r} does not exist at {self.revision}"
            )
        return _run_git_raw("show", f"{self.revision}:{path}", cwd=self.checkout)


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


def _has_commit(checkout: Path, revision: str) -> bool:
    try:
        _run_git("cat-file", "-e", f"{revision}^{{commit}}", cwd=checkout)
    except ExtensionError:
        return False
    return True


def _ensure_revision(checkout: Path, revision: str) -> str:
    if not _has_commit(checkout, revision):
        cache_ref = f"refs/adbc-quickstarts/revisions/{revision}"
        try:
            _run_git(
                "fetch",
                "--depth",
                "1",
                "origin",
                f"{revision}:{cache_ref}",
                cwd=checkout,
            )
        except ExtensionError as exc:
            raise ExtensionError(
                f"could not fetch requested quickstarts revision {revision}"
            ) from exc

    if not _has_commit(checkout, revision):
        raise ExtensionError(
            f"requested quickstarts revision {revision} is not a commit"
        )
    return _run_git("rev-parse", "--verify", f"{revision}^{{commit}}", cwd=checkout)


def ensure_checkout(
    app: Sphinx, now: float | None = None, *, revision: str | None = None
) -> tuple[Path, str]:
    """Return the latest checkout and selected commit without changing HEAD."""
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
    head = _run_git("rev-parse", "HEAD", cwd=cache)
    if revision is None or revision == head:
        return cache, head
    return cache, _ensure_revision(cache, revision)


def _load_metadata(snapshot: GitSnapshot) -> tuple[dict[str, str], dict[str, dict]]:
    try:
        languages = json.loads(snapshot.read_text(".github/data/languages.json"))
        databases = json.loads(snapshot.read_text(".github/data/databases.json"))
    except json.JSONDecodeError as exc:
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


def _example_directory(
    snapshot: GitSnapshot, language: str, driver: str, vendor: str
) -> str:
    nested = f"{language}/{driver}/{vendor}"
    if snapshot.is_dir(nested):
        return nested
    return f"{language}/{vendor}"


def discover_examples(
    snapshot: GitSnapshot,
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
            directory = _example_directory(snapshot, language, driver, vendor)
            if not snapshot.is_dir(directory):
                continue
            source = f"{directory}/{entrypoint[0]}"
            if not snapshot.is_file(source):
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
    snapshot: GitSnapshot,
    repository: str,
    commit: str,
    group: dict,
    highlight_text: tuple[str, ...],
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
        source = _strip_copyright_header(snapshot.read_text(example["source"]))
        listing = nodes.literal_block(source, source)
        listing["language"] = example["lexer"]
        listing["classes"].append("quickstart-source")
        apply_highlight_text(listing, highlight_text)
        content += listing

        relative_directory = example["directory"]
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
    option_spec = {
        "highlight-text": parse_highlight_text,
        "revision": parse_revision,
    }

    def run(self) -> list[nodes.Node]:
        driver = directives.unchanged_required(self.arguments[0]).strip().lower()
        checkout, commit = ensure_checkout(
            self.env.app, revision=self.options.get("revision")
        )
        snapshot = GitSnapshot.load(checkout, commit)
        languages, databases = _load_metadata(snapshot)
        groups = discover_examples(snapshot, driver, languages, databases)
        if not groups:
            raise self.error(f"no quickstarts found for driver {driver!r}")

        repository = self.env.config.quickstarts_repository.removesuffix(".git")
        highlight_text = self.options.get("highlight-text", ())
        multiple_vendors = len(groups) > 1
        output = nodes.container(classes=["quickstarts"])
        language_tabs = [
            _language_tabs(snapshot, repository, commit, group, highlight_text)
            for group in groups
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
    app.setup_extension("highlight_text")
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
