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

# DataFusion

:::{toctree}
:maxdepth: 1
:hidden:

v0.24.1 <v0.24.1.md>
:::

[{badge-primary}`Driver Version|v0.24.1`](#driver-datafusion-v0.24.1 "Permalink") {badge-secondary}`Release Date|2026-05-27` {badge-success}`Tested With|Apache DataFusion 53`

This driver provides access to [Apache DataFusion][datafusion].

:::{note}
This project is not part of the Apache Software Foundation.
:::

## Installation & Quickstart

The driver can be installed with [dbc](https://docs.columnar.tech/dbc):

```bash
dbc install datafusion
```

## Connecting

DataFusion is an in-process query engine and does not need a connection string or URI.

```python
from adbc_driver_manager import dbapi

dbapi.connect(driver="datafusion")
```

You can provide the URI `datafusion://`, but no other URI is currently accepted:

```python
from adbc_driver_manager import dbapi

dbapi.connect("datafusion://")
```

Note: The example above is for Python using the [adbc-driver-manager](https://pypi.org/project/adbc-driver-manager) package but the process will be similar for other driver managers.  See [adbc-quickstarts](https://github.com/columnar-tech/adbc-quickstarts).

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
      <th style="text-align: center;">Apache DataFusion</th>
    </tr>
  </thead>
  <tbody>
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
      <td colspan="1" style="text-align: center;">✅</td>
    </tr>
    <tr>
      <td>Target Schema</td>
      <td colspan="1" style="text-align: center;">✅</td>
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
      <td colspan="1" style="text-align: center;">✅</td>
    </tr>
    <tr>
      <td colspan="2">Get Parameter Schema</td>
      <td colspan="1" style="text-align: center;">✅</td>
    </tr>
    <tr>
      <td colspan="2">Get Table Schema</td>
      <td colspan="1" style="text-align: center;">✅</td>
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
<thead>
<tr>
<th style="text-align: left; vertical-align: middle;">Database Type</th>
<th style="text-align: center;">Apache DataFusion</th>
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

BYTEA

</td>
<td style="text-align: center;">

binary

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

DECIMAL

</td>
<td style="text-align: center;">

decimal128

</td>
</tr>
<tr>
<td style="text-align: left;">

DOUBLE

</td>
<td style="text-align: center;">

double

</td>
</tr>
<tr>
<td style="text-align: left;">

FLOAT

</td>
<td style="text-align: center;">

float

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

SMALLINT

</td>
<td style="text-align: center;">

int16

</td>
</tr>
<tr>
<td style="text-align: left;">

TIME

</td>
<td style="text-align: center;">

time64[ns]

</td>
</tr>
<tr>
<td style="text-align: left;">

TIMESTAMP

</td>
<td style="text-align: center;">

timestamp[ns] [^1]

</td>
</tr>
<tr>
<td style="text-align: left;">

TIMESTAMP WITH TIME ZONE

</td>
<td style="text-align: center;">

timestamp[ns] [^1] [^2]

</td>
</tr>
<tr>
<td style="text-align: left;">

VARCHAR

</td>
<td style="text-align: center;">

string, string_view ⚠️ [^3]

</td>
</tr>
</tbody>
</table>

#### Arrow to Database

<table class="docutils data align-default" style="width: 100%;">
<thead>
<tr>
<th rowspan="3" style="text-align: left; vertical-align: middle;">Arrow Type</th>
<th colspan="2" style="text-align: center;">Apache DataFusion Type</th>
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

BYTEA

</td>
</tr>
<tr>
<td style="text-align: left;">

binary_view

</td>
<td style="text-align: center;">

❌

</td>
<td style="text-align: center;">

BYTEA

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
<td style="text-align: center;">

NUMERIC

</td>
<td style="text-align: center;">

DECIMAL

</td>
</tr>
<tr>
<td style="text-align: left;">

double

</td>
<td style="text-align: center;">

DOUBLE PRECISION

</td>
<td style="text-align: center;">

DOUBLE

</td>
</tr>
<tr>
<td style="text-align: left;">

fixed_size_binary

</td>
<td style="text-align: center;">

❌

</td>
<td style="text-align: center;">

BYTEA

</td>
</tr>
<tr>
<td style="text-align: left;">

float

</td>
<td style="text-align: center;">

REAL

</td>
<td style="text-align: center;">

FLOAT

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
<td style="text-align: center;">

❌

</td>
<td style="text-align: center;">

BYTEA

</td>
</tr>
<tr>
<td style="text-align: left;">

large_string

</td>
<td style="text-align: center;">

❌

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

❌

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

❌

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

(NA/not tested)

</td>
<td style="text-align: center;">

TIME

</td>
</tr>
<tr>
<td style="text-align: left;">

time32[s]

</td>
<td style="text-align: center;">

(NA/not tested)

</td>
<td style="text-align: center;">

TIME

</td>
</tr>
<tr>
<td style="text-align: left;">

time64[ns]

</td>
<td colspan="2" style="text-align: center;">

TIME

</td>
</tr>
<tr>
<td style="text-align: left;">

time64[us]

</td>
<td style="text-align: center;">

(NA/not tested)

</td>
<td style="text-align: center;">

TIME

</td>
</tr>
<tr>
<td style="text-align: left;">

timestamp[ms]

</td>
<td style="text-align: center;">

TIMESTAMP(3)

</td>
<td style="text-align: center;">

TIMESTAMP

</td>
</tr>
<tr>
<td style="text-align: left;">

timestamp[ms] (with time zone)

</td>
<td style="text-align: center;">

❌

</td>
<td style="text-align: center;">

TIMESTAMP WITH TIME ZONE

</td>
</tr>
<tr>
<td style="text-align: left;">

timestamp[ns]

</td>
<td style="text-align: center;">

TIMESTAMP(9)

</td>
<td style="text-align: center;">

TIMESTAMP

</td>
</tr>
<tr>
<td style="text-align: left;">

timestamp[ns] (with time zone)

</td>
<td style="text-align: center;">

❌

</td>
<td style="text-align: center;">

TIMESTAMP WITH TIME ZONE

</td>
</tr>
<tr>
<td style="text-align: left;">

timestamp[s]

</td>
<td style="text-align: center;">

TIMESTAMP(0)

</td>
<td style="text-align: center;">

TIMESTAMP

</td>
</tr>
<tr>
<td style="text-align: left;">

timestamp[s] (with time zone)

</td>
<td style="text-align: center;">

❌

</td>
<td style="text-align: center;">

TIMESTAMP WITH TIME ZONE

</td>
</tr>
<tr>
<td style="text-align: left;">

timestamp[us]

</td>
<td style="text-align: center;">

TIMESTAMP(6)

</td>
<td style="text-align: center;">

TIMESTAMP

</td>
</tr>
<tr>
<td style="text-align: left;">

timestamp[us] (with time zone)

</td>
<td style="text-align: center;">

❌

</td>
<td style="text-align: center;">

TIMESTAMP WITH TIME ZONE

</td>
</tr>
</tbody>
</table>

[^1]: DataFusion uses nanosecond precision; max timestamp is 2262-04-11T23:47:16
[^2]: DataFusion does not preserve timezone metadata in Arrow output
[^3]: Return type is inconsistent depending on how the query was written

## Compatibility

This driver was tested on:

- Apache DataFusion `53.1.0`

[datafusion]: https://datafusion.apache.org/
