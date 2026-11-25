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

"""Add vendor support badges with per-driver tooltips to driver headings.

Configure tooltip text by driver slug in ``driver_vendor_support_config``.
Descriptions can be plain text or a mapping with text, link_text, and link_url.
The ``vendor-supported`` role reuses this metadata for external docs links.
"""

from html import escape

from docutils import nodes
from sphinx.application import Sphinx
from sphinx.transforms.post_transforms import SphinxPostTransform
from sphinx.util.docutils import SphinxRole

SUPPORT_ICON = """<svg class="driver-vendor-support-icon" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="4"/><path d="m4.93 4.93 4.24 4.24m5.66 5.66 4.24 4.24m-4.24-9.9 4.24-4.24m-9.9 9.9-4.24 4.24"/></svg>"""


def _badge(driver: str, tooltip: str | dict[str, str], serial: int) -> nodes.raw:
    tooltip_id = f"vendor-support-{nodes.make_id(driver)}-{serial}"
    if isinstance(tooltip, dict):
        before, label, after = tooltip["text"].partition(tooltip["link_text"])
        if not label:
            raise ValueError(f"Vendor support link text not found for {driver!r}")
        tooltip_html = (
            f'{escape(before)}<a class="reference external" '
            f'href="{escape(tooltip["link_url"], quote=True)}" '
            f'target="_blank" rel="noopener noreferrer">'
            f"{escape(label)}</a>{escape(after)}"
        )
        # Linked descriptions are interactive notes, rather than ARIA tooltips,
        # so their source links can be reached with the keyboard.
        role = "note"
    else:
        tooltip_html = escape(tooltip)
        role = "tooltip"
    html = (
        '<span class="driver-vendor-support">'
        '<button type="button" class="driver-vendor-support-badge" '
        f'aria-describedby="{tooltip_id}">'
        f"{SUPPORT_ICON}<span>Vendor-supported</span></button>"
        f'<span class="driver-vendor-support-tooltip" id="{tooltip_id}" '
        f'role="{role}">{tooltip_html}</span></span>'
    )
    return nodes.raw("", html, format="html")


class AddDriverVendorSupport(SphinxPostTransform):
    """Append the badge after the driver landing title has been styled."""

    default_priority = 10
    formats = ("html",)

    def run(self, **kwargs) -> None:
        parts = self.env.docname.split("/")
        if len(parts) < 3 or parts[0] != "drivers":
            return

        driver = parts[1]
        tooltip = self.config.driver_vendor_support_config.get(driver)
        if not tooltip:
            return

        title = next(iter(self.document.findall(nodes.title)), None)
        if title is not None:
            title += nodes.Text(" ")
            title += _badge(driver, tooltip, self.env.new_serialno("vendor-support"))


class VendorSupportedRole(SphinxRole):
    """Reuse the badge alongside links to externally hosted driver docs."""

    def run(self) -> tuple[list[nodes.Node], list[nodes.system_message]]:
        driver = self.text.strip()
        tooltip = self.config.driver_vendor_support_config.get(driver)
        if not tooltip:
            message = self.inliner.reporter.error(
                f"No vendor support tooltip configured for {driver!r}.",
                line=self.lineno,
            )
            return [], [message]

        badge = _badge(driver, tooltip, self.env.new_serialno("vendor-support"))
        self.set_source_info(badge)
        return [badge], []


def setup(app: Sphinx):
    app.add_config_value("driver_vendor_support_config", {}, "env")
    app.add_post_transform(AddDriverVendorSupport)
    app.add_role("vendor-supported", VendorSupportedRole())
    return {
        "version": "0.1.0",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
