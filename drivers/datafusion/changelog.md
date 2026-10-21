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

# Changelog for ADBC Driver for Apache DataFusion

## v0.28.0 (2026-10-21)

## New Features

- Bump DataFusion to 55.2

## Bug Fixes

- Preserve original column ordinal positions in `GetObjects` when filtering columns.
- Fix bulk-ingestion appends for table, schema, and catalog names containing mixed case or special characters.

## v0.27.0 (2026-09-02)

## New Features

- Bump DataFusion to 55

## Bug Fixes

- Cast bind parameters to the expected type

## v0.26.0 (2026-07-07)

## New Features

- Implement `ExecutePartitions` and `ReadPartition`

## v0.25.0 (2026-06-08)

## New Features

- Enable direct querying of HTTP/S3/etc. URIs and local files/directories in the same way as `datafusion-cli`

## v0.24.1 (2026-05-27)

## New Features

- Support bind parameters
- Enable ADBC ExecuteSchema, GetTableSchema, Prepare API calls
- Improve error messages
- Add support for bulk ingest modes

## Bug Fixes

- Share a context between connections
- Stream results instead of materializing them
- Remove various calls to `unwrap`
