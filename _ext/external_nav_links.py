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

"""Add external-link behavior to generated navigation markup."""

import re
from html import escape, unescape
from pathlib import Path
from urllib.parse import urlparse

from sphinx.application import Sphinx
from sphinx.util.typing import ExtensionMetadata
from sphinx_design.icons import get_octicon


_ANCHOR = re.compile(
    r"<a\b(?P<attributes>[^>]*)>(?P<body>.*?)</a>",
    flags=re.IGNORECASE | re.DOTALL,
)
_EXTERNAL_ICON = get_octicon(
    "link-external",
    height="0.65rem",
    classes=("external-nav-icon",),
)


def _find_attribute(attributes: str, name: str) -> re.Match[str] | None:
    return re.search(
        rf"\b{re.escape(name)}\s*=\s*(?P<quote>[\"'])(?P<value>.*?)(?P=quote)",
        attributes,
        flags=re.IGNORECASE | re.DOTALL,
    )


def _get_attribute(attributes: str, name: str) -> str | None:
    match = _find_attribute(attributes, name)
    return unescape(match.group("value")) if match else None


def _set_attribute(attributes: str, name: str, value: str) -> str:
    match = _find_attribute(attributes, name)
    escaped_value = escape(value, quote=True)
    if match is None:
        return f'{attributes} {name}="{escaped_value}"'

    start, end = match.span("value")
    return attributes[:start] + escaped_value + attributes[end:]


def _rewrite_nav_anchor(match: re.Match[str], site_origin: tuple[str, str]) -> str:
    attributes = match.group("attributes")
    classes = (_get_attribute(attributes, "class") or "").split()
    if "md-nav__link" not in classes:
        return match.group(0)

    destination = urlparse(_get_attribute(attributes, "href") or "")
    if destination.scheme not in {"http", "https"} or (
        destination.scheme,
        destination.netloc,
    ) == site_origin:
        return match.group(0)

    attributes = _set_attribute(attributes, "target", "_blank")
    attributes = _set_attribute(attributes, "rel", "noopener noreferrer")
    body = match.group("body")
    if "sd-octicon-link-external" not in body:
        body += _EXTERNAL_ICON
    return f"<a{attributes}>{body}</a>"


def _rewrite_external_nav_links(app: Sphinx, exception: Exception | None) -> None:
    if exception is not None or app.builder.format != "html":
        return

    site = urlparse(app.config.html_baseurl)
    site_origin = (site.scheme, site.netloc)
    encoding = app.config.html_output_encoding
    for output in Path(app.outdir).rglob("*.html"):
        source = output.read_text(encoding=encoding)
        if "md-nav__link" not in source:
            continue
        rewritten = _ANCHOR.sub(
            lambda match: _rewrite_nav_anchor(match, site_origin), source
        )
        if rewritten != source:
            output.write_text(rewritten, encoding=encoding)


def setup(app: Sphinx) -> ExtensionMetadata:
    app.connect("build-finished", _rewrite_external_nav_links, priority=950)
    return {
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
