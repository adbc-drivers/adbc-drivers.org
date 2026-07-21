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

"""Build dated posts beneath /blog and retain their legacy root URLs."""

import html
import json
import re
from pathlib import Path
from urllib.parse import quote, urljoin, urlsplit, urlunsplit
from xml.etree import ElementTree

from sphinx.application import Sphinx
from sphinx.builders.html import StandaloneHTMLBuilder
from sphinx.util.typing import ExtensionMetadata


_BLOG_POST_DOCUMENT = re.compile(
    r"^blog/(?P<dated_path>\d{4}/\d{2}/\d{2}/[^/]+)$"
)
_BLOG_POST_HTML_PATH = re.compile(
    r"^(?P<post>/blog/\d{4}/\d{2}/\d{2}/[^/]+)\.html$"
)
_BLOG_ARCHIVE_YEAR = re.compile(r"^\d{4}$")
_LEGACY_POST_LASTMOD_THROUGH = (2026, 7)


def _is_blog_post(docname: str) -> bool:
    return _BLOG_POST_DOCUMENT.fullmatch(docname) is not None


def _is_suppressed_blog_page(pagename: str, blog_path: str) -> bool:
    relative_name = pagename.removeprefix(f"{blog_path}/")
    return (
        pagename
        in {
            f"{blog_path}/archive",
            f"{blog_path}/author",
            f"{blog_path}/drafts",
        }
        or pagename.startswith(f"{blog_path}/author/")
        or (
            relative_name != pagename
            and _BLOG_ARCHIVE_YEAR.fullmatch(relative_name) is not None
        )
    )


class SelectiveHTMLBuilder(StandaloneHTMLBuilder):
    """Use directory-style output for blog posts and standard HTML elsewhere."""

    name = "foundryhtml"

    def get_target_uri(self, docname: str, typ: str | None = None) -> str:
        if _is_blog_post(docname):
            return quote(docname) + "/"
        return super().get_target_uri(docname, typ)

    def get_output_path(self, page_name: str, /) -> Path:
        if _is_blog_post(page_name):
            return Path(
                self.outdir,
                *page_name.split("/"),
                f"index{self.out_suffix}",
            )
        return super().get_output_path(page_name)

    def gen_pages_from_extensions(self) -> None:
        """Render extension pages except ABlog's unused archive indexes."""
        blog_path = self.config.blog_path.rstrip("/")
        for pagelist in self.events.emit("html-collect-pages"):
            for pagename, context, template in pagelist:
                if _is_suppressed_blog_page(pagename, blog_path):
                    continue
                self.handle_page(pagename, context, template)


def _write_legacy_blog_redirects(app: Sphinx, exception: Exception | None) -> None:
    if exception is not None or app.builder.name != SelectiveHTMLBuilder.name:
        return

    baseurl = app.config.html_baseurl.rstrip("/") + "/"
    for docname in sorted(app.env.found_docs):
        match = _BLOG_POST_DOCUMENT.fullmatch(docname)
        if match is None:
            continue

        canonical_url = urljoin(baseurl, app.builder.get_target_uri(docname))
        escaped_canonical = html.escape(canonical_url, quote=True)
        script_destination = json.dumps(canonical_url)
        redirect = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="robots" content="noindex">
  <title>Redirecting…</title>
  <link rel="canonical" href="{escaped_canonical}">
  <meta http-equiv="refresh" content="0; url={escaped_canonical}">
</head>
<body>
  <p>Redirecting to <a href="{escaped_canonical}">{escaped_canonical}</a>.</p>
  <script>
    const destination = new URL({script_destination}, window.location.href);
    destination.search = window.location.search;
    destination.hash = window.location.hash;
    window.location.replace(destination.href);
  </script>
</body>
</html>
"""
        dated_path = match.group("dated_path")
        legacy_paths = (
            Path(app.outdir, f"{dated_path}.html"),
            Path(app.outdir, *dated_path.split("/"), "index.html"),
        )
        for legacy_path in legacy_paths:
            legacy_path.parent.mkdir(parents=True, exist_ok=True)
            legacy_path.write_text(redirect, encoding="utf-8")


def _clean_sitemap_location(location: str) -> str:
    parsed = urlsplit(location)
    path = parsed.path

    if path == "/index.html":
        path = "/"
    elif path.endswith("/index.html"):
        path = path[: -len("index.html")]
    elif match := _BLOG_POST_HTML_PATH.fullmatch(path):
        path = match.group("post") + "/"
    else:
        return location

    return urlunsplit(parsed._replace(path=path))


def _clean_sitemap_urls(app: Sphinx, exception: Exception | None) -> None:
    if exception is not None or app.builder.name != SelectiveHTMLBuilder.name:
        return

    sitemap_path = Path(app.outdir, app.config.sitemap_filename)
    if not sitemap_path.exists():
        return

    tree = ElementTree.parse(sitemap_path)
    root = tree.getroot()
    namespace = "http://www.sitemaps.org/schemas/sitemap/0.9"
    url_tag = f"{{{namespace}}}url"
    loc_tag = f"{{{namespace}}}loc"
    lastmod_tag = f"{{{namespace}}}lastmod"

    from ablog.blog import Blog

    baseurl = app.config.html_baseurl.rstrip("/") + "/"
    post_dates = {
        urljoin(baseurl, app.builder.get_target_uri(post.docname)): post.date.strftime(
            "%Y-%m-%dT00:00:00Z"
        )
        for post in Blog(app).posts
        if (post.date.year, post.date.month) <= _LEGACY_POST_LASTMOD_THROUGH
    }

    changed = False
    for url in root.iter(url_tag):
        location = url.find(loc_tag)
        if location is None or location.text is None:
            continue
        cleaned = _clean_sitemap_location(location.text)
        if cleaned != location.text:
            location.text = cleaned
            changed = True

        if post_date := post_dates.get(cleaned):
            lastmod = url.find(lastmod_tag)
            if lastmod is None:
                lastmod = ElementTree.SubElement(url, lastmod_tag)
            if lastmod.text != post_date:
                lastmod.text = post_date
                changed = True

    if changed:
        ElementTree.register_namespace("", namespace)
        tree.write(
            sitemap_path,
            xml_declaration=True,
            encoding="utf-8",
            method="xml",
        )


def setup(app: Sphinx) -> ExtensionMetadata:
    app.add_builder(SelectiveHTMLBuilder)
    app.connect("build-finished", _write_legacy_blog_redirects, priority=900)
    app.connect("build-finished", _clean_sitemap_urls, priority=900)
    return {
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
