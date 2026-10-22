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

# Databricks

:::{toctree}
:maxdepth: 1
:hidden:

Changelog <changelog.md>
v0.3.0 <v0.3.0.md>
v0.2.0 <v0.2.0.md>
v0.1.3 <v0.1.3.md>
v0.1.2 <v0.1.2.md>
:::

[{badge-primary}`Driver Version|v0.3.0`](#driver-databricks-v0.3.0 "Permalink") {badge-secondary}`Release Date|2026-10-22` {badge-success}`Tested With|Databricks 17`

This driver provides access to [Databricks][databricks], a
cloud-based platform for data analytics.

:::{note}
This is an early version of the driver, and contributors are still
working with Databricks to expand the featureset and improve performance.
:::

## Installation

The Databricks driver can be installed with [dbc](https://docs.columnar.tech/dbc):

```bash
dbc install databricks
```

## Connecting

To connect, edit the `uri` option below to match your environment and run the following:

```python
from adbc_driver_manager import dbapi

conn = dbapi.connect(
    driver="databricks",
    db_kwargs={
        "uri": "databricks://token:dapi1234abcd5678efgh@dbc-a1b2345c-d6e7.cloud.databricks.com:443/sql/protocolv1/o/1234567890123456/1234-567890-abcdefgh"
    },
)
```

Note: The example above is for Python using the [adbc-driver-manager](https://pypi.org/project/adbc-driver-manager) package but the process will be similar for other driver managers.

### Connection String Format

Databricks's URI syntax supports three primary forms:

1. Databricks personal access token authentication:

   ```
   databricks://token:<personal-access-token>@<server-hostname>:<port-number>/<http-path>?<param1=value1>&<param2=value2>
   ```

   Components:
   - `scheme`: `databricks://` (required)
   - `<personal-access-token>`: (required) Databricks personal access token.
   - `<server-hostname>`: (required) Server Hostname value.
   - `port-number`: (required) Port value, which is typically 443.
   - `http-path`: (required) HTTP Path value.
   - Query params: Databricks connection attributes. For complete list of optional parameters, see [Databricks Optional Parameters](https://docs.databricks.com/dev-tools/go-sql-driver#optional-parameters)


2. OAuth user-to-machine (U2M) authentication:

   ```
   databricks://<server-hostname>:<port-number>/<http-path>?authType=OauthU2M&<param1=value1>&<param2=value2>
   ```

   Components:
   - `scheme`: `databricks://` (required)
   - `<server-hostname>`: (required) Server Hostname value.
   - `port-number`: (required) Port value, which is typically 443.
   - `http-path`: (required) HTTP Path value.
   - `authType=OauthU2M`: (required) Specifies OAuth user-to-machine authentication.
   - Query params: Additional Databricks connection attributes. For complete list of optional parameters, see [Databricks Optional Parameters](https://docs.databricks.com/dev-tools/go-sql-driver#optional-parameters)

3. OAuth machine-to-machine (M2M) authentication:

   ```
   databricks://<server-hostname>:<port-number>/<http-path>?authType=OAuthM2M&clientID=<client-id>&clientSecret=<client-secret>&<param1=value1>&<param2=value2>
   ```

   Components:
   - `scheme`: `databricks://` (required)
   - `<server-hostname>`: (required) Server Hostname value.
   - `port-number`: (required) Port value, which is typically 443.
   - `http-path`: (required) HTTP Path value.
   - `authType=OAuthM2M`: (required) Specifies OAuth machine-to-machine authentication.
   - `<client-id>`: (required) Service principal's UUID or Application ID value.
   - `<client-secret>`: (required) Secret value for the service principal's OAuth secret.
   - Query params: Additional Databricks connection attributes. For complete list of optional parameters, see [Databricks Optional Parameters](https://docs.databricks.com/dev-tools/go-sql-driver#optional-parameters)

This follows the [Databricks SQL Driver for Go](https://docs.databricks.com/dev-tools/go-sql-driver#connect-with-a-dsn-connection-string) format with the addition of the `databricks://` scheme.

:::{note}
Reserved characters in URI elements must be URI-encoded. For example, `@` becomes `%40`.
:::

Examples:

- `databricks://token:dapi1234abcd5678efgh@dbc-a1b2345c-d6e7.cloud.databricks.com:443/sql/protocolv1/o/1234567890123456/1234-567890-abcdefgh`
- `databricks://myworkspace.cloud.databricks.com:443/sql/1.0/warehouses/abc123def456?authType=OauthU2M`
- `databricks://myworkspace.cloud.databricks.com:443/sql/1.0/warehouses/abc123def456?authType=OAuthM2M&clientID=12345678-1234-1234-1234-123456789012&clientSecret=mysecret123`

## Feature & Type Support

<table class="docutils data align-default" style="width: 100%">
  <colgroup>
    <col span="1" style="width: 25%;">
    <col span="1" style="width: 25%;">
    <col span="1" style="width: 50.0%;">
  </colgroup>
  <thead>
    <tr>
      <th colspan="2">Feature</th>
      <th style="text-align: center;">Databricks</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td colspan="2">Bind Parameters</td>
      <td colspan="1" style="text-align: center;">✅</td>
    </tr>
    <tr>
      <td rowspan="8">Bulk Ingestion</td>
      <td>Create</td>
      <td colspan="1" style="text-align: center;">✅</td>
    </tr>
    <tr>
      <td>Append</td>
      <td colspan="1" style="text-align: center;">✅</td>
    </tr>
    <tr>
      <td>Create/Append</td>
      <td colspan="1" style="text-align: center;">✅</td>
    </tr>
    <tr>
      <td>Replace</td>
      <td colspan="1" style="text-align: center;">✅</td>
    </tr>
    <tr>
      <td>Temporary Table</td>
      <td colspan="1" style="text-align: center;">❌</td>
    </tr>
    <tr>
      <td>Target Catalog</td>
      <td colspan="1" style="text-align: center;">❌</td>
    </tr>
    <tr>
      <td>Target Schema</td>
      <td colspan="1" style="text-align: center;">❌</td>
    </tr>
    <tr>
      <td>Non-nullable fields are marked NOT NULL</td>
      <td colspan="1" style="text-align: center;">❌</td>
    </tr>
    <tr>
      <td rowspan="4">Catalog (GetObjects)</td>
      <td>depth=catalogs</td>
      <td colspan="1" style="text-align: center;">✅</td>
    </tr>
    <tr>
      <td>depth=db_schemas</td>
      <td colspan="1" style="text-align: center;">✅</td>
    </tr>
    <tr>
      <td>depth=tables</td>
      <td colspan="1" style="text-align: center;">✅</td>
    </tr>
    <tr>
      <td>depth=columns (all)</td>
      <td colspan="1" style="text-align: center;">❌</td>
    </tr>
    <tr>
      <td colspan="2">Get Parameter Schema</td>
      <td colspan="1" style="text-align: center;">❌</td>
    </tr>
    <tr>
      <td colspan="2">Get Table Schema</td>
      <td colspan="1" style="text-align: center;">❌</td>
    </tr>
    <tr>
      <td colspan="2">Prepared Statements</td>
      <td colspan="1" style="text-align: center;">✅</td>
    </tr>
    <tr>
      <td colspan="2">Transactions</td>
      <td colspan="1" style="text-align: center;">❌</td>
    </tr>
  </tbody>
</table>

### Types

#### Database to Arrow

<table class="docutils data align-default" style="width: 100%;">
<colgroup>
<col span="1" style="width: 50.0%;">
<col span="1" style="width: 50.0%;">
</colgroup>
<thead>
<tr>
<th style="text-align: left; vertical-align: middle;">Database Type</th>
<th style="text-align: center;">Databricks</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">

BIGINT

</td>
<td style="text-align: center;">

int64

</td>
</tr>
<tr>
<td style="text-align: left;">

BOOLEAN

</td>
<td style="text-align: center;">

bool

</td>
</tr>
<tr>
<td style="text-align: left;">

DATE

</td>
<td style="text-align: center;">

date32[day]

</td>
</tr>
<tr>
<td style="text-align: left;">

DOUBLE PRECISION

</td>
<td style="text-align: center;">

double

</td>
</tr>
<tr>
<td style="text-align: left;">

INT

</td>
<td style="text-align: center;">

int32

</td>
</tr>
<tr>
<td style="text-align: left;">

NUMERIC

</td>
<td style="text-align: center;">

decimal128

</td>
</tr>
<tr>
<td style="text-align: left;">

REAL

</td>
<td style="text-align: center;">

float

</td>
</tr>
<tr>
<td style="text-align: left;">

SMALLINT

</td>
<td style="text-align: center;">

int16

</td>
</tr>
<tr>
<td style="text-align: left;">

TIMESTAMP

</td>
<td style="text-align: center;">

timestamp[us] (with time zone)

</td>
</tr>
<tr>
<td style="text-align: left;">

TIMESTAMP(7)

</td>
<td style="text-align: center;">

❌

</td>
</tr>
<tr>
<td style="text-align: left;">

TIMESTAMP(8)

</td>
<td style="text-align: center;">

❌

</td>
</tr>
<tr>
<td style="text-align: left;">

TIMESTAMP(9)

</td>
<td style="text-align: center;">

❌

</td>
</tr>
<tr>
<td style="text-align: left;">

TIMESTAMP_NTZ

</td>
<td style="text-align: center;">

timestamp[us]

</td>
</tr>
<tr>
<td style="text-align: left;">

TIMESTAMP_NTZ(7)

</td>
<td style="text-align: center;">

❌

</td>
</tr>
<tr>
<td style="text-align: left;">

TIMESTAMP_NTZ(8)

</td>
<td style="text-align: center;">

❌

</td>
</tr>
<tr>
<td style="text-align: left;">

TIMESTAMP_NTZ(9)

</td>
<td style="text-align: center;">

❌

</td>
</tr>
<tr>
<td style="text-align: left;">

VARBINARY

</td>
<td style="text-align: center;">

binary

</td>
</tr>
<tr>
<td style="text-align: left;">

VARCHAR

</td>
<td style="text-align: center;">

string

</td>
</tr>
</tbody>
</table>

#### Arrow to Database

<table class="docutils data align-default" style="width: 100%;">
<colgroup>
<col span="1" style="width: 25%;">
<col span="1" style="width: 37.5%;">
<col span="1" style="width: 37.5%;">
</colgroup>
<thead>
<tr>
<th rowspan="3" style="text-align: left; vertical-align: middle;">Arrow Type</th>
<th colspan="2" style="text-align: center;">Databricks Type</th>
</tr>
<tr>
<th style="text-align: center;">Bind</th>
<th style="text-align: center;">Ingest</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">

binary

</td>
<td colspan="2" style="text-align: center;">

VARBINARY

</td>
</tr>
<tr>
<td style="text-align: left;">

binary_view

</td>
<td colspan="2" style="text-align: center;">

VARBINARY

</td>
</tr>
<tr>
<td style="text-align: left;">

bool

</td>
<td colspan="2" style="text-align: center;">

BOOLEAN

</td>
</tr>
<tr>
<td style="text-align: left;">

date32[day]

</td>
<td colspan="2" style="text-align: center;">

DATE

</td>
</tr>
<tr>
<td style="text-align: left;">

decimal128

</td>
<td colspan="2" style="text-align: center;">

NUMERIC

</td>
</tr>
<tr class="row-with-cell-borders">
<td style="text-align: left;">

double

</td>
<td style="text-align: center;">

DOUBLE

</td>
<td style="text-align: center;">

DOUBLE PRECISION

</td>
</tr>
<tr>
<td style="text-align: left;">

fixed_size_binary

</td>
<td colspan="2" style="text-align: center;">

VARBINARY

</td>
</tr>
<tr>
<td style="text-align: left;">

float

</td>
<td colspan="2" style="text-align: center;">

REAL

</td>
</tr>
<tr class="row-with-cell-borders">
<td style="text-align: left;">

halffloat

</td>
<td style="text-align: center;">

REAL

</td>
<td style="text-align: center;">

(NA/not tested)

</td>
</tr>
<tr>
<td style="text-align: left;">

int16

</td>
<td colspan="2" style="text-align: center;">

SMALLINT

</td>
</tr>
<tr>
<td style="text-align: left;">

int32

</td>
<td colspan="2" style="text-align: center;">

INT

</td>
</tr>
<tr>
<td style="text-align: left;">

int64

</td>
<td colspan="2" style="text-align: center;">

BIGINT

</td>
</tr>
<tr>
<td style="text-align: left;">

large_binary

</td>
<td colspan="2" style="text-align: center;">

VARBINARY

</td>
</tr>
<tr>
<td style="text-align: left;">

large_string

</td>
<td colspan="2" style="text-align: center;">

VARCHAR

</td>
</tr>
<tr>
<td style="text-align: left;">

string

</td>
<td colspan="2" style="text-align: center;">

VARCHAR

</td>
</tr>
<tr>
<td style="text-align: left;">

string_view

</td>
<td colspan="2" style="text-align: center;">

VARCHAR

</td>
</tr>
<tr class="row-with-cell-borders">
<td style="text-align: left;">

time32[ms]

</td>
<td style="text-align: center;">

❌

</td>
<td style="text-align: center;">

(NA/not tested)

</td>
</tr>
<tr class="row-with-cell-borders">
<td style="text-align: left;">

time32[s]

</td>
<td style="text-align: center;">

❌

</td>
<td style="text-align: center;">

(NA/not tested)

</td>
</tr>
<tr class="row-with-cell-borders">
<td style="text-align: left;">

time64[ns]

</td>
<td style="text-align: center;">

❌

</td>
<td style="text-align: center;">

(NA/not tested)

</td>
</tr>
<tr class="row-with-cell-borders">
<td style="text-align: left;">

time64[us]

</td>
<td style="text-align: center;">

❌

</td>
<td style="text-align: center;">

(NA/not tested)

</td>
</tr>
<tr>
<td style="text-align: left;">

timestamp[ms]

</td>
<td colspan="2" style="text-align: center;">

TIMESTAMP_NTZ

</td>
</tr>
<tr>
<td style="text-align: left;">

timestamp[ms] (with time zone)

</td>
<td colspan="2" style="text-align: center;">

TIMESTAMP

</td>
</tr>
<tr>
<td style="text-align: left;">

timestamp[ns]

</td>
<td colspan="2" style="text-align: center;">

TIMESTAMP_NTZ ⚠️ [^1]

</td>
</tr>
<tr>
<td style="text-align: left;">

timestamp[ns] (with time zone)

</td>
<td colspan="2" style="text-align: center;">

TIMESTAMP ⚠️ [^1]

</td>
</tr>
<tr>
<td style="text-align: left;">

timestamp[s]

</td>
<td colspan="2" style="text-align: center;">

TIMESTAMP_NTZ

</td>
</tr>
<tr>
<td style="text-align: left;">

timestamp[s] (with time zone)

</td>
<td colspan="2" style="text-align: center;">

TIMESTAMP

</td>
</tr>
<tr class="row-with-cell-borders">
<td style="text-align: left;">

timestamp[us]

</td>
<td style="text-align: center;">

TIMESTAMP_NTZ

</td>
<td style="text-align: center;">

TIMESTAMP(6)

</td>
</tr>
<tr>
<td style="text-align: left;">

timestamp[us] (with time zone)

</td>
<td colspan="2" style="text-align: center;">

TIMESTAMP

</td>
</tr>
</tbody>
</table>

## Compatibility

This driver was tested on:

- Databricks `2026.42`

## Previous Versions

To see documentation for previous versions of this driver, see the following:

- [v0.2.0](./v0.2.0.md)
- [v0.1.3](./v0.1.3.md)
- [v0.1.2](./v0.1.2.md)

[^1]: Nanosecond timestamps are truncated to microseconds.

[databricks]: https://www.databricks.com
