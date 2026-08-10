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

import re
import sys
from io import StringIO
from pathlib import Path

import pytest
from pygments.token import Name, Punctuation, String
from sphinx.application import Sphinx

REPOSITORY_ROOT = Path(__file__).parents[1]
sys.path.insert(0, str(REPOSITORY_ROOT / "_ext"))

import highlight_text  # noqa: E402


def _write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


@pytest.mark.parametrize(
    ("value", "expected"),
    [
        ("first, second phrase", ("first", "second phrase")),
        ('"first, second", third', ("first, second", "third")),
        (" first, first, , second ", ("first", "second")),
    ],
)
def test_parse_highlight_text(value: str, expected: tuple[str, ...]) -> None:
    assert highlight_text.parse_highlight_text(value) == expected


def test_parse_highlight_text_rejects_invalid_csv() -> None:
    with pytest.raises(ValueError, match="invalid highlight-text value"):
        highlight_text.parse_highlight_text('"unterminated')


def test_filter_matches_across_tokens_and_prefers_longer_values() -> None:
    token_filter = highlight_text.HighlightTextFilter(
        highlight_text=("call", "call(", "hello, world")
    )
    tokens = [
        (Name, "call"),
        (Punctuation, "("),
        (String.Double, '"hello, world"'),
        (Punctuation, ")"),
    ]

    assert list(token_filter.filter(None, iter(tokens))) == [
        (Name.HighlightText, "call"),
        (Punctuation.HighlightText, "("),
        (String.Double, '"'),
        (String.Double.HighlightText, "hello, world"),
        (String.Double, '"'),
        (Punctuation, ")"),
    ]


@pytest.fixture
def sphinx_output(tmp_path: Path) -> tuple[Path, str]:
    source = tmp_path / "site"
    output = tmp_path / "output"
    doctrees = tmp_path / "doctrees"
    source.mkdir()
    _write(
        source / "conf.py",
        "\n".join(
            [
                "import sys",
                f"sys.path.insert(0, {str(REPOSITORY_ROOT / '_ext')!r})",
                "extensions = ['highlight_text', 'myst_parser']",
                "myst_enable_extensions = ['colon_fence']",
                "html_theme = 'basic'",
            ]
        ),
    )
    _write(
        source / "index.rst",
        """Highlight text
==============

.. code-block:: python
   :caption: Highlighted RST
   :emphasize-lines: 1
   :highlight-text: call(, "hello, world"

   call("hello, world")

.. code-block:: python

   call("hello, world")

.. toctree::
   :hidden:

   myst
""",
    )
    _write(
        source / "myst.md",
        """# MyST highlighting

:::{code-block} python
:highlight-text: result, two words

result = "two words"
:::

```python
result = "two words"
```
""",
    )

    warnings = StringIO()
    app = Sphinx(
        source,
        source,
        output,
        doctrees,
        "html",
        warning=warnings,
        warningiserror=False,
        freshenv=True,
    )
    app.build(force_all=True)
    assert app.statuscode == 0
    return output, warnings.getvalue()


def test_sphinx_build_highlights_rst_and_myst_without_leaking(
    sphinx_output: tuple[Path, str],
) -> None:
    output, warnings = sphinx_output
    rst = (output / "index.html").read_text(encoding="utf-8")
    myst = (output / "myst.html").read_text(encoding="utf-8")

    assert warnings == ""
    assert len(re.findall(r'class="[^"]*\bhighlight-text\b', rst)) == 3
    assert 'class="n n-HighlightText highlight-text"' in rst
    assert 'class="p p-HighlightText highlight-text"' in rst
    assert 'class="s2 s2-HighlightText highlight-text"' in rst
    assert 'class="hll"' in rst
    assert "Highlighted RST" in rst
    assert rst.count("call") == 2

    assert len(re.findall(r'class="[^"]*\bhighlight-text\b', myst)) == 2
    assert 'class="n n-HighlightText highlight-text"' in myst
    assert 'class="s2 s2-HighlightText highlight-text"' in myst
