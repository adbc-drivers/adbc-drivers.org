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
:class: grid-vertical-center
Welcome to the [ADBC Driver Foundry](https://adbc-drivers.org){target=_self} driver documentation site. Learn what drivers are available, how to use them, more about [ADBC](https://arrow.apache.org/adbc), and how to get involved with the Foundry. To learn more about the Foundry, head back to the [ADBC Driver Foundry](https://adbc-drivers.org){target=_self} website.
:::
::::

:::{card}
:class-card: sd-bg-primary sd-text-white sd-card-announcement
**New: [Building Drivers](./building-drivers/index.md)**—learn how to build and ship an ADBC driver with the Foundry.
:::

## Available Drivers

Drivers available on [dbc](https://columnar.tech/dbc/) from the ADBC Driver Foundry. If you'd like your driver to be listed here, check out [Building Drivers](./building-drivers/index.md).

:::::{grid} 1 2 4 4
:margin: 0
:class-container: grid-no-padding grid-no-body
:gutter: 2

::::{grid-item-card}
:link: drivers/redshift/index
:link-type: doc
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
::::

::::{grid-item-card}
:link: drivers/datafusion/index
:link-type: doc
:class-header: sd-card-header-with-icon
**Apache DataFusion**
:::{image} _static/driver_icons/color/light_mode/datafusion.svg
:width: 24px
:align: center
:alt:
:::
^^^
::::

::::{grid-item-card}
:link: drivers/spark/index
:link-type: doc
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
::::

::::{grid-item-card}
:link: drivers/bigquery/index
:link-type: doc
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
::::

::::{grid-item-card}
:link: drivers/clickhouse/index
:link-type: doc
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
::::

::::{grid-item-card}
:link: drivers/databricks/index
:link-type: doc
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
::::

::::{grid-item-card}
:link: drivers/quack/index
:link-type: doc
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
::::

::::{grid-item-card}
:link: drivers/exasol/index
:link-type: doc
**Exasol**
^^^
::::

::::{grid-item-card}
:link: drivers/mssql/index
:link-type: doc
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
::::

::::{grid-item-card}
:link: drivers/mysql/index
:link-type: doc
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
::::

::::{grid-item-card}
:link: drivers/singlestore/index
:link-type: doc
**SingleStore**
^^^
::::

::::{grid-item-card}
:link: drivers/snowflake/index
:link-type: doc
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
::::

::::{grid-item-card}
:link: drivers/trino/index
:link-type: doc
:class-header: sd-card-header-with-icon
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
^^^
::::

:::::

Other drivers available on dbc from across the ADBC-verse:

:::::{grid} 1 2 4 4
:margin: 0
:class-container: grid-no-padding grid-no-body
:gutter: 2

::::{grid-item-card}
:link: https://duckdb.org/docs/stable/clients/adbc
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
::::

::::{grid-item-card}
:link: https://arrow.apache.org/adbc/current/driver/flight_sql.html
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
::::

::::{grid-item-card}
:link: https://arrow.apache.org/adbc/current/driver/postgresql.html
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
::::

::::{grid-item-card}
:link: https://arrow.apache.org/adbc/current/driver/sqlite.html
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
::::

::::{grid-item-card}
:link: https://docs.columnar.tech/drivers/oracle
**Oracle Database**
^^^
::::

::::{grid-item-card}
:link: https://docs.columnar.tech/drivers/sap-hana
**SAP HANA**
^^^
::::

::::{grid-item-card}
:link: https://docs.columnar.tech/drivers/teradata
**Teradata**
^^^
::::

:::::

If you'd like to see your ADBC driver listed here, please shoot an email to [hello@adbc-drivers.org](mailto:hello@adbc-drivers.org).


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
