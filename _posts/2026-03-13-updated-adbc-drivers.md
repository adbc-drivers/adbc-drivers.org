---
layout: blog
title: Updated ADBC drivers for BigQuery, MySQL, Oracle Database, Redshift, SQL Server, Snowflake, and Trino
author: ADBC Drivers Contributors
---

Today the ADBC Drivers Contributors released updated drivers for six database systems, available immediately via [dbc](https://docs.columnar.tech/dbc/). To update, just `dbc install <driver>` to get the latest version.

## Updated Drivers

The newly released drivers, and some release highlights, are:

**[Google BigQuery driver](https://github.com/adbc-drivers/bigquery) version 1.11.2** \\
**[Snowflake driver](https://github.com/adbc-drivers/snowflake) version 1.10.3** \\
**[Trino driver](https://github.com/adbc-drivers/trino) version 0.3.1**

* Update transitive dependencies to pick up security updates. (This also applies to all drivers below.)

**[Microsoft SQL Server driver](http://github.com/adbc-drivers/mssql) version 1.3.1**

* Test against SQL Server 2025.
* Use `NVARCHAR(MAX)` for bulk ingest, not `NTEXT` (which is deprecated).
* Fix a bug where reusing a statement to execute a query after a bulk ingest would give an empty result set.

**[MySQL driver](https://github.com/adbc-drivers/mysql) version 0.3.1**

* Enable bulk ingest into a temporary table.
* Fix a bug with bulk ingest and wide schemas.

**Oracle Database driver version 0.5.1**

_Note: this driver is part of Columnar's private driver registry. See [this blog post](https://columnar.tech/blog/announcing-dbc-0.2.0) to learn more._

* Support `REAL` and `DOUBLE PRECISION` types when the latest Instant Client is used.
* Don't use the `DBA_PDBS` view in GetObjects, which requires more permissions.

**[Amazon Redshift driver](https://github.com/adbc-drivers/redshift/) version 1.2.1**

* Optimize bulk ingest.

To learn more about how to use the drivers, check out the [documentation](https://docs.adbc-drivers.org/) and [quickstarts](https://github.com/columnar-tech/adbc-quickstarts).

Bug reports and feature requests are welcome at the repositories linked above. You can also start a [Discussion](https://github.com/orgs/adbc-drivers/discussions) on GitHub or join the [Columnar Community Slack](https://join.slack.com/t/columnar-community/shared_invite/zt-3gt5cb69i-KRjJj~mjUZv5doVmpcVa4w).
