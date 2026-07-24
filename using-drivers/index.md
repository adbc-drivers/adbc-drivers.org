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

# Using Drivers

All drivers listed under [Available Drivers](../drivers/index.md) can be installed with [dbc](https://docs.columnar.tech/dbc/), the package manager for ADBC drivers. Foundry releases are automatically published to Columnar's public [driver registry](https://dbc-cdn.columnar.tech), where dbc retrieves them.

## Using dbc

dbc has its own documentation that covers its installation and usage: [docs.columnar.tech/dbc](https://docs.columnar.tech/dbc/). We recommend referring to it for complete details. To get started with dbc, follow these steps:

### Installing dbc

Choose the installation method that best fits your platform and toolchain:

::::{tab-set}

:::{tab-item} Linux/macOS shell
```console
$ curl -LsSf https://dbc.columnar.tech/install.sh | sh
```
:::

:::{tab-item} Windows shell
```console
$ powershell -ExecutionPolicy ByPass -c "irm https://dbc.columnar.tech/install.ps1 | iex"
```
:::

:::{tab-item} Windows MSI
{.installer-download}
Download <https://dbc.columnar.tech/latest/dbc-latest-x64.msi> and then run the installer.
:::

:::{tab-item} WinGet
```console
$ winget install Columnar.dbc
```
:::

:::{tab-item} uv
```console
$ uv tool install dbc
```
:::

:::{tab-item} pipx
```console
$ pipx install dbc
```
:::

:::{tab-item} Homebrew
```console
$ brew install columnar-tech/tap/dbc
```
:::

:::{tab-item} npm
```console
$ npm install -g @columnar-tech/dbc
```
:::

::::

### Finding Drivers

Use dbc to search the registry to see which drivers are available:

```console
$ dbc search
bigquery           An ADBC driver for Google BigQuery developed by the ADBC Driver Foundry
clickhouse         An ADBC driver for ClickHouse developed by ClickHouse, Inc.
databricks         An ADBC Driver for Databricks developed by the ADBC Driver Foundry
datafusion         An ADBC driver for Apache DataFusion developed by the ADBC Driver Foundry
duckdb             An ADBC driver for DuckDB developed by the DuckDB Foundation
exasol             An ADBC driver for Exasol developed by Exasol Labs
flightsql          An ADBC driver for Apache Arrow Flight SQL developed under the Apache Software Foundation
mssql              An ADBC driver for Microsoft SQL Server developed by Columnar
mysql              An ADBC Driver for MySQL developed by the ADBC Driver Foundry
⋮
```

### Installing a Driver

Install a driver by passing its name to `dbc install`. For example, to install the SQLite driver:

```console
$ dbc install sqlite
```

### Finding Driver Documentation

Open the documentation for any listed driver with `dbc docs <driver>`. For example:

```console
$ dbc docs mysql
```

Your browser should open to <https://adbc-drivers.org/drivers/mysql/>.

## Running a Query

Once you've installed a driver, you can use it from any language that has an ADBC client library, also known as an ADBC driver manager. Provide the driver's name in the `driver` argument, or use a URI beginning with `drivername://` in the `uri` argument. The driver manager searches for it in the same location where dbc installs drivers.

The basic workflow—connect, execute a query, and read the result as Arrow data—works with any ADBC driver, though the syntax varies by language and the parameters vary by database. This Python example uses SQLite:

```console
$ uv run \
>     --with "adbc_driver_manager,pyarrow" python -c \
>     "from adbc_driver_manager import dbapi; \
>     con = dbapi.connect(uri='sqlite://'); \
>     cur = con.cursor(); \
>     tbl = cur.execute('select 1').fetch_arrow_table(); \
>     print(tbl)"
pyarrow.Table
1: int64
----
1: [[1]]
```

For more examples, Columnar's [adbc-quickstarts](https://github.com/columnar-tech/adbc-quickstarts) repository covers 30+ databases across 9+ programming languages.

The ADBC API goes far beyond running `SELECT` statements and returning results: it also supports bulk ingestion, catalog exploration, and much more. See the [ADBC client library documentation](https://arrow.apache.org/adbc/main/client_libraries.html) for more in-depth examples in several languages.
