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

import sys
from pathlib import Path

from docutils import nodes
from sphinx.writers.html import HTMLTranslator

# Add _ext directory to Python path for custom extensions
sys.path.insert(0, str(Path(__file__).parent / "_ext"))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "ADBC Driver Foundry Documentation"
copyright = "2025-2026 ADBC Drivers Contributors"
author = "ADBC Drivers Contributors"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "myst_parser",
    "sphinx_design",
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
html_extra_path = ["robots.txt"]
html_logo = "_static/adbc-drivers-logo.png"
html_favicon = "_static/favicon.ico"
html_static_path = ["_static"]
html_theme = "sphinx_immaterial"
html_title = "ADBC Driver Foundry Documentation"
html_baseurl = "https://docs.adbc-drivers.org/"
html_theme_options = {
    "features": [
        "content.code.copy",
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
myst_substitutions = {
    "BREAKING_CHANGE": "({octicon}`alert-fill;1em;sd-text-warning` **Breaking change**)"
}

# -- Options for OpenGraph ---------------------------------------------------

ogp_description_length = 400
ogp_site_url = "https://docs.adbc-drivers.org"
ogp_site_name = "ADBC Driver Foundry Documentation"
ogp_social_cards = {
    "image": "_static/opengraph-logo.png",
    "line_color": "#434343",
}

# -- Options for sphinx-sitemap ----------------------------------------------

# sphinx-sitemap defaults to "{lang}{version}{link}" but we don't need {lang} or
# {version}
sitemap_url_scheme = "{link}"
# We don't need this index in the sitemap and if we don't exclude it sitemap
# generation breaks for some reason
sitemap_excludes = ["genindex.html"]
sitemap_show_lastmod = True

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
        {"url": "https://github.com/adbc-drivers/singlestore", "label": "GitHub"},
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
    _external_icon = """ <svg version="1.1" width="1.0em" height="1.0em" class="sd-octicon sd-octicon-link-external" viewBox="0 0 16 16" aria-hidden="true"><path d="M3.75 2h3.5a.75.75 0 0 1 0 1.5h-3.5a.25.25 0 0 0-.25.25v8.5c0 .138.112.25.25.25h8.5a.25.25 0 0 0 .25-.25v-3.5a.75.75 0 0 1 1.5 0v3.5A1.75 1.75 0 0 1 12.25 14h-8.5A1.75 1.75 0 0 1 2 12.25v-8.5C2 2.784 2.784 2 3.75 2Zm6.854-1h4.146a.25.25 0 0 1 .25.25v4.146a.25.25 0 0 1-.427.177L13.03 4.03 9.28 7.78a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042l3.75-3.75-1.543-1.543A.25.25 0 0 1 10.604 1Z"></path></svg>"""

    def visit_reference(self, node):
        if node.get("newtab") or not (
            node.get("target") or node.get("internal") or "refuri" not in node
        ):
            node["target"] = "_blank"
        super().visit_reference(node)

    def depart_reference(self, node):
        if node.get("target") == "_blank":
            self.body.append(self._external_icon)
        super().depart_reference(node)


def setup(app):
    app.set_translator("html", ExternalLinkHtmlTranslator)

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
