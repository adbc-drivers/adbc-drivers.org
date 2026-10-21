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

# Changelog for ADBC Driver for Snowflake

## v1.15.1 (2026-10-21)

## Bug Fixes

- Update dependencies to pick up CVE fixes

## v1.15.0 (2026-10-15)

## New Features

- Add `adbc.connection.get_objects.match_exactly` option to disable wildcard matching in GetObjects filters
- Add `adbc.snowflake.sql.client_option.max_retry_count` option to control the maximum number of retries per HTTP request

## Bug Fixes

- Handle backslashes correctly in GetObjects filters
- Limit prefetching based on the number of unconsumed result streams
- Update dependencies to pick up CVE fixes

## v1.14.0 (2026-09-14)

## New Features

- Add `adbc.snowflake.sql.client_option.validate_default_parameters` option to control validation of default connection parameters

## Bug Fixes

- Preserve Snowflake timestamp scale in Arrow and JSON query results
- Detect incompatible source and target schemas during append bulk ingest
- Avoid a potential panic when escaping LIKE patterns

## v1.13.0 (2026-08-18)

## New Features

- Add proxy-specific properties

## Bug Fixes

- Handle UUID data type in metadata paths
- Bump the Go version to pick up CVE fixes

## v1.12.0 (2026-07-31)

## New Features

- Optimize GetObjects metadata query performance

## v1.11.0 (2026-06-18)

## New Features

- Support binding Arrow float16, timestamp, decimal, and binary parameters
- Support specifying the target catalog/schema in bulk ingest
- Add options to choose compression codec in bulk ingest
- Add option to retry failures in reading result set data
- Support querying and ingesting GEOGRAPHY and GEOMETRY types via GeoArrow extension types
- Implement GetStatistics
- Return `xdbc_column_size` for BINARY type columns in GetObjects
- Support ingesting Arrow list, large_list as ARRAY
- Support querying ARRAY as Arrow arrow.json
- Support queries that invoke stored procedures via `CALL`
- Improve GetObjects performance

## Bug Fixes

- Bump the Go version to pick up CVE fixes
- Fix a panic in the record reader if the bind parameter schema did not match the data
- Handle truncated reads and properly return errors
- Fix certain NUMBER columns causing a panic when `use_high_precision` was disabled

## v1.10.3 (2026-03-10)

## Bug Fixes

- Bump the Go version to pick up CVE fixes

## v1.10.1 (2026-01-11)

## Bug Fixes

- Avoid potential deadlocks in the reader

## v1.10.0 (2026-01-07)

## New Features

- Support `snowflake://` URI scheme
- Return the Snowflake version from GetInfo

## Bug Fixes

- Return an UNAUTHORIZED error code for authorization issues
- Handle TIMESTAMP(3) properly
- Sort table columns returned in GetObjects
- Do not error if a schema does not exist in GetObjects
- Return the proper timestamp precision for columns in GetTableSchema
- Do not mix up TIMESTAMP and TIMESTAMP_TZ in ExecuteSchema
