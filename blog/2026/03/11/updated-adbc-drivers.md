---
blogpost: true
date: 2026-03-11
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

# Updated ADBC drivers for BigQuery, MySQL, Oracle Database, Redshift, SQL Server, Snowflake, and Trino

Today the ADBC Drivers Contributors released updated drivers for six database systems, available immediately via [dbc](https://docs.columnar.tech/dbc/). To update, just `dbc install <driver>` to get the latest version.

## Updated Drivers

The newly released drivers, and some release highlights, are:

**[ADBC Driver for BigQuery](/drivers/bigquery/index.md) version 1.11.2**<br>
**[ADBC Driver for Snowflake](/drivers/snowflake/index.md) version 1.10.3**<br>
**[ADBC Driver for Trino](/drivers/trino/index.md) version 0.3.1**

* Update transitive dependencies to pick up security updates. (This is the only change for the three drivers listed above. The drivers listed below also include dependency updates, in addition to other changes detailed separately.)

**[ADBC Driver for Microsoft SQL Server](/drivers/mssql/index.md) version 1.3.1**

* Test against SQL Server 2025.
* Use `NVARCHAR(MAX)` for bulk ingest, not `NTEXT` (which is deprecated).
* Fix a bug where reusing a statement to execute a query after a bulk ingest would give an empty result set.

**[ADBC Driver for MySQL/MariaDB](/drivers/mysql/index.md) version 0.3.1**

* Enable bulk ingest into a temporary table.
* Fix a bug with bulk ingest and wide schemas.

**[ADBC Driver Oracle Database](https://docs.columnar.tech/drivers/oracle) version 0.5.1**

:::{note}
This driver is available from Columnar's private driver registry. See [this blog post](https://columnar.tech/blog/announcing-dbc-0.2.0) to learn more.
:::

* Support `REAL` and `DOUBLE PRECISION` types when the latest Instant Client is used.
* Don't use the `DBA_PDBS` view in GetObjects, which requires more permissions.

**[ADBC Driver for Amazon Redshift](/drivers/redshift/index.md) version 1.2.1**

* Optimize bulk ingest.

To learn more about how to use the drivers, check out the [documentation](/index.md) and [quickstarts](https://github.com/columnar-tech/adbc-quickstarts).

Bug reports and feature requests are welcome at the repositories linked above. You can also start a [Discussion](https://github.com/orgs/adbc-drivers/discussions) on GitHub or join the [Columnar Community Slack](https://join.slack.com/t/columnar-community/shared_invite/zt-3gt5cb69i-KRjJj~mjUZv5doVmpcVa4w).
