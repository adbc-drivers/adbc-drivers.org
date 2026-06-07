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

(driver-clickhouse-v0.1.0-alpha.2)=
# ClickHouse Driver v0.1.0-alpha.2

[{badge-primary}`Driver Version|v0.1.0-alpha.2`](#driver-clickhouse-v0.1.0-alpha.2 "Permalink") {badge-secondary}`Release Date|2026-05-21` {badge-success}`Tested With|ClickHouse 25.12`

This driver provides access to [ClickHouse][clickhouse], an open source data warehouse and analytical database.  It is developed by ClickHouse, Inc.  The source code can be found at [adbc_clickhouse](https://github.com/ClickHouse/adbc_clickhouse); the ADBC Driver Foundry distributes precompiled binaries of the upstream sources for Linux, macOS, and Windows.

ClickHouse is a trademark of ClickHouse, Inc. https://clickhouse.com

## Installation

The ClickHouse driver can be installed with [dbc](https://docs.columnar.tech/dbc):

```bash
dbc install --pre clickhouse
```

:::{note}
Only prerelease versions of the driver are currently available, so you must use `--pre` with dbc 0.2.0 or newer to install the driver.
:::

## Connecting

To use the driver, provide the URI of a ClickHouse database as the `uri` option.

```python
from adbc_driver_manager import dbapi

conn = dbapi.connect(
  driver="clickhouse",
  db_kwargs={
      "uri": "http://localhost:8123/",
  }
)
```

Note: The example above is for Python using the [adbc-driver-manager](https://pypi.org/project/adbc-driver-manager) package but the process will be similar for other driver managers.

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
      <th style="text-align: center;">ClickHouse</th>
    </tr>
  </thead>
  <tbody>
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
      <td colspan="1" style="text-align: center;">❌</td>
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
<thead>
<tr>
<th style="text-align: left; vertical-align: middle;">Database Type</th>
<th style="text-align: center;">ClickHouse</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">

Boolean

</td>
<td style="text-align: center;">

bool

</td>
</tr>
<tr>
<td style="text-align: left;">

Date32

</td>
<td style="text-align: center;">

date32[day] [^1]

</td>
</tr>
<tr>
<td style="text-align: left;">

DateTime64 (no time zone)

</td>
<td style="text-align: center;">

timestamp[us] (with time zone) [^2] [^3]

</td>
</tr>
<tr>
<td style="text-align: left;">

DateTime64 (with time zone)

</td>
<td style="text-align: center;">

timestamp[us] (with time zone) [^3]

</td>
</tr>
<tr>
<td style="text-align: left;">

Decimal

</td>
<td style="text-align: center;">

decimal128

</td>
</tr>
<tr>
<td style="text-align: left;">

Float32

</td>
<td style="text-align: center;">

float

</td>
</tr>
<tr>
<td style="text-align: left;">

Float64

</td>
<td style="text-align: center;">

double

</td>
</tr>
<tr>
<td style="text-align: left;">

Int16

</td>
<td style="text-align: center;">

int16

</td>
</tr>
<tr>
<td style="text-align: left;">

Int32

</td>
<td style="text-align: center;">

int32

</td>
</tr>
<tr>
<td style="text-align: left;">

Int64

</td>
<td style="text-align: center;">

int64

</td>
</tr>
<tr>
<td style="text-align: left;">

String

</td>
<td style="text-align: center;">

string

</td>
</tr>
<tr>
<td style="text-align: left;">

Time

</td>
<td style="text-align: center;">

❌ [^4]

</td>
</tr>
</tbody>
</table>

#### Arrow to Database

<table class="docutils data align-default" style="width: 100%;">
<thead>
<tr>
<th rowspan="3" style="text-align: left; vertical-align: middle;">Arrow Type</th>
<th colspan="2" style="text-align: center;">ClickHouse Type</th>
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

❌

</td>
</tr>
<tr>
<td style="text-align: left;">

binary_view

</td>
<td colspan="2" style="text-align: center;">

❌

</td>
</tr>
<tr>
<td style="text-align: left;">

bool

</td>
<td colspan="2" style="text-align: center;">

❌

</td>
</tr>
<tr>
<td style="text-align: left;">

date32[day]

</td>
<td colspan="2" style="text-align: center;">

❌

</td>
</tr>
<tr>
<td style="text-align: left;">

decimal128

</td>
<td colspan="2" style="text-align: center;">

❌

</td>
</tr>
<tr>
<td style="text-align: left;">

double

</td>
<td colspan="2" style="text-align: center;">

❌

</td>
</tr>
<tr>
<td style="text-align: left;">

fixed_size_binary

</td>
<td colspan="2" style="text-align: center;">

❌

</td>
</tr>
<tr>
<td style="text-align: left;">

float

</td>
<td colspan="2" style="text-align: center;">

❌

</td>
</tr>
<tr>
<td style="text-align: left;">

halffloat

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

int16

</td>
<td colspan="2" style="text-align: center;">

❌

</td>
</tr>
<tr>
<td style="text-align: left;">

int32

</td>
<td colspan="2" style="text-align: center;">

❌

</td>
</tr>
<tr>
<td style="text-align: left;">

int64

</td>
<td colspan="2" style="text-align: center;">

❌

</td>
</tr>
<tr>
<td style="text-align: left;">

large_binary

</td>
<td colspan="2" style="text-align: center;">

❌

</td>
</tr>
<tr>
<td style="text-align: left;">

large_string

</td>
<td colspan="2" style="text-align: center;">

❌

</td>
</tr>
<tr>
<td style="text-align: left;">

string

</td>
<td colspan="2" style="text-align: center;">

❌

</td>
</tr>
<tr>
<td style="text-align: left;">

string_view

</td>
<td colspan="2" style="text-align: center;">

❌

</td>
</tr>
<tr>
<td style="text-align: left;">

time32[ms]

</td>
<td colspan="2" style="text-align: center;">

❌

</td>
</tr>
<tr>
<td style="text-align: left;">

time32[s]

</td>
<td colspan="2" style="text-align: center;">

❌

</td>
</tr>
<tr>
<td style="text-align: left;">

time64[ns]

</td>
<td colspan="2" style="text-align: center;">

❌

</td>
</tr>
<tr>
<td style="text-align: left;">

time64[us]

</td>
<td colspan="2" style="text-align: center;">

❌

</td>
</tr>
<tr>
<td style="text-align: left;">

timestamp[ms]

</td>
<td colspan="2" style="text-align: center;">

❌

</td>
</tr>
<tr>
<td style="text-align: left;">

timestamp[ms] (with time zone)

</td>
<td colspan="2" style="text-align: center;">

❌

</td>
</tr>
<tr>
<td style="text-align: left;">

timestamp[ns]

</td>
<td colspan="2" style="text-align: center;">

❌

</td>
</tr>
<tr>
<td style="text-align: left;">

timestamp[ns] (with time zone)

</td>
<td colspan="2" style="text-align: center;">

❌

</td>
</tr>
<tr>
<td style="text-align: left;">

timestamp[s]

</td>
<td colspan="2" style="text-align: center;">

❌

</td>
</tr>
<tr>
<td style="text-align: left;">

timestamp[s] (with time zone)

</td>
<td colspan="2" style="text-align: center;">

❌

</td>
</tr>
<tr>
<td style="text-align: left;">

timestamp[us]

</td>
<td colspan="2" style="text-align: center;">

❌

</td>
</tr>
<tr>
<td style="text-align: left;">

timestamp[us] (with time zone)

</td>
<td colspan="2" style="text-align: center;">

❌

</td>
</tr>
</tbody>
</table>

[^1]: Date32 has limited range (1900-01-01 to 2299-12-31)
[^2]: ClickHouse datetime without timezone is interpreted in **server** timezone
[^3]: DateTime64 has limited range (1900 to 2299)
[^4]: ClickHouse Time type is not supported in Arrow format export

[clickhouse]: https://clickhouse.com/
