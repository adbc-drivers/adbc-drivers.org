---
blogpost: true
date: 2026-06-18
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

# Updated ADBC drivers for Exasol, MySQL, and Snowflake

<p class="blog-post-meta">
  <time datetime="2026-06-18">June 18, 2026</time>
  <span class="blog-post-author">ADBC Drivers Contributors</span>
</p>

Today the ADBC Drivers Contributors released updated drivers for Exasol, MySQL, and Snowflake, available immediately via [dbc](https://docs.columnar.tech/dbc/). To update, just `dbc install [exasol|mysql|snowflake]` to get the latest version.

## Updated Drivers

**[Exasol driver](https://github.com/exasol-labs/exarrow-rs) version [0.12.7](https://adbc-drivers.org/drivers/exasol/v0.12.7)**

- Fix empty result sets not carrying the expected schema

**[MySQL driver](https://github.com/adbc-drivers/mysql) version [0.4.0](https://adbc-drivers.org/drivers/mysql/v0.4.0)**

- Support querying unsigned types
- Fix connection exhaustion when rapidly creating and closing connections
- Guard against errors when bulk_ingest is used with zero or >65536 columns

**[Snowflake driver](https://github.com/adbc-drivers/snowflake) version [1.11.0](https://adbc-drivers.org/drivers/snowflake/v1.11.0)**

- Convert between GeoArrow types and GEOMETRY/GEOGRAPHY for both querying and ingest
- Support more Arrow types in bulk ingest as well as specifying the target catalog/schema and compression codec for Parquet files
- Implement GetStatistics
- Support queries that invoke stored procedures via `CALL`
- Improve GetObjects performance
- Various bug fixes

To learn more about how to use the drivers, check out the [documentation](https://adbc-drivers.org/) and [quickstarts](https://github.com/columnar-tech/adbc-quickstarts).

Bug reports and feature requests are welcome at the repositories linked above. You can also start a [Discussion](https://github.com/orgs/adbc-drivers/discussions) on GitHub or join the [Columnar Community Slack](https://join.slack.com/t/columnar-community/shared_invite/zt-3gt5cb69i-KRjJj~mjUZv5doVmpcVa4w).
