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

"""Render the homepage's ABlog post list as a Sphinx Design card grid."""

from docutils import nodes
from sphinx.application import Sphinx
from sphinx.util.typing import ExtensionMetadata


_GRID_CONTAINER_CLASSES = [
    "sd-container-fluid",
    "sd-sphinx-override",
    "sd-m-0",
    "grid-no-padding",
]
_GRID_ROW_CLASSES = [
    "sd-row",
    "sd-row-cols-1",
    "sd-row-cols-xs-1",
    "sd-row-cols-sm-2",
    "sd-row-cols-md-3",
    "sd-row-cols-lg-3",
    "sd-g-2",
    "sd-g-xs-2",
    "sd-g-sm-2",
    "sd-g-md-2",
    "sd-g-lg-2",
]


def _make_card(post: nodes.list_item) -> nodes.container | None:
    """Convert one ABlog post-list item into a Sphinx Design grid column."""
    title = next(
        (
            paragraph
            for paragraph in post.findall(nodes.paragraph)
            if "ablog-post-title" in paragraph.get("classes", [])
        ),
        None,
    )
    if title is None:
        return None

    title_link = next(title.findall(nodes.reference), None)
    if title_link is None or "refuri" not in title_link:
        return None

    date_text = "".join(
        child.astext() for child in title.children if child is not title_link
    ).strip()

    header = nodes.container(classes=["sd-card-header"])
    header_text = nodes.paragraph(
        classes=["sd-card-text", "homepage-blog-post-date"]
    )
    header_text += nodes.Text(date_text)
    header += header_text

    body = nodes.container(classes=["sd-card-body"])
    body_text = nodes.paragraph(classes=["sd-card-text"])
    body_text += nodes.strong("", title_link.astext())
    body += body_text

    footer = nodes.container(classes=["sd-card-footer"])
    footer_text = nodes.paragraph(classes=["sd-card-text"])
    read_more = nodes.reference(
        "",
        "",
        refuri=title_link["refuri"],
        classes=[
            "sd-sphinx-override",
            "sd-btn",
            "sd-text-wrap",
            "sd-stretched-link",
        ],
    )
    if title_link.get("internal"):
        read_more["internal"] = True
    read_more += nodes.inline("", "Read more", classes=["doc"])
    footer_text += read_more
    footer += footer_text

    card = nodes.container(
        classes=[
            "sd-card",
            "sd-sphinx-override",
            "sd-w-100",
            "sd-shadow-sm",
        ]
    )
    card += header
    card += body
    card += footer

    column = nodes.container(classes=["sd-col", "sd-d-flex-row"])
    column += card
    return column


def _render_card_grid(app: Sphinx, doctree: nodes.document, docname: str) -> None:
    """Replace ABlog's expanded homepage postlist with a card grid."""
    if app.builder.format != "html" or docname != "index":
        return

    for container in doctree.findall(nodes.container):
        if "homepage-blog-posts" not in container.get("classes", []):
            continue

        for postlist in container.findall(nodes.bullet_list):
            if "postlist" not in postlist.get("classes", []):
                continue

            row = nodes.container(classes=_GRID_ROW_CLASSES)
            for post in postlist.children:
                if not isinstance(post, nodes.list_item):
                    continue
                card = _make_card(post)
                if card is not None:
                    row += card

            if row.children:
                grid = nodes.container(classes=_GRID_CONTAINER_CLASSES)
                grid += row
                postlist.replace_self(grid)


def setup(app: Sphinx) -> ExtensionMetadata:
    # ABlog expands its PostList nodes at the default priority (500).
    app.connect("doctree-resolved", _render_card_grid, priority=750)
    return {
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
