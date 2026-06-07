---
# Copyright (c) 2025 ADBC Drivers Contributors
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

# BigQuery

:::{toctree}
:maxdepth: 1
:hidden:

v1.11.2.md
v1.11.0.md
v1.10.0.md
v1.0.0.md
:::

[{badge-primary}`Driver Version|v1.11.2`](#driver-bigquery-v1.11.2 "Permalink") {badge-secondary}`Release Date|2026-03-10` {badge-success}`Tested With|BigQuery 1.73.1`

This driver provides access to [BigQuery][bigquery], a data warehouse offered by Google Cloud.

:::{note}
This project is not affiliated with Google.
:::

## Installation

The BigQuery driver can be installed with [dbc](https://docs.columnar.tech/dbc):

```bash
dbc install bigquery
```

## Pre-requisites

Using the BigQuery driver requires some setup before you can connect:

1. Create a [Google Cloud account](http://console.cloud.google.com)
1. Install the [Google Cloud CLI](https://cloud.google.com/cli) (for managing credentials)
1. Authenticate with Google Cloud
    - Run `gcloud auth application-default login`
1. Create, find, or reuse a project and dataset (record these for later)

## Connecting

To connect, replace `my-gcp-project` and `my-gcp-dataset` below with the appropriate values for your situation and run the following:

```python
from adbc_driver_manager import dbapi

conn = dbapi.connect(
  driver="bigquery",
  db_kwargs={
      "adbc.bigquery.sql.project_id": "my-gcp-project",
      "adbc.bigquery.sql.dataset_id": "my-gcp-dataset"
  }
)
```

Note: The example above is for Python using the [adbc-driver-manager](https://pypi.org/project/adbc-driver-manager) package but the process will be similar for other driver managers. See [adbc-quickstarts](https://github.com/columnar-tech/adbc-quickstarts).

The driver supports connecting with individual options or connection strings.

## Connection String Format

BigQuery URI syntax:

```
bigquery://[Host]:[Port]/ProjectID?OAuthType=[AuthValue]&[Key]=[Value]&[Key]=[Value]...
```

The format follows a similar approach to the [Simba BigQuery JDBC Connection String Format](https://storage.googleapis.com/simba-bq-release/jdbc/Simba%20Google%20BigQuery%20JDBC%20Connector%20Install%20and%20Configuration%20Guide_1.6.3.1004.pdf).

Components:

- `Scheme`: `bigquery://` (required)
- `Host`: BigQuery API endpoint (optional, defaults to `bigquery.googleapis.com`)
- `Port`: TCP port (optional, defaults to 443)
- `ProjectID`: Google Cloud Project ID (required)
- `OAuthType`: Authentication type number (optional, defaults to `0`)
  - `0` - Application Default Credentials (default)
  - `1` - Service Account JSON File
  - `2` - Service Account JSON String
  - `3` - User Authentication (OAuth)
- Additional Parameters: Connection configuration as key-value pairs. For a complete list of available parameters, see the [Simba BigQuery JDBC Connector Configuration Options](https://storage.googleapis.com/simba-bq-release/jdbc/Simba%20Google%20BigQuery%20JDBC%20Connector%20Install%20and%20Configuration%20Guide_1.6.3.1004.pdf).

:::{note}
Reserved characters in URI elements must be URI-encoded. For example, `@` becomes `%40`.
:::

Examples:

- `bigquery:///my-project-123` (uses Application Default Credentials)
- `bigquery://bigquery.googleapis.com/my-project-123?OAuthType=1&AuthCredentials=/path/to/key.json`
- `bigquery:///my-project-123?OAuthType=3&AuthClientId=123.apps.googleusercontent.com&AuthClientSecret=secret&AuthRefreshToken=token`
- `bigquery://bigquery.googleapis.com/my-project-123?OAuthType=0&DatasetId=analytics&Location=US`
- `bigquery:///my-project-123?OAuthType=2&AuthCredentials=%7B%22type%22%3A%22service_account%22...%7D&DatasetId=data_warehouse`

## Feature & Type Support

<table class="docutils data align-default" style="width: 100%">
  <colgroup>
    <col span="1" style="width: 25%;">
    <col span="1" style="width: 25%;">
    <col span="1" style="width: 50%;">
  </colgroup>
  <thead>
    <tr>
      <th>Feature</th>
      <th colspan="2">Support</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="8">Bulk Ingestion</td>
      <td>Create</td>
      <td>✅</td>
    </tr>
    <tr>
      <td>Append</td>
      <td>✅</td>
    </tr>
    <tr>
      <td>Create/Append</td>
      <td>✅</td>
    </tr>
    <tr>
      <td>Replace</td>
      <td>✅</td>
    </tr>
    <tr>
      <td>Temporary Table</td>
      <td>❌</td>
    </tr>
    <tr>
      <td>Specify target catalog</td>
      <td>❌</td>
    </tr>
    <tr>
      <td>Specify target schema</td>
      <td>✅</td>
    </tr>
    <tr>
      <td>Non-nullable fields are marked NOT NULL</td>
      <td>✅</td>
    </tr>
    <tr>
      <td rowspan="4">Catalog (GetObjects)</td>
      <td>depth=catalogs</td>
      <td>✅</td>
    </tr>
    <tr>
      <td>depth=db_schemas</td>
      <td>✅</td>
    </tr>
    <tr>
      <td>depth=tables</td>
      <td>✅</td>
    </tr>
    <tr>
      <td>depth=columns (all)</td>
      <td>✅</td>
    </tr>
    <tr>
      <td>Get Parameter Schema</td>
      <td colspan="2">❌</td>
    </tr>
    <tr>
      <td>Get Table Schema</td>
      <td colspan="2">✅</td>
    </tr>
    <tr>
      <td>Prepared Statements</td>
      <td colspan="2">✅</td>
    </tr>
    <tr>
      <td>Transactions</td>
      <td colspan="2">✅</td>
    </tr>
  </tbody>
</table>

### Types

#### BigQuery to Arrow

:::{list-table}
:header-rows: 1
:width: 100%
:widths: 1 3

* - BigQuery Type
  - Arrow Type
* - ARRAY
  - list [^1]
* - BIGNUMERIC
  - decimal256(76, 38)
* - BOOL
  - bool
* - BOOLEAN
  - bool
* - BYTES
  - binary
* - DATE
  - date32[day]
* - DATETIME
  - timestamp[us] [^2]
* - FLOAT64
  - double
* - GEOGRAPHY
  - extension&lt;geoarrow.wkt&gt;
* - INT64
  - int64
* - INTERVAL
  - month_day_nano_interval
* - JSON
  - extension&lt;arrow.json&gt;
* - NUMERIC
  - decimal128(38, 9) [^3] [^4] [^5]
* - RANGE&lt;DATE&gt;
  - struct&lt;start: date32[day], end: date32[day]&gt;
* - RANGE&lt;DATETIME&gt;
  - struct&lt;start: timestamp[us], end: timestamp[us]&gt;
* - RANGE&lt;TIMESTAMP&gt;
  - struct&lt;start: timestamp[us, tz=UTC], end: timestamp[us, tz=UTC]&gt;
* - STRING
  - string
* - STRUCT
  - struct
* - TIME
  - time64[us]
* - TIMESTAMP
  - timestamp[us] (with time zone) [^6]
:::

#### Arrow to BigQuery


<table class="docutils data align-default" style="width: 100%;">
<thead>
<tr>
<th rowspan="2" style="text-align: center; vertical-align: middle;">Arrow Type</th>
<th colspan="3" style="text-align: center;">BigQuery Type</th>
</tr>
<tr>
<th style="text-align: center;">Bind</th>
<th style="text-align: center;">Ingest</th>
<th style="text-align: center;">Ingest (Storage Write API)</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;">

binary

</td>
<td colspan="3" style="text-align: center;">

BYTES

</td>
</tr>
<tr>
<td style="text-align: center;">

binary_view

</td>
<td style="text-align: center;">

BYTES

</td>
<td style="text-align: center;">

❌ [^9]

</td>
<td style="text-align: center;">

❌ [^10] [^11]

</td>
</tr>
<tr>
<td style="text-align: center;">

bool

</td>
<td colspan="3" style="text-align: center;">

BOOLEAN

</td>
</tr>
<tr>
<td style="text-align: center;">

date32[day]

</td>
<td colspan="3" style="text-align: center;">

DATE

</td>
</tr>
<tr>
<td style="text-align: center;">

decimal128

</td>
<td colspan="3" style="text-align: center;">

NUMERIC

</td>
</tr>
<tr>
<td style="text-align: center;">

double

</td>
<td colspan="3" style="text-align: center;">

FLOAT64

</td>
</tr>
<tr>
<td style="text-align: center;">

fixed_size_binary

</td>
<td colspan="3" style="text-align: center;">

BYTES

</td>
</tr>
<tr>
<td style="text-align: center;">

float

</td>
<td style="text-align: center;">

(not tested)

</td>
<td colspan="2" style="text-align: center;">

FLOAT64

</td>
</tr>
<tr>
<td style="text-align: center;">

int16

</td>
<td style="text-align: center;">

(not tested)

</td>
<td colspan="2" style="text-align: center;">

INT64

</td>
</tr>
<tr>
<td style="text-align: center;">

int32

</td>
<td style="text-align: center;">

(not tested)

</td>
<td colspan="2" style="text-align: center;">

INT64

</td>
</tr>
<tr>
<td style="text-align: center;">

int64

</td>
<td colspan="3" style="text-align: center;">

INT64

</td>
</tr>
<tr>
<td style="text-align: center;">

large_binary

</td>
<td colspan="3" style="text-align: center;">

BYTES

</td>
</tr>
<tr>
<td style="text-align: center;">

large_string

</td>
<td colspan="3" style="text-align: center;">

STRING

</td>
</tr>
<tr>
<td style="text-align: center;">

list

</td>
<td style="text-align: center;">

(not tested)

</td>
<td style="text-align: center;">

ARRAY [^12] [^13] [^14]

</td>
<td style="text-align: center;">

(not tested)

</td>
</tr>
<tr>
<td style="text-align: center;">

string

</td>
<td colspan="3" style="text-align: center;">

STRING

</td>
</tr>
<tr>
<td style="text-align: center;">

string_view

</td>
<td style="text-align: center;">

STRING

</td>
<td style="text-align: center;">

❌ [^15]

</td>
<td style="text-align: center;">

❌ [^16] [^17]

</td>
</tr>
<tr>
<td style="text-align: center;">

struct

</td>
<td style="text-align: center;">

(not tested)

</td>
<td colspan="2" style="text-align: center;">

STRUCT

</td>
</tr>
<tr>
<td style="text-align: center;">

time32[ms]

</td>
<td colspan="3" style="text-align: center;">

TIME

</td>
</tr>
<tr>
<td style="text-align: center;">

time32[s]

</td>
<td colspan="3" style="text-align: center;">

TIME

</td>
</tr>
<tr>
<td style="text-align: center;">

time64[ns]

</td>
<td style="text-align: center;">

❌ [^7]

</td>
<td style="text-align: center;">

❌ [^18]

</td>
<td style="text-align: center;">

❌ [^19]

</td>
</tr>
<tr>
<td style="text-align: center;">

time64[us]

</td>
<td colspan="3" style="text-align: center;">

TIME

</td>
</tr>
<tr>
<td style="text-align: center;">

timestamp[ms]

</td>
<td style="text-align: center;">

DATETIME

</td>
<td style="text-align: center;">

❌ [^20]

</td>
<td style="text-align: center;">

DATETIME

</td>
</tr>
<tr>
<td style="text-align: center;">

timestamp[ms] (with time zone)

</td>
<td colspan="3" style="text-align: center;">

TIMESTAMP

</td>
</tr>
<tr>
<td style="text-align: center;">

timestamp[ns]

</td>
<td style="text-align: center;">

DATETIME [^8]

</td>
<td style="text-align: center;">

❌ [^20]

</td>
<td style="text-align: center;">

❌ [^19]

</td>
</tr>
<tr>
<td style="text-align: center;">

timestamp[ns] (with time zone)

</td>
<td style="text-align: center;">

TIMESTAMP

</td>
<td style="text-align: center;">

❌ [^21]

</td>
<td style="text-align: center;">

❌ [^19]

</td>
</tr>
<tr>
<td style="text-align: center;">

timestamp[s]

</td>
<td style="text-align: center;">

DATETIME

</td>
<td style="text-align: center;">

❌ [^20]

</td>
<td style="text-align: center;">

DATETIME

</td>
</tr>
<tr>
<td style="text-align: center;">

timestamp[s] (with time zone)

</td>
<td colspan="3" style="text-align: center;">

TIMESTAMP

</td>
</tr>
<tr>
<td style="text-align: center;">

timestamp[us]

</td>
<td style="text-align: center;">

DATETIME

</td>
<td style="text-align: center;">

❌ [^20]

</td>
<td style="text-align: center;">

DATETIME

</td>
</tr>
<tr>
<td style="text-align: center;">

timestamp[us] (with time zone)

</td>
<td colspan="3" style="text-align: center;">

TIMESTAMP

</td>
</tr>
</tbody>
</table>

## Previous Versions

To see documentation for previous versions of this driver, see the following:

- [v1.11.0](./v1.11.0.md)
- [v1.10.0](./v1.10.0.md)
- [v1.0.0](./v1.0.0.md)

[^1]: BigQuery treats NULL arrays as empty arrays in result sets, even though you can differentiate between them during query execution.  See https://cloud.google.com/bigquery/docs/reference/standard-sql/data-types#array_nulls for more details.
[^2]: BigQuery's datetime is a naive timestamp; use TIMESTAMP for zoned timestamps
[^3]: Negative scales are not supported
[^4]: Scale must be in [0, 9]
[^5]: The declared precision/scale is ignored in queries: it will always be decimal128(38, 9)
[^6]: BigQuery's timestamp is effectively an Instant; use DATETIME for naive timestamps
[^7]: https://github.com/adbc-drivers/bigquery/issues/86
[^8]: Timestamp will be rounded to microseconds
[^9]: arrow-go does not support writing binary view to Parquet
[^10]: arrow-go does not support casting binary_view to binary
[^11]: BigQuery cannot natively ingest binary_view
[^12]: BigQuery does not support NULL lists; it will instead return an empty list
[^13]: BigQuery does not support NULL list elements; it will instead raise an error
[^14]: See the BigQuery documentation for the [ARRAY type](https://cloud.google.com/bigquery/docs/reference/standard-sql/data-types#array_type)
[^15]: arrow-go does not support writing string view to Parquet
[^16]: arrow-go does not support casting string_view to string
[^17]: BigQuery cannot natively ingest string_view
[^18]: This is broken on Google's side; it appears BigQuery treats time64[ns] as int64, and throws a type error
[^19]: The driver refuses to truncate to microseconds; it will work if the data is only microsecond precision and not nanosecond precision.
[^20]: This is broken on Google's side, as BigQuery doesn't properly parse Parquet types. See https://github.com/googleapis/google-cloud-python/issues/6542.
[^21]: From experimentation, it appears that BigQuery will accept nanosecond timestamps, but will interpret them as microseconds. Do not use!

[bigquery]: https://cloud.google.com/bigquery/
