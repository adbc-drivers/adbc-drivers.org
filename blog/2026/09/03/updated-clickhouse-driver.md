---
blogpost: true
date: 2026-09-03
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

# Updated ADBC driver for ClickHouse

Today the ADBC Drivers Contributors released an updated driver for ClickHouse, version 0.1.1, available immediately via [dbc](https://docs.columnar.tech/dbc/). To update, just `dbc install clickhouse` to get the latest version.

Version 0.1.1 has several improvements and bug fixes, including:
- Set the default database and ClickHouse settings on connect
- Set ClickHouse settings after connection
- No more interpretation of `?` and `??` tokens in queries (queries are sent verbatim)

For more details, see the [full changelog](clickhouse-v0-1-1). To learn more about how to use the driver, check out the [documentation](/drivers/clickhouse/v0.1.1.md) and [quickstarts](https://github.com/columnar-tech/adbc-quickstarts).

Please submit bug reports and feature requests directly to the [adbc_clickhouse](https://github.com/ClickHouse/adbc_clickhouse) repository. You can also start a [Discussion](https://github.com/orgs/adbc-drivers/discussions) on GitHub or connect with us on the [Columnar Community Slack](https://join.slack.com/t/columnar-community/shared_invite/zt-3gt5cb69i-KRjJj~mjUZv5doVmpcVa4w).
