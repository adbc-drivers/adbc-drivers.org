---
layout: blog
title: Updated ADBC drivers for ClickHouse and SQL Server
author: ADBC Drivers Contributors
---

Today the ADBC Drivers Contributors released updated drivers for ClickHouse and Microsoft SQL Server, available immediately via [dbc](https://docs.columnar.tech/dbc/). To update, just `dbc install mssql` or `dbc install clickhouse --pre` to get the latest version.

## Updated Drivers

The new drivers are patch releases to fix reported bugs.

**[ClickHouse driver](https://docs.adbc-drivers.org/drivers/clickhouse) version 0.1.0-alpha.2**

* Enable TLS support at build time.

**[Microsoft SQL Server driver](http://docs.adbc-drivers.org/drivers/mssql) version 1.4.1**

* Restore support for querying IMAGE, SMALLDATETIME, UNIQUEIDENTIFIER, and XML columns

To learn more about how to use the drivers, check out the [documentation](https://docs.adbc-drivers.org/) and [quickstarts](https://github.com/columnar-tech/adbc-quickstarts).

Bug reports and feature requests are welcome at the repositories linked above. You can also start a [Discussion](https://github.com/orgs/adbc-drivers/discussions) on GitHub or join the [Columnar Community Slack](https://join.slack.com/t/columnar-community/shared_invite/zt-3gt5cb69i-KRjJj~mjUZv5doVmpcVa4w).
