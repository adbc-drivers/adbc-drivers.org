# Copyright (c) 2025 ADBC Drivers Contributors
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

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import locale
import shutil
import sys
from html import escape as escape_html
from pathlib import Path
from urllib.parse import urlparse

from docutils import nodes
from sphinx.writers.html import HTMLTranslator
from sphinx_design.icons import get_octicon

# ABlog formats month names with ``datetime.strftime``, which otherwise uses
# the locale of the machine running the build. Keep the English-language site
# output deterministic while leaving every other locale category untouched.
locale.setlocale(locale.LC_TIME, "C")

# Add _ext directory to Python path for custom extensions
sys.path.insert(0, str(Path(__file__).parent / "_ext"))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "ADBC Driver Foundry"
copyright = "2025-2026 ADBC Drivers Contributors"
author = "ADBC Drivers Contributors"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "ablog",
    "homepage_blog_cards",
    "myst_parser",
    "sphinx_copybutton",
    "sphinx_design",
    "external_nav_links",
    "selective_html",
    "sphinx_immaterial",
    "sphinx.ext.intersphinx",
    "sphinx_sitemap",
    "sphinxext.opengraph",
    "driver_header_links",
]

templates_path = ["_templates"]
exclude_patterns = [
    ".worktrees",
    "_build",
    "Thumbs.db",
    ".DS_Store",
    "venv",
    ".venv",
    ".pixi",
    ".git",
    "generated",
    "README.md",
    "CONTRIBUTING.md",
]
suppress_warnings = ["myst.header"]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_css_files = ["custom.css"]
html_extra_path = ["robots.txt", "CNAME"]
html_logo = "_static/adbc-drivers-logo.png"
html_favicon = "_static/favicon.ico"
html_static_path = ["_static"]
html_theme = "sphinx_immaterial"
html_title = "ADBC Driver Foundry"
html_baseurl = "https://adbc-drivers.org/"
# Render links to index documents as their containing directory. The
# selective_html builder applies the same clean-URL treatment to blog posts.
html_use_directory_uris_for_index_pages = True
html_theme_options = {
    "features": [
        "navigation.tabs",
    ],
    "font": {
        "text": "IBM Plex Sans",
        "code": "IBM Plex Mono",
    },
    "palette": [
        {
            "media": "(prefers-color-scheme)",
            "primary": "black",
            "accent": "light-blue",
            "scheme": "default",
            "toggle": {
                "icon": "material/theme-light-dark",
                "name": "Switch to light mode",
            },
        },
        {
            "media": "(prefers-color-scheme: light)",
            "primary": "black",
            "accent": "light-blue",
            "scheme": "default",
            "toggle": {
                "icon": "material/weather-sunny",
                "name": "Switch to dark mode",
            },
        },
        {
            "media": "(prefers-color-scheme: dark)",
            "primary": "black",
            "accent": "light-blue",
            "scheme": "slate",
            "toggle": {
                "icon": "material/weather-night",
                "name": "Switch to system preference",
            },
        },
    ],
    "social": [],
    "toc_title": "Contents",
    "repo_url": "https://github.com/adbc-drivers",
    "repo_name": "adbc-drivers",
    "icon": {"repo": "fontawesome/brands/github"},
}

# Copy only entered commands from console transcripts, without their prompts.
copybutton_prompt_text = r"(?:\$|#|>) "
copybutton_prompt_is_regexp = True
copybutton_only_copy_prompt_lines = True
copybutton_remove_prompts = True

# -- Options for Intersphinx -------------------------------------------------

intersphinx_mapping = {
    "arrow": ("https://arrow.apache.org/docs/", None),
    "adbc": ("https://arrow.apache.org/adbc/current/", None),
    "python": ("https://docs.python.org/3", None),
}

# -- Options for MyST --------------------------------------------------------

myst_enable_extensions = [
    "attrs_block",
    "attrs_inline",
    "colon_fence",
    "deflist",
    "linkify",
    "substitution",
]
myst_heading_anchors = 3
myst_update_mathjax = False
myst_substitutions = {
    "BREAKING_CHANGE": "({octicon}`alert-fill;1em;sd-text-warning` **Breaking change**)"
}

# -- Options for OpenGraph ---------------------------------------------------

ogp_description_length = 400
ogp_site_url = "https://adbc-drivers.org"
ogp_site_name = "ADBC Driver Foundry"
ogp_social_cards = {
    "image": "_static/opengraph-logo.png",
    "line_color": "#434343",
}

