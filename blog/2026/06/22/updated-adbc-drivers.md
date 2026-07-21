---
blogpost: true
date: 2026-06-22
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

# Updated ADBC drivers for BigQuery and Oracle Database

<p class="blog-post-meta">
  <time datetime="2026-06-22">June 22, 2026</time>
  <span class="blog-post-author">ADBC Drivers Contributors</span>
</p>

Today the ADBC Drivers Contributors released updated drivers for BigQuery and Oracle Database, available immediately via [dbc](https://docs.columnar.tech/dbc/). To update, just `dbc install [bigquery|oracle]` to get the latest version[^trial].

## Updated Drivers

**[BigQuery driver](https://github.com/adbc-drivers/bigquery) version [1.12.0](https://adbc-drivers.org/drivers/bigquery/v1.12.0)**

- Make option names more consistent (allow `bigquery.foo` in addition to `adbc.bigquery.sql.foo`)
- Add query statistics to the schema metadata of the result
- Implement GetStatistics
- Add the SRID to returned GeoArrow metadata
- Allow binding Arrow time[ns] values by truncating
- Auto-detect the credential type from JSON credentials
- Improve error handling around authentication
- Handle dry-run queries properly instead of erroring

**Oracle Database driver version [0.6.0](https://docs.columnar.tech/drivers/oracle/v0.6.0)**

:::{note}
The default execution mode will become `batch` in the next minor version (v0.7.0) and the `row` option will be removed the following minor version (v0.8.0).
:::

- Support querying/bulk ingesting interval types
- Support retrieving the value of OUT bind parameters as columns of the result set
- Add an option to control the Arrow type of NUMBER types without a precision/scale
- Support querying and ingesting SDO_GEOMETRY columns as GeoArrow extension types
- Retrieve the result of `DBMS_SQL.RETURN_RESULT`
- Allow setting various options on initial connection

To learn more about how to use the drivers, check out the [documentation](https://adbc-drivers.org/) and [quickstarts](https://github.com/columnar-tech/adbc-quickstarts).

Bug reports and feature requests are welcome at the repositories linked above. You can also start a [Discussion](https://github.com/orgs/adbc-drivers/discussions) on GitHub or join the [Columnar Community Slack](https://join.slack.com/t/columnar-community/shared_invite/zt-3gt5cb69i-KRjJj~mjUZv5doVmpcVa4w).

[^trial]: For the Oracle Database driver, you will need to log in with `dbc auth login` first.
