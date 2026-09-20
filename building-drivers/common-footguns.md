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

# Development Footguns

An assorted list of footguns we've run into during development. This list is intended to help you (and your agents) during development and code review.

- Go: it's easy to have the schema and data for record readers not match. Tests should validate that the schema of the _reader_ matches the expectation and that the schema of the _reader_ and the _record batch_ matches. (Example: [bigquery#303](https://github.com/adbc-drivers/bigquery/pull/303#discussion_r4032908603))
  - This is a common footgun in general in Arrow implementations.
