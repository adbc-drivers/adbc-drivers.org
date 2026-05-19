---
layout: blog
title: Updated ADBC driver for SQL Server
author: ADBC Drivers Contributors
---

Today the ADBC Drivers Contributors released an updated driver for Microsoft SQL Server, version 1.4.0, available immediately via [dbc](https://docs.columnar.tech/dbc/). To update, just `dbc install mssql` to get the latest version.

Version 1.4.0 has several improvements and bug fixes, including:

- Ingest and query for GEOMETRY/GEOGRAPHY types using GeoArrow extension types
- Control over which Arrow type is used for large string types like NVARCHAR(MAX)
- Fixed support for Kerberos authentication

For more details, see the [full changelog](https://docs.adbc-drivers.org/drivers/mssql/changelog#v1-4-0-2026-05-19). To learn more about how to use the driver, check out the [documentation](https://docs.adbc-drivers.org/drivers/mssql/v1.4.0) and [quickstarts](https://github.com/columnar-tech/adbc-quickstarts).

Bug reports and feature requests are welcome through GitHub Issues in the [`adbc-drivers/mssql` repository](https://github.com/adbc-drivers/mssql). You can also start a [Discussion](https://github.com/orgs/adbc-drivers/discussions) on GitHub or join the [Columnar Community Slack](https://join.slack.com/t/columnar-community/shared_invite/zt-3gt5cb69i-KRjJj~mjUZv5doVmpcVa4w).
