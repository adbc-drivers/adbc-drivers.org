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

"""Render cached ADBC quickstart examples and their source listings."""

from __future__ import annotations

import json
import shutil
import subprocess
import tempfile
import time
from html import escape
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


def _source_pagename(driver: str, vendor: str, language: str) -> str:
    return f"drivers/{driver}/quickstarts/{vendor}/{language}"


def _language_grid(
    directive: "QuickstartsDirective",
    driver: str,
    vendor: str,
    examples: list[dict],
) -> nodes.container:
    grid = create_component(
        "grid-container",
        ["sd-container-fluid", "sd-sphinx-override", "sd-mb-4", "grid-no-padding"],
    )
    row = create_component(
        "grid-row",
        [
            "sd-row",
            "sd-row-cols-1",
            "sd-row-cols-xs-2",
            "sd-row-cols-sm-3",
            "sd-row-cols-md-4",
            "sd-row-cols-lg-4",
            "sd-g-2",
        ],
    )
    grid += row
    for example in examples:
        pagename = _source_pagename(driver, vendor, example["language"])
        uri = directive.env.app.builder.get_relative_uri(
            directive.env.docname, pagename
        )
        link = nodes.reference(
            "",
            "",
            nodes.strong("", example["language_name"]),
            refuri=uri,
            classes=["sd-stretched-link"],
            internal=True,
        )
        body = create_component("card-body", ["sd-card-body", "sd-card-center"])
        body += nodes.paragraph("", "", link, classes=["sd-card-text"])
        card = create_component(
            "card",
            [
                "sd-card",
                "sd-sphinx-override",
                "sd-w-100",
                "sd-shadow-sm",
                "sd-card-hover",
            ],
        )
        card += body
        column = create_component("grid-item", ["sd-col", "sd-d-flex-column"])
        column += card
        row += column
    return grid


def _tab_set(
    driver: str, groups: list[dict], grids: list[nodes.Node]
) -> nodes.container:
    tabs = create_component("tab-set", classes=["sd-tab-set"])
    for group, grid in zip(groups, grids, strict=True):
        item = create_component(
            "tab-item",
            classes=["sd-tab-item"],
            selected=group["vendor"] == driver,
        )
        item += nodes.rubric(
            group["vendor_name"],
            group["vendor_name"],
            classes=["sd-tab-label"],
        )
        content = create_component(
            "tab-content",
            classes=["sd-tab-content"],
        )
        content += grid
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

        pages = getattr(self.env, "quickstarts_pages", {})
        repository = self.env.config.quickstarts_repository.removesuffix(".git")
        multiple_vendors = len(groups) > 1
        output = nodes.container(classes=["quickstarts"])
        grids = [
            _language_grid(self, driver, group["vendor"], group["examples"])
            for group in groups
        ]
        if multiple_vendors:
            output += _tab_set(driver, groups, grids)
        else:
            output += grids[0]
        for group in groups:
            for example in group["examples"]:
                relative_directory = (
                    example["directory"].relative_to(checkout).as_posix()
                )
                pagename = _source_pagename(
                    driver, group["vendor"], example["language"]
                )
                driver_name = databases[driver]["name"]
                if group["vendor"] == driver:
                    title = (
                        f"{example['language_name']} quickstart with the ADBC driver "
                        f"for {driver_name}"
                    )
                else:
                    title = (
                        f"{example['language_name']} quickstart for "
                        f"{group['vendor_name']} with the ADBC driver for {driver_name}"
                    )
                description = (
                    f"This example shows how to use the ADBC driver for {driver_name} "
                    f"in {example['language_name']}"
                )
                if group["vendor"] != driver:
                    description += f" with {group['vendor_name']}"
                pages[pagename] = {
                    "docname": self.env.docname,
                    "title": title,
                    "description": description + ".",
                    "source": example["source"].read_text(encoding="utf-8"),
                    "lexer": example["lexer"],
                    "github_url": (
                        f"{repository}/tree/{quote(commit, safe='')}/"
                        f"{quote(relative_directory, safe='/')}"
                    ),
                }
        self.env.quickstarts_pages = pages

        footer = nodes.paragraph()
        footer += nodes.Text("…and more languages are supported! Find an ")
        footer += nodes.reference(
            "",
            "ADBC client library",
            refuri=CLIENT_LIBRARIES_URL,
        )
        footer += nodes.Text(" for your language.")
        output += footer
        return [output]


def _collect_source_pages(app: Sphinx):
    if app.builder.format != "html":
        return
    for pagename, page in sorted(getattr(app.env, "quickstarts_pages", {}).items()):
        title = escape(page["title"])
        highlighted = app.builder.highlighter.highlight_block(
            page["source"], page["lexer"], location=pagename
        )
        github_link = nodes.paragraph()
        introduction = nodes.paragraph("", page["description"])
        github_link += nodes.reference(
            "",
            "View the full example on GitHub",
            refuri=page["github_url"],
        )
        github_link += nodes.Text(".")
        prose = nodes.container("", introduction, github_link)
        prose_html = app.builder.render_partial(prose)["fragment"]
        body = f"<h1>{title}</h1>{prose_html}{highlighted}"
        yield pagename, {"title": title, "body": body}, "page.html"


def _purge_pages(app: Sphinx, env, docname: str) -> None:
    pages = getattr(env, "quickstarts_pages", {})
    env.quickstarts_pages = {
        pagename: page
        for pagename, page in pages.items()
        if page.get("docname") != docname
    }


def setup(app: Sphinx) -> ExtensionMetadata:
    app.add_config_value(
        "quickstarts_repository",
        "https://github.com/columnar-tech/adbc-quickstarts.git",
        "env",
    )
    app.add_config_value("quickstarts_ref", "main", "env")
    app.add_config_value("quickstarts_cache_ttl", 3600, "env", types={int})
    app.add_directive("quickstarts", QuickstartsDirective)
    app.connect("html-collect-pages", _collect_source_pages)
    app.connect("env-purge-doc", _purge_pages)
    return {
        "version": "0.1.0",
        "parallel_read_safe": False,
        "parallel_write_safe": True,
    }
