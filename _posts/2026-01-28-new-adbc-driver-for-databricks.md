---
layout: blog
title: New ADBC driver for Databricks
author: ADBC Drivers Contributors
---

Today the ADBC Drivers Contributors released a new driver for Databricks version 0.1.2, available immediately via [dbc](https://docs.columnar.tech/dbc/). Just `dbc install databricks` to get the latest version.

The driver supports querying data, bulk ingestion, and querying the catalog (listing tables and columns and so on). Documentation can be found at [docs.adbc-drivers.org](http://docs.adbc-drivers.org/drivers/databricks/). As the version number implies, this is an early version of the driver.  We are still working with Databricks on adding more features and improving performance, so stay tuned.

This driver uses Databricks's Thrift transport with Cloud Fetch and Apache Arrow data transfer enabled.  It can connect to serverless compute, provisioned ("classic") compute, and SQL warehouses, by setting the server hostname, port, and HTTP path appropriately.  See the [documentation](https://docs.databricks.com/dev-tools/go-sql-driver) for the official Go SDK for details on how to get these values.

Bug reports and feature requests are welcome at the repositories linked above. You can also start a [Discussion](https://github.com/orgs/adbc-drivers/discussions) on GitHub or join the [Columnar Community Slack](https://join.slack.com/t/columnar-community/shared_invite/zt-3gt5cb69i-KRjJj~mjUZv5doVmpcVa4w).
