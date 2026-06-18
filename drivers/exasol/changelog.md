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

# Changelog for Exasol Driver

For full details, see the [upstream changelog](https://github.com/exasol-labs/exarrow-rs/blob/main/CHANGELOG.md).

## v0.12.7 (2026-06-18)

Fixes:

- Preserve the schema of empty result sets

## v0.12.6 (2026-06-08)

Fixes:

- If a nonexistent schema is specified in the connection URI, the driver will still connect instead of failing
- `?` characters inside string literals, quoted identifiers, and comments are no longer treated as bind parameter placeholders
- Multi-value `WHERE col IN (...)` now properly returns all matching rows
- Apply the `query_timeout` connection parameter to all statements
- Update dependencies with security advisories (see the [upstream changelogs](https://github.com/exasol-labs/exarrow-rs/releases) for details)

## v0.12.0 (2026-04-30)

New features:

- Use the native TCP transport instead of WebSocket by default for improved performance
- Improve result set parsing performance
- Directly upload Parquet data when importing (instead of converting to CSV)
  - Issue `OPEN SCHEMA` if a schema is present in the connection URI (`exasol://u:p@localhost:8563/my_schema`)

## v0.9.0 (2026-04-16)

New features:

- Add support for validating TLS certificate fingerprints
- Add support for 1024-bit RSA public keys during login (used by some instances, e.g. `demodb.exasol.com`)
- {{BREAKING_CHANGE}} Default to `tls=true` in connections to match Exasol 7.1+

Fixes:

- Update dependencies with security advisories (see the [upstream changelog](https://github.com/exasol-labs/exarrow-rs/releases/tag/v0.7.3) for details)

## v0.7.0 (2026-03-20)

New features:

- Add support for GetObjects
- Add support for GetParameterSchema
- Add support for GetTableSchema
- Add support for transactions
- Add support for getting the current catalog

Fixes:

- Fix support for large result sets

## v0.6.3 (2026-03-03)

- Initial release supporting query execution
