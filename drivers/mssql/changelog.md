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

# Changelog for Microsoft SQL Server Driver

## v1.3.1 (2026-03-11)

Fixes:

- Ingest string columns as `NVARCHAR(MAX)` (instead of the deprecated `NTEXT`)
- Fix a bug where reusing a statement to execute a query after a bulk ingest would give an empty result set

## v1.3.0 (2026-02-19)

New features:

- Improve query performance by optimizing the underlying [microsoft/go-mssqldb](https://github.com/microsoft/go-mssqldb) library[^opt-1.3.0]

## v1.2.0 (2026-01-12)

New features:

- Add support for Microsoft Entra ID authentication

## v1.1.0 (2026-01-07)

New features:

- Add support for querying DATETIME2, CHAR/NCHAR types
- Add for binding/ingesting Arrow large/view/fixed-size string and binary types

## v1.0.0 (2025-09-18)

- Initial release

[^opt-1.3.0]: https://columnar.tech/blog/adbc-driver-optimization-deep-dive
