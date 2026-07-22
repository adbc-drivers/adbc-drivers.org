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

# ADBC Driver Foundry

::::{grid} 1 1 2 2
:gutter: 2
:class-row: homepage-intro-grid

:::{grid-item}
```{include} _static/adbc-drivers-logo.svg
```
:::
:::{grid-item}
:class: grid-vertical-center
Welcome to the **ADBC Driver Foundry**, a community hub for developers and users of [ADBC](https://arrow.apache.org/adbc) drivers. Learn what drivers are available, how to use them, and how to get involved with the Foundry. Read the latest project news on the [Blog](./blog/index.md).
:::
::::

:::{card}
:class-card: sd-bg-primary sd-text-white sd-card-announcement
:link: building-drivers/index
:link-type: doc
:link-alt: Building Drivers
**New: Building Drivers**—learn how to build and ship an ADBC driver with the Foundry.
:::

## Available Drivers

Drivers available on [dbc](https://columnar.tech/dbc/) from the ADBC Driver Foundry. If you'd like your driver to be listed here, check out [Building Drivers](./building-drivers/index.md).

:::::{grid} 1 2 3 4
:margin: 0
:class-container: grid-no-padding grid-no-body
:gutter: 2

::::{grid-item-card}
:link: drivers/redshift/index
:link-type: doc
:class-body: sd-card-with-icon
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
::::

::::{grid-item-card}
:link: drivers/datafusion/index
:link-type: doc
:class-body: sd-card-with-icon
**Apache DataFusion**
:::{image} _static/driver_icons/color/light_mode/datafusion.svg
:width: 24px
:align: center
:alt:
:::
::::

::::{grid-item-card}
:link: drivers/spark/index
:link-type: doc
:class-body: sd-card-with-icon
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
::::

::::{grid-item-card}
:link: drivers/bigquery/index
:link-type: doc
:class-body: sd-card-with-icon
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
::::

::::{grid-item-card}
:link: drivers/clickhouse/index
:link-type: doc
:class-body: sd-card-with-icon
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
::::

::::{grid-item-card}
:link: drivers/databricks/index
:link-type: doc
:class-body: sd-card-with-icon
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
::::

::::{grid-item-card}
:link: drivers/quack/index
:link-type: doc
:class-body: sd-card-with-icon
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
::::

::::{grid-item-card}
:link: drivers/exasol/index
:link-type: doc
:class-body: sd-card-center
**Exasol**
::::

::::{grid-item-card}
:link: drivers/mssql/index
:link-type: doc
:class-body: sd-card-with-icon
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
::::

::::{grid-item-card}
:link: drivers/mysql/index
:link-type: doc
:class-body: sd-card-with-icon
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
::::

::::{grid-item-card}
:link: drivers/singlestore/index
:link-type: doc
:class-body: sd-card-center
**SingleStore**
::::

::::{grid-item-card}
:link: drivers/snowflake/index
:link-type: doc
:class-body: sd-card-with-icon
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
::::

::::{grid-item-card}
:link: drivers/trino/index
:link-type: doc
:class-body: sd-card-with-icon
**Trino**
:::{image} _static/driver_icons/color/light_mode/trino.svg
:class: only-light
:width: 18px
:align: center
:alt:
:::
:::{image} _static/driver_icons/color/dark_mode/trino.svg
:class: only-dark
:width: 18px
:align: center
:alt:
:::
::::

:::::

Other drivers available on dbc from across the ADBC-verse:

:::::{grid} 1 2 3 4
:margin: 0
:class-container: grid-no-padding grid-no-body
:gutter: 2

::::{grid-item-card}
:link: https://duckdb.org/docs/stable/clients/adbc
:class-body: sd-card-with-icon
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
::::

::::{grid-item-card}
:link: https://arrow.apache.org/adbc/current/driver/flight_sql.html
:class-body: sd-card-with-icon
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
::::

::::{grid-item-card}
:link: https://arrow.apache.org/adbc/current/driver/postgresql.html
:class-body: sd-card-with-icon

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
::::

::::{grid-item-card}
:link: https://arrow.apache.org/adbc/current/driver/sqlite.html
:class-body: sd-card-with-icon
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
::::

::::{grid-item-card}
:link: https://docs.columnar.tech/drivers/oracle
:class-body: sd-card-center
**Oracle Database**
::::

::::{grid-item-card}
:link: https://docs.columnar.tech/drivers/sap-hana
:class-body: sd-card-center
**SAP HANA**
::::

::::{grid-item-card}
:link: https://docs.columnar.tech/drivers/teradata
:class-body: sd-card-center
**Teradata**
::::

:::::

If you'd like to see your ADBC driver listed here, please email us at [hello@adbc-drivers.org](mailto:hello@adbc-drivers.org).


## Guides

:::::{grid} 1 2 3 3
:margin: 0
:class-container: grid-no-padding
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
:class-container: grid-no-padding
:gutter: 2

::::{grid-item-card}
**ADBC**
^^^
Official documentation for the ADBC specification and project, a part of the Apache Arrow project.
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
Drivers <drivers/index.md>
Using Drivers <using-drivers/index.md>
Building Drivers <building-drivers/index.md>
Blog <blog/index.md>
About <about/index.md>
:::
