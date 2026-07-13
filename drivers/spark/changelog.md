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

# Changelog for Apache Spark Driver

## v0.1.0-alpha.3 (2026-07-10)

New features:

- Add the `spark.ingest.location` option to specify the LOCATION clause for CREATE TABLE in bulk ingest
- Improve compatibility with Spark Connect on Amazon EMR
- Improve compatibility with Livy on Amazon EMR

Fixes:

- Properly release Spark Connect sessions on disconnect
- Accept `auth_type=none` for Livy
- Accept no username with Spark Connect when `auth_type=none`

## v0.1.0-alpha.2 (2026-06-02)

- Initial release
