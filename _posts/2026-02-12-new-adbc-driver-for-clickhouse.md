---
layout: blog
title: Preview of a new ADBC driver for ClickHouse
author: ADBC Drivers Contributors
---

Today the ADBC Drivers Contributors released a preview of a new driver for [ClickHouse](https://clickhouse.com/), available immediately via [dbc](https://docs.columnar.tech/dbc/). If you have [dbc 0.2.0](https://columnar.tech/blog/announcing-dbc-0.2.0) or newer, run `dbc install clickhouse --pre` to try it out today.

The driver supports querying data; it does not support ADBC bulk ingestion, but can insert Arrow data with an appropriately formatted `INSERT` query. Documentation can be found at [docs.adbc-drivers.org](https://docs.adbc-drivers.org/drivers/clickhouse/). Again, this is a preview release, and ClickHouse is still working on adding more features, so stay tuned.

This driver was developed by ClickHouse themselves and uses the [HTTP transport](https://clickhouse.com/docs/interfaces/http) with native Apache Arrow support. To connect, use the `http` or `https` URL for your ClickHouse server as the `uri` option.  See the [documentation](https://clickhouse.com/docs/interfaces/http#overview) for the HTTP interface for details.

Please submit bug reports and feature requests to ClickHouse directly at [adbc_clickhouse](https://github.com/ClickHouse/adbc_clickhouse). You can also start a [Discussion](https://github.com/orgs/adbc-drivers/discussions) on GitHub or join the [Columnar Community Slack](https://join.slack.com/t/columnar-community/shared_invite/zt-3gt5cb69i-KRjJj~mjUZv5doVmpcVa4w).
