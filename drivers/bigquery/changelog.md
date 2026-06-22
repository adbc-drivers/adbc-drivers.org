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

# Changelog for BigQuery Driver

## v1.12.0 (2026-06-22)

New features:

- Make option names more consistent (allow `bigquery.foo` in addition to `adbc.bigquery.sql.foo`)
- Allow overriding the gRPC endpoint for the BigQuery Storage Read API to enable (in theory) connecting to the BigQuery emulator
- Add query statistics to the schema metadata of the result
- Implement GetStatistics

Fixes:

- Add the SRID to returned GeoArrow metadata
- Allow binding Arrow time[ns] values by truncating
- Auto-detect the credential type from JSON credentials
- Improve error handling around authentication
- Handle dry-run queries properly instead of erroring
- Process the connection URI first to avoid potential nondeterminism in connection options

## v1.11.2 (2026-03-10)

Fixes:

- Handle cancellation during bulk ingest better

## v1.11.0 (2026-02-19)

New features:

- Add experimental support for using the BigQuery Storage Write API for bulk ingest
- Improve read performance by enabling Arrow compression

Fixes:

- Wait for table existence to propagate in bulk ingest

## v1.10.0 (2026-01-07)

:::{note}
The version number was bumped to align with the upstream arrow-adbc release.
:::

New features:

- Support `bigquery://` connection URIs
- Add `BIGQUERY:type` field metadata to note the original database type
- Support setting the quota project for a connection
- Support bulk ingest of list and struct types

Fixes:

- Work around hanging due to infinite retries in Google SDKs
- Always return `decimal256(76,38)` for BIGDECIMAL columns

## v1.0.0 (2025-09-17)

New features:

- Support service account impersonation
- Allow specifying the BigQuery location
- Error gracefully if the user lacks `roles/bigquery.readSessionUser` to use BigQuery Storage Read API
- Enable bulk ingest into a specified project/dataset (catalog/schema)
- Tag GEOGRAPHY columns with GeoArrow extension metadata

Fixes:

- Put extension type metadata on the child in the case of nested types (like array-of-geography)
- Export `AdbcDriverBigQueryInit` for backwards compatibility and ``AdbcDriverBigqueryInit` for driver managers
- Always return `decimal128(38,9)` and ignore the declared precision/scale (which is not used for result data)
