---
layout: blog
title: New ADBC driver for Exasol
author: ADBC Drivers Contributors
---

The ADBC driver for [Exasol](https://www.exasol.com/), version 0.7.0, is now available via [dbc](https://docs.columnar.tech/dbc/). Just `dbc install exasol` to get the latest version.

The driver supports query execution and inspecting the catalog (GetObjects, GetTableSchema, etc.); features like bulk ingestion and bind parameters are in the works. Documentation can be found at [docs.adbc-drivers.org](http://docs.adbc-drivers.org/drivers/exasol/). The Exasol Labs community is still working on adding more features and tuning performance, so check back for updates.

This driver is developed by the [Exasol Labs 🧪](https://github.com/exasol-labs) community initiative. Bug reports and feature requests are welcome through [GitHub Issues in the `exarrow-rs` repository](https://github.com/exasol-labs/exarrow-rs) under Exasol Labs. You can also start a [Discussion](https://github.com/orgs/adbc-drivers/discussions) on GitHub or join the [Columnar Community Slack](https://join.slack.com/t/columnar-community/shared_invite/zt-3gt5cb69i-KRjJj~mjUZv5doVmpcVa4w).
