---
blogpost: true
date: 2026-11-09
author: ADBC Drivers Contributors
hide-toc: true
orphan: true
---

<!--
  Copyright (c) 2026 ADBC Drivers Contributors

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

# Updated ADBC drivers for ClickHouse and Exasol

The ADBC Drivers Contributors have released an update to drivers for ClickHouse and Exasol. Both are available now via [dbc](https://docs.columnar.tech/dbc/).

To update, run `dbc install <driver>`.

## Updated Drivers

**[ADBC Driver for ClickHouse](https://github.com/ClickHouse/adbc_clickhouse) version [v0.1.2](/drivers/clickhouse/v0.1.2.md)**

- Add driver build for Windows/arm64
- GetTableSchema now returns decimal128, matching the server
- Fix `decompression error: incorrect magic number` against ClickHouse 26.9+

**[ADBC Driver for Exasol](https://github.com/exasol-labs/exarrow-rs) version [v0.32.0](/drivers/exasol/v0.32.0.md)**

- Bump exarrow-rs to v0.32.0

To learn more about any of these drivers, check out the [documentation](/index.md) and [quickstarts](https://github.com/columnar-tech/adbc-quickstarts).

Bug reports and feature requests are welcome at the repositories linked above. You can also start a [Discussion](https://github.com/orgs/adbc-drivers/discussions) on GitHub or join the [Columnar Community Slack](https://join.slack.com/t/columnar-community/shared_invite/zt-3gt5cb69i-KRjJj~mjUZv5doVmpcVa4w).
