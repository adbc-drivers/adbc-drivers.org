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

"""Define inline self-links that can also be referenced with the ref role."""

from docutils import nodes
from sphinx.application import Sphinx
from sphinx.util.docutils import ReferenceRole
from sphinx.util.typing import ExtensionMetadata


class AnchorRole(ReferenceRole):
    """Create an inline target from ``text <label>`` or just ``label``."""

    def run(self) -> tuple[list[nodes.Node], list[nodes.system_message]]:
        title = self.title.strip()
        target = nodes.fully_normalize_name(self.target)
        if not title or not target:
            message = self.inliner.reporter.error(
                "The anchor role requires nonempty text and a label.",
                line=self.lineno,
            )
            problematic = self.inliner.problematic(self.rawtext, self.rawtext, message)
            return [problematic], [message]

        node = nodes.reference(self.rawtext, title, **self.options)
        node["internal"] = True
        node["inline_anchor"] = True
        node["names"] = [target]
        self.set_source_info(node)
        self.inliner.document.note_explicit_target(node)
        node["refid"] = node["ids"][0]
        return [node], []


def _register_anchor_captions(app: Sphinx, doctree: nodes.document) -> None:
    """Give inline labels captions after Sphinx has collected their targets."""
    domain = app.env.domains.standard_domain
    for node in doctree.findall(nodes.reference):
        if not node.get("inline_anchor"):
            continue
        for name in node["names"]:
            # Docutils removes duplicate explicit names from the node, so only
            # valid targets get a caption. The standard domain owns label
            # cleanup on reread, parallel merging, and cross-page resolution.
            domain.labels[name] = (app.env.docname, node["ids"][0], node.astext())


def setup(app: Sphinx) -> ExtensionMetadata:
    app.add_role("anchor", AnchorRole())
    app.connect("doctree-read", _register_anchor_captions)
    return {
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