# -- Options for sphinx-sitemap ----------------------------------------------

# sphinx-sitemap defaults to "{lang}{version}{link}" but we don't need {lang} or
# {version}
sitemap_url_scheme = "{link}"
# Exclude utility and duplicate indexes. ABlog generates these pages to support
# its archive widgets, but they are not useful search-engine landing pages.
sitemap_excludes = [
    "genindex.html",
    "blog.html",
    "blog/archive.html",
    "blog/author.html",
    "blog/author/*.html",
    "blog/drafts.html",
    "blog/[0-9][0-9][0-9][0-9].html",
]
sitemap_show_lastmod = True

# -- Options for ABlog -------------------------------------------------------

blog_path = "blog"
blog_baseurl = html_baseurl.rstrip("/")
blog_title = "ADBC Driver Foundry Blog"
blog_feed_subtitle = "News and releases from the ADBC Driver Foundry"
blog_feed_fulltext = True
blog_authors = {
    "ADBC Drivers Contributors": (
        "ADBC Drivers Contributors",
        "https://github.com/adbc-drivers",
    ),
}
blog_default_author = "ADBC Drivers Contributors"
post_date_format = "%B %d, %Y"
post_date_format_short = "%B %d"
post_show_prev_next = True
BLOG_SIDEBAR_POST_COUNT = 5

# -- Customization -----------------------------------------------------------

# Custom shields.io style badges. See custom.css for corresponding css.
custom_badge_variants = ["primary", "secondary", "success", "warning", "danger", "info"]

# -- Driver Header Links Extension Configuration -----------------------------

# Maps driver names to lists of link dicts with 'url' and optional 'label' keys.
# GitHub URLs automatically display an icon (label used for accessibility).
# Non-GitHub URLs display the label text (defaults to "Link" if not specified).
driver_header_links_config = {
    "bigquery": [
        {"url": "https://github.com/adbc-drivers/bigquery", "label": "GitHub"},
    ],
    "clickhouse": [
        {"url": "https://github.com/ClickHouse/adbc_clickhouse", "label": "GitHub"},
    ],
    "databricks": [
        {"url": "https://github.com/adbc-drivers/databricks", "label": "GitHub"},
    ],
    "datafusion": [
        {"url": "https://github.com/adbc-drivers/datafusion", "label": "GitHub"},
    ],
    "exasol": [
        {"url": "https://github.com/adbc-drivers/exasol", "label": "GitHub"},
    ],
    "mssql": [
        {"url": "https://github.com/adbc-drivers/mssql", "label": "GitHub"},
    ],
    "mysql": [
        {"url": "https://github.com/adbc-drivers/mysql", "label": "GitHub"},
    ],
    "quack": [
        {"url": "https://github.com/adbc-drivers/quack", "label": "GitHub"},
    ],
    "redshift": [
        {"url": "https://github.com/adbc-drivers/redshift", "label": "GitHub"},
    ],
    "singlestore": [
        {
            "url": "https://github.com/singlestore-labs/singlestore-adbc-connector",
            "label": "GitHub",
        },
    ],
    "snowflake": [
        {"url": "https://github.com/adbc-drivers/snowflake", "label": "GitHub"},
    ],
    "spark": [
        {"url": "https://github.com/adbc-drivers/spark", "label": "GitHub"},
    ],
    "trino": [
        {"url": "https://github.com/adbc-drivers/trino", "label": "GitHub"},
    ],
}


def badge_role(name, rawtext, text, lineno, inliner, options={}, content=[]):
    """
    Custom badge role that creates shields.io-style badges with one or two
    parts.

    Variants include: primary, secondary, success, warning, danger, info

    Examples:

    - {badge-primary}`Hello World`
    - {badge-secondary}`Driver Version|v0.1.0`

    To use URLs or refs, wrap the badge up in `[]()`:

    - [{badge-primary}`Website|example.com`](http://example.com)
    - [{badge-primary}`Permalink`](#driver-mysql-v0.1.0)

    """
    from html import escape

    variant = name.split("-", 1)[-1] if "-" in name else "primary"
    parts = [p.strip() for p in text.split("|")]

    label = ""
    value = ""
    if len(parts) == 1:
        value = parts[0]
    elif len(parts) >= 2:
        label = parts[0]
        value = parts[1]

    label = escape(label)
    value = escape(value)

    if label:
        html = f"""<span class="custom-badge custom-badge-{variant}">
            <span class="custom-badge-label">{label}</span>
            <span class="custom-badge-value">{value}</span>
        </span>"""
    else:
        html = f"""<span class="custom-badge custom-badge-{variant}">
            <span class="custom-badge-value">{value}</span>
        </span>"""

    node = nodes.raw("", html, format="html")
    return [node], []


