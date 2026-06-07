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

# Microsoft SQL Server

:::{toctree}
:maxdepth: 1
:hidden:

Changelog <changelog.md>
v1.4.1 <v1.4.1.md>
v1.4.0 <v1.4.0.md>
v1.3.1 <v1.3.1.md>
v1.3.0 <v1.3.0.md>
v1.2.0 <v1.2.0.md>
v1.1.0 <v1.1.0.md>
v1.0.0 <v1.0.0.md>
:::

:::{note}
This project is not associated with Microsoft.
:::

[{badge-primary}`Driver Version|v1.4.1`](#driver-mssql-v1.4.1 "Permalink") {badge-secondary}`Release Date|2026-05-22` {badge-success}`Tested With|Microsoft SQL Server 2025`

This driver provides access to [Microsoft SQL Server][mssql].

## Installation & Quickstart

The driver can be installed with [dbc](https://docs.columnar.tech/dbc):

```bash
dbc install mssql
```

## Connecting

To use the driver, provide a SQL Server connection string as the `uri` option. The driver supports URI format and DSN-style connection strings, but URIs are recommended.

```python
from adbc_driver_manager import dbapi

dbapi.connect(
  driver="mssql",
  db_kwargs={
      "uri": "mssql://sa:password@localhost:1433"
  }
)
```

Note: The example above is for Python using the [adbc-driver-manager](https://pypi.org/project/adbc-driver-manager) package but the process will be similar for other driver managers.  See [adbc-quickstarts](https://github.com/columnar-tech/adbc-quickstarts).

### Connection String Format

SQL Server URI syntax:

```
mssql://[user:[password]]@host[:port][/instance][?param1=value&param2=value]

sqlserver://[user:[password]]@host[:port][/instance][?param1=value&param2=value]
```

This follows the format of [Microsoft's official Go MSSQL driver](https://github.com/microsoft/go-mssqldb/tree/main?tab=readme-ov-file#the-connection-string-can-be-specified-in-one-of-three-formats).

Components:

- `scheme`: `mssql://` or `sqlserver://` (required) - both schemes are supported
- `user/password`: (optional) Credentials for standard SQL Server authentication.
- `host`: (required) The hostname or IP address of the SQL Server machine.
- `port`: (optional) Defaults to 1433.
- `instance`: (optional) The name of the SQL Server instance (e.g., SQLExpress).
- `Query Parameters`: Additional configuration options. For a list of common parameters, see the [Microsoft's official Go MSSQL driver](https://github.com/microsoft/go-mssqldb?tab=readme-ov-file#common-parameters)

:::{note}
Reserved characters in URI elements must be URI-encoded. For example, `@` becomes `%40`.
:::

Examples:

- `mssql://username:mypass@localhost?database=master&connection+timeout=30`
- `mssql://username:mypass@localhost:1234?database=master&connection+timeout=30`
- `mssql://username@localhost/SQLExpress?database=master&connection+timeout=30`
- `sqlserver://sa@localhost/SQLExpress?database=master&connection+timeout=30`
- `sqlserver://sa:mypass@localhost?database=master&connection+timeout=30`
- `sqlserver://sa:mypass@localhost:1234?database=master&connection+timeout=30`


EntraID (Azure Active Directory) authentication is enabled by adding a `fedauth` parameter to your connection URI. For more information, see the documentation for [Microsoft's official Go MSSQL driver](https://github.com/microsoft/go-mssqldb?tab=readme-ov-file#azure-active-directory-authentication).

This driver also supports other types of connection strings that are supported by [Microsoft's official Go MSSQL driver](https://github.com/microsoft/go-mssqldb/tree/main?tab=readme-ov-file#the-connection-string-can-be-specified-in-one-of-three-formats).

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
      <th style="text-align: center;">Microsoft SQL Server</th>
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
      <td colspan="1" style="text-align: center;">✅</td>
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
      <td colspan="1" style="text-align: center;">✅</td>
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
      <td colspan="1" style="text-align: center;">✅</td>
    </tr>
  </tbody>
</table>

### Types

#### Database to Arrow

<table class="docutils data align-default" style="width: 100%;">
<thead>
<tr>
<th style="text-align: left; vertical-align: middle;">Database Type</th>
<th style="text-align: center;">Microsoft SQL Server</th>
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

BIT

</td>
<td style="text-align: center;">

bool

</td>
</tr>
<tr>
<td style="text-align: left;">

CHAR

</td>
<td style="text-align: center;">

string

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

DATETIME

</td>
<td style="text-align: center;">

timestamp[us] (with time zone)

</td>
</tr>
<tr>
<td style="text-align: left;">

DATETIME2

</td>
<td style="text-align: center;">

timestamp[us] (with time zone)

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

DOUBLE PRECISION

</td>
<td style="text-align: center;">

double

</td>
</tr>
<tr>
<td style="text-align: left;">

GEOGRAPHY

</td>
<td style="text-align: center;">

extension&lt;geoarrow.wkb&gt;

</td>
</tr>
<tr>
<td style="text-align: left;">

GEOMETRY

</td>
<td style="text-align: center;">

extension&lt;geoarrow.wkb&gt;

</td>
</tr>
<tr>
<td style="text-align: left;">

IMAGE

</td>
<td style="text-align: center;">

binary

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

MONEY

</td>
<td style="text-align: center;">

decimal128

</td>
</tr>
<tr>
<td style="text-align: left;">

NCHAR

</td>
<td style="text-align: center;">

string

</td>
</tr>
<tr>
<td style="text-align: left;">

NTEXT

</td>
<td style="text-align: center;">

string

</td>
</tr>
<tr>
<td style="text-align: left;">

NTEXT (mssql.query.large_text_type = large_string)

</td>
<td style="text-align: center;">

large_string

</td>
</tr>
<tr>
<td style="text-align: left;">

NTEXT (mssql.query.large_text_type = string_view)

</td>
<td style="text-align: center;">

string_view

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

NVARCHAR

</td>
<td style="text-align: center;">

string

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

SMALLDATETIME

</td>
<td style="text-align: center;">

timestamp[us] (with time zone)

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

SMALLMONEY

</td>
<td style="text-align: center;">

decimal128

</td>
</tr>
<tr>
<td style="text-align: left;">

TEXT

</td>
<td style="text-align: center;">

string

</td>
</tr>
<tr>
<td style="text-align: left;">

TEXT (mssql.query.large_text_type = large_string)

</td>
<td style="text-align: center;">

large_string

</td>
</tr>
<tr>
<td style="text-align: left;">

TEXT (mssql.query.large_text_type = string_view)

</td>
<td style="text-align: center;">

string_view

</td>
</tr>
<tr>
<td style="text-align: left;">

TIME

</td>
<td style="text-align: center;">

time64[ns] ⚠️ [^1]

</td>
</tr>
<tr>
<td style="text-align: left;">

TIME(0)

</td>
<td style="text-align: center;">

time32[s]

</td>
</tr>
<tr>
<td style="text-align: left;">

TIME(1)

</td>
<td style="text-align: center;">

time32[ms]

</td>
</tr>
<tr>
<td style="text-align: left;">

TIME(2)

</td>
<td style="text-align: center;">

time32[ms]

</td>
</tr>
<tr>
<td style="text-align: left;">

TIME(3)

</td>
<td style="text-align: center;">

time32[ms]

</td>
</tr>
<tr>
<td style="text-align: left;">

TIME(4)

</td>
<td style="text-align: center;">

time64[us]

</td>
</tr>
<tr>
<td style="text-align: left;">

TIME(5)

</td>
<td style="text-align: center;">

time64[us]

</td>
</tr>
<tr>
<td style="text-align: left;">

TIME(6)

</td>
<td style="text-align: center;">

time64[us]

</td>
</tr>
<tr>
<td style="text-align: left;">

TIME(7)

</td>
<td style="text-align: center;">

time64[ns]

</td>
</tr>
<tr>
<td style="text-align: left;">

TINYINT

</td>
<td style="text-align: center;">

uint8

</td>
</tr>
<tr>
<td style="text-align: left;">

UNIQUEIDENTIFIER

</td>
<td style="text-align: center;">

extension&lt;arrow.uuid&gt;

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
<tr>
<td style="text-align: left;">

XML

</td>
<td style="text-align: center;">

string

</td>
</tr>
</tbody>
</table>

#### Arrow to Database

<table class="docutils data align-default" style="width: 100%;">
<thead>
<tr>
<th rowspan="3" style="text-align: left; vertical-align: middle;">Arrow Type</th>
<th colspan="2" style="text-align: center;">Microsoft SQL Server Type</th>
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
<td style="text-align: center;">

VARBINARY

</td>
<td style="text-align: center;">

VARBINARY(MAX)

</td>
</tr>
<tr>
<td style="text-align: left;">

binary_view

</td>
<td style="text-align: center;">

VARBINARY

</td>
<td style="text-align: center;">

VARBINARY(MAX)

</td>
</tr>
<tr>
<td style="text-align: left;">

bool

</td>
<td colspan="2" style="text-align: center;">

BIT

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

DECIMAL(10,2)

</td>
<td style="text-align: center;">

NUMERIC

</td>
</tr>
<tr>
<td style="text-align: left;">

double

</td>
<td colspan="2" style="text-align: center;">

DOUBLE PRECISION

</td>
</tr>
<tr>
<td style="text-align: left;">

extension&lt;geoarrow.wkb&gt;

</td>
<td style="text-align: center;">

(NA/not tested)

</td>
<td style="text-align: center;">

GEOGRAPHY, GEOMETRY

</td>
</tr>
<tr>
<td style="text-align: left;">

fixed_size_binary

</td>
<td style="text-align: center;">

VARBINARY

</td>
<td style="text-align: center;">

VARBINARY(MAX)

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
<tr>
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
<td style="text-align: center;">

VARBINARY

</td>
<td style="text-align: center;">

VARBINARY(MAX)

</td>
</tr>
<tr>
<td style="text-align: left;">

large_string

</td>
<td style="text-align: center;">

NVARCHAR

</td>
<td style="text-align: center;">

NVARCHAR(MAX)

</td>
</tr>
<tr>
<td style="text-align: left;">

string

</td>
<td style="text-align: center;">

NVARCHAR

</td>
<td style="text-align: center;">

NVARCHAR(MAX)

</td>
</tr>
<tr>
<td style="text-align: left;">

string_view

</td>
<td style="text-align: center;">

NVARCHAR

</td>
<td style="text-align: center;">

NVARCHAR(MAX)

</td>
</tr>
<tr>
<td style="text-align: left;">

time32[ms]

</td>
<td style="text-align: center;">

TIME(3), TIME(2), TIME, TIME(1)

</td>
<td style="text-align: center;">

TIME(7) ⚠️ [^3]

</td>
</tr>
<tr>
<td style="text-align: left;">

time32[s]

</td>
<td style="text-align: center;">

TIME, TIME(0)

</td>
<td style="text-align: center;">

TIME(7) ⚠️ [^3]

</td>
</tr>
<tr>
<td style="text-align: left;">

time64[ns]

</td>
<td style="text-align: center;">

TIME, TIME(7)

</td>
<td style="text-align: center;">

TIME(7) ⚠️ [^3]

</td>
</tr>
<tr>
<td style="text-align: left;">

time64[us]

</td>
<td style="text-align: center;">

TIME(6), TIME(5), TIME(4), TIME

</td>
<td style="text-align: center;">

TIME(7) ⚠️ [^3]

</td>
</tr>
<tr>
<td style="text-align: left;">

timestamp[ms]

</td>
<td colspan="2" style="text-align: center;">

DATETIME2

</td>
</tr>
<tr>
<td style="text-align: left;">

timestamp[ms] (with time zone)

</td>
<td colspan="2" style="text-align: center;">

DATETIME2

</td>
</tr>
<tr>
<td style="text-align: left;">

timestamp[ns]

</td>
<td style="text-align: center;">

DATETIME2 [^2]

</td>
<td style="text-align: center;">

DATETIME2

</td>
</tr>
<tr>
<td style="text-align: left;">

timestamp[ns] (with time zone)

</td>
<td style="text-align: center;">

DATETIME2 [^2]

</td>
<td style="text-align: center;">

DATETIME2

</td>
</tr>
<tr>
<td style="text-align: left;">

timestamp[s]

</td>
<td colspan="2" style="text-align: center;">

DATETIME2

</td>
</tr>
<tr>
<td style="text-align: left;">

timestamp[s] (with time zone)

</td>
<td colspan="2" style="text-align: center;">

DATETIME2

</td>
</tr>
<tr>
<td style="text-align: left;">

timestamp[us]

</td>
<td colspan="2" style="text-align: center;">

DATETIME2

</td>
</tr>
<tr>
<td style="text-align: left;">

timestamp[us] (with time zone)

</td>
<td colspan="2" style="text-align: center;">

DATETIME2

</td>
</tr>
</tbody>
</table>

## Options

### Options Affecting Queries

`mssql.query.large_text_type`
: Values: `string`, `string_view`, or `large_string`. Default: `string`

  Determines the Arrow string type to use for `VARCHAR(MAX)` and
  `NVARCHAR(MAX)` (and their deprecated aliases `TEXT` and `NTEXT`) columns.

  This does not affect bulk ingest.

## Compatibility

This driver was tested on:

- Microsoft SQL Server `17.0.4045.5 Enterprise Evaluation Edition (64-bit)`

## Previous Versions

To see documentation for previous versions of this driver, see the following:

- [v1.3.1](./v1.3.1.md)
- [v1.3.0](./v1.3.0.md)
- [v1.2.0](./v1.2.0.md)
- [v1.1.0](./v1.1.0.md)
- [v1.0.0](./v1.0.0.md)

[^1]: while the documentation claims 7 digits of precision, the client only receives 6
[^2]: Values rounded to microsecond precision
[^3]: ingested as TIME(7)

[mssql]: https://www.microsoft.com/sql-server
