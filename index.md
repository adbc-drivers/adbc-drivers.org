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
hide-navigation: true
hide-toc: true
---

# ADBC Driver Foundry Documentation

::::{grid} 1 1 2 2

:::{grid-item}
```{include} _static/adbc-drivers-logo.svg
```
:::
:::{grid-item}
Welcome to the [ADBC Driver Foundry](https://adbc-drivers.org){target=_self} driver documentation site. Learn what drivers are available, how to use them, more about [ADBC](https://arrow.apache.org/adbc), and how to get involved with the Foundry. To learn more about the Foundry, head back to the [ADBC Driver Foundry](https://adbc-drivers.org){target=_self} website.
:::
::::

:::{card}
:class-card: sd-bg-primary sd-text-white sd-card-announcement
**New: [Building Drivers](./building-drivers/index.md)**—learn how to build and ship an ADBC driver with the Foundry.
:::

## Available Drivers

Drivers available from the ADBC Driver Foundry. If you'd like your driver to be listed here, check out [Building Drivers](./building-drivers/index.md).

:::::{grid} 1 2 4 4
:margin: 0
:class-container: drivers-grid
:gutter: 2

::::{grid-item-card}
:class-header: sd-card-header-with-icon
**Amazon Redshift**
:::{image} _static/driver_icons/color/light_mode/redshift.svg
:class: only-light
:width: 18px
:align: center
:alt:
:::
:::{image} _static/driver_icons/color/dark_mode/redshift.svg
:class: only-dark
:width: 18px
:align: center
:alt:
:::
^^^
Work with Amazon Redshift, a data warehouse offered by AWS. Supports both Provisioned and Serverless offerings.
+++
:::{button-ref} drivers/redshift/index
:click-parent:
Documentation
:::
::::

::::{grid-item-card}
:class-header: sd-card-header-with-icon
**Apache DataFusion**
:::{image} _static/driver_icons/color/light_mode/datafusion.svg
:width: 24px
:align: center
:alt:
:::
^^^
Embed Apache DataFusion, an extensible query engine that uses Apache Arrow as its in-memory format.
+++
:::{button-ref} drivers/datafusion/index
:click-parent:
Documentation
:::
::::

::::{grid-item-card}
:class-header: sd-card-header-with-icon
**Apache Spark**
:::{image} _static/driver_icons/color/light_mode/spark.svg
:class: only-light
:width: 24px
:align: center
:alt:
:::
:::{image} _static/driver_icons/color/dark_mode/spark.svg
:class: only-dark
:width: 24px
:align: center
:alt:
:::
^^^
Connect to Apache Spark, a multi-language engine for large data analytics on single-node machines and multi-node clusters. Supports the HiveServer2 Thrift protocol, Spark Connect, and Apache Livy.
+++
:::{button-ref} drivers/spark/index
:click-parent:
Documentation
:::
::::

::::{grid-item-card}
:class-header: sd-card-header-with-icon
**BigQuery**
:::{image} _static/driver_icons/color/light_mode/bigquery.svg
:class: only-light
:width: 24px
:align: center
:alt:
:::
:::{image} _static/driver_icons/color/dark_mode/bigquery.svg
:class: only-dark
:width: 24px
:align: center
:alt:
:::
^^^
Work with BigQuery, a data warehouse offered by Google Cloud.
+++
:::{button-ref} drivers/bigquery/index
:click-parent:
Documentation
:::
::::

::::{grid-item-card}
:class-header: sd-card-header-with-icon
**ClickHouse**
:::{image} _static/driver_icons/color/light_mode/clickhouse.svg
:class: only-light
:width: 20px
:align: center
:alt:
:::
:::{image} _static/driver_icons/color/dark_mode/clickhouse.svg
:class: only-dark
:width: 20px
:align: center
:alt:
:::
^^^
Work with ClickHouse, an open source data warehouse and analytical database by ClickHouse, Inc.
+++
:::{button-ref} drivers/clickhouse/index
:click-parent:
Documentation
:::
::::

::::{grid-item-card}
:class-header: sd-card-header-with-icon
**Databricks**
:::{image} _static/driver_icons/color/light_mode/databricks.svg
:class: only-light
:width: 24px
:align: center
:alt:
:::
:::{image} _static/driver_icons/color/dark_mode/databricks.svg
:class: only-dark
:width: 24px
:align: center
:alt:
:::
^^^
Work with Databricks, a cloud data platform.
+++
:::{button-ref} drivers/databricks/index
:click-parent:
Documentation
:::
::::

::::{grid-item-card}
:class-header: sd-card-header-with-icon
**DuckDB Quack**
:::{image} _static/driver_icons/color/light_mode/quack.svg
:class: only-light
:width: 24px
:align: center
:alt:
:::
:::{image} _static/driver_icons/color/dark_mode/quack.svg
:class: only-dark
:width: 24px
:align: center
:alt:
:::
^^^
Connect to a remote DuckDB instance via the Quack protocol.
+++
:::{button-ref} drivers/quack/index
:click-parent:
Documentation
:::
::::

::::{grid-item-card}
**Exasol**
^^^
Work with the Exasol in-memory analytics engine.
+++
:::{button-ref} drivers/exasol/index
:click-parent:
Documentation
:::
::::

::::{grid-item-card}
:class-header: sd-card-header-with-icon
**Microsoft SQL Server**
:::{image} _static/driver_icons/color/light_mode/mssql.svg
:class: only-light
:width: 20px
:align: center
:alt:
:::
:::{image} _static/driver_icons/color/dark_mode/mssql.svg
:class: only-dark
:width: 20px
:align: center
:alt:
:::
^^^
Work with Microsoft SQL Server, a relational database system offered by Microsoft.
+++
:::{button-ref} drivers/mssql/index
:click-parent:
Documentation
:::
::::

::::{grid-item-card}
:class-header: sd-card-header-with-icon
**MySQL/MariaDB**
:::{image} _static/driver_icons/color/light_mode/mysql.svg
:class: only-light
:width: 24px
:align: center
:alt:
:::
:::{image} _static/driver_icons/color/dark_mode/mysql.svg
:class: only-dark
:width: 24px
:align: center
:alt:
:::
^^^
Work with MySQL, a free and open source relational database management system.

Also supports MariaDB.
+++
:::{button-ref} drivers/mysql/index
:click-parent:
Documentation
:::
::::

::::{grid-item-card}
**SingleStore**
^^^
Work with SingleStore, a distributed database for low-latency SQL.
+++
:::{button-ref} drivers/singlestore/index
:click-parent:
Documentation
:::
::::

::::{grid-item-card}
:class-header: sd-card-header-with-icon
**Snowflake**
:::{image} _static/driver_icons/color/light_mode/snowflake.svg
:class: only-light
:width: 24px
:align: center
:alt:
:::
:::{image} _static/driver_icons/color/dark_mode/snowflake.svg
:class: only-dark
:width: 24px
:align: center
:alt:
:::
^^^
Work with Snowflake, a cloud data warehouse.
+++
:::{button-ref} drivers/snowflake/index
:click-parent:
Documentation
:::
::::

::::{grid-item-card}
:class-header: sd-card-header-with-icon
**Trino**
:::{image} _static/driver_icons/color/light_mode/trino.svg
:class: only-light
:width: 24px
:align: center
:alt:
:::
:::{image} _static/driver_icons/color/dark_mode/trino.svg
:class: only-dark
:width: 24px
:align: center
:alt:
:::
^^^
Work with Trino, a distributed SQL query engine.
+++
:::{button-ref} drivers/trino/index
:click-parent:
Documentation
:::
::::

:::::

## Other Drivers

Drivers available across the ADBC-verse:

:::::{grid} 1 2 4 4
:margin: 0
:class-container: drivers-grid
:gutter: 2

::::{grid-item-card}
:class-header: sd-card-header-with-icon
**DuckDB**
:::{image} _static/driver_icons/color/light_mode/duckdb.svg
:class: only-light
:width: 24px
:align: center
:alt:
:::
:::{image} _static/driver_icons/color/dark_mode/duckdb.svg
:class: only-dark
:width: 24px
:align: center
:alt:
:::
^^^
DuckDB ADBC driver from the DuckDB project
+++
:::{button-link} https://duckdb.org/docs/stable/clients/adbc
:click-parent:
Documentation
:::
::::

::::{grid-item-card}
:class-header: sd-card-header-with-icon
**Flight SQL**
:::{image} _static/driver_icons/color/light_mode/flightsql.svg
:class: only-light
:width: 24px
:align: center
:alt:
:::
:::{image} _static/driver_icons/color/dark_mode/flightsql.svg
:class: only-dark
:width: 24px
:align: center
:alt:
:::
^^^
Arrow Flight SQL ADBC driver from the Apache Arrow project
+++
:::{button-link} https://arrow.apache.org/adbc/current/driver/flight_sql.html
:click-parent:
Documentation
:::
::::

::::{grid-item-card}
:class-header: sd-card-header-with-icon

**PostgreSQL**
:::{image} _static/driver_icons/color/light_mode/postgresql.svg
:class: only-light
:width: 24px
:align: center
:alt:
:::
:::{image} _static/driver_icons/color/dark_mode/postgresql.svg
:class: only-dark
:width: 24px
:align: center
:alt:
:::
^^^
PostgreSQL ADBC driver from the Apache Arrow project
+++
:::{button-link} https://arrow.apache.org/adbc/current/driver/postgresql.html
:click-parent:
Documentation
:::
::::

::::{grid-item-card}
:class-header: sd-card-header-with-icon
**SQLite**
:::{image} _static/driver_icons/color/light_mode/sqlite.svg
:class: only-light
:width: 24px
:align: center
:alt:
:::
:::{image} _static/driver_icons/color/dark_mode/sqlite.svg
:class: only-dark
:width: 24px
:align: center
:alt:
:::
^^^
SQLite ADBC driver from the Apache Arrow project
+++
:::{button-link} https://arrow.apache.org/adbc/current/driver/sqlite.html
:click-parent:
Documentation
:::
::::

::::{grid-item-card}
**Oracle Database**
^^^
ADBC driver for Oracle Database from Columnar
+++
:::{button-link} https://docs.columnar.tech/drivers/oracle
:click-parent:
Documentation
:::
::::

::::{grid-item-card}
**SAP HANA**
^^^
ADBC driver for SAP HANA from Columnar
+++
:::{button-link} https://docs.columnar.tech/drivers/sap-hana
:click-parent:
Documentation
:::
::::

::::{grid-item-card}
**Teradata**
^^^
ADBC driver for Teradata from Columnar
+++
:::{button-link} https://docs.columnar.tech/drivers/teradata
:click-parent:
Documentation
:::
::::

:::::

If you'd like to see your ADBC driver listed here, please shoot an email to [hello@adbc-drivers.org](mailto:hello@adbc-drivers.org).


## Guides

:::::{grid} 1 2 3 3
:margin: 0
:class-container: drivers-grid
:gutter: 2

::::{grid-item-card}
**Using Drivers**
^^^
Learn how to install drivers from the Foundry and use them with your favorite programming language.
+++
:::{button-ref} using-drivers/index
:click-parent:
Read Guide
:::
::::

::::{grid-item-card}
**Building Drivers**
^^^
Learn how to build an ADBC driver in the Foundry.
+++
:::{button-ref} building-drivers/index
:click-parent:
Read Guide
:::
::::

:::::

## ADBC Resources

:::::{grid} 1 2 3 3
:margin: 0
:class-container: drivers-grid
:gutter: 2

::::{grid-item-card}
**Apache Arrow ADBC**
^^^
Official documentation for the ADBC specification and project.
+++
:::{button-link} https://arrow.apache.org/adbc/current/index.html
:click-parent:
Documentation
:::
::::

::::{grid-item-card}
**dbc**
^^^
Install and manage drivers easily with a CLI from Columnar.
+++
:::{button-link} https://docs.columnar.tech/dbc/
:click-parent:
Documentation
:::
::::

::::{grid-item-card}
**ADBC Quickstarts**
^^^
Simple examples showing how to use ADBC with various databases, query engines, and data platforms.
+++
:::{button-link} https://github.com/columnar-tech/adbc-quickstarts
:click-parent:
Repository
:::
::::

:::::

:::{toctree}
:maxdepth: 3
:hidden:

Home <self>
building-drivers/index.md
using-drivers/index.md
drivers/index.md
Back to ADBC Driver Foundry <https://adbc-drivers.org>
:::
