---
layout: blog
title: Updated ADBC drivers for BigQuery, SQL Server, MySQL, Redshift, Snowflake, and Trino
author: ADBC Drivers Contributors
---

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

Additionally, all drivers now support connecting with URIs in addition to their native connection string formats. To learn more about how to use the drivers, check out the [documentation](https://docs.adbc-drivers.org/) and [quickstarts](https://github.com/columnar-tech/adbc-quickstarts).

Bug reports and feature requests are welcome at the repositories linked above. You can also start a [Discussion](https://github.com/orgs/adbc-drivers/discussions) on GitHub or join the [Columnar Community Slack](https://join.slack.com/t/columnar-community/shared_invite/zt-3gt5cb69i-KRjJj~mjUZv5doVmpcVa4w).
