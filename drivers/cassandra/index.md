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

# Apache Cassandra

:::{toctree}
:maxdepth: 1
:hidden:

Changelog <changelog.md>
v0.1.0-alpha.1 <v0.1.0-alpha.1.md>
:::

{badge-primary}`Driver Version|v0.1.0-alpha.1` {badge-secondary}`Release Date|2026-08-24` {badge-success}`Tested With|Apache Cassandra 5.0` {badge-success}`Tested With|DataStax Enterprise 6.9`

:::{warning}
This is documentation for a prerelease version.
:::

This driver provides access to [Apache Cassandra][cassandra], a distributed,
open-source NoSQL database.

## Installation

The Cassandra driver can be installed with
[dbc](https://docs.columnar.tech/dbc):

```bash
dbc install --pre cassandra
```

## Connecting

To connect, provide a Cassandra connection string as the `uri` option:

```python
from adbc_driver_manager import dbapi

conn = dbapi.connect(
    driver="cassandra",
    db_kwargs={
        "uri": "cassandra://localhost:9042/my_keyspace",
    },
)
```

The example uses Python and the
[adbc-driver-manager](https://pypi.org/project/adbc-driver-manager) package,
but the same options apply through other ADBC driver managers. See
[adbc-quickstarts](https://github.com/columnar-tech/adbc-quickstarts) for
end-to-end examples.

### Connection String Format

```text
cassandra://[username[:password]@][host[:port]][/keyspace][?parameter1=value1&parameter2=value2...]
```

Components:

- `scheme`: `cassandra://` (required)
- `username`: Username for authentication (optional)
- `password`: Password for authentication (optional; requires a username)
- `host`: Cassandra contact point (optional; defaults to `127.0.0.1`)
- `port`: Native transport port (optional; defaults to `9042`)
- `keyspace`: Initial keyspace (optional)
- Query parameters: Connection options listed below

Examples:

- `cassandra://localhost:9042/my_keyspace`
- `cassandra://user:password@cassandra.example.com/my_keyspace`
- `cassandra://localhost/my_keyspace?page_size=1000&consistency=ONE&timeout=5000`
- `cassandra:///my_keyspace?enable_tls=true&tls_ca_path=%2Fpath%2Fto%2Fca.pem`

The URI accepts one contact point. To supply multiple contact points, use the
`cassandra.hosts` option instead. Query parameter values must be URL-encoded
when necessary. Unknown or repeated query parameters are rejected. Options
specified separately from the URI take precedence over URI values.

## Feature & Type Support

<table class="docutils data align-default" style="width: 100%">
  <colgroup>
    <col span="1" style="width: 25%;">
    <col span="1" style="width: 25%;">
    <col span="1" style="width: 25.0%;">
    <col span="1" style="width: 25.0%;">
  </colgroup>
  <thead>
    <tr>
      <th colspan="2">Feature</th>
      <th style="text-align: center;">Apache Cassandra</th>
      <th style="text-align: center;">DataStax Enterprise</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td colspan="2">Bind Parameters</td>
      <td colspan="2" style="text-align: center;">✅</td>
    </tr>
    <tr>
      <td rowspan="8">Bulk Ingestion</td>
      <td>Create</td>
      <td colspan="2" style="text-align: center;">✅</td>
    </tr>
    <tr>
      <td>Append</td>
      <td colspan="2" style="text-align: center;">✅</td>
    </tr>
    <tr>
      <td>Create/Append</td>
      <td colspan="2" style="text-align: center;">✅</td>
    </tr>
    <tr>
      <td>Replace</td>
      <td colspan="2" style="text-align: center;">✅</td>
    </tr>
    <tr>
      <td>Temporary Table</td>
      <td colspan="2" style="text-align: center;">❌</td>
    </tr>
    <tr>
      <td>Target Catalog</td>
      <td colspan="2" style="text-align: center;">❌</td>
    </tr>
    <tr>
      <td>Target Schema</td>
      <td colspan="2" style="text-align: center;">❌</td>
    </tr>
    <tr>
      <td>Non-nullable fields are marked NOT NULL</td>
      <td colspan="2" style="text-align: center;">❌</td>
    </tr>
    <tr>
      <td rowspan="4">Catalog (GetObjects)</td>
      <td>depth=catalogs</td>
      <td colspan="2" style="text-align: center;">❌</td>
    </tr>
    <tr>
      <td>depth=db_schemas</td>
      <td colspan="2" style="text-align: center;">❌</td>
    </tr>
    <tr>
      <td>depth=tables</td>
      <td colspan="2" style="text-align: center;">❌</td>
    </tr>
    <tr>
      <td>depth=columns (all)</td>
      <td colspan="2" style="text-align: center;">❌</td>
    </tr>
    <tr>
      <td colspan="2">Get Parameter Schema</td>
      <td colspan="2" style="text-align: center;">❌</td>
    </tr>
    <tr>
      <td colspan="2">Get Table Schema</td>
      <td colspan="2" style="text-align: center;">✅</td>
    </tr>
    <tr>
      <td colspan="2">Prepared Statements</td>
      <td colspan="2" style="text-align: center;">✅</td>
    </tr>
    <tr>
      <td colspan="2">Transactions</td>
      <td colspan="2" style="text-align: center;">❌</td>
    </tr>
  </tbody>
</table>

### Types

#### Database to Arrow

<table class="docutils data align-default" style="width: 100%;">
<colgroup>
<col span="1" style="width: 33.333333333333336%;">
<col span="1" style="width: 33.333333333333336%;">
<col span="1" style="width: 33.333333333333336%;">
</colgroup>
<thead>
<tr>
<th style="text-align: left; vertical-align: middle;">Database Type</th>
<th style="text-align: center;">Apache Cassandra</th>
<th style="text-align: center;">DataStax Enterprise</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">

BIGINT

</td>
<td colspan="2" style="text-align: center;">

int64

</td>
</tr>
<tr>
<td style="text-align: left;">

BOOLEAN

</td>
<td colspan="2" style="text-align: center;">

bool

</td>
</tr>
<tr>
<td style="text-align: left;">

DATE

</td>
<td colspan="2" style="text-align: center;">

date32[day]

</td>
</tr>
<tr>
<td style="text-align: left;">

DOUBLE PRECISION

</td>
<td colspan="2" style="text-align: center;">

double

</td>
</tr>
<tr>
<td style="text-align: left;">

INT

</td>
<td colspan="2" style="text-align: center;">

int32

</td>
</tr>
<tr>
<td style="text-align: left;">

LIST

</td>
<td colspan="2" style="text-align: center;">

list

</td>
</tr>
<tr>
<td style="text-align: left;">

MAP

</td>
<td colspan="2" style="text-align: center;">

map&lt;string, int32&gt; [^1]

</td>
</tr>
<tr>
<td style="text-align: left;">

NUMERIC

</td>
<td colspan="2" style="text-align: center;">

decimal128

</td>
</tr>
<tr>
<td style="text-align: left;">

REAL

</td>
<td colspan="2" style="text-align: center;">

float

</td>
</tr>
<tr>
<td style="text-align: left;">

SET

</td>
<td colspan="2" style="text-align: center;">

list

</td>
</tr>
<tr>
<td style="text-align: left;">

SMALLINT

</td>
<td colspan="2" style="text-align: center;">

int16

</td>
</tr>
<tr>
<td style="text-align: left;">

TIME

</td>
<td colspan="2" style="text-align: center;">

time64[ns]

</td>
</tr>
<tr>
<td style="text-align: left;">

TIMESTAMP

</td>
<td colspan="2" style="text-align: center;">

timestamp[ms]

</td>
</tr>
<tr>
<td style="text-align: left;">

TIMESTAMP(p) (1 &lt;= p &lt;= 3)

</td>
<td colspan="2" style="text-align: center;">

timestamp[ms]

</td>
</tr>
<tr>
<td style="text-align: left;">

VARBINARY

</td>
<td colspan="2" style="text-align: center;">

binary

</td>
</tr>
<tr>
<td style="text-align: left;">

VARCHAR

</td>
<td colspan="2" style="text-align: center;">

string

</td>
</tr>
</tbody>
</table>

#### Arrow to Database

<table class="docutils data align-default" style="width: 100%;">
<colgroup>
<col span="1" style="width: 25%;">
<col span="1" style="width: 18.75%;">
<col span="1" style="width: 18.75%;">
<col span="1" style="width: 18.75%;">
<col span="1" style="width: 18.75%;">
</colgroup>
<thead>
<tr>
<th rowspan="3" style="text-align: left; vertical-align: middle;">Arrow Type</th>
<th colspan="2" style="text-align: center;">Apache Cassandra Type</th>
<th colspan="2" style="text-align: center;">DataStax Enterprise Type</th>
</tr>
<tr>
<th style="text-align: center;">Bind</th>
<th style="text-align: center;">Ingest</th>
<th style="text-align: center;">Bind</th>
<th style="text-align: center;">Ingest</th>
</tr>
</thead>
<tbody>
<tr class="row-with-cell-borders">
<td style="text-align: left;">

binary

</td>
<td style="text-align: center;">

BLOB

</td>
<td style="text-align: center;">

VARBINARY

</td>
<td style="text-align: center;">

BLOB

</td>
<td style="text-align: center;">

VARBINARY

</td>
</tr>
<tr class="row-with-cell-borders">
<td style="text-align: left;">

binary_view

</td>
<td style="text-align: center;">

BLOB

</td>
<td style="text-align: center;">

VARBINARY

</td>
<td style="text-align: center;">

BLOB

</td>
<td style="text-align: center;">

VARBINARY

</td>
</tr>
<tr>
<td style="text-align: left;">

bool

</td>
<td colspan="4" style="text-align: center;">

BOOLEAN

</td>
</tr>
<tr>
<td style="text-align: left;">

date32[day]

</td>
<td colspan="4" style="text-align: center;">

DATE

</td>
</tr>
<tr class="row-with-cell-borders">
<td style="text-align: left;">

decimal128

</td>
<td style="text-align: center;">

DECIMAL

</td>
<td style="text-align: center;">

NUMERIC

</td>
<td style="text-align: center;">

DECIMAL

</td>
<td style="text-align: center;">

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
<td style="text-align: center;">

DOUBLE

</td>
<td style="text-align: center;">

DOUBLE PRECISION

</td>
</tr>
<tr class="row-with-cell-borders">
<td style="text-align: left;">

fixed_size_binary

</td>
<td style="text-align: center;">

BLOB

</td>
<td style="text-align: center;">

VARBINARY

</td>
<td style="text-align: center;">

BLOB

</td>
<td style="text-align: center;">

VARBINARY

</td>
</tr>
<tr class="row-with-cell-borders">
<td style="text-align: left;">

float

</td>
<td style="text-align: center;">

FLOAT

</td>
<td style="text-align: center;">

REAL

</td>
<td style="text-align: center;">

FLOAT

</td>
<td style="text-align: center;">

REAL

</td>
</tr>
<tr class="row-with-cell-borders">
<td style="text-align: left;">

halffloat

</td>
<td style="text-align: center;">

FLOAT

</td>
<td style="text-align: center;">

(NA/not tested)

</td>
<td style="text-align: center;">

FLOAT

</td>
<td style="text-align: center;">

(NA/not tested)

</td>
</tr>
<tr>
<td style="text-align: left;">

int16

</td>
<td colspan="4" style="text-align: center;">

SMALLINT

</td>
</tr>
<tr>
<td style="text-align: left;">

int32

</td>
<td colspan="4" style="text-align: center;">

INT

</td>
</tr>
<tr>
<td style="text-align: left;">

int64

</td>
<td colspan="4" style="text-align: center;">

BIGINT

</td>
</tr>
<tr class="row-with-cell-borders">
<td style="text-align: left;">

large_binary

</td>
<td style="text-align: center;">

BLOB

</td>
<td style="text-align: center;">

VARBINARY

</td>
<td style="text-align: center;">

BLOB

</td>
<td style="text-align: center;">

VARBINARY

</td>
</tr>
<tr class="row-with-cell-borders">
<td style="text-align: left;">

large_string

</td>
<td style="text-align: center;">

TEXT

</td>
<td style="text-align: center;">

VARCHAR

</td>
<td style="text-align: center;">

TEXT

</td>
<td style="text-align: center;">

VARCHAR

</td>
</tr>
<tr class="row-with-cell-borders">
<td style="text-align: left;">

list

</td>
<td style="text-align: center;">

LIST, SET

</td>
<td style="text-align: center;">

LIST

</td>
<td style="text-align: center;">

LIST, SET

</td>
<td style="text-align: center;">

LIST

</td>
</tr>
<tr>
<td style="text-align: left;">

map&lt;string, int32&gt;

</td>
<td colspan="4" style="text-align: center;">

MAP [^1]

</td>
</tr>
<tr class="row-with-cell-borders">
<td style="text-align: left;">

string

</td>
<td style="text-align: center;">

TEXT

</td>
<td style="text-align: center;">

VARCHAR

</td>
<td style="text-align: center;">

TEXT

</td>
<td style="text-align: center;">

VARCHAR

</td>
</tr>
<tr class="row-with-cell-borders">
<td style="text-align: left;">

string_view

</td>
<td style="text-align: center;">

TEXT

</td>
<td style="text-align: center;">

VARCHAR

</td>
<td style="text-align: center;">

TEXT

</td>
<td style="text-align: center;">

VARCHAR

</td>
</tr>
<tr>
<td style="text-align: left;">

time32[ms]

</td>
<td colspan="4" style="text-align: center;">

TIME

</td>
</tr>
<tr>
<td style="text-align: left;">

time32[s]

</td>
<td colspan="4" style="text-align: center;">

TIME

</td>
</tr>
<tr>
<td style="text-align: left;">

time64[ns]

</td>
<td colspan="4" style="text-align: center;">

TIME

</td>
</tr>
<tr>
<td style="text-align: left;">

time64[us]

</td>
<td colspan="4" style="text-align: center;">

TIME

</td>
</tr>
<tr>
<td style="text-align: left;">

timestamp[ms]

</td>
<td colspan="4" style="text-align: center;">

TIMESTAMP(3)

</td>
</tr>
<tr>
<td style="text-align: left;">

timestamp[ns]

</td>
<td colspan="4" style="text-align: center;">

TIMESTAMP(9)

</td>
</tr>
<tr>
<td style="text-align: left;">

timestamp[s]

</td>
<td colspan="4" style="text-align: center;">

TIMESTAMP(0)

</td>
</tr>
<tr>
<td style="text-align: left;">

timestamp[us]

</td>
<td colspan="4" style="text-align: center;">

TIMESTAMP(6)

</td>
</tr>
</tbody>
</table>

## Options

### Connection Options

`uri`
: **Type:** string. **Default:** not set.

  Cassandra connection string in the format described above. If it is not
  set, the driver uses the defaults of `127.0.0.1` and port `9042`.

`username` and `password`
: **Type:** string. **Default:** not set.

  Standard ADBC options for username/password authentication. The aliases
  `cassandra.auth.username` and `cassandra.auth.password` are also supported.

`cassandra.hosts`
: **Type:** string. **Default:** `127.0.0.1`.

  Comma-separated list of Cassandra contact points. All contact points use the
  port set by `cassandra.port`.

`cassandra.port`
: **Type:** integer. **Default:** `9042`.

  Native transport port used for all contact points.

`cassandra.keyspace`
: **Type:** string. **Default:** not set.

  Initial keyspace for the connection.

`cassandra.num_conns` (URI query parameter: `num_conns`)
: **Type:** integer. **Default:** `2`.

  Number of connections to create per host.

`cassandra.page_size` (URI query parameter: `page_size`)
: **Type:** integer. **Default:** `5000`.

  Maximum number of rows requested in each page of query results.

`cassandra.consistency` (URI query parameter: `consistency`)
: **Values:** `ANY`, `ONE`, `TWO`, `THREE`, `QUORUM`, `ALL`, `LOCAL_QUORUM`,
  `EACH_QUORUM`, or `LOCAL_ONE`. **Default:** `LOCAL_QUORUM`.

  Cassandra consistency level to use for queries. Values are
  case-insensitive.

`cassandra.connect_timeout` (URI query parameter: `connect_timeout`)
: **Type:** integer. **Default:** `10000`.

  Connection timeout in milliseconds.

`cassandra.timeout` (URI query parameter: `timeout`)
: **Type:** integer. **Default:** `10000`.

  Query timeout in milliseconds.

`cassandra.protocol_version` (URI query parameter: `protocol_version`)
: **Type:** integer. **Default:** `4`.

  CQL native protocol version.

### TLS Options

Boolean URI query parameters must be `true` or `false`.

`cassandra.enable_tls` (URI query parameter: `enable_tls`)
: **Type:** boolean. **Default:** `false`.

  Enable TLS for the connection.

`cassandra.tls.ca_path` (URI query parameter: `tls_ca_path`)
: **Type:** string. **Default:** not set.

  Path to a PEM-encoded CA certificate used to verify the server certificate.

`cassandra.tls.cert_path` and `cassandra.tls.key_path` (URI query parameters:
`tls_cert_path` and `tls_key_path`)
: **Type:** string. **Default:** not set.

  Paths to a PEM-encoded client certificate and private key. Set both options
  to configure mutual TLS.

`cassandra.tls.hostname_override` (URI query parameter:
`tls_hostname_override`)
: **Type:** string. **Default:** not set.

  Server name used for certificate verification.

`cassandra.tls.skip_verify` (URI query parameter: `tls_skip_verify`)
: **Type:** boolean. **Default:** `false`.

  Disable server certificate verification. This is not recommended for
  production use.

## Compatibility

This driver was tested on:

- Cassandra `5.0.9`

- DataStax Enterprise `4.0.0.6925`

[^1]: The order of entries within a map value is not deterministic: the underlying gocql driver unmarshals a CQL map into a Go map, whose iteration order is randomized. All keys and values are returned correctly, but two identical queries may return a map's entries in a different order.

[cassandra]: https://cassandra.apache.org/
