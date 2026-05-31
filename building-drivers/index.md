---
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
{}
---

# Building Drivers

As ADBC has grown, the focus has shifted to building out drivers for all manner of different systems. For the first couple years of the project's history, most drivers were centrally developed by Apache Arrow contributors, with one or two drivers developed indepndently in scattered places. The ADBC Driver Foundry ("the Foundry") aims to scale up driver development by providing an open source hub for federated driver development, along with resources to support database vendors and users in development.

The federated nature of the Foundry lets each driver have its own repository, with its own maintainers and privileges. At the same time, it provides centralized frameworks and consistent processes to ensure a common level of functionality and polish, and gives users a single place to discover, download, and submit feedback on drivers.

Concretely, the Foundry provides:

- A home for your drivers in our [adbc-drivers](https://github.com/adbc-drivers) GitHub organization
- Well-tested and feature complete SDKs for building drivers in a variety of languages
- Ready to run CI workflows for building, testing, and releasing drivers on all major platforms
- A powerful driver validation suite to help you test and document your drivers capabilities
- A place to host documentation for your driver (this website)

If you're interested in building a driver with the Foundry, continue reading to understand the process. If you have any questions, we encourage you to join the [Columnar Community Slack](https://join.slack.com/t/columnar-community/shared_invite/zt-3gt5cb69i-KRjJj~mjUZv5doVmpcVa4w) or to file an issue at [adbc-drivers/onboarding](https://github.com/adbc-drivers/onboarding).

## Repository Modes

Your code can live in a repo in the [adbc-drivers](https://github.com/adbc-drivers) organization or under your GitHub organization.

**Internal**: If you choose to develop under [adbc-drivers](https://github.com/adbc-drivers), a Foundry administrator can grant your team members enough permission to operate entirely independently, including managing secrets and environments for access to external cloud resources.

**External:** If you prefer to develop your driver under your own organization, a Foundry administrator can create a build-only repository for your driver under adbc-drivers.

## Process

At a high level, here's what the process looks like to from zero to a fully released and dbc-installable driver.

1. File an issue at [adbc-drivers/onboarding](https://github.com/adbc-drivers/onboarding). Fill in the template describing the driver you want to build or contribute.
2. A Foundry administrator creates a repo under adbc-drivers.org for your driver.
3. A Foundry administrator adds templates with common workflows, CI, and validation.
4. They invite members of your team and give you appropriate access.
5. You develop the driver as you see fit.
6. You tag releases as they are ready.

When you tag a release, you can coordinate with Foundry administrators to make it available on distribution channels like [dbc](https://columnar.tech/dbc).

## Resources

The Foundry offers a variety of tools to help develop and maintain drivers.

### SDKs

The Foundry is focused on building drivers as shared libraries that can be loaded by any ADBC Driver Manager. Under this mode, drivers can be written in any language that can export a C ABI.

In practice, most drivers are written in C/C++, Go, or Rust. And because Go and Rust are such common choices, the Foundry provides frameworks for both languages that include helpers for common concerns such as error handling and managing result sets, testing, and more. Both of these projects use a "HEAD-only" model where formal releases are not made: just depend on the latest commit. (Also, we currently do not publish these helper frameworks to package managers like crates.io, though that may change in the future.)

#### Go

[driverbase-go](https://github.com/adbc-drivers/driverbase-go)

Components:

- driverbase: a framework for building drivers
- ffitemplate: a template that generates the necessary FFI glue code
- testutil: helpers for writing unit tests
- validation: a Go-specific common test suite that can also be used to test the driver

#### Rust

[driverbase-rs](https://github.com/adbc-drivers/driverbase-rs/)

Components:

- driverbase: a framework for building drivers

(building-drivers-internal-tooling)=
### Internal Tooling/Templating

The Foundry maintains a set of scripts that are used to build, test, and release the drivers. We ask that your driver include these scripts, even if you do not make use of them yourself, as they prepare artifacts in the right format and help us amortize maintenance across all the drivers. (For example, they build Linux drivers in a container to ensure they don't depend on too new of a glibc.)

These scripts are all invoked through [pixi](https://pixi.prefix.dev/latest/). We also maintain a tool in [adbc-drivers/dev](https://github.com/adbc-drivers/dev) that templates out common GitHub Actions workflows and the pixi config itself, so that you do not have to update this yourself. It can be run as follows (using [uv](https://docs.astral.sh/uv/)):

```shell
# from the repo root
uvx \
  --from git+https://github.com/adbc-drivers/dev \
  adbc-gen-workflow generate $(pwd)
```

Based on the configuration file in `.github/workflows/generate.toml`, it will generate CI workflows (see below) and a pixi config. We provide a [JSON schema for the configuration file](https://github.com/adbc-drivers/dev/blob/main/schema/generate-schema.json), and the tool will generate a minimal config if it is run from a repository without a config file. See below for more information about how to use the tool.

#### pre-commit

The Foundry maintains [pre-commit](https://pre-commit.com/) hooks to validate license headers (see below), which we suggest you use. Also, we encourage the use of pre-commit for things like formatting code.

### Testing

We encourage you to test your driver thoroughly. In particular, we encourage you to use the validation suite (described next), but unit tests and other integration tests you develop yourself may also be added.

### Validation & Conformance Testing

The Foundry provides a validation suite at [adbc-drivers/validation](https://github.com/adbc-drivers/validation) that tests common driver functionality and generates user documentation based on the results. These tests are independent of the driver's implementation.

Specifically, the validation suite is a [pytest](https://docs.pytest.org/en/stable/) test suite designed to be overridden and customized for your particular driver. It loads the driver shared library, tests different driver features like the metadata catalog, and runs a series of queries and bulk ingest operations. The test suite records the results and asserts that the expected Arrow data types, result data, etc. are received. This tests both feature completeness and correctness. The results are used to generate documentation showing users supported features and how the driver maps your database's column types to Arrow data types and vice versa.

If you use the standard CI pipelines described below, then this suite will be run for each PR and release, and the generated documentation will be included in the release artifacts. We the Foundry administrators ask that you run this suite so that we can include the documentation on [docs.adbc-drivers.org](https://docs.adbc-drivers.org).

#### Bootstrapping

Currently, we do not have a tool to template this out. We encourage you (or your agent) to look at existing examples.

Examples for data systems that run in the cloud:

- [BigQuery](https://github.com/adbc-drivers/bigquery/tree/main/go/validation)
- [Snowflake](https://github.com/adbc-drivers/snowflake/tree/main/go/validation)

Examples for data systems that run locally and can be dockerized for testing:

- [MySQL](https://github.com/adbc-drivers/mysql/tree/main/go/validation)
- [Trino](https://github.com/adbc-drivers/trino/tree/main/go/validation)

In addition to the tests themselves, a documentation skeleton must be added at `docs/<drivername>.md`. For example, see the template for [BigQuery](https://github.com/adbc-drivers/bigquery/blob/main/go/docs/bigquery.md). This skeleton will be filled in with the result of the tests. The documentation is written in [MyST Markdown](https://mystmd.org/) and will be rendered with the [Sphinx documentation system](https://www.sphinx-doc.org/en/master/), so you can use the full power of Sphinx directives in addition to basic Markdown.

#### Customizing Tests

The main customization point is your implementation of the `DriverQuirks` class, which defines which features are supported (and hence tested).

The queries run by the validation suite can be overridden. See the [documentation](https://github.com/adbc-drivers/validation#adding-new-tests) on the expected format.

Individual tests can be overridden by subclassing/overriding the base test classes. It is not recommended to do this unless necessary as it creates more maintenance work when the tests change or are updated.

#### Running Validation

The pixi config (discussed above) already has dependencies on pytest and the validation suite and can be used to run the tests:

```shell
pixi run validate
```

This wraps pytest's CLI and accepts the same arguments:

```shell
# Run only ingest tests
pixi run validate -k 'ingest'

# Run only GetObjects tests
pixi run validate -k 'get_objects'
```

This will generate a `validation-report.xml` file. The documentation can then be generated:

```shell
pixi run gendocs --output generated/
```

It is recommended to generate the documentation from a full run of the test suite; the generator may not handle partial test results properly in all cases.

### Benchmarks & Performance Testing

We are working on infrastructure for benchmarking. Please talk to us if you would like to learn more.

### CI, Build, and Release

As described {ref}`above <building-drivers-internal-tooling>`, we maintain tools that template out common GitHub Actions workflows and generate packages for release. While maintaining your own CI is of course an option, we recommend at least using the generated workflows as a base.

The basic config will look like this:

```toml
driver = "mysql"

[lang.go]
```

This expects the driver to be located in the `go/` subdirectory. You can configure it to expect the driver at the root instead:

```toml
driver = "mysql"

[lang.go]
subdir = "."
```

See the [JSON schema for the configuration
file](https://github.com/adbc-drivers/dev/blob/main/schema/generate-schema.json) for more details about what can be customized.

If your driver is located in another repo or you wish to use C/C++, you will need custom code. You can see an example of this in the [Quack driver](https://github.com/adbc-drivers/quack), which defines `ci/scripts/build.sh` and `ci/scripts/test.sh` to wire up the C++ build system to the CI workflows.

If you include a `compose.yaml`, you can run tests/validation against a container. There are also various other hooks like `pre-test.sh` and `pre-build.sh` to do any other customization that may be needed.

### Licensing

Generally, drivers are open source under a permissive license. We suggest (and use) [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0), not least because many of us come from a background as maintainers of or contributors to Apache Software Foundation projects, but other permissive open source licenses like MIT or BSD are also reasonable. Please ensure that your driver does not depend on proprietary or copyleft components (i.e. that the driver actually fulfills the requirements of a permissive license).

If you would like to distribute a binary-only driver, or a driver that has binary-only dependencies, please talk with us.

For Apache-licensed repositories:

- All files (within reason) should have the Apache license header and copyright declaration:

  ```text
  Copyright (c) 2026 ADBC Drivers Contributors

  [...]
  ```

- Files that were originally migrated from an Apache Software Foundation repository should keep the original header with this prefix on top:

  ```text
  Copyright (c) 2026 ADBC Drivers Contributors

  This file has been modified from its original version, which is
  under the Apache License:
  ```

- Use our pre-commit hook (see above), which will check this:

  ```yaml
  - repo: https://github.com/adbc-drivers/dev
    rev: <insert latest revision>
    hooks:
    - id: rat
  ```

  The pre-commit hook can be configured with `.rat-excludes` and `.rat-apache` files at the root. The former lists (glob) patterns of files to ignore; the latter maintains an allowlist of files that are expected and allowed to have the "This file has been modified from its original version…" text.

### Distribution & Packaging

If you use {ref}`standard CI workflows <building-drivers-internal-tooling>`, then pushing a tag will trigger a build-test-release that ends with a new release on GitHub containing packages that we can then upload to the CDN. Otherwise, you will need to generate appropriate packages yourself; you can see the [packaging script](https://github.com/adbc-drivers/dev/blob/main/adbc_drivers_dev/package.py) as a reference for the format. You will also need to generate a `manifest.toml` and ideally a documentation page (again, all of this is handled by the standard CI workflows).

Once you have a GitHub release with the expected formats, let a Foundry administrator know so we can check the release and upload it to the dbc CDN.

### Repository Standards

We ask that all open source repositories follow these standards:

## FAQ

### Why not under apache/arrow-adbc?

apache/arrow-adbc is under the Apache Software Foundation, and the maintenance is shared with the broader Apache Arrow project. That creates problems for driver developers and for the Arrow maintainers. For contributors focusing on particular drivers, granting them privileges for their particular projects is difficult or impossible, and the road to maintainership requires demonstrating contributions to the Arrow project as a whole. And for the Arrow maintainers, reviewing contributions and releasing drivers adds to the already large workload of a relatively small group. The Foundry solves this mismatch between the centralized privilege model of Apache projects and the federated nature of driver development.

### Who owns the repo under adbc-drivers?

TODO: Talk about how we envision that the driver/author will be who owns the repo and that the Foundry will help manage it.

### When is a driver ready for release?

Talk about prereleases

### After I build my driver, how does it become available with dbc?

TODO

### Who is responsible for releasing?

TODO

### Who is responsible for responding to issues?

TODO

### What's the best language for writing drivers?

As long as you can produce a shared library on Linux/macOS/Windows that implements the ADBC C APIs, then any language works in principle. We have found that Go and Rust are most convenient, due to the tooling we've built around them. C/C++ also works, but setting up the build has been more trouble. In theory, C#/.NET would also work, but we currently do not distribute any drivers based on this toolchain.
