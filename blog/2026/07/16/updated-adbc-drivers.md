---
blogpost: true
date: 2026-07-16
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

# Updated ADBC drivers for Apache Spark, BigQuery, Databricks, DuckDB Quack, MySQL, and Oracle Database

<p class="blog-post-meta">
  <time datetime="2026-07-16">July 16, 2026</time>
  <span class="blog-post-author">ADBC Drivers Contributors</span>
</p>

Today the ADBC Drivers Contributors released updates to drivers for Apache Spark, BigQuery, Databricks, DuckDB Quack, MySQL, and Oracle Database. All are available now via [dbc](https://docs.columnar.tech/dbc/).

## Updated Drivers

**[Apache Spark driver](https://github.com/adbc-drivers/spark) version [0.1.0-alpha.3](https://adbc-drivers.org/drivers/spark/v0.1.0-alpha.3)**

- Improved compatibility for both Spark Connect and Apache Livy on Amazon EMR
- Added the `spark.ingest.location` option to specify the LOCATION clause in CREATE TABLE in bulk ingest
- Properly release Spark Connect sessions on disconnect
- Accept `auth_type=none` for Apache Livy and Spark Connect connections without authentication

**[BigQuery driver](https://github.com/adbc-drivers/bigquery) version [1.12.1](https://adbc-drivers.org/drivers/bigquery/v1.12.1)**

- Bumped Go version to address security vulnerabilities

**[Databricks driver](https://github.com/adbc-drivers/databricks) version [0.1.3](https://adbc-drivers.org/drivers/databricks/v0.1.3)**

- Bumped Go version to address security vulnerabilities

**[DuckDB Quack driver](https://github.com/adbc-drivers/quack) version [0.1.0-alpha.2](https://adbc-drivers.org/drivers/quack/v0.1.0-alpha.2)**

- Bumped DuckDB from 1.5.3 to 1.5.4

**[MySQL driver](https://github.com/adbc-drivers/mysql) version [0.5.0](https://adbc-drivers.org/drivers/mysql/v0.5.0)**

- Added an option to control how dates and datetimes with zero components (e.g. `0000-00-00`) are handled: either raise an error (the default) or treat the value as NULL

**[Oracle Database driver](https://docs.columnar.tech/drivers/oracle) version [0.6.1](https://docs.columnar.tech/drivers/oracle/v0.6.1)**

- Bumped Go version and dependencies to address security vulnerabilities

To learn more about any of these drivers, check out the [documentation](https://adbc-drivers.org/) and [quickstarts](https://github.com/columnar-tech/adbc-quickstarts).

Bug reports and feature requests are welcome at the repositories linked above. You can also start a [Discussion](https://github.com/orgs/adbc-drivers/discussions) on GitHub or join the [Columnar Community Slack](https://join.slack.com/t/columnar-community/shared_invite/zt-3gt5cb69i-KRjJj~mjUZv5doVmpcVa4w).
