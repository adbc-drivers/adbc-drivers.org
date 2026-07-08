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

# Changelog for Amazon Redshift Driver

## v1.4.0 (2026-07-07)

Fixes:

- Correctly query decimal values whose decimal representation ended in multiple zeroes

## v1.3.0 (2026-05-25)

New features:

- Add `REDSHIFT:type` metadata on result set schema fields to provide the database's type name
- Preserve SRID in GEOMETRY and GEOGRAPHY columns
- Ingest GeoArrow arrays as GEOMETRY/GEOGRAPHY (this uses a staging table as these types cannot be directly uploaded)

Fixes:

- Ingest Arrow strings as VARCHAR(MAX) instead of TEXT
- Pass credentials to COPY in bulk ingest, when AWS access key/secret key are specified directly
- Fix GetTableSchema only being usable once per connection

## v1.2.1 (2026-03-11)

New features:

- Improve ingest performance by uploading fewer, larger files

## v1.1.0 (2026-01-07)

New features:

- Support IdP token authentication
- Support more options for IdP browser authentication
- Support bind/ingest for Arrow list and struct types (as Redshift SUPER columns)
- Support GEOMETRY, GEOGRAPHY, HLLSKETCH, and SUPER

## v1.0.0 (2025-09-18)

- Initial release
