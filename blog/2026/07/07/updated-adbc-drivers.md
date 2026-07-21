---
blogpost: true
date: 2026-07-07
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

# Updated ADBC drivers for Amazon Redshift, Apache DataFusion, and Microsoft SQL Server

<p class="blog-post-meta">
  <time datetime="2026-07-07">July 07, 2026</time>
  <span class="blog-post-author">ADBC Drivers Contributors</span>
</p>

Today the ADBC Drivers Contributors released updated drivers for Amazon Redshift, Apache DataFusion, and Microsoft SQL Server, available immediately via [dbc](https://docs.columnar.tech/dbc/). To update, just `dbc install [redshift|datafusion|mssql]` to get the latest version.

## Updated Drivers

**[Amazon Redshift driver](https://github.com/adbc-drivers/amazon) version [1.4.0](https://adbc-drivers.org/drivers/redshift/v1.4.0)**

- Correctly query decimal values whose decimal representation ended in multiple zeroes

**[Apache DataFusion driver](https://github.com/adbc-drivers/datafusion) version [0.26.0](https://adbc-drivers.org/drivers/datafusion/v0.26.0)**

- Implement `ExecutePartitions` and `ReadPartition`

**[Microsoft SQL Server driver](https://github.com/adbc-drivers/microsoft) version [1.5.0](https://adbc-drivers.org/drivers/mssql/v1.5.0)**

- Add support for Microsoft Fabric Data Warehouse, including ingest support, OneLake support, `INSERT BULK`, and compatibility improvements
- Add support for querying, binding, and ingesting `SQL_VARIANT`
- **Breaking change:** `geoarrow.wkb` ingest now uses `GEOGRAPHY` only when an SRID and `"edges":"spherical"` are defined; see `mssql.ingest.geo_type`
- Fix typos in `INSERT BULK` support

To learn more about how to use the drivers, check out the [documentation](https://adbc-drivers.org/) and [quickstarts](https://github.com/columnar-tech/adbc-quickstarts).

Bug reports and feature requests are welcome at the repositories linked above. You can also start a [Discussion](https://github.com/orgs/adbc-drivers/discussions) on GitHub or join the [Columnar Community Slack](https://join.slack.com/t/columnar-community/shared_invite/zt-3gt5cb69i-KRjJj~mjUZv5doVmpcVa4w).
