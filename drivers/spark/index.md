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

# Apache Spark

:::{toctree}
:maxdepth: 1
:hidden:

Changelog <changelog.md>
v0.1.0 <v0.1.0.md>
v0.1.0-alpha.3 <v0.1.0-alpha.3.md>
v0.1.0-alpha.2 <v0.1.0-alpha.2.md>
:::

[{badge-primary}`Driver Version|v0.1.0`](#driver-spark-v0.1.0 "Permalink") {badge-secondary}`Release Date|2026-07-20` {badge-success}`Tested With|Spark 3.x (Hive metastore) 3.5-livy` {badge-success}`Tested With|Spark 3.x (Hive metastore) 3.5-thrift` {badge-success}`Tested With|Spark 4.x (Hive metastore) 4.0-connect` {badge-success}`Tested With|Spark 4.x (Hive metastore) 4.0-thrift` {badge-success}`Tested With|Spark 4.x (Hive metastore) 4.0-thrifthttp` {badge-success}`Tested With|Spark 4.x (Hive metastore) 4.1-connect` {badge-success}`Tested With|Spark 4.x (Hive metastore) emr-8.0-connect` {badge-success}`Tested With|Spark 4.x (Iceberg metastore) 4.1-connect`

This driver provides access to [Apache Spark][spark] (commonly referred to
as just "Spark").

:::{note}
This project is not affiliated with the Apache Software Foundation.
:::

## Installation & Quickstart

The driver can be installed with [dbc](https://docs.columnar.tech/dbc):

```bash
dbc install spark
```

## Connecting

To use the driver, provide a connection string as the `uri` option.

```python
from adbc_driver_manager import dbapi

dbapi.connect(
  driver="spark",
  db_kwargs={
      "uri": "spark://localhost:10000?auth_type=plain&api=thrift%2Bbinary"
  }
)
```

Note: The example above is for Python using the [adbc-driver-manager](https://pypi.org/project/adbc-driver-manager) package but the process will be similar for other driver managers.  See [adbc-quickstarts](https://github.com/columnar-tech/adbc-quickstarts).

### Connection String Format

- The URI scheme is "spark://".
- The host and port should be provided.
- If not specified, the `api` defaults to `thrift+binary` (URI-encoded: `thrift%2Bbinary`).
- Options can be specified as query parameters or as driver options.

:::{note}
Reserved characters in URI elements must be URI-encoded. For example, `@` becomes `%40` and `+` becomes `%2B`.
:::

### Connection Options

These parameters can be specified in the URI as query parameters, or as connection parameters:

`spark.api` (query parameter: `api`)
: **Values**: `connect`, `livy`, `thrift+binary`, or `thrift+http`.

  The protocol used to connect to Spark.

  | Value           | Backend                        |
  |-----------------|--------------------------------|
  | `connect`       | Spark Connect                  |
  | `livy`          | Apache Livy                    |
  | `thrift+binary` | HiveServer2 Thrift (over TCP)  |
  | `thrift+http`   | HiveServer2 Thrift (over HTTP) |

`spark.auth_type` (query parameter: `auth_type`)
: **Values**: `sql`, `spark`, or `pyspark`.

  How to authenticate to Spark.

  | Auth Type   | Applicable Backends            | Description               |
  |-------------|--------------------------------|---------------------------|
  | `aws_sigv4` | `livy`                         | Use AWS SDK               |
  | `basic`     | `livy`                         | Username/password         |
  | `ldap`      | `thrift+binary`, `thrift+http` | Not yet implemented       |
  | `kerberos`  | `thrift+binary`, `thrift+http` | Not yet implemented       |
  | `none`      | `connect`, `livy`              | No authentication         |
  | `nosasl`    | `thrift+binary`, `thrift+http` | No authentication         |
  | `plain`     | `thrift+binary`, `thrift+http` | Username/password         |
  | `token`     | `connect`                      | Username/password (token) |

`spark.livy.session_kind` (query parameter: `livy.session_kind`)
: **Values**: `sql`, `spark`, or `pyspark`.

  For the Livy backend, what kind of session to create.

  :::{warning}
  Currently only `sql` is tested/supported.
  :::

`spark.connect.session_id` (query parameter: `connect.session_id`)
: **Type**: string.

  For the Spark Connect backend, reuse this client session.

`spark.connect.release_session` (query parameter: `connect.release_session`)
: **Type**: boolean. **Default**: true.

  For the Spark Connect backend, whether to call `ReleaseSession` when the connection is closed. Set to `false` to keep a session available after closing the connection.

`spark.livy.session_id` (query parameter: `livy.session_id`)
: **Type**: string.

  For the Livy backend, reuse this client session.

`spark.livy.release_session` (query parameter: `livy.release_session`)
: **Type**: boolean. **Default**: true.

  For the Livy backend, whether to delete the session when the connection is closed. Set to `false` to keep a session available after closing the connection.

`spark.tls` (query parameter: `tls`)
: **Type** boolean. **Default**: false.

  Whether to use TLS for connecting. Only applies to `connect`, `livy`, and `thrift+http`.

`spark.validate_server_certificate` (query parameter: `validateservercertificate`)
: **Type** boolean. **Default**: true.

  Whether to validate the server's TLS certificate. Should only be disabled for development/testing.

`adbc.connection.catalog` (query parameter: `catalog`)
: **Type**: string.

  This is a standard ADBC option; it can additionally be specified during connection to select which catalog to use instead of the server default.

## Limitations

Different backends and cluster configurations have limitations; some limitations related to data type support are also noted further below.

### HiveServer2/Thrift Protocol

- In Spark 3.x, binary data that does not happen to be valid UTF-8 will be corrupted.
- The client cannot tell whether a timestamp carries a time zone or not; all timestamps are assumed to be in UTC as a result.

### Apache Livy

- Only the first 1000 rows of a result set can be fetched. This can be tuned by configuring Spark with `spark.sql.repl.eagerEval.maxNumRows`.
- In general, we have found that performance is worse than with Spark Connect or HiveServer2.
- Connecting to an Amazon EMR (Serverless) cluster via Livy requires setting the `emr-serverless.session.executionRoleArn` session config option to an appropriate role ARN. This can be set via the ADBC option `spark.opt.emr-serverless.session.executionRoleArn`.
- By default, the driver will attempt to start a new Livy session, which tends to take some time (~a few minutes), especially when using Amazon EMR. To amortize this time across multiple connections, the option `spark.livy.session_id` can be used to fetch the session ID, and to provide it upon connection, bypassing creating a new session.
- By default, the driver will close the session when the connection is closed. Setting `spark.livy.release_session` to `false` on connection will avoid this, making it easier to reuse the session.

### Spark Connect

- To connect to Amazon EMR, the connection URI should look like this:

  ```
  spark://:<AUTH TOKEN>@<SESSION ID>.s.emr-serverless-services.<REGION>.amazonaws.com:443?tls=true&auth_type=token&api=connect
  ```

  The full hostname can be obtained from the AWS API, e.g. via the CLI:

  ```
  aws emr-serverless get-session-endpoint --application-id <APPLICATION ID> --session-id <SESSION ID>
  ```

  This command will also give you the auth token.

### Amazon EMR (Serverless)

- Amazon EMR is not currently enabled in our automated integration testing.
- To use bulk ingest, set `spark.ingest.location` to a path on S3 where the table data will be stored.
- In our testing, once 25 sessions have been created via Spark Connect (note that this is distinct from an EMR "session"), the server will reject further connections with `Maximum allowed sessions (25) exceeded`, even if prior sessions have been released. (In other words, the maximum session limit is not a maximum _concurrent_ session limit.) A new EMR session must be created to continue.

Also see the above caveats for specific ways to connect to EMR.

### Azure Synapse Analytics

:::{warning}
We have not yet confirmed driver functionality with Azure Synapse Analytics.
:::

- Only Livy is supported.
- The hostname/port to use in the connection URI is `<WORKSPACE NAME>.dev.azuresynapse.net:443`. This can be found as the "Development endpoint" in the Azure portal.
- The connection URI must contain a path component like this:

  ```
  /livyApi/versions/2024-09-20/sparkpools/<NAME OF SPARK POOL>
  ```

- Your user or service principal must have the "Synapse Compute Operator" role. Synapse roles can only be assigned from Synapse Studio, not Azure Portal. See the [Azure documentation](https://learn.microsoft.com/azure/synapse-analytics/security/how-to-manage-synapse-rbac-role-assignments) for more details.

## Feature & Type Support

<table class="docutils data align-default" style="width: 100%">
  <colgroup>
    <col span="1" style="width: 25%;">
    <col span="1" style="width: 25%;">
    <col span="1" style="width: 16.666666666666668%;">
    <col span="1" style="width: 16.666666666666668%;">
    <col span="1" style="width: 16.666666666666668%;">
  </colgroup>
  <thead>
    <tr>
      <th colspan="2">Feature</th>
      <th style="text-align: center;">Spark 3.x (Hive metastore)</th>
      <th style="text-align: center;">Spark 4.x (Hive metastore)</th>
      <th style="text-align: center;">Spark 4.x (Iceberg metastore)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td colspan="2">Bind Parameters</td>
      <td colspan="3" style="text-align: center;">❌</td>
    </tr>
    <tr>
      <td rowspan="8">Bulk Ingestion</td>
      <td>Create</td>
      <td colspan="3" style="text-align: center;">✅</td>
    </tr>
    <tr>
      <td>Append</td>
      <td colspan="3" style="text-align: center;">✅</td>
    </tr>
    <tr>
      <td>Create/Append</td>
      <td colspan="3" style="text-align: center;">✅</td>
    </tr>
    <tr>
      <td>Replace</td>
      <td colspan="3" style="text-align: center;">✅</td>
    </tr>
    <tr>
      <td>Temporary Table</td>
      <td colspan="3" style="text-align: center;">❌</td>
    </tr>
    <tr>
      <td>Target Catalog</td>
      <td colspan="3" style="text-align: center;">❌</td>
    </tr>
    <tr>
      <td>Target Schema</td>
      <td colspan="3" style="text-align: center;">❌</td>
    </tr>
    <tr>
      <td>Non-nullable fields are marked NOT NULL</td>
      <td colspan="3" style="text-align: center;">❌</td>
    </tr>
    <tr>
      <td rowspan="4">Catalog (GetObjects)</td>
      <td>depth=catalogs</td>
      <td colspan="3" style="text-align: center;">✅</td>
    </tr>
    <tr>
      <td>depth=db_schemas</td>
      <td colspan="3" style="text-align: center;">✅</td>
    </tr>
    <tr>
      <td>depth=tables</td>
      <td colspan="3" style="text-align: center;">✅</td>
    </tr>
    <tr>
      <td>depth=columns (all)</td>
      <td colspan="3" style="text-align: center;">✅</td>
    </tr>
    <tr>
      <td colspan="2">Get Parameter Schema</td>
      <td colspan="3" style="text-align: center;">❌</td>
    </tr>
    <tr>
      <td colspan="2">Get Table Schema</td>
      <td colspan="1" style="text-align: center;">❌</td>
      <td colspan="2" style="text-align: center;">✅</td>
    </tr>
    <tr>
      <td colspan="2">Prepared Statements</td>
      <td colspan="3" style="text-align: center;">✅</td>
    </tr>
    <tr>
      <td colspan="2">Transactions</td>
      <td colspan="3" style="text-align: center;">❌</td>
    </tr>
  </tbody>
</table>

### Types

#### Database to Arrow

<table class="docutils data align-default" style="width: 100%;">
<colgroup>
<col span="1" style="width: 25.0%;">
<col span="1" style="width: 25.0%;">
<col span="1" style="width: 25.0%;">
<col span="1" style="width: 25.0%;">
</colgroup>
<thead>
<tr>
<th style="text-align: left; vertical-align: middle;">Database Type</th>
<th style="text-align: center;">Spark 3.x (Hive metastore)</th>
<th style="text-align: center;">Spark 4.x (Hive metastore)</th>
<th style="text-align: center;">Spark 4.x (Iceberg metastore)</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">

BIGINT

</td>
<td colspan="3" style="text-align: center;">

int64

</td>
</tr>
<tr>
<td style="text-align: left;">

BINARY

</td>
<td colspan="3" style="text-align: center;">

binary ⚠️ [^1]

</td>
</tr>
<tr>
<td style="text-align: left;">

BOOLEAN

</td>
<td colspan="3" style="text-align: center;">

bool

</td>
</tr>
<tr>
<td style="text-align: left;">

DATE

</td>
<td colspan="3" style="text-align: center;">

date32[day]

</td>
</tr>
<tr>
<td style="text-align: left;">

DOUBLE

</td>
<td colspan="3" style="text-align: center;">

double

</td>
</tr>
<tr>
<td style="text-align: left;">

INT

</td>
<td colspan="3" style="text-align: center;">

int32

</td>
</tr>
<tr>
<td style="text-align: left;">

NUMERIC

</td>
<td colspan="3" style="text-align: center;">

decimal128

</td>
</tr>
<tr>
<td style="text-align: left;">

REAL

</td>
<td colspan="3" style="text-align: center;">

float

</td>
</tr>
<tr class="row-with-cell-borders">
<td style="text-align: left;">

SMALLINT

</td>
<td colspan="2" style="text-align: center;">

int16

</td>
<td style="text-align: center;">

int16, int32 ⚠️ [^6]

</td>
</tr>
<tr>
<td style="text-align: left;">

TIMESTAMP

</td>
<td colspan="3" style="text-align: center;">

timestamp[us] (with time zone)

</td>
</tr>
<tr class="row-with-cell-borders">
<td style="text-align: left;">

TIMESTAMP_NTZ

</td>
<td style="text-align: center;">

timestamp[us] (with time zone) ⚠️ [^2] [^3] [^4] [^5]

</td>
<td style="text-align: center;">

timestamp[us], timestamp[us] (with time zone) ⚠️ [^3] [^6]

</td>
<td style="text-align: center;">

timestamp[us] ⚠️ [^3]

</td>
</tr>
<tr>
<td style="text-align: left;">

VARCHAR

</td>
<td colspan="3" style="text-align: center;">

string

</td>
</tr>
</tbody>
</table>

#### Arrow to Database

<table class="docutils data align-default" style="width: 100%;">
<colgroup>
<col span="1" style="width: 25.0%;">
<col span="1" style="width: 25.0%;">
<col span="1" style="width: 25.0%;">
<col span="1" style="width: 25.0%;">
</colgroup>
<thead>
<tr>
<th rowspan="3" style="text-align: left; vertical-align: middle;">Arrow Type</th>
<th colspan="1" style="text-align: center;">Spark 3.x (Hive metastore) Type</th>
<th colspan="1" style="text-align: center;">Spark 4.x (Hive metastore) Type</th>
<th colspan="1" style="text-align: center;">Spark 4.x (Iceberg metastore) Type</th>
</tr>
<tr>
<th style="text-align: center;">Ingest</th>
<th style="text-align: center;">Ingest</th>
<th style="text-align: center;">Ingest</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">

binary

</td>
<td colspan="3" style="text-align: center;">

VARBINARY

</td>
</tr>
<tr>
<td style="text-align: left;">

bool

</td>
<td colspan="3" style="text-align: center;">

BOOLEAN

</td>
</tr>
<tr>
<td style="text-align: left;">

date32[day]

</td>
<td colspan="3" style="text-align: center;">

DATE

</td>
</tr>
<tr>
<td style="text-align: left;">

decimal128

</td>
<td colspan="3" style="text-align: center;">

NUMERIC ⚠️ [^7]

</td>
</tr>
<tr>
<td style="text-align: left;">

double

</td>
<td colspan="3" style="text-align: center;">

DOUBLE PRECISION

</td>
</tr>
<tr class="row-with-cell-borders">
<td style="text-align: left;">

fixed_size_binary

</td>
<td style="text-align: center;">

❌

</td>
<td style="text-align: center;">

VARBINARY ⚠️

</td>
<td style="text-align: center;">

VARBINARY

</td>
</tr>
<tr>
<td style="text-align: left;">

float

</td>
<td colspan="3" style="text-align: center;">

REAL

</td>
</tr>
<tr>
<td style="text-align: left;">

int16

</td>
<td colspan="3" style="text-align: center;">

SMALLINT

</td>
</tr>
<tr>
<td style="text-align: left;">

int32

</td>
<td colspan="3" style="text-align: center;">

INT

</td>
</tr>
<tr>
<td style="text-align: left;">

int64

</td>
<td colspan="3" style="text-align: center;">

BIGINT

</td>
</tr>
<tr>
<td style="text-align: left;">

large_binary

</td>
<td colspan="3" style="text-align: center;">

VARBINARY

</td>
</tr>
<tr>
<td style="text-align: left;">

large_string

</td>
<td colspan="3" style="text-align: center;">

VARCHAR

</td>
</tr>
<tr>
<td style="text-align: left;">

string

</td>
<td colspan="3" style="text-align: center;">

VARCHAR

</td>
</tr>
<tr class="row-with-cell-borders">
<td style="text-align: left;">

timestamp[ms]

</td>
<td style="text-align: center;">

❌

</td>
<td colspan="2" style="text-align: center;">

TIMESTAMP(3)

</td>
</tr>
<tr class="row-with-cell-borders">
<td style="text-align: left;">

timestamp[ms] (with time zone)

</td>
<td style="text-align: center;">

❌

</td>
<td colspan="2" style="text-align: center;">

TIMESTAMP(3) WITH TIME ZONE

</td>
</tr>
<tr>
<td style="text-align: left;">

timestamp[ns]

</td>
<td colspan="3" style="text-align: center;">

❌

</td>
</tr>
<tr>
<td style="text-align: left;">

timestamp[ns] (with time zone)

</td>
<td colspan="3" style="text-align: center;">

❌

</td>
</tr>
<tr class="row-with-cell-borders">
<td style="text-align: left;">

timestamp[s]

</td>
<td style="text-align: center;">

❌

</td>
<td colspan="2" style="text-align: center;">

TIMESTAMP(0)

</td>
</tr>
<tr class="row-with-cell-borders">
<td style="text-align: left;">

timestamp[s] (with time zone)

</td>
<td style="text-align: center;">

❌

</td>
<td colspan="2" style="text-align: center;">

TIMESTAMP(0) WITH TIME ZONE

</td>
</tr>
<tr class="row-with-cell-borders">
<td style="text-align: left;">

timestamp[us]

</td>
<td style="text-align: center;">

❌

</td>
<td colspan="2" style="text-align: center;">

TIMESTAMP(6)

</td>
</tr>
<tr class="row-with-cell-borders">
<td style="text-align: left;">

timestamp[us] (with time zone)

</td>
<td style="text-align: center;">

❌

</td>
<td colspan="2" style="text-align: center;">

TIMESTAMP(6) WITH TIME ZONE

</td>
</tr>
</tbody>
</table>

[^1]: The HiveServer2 backend mangles binary values
[^2]: The Livy backend does not support TIMESTAMP_NTZ
[^3]: The HiveServer2 backend cannot differentiate between TIMESTAMP and TIMESTAMP_NTZ
[^4]: Spark 3.5 + Hive 3 does not support TIMESTAMP_NTZ
[^5]: select is not supported
[^6]: Return type is inconsistent depending on how the query was written
[^7]: Negative scales are not supported

## Compatibility

This driver was tested on:

- Apache Spark `3.5.8 (HiveServer2+binary)`

- Apache Spark `3.5.8 5a48a37b2dbd7b51e3640cd1d947438459556cc6 (Apache Livy)`

- Apache Spark `4.0.2 32dd9decae988c1c33a5b0b2c24d2aaef6ef6daa (Spark Connect)`

- Apache Spark `4.0.3 (HiveServer2+HTTP)`

- Apache Spark `4.0.3 (HiveServer2+binary)`

- Apache Spark `4.0.3 322ddd90b63c5d299427b7e32e255e25736db7ee (Spark Connect)`

- Apache Spark `4.1.2 f0bb2e6a47d0ebda424ffd633fcea8644a597954 (Spark Connect)`

## Previous Versions

To see documentation for previous versions of this driver, see the following:

- [v0.1.0-alpha.3.md](./v0.1.0-alpha.3.md)
- [v0.1.0-alpha.2.md](./v0.1.0-alpha.2.md)

[spark]: https://spark.apache.org/
