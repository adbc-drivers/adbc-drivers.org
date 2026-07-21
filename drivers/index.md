---
# Copyright (c) 2025 ADBC Drivers Contributors
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

# Available Drivers

The ADBC Driver Foundry provides a set of ADBC drivers for different
vendors.  All drivers implement the ADBC 1.1 interface and can be used from
different languages including Go, Python, R, Rust, and more.

Documentation for the following ADBC Driver Foundry drivers is hosted on this website:

:::{toctree}
:maxdepth: 1

bigquery/index.md
clickhouse/index.md
databricks/index.md
datafusion/index.md
exasol/index.md
mssql/index.md
mysql/index.md
quack/index.md
redshift/index.md
singlestore/index.md
snowflake/index.md
spark/index.md
trino/index.md
:::

The following drivers are also installable with [dbc](https://docs.columnar.tech/dbc/), but their documentation is hosted elsewhere:

- [DuckDB](https://duckdb.org/docs/stable/clients/adbc)
- [Flight SQL](https://arrow.apache.org/adbc/current/driver/flight_sql.html)
- [PostgreSQL](https://arrow.apache.org/adbc/current/driver/postgresql.html)
- [SQLite](https://arrow.apache.org/adbc/current/driver/sqlite.html)
- [Oracle Database](https://docs.columnar.tech/drivers/oracle)
- [SAP HANA](https://docs.columnar.tech/drivers/sap-hana)
- [Teradata](https://docs.columnar.tech/drivers/teradata)

:::{toctree}
:hidden:
:maxdepth: 1

DuckDB <https://duckdb.org/docs/stable/clients/adbc>
Flight SQL <https://arrow.apache.org/adbc/current/driver/flight_sql.html>
PostgreSQL <https://arrow.apache.org/adbc/current/driver/postgresql.html>
SQLite <https://arrow.apache.org/adbc/current/driver/sqlite.html>
Oracle Database <https://docs.columnar.tech/drivers/oracle>
SAP HANA <https://docs.columnar.tech/drivers/sap-hana>
Teradata <https://docs.columnar.tech/drivers/teradata>
:::

If you'd like to see your driver show up in the list, check out our [Building Drivers](../building-drivers/index.md) guide or email us at [hello@adbc-drivers.org](mailto:hello@adbc-drivers.org).
