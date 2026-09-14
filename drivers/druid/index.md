---
# Copyright (c) 2026 ADBC Drivers Contributors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
{}
---

(driver-druid-prerelease)=
# Apache Druid

:::{toctree}
:maxdepth: 1
:hidden:

Changelog <changelog.md>
v0.1.0-alpha.1 <v0.1.0-alpha.1.md>
:::

{badge-primary}`Driver Version|v0.1.0-alpha.1` {badge-secondary}`Release Date|2026-09-14` {badge-success}`Tested With|Apache Druid 37`

:::{warning}
This is documentation for a prerelease version.
:::

This driver provides access to [Apache Druid][druid], a high-performance,
real-time analytics database.

:::{note}
This project is not part of the Apache Software Foundation.
:::

## Installation & Quickstart

The Druid driver can be installed with [dbc](https://docs.columnar.tech/dbc):

```bash
dbc install --pre druid
```

## Connecting

To use the driver, provide the URI of a Druid database as the `uri` option.

```python
from adbc_driver_manager import dbapi

connection = dbapi.connect(
    driver="druid",
    db_kwargs={
        "uri": "druid://localhost:8888?tls=false",
    },
)
```

Note: The example above is for Python using the [adbc-driver-manager](https://pypi.org/project/adbc-driver-manager) package but the process will be similar for other driver managers. See [adbc-quickstarts](https://github.com/columnar-tech/adbc-quickstarts).

### Connection String Format

```text
druid://[username[:password]@]host[:port][/path][?tls=true|false&tls_ca=path]
```

Components:

- Scheme: `druid://` (also accepts `http://` and `https://`)
- `username`: HTTP Basic authentication username (optional)
- `password`: HTTP Basic authentication password (optional; requires a username)
- `host`: Druid Router or Broker host (required)
- `port`: Service port (optional; defaults to 443 for HTTPS and 80 for HTTP)
- `path`: Base path when Druid is exposed through a reverse proxy (optional)
- `tls`: Whether to use HTTPS; defaults to `true` and only applies to
  `druid://` URIs
- `tls_ca`: Path to a PEM CA certificate used to verify the server

#### HTTPS/SSL Configuration

The `druid://` scheme uses HTTPS and the system trust store by default. To
connect to a plaintext Druid endpoint, set `tls=false`.

Examples:

- `druid://druid.example.com` → HTTPS on port 443
- `druid://druid.example.com:9088` → HTTPS on port 9088
- `druid://localhost:9088?tls_ca=/path/to/ca.crt` → HTTPS with a
  custom CA
- `druid://localhost:8888?tls=false` → HTTP on port 8888
- `https://druid.example.com:9088` → Explicit HTTPS URL
- `http://localhost:8888` → Explicit HTTP URL

Reserved characters in credentials must be percent-encoded. For example, `@`
becomes `%40`. Credentials can instead be supplied with the ADBC `username`
and `password` database options; those options override credentials in the URI
and are recommended when the URI may appear in logs or shell history.

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
      <th style="text-align: center;">Apache Druid</th>
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
      <td colspan="1" style="text-align: center;">❌</td>
    </tr>
    <tr>
      <td>Append</td>
      <td colspan="1" style="text-align: center;">❌</td>
    </tr>
    <tr>
      <td>Create/Append</td>
      <td colspan="1" style="text-align: center;">❌</td>
    </tr>
    <tr>
      <td>Replace</td>
      <td colspan="1" style="text-align: center;">❌</td>
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
      <td colspan="1" style="text-align: center;">❌</td>
    </tr>
    <tr>
      <td>depth=db_schemas</td>
      <td colspan="1" style="text-align: center;">❌</td>
    </tr>
    <tr>
      <td>depth=tables</td>
      <td colspan="1" style="text-align: center;">❌</td>
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
      <td colspan="1" style="text-align: center;">✅</td>
    </tr>
    <tr>
      <td colspan="2">Prepared Statements</td>
      <td colspan="1" style="text-align: center;">❌</td>
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
<th style="text-align: center;">Apache Druid</th>
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

int64

</td>
</tr>
<tr>
<td style="text-align: left;">

NUMERIC

</td>
<td style="text-align: center;">

double ⚠️ [^1]

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

❌

</td>
</tr>
<tr>
<td style="text-align: left;">

TIME

</td>
<td style="text-align: center;">

❌

</td>
</tr>
<tr>
<td style="text-align: left;">

TIMESTAMP

</td>
<td style="text-align: center;">

timestamp[ms]

</td>
</tr>
<tr>
<td style="text-align: left;">

TIMESTAMP WITH TIME ZONE

</td>
<td style="text-align: center;">

❌

</td>
</tr>
<tr>
<td style="text-align: left;">

TIMESTAMP(0)

</td>
<td style="text-align: center;">

❌

</td>
</tr>
<tr>
<td style="text-align: left;">

TIMESTAMP(0) WITH TIME ZONE

</td>
<td style="text-align: center;">

❌

</td>
</tr>
<tr>
<td style="text-align: left;">

TIMESTAMP(p) (1 &lt;= p &lt;= 3)

</td>
<td style="text-align: center;">

timestamp[ms]

</td>
</tr>
<tr>
<td style="text-align: left;">

TIMESTAMP(p) (1 &lt;= p &lt;= 3) WITH TIME ZONE

</td>
<td style="text-align: center;">

❌

</td>
</tr>
<tr>
<td style="text-align: left;">

TIMESTAMP(p) (4 &lt;= p &lt;= 6)

</td>
<td style="text-align: center;">

❌

</td>
</tr>
<tr>
<td style="text-align: left;">

TIMESTAMP(p) (4 &lt;= p &lt;= 6) WITH TIME ZONE

</td>
<td style="text-align: center;">

❌

</td>
</tr>
<tr>
<td style="text-align: left;">

TIMESTAMP(p) (7 &lt;= p &lt;= 9)

</td>
<td style="text-align: center;">

❌

</td>
</tr>
<tr>
<td style="text-align: left;">

TIMESTAMP(p) (7 &lt;= p &lt;= 9) WITH TIME ZONE

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

❌

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
<col span="1" style="width: 75.0%;">
</colgroup>
<thead>
<tr>
<th rowspan="3" style="text-align: left; vertical-align: middle;">Arrow Type</th>
<th colspan="1" style="text-align: center;">Apache Druid Type</th>
</tr>
<tr>
<th style="text-align: center;">Bind</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">

binary

</td>
<td style="text-align: center;">

❌

</td>
</tr>
<tr>
<td style="text-align: left;">

binary_view

</td>
<td style="text-align: center;">

❌

</td>
</tr>
<tr>
<td style="text-align: left;">

bool

</td>
<td style="text-align: center;">

BOOLEAN

</td>
</tr>
<tr>
<td style="text-align: left;">

date32[day]

</td>
<td style="text-align: center;">

DATE ⚠️ [^2]

</td>
</tr>
<tr>
<td style="text-align: left;">

decimal128

</td>
<td style="text-align: center;">

NUMERIC ⚠️ [^1]

</td>
</tr>
<tr>
<td style="text-align: left;">

double

</td>
<td style="text-align: center;">

DOUBLE PRECISION

</td>
</tr>
<tr>
<td style="text-align: left;">

fixed_size_binary

</td>
<td style="text-align: center;">

❌

</td>
</tr>
<tr>
<td style="text-align: left;">

float

</td>
<td style="text-align: center;">

REAL

</td>
</tr>
<tr>
<td style="text-align: left;">

halffloat

</td>
<td style="text-align: center;">

REAL

</td>
</tr>
<tr>
<td style="text-align: left;">

int16

</td>
<td style="text-align: center;">

SMALLINT

</td>
</tr>
<tr>
<td style="text-align: left;">

int32

</td>
<td style="text-align: center;">

INT

</td>
</tr>
<tr>
<td style="text-align: left;">

int64

</td>
<td style="text-align: center;">

BIGINT

</td>
</tr>
<tr>
<td style="text-align: left;">

large_binary

</td>
<td style="text-align: center;">

❌

</td>
</tr>
<tr>
<td style="text-align: left;">

large_string

</td>
<td style="text-align: center;">

VARCHAR

</td>
</tr>
<tr>
<td style="text-align: left;">

string

</td>
<td style="text-align: center;">

VARCHAR

</td>
</tr>
<tr>
<td style="text-align: left;">

string_view

</td>
<td style="text-align: center;">

VARCHAR

</td>
</tr>
<tr>
<td style="text-align: left;">

time32[ms]

</td>
<td style="text-align: center;">

❌

</td>
</tr>
<tr>
<td style="text-align: left;">

time32[s]

</td>
<td style="text-align: center;">

❌

</td>
</tr>
<tr>
<td style="text-align: left;">

time64[ns]

</td>
<td style="text-align: center;">

❌

</td>
</tr>
<tr>
<td style="text-align: left;">

time64[us]

</td>
<td style="text-align: center;">

❌

</td>
</tr>
<tr>
<td style="text-align: left;">

timestamp[ms]

</td>
<td style="text-align: center;">

TIMESTAMP(3) ⚠️ [^3]

</td>
</tr>
<tr>
<td style="text-align: left;">

timestamp[ms] (with time zone)

</td>
<td style="text-align: center;">

❌

</td>
</tr>
<tr>
<td style="text-align: left;">

timestamp[ns]

</td>
<td style="text-align: center;">

❌

</td>
</tr>
<tr>
<td style="text-align: left;">

timestamp[ns] (with time zone)

</td>
<td style="text-align: center;">

❌

</td>
</tr>
<tr>
<td style="text-align: left;">

timestamp[s]

</td>
<td style="text-align: center;">

❌

</td>
</tr>
<tr>
<td style="text-align: left;">

timestamp[s] (with time zone)

</td>
<td style="text-align: center;">

❌

</td>
</tr>
<tr>
<td style="text-align: left;">

timestamp[us]

</td>
<td style="text-align: center;">

❌

</td>
</tr>
<tr>
<td style="text-align: left;">

timestamp[us] (with time zone)

</td>
<td style="text-align: center;">

❌

</td>
</tr>
</tbody>
</table>

[^1]: Druid represents DECIMAL values as DOUBLE, so values can lose precision.
[^2]: Druid 37 rejects NULL DATE query parameters, so NULL binding is not supported.
[^3]: Druid 37 rejects NULL TIMESTAMP query parameters, so NULL binding is not supported.

## Options

### Statement Options

``druid.statement.<option_name>``
: Type: string, integer, or double.

  Sets a Druid SQL query-context parameter. The driver removes the
  ``druid.statement.`` prefix and sends the remaining option name to Druid.
  For example, ``druid.statement.timeout`` sets Druid's ``timeout`` context
  parameter. Byte values are not supported.

## Compatibility

This driver was tested on:

- Apache Druid `37.0.0`

[druid]: https://druid.apache.org/
