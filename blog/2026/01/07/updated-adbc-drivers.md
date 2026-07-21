---
blogpost: true
date: 2026-01-07
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

# Updated ADBC drivers for BigQuery, SQL Server, MySQL, Redshift, Snowflake, and Trino

<p class="blog-post-meta">
  <time datetime="2026-01-07">January 07, 2026</time>
  <span class="blog-post-author">ADBC Drivers Contributors</span>
</p>

Today the ADBC Drivers Contributors released updated drivers for six database systems, available immediately via [dbc](https://docs.columnar.tech/dbc/). To update, just `dbc install <driver>` to get the latest version.

## Updated Drivers

The newly released drivers, and some release highlights, are:

### [Google BigQuery driver](https://github.com/adbc-drivers/bigquery) version 1.10.0
* Support for bulk ingest of Arrow’s list and struct types
* General bug fixes, including fixing hangs in certain cases

### [Microsoft SQL Server driver](http://github.com/adbc-drivers/mssql) version 1.1.0
* Improved support for `DATETIME2`, `CHAR`/`NCHAR`
* Support for binding/ingesting Arrow’s large/view/fixed-size string and binary types

### [MySQL driver](https://github.com/adbc-drivers/mysql) version 0.2.0
* Force the connection timezone to UTC for consistent handling
* Support the `BIT` type

### [Amazon Redshift driver](https://github.com/adbc-drivers/redshift/) version 1.1.0
* Experimental support for IdP token authentication and more options for IdP browser authentication
* Support for binding/ingesting Arow’s list/struct types (they become `SUPER` in Redshift)
* Improved support for `GEOMETRY`, `GEOGRAPHY`, `HLLSKETCH`, and `SUPER`

### [Snowflake driver](https://github.com/adbc-drivers/snowflake) version 1.10.0
* Improved handling of `TIMESTAMP_TZ`

### [Trino driver](https://github.com/adbc-drivers/trino) version 0.2.0
* Fixed timeouts during long-running queries
* Improved support for binary types

Additionally, all drivers now support connecting with URIs in addition to their native connection string formats. To learn more about how to use the drivers, check out the [documentation](https://adbc-drivers.org/) and [quickstarts](https://github.com/columnar-tech/adbc-quickstarts).

Bug reports and feature requests are welcome at the repositories linked above. You can also start a [Discussion](https://github.com/orgs/adbc-drivers/discussions) on GitHub or join the [Columnar Community Slack](https://join.slack.com/t/columnar-community/shared_invite/zt-3gt5cb69i-KRjJj~mjUZv5doVmpcVa4w).
