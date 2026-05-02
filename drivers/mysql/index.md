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

# MySQL/MariaDB

:::{toctree}
:maxdepth: 1
:hidden:

changelog.md
v0.3.1.md
v0.3.0.md
v0.2.0.md
v0.1.0.md
:::

[{badge-primary}`Driver Version|v0.3.1`](#driver-mysql-v0.3.1 "Permalink") {badge-success}`Tested With|MySQL 9.4`

This driver provides access to [MySQL][mysql]{target="_blank"}, a free and
open-source relational database management system.

## Installation

The MySQL driver can be installed with [dbc](https://docs.columnar.tech/dbc):

```bash
dbc install mysql
```

## Connecting

To connect, edit the `uri` option below to match your environment and run the following:

```python
from adbc_driver_manager import dbapi

conn = dbapi.connect(
  driver="mysql",
  db_kwargs = {
    "uri": "root@tcp(localhost:3306)/demo"
  }
)
```

Note: The example above is for Python using the [adbc-driver-manager](https://pypi.org/project/adbc-driver-manager) package but the process will be similar for other driver managers. See [adbc-quickstarts](https://github.com/columnar-tech/adbc-quickstarts).

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
- `schema`: Optional (can be empty, MySQL database name)
- Query params: MySQL connection attributes

:::{note}
Reserved characters in URI elements must be URI-encoded. For example, `@` becomes `%40`. If you include a zone ID in an IPv6 address, the `%` character used as the separator must be replaced with `%25`.
:::

When connecting via Unix domain sockets, use the parentheses syntax to wrap the socket path: `(/path/to/socket.sock)`.

The driver also supports the MySQL DSN format (see [Go MySQL Driver documentation](https://github.com/go-sql-driver/mysql?tab=readme-ov-file#dsn-data-source-name)), but standard URIs are recommended.

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
      <td>✅</td>
    </tr>
    <tr>
      <td>Specify target catalog</td>
      <td>❌</td>
    </tr>
    <tr>
      <td>Specify target schema</td>
      <td>❌</td>
    </tr>
    <tr>
      <td>Non-nullable fields are marked NOT NULL</td>
      <td>❌</td>
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
      <td colspan="2">❌</td>
    </tr>
  </tbody>
</table>

### Types

#### MySQL to Arrow

:::{list-table}
:header-rows: 1
:width: 100%
:widths: 1 3

* - MySQL Type
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
* - INT
  - int32
* - JSON
  - extension&lt;arrow.json&gt;
* - NUMERIC
  - decimal64
* - REAL
  - ❌
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

#### Arrow to MySQL


<table class="docutils data align-default" style="width: 100%;">
<thead>
<tr>
<th rowspan="2" style="text-align: center; vertical-align: middle;">Arrow Type</th>
<th colspan="2" style="text-align: center;">MySQL Type</th>
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

❌

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

This driver was tested on the following versions of MySQL:

- 9.4.0 (MySQL Community Server - GPL)

## Previous Versions

To see documentation for previous versions of this driver, see the following:

- [v0.3.0](./v0.3.0.md)
- [v0.2.0](./v0.2.0.md)
- [v0.1.0](./v0.1.0.md)

[^1]: Return type is inconsistent depending on how the query was written

[mysql]: https://www.mysql.com/
