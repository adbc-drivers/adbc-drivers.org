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

All of the drivers listed under [Available Drivers](../drivers/index.md) (and more) can be installed with [dbc](https://docs.columnar.tech/dbc/), Columnar's CLI for installing and managing ADBC drivers. When drivers are released from the Foundry, they are automatically made available on Columnar's fast, reliable, and globally-available CDN which dbc pulls from.

## Using dbc

dbc has its own documentation that covers its installation and usage: [https://docs.columnar.tech/dbc/](https://docs.columnar.tech/dbc/). We recommended checking that out.

To give you a sense of how simple it is to use dbc, the following steps should work for most users to get started:

### Install dbc

```sh
curl -LsSf https://dbc.columnar.tech/install.sh | sh
```

### Find Drivers

```sh
$ dbc search
bigquery           An ADBC driver for Google BigQuery developed by the ADBC Driver Foundry
databricks         An ADBC Driver for Databricks developed by the ADBC Driver Foundry
duckdb             An ADBC driver for DuckDB developed by the DuckDB Foundation
exasol             An ADBC driver for Exasol developed by Exasol Labs
flightsql          An ADBC driver for Apache Arrow Flight SQL developed under the Apache Software Foundation
mssql              An ADBC driver for Microsoft SQL Server developed by Columnar
mysql              An ADBC Driver for MySQL developed by the ADBC Driver Foundry
```

## Install a Driver

```sh
dbc install sqlite
```

## Run a Query

```sh
$ uv run --with "adbc_driver_manager,pyarrow" python -c "from adbc_driver_manager import dbapi; con = dbapi.connect(uri=\"sqlite://\"); cur = con.cursor(); tbl = cur.execute(\"select 1\").fetch_arrow_table(); print(tbl)"
pyarrow.Table
1: int64
----
1: [[1]]
```

## Using Drivers

To find the documentation for any driver dbc lists, run `dbc doc <driver>`. For example,

```console
$ dbc docs mysql
# your browser should open to https://adbc-drivers.org/drivers/mysql/
```

Another great resource for getting started with ADBC is Columnar's [adbc-quickstarts](https://github.com/columnar-tech/adbc-quickstarts) repo.
