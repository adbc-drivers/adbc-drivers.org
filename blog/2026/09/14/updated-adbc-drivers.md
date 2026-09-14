---
blogpost: true
date: 2026-09-14
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

# Updated ADBC drivers for Apache Cassandra, Apache Spark, Amazon Redshift, BigQuery, Microsoft SQL Server, MySQL/MariaDB, Oracle Database, Presto, Snowflake, and Trino

<p class="blog-post-meta">
  <time datetime="2026-09-14">September 14, 2026</time>
  <span class="blog-post-author">ADBC Drivers Contributors</span>
</p>

Today the ADBC Drivers Contributors released updates to drivers for Apache Cassandra, Apache Spark, Amazon Redshift, BigQuery, Microsoft SQL Server, MySQL/MariaDB, Oracle Database, Presto, Snowflake, and Trino. All are available now via [dbc](https://docs.columnar.tech/dbc/).[^private]

## Updated Drivers

**[ADBC Driver for Apache Cassandra](https://github.com/adbc-drivers/cassandra) version [0.1.0-alpha.2](/drivers/cassandra/v0.1.0-alpha.2.md)**

- Add Cassandra vector column support
- Add ScyllaDB validation coverage
- Update dependencies to pick up CVE fixes and bump the Go version

**[ADBC Driver for Apache Spark](https://github.com/adbc-drivers/spark) version [0.2.1](/drivers/spark/v0.2.1.md)**

- Update dependencies to pick up CVE fixes and bump the Go version

**[ADBC Driver for Amazon Redshift](https://github.com/adbc-drivers/redshift) version [1.7.0](/drivers/redshift/v1.7.0.md)**

- Cache AWS Identity Center browser authentication tokens on disk to reduce repeated browser prompts across connections and processes
- Fix `redshift.connect_timeout` and `redshift.connect_timeout_ms` being incorrectly reported as unknown options
- Update dependencies to pick up CVE fixes and bump the Go version

**[BigQuery ADBC driver](https://github.com/adbc-drivers/bigquery) version [1.13.0](/drivers/bigquery/v1.13.0.md)**

- Return hidden datasets from `GetObjects`
- Add normalized BigQuery job statistics keys to result set schema metadata
- Skip inaccessible tables in `GetObjects`
- Include links to BigQuery jobs in error messages
- Map Google Cloud API errors to more specific ADBC status codes
- Add `BIGQUERY:query_id` to result set schema metadata
- Support `SCRIPT` queries that return result sets
- Exclude hidden datasets from `GetStatistics`
- Cancel server-side BigQuery jobs when statement execution is cancelled or result reading stops early
- Restrict statement cancellation to active execution
- Apply polling backoff consistently while waiting for jobs
- Allow empty impersonation delegate and scope values

**[ADBC Driver for Microsoft SQL Server](https://github.com/adbc-drivers/mssql) version [1.6.2](/drivers/mssql/v1.6.2.md)**

- Prevent excessive memory allocation when parsing malformed GeoArrow WKB values
- Update dependencies to pick up CVE fixes and bump the Go version

**[ADBC Driver for MySQL/MariaDB](https://github.com/adbc-drivers/mysql) version [0.6.1](/drivers/mysql/v0.6.1.md)**

- Update dependencies to pick up CVE fixes and bump the Go version

**[ADBC Driver for Oracle Database](https://docs.columnar.tech/drivers/oracle) version [0.6.3](https://docs.columnar.tech/drivers/oracle/v0.6.3)**

- Update dependencies to pick up CVE fixes and bump the Go version

**[ADBC Driver for Presto](https://github.com/adbc-drivers/presto) version [0.1.0-alpha.2](/drivers/presto/v0.1.0-alpha.2.md)**

- Update dependencies to pick up CVE fixes and bump the Go version

**[ADBC Driver for Snowflake](https://github.com/adbc-drivers/snowflake) version [1.14.0](/drivers/snowflake/v1.14.0.md)**

- Add the `adbc.snowflake.sql.client_option.validate_default_parameters` option to control validation of default connection parameters
- Preserve Snowflake timestamp scale in Arrow and JSON query results
- Detect incompatible source and target schemas during append bulk ingest
- Avoid a potential panic when escaping `LIKE` patterns

**[ADBC Driver for Trino](https://github.com/adbc-drivers/trino) version [0.5.3](/drivers/trino/v0.5.3.md)**

- Update dependencies to pick up CVE fixes and bump the Go version

To learn more about any of these drivers, check out the [documentation](/index.md) and [quickstarts](https://github.com/columnar-tech/adbc-quickstarts).

Bug reports and feature requests are welcome at the repositories linked above. You can also start a [Discussion](https://github.com/orgs/adbc-drivers/discussions) on GitHub or join the [Columnar Community Slack](https://join.slack.com/t/columnar-community/shared_invite/zt-3gt5cb69i-KRjJj~mjUZv5doVmpcVa4w).

[^private]: The Oracle Database driver is available from Columnar's private driver registry and requires `dbc auth login`.
