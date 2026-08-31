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

"""Generate descriptive metadata and styled headings for driver pages."""

from typing import Any

import sphinxext.opengraph as opengraph
from docutils import nodes
from sphinx.application import Sphinx
from sphinx.transforms.post_transforms import SphinxPostTransform

DRIVER_TITLE_PREFIX = "ADBC Driver for"

LANDING_PAGE_OG_TITLES = {
    "blog/index": "ADBC Drivers Blog",
    "building-drivers/index": "Building ADBC Drivers",
    "drivers/index": "Available ADBC Drivers",
    "using-drivers/index": "Using ADBC Drivers",
}


def _driver_page_parts(pagename: str) -> list[str] | None:
    """Return parts for a direct child of a driver directory."""
    # Sphinx pagenames omit the file extension. Direct children of a driver
    # directory therefore have the shape ``drivers/<driver>/<page>``.
    parts = pagename.split("/")
    if len(parts) == 3 and parts[0] == "drivers":
        return parts
    return None


def _driver_landing_title(page_title: str) -> tuple[str, str]:
    """Return the system name and complete title for a driver landing page."""
    # Guard against an upstream heading that already contains either part of
    # the generated title so a future docs pull cannot double the wording.
    system = page_title.removeprefix(f"{DRIVER_TITLE_PREFIX} ")
    system = system.removesuffix(" Driver")
    return system, f"{DRIVER_TITLE_PREFIX} {system}"


class StyleDriverLandingTitle(SphinxPostTransform):
    """Add a real, visually de-emphasized kicker to driver landing-page H1s."""

    default_priority = 5
    formats = ("html",)

    def run(self, **kwargs: Any) -> None:
        parts = _driver_page_parts(self.env.docname)
        if parts is None or parts[2] != "index":
            return

        title_node = next(iter(self.document.findall(nodes.title)), None)
        if title_node is None:
            return

        system, _ = _driver_landing_title(title_node.astext())

        # This runs after Sphinx has collected document titles and generated
        # section IDs. Consequently, navigation retains its concise label and
        # existing fragments such as ``#trino`` remain stable.
        title_node.children[:] = []
        title_node += nodes.inline(
            "", DRIVER_TITLE_PREFIX, classes=["driver-title-kicker"]
        )
        title_node += nodes.Text(" ")
        title_node += nodes.inline("", system, classes=["driver-title-system"])


def configure_titles(
    app: Sphinx,
    pagename: str,
    templatename: str,
    context: dict[str, Any],
    doctree: nodes.document | None,
) -> None:
    """Configure browser and Open Graph titles before the theme renders."""
    title = LANDING_PAGE_OG_TITLES.get(pagename)
    parts = _driver_page_parts(pagename)

    if parts is not None:
        # The rendered title can contain HTML, so parse it exactly as
        # sphinxext-opengraph does before using it as metadata text.
        page_title, _ = opengraph.get_title(context["title"])
        if parts[2] == "index":
            _, title = _driver_landing_title(page_title)

            # Unlike metadata-only overrides, changing the template context
            # also gives sphinxext-opengraph the descriptive title when it
            # generates the social-card image. Save both forms so a later hook
            # can keep the theme's visible header label concise while setting
            # its browser title independently.
            context["driver_landing_display_title"] = page_title
            context["driver_landing_browser_title"] = title
            context["title"] = title
        # Some changelog headings already contain "ADBC Driver". Checking the
        # whole title prevents turning that into "ADBC ADBC Driver".
        elif "ADBC" not in page_title and "Driver" in page_title:
            title = page_title.replace("Driver", "ADBC Driver")

    if title is None:
        return

    # Pages without source-level metadata expose this context value as None.
    if context["meta"] is None:
        context["meta"] = {}
    context["meta"]["og:title"] = title


def configure_theme_title(
    app: Sphinx,
    pagename: str,
    templatename: str,
    context: dict[str, Any],
    doctree: nodes.document | None,
) -> None:
    """Restore the concise title used in the theme's visible header."""
    display_title = context.get("driver_landing_display_title")
    page = context.get("page")
    if display_title is None or not isinstance(page, dict):
        return

    # sphinx-immaterial creates ``page`` from the descriptive context title,
    # then also shows ``page.title`` in its compact top header. The base
    # template reads the separately saved browser title for the HTML <title>.
    page["title"] = display_title


def setup(app: Sphinx):
    """Register the heading transform and title configuration hook."""
    app.add_post_transform(StyleDriverLandingTitle)

    # sphinxext-opengraph and sphinx-immaterial read this context at the
    # default priority (500), so configure their inputs first.
    app.connect("html-page-context", configure_titles, priority=400)
    # sphinx-immaterial creates ``page`` at priority 500.
    app.connect("html-page-context", configure_theme_title, priority=600)

    return {
        "version": "0.1.0",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
