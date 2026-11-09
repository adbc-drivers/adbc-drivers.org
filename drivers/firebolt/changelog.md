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

# Changelog for Firebolt Driver

## v0.3.1 (2026-11-09)

## New Features

- Stream query results instead of buffering the full response
- Support Zstandard- and LZ4-compressed Arrow IPC results
- Avoid extra payload copies during bulk ingestion

## Bug Fixes

- Catch exceptions in connection operations to prevent process crashes

## v0.2.0 (2026-10-12)

- Initial release through the ADBC Driver Foundry
