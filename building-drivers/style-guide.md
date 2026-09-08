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

# Style Guide

Miscellaneous recommendations for building drivers that aren't quite part of the API contract, but which are meant to ensure a consistent "look-and-feel" for drivers. This page is meant both for humans and for agents. Agents can use this during code review and development to ensure drivers follow existing conventions.

## Naming

### Option Naming

ADBC option keys should follow this format:

```
vendor[.component].option
```

ADBC option keys should follow these rules:

- ❌ DO NOT start with `adbc.`; we already know this is an ADBC driver.
- ❌ DO NOT contain a ".sql." subpart, unless the option's purpose is actually related to the SQL dialect itself.

Examples:

- ❌ `adbc.bigquery.sql.endpoint`—setting the API endpoint has nothing to do with SQL, and we already know this is an ADBC driver.
- ✔️ `bigquery.endpoint`

#### Common Options

Certain options tend to reocur, but are not part of the ADBC specification. They should have generally consistent names and options:

|Column 1|Column 2|Column 3|
|--------|--------|--------|
|.       |        |        |
|.       |        |        |
|.       |        |        |

### Schema Metadata Key Naming

In metadata of Arrow schemas and fields, keys should follow the Arrow convention[^arrow-metadata-key-convention]:

```
NAMESPACE[:sub_namespace]:property_name
```

Examples:

- ❌ `BIGQUERY:Statistics:TotalBytesProcessed`
- ✔️ `BIGQUERY:statistics:total_bytes_processed`

[^arrow-metadata-key-convention]: While not explicitly documented, it is implied in https://arrow.apache.org/docs/format/Columnar.html#custom-application-metadata and in existing usage.

## Connection URIs

Drivers should support connecting via URI in addition to the native connection string format of the vendor and/or connecting by setting a list of options (in lieu of a single connection string). Such URIs should meet the following requirements:

-
