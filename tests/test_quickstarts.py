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
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest import mock

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


class QuickstartsTest(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory(prefix="temp_quickstarts_test_")
        self.root = Path(self.temporary.name)
        self.repository = self.root / "repository"
        self.repository.mkdir()
        _write(
            self.repository / ".github/data/languages.json",
            json.dumps({"python": "Python", "go": "Go"}),
        )
        _write(
            self.repository / ".github/data/databases.json",
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
        _write(self.repository / "python/mysql/mariadb/main.py", "print('maria')\n")
        _write(self.repository / "python/mysql/mysql/main.py", "print('mysql')\n")
        _write(self.repository / "go/mysql/mysql/main.go", "package main\n")
        _write(self.repository / "python/mysql/tidb/README.md", "Missing main file\n")
        _write(self.repository / "python/bigquery/main.py", "print('bigquery')\n")
        _git(self.repository, "init", "--initial-branch=main")
        _git(self.repository, "add", ".")
        _git(
            self.repository,
            "-c",
            "user.name=Quickstarts Test",
            "-c",
            "user.email=quickstarts@example.invalid",
            "commit",
            "-m",
            "fixture",
        )
        self.commit = _git(self.repository, "rev-parse", "HEAD")

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def test_discover_standalone_and_grouped_examples(self) -> None:
        languages, databases = quickstarts._load_metadata(self.repository)
        groups = quickstarts.discover_examples(
            self.repository, "mysql", languages, databases
        )

        self.assertEqual(["mariadb", "mysql"], [group["vendor"] for group in groups])
        self.assertEqual(
            ["go", "python"],
            [example["language"] for example in groups[1]["examples"]],
        )
        standalone = quickstarts.discover_examples(
            self.repository, "bigquery", languages, databases
        )
        self.assertEqual(
            "python/bigquery/main.py",
            standalone[0]["examples"][0]["source"]
            .relative_to(self.repository)
            .as_posix(),
        )

    def test_cache_freshness(self) -> None:
        timestamp = self.repository / quickstarts._CACHE_TIMESTAMP
        timestamp.touch()
        modified = timestamp.stat().st_mtime
        self.assertTrue(
            quickstarts._cache_is_fresh(self.repository, 3600, modified + 3599)
        )
        self.assertFalse(
            quickstarts._cache_is_fresh(self.repository, 3600, modified + 3600)
        )

    def test_refresh_failure_uses_stale_checkout(self) -> None:
        doctrees = self.root / "stale-doctrees"
        cache = doctrees / "adbc-quickstarts"
        _git(self.root, "clone", str(self.repository), str(cache))
        app = SimpleNamespace(
            doctreedir=doctrees,
            config=SimpleNamespace(
                quickstarts_repository=str(self.repository),
                quickstarts_ref="main",
                quickstarts_cache_ttl=3600,
            ),
        )
        run_git = quickstarts._run_git

        def fail_fetch(*arguments: str, cwd: Path | None = None) -> str:
            if arguments[0] == "fetch":
                raise quickstarts.ExtensionError("refresh failed")
            return run_git(*arguments, cwd=cwd)

        with mock.patch.object(quickstarts, "_run_git", side_effect=fail_fetch):
            checkout, commit = quickstarts.ensure_checkout(app, now=10_000_000_000)

        self.assertEqual(cache, checkout)
        self.assertEqual(self.commit, commit)

    def test_initial_clone_failure_is_fatal(self) -> None:
        app = SimpleNamespace(
            doctreedir=self.root / "empty-doctrees",
            config=SimpleNamespace(
                quickstarts_repository="invalid",
                quickstarts_ref="main",
                quickstarts_cache_ttl=3600,
            ),
        )
        with (
            mock.patch.object(
                quickstarts,
                "_clone_checkout",
                side_effect=quickstarts.ExtensionError("clone failed"),
            ),
            self.assertRaisesRegex(quickstarts.ExtensionError, "clone failed"),
        ):
            quickstarts.ensure_checkout(app)

    def test_sphinx_build_generates_dropdowns_and_source_pages(self) -> None:
        source = self.root / "site"
        output = self.root / "output"
        doctrees = self.root / "doctrees"
        source.mkdir()
        _write(
            source / "conf.py",
            "\n".join(
                [
                    "import sys",
                    f"sys.path.insert(0, {str(REPOSITORY_ROOT / '_ext')!r})",
                    "extensions = ['sphinx_design', 'quickstarts']",
                    "html_theme = 'basic'",
                    f"quickstarts_repository = {str(self.repository)!r}",
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
        self.assertEqual(0, app.statuscode)

        index = (output / "index.html").read_text(encoding="utf-8")
        self.assertIn("sd-tab-label", index)
        self.assertIn("MariaDB", index)
        self.assertIn('checked="checked"', index)
        self.assertIn(
            f'href="{quickstarts.CLIENT_LIBRARIES_URL}"',
            index,
        )
        self.assertIn(">ADBC client library</a> for your language", index)

        generated = output / "quickstarts/mysql/python.html"
        self.assertTrue(generated.is_file())
        page = generated.read_text(encoding="utf-8")
        self.assertIn("Python quickstart with the ADBC driver for MySQL", page)
        self.assertIn(
            "This example shows how to use the ADBC driver for MySQL in Python.",
            page,
        )
        self.assertIn("View the full example on GitHub", page)
        self.assertIn("print", page)
        self.assertIn(self.commit, page)

        mariadb = (output / "quickstarts/mariadb/python.html").read_text(
            encoding="utf-8"
        )
        self.assertIn(
            "Python quickstart for MariaDB with the ADBC driver for MySQL",
            mariadb,
        )
        self.assertIn(
            "This example shows how to use the ADBC driver for MySQL in Python "
            "with MariaDB.",
            mariadb,
        )


if __name__ == "__main__":
    unittest.main()
