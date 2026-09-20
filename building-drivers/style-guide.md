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

:::{workinprogress}
:::

This style guide provides miscellaneous recommendations for building drivers that aren't quite part of the API contract, but which are meant to ensure a consistent "look-and-feel" for drivers. This page is meant both for humans and for agents. Agents can use this during code review and development to ensure drivers follow existing conventions.

## Naming Conventions

### Option Naming

ADBC option keys should follow this format:

```
vendor[.components].option
```

Rationale: the `vendor.` prefix differentiates the option from other drivers' options and from those defined by ADBC itself. The ADBC spec uses unprefixed option names (like `uri`) so this prevents conflicts.

ADBC option keys should follow these rules:

- MUST NOT start with `adbc.`; we already know this is an ADBC driver.
- SHOULD NOT contain a ".sql." subpart, unless the option's purpose is actually related to the SQL dialect itself.

Examples:

- ❌ `adbc.bigquery.sql.endpoint`—setting the API endpoint has nothing to do with SQL, and we already know this is an ADBC driver.
- ✔️ `bigquery.endpoint`

### Schema Metadata Key Naming

In metadata of Arrow schemas and fields, keys should follow the Arrow convention [^arrow-metadata-key-convention]:

```
NAMESPACE[:sub_namespace]:property_name
```

Examples:

- ❌ `BIGQUERY:Statistics:TotalBytesProcessed`
- ✔️ `BIGQUERY:statistics:total_bytes_processed`

[^arrow-metadata-key-convention]: While not explicitly documented, it is implied in https://arrow.apache.org/docs/format/Columnar.html#custom-application-metadata and in existing usage.

## Connection URIs

Drivers should support connecting via URI in addition to the native connection string format of the vendor and/or connecting by setting a list of options (in lieu of a single connection string).

Such URIs should follow these rules:

- MUST accept the scheme with the same name as the driver (e.g. the BigQuery driver must support `bigquery://`).
  - MAY accept other schemes.
  - SHOULD accept other schemes that are commonly supported by the vendor. (For example, `sc://` for Spark Connect in addition to `spark://`.)
- SHOULD accept connection options via query parameters, in addition to AdbcDatabase options.
  - SHOULD keep names consistent between query parameters and options.
  - If both are present, AdbcDatabase options SHOULD take precedence.

Rationale: ADBC driver managers generally can infer the driver name from the URI option, if given, so supporting URIs makes it easy for users to get started without having to specify more options to name the specific driver.

## Behavioral Conventions

- Connections should be secure by default: TLS (or the equivalent) should be opt-out, not opt-in.

### Common Options

Certain options tend to reocur, but are not part of the ADBC specification. They should have generally consistent names and option values:

:::{workinprogress}
:::
