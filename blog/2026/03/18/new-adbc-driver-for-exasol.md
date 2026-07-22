---
blogpost: true
date: 2026-03-18
author: ADBC Drivers Contributors
hide-toc: true
orphan: true
---

<!--
  Copyright (c) 2025-2026 ADBC Drivers Contributors

  Licensed under the Apache License, Version 2.0 (the "License");
  you may not use this file except in compliance with the License.
  You may obtain a copy of the License at

          http://www.apache.org/licenses/LICENSE-2.0

  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License.
-->

# New ADBC driver for Exasol

<p class="blog-post-meta">
  <time datetime="2026-03-18">March 18, 2026</time>
  <span class="blog-post-author">ADBC Drivers Contributors</span>
</p>

The ADBC driver for [Exasol](https://www.exasol.com/), version 0.7.0, is now available via [dbc](https://docs.columnar.tech/dbc/). Just `dbc install exasol` to get the latest version.

The driver supports query execution and inspecting the catalog (GetObjects, GetTableSchema, etc.); features like bulk ingestion and bind parameters are in the works. Documentation can be found at [adbc-drivers.org](https://adbc-drivers.org/drivers/exasol/). The Exasol Labs community is still working on adding more features and tuning performance, so check back for updates.

This driver is developed by the [Exasol Labs 🧪](https://github.com/exasol-labs) community initiative. Bug reports and feature requests are welcome through [GitHub Issues in the `exarrow-rs` repository](https://github.com/exasol-labs/exarrow-rs) under Exasol Labs. You can also start a [Discussion](https://github.com/orgs/adbc-drivers/discussions) on GitHub or join the [Columnar Community Slack](https://join.slack.com/t/columnar-community/shared_invite/zt-3gt5cb69i-KRjJj~mjUZv5doVmpcVa4w).
