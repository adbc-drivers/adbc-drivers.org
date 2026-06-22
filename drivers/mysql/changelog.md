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

# Changelog for MySQL/MariaDB Driver

## v0.4.0 (2026-06-18)

New features:

- Support querying unsigned types

Fixes:

- Guard against zero columns, >65536 columns in bulk ingest
- Disable underlying connection pooling to avoid connection exhaustion

## v0.3.1 (2026-03-11)

New features:

- Enable bulk ingest into temporary tables

Fixes:

- Cap the size of batched INSERTS in bulk ingest, fixing a bug with wide tables

## v0.3.0 (2026-02-19)

New features:

- Improve bulk ingest performance by batching INSERT statements[^opt-0.3.0]

[^opt-0.3.0]: https://columnar.tech/blog/adbc-driver-optimization-deep-dive

## v0.2.0 (2026-01-07)

New features:

- Support querying the `BIT` type
- Force connection timezone to UTC for consistent handling

## v0.1.0 (2025-09-18)

- Initial release
