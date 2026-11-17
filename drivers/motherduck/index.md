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

# MotherDuck

:::{toctree}
:maxdepth: 1
:hidden:

Changelog <changelog.md>
v0.1.0-alpha.1 <v0.1.0-alpha.1.md>
:::

{badge-primary}`Driver Version|v0.1.0-alpha.1` {badge-secondary}`Release Date|2026-11-16` {badge-success}`Tested With|MotherDuck latest`

:::{warning}
This is documentation for a prerelease version.
:::

This driver provides access to [MotherDuck](https://motherduck.com/), a
serverless cloud data warehouse built on DuckDB.

## Installation & Quickstart

The driver can be installed with [dbc](https://docs.columnar.tech/dbc):

```bash
dbc install --pre motherduck
```

## Connecting

The driver connects to MotherDuck's PostgreSQL protocol endpoint and uses your
MotherDuck token as the password. Set the token in the `MOTHERDUCK_TOKEN`
environment variable, which keeps it out of connection strings and logs, and
give the database to connect to and your account's region. Find your region
with `md_user_info()`.

```python
from adbc_driver_manager import dbapi

with dbapi.connect(
    driver="motherduck",
    db_kwargs={
        "uri": "motherduck:///my_db",
        "motherduck.region": "us-east-1",
    },
) as conn:
    with conn.cursor() as cursor:
        cursor.execute("SELECT 42")
        print(cursor.fetch_arrow_table())
```

The region sets the host, so the URI can leave it out. `us-east-1` connects to
`pg.us-east-1-aws.motherduck.com`. Without the option, put the host in the URI
instead: `motherduck://pg.us-east-1-aws.motherduck.com/my_db`.

The URI's scheme names the driver, so an ADBC driver manager can pick this
driver from a `motherduck://` URI alone. Pass the URI in place of the driver
name:

```python
from adbc_driver_manager import dbapi

with dbapi.connect(
    "motherduck:///my_db",
    db_kwargs={"motherduck.region": "us-east-1"},
) as conn:
    ...
```

A driver manager matches the scheme against the driver's name, so it doesn't
find the driver from an `md://` or `md:` URI. When you use those, name the
driver as well, with `driver="motherduck"`.

By default the driver connects in `single` attach mode, which attaches only the
database named in the connection. To work across every database in the account,
connect to `md:` and set `motherduck.attach_mode` to `workspace`.

### Connection String Format

The URI is a `motherduck://` URI:

```text
motherduck://[USER[:TOKEN]@][HOST[:PORT]]/DATABASE[?PARAMETER=VALUE&...]
```

Two short forms are accepted: `md://`, with the same syntax, and DuckDB's
`md:[DATABASE][?PARAMETER=VALUE&...]`, which has no host, so set
`motherduck.region` too. `md:` alone is the workspace, the same as
`md%3A` as the database. The driver accepts no other scheme, and the scheme is
lowercase.

Components:

- `DATABASE`: the MotherDuck database to connect to, or `md:` (written `md%3A`
  in a URI) in `workspace` attach mode.
- `HOST` and `PORT`: the endpoint, such as `pg.us-east-1-aws.motherduck.com`.
  Optional when `motherduck.region` is set; the port is then 5432 unless
  the URI sets one.
- `USER`: optional. The default is `postgres`, which MotherDuck expects.
- `TOKEN`: the MotherDuck token. Prefer `MOTHERDUCK_TOKEN` or a database option
  to putting it in the URI.

The query takes the [driver options](#driver-options) by name, such as
`motherduck:///my_db?motherduck.region=us-east-1&motherduck.connect_timeout=10`.
Percent-encode values; an empty value is unset. Every option except
`motherduck.token` can be set this way (a token doesn't belong in a query, which
is more likely to be logged than the URI's password), and an option set on the
database takes precedence over the URI's. Any other query parameter, including
the PostgreSQL settings below, is rejected with `INVALID_ARGUMENT`.

### Authentication

The driver takes the token from the first of these that is set:

1. The `password` database option, or its alias `motherduck.token`.
2. The password in the URI.
3. The `MOTHERDUCK_TOKEN` environment variable.

Without a token, connecting fails with `UNAUTHENTICATED`.

### Driver Options

| Option | Level | Description |
| --- | --- | --- |
| `motherduck.attach_mode` | Database | `single` (default) attaches only the named database; `workspace` attaches every database in the account. |
| `motherduck.region` | Database | The MotherDuck region, such as `us-east-1` or `eastus2`, which sets the host. |
| `motherduck.session_name` | Database | MotherDuck's [session name](https://motherduck.com/docs/sql-reference/connection-string-parameters/#session_name), which routes connections with the same name to the same replica under read scaling. |
| `motherduck.application_name` | Database | Your application's name. The driver adds `adbc_driver_motherduck/<version>` after it, so it appears in MotherDuck's query history. A name too long to fit in PostgreSQL's 63 bytes is shortened. |
| `motherduck.connect_timeout` | Database | The longest time to wait while connecting, in whole seconds, as a string or an integer. Unset by default, which sets no timeout of its own. `0` waits indefinitely; the shortest timeout is 2 seconds, so `1` acts as `2`. |
| `motherduck.db_schema` | Database | The schema every new connection starts in. Connecting fails if it doesn't exist. |
| `adbc.connection.db_schema` | Connection | Changes a single connection's schema, in its current database. |
| `motherduck.token` | Database | Alias for the standard `password` option. Not accepted in the URI's query. |
| `motherduck.tls_root_cert_path` | Database | Optional; unset by default, which uses the OS's trusted CA certificates. A PEM file of root certificates to verify the server with instead, such as a corporate CA bundle. Uses `sslmode=verify-full`; connecting fails if the file can't be read. |
| `motherduck.tls_verify` | Database | Optional. `true` (default) verifies the server's certificate; `false` encrypts without verifying (`sslmode=require`). |

## Differences from the PostgreSQL Driver

Applications may have used the ADBC PostgreSQL driver
(`adbc_driver_postgresql`) to connect to MotherDuck's PostgreSQL protocol
endpoint. This driver builds on that implementation with connection handling
and metadata support adapted for MotherDuck. If you are migrating an existing
application from the PostgreSQL driver, review the differences below:

- **A separate driver.** Load `motherduck`, not `postgresql`.
- **MotherDuck only.** The driver connects only to MotherDuck's PostgreSQL
  endpoint. Plain PostgreSQL servers aren't supported, because every connection
  sets `attach_mode`.
- **Connection URI.** The URI must use the `motherduck://` scheme (or `md://`, or `md:`),
  not `postgresql://`.
- **Connection settings.** The MotherDuck token is the password, and the user
  defaults to `postgres`. `PGUSER`, `PGPASSWORD`, `PGAPPNAME`, and password
  files are never used, and `sslmode` defaults to
  `verify-full`. The `motherduck.*` options have no PostgreSQL equivalent.
- **Options that differ.** `adbc.postgresql.use_copy` defaults to `false`, and
  setting it to `true` fails. `adbc.postgresql.type_resolver_mode` is accepted
  and ignored. `adbc.connection.db_schema` names a schema, not an arbitrary
  `search_path`; use `USE <database>` to change databases.
- **Results and errors.** DML and DDL return an empty stream, and `rows_affected`
  for `UPDATE` and `DELETE` is the number of rows changed. Data conversion
  errors map to `INTERNAL` instead of `INVALID_DATA`.
- **Missing features.** Bulk ingest, COPY result reads, statistics, and others
  don't work; the feature table below shows what is supported.

### PostgreSQL settings are not supported

The PostgreSQL client library has additional settings that are not part of this
driver's supported interface. They may change or stop working in a future
version, including a version that no longer uses that library:

- URI query parameters, such as `sslmode`, `sslrootcert`, `options` and
  `service`. These are rejected: the URI's query takes only the `motherduck.*`
  options.
- PostgreSQL environment variables, such as `PGHOST`, `PGPORT`, `PGSSLMODE`,
  `PGSSLROOTCERT` and `PGOPTIONS`, and files such as `~/.pg_service.conf`.
  Some are read today and some are ignored.

Use the `motherduck.*` options and the standard ADBC options instead,
such as `motherduck.tls_root_cert_path` and `motherduck.tls_verify`
for certificate verification. By default the driver verifies the server's
certificate with the OS's trusted CA certificates (or `SSL_CERT_FILE`), so most
connections need no TLS settings. If the driver finds no CA certificates,
connecting fails; install the OS's CA certificates (such as the
`ca-certificates` package) or use one of those options.

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
      <th style="text-align: center;">MotherDuck</th>
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
      <td colspan="1" style="text-align: center;">✅</td>
    </tr>
    <tr>
      <td>depth=db_schemas</td>
      <td colspan="1" style="text-align: center;">✅</td>
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
<colgroup>
<col span="1" style="width: 50.0%;">
<col span="1" style="width: 50.0%;">
</colgroup>
<thead>
<tr>
<th style="text-align: left; vertical-align: middle;">Database Type</th>
<th style="text-align: center;">MotherDuck</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">

TIMESTAMP(0)

</td>
<td style="text-align: center;">

timestamp[us]

</td>
</tr>
<tr>
<td style="text-align: left;">

TIMESTAMP(p) (1 &lt;= p &lt;= 3)

</td>
<td style="text-align: center;">

timestamp[us]

</td>
</tr>
<tr>
<td style="text-align: left;">

TIMESTAMP(p) (4 &lt;= p &lt;= 6)

</td>
<td style="text-align: center;">

timestamp[us]

</td>
</tr>
<tr>
<td style="text-align: left;">

bigint

</td>
<td style="text-align: center;">

int64

</td>
</tr>
<tr>
<td style="text-align: left;">

bool

</td>
<td style="text-align: center;">

bool

</td>
</tr>
<tr>
<td style="text-align: left;">

bytea

</td>
<td style="text-align: center;">

binary

</td>
</tr>
<tr>
<td style="text-align: left;">

date

</td>
<td style="text-align: center;">

date32[day]

</td>
</tr>
<tr>
<td style="text-align: left;">

double precision

</td>
<td style="text-align: center;">

double

</td>
</tr>
<tr>
<td style="text-align: left;">

integer

</td>
<td style="text-align: center;">

int32

</td>
</tr>
<tr>
<td style="text-align: left;">

json

</td>
<td style="text-align: center;">

extension&lt;arrow.json&gt;

</td>
</tr>
<tr>
<td style="text-align: left;">

numeric

</td>
<td style="text-align: center;">

extension&lt;arrow.opaque[storage_type=string, type_name=numeric, vendor_name=PostgreSQL]&gt;

</td>
</tr>
<tr>
<td style="text-align: left;">

real

</td>
<td style="text-align: center;">

float

</td>
</tr>
<tr>
<td style="text-align: left;">

smallint

</td>
<td style="text-align: center;">

int16

</td>
</tr>
<tr>
<td style="text-align: left;">

text

</td>
<td style="text-align: center;">

string

</td>
</tr>
<tr>
<td style="text-align: left;">

time

</td>
<td style="text-align: center;">

time64[us]

</td>
</tr>
<tr>
<td style="text-align: left;">

timestamp

</td>
<td style="text-align: center;">

timestamp[us]

</td>
</tr>
<tr>
<td style="text-align: left;">

timestamptz

</td>
<td style="text-align: center;">

timestamp[us] (with time zone)

</td>
</tr>
<tr>
<td style="text-align: left;">

uuid

</td>
<td style="text-align: center;">

extension&lt;arrow.uuid&gt;

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
<th colspan="2" style="text-align: center;">MotherDuck Type</th>
</tr>
<tr>
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

bytea

</td>
<td style="text-align: center;">

❌

</td>
</tr>
<tr class="row-with-cell-borders">
<td style="text-align: left;">

binary_view

</td>
<td style="text-align: center;">

bytea

</td>
<td style="text-align: center;">

❌

</td>
</tr>
<tr class="row-with-cell-borders">
<td style="text-align: left;">

bool

</td>
<td style="text-align: center;">

bool

</td>
<td style="text-align: center;">

❌

</td>
</tr>
<tr class="row-with-cell-borders">
<td style="text-align: left;">

date32[day]

</td>
<td style="text-align: center;">

date

</td>
<td style="text-align: center;">

❌

</td>
</tr>
<tr class="row-with-cell-borders">
<td style="text-align: left;">

decimal128

</td>
<td style="text-align: center;">

numeric

</td>
<td style="text-align: center;">

❌

</td>
</tr>
<tr class="row-with-cell-borders">
<td style="text-align: left;">

double

</td>
<td style="text-align: center;">

double precision

</td>
<td style="text-align: center;">

❌

</td>
</tr>
<tr class="row-with-cell-borders">
<td style="text-align: left;">

extension&lt;arrow.uuid&gt;

</td>
<td style="text-align: center;">

uuid

</td>
<td style="text-align: center;">

❌

</td>
</tr>
<tr class="row-with-cell-borders">
<td style="text-align: left;">

fixed_size_binary

</td>
<td style="text-align: center;">

bytea

</td>
<td style="text-align: center;">

❌

</td>
</tr>
<tr class="row-with-cell-borders">
<td style="text-align: left;">

float

</td>
<td style="text-align: center;">

real

</td>
<td style="text-align: center;">

❌

</td>
</tr>
<tr class="row-with-cell-borders">
<td style="text-align: left;">

halffloat

</td>
<td style="text-align: center;">

real

</td>
<td style="text-align: center;">

(NA/not tested)

</td>
</tr>
<tr class="row-with-cell-borders">
<td style="text-align: left;">

int16

</td>
<td style="text-align: center;">

smallint

</td>
<td style="text-align: center;">

❌

</td>
</tr>
<tr class="row-with-cell-borders">
<td style="text-align: left;">

int32

</td>
<td style="text-align: center;">

integer

</td>
<td style="text-align: center;">

❌

</td>
</tr>
<tr class="row-with-cell-borders">
<td style="text-align: left;">

int64

</td>
<td style="text-align: center;">

bigint

</td>
<td style="text-align: center;">

❌

</td>
</tr>
<tr class="row-with-cell-borders">
<td style="text-align: left;">

large_binary

</td>
<td style="text-align: center;">

bytea

</td>
<td style="text-align: center;">

❌

</td>
</tr>
<tr class="row-with-cell-borders">
<td style="text-align: left;">

large_string

</td>
<td style="text-align: center;">

text

</td>
<td style="text-align: center;">

❌

</td>
</tr>
<tr class="row-with-cell-borders">
<td style="text-align: left;">

list

</td>
<td style="text-align: center;">

(NA/not tested)

</td>
<td style="text-align: center;">

❌

</td>
</tr>
<tr class="row-with-cell-borders">
<td style="text-align: left;">

string

</td>
<td style="text-align: center;">

text

</td>
<td style="text-align: center;">

❌

</td>
</tr>
<tr class="row-with-cell-borders">
<td style="text-align: left;">

string_view

</td>
<td style="text-align: center;">

text

</td>
<td style="text-align: center;">

❌

</td>
</tr>
<tr class="row-with-cell-borders">
<td style="text-align: left;">

time32[ms]

</td>
<td style="text-align: center;">

time

</td>
<td style="text-align: center;">

❌

</td>
</tr>
<tr class="row-with-cell-borders">
<td style="text-align: left;">

time32[s]

</td>
<td style="text-align: center;">

time

</td>
<td style="text-align: center;">

❌

</td>
</tr>
<tr class="row-with-cell-borders">
<td style="text-align: left;">

time64[ns]

</td>
<td style="text-align: center;">

time

</td>
<td style="text-align: center;">

❌

</td>
</tr>
<tr class="row-with-cell-borders">
<td style="text-align: left;">

time64[us]

</td>
<td style="text-align: center;">

time

</td>
<td style="text-align: center;">

❌

</td>
</tr>
<tr class="row-with-cell-borders">
<td style="text-align: left;">

timestamp[ms]

</td>
<td style="text-align: center;">

timestamp

</td>
<td style="text-align: center;">

❌

</td>
</tr>
<tr class="row-with-cell-borders">
<td style="text-align: left;">

timestamp[ms] (with time zone)

</td>
<td style="text-align: center;">

timestamptz

</td>
<td style="text-align: center;">

❌

</td>
</tr>
<tr class="row-with-cell-borders">
<td style="text-align: left;">

timestamp[ns]

</td>
<td style="text-align: center;">

duckdb_timestamp_ns

</td>
<td style="text-align: center;">

❌

</td>
</tr>
<tr class="row-with-cell-borders">
<td style="text-align: left;">

timestamp[ns] (with time zone)

</td>
<td style="text-align: center;">

timestamptz

</td>
<td style="text-align: center;">

❌

</td>
</tr>
<tr class="row-with-cell-borders">
<td style="text-align: left;">

timestamp[s]

</td>
<td style="text-align: center;">

timestamp

</td>
<td style="text-align: center;">

❌

</td>
</tr>
<tr class="row-with-cell-borders">
<td style="text-align: left;">

timestamp[s] (with time zone)

</td>
<td style="text-align: center;">

timestamptz

</td>
<td style="text-align: center;">

❌

</td>
</tr>
<tr class="row-with-cell-borders">
<td style="text-align: left;">

timestamp[us]

</td>
<td style="text-align: center;">

timestamp

</td>
<td style="text-align: center;">

❌

</td>
</tr>
<tr class="row-with-cell-borders">
<td style="text-align: left;">

timestamp[us] (with time zone)

</td>
<td style="text-align: center;">

timestamptz

</td>
<td style="text-align: center;">

❌

</td>
</tr>
</tbody>
</table>



## Compatibility

This driver was tested against the MotherDuck cloud service. The driver does
not report a server version.
