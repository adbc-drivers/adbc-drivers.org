---
blogpost: true
date: 2026-05-22
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

# Updated ADBC drivers for ClickHouse and SQL Server

<p class="blog-post-meta">
  <time datetime="2026-05-22">May 22, 2026</time>
  <span class="blog-post-author">ADBC Drivers Contributors</span>
</p>

Today the ADBC Drivers Contributors released updated drivers for ClickHouse and Microsoft SQL Server, available immediately via [dbc](https://docs.columnar.tech/dbc/). To update, just `dbc install mssql` or `dbc install clickhouse --pre` to get the latest version.

## Updated Drivers

The new drivers are patch releases to fix reported bugs.

**[ClickHouse driver](https://adbc-drivers.org/drivers/clickhouse) version 0.1.0-alpha.2**

* Enable TLS support at build time.

**[Microsoft SQL Server driver](https://adbc-drivers.org/drivers/mssql) version 1.4.1**

* Restore support for querying IMAGE, SMALLDATETIME, UNIQUEIDENTIFIER, and XML columns

To learn more about how to use the drivers, check out the [documentation](https://adbc-drivers.org/) and [quickstarts](https://github.com/columnar-tech/adbc-quickstarts).

Bug reports and feature requests are welcome at the repositories linked above. You can also start a [Discussion](https://github.com/orgs/adbc-drivers/discussions) on GitHub or join the [Columnar Community Slack](https://join.slack.com/t/columnar-community/shared_invite/zt-3gt5cb69i-KRjJj~mjUZv5doVmpcVa4w).
