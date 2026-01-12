---
layout: blog
title: Updated ADBC drivers for SQL Server and Snowflake
author: ADBC Drivers Contributors
---

Today the ADBC Drivers Contributors released updated drivers for two database systems, available immediately via [dbc](https://docs.columnar.tech/dbc/). To update, just `dbc install <driver>` to get the latest version.

## Updated Drivers

The newly released drivers, and some release highlights, are:

### [Microsoft SQL Server driver](http://github.com/adbc-drivers/mssql) version 1.2.0
* Add support for EntraID authentication

### [Snowflake driver](https://github.com/adbc-drivers/snowflake) version 1.10.1
* Fix occasional deadlocks when reading data ([bug report](https://github.com/apache/arrow-adbc/issues/3730))

Bug reports and feature requests are welcome at the repositories linked above. You can also start a [Discussion](https://github.com/orgs/adbc-drivers/discussions) on GitHub or join the [Columnar Community Slack](https://join.slack.com/t/columnar-community/shared_invite/zt-3gt5cb69i-KRjJj~mjUZv5doVmpcVa4w).
