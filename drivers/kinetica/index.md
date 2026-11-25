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

# Kinetica

:::{toctree}
:maxdepth: 1
:hidden:

Changelog <changelog.md>
v7.2.1 <v7.2.1.md>
:::

[{badge-primary}`Driver Version|7.2.1`](v7.2.1.md "Permalink") {badge-secondary}`Release Date|2026-11-24` {badge-success}`Tested With|Kinetica 7.2`

This driver provides access to [Kinetica][kinetica], a GPU-accelerated
database for real-time analytics.  It is developed by Kinetica DB, Inc.; the
ADBC Driver Foundry builds and distributes it for Linux, macOS, and Windows.

Query results come back from the server as Arrow, and bulk ingest is routed to
the worker ranks that hold each row.

## Installation

The Kinetica driver can be installed with [dbc](https://docs.columnar.tech/dbc):

```bash
dbc install kinetica
```

For Python, the driver is also published as a package that bundles it:

```bash
pip install adbc-driver-kinetica
```

## Connecting

To use the driver, give the URL of a Kinetica server as the `uri` option, with
`username` and `password`.

```python
from adbc_driver_manager import dbapi

conn = dbapi.connect(
    driver="kinetica",
    db_kwargs={
        "uri": "http://localhost:9191",
        "username": "admin",
        "password": "...",
    },
)
```

Note: The example above is for Python using the
[adbc-driver-manager](https://pypi.org/project/adbc-driver-manager) package but
the process will be similar for other driver managers.

The `uri` may also be a `kinetica://` URI, by which a driver manager given
only the URI knows to load this driver:

```text
kinetica://[user[:password]@]host[:port][,host[:port]...][/path][?name=value&...]
```

It connects over HTTPS unless it says `tls=false`. Every other parameter is
an option under its own name, such as `kinetica.query.max_rows=1000`, and an
option set directly takes precedence over the URI's. Several hosts are an HA
ring, tried in the order given.

```python
conn = dbapi.connect(
    "kinetica://localhost:9191?tls=false",
    db_kwargs={"username": "admin", "password": "..."},
)
```

Kinetica's own options are named `kinetica.*`; see [Options](#options).

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
<th style="text-align: center;">Kinetica</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2">

Bind Parameters

</td>
<td colspan="1" style="text-align: center;">

✅

</td>
</tr>
<tr>
<td rowspan="8">

Bulk Ingestion

</td>
<td>

Create

</td>
<td colspan="1" style="text-align: center;">

✅

</td>
</tr>
<tr>
<td>

Append

</td>
<td colspan="1" style="text-align: center;">

✅

</td>
</tr>
<tr>
<td>

Create/Append

</td>
<td colspan="1" style="text-align: center;">

✅

</td>
</tr>
<tr>
<td>

Replace

</td>
<td colspan="1" style="text-align: center;">

✅

</td>
</tr>
<tr>
<td>

Temporary Table

</td>
<td colspan="1" style="text-align: center;">

❌

</td>
</tr>
<tr>
<td>

Target Catalog

</td>
<td colspan="1" style="text-align: center;">

❌

</td>
</tr>
<tr>
<td>

Target Schema

</td>
<td colspan="1" style="text-align: center;">

✅

</td>
</tr>
<tr>
<td>

Non-nullable fields are marked NOT NULL

</td>
<td colspan="1" style="text-align: center;">

❌

</td>
</tr>
<tr>
<td rowspan="4">

Catalog (GetObjects)

</td>
<td>

depth=catalogs

</td>
<td colspan="1" style="text-align: center;">

✅

</td>
</tr>
<tr>
<td>

depth=db_schemas

</td>
<td colspan="1" style="text-align: center;">

✅

</td>
</tr>
<tr>
<td>

depth=tables

</td>
<td colspan="1" style="text-align: center;">

✅

</td>
</tr>
<tr>
<td>

depth=columns (all)

</td>
<td colspan="1" style="text-align: center;">

✅

</td>
</tr>
<tr>
<td colspan="2">

Get Parameter Schema

</td>
<td colspan="1" style="text-align: center;">

✅

</td>
</tr>
<tr>
<td colspan="2">

Get Table Schema

</td>
<td colspan="1" style="text-align: center;">

✅

</td>
</tr>
<tr>
<td colspan="2">

Prepared Statements

</td>
<td colspan="1" style="text-align: center;">

✅

</td>
</tr>
<tr>
<td colspan="2">

Transactions

</td>
<td colspan="1" style="text-align: center;">

❌

</td>
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
<th style="text-align: center;">Kinetica</th>
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

BLOB

</td>
<td style="text-align: center;">

binary

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

date32[day] ⚠️ [^1] [^2] [^3]

</td>
</tr>
<tr>
<td style="text-align: left;">

DATETIME

</td>
<td style="text-align: center;">

timestamp[ms] [^2]

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

int32

</td>
</tr>
<tr>
<td style="text-align: left;">

NUMERIC

</td>
<td style="text-align: center;">

decimal128 ⚠️ [^3] [^4]

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

int16

</td>
</tr>
<tr>
<td style="text-align: left;">

TIME

</td>
<td style="text-align: center;">

time32[ms], time64[us] ⚠️ [^3] [^5] [^6] [^7]

</td>
</tr>
<tr>
<td style="text-align: left;">

TIMESTAMP

</td>
<td style="text-align: center;">

timestamp[ms] (with time zone), timestamp[us] ⚠️ [^2] [^3] [^7] [^8]

</td>
</tr>
<tr>
<td style="text-align: left;">

TIMESTAMP WITH TIME ZONE

</td>
<td style="text-align: center;">

❌ [^9]

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
<th colspan="2" style="text-align: center;">Kinetica Type</th>
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

VARBINARY

</td>
</tr>
<tr>
<td style="text-align: left;">

binary_view

</td>
<td colspan="2" style="text-align: center;">

VARBINARY

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
<tr class="row-with-cell-borders">
<td style="text-align: left;">

date32[day]

</td>
<td style="text-align: center;">

DATE [^2]

</td>
<td style="text-align: center;">

DATE

</td>
</tr>
<tr class="row-with-cell-borders">
<td style="text-align: left;">

decimal128

</td>
<td style="text-align: center;">

NUMERIC

</td>
<td style="text-align: center;">

NUMERIC ⚠️ [^10]

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

fixed_size_binary

</td>
<td colspan="2" style="text-align: center;">

VARBINARY

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
<tr class="row-with-cell-borders">
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
<td colspan="2" style="text-align: center;">

VARBINARY

</td>
</tr>
<tr>
<td style="text-align: left;">

large_string

</td>
<td colspan="2" style="text-align: center;">

VARCHAR

</td>
</tr>
<tr>
<td style="text-align: left;">

string

</td>
<td colspan="2" style="text-align: center;">

VARCHAR

</td>
</tr>
<tr>
<td style="text-align: left;">

string_view

</td>
<td colspan="2" style="text-align: center;">

VARCHAR

</td>
</tr>
<tr>
<td style="text-align: left;">

time32[ms]

</td>
<td colspan="2" style="text-align: center;">

TIME

</td>
</tr>
<tr>
<td style="text-align: left;">

time32[s]

</td>
<td colspan="2" style="text-align: center;">

TIME

</td>
</tr>
<tr>
<td style="text-align: left;">

time64[ns]

</td>
<td colspan="2" style="text-align: center;">

TIME ⚠️ [^6]

</td>
</tr>
<tr>
<td style="text-align: left;">

time64[us]

</td>
<td colspan="2" style="text-align: center;">

TIME ⚠️ [^6]

</td>
</tr>
<tr class="row-with-cell-borders">
<td style="text-align: left;">

timestamp[ms]

</td>
<td style="text-align: center;">

DATETIME [^2]

</td>
<td style="text-align: center;">

TIMESTAMP(3) [^2]

</td>
</tr>
<tr class="row-with-cell-borders">
<td style="text-align: left;">

timestamp[ms] (with time zone)

</td>
<td style="text-align: center;">

TIMESTAMP [^2]

</td>
<td style="text-align: center;">

TIMESTAMP(3) WITH TIME ZONE [^2]

</td>
</tr>
<tr class="row-with-cell-borders">
<td style="text-align: left;">

timestamp[ns]

</td>
<td style="text-align: center;">

DATETIME ⚠️ [^2] [^6]

</td>
<td style="text-align: center;">

TIMESTAMP(9) ⚠️ [^2] [^6]

</td>
</tr>
<tr class="row-with-cell-borders">
<td style="text-align: left;">

timestamp[ns] (with time zone)

</td>
<td style="text-align: center;">

TIMESTAMP ⚠️ [^2] [^6]

</td>
<td style="text-align: center;">

TIMESTAMP(9) WITH TIME ZONE ⚠️ [^2] [^6]

</td>
</tr>
<tr class="row-with-cell-borders">
<td style="text-align: left;">

timestamp[s]

</td>
<td style="text-align: center;">

DATETIME [^2]

</td>
<td style="text-align: center;">

TIMESTAMP(0) [^2]

</td>
</tr>
<tr class="row-with-cell-borders">
<td style="text-align: left;">

timestamp[s] (with time zone)

</td>
<td style="text-align: center;">

TIMESTAMP [^2]

</td>
<td style="text-align: center;">

TIMESTAMP(0) WITH TIME ZONE [^2]

</td>
</tr>
<tr class="row-with-cell-borders">
<td style="text-align: left;">

timestamp[us]

</td>
<td style="text-align: center;">

DATETIME ⚠️ [^2] [^6]

</td>
<td style="text-align: center;">

TIMESTAMP(6) ⚠️ [^2] [^6]

</td>
</tr>
<tr class="row-with-cell-borders">
<td style="text-align: left;">

timestamp[us] (with time zone)

</td>
<td style="text-align: center;">

TIMESTAMP ⚠️ [^2] [^6]

</td>
<td style="text-align: center;">

TIMESTAMP(6) WITH TIME ZONE ⚠️ [^2] [^6]

</td>
</tr>
</tbody>
</table>

## Options

Options are set on the database, a connection or a statement, as each says
below.  Any option set on the database can also be given as a parameter of a
`kinetica://` URI, under the same name; one set directly takes precedence.  A
boolean takes `true` or `false`.

### Connection Options

`kinetica.session_id`
: **Type:** string. **Default:** (empty)

  The server session whose SQL `#name` temp tables a connection uses.  Connections given the same session share its temp tables, and the caller drops it when done, with Kinetica's `/drop/session`.  Empty gives each connection a session of its own, dropped when the connection closes.

  Set on the database.

`kinetica.impersonate_user`
: **Type:** string. **Default:** (empty)

  The user each connection acts as from the start, which the server reads as impersonation.  `SET USER` and `EXECUTE AS USER` step into another user from there, and `REVERT` comes back to this one.

  Set on the database.

`kinetica.fake_transactions`
: **Type:** boolean. **Default:** `false`

  Accept the transaction calls, such as turning autocommit off, and do nothing, rather than refuse them.  Kinetica has no transactions, so a rollback undoes nothing either way; this decides whether a caller is told.

  Set on the database or a connection.

`kinetica.replication`
: **Values:** `sync`, `sync_parallel`, `async`, `async_parallel`, `none`. **Default:** (the server's)

  How far a write must have replicated across an HA ring before the server answers.  The server's own spellings, such as `REPL_SYNC`, are accepted too.

  Set on the database.

`kinetica.no_sync`
: **Type:** boolean. **Default:** `false`

  Shorthand for a `kinetica.replication` of `none`.  `kinetica.replication` wins where both are given.

  Set on the database.

`kinetica.primary_url`
: **Type:** string. **Default:** the first address of the URI

  The cluster that failover returns to once it is reachable again.

  Set on the database.

`kinetica.failover`
: **Type:** boolean. **Default:** `true`

  Fail over to another cluster of the HA ring when one fails.

  Set on the database.

`kinetica.failover_order`
: **Values:** `sequential`, `random`. **Default:** `sequential`

  The order the clusters of the ring are tried in when one fails.

  Set on the database.

`kinetica.auto_discovery`
: **Type:** boolean. **Default:** `true`

  Discover the rest of the HA ring from the cluster first reached.  Off, only the addresses the URI gives are used.

  Set on the database.

`kinetica.failback_poll_interval`
: **Type:** integer. **Default:** `5`

  Seconds between polls of the primary cluster, which is how a connection that failed away from it comes back.

  Set on the database.

`kinetica.hostname_regex`
: **Type:** string. **Default:** (empty)

  A regular expression choosing which of a worker's addresses to use where it publishes more than one.  Bulk ingest goes to the addresses it keeps.

  Set on the database.

`kinetica.request_timeout`
: **Type:** integer. **Default:** `0`

  Seconds a request may take before it is abandoned; `0` for no limit.

  Set on the database.

`kinetica.connect_timeout`
: **Type:** integer. **Default:** `5`

  Seconds to wait for the server to answer.

  Set on the database.

`kinetica.initial_connect_timeout`
: **Type:** integer. **Default:** `0`

  Seconds to spend reaching a cluster for the first time before trying the next.

  Set on the database.

`kinetica.max_retries`
: **Type:** integer. **Default:** `5`

  How many times a request is sent again: one that failed on the wire, or one a cluster that is just back online refused while it was still starting.

  Set on the database.

`kinetica.snappy`
: **Type:** boolean. **Default:** `true`

  Compress bulk record requests with Snappy.

  Set on the database.

`kinetica.trust_store_path`
: **Type:** string. **Default:** (empty)

  The trust store holding the certificate authority that signed the server's certificate, for an `https` connection.

  Set on the database.

`kinetica.trust_store_password`
: **Type:** string. **Default:** (empty)

  The trust store's password.  It can be set but not read back.

  Set on the database.

`kinetica.bypass_ssl_cert_check`
: **Type:** boolean. **Default:** `false`

  Accept the server's certificate without checking it.  Prefer a trust store wherever the certificate can be trusted.

  Set on the database.

`kinetica.log_level`
: **Values:** `off`, `error`, `warn`, `info`, `debug`, `trace`. **Default:** `off`

  How much the driver logs.  A host program that has installed a logger of its own keeps it.

  Set on the database.

`kinetica.log_path`
: **Type:** string. **Default:** (empty)

  The file the log is appended to.  Empty writes to standard error.

  Set on the database.

### Authentication Options

`kinetica.auth_method`
: **Values:** `password`, `oauth`. **Default:** `password`

  How the connection signs in: with `username` and `password`, or with an OAuth bearer token.

  Set on the database.

`kinetica.oauth_token`
: **Type:** string. **Default:** (empty)

  A bearer token the caller already holds, presented as it is.  The driver does not acquire one.

  Set on the database.

`kinetica.oauth_grant`
: **Values:** `client_credentials`, `authorization_code`, `device_code`, `refresh_token`, `token-exchange`, `jwt-bearer`. **Default:** (none)

  How the driver acquires a bearer token, when the caller does not hold one.  Each grant's URN, as its RFC names it, is accepted too.

  Set on the database.

`kinetica.auth_provider`
: **Values:** `entra`, `okta`, `command`. **Default:** (none)

  An identity provider whose own parameters the driver turns into the generic ones (`entra`, `okta`), or `command`, which runs `kinetica.oauth.command` and takes what it prints as the token.  The command runs under `sh -c`, or `cmd.exe /c` on Windows, with the privileges of the process holding the connection, so it must never come from untrusted input.

  `entra` and `okta` are each implied by a parameter only they read (`kinetica.oauth.tenant_id`, `kinetica.oauth.application_id_uri`, `kinetica.oauth.okta_domain`), so naming one is an override rather than a requirement.

  Set on the database.

`kinetica.token_name_claim`
: **Type:** string. **Default:** `sub` (`preferred_username` under `entra`)

  The claim of a bearer token the user name is read from.  The name a token gives takes precedence over `username`.

  Set on the database.

`kinetica.oauth_token_cache`
: **Values:** `memory`, `none`. **Default:** `memory`

  `memory` shares one token between every connection of the process that would ask for the same one; `none` signs in for each connection.

  Set on the database.

`kinetica.oauth.<name>`
: **Type:** string.

  What an OAuth flow needs: `issuer`, `token_url`, `authorize_url`, `device_url`, `client_id`, `client_secret`, `scope`, `audience`, `subject`, `refresh_token`, `subject_token`, `subject_token_type`, `private_key`, `private_key_file`, `key_id` and `algorithm`.  Given an issuer and nothing else, the endpoints are read from its OpenID Connect discovery document.

  A provider's own parameters are named the same way: `command` and `command_timeout_seconds` (default `60`) for `command`; `tenant_id`, `application_id_uri` (or `resource`) and `authority_host` for `entra`; `okta_domain` and `auth_server_id` for `okta`.

  Set on the database.

### Query Options

`kinetica.query.batch_size`
: **Type:** integer. **Default:** `20000`

  Rows requested from the server per page of a result, capped at the server's own limit.

  Set on a statement.

`kinetica.query.max_rows`
: **Type:** integer. **Default:** (none)

  The most rows a read hands back, however many the result holds.  Unset or negative hands back all of them.

  Set on the database, a connection or a statement; the statement's own wins.

`kinetica.query.use_key_lookup`
: **Type:** boolean. **Default:** `false`

  Send a read that pins every key column of a table to the rank holding its row, rather than to the SQL engine.  The rows are the same either way; `kinetica.key_lookup` says which way the last read went.

  Set on the database, a connection or a statement; the statement's own wins.

These are sent with every statement, but only when set, so an unset one
leaves the server's own default in place.

`kinetica.query.cost_based_optimization`
: **Type:** boolean. **Default:** (the server's)

  Whether the planner costs its alternatives.

  Set on the database or a connection.

`kinetica.query.rule_based_optimization`
: **Type:** boolean. **Default:** (the server's)

  Whether the rule-based rewrites run.

  Set on the database or a connection.

`kinetica.query.ssq_optimization`
: **Type:** boolean. **Default:** (the server's)

  Whether scalar subqueries are optimized.

  Set on the database or a connection.

`kinetica.query.distributed_operations`
: **Type:** boolean. **Default:** (the server's)

  Whether data may be resharded or replicated among the ranks, so that a join, a set operation or an intermediate result over data not already distributed compatibly can run.  Off, such a query fails.

  Set on the database or a connection.

`kinetica.query.parallel_execution`
: **Type:** boolean. **Default:** (the server's)

  Whether the steps of a plan may run at once.

  Set on the database or a connection.

`kinetica.query.plan_cache`
: **Type:** boolean. **Default:** (the server's)

  Whether a plan already worked out may be reused.

  Set on the database or a connection.

`kinetica.query.results_caching`
: **Type:** boolean. **Default:** (the server's)

  Whether a result already worked out may be reused.

  Set on the database or a connection.

`kinetica.query.ignore_existing_pk`
: **Type:** boolean. **Default:** (the server's)

  Whether a row whose primary key is already in the table is passed over rather than refused.

  Set on the database or a connection.

`kinetica.query.update_on_existing_pk`
: **Type:** boolean. **Default:** (the server's)

  Whether such a row replaces the one already in the table.

  Set on the database or a connection.

`kinetica.query.validate_change_column`
: **Type:** boolean. **Default:** (the server's)

  Whether a column being changed is checked first.

  Set on the database or a connection.

`kinetica.query.use_approx_count_distinct`
: **Type:** boolean. **Default:** (the server's)

  Whether distinct values may be counted approximately.

  Set on the database or a connection.

`kinetica.query.ttl`
: **Type:** integer. **Default:** (the server's)

  Minutes to keep what a statement makes.

  Set on the database or a connection.

`kinetica.query.paging_table_ttl`
: **Type:** integer. **Default:** `20`

  Minutes the server keeps the result a paged read works through.  The driver clears it as soon as the read is done, so this only matters for a read left unfinished.

  Set on the database or a connection.

### Ingest Options

`kinetica.ingest.error_mode`
: **Values:** `abort`, `skip`, `permissive`. **Default:** `abort`

  What to do about a row the workers cannot take: `abort` fails the batch it is in; `skip` takes the rest of the batch without it; `permissive` takes the rest and asks the server to say what was wrong with each row it refused.

  Set on the database or a connection.

`kinetica.ingest.truncate_strings`
: **Type:** boolean. **Default:** `false`

  Cut a string too long for its column to fit, rather than refusing it.

  Set on the database or a connection.

`kinetica.ingest.rows_per_insertion`
: **Type:** integer. **Default:** `50000`

  Rows sent to a worker at a time.

  Set on the database or a connection.

`kinetica.ingest.multihead_insert`
: **Type:** boolean. **Default:** `true`

  Send rows straight to the worker ranks that hold them.  Off, they go through the head rank.

  Set on the database or a connection.

The options below read a local file loaded by
`INSERT INTO t SELECT * FROM FILE."data.csv"`.  A statement can also give each
in its own `WITH OPTIONS (...)`, as `file read` and the option's last part
(`file read limit = 100`), which beats the connection's.

`kinetica.ingest.file.delimiter`
: **Type:** string. **Default:** (from the file's extension)

  The field separator.  Unset, it is `|` for `.psv`, a tab for `.tsv`, and otherwise a comma.  A tab may be written `\t`.

  Set on the database or a connection.

`kinetica.ingest.file.quote_char`
: **Type:** string. **Default:** `"`

  The quote character.

  Set on the database or a connection.

`kinetica.ingest.file.escape_char`
: **Type:** string. **Default:** (none)

  The escape character.  Unset, a quote is escaped by doubling it.

  Set on the database or a connection.

`kinetica.ingest.file.comment_char`
: **Type:** string. **Default:** (none)

  A line starting with this is skipped.

  Set on the database or a connection.

`kinetica.ingest.file.has_header`
: **Type:** boolean. **Default:** `true`

  Whether the first line names the columns.

  Set on the database or a connection.

`kinetica.ingest.file.null_string`
: **Type:** string. **Default:** (none)

  The text that stands for a null.  Unset, an empty field is null.

  Set on the database or a connection.

`kinetica.ingest.file.skip`
: **Type:** integer. **Default:** `0`

  Rows to pass over at the start of each file, after its header.

  Set on the database or a connection.

`kinetica.ingest.file.limit`
: **Type:** integer. **Default:** (none)

  The most rows to read across every file matched.

  Set on the database or a connection.

`kinetica.ingest.file.initial_clear`
: **Type:** boolean. **Default:** `false`

  Empty the table before loading the file into it.

  Set on the database or a connection.

### Statement Results

These are read from a statement with `get_option_int` after it runs, since the
ADBC C API has no room for them on a call that also returns a reader.

`kinetica.count_affected`
: **Type:** integer.

  Rows the last statement changed, or `-1` if it was a query.

`kinetica.total_number_of_records`
: **Type:** integer.

  Rows the last statement's whole result holds, however many have been read so far, or `-1` if it produced no result.  A query bound to several rows of parameters runs once for each, and this adds up the runs made so far.  Also read as the standard max-progress option.

`kinetica.key_lookup`
: **Type:** integer.

  `1` if the last read was answered by the rank holding its row, `0` if it went through the SQL engine.

## Compatibility

The driver needs Kinetica 7.2.3.24 or later, the first version to return query
results as Arrow.  A connection to an older server is refused when it opens,
naming both versions.

This driver was tested on:

- Kinetica `7.2.3.24.20261101191740`

[^1]: Kinetica returns a DATE computed from constants as a string
[^2]: Kinetica's dates run from 1000-01-01 to 2900-12-31
[^3]: literal is not supported
[^4]: Kinetica returns a NUMERIC computed from constants as a string
[^5]: Kinetica returns a TIME computed from constants as a string
[^6]: Kinetica stores times and timestamps to the millisecond; finer digits are dropped
[^7]: Return type is inconsistent depending on how the query was written
[^8]: Kinetica returns a TIMESTAMP computed from constants as a string
[^9]: Kinetica's SQL engine refuses a TIMESTAMP WITH TIME ZONE literal
[^10]: Kinetica's DECIMAL has no negative scale

[kinetica]: https://www.kinetica.com/
