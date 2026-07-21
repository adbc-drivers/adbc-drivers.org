---
blogpost: true
date: 2026-01-12
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

# Updated ADBC drivers for SQL Server and Snowflake

<p class="blog-post-meta">
  <time datetime="2026-01-12">January 12, 2026</time>
  <span class="blog-post-author">ADBC Drivers Contributors</span>
</p>

Today the ADBC Drivers Contributors released updated drivers for two database systems, available immediately via [dbc](https://docs.columnar.tech/dbc/). To update, just `dbc install <driver>` to get the latest version.

## Updated Drivers

The newly released drivers, and some release highlights, are:

### [Microsoft SQL Server driver](http://github.com/adbc-drivers/mssql) version 1.2.0
* Add support for Entra ID authentication.  To use it, [install the Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli?view=azure-cli-latest), log in via `az login`, and add `fedauth=` to your connection URI, like so:

  <!-- allow wrapping -->
  `sqlserver://my-database-endpoint.database.windows.net:1433?database=my-database-name&fedauth=ActiveDirectoryDefault`

  See the [documentation](https://adbc-drivers.org/drivers/mssql/v1.2.0.html#connection-string-format) for more information.

### [Snowflake driver](https://github.com/adbc-drivers/snowflake) version 1.10.1
* Fix occasional deadlocks when reading data ([bug report](https://github.com/apache/arrow-adbc/issues/3730))

Bug reports and feature requests are welcome at the repositories linked above. You can also start a [Discussion](https://github.com/orgs/adbc-drivers/discussions) on GitHub or join the [Columnar Community Slack](https://join.slack.com/t/columnar-community/shared_invite/zt-3gt5cb69i-KRjJj~mjUZv5doVmpcVa4w).
