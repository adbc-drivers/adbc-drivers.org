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

# Changelog for Trino Driver

## v0.4.0 (2026-06-09)

New features:

- Add `trino.statement.last_query_id` option to retrieve the query ID ([trino#84](https://github.com/adbc-drivers/trino/issues/84))
- Support ADBC's GetStatistics API call
- Support specifying the target catalog/schema for bulk ingest

## v0.3.1 (2026-03-10)

Patch release updating dependencies only.

## v0.3.0 (2026-02-19)

New features:

- Optimize bulk ingest by batching INSERTs accounting for Trino query size limits
- Test and enable Trino UUID and Arrow float16 types
- Add option to bypass TLS certificate validation

## v0.2.0 (2026-02-19)

New features:

- Improve error messages
- Support binding Arrow binary_view and fixed_size_binary types

Fixes:

- Override the HTTP client timeout to prevent spurious timeouts

## v0.1.0 (2025-10-16)

Initial release.
