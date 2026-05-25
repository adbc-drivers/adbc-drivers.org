---
layout: blog
title: Updated ADBC driver for Redshift
author: ADBC Drivers Contributors
---

Today the ADBC Drivers Contributors released an updated driver for Amazon Redshift, version 1.3.0, available immediately via [dbc](https://docs.columnar.tech/dbc/). To update, just `dbc install redshift` to get the latest version.

Version 1.3.0 has several improvements and bug fixes, including:

- Support for ingesting GeoArrow data as GEOMETRY/GEOGRAPHY columns
- Inferring/preserving SRID in querying/ingesting geo data
- Fix GetTableSchema only being callable once per connection
- Pass through credentials when executing COPY in bulk ingest
- Map Arrow strings to VARCHAR(MAX) in bulk ingest instead of TEXT

For more details, see the [full changelog](https://docs.adbc-drivers.org/drivers/redshift/changelog#v1-3-0-2026-05-25). To learn more about how to use the driver, check out the [documentation](https://docs.adbc-drivers.org/drivers/redshift/v1.3.0) and [quickstarts](https://github.com/columnar-tech/adbc-quickstarts).

Bug reports and feature requests are welcome through GitHub Issues in the [`adbc-drivers/redshift` repository](https://github.com/adbc-drivers/redshift). You can also start a [Discussion](https://github.com/orgs/adbc-drivers/discussions) on GitHub or join the [Columnar Community Slack](https://join.slack.com/t/columnar-community/shared_invite/zt-3gt5cb69i-KRjJj~mjUZv5doVmpcVa4w).
