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

"""Add site-name and breadcrumb structured data to HTML pages."""

import json
from typing import Any
from urllib.parse import urljoin

from docutils import nodes
from sphinx.application import Sphinx

SITE_NAME = "ADBC Driver Foundry"
SITE_ALTERNATE_NAMES = ["ADBC Drivers", "adbc-drivers.org"]

TOP_LEVEL_NAMES = {
    "about/index": "About",
    "blog/index": "ADBC Drivers Blog",
    "building-drivers/index": "Building ADBC Drivers",
    "drivers/index": "Available ADBC Drivers",
    "using-drivers/index": "Using ADBC Drivers",
}


def _page_url(app: Sphinx, pagename: str) -> str:
    """Return the absolute public URL for a Sphinx document."""
    return urljoin(app.config.html_baseurl, app.builder.get_target_uri(pagename))


def _page_title(app: Sphinx, pagename: str) -> str:
    """Return a document's plain-text title."""
    title = app.env.titles.get(pagename)
    return title.astext() if title is not None else pagename.rsplit("/", 1)[-1]


def _breadcrumb_pages(app: Sphinx, pagename: str) -> list[tuple[str, str]]:
    """Return the user-facing page hierarchy for a document."""
    home = ("index", SITE_NAME)

    if pagename in TOP_LEVEL_NAMES:
        return [home, (pagename, TOP_LEVEL_NAMES[pagename])]

    if pagename.startswith("blog/"):
        return [
            home,
            ("blog/index", TOP_LEVEL_NAMES["blog/index"]),
            (pagename, _page_title(app, pagename)),
        ]

    parts = pagename.split("/")
    if len(parts) == 3 and parts[0] == "drivers":
        driver_landing = f"drivers/{parts[1]}/index"
        pages = [
            home,
            ("drivers/index", TOP_LEVEL_NAMES["drivers/index"]),
            (driver_landing, _page_title(app, driver_landing)),
        ]
        if parts[2] != "index":
            # Version numbers make clearer breadcrumbs than the longer H1s on
            # version-specific documentation pages.
            leaf_name = (
                parts[2] if parts[2].startswith("v") else _page_title(app, pagename)
            )
            pages.append((pagename, leaf_name))
        return pages

    return [home, (pagename, _page_title(app, pagename))]


def _breadcrumb_data(app: Sphinx, pagename: str) -> dict[str, Any]:
    pages = _breadcrumb_pages(app, pagename)
    return {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {
                "@type": "ListItem",
                "position": position,
                "name": name,
                "item": _page_url(app, docname),
            }
            for position, (docname, name) in enumerate(pages, start=1)
        ],
    }


def configure_structured_data(
    app: Sphinx,
    pagename: str,
    templatename: str,
    context: dict[str, Any],
    doctree: nodes.document | None,
) -> None:
    """Add JSON-LD to canonical pages backed by source documents."""
    if app.builder.format != "html" or doctree is None:
        return

    if pagename == app.config.root_doc:
        data = {
            "@context": "https://schema.org",
            "@type": "WebSite",
            "name": SITE_NAME,
            "alternateName": SITE_ALTERNATE_NAMES,
            "url": _page_url(app, pagename),
        }
    elif context.get("canonical_url") == context.get("pageurl"):
        # Current version pages are copies of their driver landing pages. Their
        # canonical tags point to those landing pages, whose breadcrumb markup
        # is the version Google should use.
        data = _breadcrumb_data(app, pagename)
    else:
        return

    # Prevent a title containing "</script>" from ending the JSON-LD element.
    context["structured_data_json"] = json.dumps(
        data, ensure_ascii=False, indent=2
    ).replace("<", r"\u003c")


def setup(app: Sphinx):
    """Register the structured-data context hook."""
    # Canonical URLs and document titles are finalized by earlier hooks.
    app.connect("html-page-context", configure_structured_data, priority=900)

    return {
        "version": "0.1.0",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
