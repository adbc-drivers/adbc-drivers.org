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

# Snowflake

:::{toctree}
:maxdepth: 1
:hidden:

v1.10.3.md
v1.10.1.md
v1.10.0.md
:::

[{badge-primary}`Driver Version|v1.10.3`](#driver-snowflake-v1.10.3 "Permalink") {badge-secondary}`Release Date|2026-03-10` {badge-success}`Tested With|Snowflake 10`

This driver provides access to [Snowflake][snowflake], a cloud-based data warehouse platform.

## Installation & Quickstart

The driver can be installed with [dbc](https://docs.columnar.tech/dbc):

```bash
dbc install snowflake
```

## Pre-requisites

Using the Snowflake driver requires a Snowflake account and authentication. See [Getting Started With Snowflake](https://docs.snowflake.com/en/user-guide-getting-started) for instructions.

## Connecting

To connect, replace the Snowflake options below with the appropriate values for your situation and run the following:

```python
from adbc_driver_manager import dbapi

conn = dbapi.connect(
    driver="snowflake",
    db_kwargs={
        "username": "USER",

        ### for username/password authentication: ###
        "adbc.snowflake.sql.auth_type": "auth_snowflake",
        "password": "PASS",

        ### for JWT authentication: ###
        #"adbc.snowflake.sql.auth_type": "auth_jwt",
        #"adbc.snowflake.sql.client_option.jwt_private_key": "/path/to/rsa_key.p8",

        "adbc.snowflake.sql.account": "ACCOUNT-IDENT",
        "adbc.snowflake.sql.db": "SNOWFLAKE_SAMPLE_DATA",
        "adbc.snowflake.sql.schema": "TPCH_SF1",
        "adbc.snowflake.sql.warehouse": "MY_WAREHOUSE",
        "adbc.snowflake.sql.role": "MY_ROLE"
    }
)
```

Note: The example above is for Python using the [adbc-driver-manager](https://pypi.org/project/adbc-driver-manager) package but the process will be similar for other driver managers.  See [adbc-quickstarts](https://github.com/columnar-tech/adbc-quickstarts).

The driver supports connecting with individual options or connection strings.

### Connection String Format

Snowflake URI syntax:

```
snowflake://user[:password]@host[:port]/database[/schema][?param1=value1&param2=value2]
```

This follows the [Go Snowflake Driver Connection String](https://pkg.go.dev/github.com/snowflakedb/gosnowflake#hdr-Connection_String) format with the addition of the `snowflake://` scheme.

Components:

- `scheme`: `snowflake://` (required)
- `user/password`: (optional) For username/password authentication
- `host`: (required) The Snowflake account identifier string (e.g., myorg-account1) OR the full hostname (e.g., private.network.com). If a full hostname is used, the actual Snowflake account identifier must be provided separately via the account query parameter (see example 3).
- `port`: The port is optional and defaults to 443.
- `database`: Database name (required)
- `schema`: Schema name (optional)
- `Query Parameters`: Additional configuration options. For a complete list of parameters, see the [Go Snowflake Driver Connection Parameters](https://pkg.go.dev/github.com/snowflakedb/gosnowflake#hdr-Connection_Parameters)

:::{note}
Reserved characters in URI elements must be URI-encoded. For example, `@` becomes `%40`.
:::

Examples:

- `snowflake://jane.doe:MyS3cr3t!@myorg-account1/ANALYTICS_DB/SALES_DATA?warehouse=WH_XL&role=ANALYST`
- `snowflake://service_user@myorg-account2/RAW_DATA_LAKE?authenticator=oauth&application=ADBC_APP`
- `snowflake://sys_admin@private.network.com:443/OPS_MONITOR/DBA?account=vpc-id-1234&insecureMode=true&client_session_keep_alive=true` (Uses full hostname, requires explicit account parameter)

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
      <td colspan="2">✅</td>
    </tr>
  </tbody>
</table>

### Types

#### Snowflake to Arrow

:::{list-table}
:header-rows: 1
:width: 100%
:widths: 1 3

* - Snowflake Type
  - Arrow Type
* - BIGINT
  - int64
* - BOOLEAN
  - bool
* - DATE
  - date32[day]
* - DOUBLE PRECISION
  - double
* - INT
  - int64
* - NUMERIC
  - double
* - REAL
  - double
* - SMALLINT
  - int64
* - TIME
  - time64[ns]
* - TIMESTAMP
  - timestamp[us]
* - TIMESTAMP WITH TIME ZONE
  - timestamp[us] (with time zone)
* - VARBINARY
  - binary
* - VARCHAR
  - string
:::

#### Arrow to Snowflake


<table class="docutils data align-default" style="width: 100%;">
<thead>
<tr>
<th rowspan="2" style="text-align: center; vertical-align: middle;">Arrow Type</th>
<th colspan="2" style="text-align: center;">Snowflake Type</th>
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
<td style="text-align: center;">

❌

</td>
<td style="text-align: center;">

BINARY

</td>
</tr>
<tr>
<td style="text-align: center;">

binary_view

</td>
<td colspan="2" style="text-align: center;">

❌

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
<td style="text-align: center;">

❌

</td>
<td style="text-align: center;">

DATE

</td>
</tr>
<tr>
<td style="text-align: center;">

decimal128

</td>
<td style="text-align: center;">

❌

</td>
<td style="text-align: center;">

(not tested)

</td>
</tr>
<tr>
<td style="text-align: center;">

double

</td>
<td style="text-align: center;">

DOUBLE PRECISION

</td>
<td style="text-align: center;">

NUMERIC, REAL, DOUBLE PRECISION

</td>
</tr>
<tr>
<td style="text-align: center;">

fixed_size_binary

</td>
<td style="text-align: center;">

❌

</td>
<td style="text-align: center;">

BINARY(n)

</td>
</tr>
<tr>
<td style="text-align: center;">

float

</td>
<td style="text-align: center;">

REAL

</td>
<td style="text-align: center;">

(not tested)

</td>
</tr>
<tr>
<td style="text-align: center;">

halffloat

</td>
<td style="text-align: center;">

❌

</td>
<td style="text-align: center;">

(not tested)

</td>
</tr>
<tr>
<td style="text-align: center;">

int16

</td>
<td style="text-align: center;">

SMALLINT

</td>
<td style="text-align: center;">

(not tested)

</td>
</tr>
<tr>
<td style="text-align: center;">

int32

</td>
<td style="text-align: center;">

INT

</td>
<td style="text-align: center;">

(not tested)

</td>
</tr>
<tr>
<td style="text-align: center;">

int64

</td>
<td style="text-align: center;">

BIGINT

</td>
<td style="text-align: center;">

BIGINT, SMALLINT, INT

</td>
</tr>
<tr>
<td style="text-align: center;">

large_binary

</td>
<td style="text-align: center;">

❌

</td>
<td style="text-align: center;">

BINARY

</td>
</tr>
<tr>
<td style="text-align: center;">

large_string

</td>
<td style="text-align: center;">

VARCHAR

</td>
<td style="text-align: center;">

STRING

</td>
</tr>
<tr>
<td style="text-align: center;">

string

</td>
<td style="text-align: center;">

VARCHAR

</td>
<td style="text-align: center;">

STRING

</td>
</tr>
<tr>
<td style="text-align: center;">

string_view

</td>
<td colspan="2" style="text-align: center;">

❌

</td>
</tr>
<tr>
<td style="text-align: center;">

time32[ms]

</td>
<td style="text-align: center;">

❌

</td>
<td style="text-align: center;">

TIME(3)

</td>
</tr>
<tr>
<td style="text-align: center;">

time32[s]

</td>
<td style="text-align: center;">

❌

</td>
<td style="text-align: center;">

TIME(0)

</td>
</tr>
<tr>
<td style="text-align: center;">

time64[ns]

</td>
<td style="text-align: center;">

❌

</td>
<td style="text-align: center;">

TIME(9)

</td>
</tr>
<tr>
<td style="text-align: center;">

time64[us]

</td>
<td style="text-align: center;">

❌

</td>
<td style="text-align: center;">

TIME(6)

</td>
</tr>
<tr>
<td style="text-align: center;">

timestamp[ms]

</td>
<td style="text-align: center;">

❌

</td>
<td style="text-align: center;">

TIMESTAMP_NTZ(3)

</td>
</tr>
<tr>
<td style="text-align: center;">

timestamp[ms] (with time zone)

</td>
<td style="text-align: center;">

❌

</td>
<td style="text-align: center;">

TIMESTAMP_LTZ(3)

</td>
</tr>
<tr>
<td style="text-align: center;">

timestamp[ns]

</td>
<td style="text-align: center;">

❌

</td>
<td style="text-align: center;">

TIMESTAMP_NTZ(9)

</td>
</tr>
<tr>
<td style="text-align: center;">

timestamp[ns] (with time zone)

</td>
<td style="text-align: center;">

❌

</td>
<td style="text-align: center;">

TIMESTAMP_LTZ(9)

</td>
</tr>
<tr>
<td style="text-align: center;">

timestamp[s]

</td>
<td style="text-align: center;">

❌

</td>
<td style="text-align: center;">

TIMESTAMP_NTZ(0)

</td>
</tr>
<tr>
<td style="text-align: center;">

timestamp[s] (with time zone)

</td>
<td style="text-align: center;">

❌

</td>
<td style="text-align: center;">

TIMESTAMP_LTZ(0)

</td>
</tr>
<tr>
<td style="text-align: center;">

timestamp[us]

</td>
<td style="text-align: center;">

❌

</td>
<td style="text-align: center;">

TIMESTAMP_NTZ(6)

</td>
</tr>
<tr>
<td style="text-align: center;">

timestamp[us] (with time zone)

</td>
<td style="text-align: center;">

❌

</td>
<td style="text-align: center;">

TIMESTAMP_LTZ(6)

</td>
</tr>
</tbody>
</table>



## Previous Versions

To see documentation for previous versions of this driver, see the following:

- [v1.10.1](./v1.10.0.md)
- [v1.10.0](./v1.10.0.md)

[snowflake]: https://www.snowflake.com/
