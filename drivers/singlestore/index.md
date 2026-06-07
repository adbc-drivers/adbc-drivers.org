---
# Copyright (c) 2025 ADBC Drivers Contributors
# Copyright (c) 2026 SingleStore, Inc.
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

# SingleStore

:::{toctree}
:maxdepth: 1
:hidden:

v0.1.0-beta.1.md
:::

[{badge-primary}`Driver Version|v0.1.0-beta.1`](#driver-singlestore-v0.1.0-beta.1 "Permalink") {badge-secondary}`Release Date|2026-04-01` {badge-success}`Tested With|SingleStore 9.0.20`

This driver provides access to [SingleStore][singlestore]{target="_blank"}, a distributed database for low-latency SQL. It is developed by SingleStore, Inc. The source code can be found at [singlestore-adbc-connector](https://github.com/singlestore-labs/singlestore-adbc-connector); the ADBC Driver Foundry distributes precompiled binaries of the upstream sources for Linux, macOS, and Windows.

## Installation

The SingleStore driver can be installed with [dbc](https://docs.columnar.tech/dbc):

```bash
dbc install --pre singlestore
```

:::{note}
Only prerelease versions of the driver are currently available, so you must use `--pre` with dbc 0.2.0 or newer to install the driver.
:::

## Connecting

To connect, edit the `uri` option below to match your environment and run the following:

```python
from adbc_driver_manager import dbapi

conn = dbapi.connect(
  driver="singlestore",
  db_kwargs = {
    "uri": "root@tcp(localhost:3306)/demo"
  }
)
```

Note: The example above is for Python using the [adbc-driver-manager](https://pypi.org/project/adbc-driver-manager) package but the process will be similar for other driver managers.

### Connection String Format

Connection strings are passed with the `uri` option which uses the following format:

```text
mysql://[user[:[password]]@]host[:port][/schema][?attribute1=value1&attribute2=value2...]
```

Examples:

- `mysql://localhost/mydb`
- `mysql://user:pass@localhost:3306/mydb`
- `mysql://user:pass@host/db?charset=utf8mb4&timeout=30s`
- `mysql://user@(/path/to/socket.sock)/db` (Unix domain socket)
- `mysql://user@localhost/mydb` (no password)

This follows MySQL's official [URI-like connection string format](https://dev.mysql.com/doc/refman/8.4/en/connecting-using-uri-or-key-value-pairs.html#connecting-using-uri). Also see [MySQL Connection Parameters](https://dev.mysql.com/doc/refman/8.4/en/connecting-using-uri-or-key-value-pairs.html#connection-parameters-base) for the complete specification.

Components:
- `scheme`: `mysql://` (required)
- `user`: Optional (for authentication)
- `password`: Optional (for authentication, requires user)
- `host`: Required (must be explicitly specified)
- `port`: Optional (defaults to 3306)
- `schema`: Optional (can be empty, SingleStore database name)
- Query params: SingleStore connection attributes

:::{note}
Reserved characters in URI elements must be URI-encoded. For example, `@` becomes `%40`. If you include a zone ID in an IPv6 address, the `%` character used as the separator must be replaced with `%25`.
:::

When connecting via Unix domain sockets, use the parentheses syntax to wrap the socket path: `(/path/to/socket.sock)`.

The driver also supports the SingleStore DSN format (see [Go SingleStore Driver documentation](https://github.com/singlestore-labs/go-singlestore-driver?tab=readme-ov-file#dsn-data-source-name)), but standard URIs are recommended.

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
      <td>✅</td>
    </tr>
    <tr>
      <td>Specify target schema</td>
      <td>❌</td>
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

### Driver-Specific Features

<table class="docutils data align-default" style="width: 100%">
  <colgroup>
    <col span="1" style="width: 25%;">
    <col span="1" style="width: 25%;">
    <col span="1" style="width: 10%;">
    <col span="1" style="width: 40%;">
  </colgroup>
  <thead>
    <tr>
      <th>Feature</th>
      <th>Name</th>
      <th>Support</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
            <tr>
          <td rowspan="1">Configuration</td>
          <td>Connect with URI</td>
      <td>✅</td>
      <td>Test authentication with credentials embedded in URI.</td>
    </tr>
          </tbody>
</table>

### Types

#### SingleStore to Arrow

:::{list-table}
:header-rows: 1
:width: 100%
:widths: 1 3

* - SingleStore Type
  - Arrow Type
* - BIGINT
  - int64
* - BIT
  - binary
* - BOOLEAN
  - int64, int8 ⚠️ [^1]
* - DATE
  - date32[day]
* - DATETIME
  - timestamp[us]
* - DOUBLE PRECISION
  - double
* - FLOAT
  - float
* - INT
  - int32
* - JSON
  - extension&lt;arrow.json&gt;
* - NUMERIC
  - decimal64
* - REAL
  - float
* - SMALLINT
  - int16
* - TIME
  - time64[us]
* - TIMESTAMP
  - timestamp[us], timestamp[us] (with time zone) ⚠️ [^1]
* - VARBINARY
  - binary
* - VARCHAR
  - string
:::

#### Arrow to SingleStore


<table class="docutils data align-default" style="width: 100%;">
<thead>
<tr>
<th rowspan="2" style="text-align: center; vertical-align: middle;">Arrow Type</th>
<th colspan="2" style="text-align: center;">SingleStore Type</th>
</tr>
<tr>
<th style="text-align: center;">Bind</th>
<th style="text-align: center;">Ingest</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;">

binary

</td>
<td colspan="2" style="text-align: center;">

VARBINARY

</td>
</tr>
<tr>
<td style="text-align: center;">

binary_view

</td>
<td colspan="2" style="text-align: center;">

VARBINARY

</td>
</tr>
<tr>
<td style="text-align: center;">

bool

</td>
<td colspan="2" style="text-align: center;">

BOOLEAN

</td>
</tr>
<tr>
<td style="text-align: center;">

date32[day]

</td>
<td colspan="2" style="text-align: center;">

DATE

</td>
</tr>
<tr>
<td style="text-align: center;">

decimal128

</td>
<td colspan="2" style="text-align: center;">

DECIMAL

</td>
</tr>
<tr>
<td style="text-align: center;">

double

</td>
<td colspan="2" style="text-align: center;">

DOUBLE PRECISION

</td>
</tr>
<tr>
<td style="text-align: center;">

fixed_size_binary

</td>
<td colspan="2" style="text-align: center;">

VARBINARY

</td>
</tr>
<tr>
<td style="text-align: center;">

float

</td>
<td colspan="2" style="text-align: center;">

FLOAT

</td>
</tr>
<tr>
<td style="text-align: center;">

int16

</td>
<td colspan="2" style="text-align: center;">

SMALLINT

</td>
</tr>
<tr>
<td style="text-align: center;">

int32

</td>
<td colspan="2" style="text-align: center;">

INT

</td>
</tr>
<tr>
<td style="text-align: center;">

int64

</td>
<td colspan="2" style="text-align: center;">

BIGINT

</td>
</tr>
<tr>
<td style="text-align: center;">

large_binary

</td>
<td colspan="2" style="text-align: center;">

VARBINARY

</td>
</tr>
<tr>
<td style="text-align: center;">

large_string

</td>
<td colspan="2" style="text-align: center;">

VARCHAR

</td>
</tr>
<tr>
<td style="text-align: center;">

string

</td>
<td colspan="2" style="text-align: center;">

VARCHAR

</td>
</tr>
<tr>
<td style="text-align: center;">

string_view

</td>
<td colspan="2" style="text-align: center;">

VARCHAR

</td>
</tr>
<tr>
<td style="text-align: center;">

time32[ms]

</td>
<td colspan="2" style="text-align: center;">

TIME

</td>
</tr>
<tr>
<td style="text-align: center;">

time32[s]

</td>
<td colspan="2" style="text-align: center;">

TIME

</td>
</tr>
<tr>
<td style="text-align: center;">

time64[ns]

</td>
<td colspan="2" style="text-align: center;">

TIME

</td>
</tr>
<tr>
<td style="text-align: center;">

time64[us]

</td>
<td colspan="2" style="text-align: center;">

TIME

</td>
</tr>
<tr>
<td style="text-align: center;">

timestamp[ms]

</td>
<td colspan="2" style="text-align: center;">

DATETIME

</td>
</tr>
<tr>
<td style="text-align: center;">

timestamp[ms] (with time zone)

</td>
<td colspan="2" style="text-align: center;">

TIMESTAMP

</td>
</tr>
<tr>
<td style="text-align: center;">

timestamp[ns]

</td>
<td colspan="2" style="text-align: center;">

DATETIME

</td>
</tr>
<tr>
<td style="text-align: center;">

timestamp[ns] (with time zone)

</td>
<td colspan="2" style="text-align: center;">

TIMESTAMP

</td>
</tr>
<tr>
<td style="text-align: center;">

timestamp[s]

</td>
<td colspan="2" style="text-align: center;">

DATETIME

</td>
</tr>
<tr>
<td style="text-align: center;">

timestamp[s] (with time zone)

</td>
<td colspan="2" style="text-align: center;">

TIMESTAMP

</td>
</tr>
<tr>
<td style="text-align: center;">

timestamp[us]

</td>
<td colspan="2" style="text-align: center;">

DATETIME

</td>
</tr>
<tr>
<td style="text-align: center;">

timestamp[us] (with time zone)

</td>
<td colspan="2" style="text-align: center;">

TIMESTAMP

</td>
</tr>
</tbody>
</table>

## Compatibility

This driver was tested on the following versions of SingleStore:

- 9.0.20 (SingleStoreDB source distribution (compatible; MySQL Enterprise & MySQL Commercial))

[^1]: Return type is inconsistent depending on how the query was written

[singlestore]: https://www.singlestore.com/
