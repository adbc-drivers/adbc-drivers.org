---
blogpost: true
date: 2026-07-31
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

# Updated ADBC drivers for Amazon Redshift, Microsoft SQL Server, Snowflake, and Trino

<p class="blog-post-meta">
  <time datetime="2026-07-31">July 31, 2026</time>
  <span class="blog-post-author">ADBC Drivers Contributors</span>
</p>

Today the ADBC Drivers Contributors released updates to drivers for Amazon Redshift, Microsoft SQL Server, Snowflake, and Trino. All are available now via [dbc](https://docs.columnar.tech/dbc/).

## Updated Drivers

**[Amazon Redshift ADBC driver](https://github.com/adbc-drivers/redshift) version [1.5.0](/drivers/redshift/v1.5.0.md)**

- Support dictionary-encoded bind parameters and the Arrow null type
- Make VARBYTE size configurable and increase default size for GeoArrow data staged as VARBYTE in bulk ingest
- Support server-side statement cancellation

**[Microsoft SQL Server ADBC driver](https://github.com/adbc-drivers/mssql) version [1.6.0](/drivers/mssql/v1.6.0.md)**

- Support dictionary/null binding
- Implement experimental trace propagation

**[Snowflake ADBC driver](https://github.com/adbc-drivers/snowflake) version [1.12.0](/drivers/snowflake/v1.12.0.md)**

- Optimize GetObjects metadata query performance

**[Trino ADBC driver](https://github.com/adbc-drivers/trino) version [0.5.1](/drivers/trino/v0.5.1.md)**

- Update dependencies

To learn more about any of these drivers, check out the [documentation](/index.md) and [quickstarts](https://github.com/columnar-tech/adbc-quickstarts).

Bug reports and feature requests are welcome at the repositories linked above. You can also start a [Discussion](https://github.com/orgs/adbc-drivers/discussions) on GitHub or join the [Columnar Community Slack](https://join.slack.com/t/columnar-community/shared_invite/zt-3gt5cb69i-KRjJj~mjUZv5doVmpcVa4w).
