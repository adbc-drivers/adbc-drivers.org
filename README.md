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

# ADBC Driver Foundry Website

Source code for the [ADBC Driver Foundry website](https://adbc-drivers.org),
including driver documentation, the Foundry blog, and information about the
project.
This project uses [Sphinx](https://sphinx-doc.org) and can be built with [Pixi](https://pixi.sh).

## Building

## Prerequisites

- [Pixi](https://pixi.sh) (see [Pixi Installation](https://pixi.sh/latest/installation/))

## Build and Preview

Build the site with:

```console
$ pixi run build
```

To preview the site you built, run:

```console
$ pixi run serve
```

Then open your web browser to <http://localhost:8000>.

For development, you can instead use the development server which will automatically rebuild the site when changes are made:

```console
$ pixi run watch
```

Then visit <http://localhost:8000>.

Note that the theme used does not always work well with incremental builds.
You may need to remove `_build` and start again, especially when changing theme options.

## Adding a blog post

Blog posts are regular MyST Markdown documents stored at
`YYYY/MM/DD/post-slug.md`. Mark the document with `blogpost: true` and a date
in its YAML front matter; ABlog then adds it to `/blog/` and the Atom feed. The
source path intentionally produces the existing date-based public URL, such as
`/2026/07/20/updated-spark-driver.html`.

Use an existing post as the template so the author/date byline and page options
remain consistent. Ensure that `hide-toc: true` and `orphan: true` are included
in the YAML.

## Domains

The canonical production domain is `adbc-drivers.org`. The GitHub Pages custom
domain for this repository must be set to that apex domain. The legacy
`docs.adbc-drivers.org` host should issue a permanent redirect to the same path,
query, and fragment on `adbc-drivers.org`; the site also includes a client-side
host redirect as a fallback when the legacy hostname serves this artifact.

## Contributing

See [CONTRIBUTING.md](./CONTRIBUTING.md) for information on how to contribute.
