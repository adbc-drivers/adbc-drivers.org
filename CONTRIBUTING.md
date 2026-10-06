<!--
  Copyright (c) 2025 ADBC Drivers Contributors

  Licensed under the Apache License, Version 2.0 (the "License");
  you may not use this file except in compliance with the License.
  You may obtain a copy of the License at

          http://www.apache.org/licenses/LICENSE-2.0

  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License.
-->

# How to Contribute

## Reporting Issues

Please file issues on the GitHub issue tracker:
https://github.com/adbc-drivers/adbc-drivers.org/issues

> [!TIP]
>
> The markdown pages under the `./drivers` folder are generated automatically
> during the release process for each driver and then synchronized into this
> repo after drivers are released. If you report an issue with the documentation
> for a driver, a maintainer may redirect or duplicate your issue to the
> repository for the driver.

Potential security vulnerabilities should be reported to
[security@adbc-drivers.org](mailto:security@adbc-drivers.org) instead.  See
[SECURITY.md](https://github.com/adbc-drivers/adbc-drivers.org?tab=security-ov-file#readme).

## Opening a Pull Request

Before opening a pull request:

- Review your changes and make sure no stray files, etc. are included.
- Ensure the Apache license header is at the top of all files.
- Check if there is an existing issue.  If not, please file one, unless the
  change is trivial.
- Assign the issue to yourself by commenting just the word `take`.
- Run the static checks by installing [pre-commit](https://pre-commit.com/),
  then running `pre-commit run --all-files` from inside the repository.  Make
  sure all your changes are staged/committed (unstaged changes will be
  ignored).

When writing the pull request description:

- Ensure the title follows [Conventional
  Commits](https://www.conventionalcommits.org/en/v1.0.0/) format.  The
  component should be `docs` if it affects the content of any pages, or it can
  be omitted for general maintenance. Example
  titles:
  - `docs: add new page for xyz`
  - `chore: update action versions`
  - `chore: update sphinx version`

- Make sure the bottom of the description has `Closes #NNN`, `Fixes #NNN`, or
  similar, so that the issue will be linked to your pull request.

## Setting up a Developer Environment

We use [Pixi](https://pixi.sh) for managing the development process. See [Pixi Installation](https://pixi.sh/latest/installation/) for information on how to install Pixi.

Once Pixi is installed, run:

```sh
pixi run
```

to see the available tasks.

## Code of Conduct

Contributors are expected to follow our [Code of Conduct](https://github.com/adbc-drivers/adbc-drivers.org?tab=coc-ov-file).
