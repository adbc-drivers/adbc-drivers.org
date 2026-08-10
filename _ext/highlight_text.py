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

"""Highlight selected substrings in Sphinx ``code-block`` directives."""

from __future__ import annotations

import copy
import csv
import re
from collections.abc import Iterable, Iterator
from typing import Any

from docutils import nodes
from docutils.parsers.rst import directives
from pygments.filter import Filter
from pygments.formatters import HtmlFormatter
from pygments.lexer import Lexer
from pygments.token import _TokenType
from sphinx.application import Sphinx
from sphinx.directives.code import CodeBlock
from sphinx.highlighting import PygmentsBridge
from sphinx.util.typing import ExtensionMetadata

_HIGHLIGHT_OPTION = "highlight-text"
_HIGHLIGHT_ARGUMENT = "highlight_text"
_HIGHLIGHT_TOKEN = "HighlightText"

TokenStream = Iterable[tuple[_TokenType, str]]


def parse_highlight_text(argument: str) -> tuple[str, ...]:
    """Parse a comma-separated list of literal substrings."""
    try:
        values = next(csv.reader([argument], skipinitialspace=True, strict=True))
    except csv.Error as exc:
        raise ValueError(f"invalid highlight-text value: {exc}") from exc

    return tuple(dict.fromkeys(value.strip() for value in values if value.strip()))


def _match_pattern(values: Iterable[str]) -> re.Pattern[str] | None:
    unique_values = tuple(dict.fromkeys(values))
    if not unique_values:
        return None

    # Prefer the complete value when one configured substring prefixes another.
    ordered_values = sorted(unique_values, key=lambda value: (-len(value), value))
    return re.compile("|".join(re.escape(value) for value in ordered_values))


class HighlightTextFilter(Filter):
    """Mark exact substring matches without discarding syntax token types."""

    def __init__(self, *, highlight_text: Iterable[str]) -> None:
        super().__init__()
        self.pattern = _match_pattern(highlight_text)

    def filter(
        self, lexer: Lexer, stream: TokenStream
    ) -> Iterator[tuple[_TokenType, str]]:
        tokens = list(stream)
        if self.pattern is None:
            yield from tokens
            return

        source = "".join(value for _, value in tokens)
        matches = [(match.start(), match.end()) for match in self.pattern.finditer(source)]
        if not matches:
            yield from tokens
            return

        offset = 0
        match_index = 0
        for token_type, value in tokens:
            token_end = offset + len(value)
            while match_index < len(matches) and matches[match_index][1] <= offset:
                match_index += 1

            boundaries = {offset, token_end}
            index = match_index
            while index < len(matches) and matches[index][0] < token_end:
                start, end = matches[index]
                boundaries.add(max(offset, start))
                boundaries.add(min(token_end, end))
                index += 1

            ordered_boundaries = sorted(boundaries)
            for start, end in zip(ordered_boundaries, ordered_boundaries[1:]):
                if start == end:
                    continue
                highlighted = any(
                    match_start < end and match_end > start
                    for match_start, match_end in matches[match_index:index]
                )
                segment_type = (
                    getattr(token_type, _HIGHLIGHT_TOKEN)
                    if highlighted
                    else token_type
                )
                yield segment_type, value[start - offset : end - offset]

            offset = token_end


class HighlightTextHtmlFormatter(HtmlFormatter[str]):
    """Give marked token subtypes a stable class for site styling."""

    def _get_css_classes(self, token_type: _TokenType) -> str:
        classes = super()._get_css_classes(token_type)
        if token_type[-1] == _HIGHLIGHT_TOKEN:
            return f"{classes} highlight-text"
        return classes


class HighlightTextPygmentsBridge(PygmentsBridge):
    """Add the substring filter to one HTML highlighting operation."""

    html_formatter = HighlightTextHtmlFormatter

    @classmethod
    def from_bridge(cls, bridge: PygmentsBridge) -> HighlightTextPygmentsBridge:
        replacement = cls.__new__(cls)
        replacement.__dict__.update(bridge.__dict__)
        replacement.formatter = cls.html_formatter
        return replacement

    def get_lexer(
        self,
        source: str,
        lang: str,
        opts: dict[str, Any] | None = None,
        force: bool = False,
        location: Any = None,
    ) -> Lexer:
        lexer_options = dict(opts or {})
        highlight_text = lexer_options.pop(_HIGHLIGHT_ARGUMENT, ())
        lexer = super().get_lexer(source, lang, lexer_options, force, location)
        if not highlight_text:
            return lexer

        # Sphinx keeps some lexer instances globally. Copy both the instance and
        # its filter list so highlighting cannot leak into later code blocks.
        lexer = copy.copy(lexer)
        lexer.filters = list(lexer.filters)
        lexer.add_filter(HighlightTextFilter(highlight_text=highlight_text))
        return lexer

    def highlight_block(
        self,
        source: str,
        lang: str,
        opts: dict[str, Any] | None = None,
        force: bool = False,
        location: Any = None,
        **kwargs: Any,
    ) -> str:
        lexer_options = dict(opts or {})
        highlight_text = kwargs.pop(_HIGHLIGHT_ARGUMENT, ())
        if highlight_text:
            lexer_options[_HIGHLIGHT_ARGUMENT] = highlight_text
        return super().highlight_block(
            source,
            lang,
            lexer_options,
            force,
            location,
            **kwargs,
        )


class HighlightTextCodeBlock(CodeBlock):
    """Extend ``code-block`` with the ``highlight-text`` option."""

    option_spec = {
        **CodeBlock.option_spec,
        _HIGHLIGHT_OPTION: parse_highlight_text,
    }

    def run(self) -> list[nodes.Node]:
        result = super().run()
        highlight_text = self.options.get(_HIGHLIGHT_OPTION)
        if not highlight_text:
            return result

        for node in result:
            literal_blocks = (
                [node]
                if isinstance(node, nodes.literal_block)
                else list(node.findall(nodes.literal_block))
            )
            for literal_block in literal_blocks:
                literal_block.setdefault("highlight_args", {})[
                    _HIGHLIGHT_ARGUMENT
                ] = highlight_text

        return result


def _install_highlighter(app: Sphinx) -> None:
    if app.builder.format != "html":
        return

    for attribute in ("highlighter", "dark_highlighter"):
        highlighter = getattr(app.builder, attribute, None)
        if isinstance(highlighter, PygmentsBridge) and not isinstance(
            highlighter, HighlightTextPygmentsBridge
        ):
            setattr(
                app.builder,
                attribute,
                HighlightTextPygmentsBridge.from_bridge(highlighter),
            )


def setup(app: Sphinx) -> ExtensionMetadata:
    app.add_directive("code-block", HighlightTextCodeBlock, override=True)
    app.connect("builder-inited", _install_highlighter)
    return {
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
