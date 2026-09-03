---
# Copyright (c) 2026 ADBC Drivers Contributors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
{}
---

# Changelog for ClickHouse Driver

See the [upstream
changelog](https://github.com/ClickHouse/adbc_clickhouse/blob/main/CHANGELOG.md)
in `ClickHouse/adbc_clickhouse` for full details.

(clickhouse-v0-1-1)=
## v0.1.1 (2026-09-03)

See [v0.1.1](https://github.com/ClickHouse/adbc_clickhouse/blob/main/CHANGELOG.md#011---2026-08-31) upstream.

New features:

- Add `clickhouse.setting.<setting_name>` options to sets arbitrary ClickHouse settings
- Treat query parameters (besides `protocol`, `database`) in the connection URI as ClickHouse settings
- Add the ability to retrieve `clickhouse.client.session_id` from a connection
- Add the ability to configure the default database of a connection

Fixed:

- Send SQL queries to the server verbatim, instead of treating `?` as a bind parameter

## v0.1.0 (2026-07-06)

See [v0.1.0](https://github.com/ClickHouse/adbc_clickhouse/blob/main/CHANGELOG.md#010---2026-07-01) upstream.

- Initial release.
