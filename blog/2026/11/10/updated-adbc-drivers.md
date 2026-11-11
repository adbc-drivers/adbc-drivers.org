---
blogpost: true
date: 2026-11-10
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

# Updated ADBC drivers for Apache Cassandra, Apache Spark, Amazon Redshift, BigQuery, Databricks, MariaDB, Microsoft SQL Server, MySQL, Oracle Database, Presto, SAP HANA, Snowflake, and Trino

The ADBC Drivers Contributors have released updates to drivers for Apache Cassandra, Apache Spark, Amazon Redshift, BigQuery, Databricks, Microsoft SQL Server, MySQL, Oracle Database[^private], Presto, SAP HANA[^private], Snowflake, and Trino. Also, we have released a new ADBC driver for MariaDB. All are available now via [dbc](https://docs.columnar.tech/dbc/).

To update, run `dbc install <driver>`. For the Cassandra and Presto alpha releases, use `dbc install --pre <driver>`.

## Updated Drivers

All drivers were updated to pick up CVE fixes in the Go runtime and in dependencies, and to add builds for Windows/arm64.

**[ADBC Driver for Apache Cassandra](https://github.com/adbc-drivers/cassandra) version [0.1.0-alpha.5](/drivers/cassandra/v0.1.0-alpha.5.md)**

- Support vector columns

**[ADBC Driver for Apache Spark](https://github.com/adbc-drivers/spark) version [0.4.0](/drivers/spark/v0.4.0.md)**

- Filter out tables in GetObjects that don't belong to the schema in question

**[ADBC Driver for Amazon Redshift](https://github.com/adbc-drivers/redshift) version [1.9.0](/drivers/redshift/v1.9.0.md)**

- Allow passing username with cluster_type=redshift-iam to have the driver fetch the credentials for that user (instead of assuming the IAM user)

**[ADBC Driver for BigQuery](https://github.com/adbc-drivers/bigquery) version [1.15.0](/drivers/bigquery/v1.15.0.md)**

- Support 4-part table references in `destination_table`

**[ADBC Driver for Databricks](https://github.com/adbc-drivers/databricks) version [0.4.0](/drivers/databricks/v0.4.0.md)**

- Add `databricks.auth_type`
- Return NOT_FOUND if the SQLSTATE indicates a related error

**[ADBC Driver for Microsoft SQL Server](https://github.com/adbc-drivers/mssql) version [1.8.0](/drivers/mssql/v1.8.0.md)**

- When ingesting into a `VARCHAR`, let the server handle encoding conversions

**[ADBC Driver for MariaDB](https://github.com/adbc-drivers/mysql) version [0.1.6](/drivers/mysql/v0.1.6.md)**

- Initial release.

**[ADBC Driver for MySQL](https://github.com/adbc-drivers/mysql) version [0.8.0](/drivers/mysql/v0.8.0.md)**

- Add basic support for Substrait by translating simple plans into SQL. This support is experimental and may have breaking changes or be removed without notice

**[ADBC Driver for Oracle Database](https://docs.columnar.tech/drivers/oracle) version [0.7.0](https://docs.columnar.tech/drivers/oracle/v0.7.0)**

No additional changes.

**[ADBC Driver for Presto](https://github.com/adbc-drivers/presto) version [0.1.0-alpha.5](/drivers/presto/v0.1.0-alpha.5.md)**

- Default `presto://` to TLS

**[ADBC Driver for SAP HANA](https://docs.columnar.tech/drivers/sap-hana) version [0.1.0-alpha.7](https://docs.columnar.tech/drivers/oracle/v0.1.0-alpha.7)**

No additional changes.

**[ADBC Driver for Snowflake](https://github.com/adbc-drivers/snowflake) version [1.16.0](/drivers/snowflake/v1.16.0.md)**

- Allow retrieving the query ID
- Various internal optimizations to reduce memory usage and use recommended Snowflake APIs
- Respect cancellation inside GetCurrentCatalog/GetCurrentDbSchema/GetInfo
- Fix spurious errors in bulk ingest
- Restore intended default behavior of wrap-on-overflow for nanosecond timestamps
- Fix race on shared session params when creating new connections

**[ADBC Driver for Trino](https://github.com/adbc-drivers/trino) version [0.8.0](/drivers/trino/v0.8.0.md)**

- Add option to send extra HTTP headers on requests
- Support client certificate authentication
- Add option to impersonate a user
- Tolerate trailing semicolons in queries
- Serialize timezone-aware timestamps in UTC, fixing precision issues in bulk ingest and parameter binding

To learn more about any of these drivers, check out the [documentation](/index.md) and [quickstarts](https://github.com/columnar-tech/adbc-quickstarts).

Bug reports and feature requests are welcome at the repositories linked above. You can also start a [Discussion](https://github.com/orgs/adbc-drivers/discussions) on GitHub or join the [Columnar Community Slack](https://join.slack.com/t/columnar-community/shared_invite/zt-3gt5cb69i-KRjJj~mjUZv5doVmpcVa4w).

[^private]: The Oracle Database and SAP HANA drivers are available from Columnar's private driver registry and require `dbc auth login`.
