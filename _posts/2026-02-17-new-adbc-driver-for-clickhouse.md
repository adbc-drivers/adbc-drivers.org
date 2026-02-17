---
layout: blog
title: Preview of a new ADBC driver for ClickHouse
author: ADBC Drivers Contributors
---

The ADBC Drivers Contributors are excited to announce a preview version of a new driver for [ClickHouse](https://clickhouse.com/). The driver is available immediately via [dbc](https://docs.columnar.tech/dbc/). If you have [dbc 0.2.0](https://columnar.tech/blog/announcing-dbc-0.2.0) or newer installed, run `dbc install clickhouse --pre` to try it out today.

The driver supports querying data and can insert Arrow data using an appropriately formatted `INSERT` query. Full ADBC bulk ingestion support is not yet available. Documentation can be found at [docs.adbc-drivers.org](https://docs.adbc-drivers.org/drivers/clickhouse/). This is a preview release, and more features are actively being developed, so stay tuned.

The driver was developed by ClickHouse and uses the [HTTP transport](https://clickhouse.com/docs/interfaces/http) with native Apache Arrow support. To connect, simply provide the `http` or `https` URL of your ClickHouse server as the `uri` option. See the [HTTP interface documentation](https://clickhouse.com/docs/interfaces/http#overview) for more details.

To get started, check out the [ADBC Quickstarts](https://github.com/columnar-tech/adbc-quickstarts) repository for runnable examples demonstrating the ClickHouse driver in C++, Go, Java, Python, R, and Rust.

Please submit bug reports and feature requests directly to the [adbc_clickhouse](https://github.com/ClickHouse/adbc_clickhouse) repository. You can also start a [Discussion](https://github.com/orgs/adbc-drivers/discussions) on GitHub or connect with us on the [Columnar Community Slack](https://join.slack.com/t/columnar-community/shared_invite/zt-3gt5cb69i-KRjJj~mjUZv5doVmpcVa4w).
