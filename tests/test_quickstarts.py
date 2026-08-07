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

import json
import subprocess
import sys
from pathlib import Path
from types import SimpleNamespace

import pytest
from sphinx.application import Sphinx

REPOSITORY_ROOT = Path(__file__).parents[1]
sys.path.insert(0, str(REPOSITORY_ROOT / "_ext"))

import quickstarts  # noqa: E402


def _git(repository: Path, *arguments: str) -> str:
    result = subprocess.run(
        ["git", *arguments],
        cwd=repository,
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout.strip()


def _write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


@pytest.fixture
def repository(tmp_path: Path) -> Path:
    repository = tmp_path / "repository"
    repository.mkdir()
    _write(
        repository / ".github/data/languages.json",
        json.dumps({"python": "Python", "go": "Go"}),
    )
    _write(
        repository / ".github/data/databases.json",
        json.dumps(
            {
                "mariadb": {"name": "MariaDB", "parent": "mysql"},
                "mysql": {
                    "name": "MySQL",
                    "parent": "mysql",
                    "display_name_when_parent": "MySQL-compatible systems",
                },
                "tidb": {"name": "TiDB", "parent": "mysql"},
                "bigquery": {"name": "Google BigQuery", "parent": None},
            }
        ),
    )
    _write(repository / "python/mysql/mariadb/main.py", "print('maria')\n")
    _write(repository / "python/mysql/mysql/main.py", "print('mysql')\n")
    _write(repository / "go/mysql/mysql/main.go", "package main\n")
    _write(repository / "python/mysql/tidb/README.md", "Missing main file\n")
    _write(repository / "python/bigquery/main.py", "print('bigquery')\n")
    _git(repository, "init", "--initial-branch=main")
    _git(repository, "add", ".")
    _git(
        repository,
        "-c",
        "user.name=Quickstarts Test",
        "-c",
        "user.email=quickstarts@example.invalid",
        "commit",
        "-m",
        "fixture",
    )
    return repository


@pytest.fixture
def sphinx_output(tmp_path: Path, repository: Path) -> Path:
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
                "extensions = ['sphinx_design', 'quickstarts']",
                "html_theme = 'basic'",
                f"quickstarts_repository = {str(repository)!r}",
                "quickstarts_ref = 'main'",
                "quickstarts_cache_ttl = 3600",
            ]
        ),
    )
    _write(
        source / "index.rst",
        (
            "Quickstarts\n===========\n\n"
            ".. quickstarts:: mysql\n\n"
            ".. toctree::\n\n"
            "   later\n"
        ),
    )
    _write(source / "later.rst", "Later document\n==============\n")

    app = Sphinx(
        source,
        source,
        output,
        doctrees,
        "html",
        warningiserror=False,
        freshenv=True,
    )
    app.build(force_all=True)
    assert app.statuscode == 0
    return output


def test_discover_standalone_and_grouped_examples(repository: Path) -> None:
    languages, databases = quickstarts._load_metadata(repository)
    groups = quickstarts.discover_examples(repository, "mysql", languages, databases)

    assert [group["vendor"] for group in groups] == ["mariadb", "mysql"]
    assert [example["language"] for example in groups[1]["examples"]] == [
        "go",
        "python",
    ]
    standalone = quickstarts.discover_examples(
        repository, "bigquery", languages, databases
    )
    assert (
        standalone[0]["examples"][0]["source"].relative_to(repository).as_posix()
        == "python/bigquery/main.py"
    )


def test_cache_freshness(repository: Path) -> None:
    timestamp = repository / quickstarts._CACHE_TIMESTAMP
    timestamp.touch()
    modified = timestamp.stat().st_mtime
    assert quickstarts._cache_is_fresh(repository, 3600, modified + 3599)
    assert not quickstarts._cache_is_fresh(repository, 3600, modified + 3600)


def test_refresh_failure_uses_stale_checkout(
    repository: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    doctrees = repository.parent / "stale-doctrees"
    cache = doctrees / "adbc-quickstarts"
    _git(repository.parent, "clone", str(repository), str(cache))
    app = SimpleNamespace(
        doctreedir=doctrees,
        config=SimpleNamespace(
            quickstarts_repository=str(repository),
            quickstarts_ref="main",
            quickstarts_cache_ttl=3600,
        ),
    )
    run_git = quickstarts._run_git

    def fail_fetch(*arguments: str, cwd: Path | None = None) -> str:
        if arguments[0] == "fetch":
            raise quickstarts.ExtensionError("refresh failed")
        return run_git(*arguments, cwd=cwd)

    monkeypatch.setattr(quickstarts, "_run_git", fail_fetch)
    checkout, commit = quickstarts.ensure_checkout(app, now=10_000_000_000)

    assert checkout == cache
    assert commit == _git(repository, "rev-parse", "HEAD")


def test_initial_clone_failure_is_fatal(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    app = SimpleNamespace(
        doctreedir=tmp_path / "empty-doctrees",
        config=SimpleNamespace(
            quickstarts_repository="invalid",
            quickstarts_ref="main",
            quickstarts_cache_ttl=3600,
        ),
    )

    def fail_clone(*args, **kwargs) -> None:
        raise quickstarts.ExtensionError("clone failed")

    monkeypatch.setattr(quickstarts, "_clone_checkout", fail_clone)
    with pytest.raises(quickstarts.ExtensionError, match="clone failed"):
        quickstarts.ensure_checkout(app)


def test_sphinx_build_generates_tabs_and_source_pages(
    repository: Path, sphinx_output: Path
) -> None:
    index = (sphinx_output / "index.html").read_text(encoding="utf-8")
    assert "sd-tab-label" in index
    assert "MariaDB" in index
    assert 'checked="checked"' in index
    assert "quickstart-modal-link" in index
    assert 'href="drivers/mysql/quickstarts/mysql/python.html"' in index
    assert f'href="{quickstarts.CLIENT_LIBRARIES_URL}"' in index
    assert ">ADBC client library</a> for your language" in index

    generated = sphinx_output / "drivers/mysql/quickstarts/mysql/python.html"
    assert generated.is_file()
    page = generated.read_text(encoding="utf-8")
    assert "Python quickstart with the ADBC driver for MySQL" in page
    assert "This example shows how to use the ADBC driver for MySQL in Python." in page
    assert "View the full example on GitHub" in page
    assert "print" in page
    assert _git(repository, "rev-parse", "HEAD") in page
    modal_start = page.index('data-quickstart-modal-content=""')
    modal_end = page.index("</div>", modal_start)
    assert "This example shows how" not in page[modal_start:modal_end]
    assert "View the full example on GitHub" in page[modal_start:]
    assert "print" in page[modal_start:]

    assert (sphinx_output / "_static/quickstarts.js").is_file()
    assert (sphinx_output / "_static/quickstarts.css").is_file()
    assert 'src="_static/quickstarts.js?' in index
    assert 'href="_static/quickstarts.css?' in index

    mariadb = (
        sphinx_output / "drivers/mysql/quickstarts/mariadb/python.html"
    ).read_text(encoding="utf-8")
    assert "Python quickstart for MariaDB with the ADBC driver for MySQL" in mariadb
    assert (
        "This example shows how to use the ADBC driver for MySQL in Python with "
        "MariaDB." in mariadb
    )