class ExternalLinkHtmlTranslator(HTMLTranslator):
    _external_icon = " " + get_octicon("link-external")

    def visit_reference(self, node):
        same_site = urlparse(node.get("refuri", "")).hostname in {
            "adbc-drivers.org",
            "www.adbc-drivers.org",
        }
        if node.get("newtab") or not (
            node.get("target")
            or node.get("internal")
            or same_site
            or "refuri" not in node
        ):
            node["target"] = "_blank"
        super().visit_reference(node)

    def depart_reference(self, node):
        if node.get("target") == "_blank":
            self.body.append(self._external_icon)
        super().depart_reference(node)


def setup(app):
    app.set_translator("html", ExternalLinkHtmlTranslator)
    app.set_translator("foundryhtml", ExternalLinkHtmlTranslator)

    # sphinx-immaterial omits this legacy Sphinx global, but
    # sphinx-copybutton 0.5.2 still reads it during startup.
    app.add_js_file(
        None,
        body='window.DOCUMENTATION_OPTIONS = {URL_ROOT: ""};',
        priority=400,
    )

    # Register custom badge roles with Sphinx
    for variant in custom_badge_variants:
        role_name = f"badge-{variant}"
        app.add_role(role_name, badge_role)

    # Remove last_updated dates from pages.
    #
    # When we added sphinx-sitemap last modified dates started showing up at the
    # bottom of every page. sphinx-sitemap uses sphinx-last-updated-by-git which
    # turns on `html_last_updated_fmt and ignores what the user has set so we
    # have to put a hook in to force it back to None at this phase of the build.
    def reset_last_updated_fmt(app):
        app.config.html_last_updated_fmt = None

    app.connect("builder-inited", reset_last_updated_fmt)

    # With top-level navigation rendered as tabs, the left sidebar is useful
    # only when the active section has child pages. Hide it for leaf sections,
    # orphaned blog posts, and generated pages that are outside the toctree.
    def configure_section_navigation(app, pagename, templatename, context, doctree):
        blog = context.get("ablog")
        blog_path = getattr(blog, "blog_path", "blog")
        show_blog_sidebar = blog is not None and (
            pagename in blog
            or pagename == blog_path
            or pagename.startswith(f"{blog_path}/")
        )
        context["show_blog_sidebar"] = show_blog_sidebar
        context["blog_sidebar_post_count"] = BLOG_SIDEBAR_POST_COUNT

        page = context.get("page")
        navigation = context.get("nav")

        if not isinstance(page, dict) or navigation is None:
            return

        if show_blog_sidebar:
            return

        has_subpages = any(item.active and item.children for item in navigation)
        if has_subpages:
            return

        hidden = page.setdefault("meta", {}).setdefault("hide", [])
        if "navigation" not in hidden:
            hidden.append("navigation")

    # sphinx-immaterial creates `page` and `nav` at the default priority, so
    # run this afterward.
    app.connect("html-page-context", configure_section_navigation, priority=900)

    # Jekyll published the original blog feed at /feed.xml. ABlog publishes
    # the canonical feed at /blog/atom.xml, and a Cloudflare Redirect Rule
    # redirects the old endpoint to it. Retain a byte-for-byte copy at the old
    # endpoint as a backup. External-link icons are useful in the site UI, but
    # add noisy inline SVG markup to feed readers, so remove them before making
    # the backup copy.
    def finalize_blog_feeds(app, exception):
        if exception is not None or app.builder.format != "html":
            return

        source = Path(app.outdir) / "blog" / "atom.xml"
        if source.exists():
            feed = source.read_text(encoding="utf-8")
            external_icon = escape_html(
                ExternalLinkHtmlTranslator._external_icon, quote=False
            )
            feed = feed.replace(external_icon, "")
            source.write_text(feed, encoding="utf-8")
            shutil.copyfile(source, Path(app.outdir) / "feed.xml")

    app.connect("build-finished", finalize_blog_feeds)
