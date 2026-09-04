---
blogpost: true
date: 2026-08-21
author: ADBC Drivers Contributors
hide-toc: true
orphan: true
---

<!--
  Copyright (c) 2025-2026 ADBC Drivers Contributors

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

# Updated ADBC drivers for Apache Spark, Amazon Redshift, Microsoft SQL Server, MySQL, Oracle Database, Snowflake, and Trino

Today the ADBC Drivers Contributors released updates to drivers for Apache Spark, Amazon Redshift, Microsoft SQL Server, MySQL, Oracle Database, Snowflake, and Trino. All are available now via [dbc](https://docs.columnar.tech/dbc/).[^private]

## Updated Drivers

**[ADBC Driver for Apache Spark](https://github.com/adbc-drivers/spark) version [0.2.0](/drivers/spark/v0.2.0.md)**

- Support Microsoft Fabric Lakehouse with Livy
- Bump the Go version to pick up CVE fixes

**[ADBC Driver for Amazon Redshift](https://github.com/adbc-drivers/redshift) version [1.6.0](/drivers/redshift/v1.6.0.md)**

- Report 0 affected rows instead of -1 for DDL statements
- Bump the Go version to pick up CVE fixes

**[ADBC Driver for Microsoft SQL Server](https://github.com/adbc-drivers/mssql) version [1.6.1](/drivers/mssql/v1.6.1.md)**

- Bump the Go version to pick up CVE fixes

**[ADBC Driver for MySQL/MariaDB](https://github.com/adbc-drivers/mysql) version [0.6.0](/drivers/mysql/v0.6.0.md)**

- Add transaction support
- Handle all timestamp precisions
- Skip setting the MySQL session time zone for non-MySQL backends, improving compatibility with Databend
- Bump the Go version to pick up CVE fixes

**[ADBC Driver for Oracle Database](https://docs.columnar.tech/drivers/oracle) version [0.6.2](https://docs.columnar.tech/drivers/oracle/v0.6.2)**

- Add options to control the database type used for ingested string columns
- Support binding dictionary-encoded parameters
- Correct timestamp precision in ExecuteSchema and GetTableSchema
- Bump the Go version and dependencies to address security vulnerabilities

**[ADBC Driver for Snowflake](https://github.com/adbc-drivers/snowflake) version [1.13.0](/drivers/snowflake/v1.13.0.md)**

- Add proxy-specific properties
- Handle the UUID data type in metadata paths
- Bump the Go version to pick up CVE fixes

**[ADBC Driver for Trino](https://github.com/adbc-drivers/trino) version [0.5.2](/drivers/trino/v0.5.2.md)**

- Handle all timestamp precisions
- Bump the Go version to pick up CVE fixes

To learn more about any of these drivers, check out the [documentation](/index.md) and [quickstarts](https://github.com/columnar-tech/adbc-quickstarts).

Bug reports and feature requests are welcome at the repositories linked above. You can also start a [Discussion](https://github.com/orgs/adbc-drivers/discussions) on GitHub or join the [Columnar Community Slack](https://join.slack.com/t/columnar-community/shared_invite/zt-3gt5cb69i-KRjJj~mjUZv5doVmpcVa4w).

[^private]: The Oracle Database driver is available from Columnar's private driver registry and requires `dbc auth login`.
