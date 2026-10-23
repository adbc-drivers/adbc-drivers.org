---
blogpost: true
date: 2026-10-23
author: ADBC Drivers Contributors
hide-toc: true
orphan: true
---

<!--
  Copyright (c) 2026 ADBC Drivers Contributors

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

# Updated ADBC drivers for Apache Cassandra, Apache DataFusion, Apache Spark, Amazon Redshift, BigQuery, Databricks, DuckDB Quack, Microsoft SQL Server, MySQL/MariaDB, Oracle Database, Presto, Snowflake, and Trino

The ADBC Drivers Contributors have released updates to drivers for Apache Cassandra, Apache DataFusion, Apache Spark, Amazon Redshift, BigQuery, Databricks, DuckDB Quack, Microsoft SQL Server, MySQL/MariaDB, Oracle Database, Presto, Snowflake, and Trino. All are available now via [dbc](https://docs.columnar.tech/dbc/).[^private]

To update, run `dbc install <driver>`. For the Cassandra and Presto alpha releases, use `dbc install --pre <driver>`.

## Updated Drivers

**[ADBC Driver for Apache Cassandra](https://github.com/adbc-drivers/cassandra) version [0.1.0-alpha.4](/drivers/cassandra/v0.1.0-alpha.4.md)**

- Update dependencies to pick up CVE fixes

**[ADBC Driver for Apache DataFusion](https://github.com/adbc-drivers/datafusion) version [0.28.0](/drivers/datafusion/v0.28.0.md)**

- Update DataFusion to 55.2
- Preserve original column ordinal positions in `GetObjects` results when filtering columns
- Fix bulk ingestion appends for table, schema, and catalog names containing mixed case or special characters

**[ADBC Driver for Apache Spark](https://github.com/adbc-drivers/spark) version [0.3.0](/drivers/spark/v0.3.0.md)**

- Support dictionary-encoded bulk ingestion
- Prevent table listings from failing when `DESCRIBE TABLE` fails on an individual table
- Update dependencies to pick up CVE fixes

**[ADBC Driver for Amazon Redshift](https://github.com/adbc-drivers/redshift) version [1.8.1](/drivers/redshift/v1.8.1.md)**

- Update dependencies to pick up CVE fixes

**[BigQuery ADBC driver](https://github.com/adbc-drivers/bigquery) version [1.14.1](/drivers/bigquery/v1.14.1.md)**

- Update dependencies to pick up CVE fixes

**[ADBC Driver for Databricks](https://github.com/adbc-drivers/databricks) version [0.3.0](/drivers/databricks/v0.3.0.md)**

- Support dictionary arrays in binding and ingestion
- Update dependencies to pick up CVE fixes

**[ADBC Driver for DuckDB Quack](https://github.com/adbc-drivers/quack) version [0.1.0](/drivers/quack/v0.1.0.md)**

- Update DuckDB from `1.5.6` to `2.0.0`
- Enable TLS certificate verification by default

**[ADBC Driver for Microsoft SQL Server](https://github.com/adbc-drivers/mssql) version [1.7.1](/drivers/mssql/v1.7.1.md)**

- Update dependencies to pick up CVE fixes

**[ADBC Driver for MySQL/MariaDB](https://github.com/adbc-drivers/mysql) version [0.7.1](/drivers/mysql/v0.7.1.md)**

- Update dependencies to pick up CVE fixes

**[ADBC Driver for Oracle Database](https://docs.columnar.tech/drivers/oracle) version [0.6.4](https://docs.columnar.tech/drivers/oracle/v0.6.4)**

- Update dependencies to pick up CVE fixes

**[ADBC Driver for Presto](https://github.com/adbc-drivers/presto) version [0.1.0-alpha.4](/drivers/presto/v0.1.0-alpha.4.md)**

- Update dependencies to pick up CVE fixes

**[ADBC Driver for Snowflake](https://github.com/adbc-drivers/snowflake) version [1.15.1](/drivers/snowflake/v1.15.1.md)**

- Update dependencies to pick up CVE fixes

**[ADBC Driver for Trino](https://github.com/adbc-drivers/trino) version [0.7.0](/drivers/trino/v0.7.0.md)**

- Update trino-go-client to `1.4.1`
- Support parameterized year/month and day/time intervals as Arrow month-day-nanosecond intervals
- Report fractional-second precision correctly in interval field metadata
- Update dependencies to pick up CVE fixes

To learn more about any of these drivers, check out the [documentation](/index.md) and [quickstarts](https://github.com/columnar-tech/adbc-quickstarts).

Bug reports and feature requests are welcome at the repositories linked above. You can also start a [Discussion](https://github.com/orgs/adbc-drivers/discussions) on GitHub or join the [Columnar Community Slack](https://join.slack.com/t/columnar-community/shared_invite/zt-3gt5cb69i-KRjJj~mjUZv5doVmpcVa4w).

[^private]: The Oracle Database driver is available from Columnar's private driver registry and requires `dbc auth login`.
