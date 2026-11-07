---
# Copyright (c) 2026 ADBC Drivers Contributors
# Copyright (c) 2026 lefred - MariaDB Foundation
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

# Changelog for MariaDB Driver

For full details, see the [upstream releases](https://github.com/adbc-drivers/mariadb/releases).

## v0.1.6 (2026-11-06)

- Update Go and dependencies.
- Update release and validation workflows.

## v0.1.5 (2026-10-20)

- Export the `AdbcDriverMariadbInit` entrypoint.
- Accept native Go DSNs containing a password.
- Update dependencies and validation expectations.

## v0.1.4 (2026-07-17)

- Support `ST_GeomFromWKB` during bulk ingestion.

## v0.1.3 (2026-07-16)

- Add transaction isolation levels and parameter schema discovery.

## v0.1.2 (2026-07-16)

- Add statistics support.

## v0.1.1 (2026-07-16)

- Add transaction support.

## v0.1.0 (2026-07-15)

- Initial release.
