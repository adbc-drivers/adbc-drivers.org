---
# Copyright (c) 2026 ADBC Drivers Contributors
{}
---

# Amazon Redshift

:::{toctree}
:maxdepth: 1
:hidden:

Changelog <changelog.md>
v1.9.0 <v1.9.0.md>
v1.8.1 <v1.8.1.md>
v1.8.0 <v1.8.0.md>
v1.7.0 <v1.7.0.md>
v1.6.0 <v1.6.0.md>
v1.5.0 <v1.5.0.md>
v1.4.0 <v1.4.0.md>
v1.3.0 <v1.3.0.md>
v1.2.1 <v1.2.1.md>
v1.1.0 <v1.1.0.md>
v1.0.0 <v1.0.0.md>
:::

[{badge-primary}`Driver Version|v1.9.0`](#driver-redshift-v1.9.0 "Permalink") {badge-secondary}`Release Date|2026-11-10` {badge-success}`Tested With|Amazon Redshift aws`

This driver provides access to [Amazon Redshift][redshift]{target="_blank"}
(commonly referred to as just "Redshift").

:::{note}
This project is not affiliated with Amazon.
:::

## Installation

The Redshift driver can be installed with [dbc](https://docs.columnar.tech/dbc):

```bash
dbc install redshift
```

## Connecting

To connect, edit the `uri`, `redshift.cluster_type`, `redshift.workgroup_name`, and `redshift.db_name` options below to match your environment and run the following:

```python
from adbc_driver_manager import dbapi

dbapi.connect(
    driver="redshift",
    db_kwargs={
        "uri": "postgresql://localhost:5439",
        # "uri": "postgresql://<cluster hostname>:<cluster port>", # for direct connection
        "redshift.cluster_type": "redshift-serverless",  # for Redshift Serverless
        # "redshift.cluster_type": "redshift-iam", # for Redshift Provisioned with IAM auth
        # "redshift.cluster_type": "redshift", # for Redshift Provisioned with user/password auth
        "redshift.workgroup_name": "<WORKGROUP_NAME>",  # for Redshift Serverless
        # "redshift.cluster_identifier": "<CLUSTER IDENTIFIER>", # for Redshift Provisioned
        "redshift.db_name": "sample_data_dev",
    },
)
```

Note: The example above is for Python using the [adbc-driver-manager](https://pypi.org/project/adbc-driver-manager) package but the process will be similar for other driver managers.

### Connection String Format

Connection strings are passed with the `uri` option. Redshift's URI syntax supports two primary forms:

1. Explicit endpoint, for direct connections or standard user/password authentication:

   ```
   redshift://[user[:password]@]host[:port]/dbname[?param1=value1&param2=value2]
   ```

2. Endpoint discovery, for IAM authentication and serverless connections:

   ```
   redshift:///dbname[?param1=value1&param2=value2]
   ```

   Note the triple slash (`///`). This indicates an empty host, signaling the driver to discover the endpoint using the provided query parameters (e.g., `cluster_identifier` or `workgroup_name`).

Components:
- Scheme: redshift:// (required)
- User/Password: Optional (for standard user/password authentication with `cluster_type=redshift`)
  - Ignored if cluster_type is `redshift-serverless`
  - If cluster_type is `redshift-iam`, then if omitted, the driver will log in with the current IAM identity; else it will fetch credentials for the given username
  - For cluster_type `redshift`, the driver will fetch credentials for the given username
- Host/Port: The Redshift cluster endpoint (e.g., my-cluster.c...com:5439)
  - If omitted (using redshift:///), the driver will discover this using the AWS SDK
- Database: Required (e.g., /dev)
- Query Parameters: Configuration options

See [Amazon Redshift JDBC Connection URL](https://docs.aws.amazon.com/redshift/latest/mgmt/jdbc20-build-connection-url.html) for connection URL format and [Amazon Redshift JDBC Configuration Options](https://docs.aws.amazon.com/redshift/latest/mgmt/jdbc20-configuration-options.html) for complete parameter reference.

:::{note}
Reserved characters in URI elements must be URI-encoded. For example, `@` becomes `%40`.
:::

Examples:
- redshift://admin_user:secret@my-cluster.region.redshift.amazonaws.com:5439/dev
- redshift:///dev?cluster_type=redshift-iam&cluster_identifier=my-cluster
- redshift:///dev?cluster_type=redshift-serverless&workgroup_name=my-workgroup
- redshift://admin:pass@localhost:5439/dev?sslmode=disable
- redshift:///dev?cluster_type=redshift-serverless&workgroup_name=my-workgroup&aws_region=us-west-1&aws_access_key_id=AKIA...&aws_secret_access_key=secret
- redshift:///dev?cluster_type=redshift-iam&cluster_identifier=my-cluster&auth_provider=BrowserIdcAuthPlugin&idc_region=us-east-1&issuer_url=https://example.com
- redshift:///dev?cluster_type=redshift&cluster_identifier=my-cluster&username=newuser&auto_create_user=true

The driver also supports standard PostgreSQL connection strings (e.g., `postgresql://user:pass@host:port/dbname`) as the `uri` option. When using this format, all Redshift-specific parameters (e.g., `redshift.cluster_type`, `redshift.workgroup_name`) must be passed as separate connection options. However, using the standard `redshift://` URI is recommended.

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
      <th style="text-align: center;">Amazon Redshift</th>
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
<colgroup>
<col span="1" style="width: 50.0%;">
<col span="1" style="width: 50.0%;">
</colgroup>
<thead>
<tr>
<th style="text-align: left; vertical-align: middle;">Database Type</th>
<th style="text-align: center;">Amazon Redshift</th>
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

HLLSKETCH

</td>
<td style="text-align: center;">

extension&lt;arrow.opaque[storage_type=string, type_name=HLLSKETCH, vendor_name=Amazon Redshift]&gt;

</td>
</tr>
<tr>
<td style="text-align: left;">

INTEGER

</td>
<td style="text-align: center;">

int32

</td>
</tr>
<tr>
<td style="text-align: left;">

INTERVAL DAY TO SECOND

</td>
<td style="text-align: center;">

month_day_nano_interval

</td>
</tr>
<tr>
<td style="text-align: left;">

INTERVAL YEAR TO MONTH

</td>
<td style="text-align: center;">

month_day_nano_interval

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

SUPER

</td>
<td style="text-align: center;">

extension&lt;arrow.json&gt;

</td>
</tr>
<tr>
<td style="text-align: left;">

TIME

</td>
<td style="text-align: center;">

time64[us]

</td>
</tr>
<tr>
<td style="text-align: left;">

TIMESTAMP

</td>
<td style="text-align: center;">

timestamp[us]

</td>
</tr>
<tr>
<td style="text-align: left;">

TIMESTAMP WITH TIME ZONE

</td>
<td style="text-align: center;">

timestamp[us] (with time zone)

</td>
</tr>
<tr>
<td style="text-align: left;">

TIMETZ

</td>
<td style="text-align: center;">

extension&lt;arrow.opaque[storage_type=string, type_name=TIMETZ, vendor_name=Amazon Redshift]&gt; [^1]

</td>
</tr>
<tr>
<td style="text-align: left;">

VARBYTE

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
<th colspan="2" style="text-align: center;">Amazon Redshift Type</th>
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

VARBYTE ⚠️ [^2]

</td>
<td style="text-align: center;">

VARBYTE

</td>
</tr>
<tr class="row-with-cell-borders">
<td style="text-align: left;">

binary_view

</td>
<td style="text-align: center;">

VARBYTE ⚠️ [^2]

</td>
<td style="text-align: center;">

❌ [^9]

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
<tr class="row-with-cell-borders">
<td style="text-align: left;">

decimal128

</td>
<td style="text-align: center;">

DECIMAL

</td>
<td style="text-align: center;">

DECIMAL, NUMERIC ⚠️ [^10]

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
<tr class="row-with-cell-borders">
<td style="text-align: left;">

extension&lt;arrow.json&gt;

</td>
<td style="text-align: center;">

SUPER

</td>
<td style="text-align: center;">

SUPER ⚠️ [^11]

</td>
</tr>
<tr class="row-with-cell-borders">
<td style="text-align: left;">

extension&lt;geoarrow.wkb&gt;

</td>
<td style="text-align: center;">

GEOGRAPHY, GEOMETRY ⚠️ [^3] [^4]

</td>
<td style="text-align: center;">

(NA/not tested)

</td>
</tr>
<tr class="row-with-cell-borders">
<td style="text-align: left;">

extension&lt;geoarrow.wkt&gt;

</td>
<td style="text-align: center;">

GEOGRAPHY, GEOMETRY ⚠️ [^5] [^6]

</td>
<td style="text-align: center;">

GEOMETRY

</td>
</tr>
<tr class="row-with-cell-borders">
<td style="text-align: left;">

fixed_size_binary

</td>
<td style="text-align: center;">

VARBYTE ⚠️ [^2]

</td>
<td style="text-align: center;">

❌ [^12]

</td>
</tr>
<tr class="row-with-cell-borders">
<td style="text-align: left;">

float

</td>
<td style="text-align: center;">

REAL ⚠️ [^7]

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

INTEGER

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
<tr class="row-with-cell-borders">
<td style="text-align: left;">

large_binary

</td>
<td style="text-align: center;">

VARBYTE ⚠️ [^2]

</td>
<td style="text-align: center;">

VARBYTE

</td>
</tr>
<tr class="row-with-cell-borders">
<td style="text-align: left;">

large_string

</td>
<td style="text-align: center;">

VARCHAR

</td>
<td style="text-align: center;">

VARCHAR(MAX)

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

SUPER

</td>
</tr>
<tr class="row-with-cell-borders">
<td style="text-align: left;">

string

</td>
<td style="text-align: center;">

VARCHAR

</td>
<td style="text-align: center;">

VARCHAR(MAX)

</td>
</tr>
<tr class="row-with-cell-borders">
<td style="text-align: left;">

string_view

</td>
<td style="text-align: center;">

VARCHAR

</td>
<td style="text-align: center;">

❌ [^13]

</td>
</tr>
<tr>
<td style="text-align: left;">

struct

</td>
<td colspan="2" style="text-align: center;">

SUPER

</td>
</tr>
<tr class="row-with-cell-borders">
<td style="text-align: left;">

time32[ms]

</td>
<td style="text-align: center;">

TIME

</td>
<td style="text-align: center;">

❌ [^14]

</td>
</tr>
<tr class="row-with-cell-borders">
<td style="text-align: left;">

time32[s]

</td>
<td style="text-align: center;">

TIME

</td>
<td style="text-align: center;">

❌ [^14]

</td>
</tr>
<tr class="row-with-cell-borders">
<td style="text-align: left;">

time64[ns]

</td>
<td style="text-align: center;">

TIME

</td>
<td style="text-align: center;">

❌ [^14]

</td>
</tr>
<tr class="row-with-cell-borders">
<td style="text-align: left;">

time64[us]

</td>
<td style="text-align: center;">

TIME

</td>
<td style="text-align: center;">

❌ [^14]

</td>
</tr>
<tr>
<td style="text-align: left;">

timestamp[ms]

</td>
<td colspan="2" style="text-align: center;">

TIMESTAMP

</td>
</tr>
<tr class="row-with-cell-borders">
<td style="text-align: left;">

timestamp[ms] (with time zone)

</td>
<td style="text-align: center;">

TIMESTAMP(3) WITH TIME ZONE

</td>
<td style="text-align: center;">

TIMESTAMPTZ

</td>
</tr>
<tr class="row-with-cell-borders">
<td style="text-align: left;">

timestamp[ns]

</td>
<td style="text-align: center;">

TIMESTAMP [^8]

</td>
<td style="text-align: center;">

TIMESTAMP

</td>
</tr>
<tr class="row-with-cell-borders">
<td style="text-align: left;">

timestamp[ns] (with time zone)

</td>
<td style="text-align: center;">

TIMESTAMP(9) WITH TIME ZONE

</td>
<td style="text-align: center;">

TIMESTAMPTZ

</td>
</tr>
<tr>
<td style="text-align: left;">

timestamp[s]

</td>
<td colspan="2" style="text-align: center;">

TIMESTAMP

</td>
</tr>
<tr class="row-with-cell-borders">
<td style="text-align: left;">

timestamp[s] (with time zone)

</td>
<td style="text-align: center;">

TIMESTAMP(0) WITH TIME ZONE

</td>
<td style="text-align: center;">

TIMESTAMPTZ

</td>
</tr>
<tr>
<td style="text-align: left;">

timestamp[us]

</td>
<td colspan="2" style="text-align: center;">

TIMESTAMP

</td>
</tr>
<tr class="row-with-cell-borders">
<td style="text-align: left;">

timestamp[us] (with time zone)

</td>
<td style="text-align: center;">

TIMESTAMP(6) WITH TIME ZONE

</td>
<td style="text-align: center;">

TIMESTAMPTZ

</td>
</tr>
</tbody>
</table>

## Options

### Connection Options

`redshift.application_name`
: **Type:** string.

  The application name to present to the server.

`redshift.auth.idc_client_display_name`
: **Type:** string.

  For browser-based authentication, the client name to display in the AWS IAM Identity Center.

`redshift.auth.idc_region`
: **Type:** string.

  For browser-based authentication, the AWS region of the IdC.

`redshift.auth.idp_response_timeout_seconds`
: **Type:** integer. **Default:** 120

  For IdP token authentication, how long to wait (in seconds) for the SSO flow to complete.

`redshift.auth.issuer_url`
: **Type:** string.

  For browser-based authentication, the issuer URL.

`redshift.auth.listen_port`
: **Type:** integer. **Default:** 7890.

  For browser-based authentication, the local port to listen on. Use port 0 to have the operating system assign a free port.

`redshift.auth.provider`
: **Values:** `userpass`, `BrowserIdcAuthPlugin`, `IdpTokenAuthPlugin`. **Default:** `userpass`.

  How to authenticate. The default is user-password; `BrowserIdcAuthPlugin` triggers an authentication flow in the browser, while `IdpTokenAuthPlugin` fetches a token from an IdP.

`redshift.auth.token`
: **Type:** string.

  An auth token to use with IdP token authentication.

`redshift.auth.token_endpoint.request_data`
: **Type:** string.

  The form-urlencoded request body to POST to the IdP token endpoint.

`redshift.auth.token_endpoint.request_headers`
: **Type:** string.

  Request headers to send to the IdP token endpoint, encoded as a JSON map.

`redshift.auth.token_endpoint.request_url`
: **Type:** string.

  The URL of the IdP token endpoint.

`redshift.auth.token_type`
: **Values:** `ACCESS_TOKEN`, `EXT_JWT`.

  The token type to use with IdP token authentication.

`redshift.auto_create_user`
: **Type:** boolean. **Default:** false.

  When connecting via IAM, whether to create the user if it does not exist.

`redshift.aws.access_key_id`
: **Type:** string.

  Explicitly supply the access key ID (by default the AWS SDK configures this, if needed).

`redshift.aws.region`
: **Type:** string.

  Explicitly supply the region (by default the AWS SDK configures this).

`redshift.aws.secret_access_key`
: **Type:** string.

  Explicitly supply the secret access key (by default the AWS SDK configures this, if needed).

`redshift.aws.session_token`
: **Type:** string.

  Explicitly supply the session token (by default the AWS SDK configures this, if needed).

`redshift.aws.profile`
: **Type:** string.

  Explicitly supply the profile to use (by default the AWS SDK configures this).

`redshift.cluster_identifier`
: **Type:** string.

  The cluster to connect to (only applicable if `cluster_type` is `redshift` or `redshift-iam`).

`redshift.cluster_type`
: **Values:** `redshift`, `redshift-iam`, or `redshift-serverless`.

  The type of Redshift cluster we are connecting to. `redshift` and `redshift-iam` both refer to Redshift clusters, while `redshift-serverless` means Redshift Serverless. They defer in how various other connection parameters are validated/inferred; see the connection documentation above.

`redshift.connect_timeout_ms`
: **Type:** integer.

  A connection timeout, in milliseconds.

`redshift.custom_domain_name`
: **Type:** string.

  Specify the workgroup to use by its custom domain name.

`redshift.db_groups`
: **Type:** string.

  A list of groups that the user should join on connection, as a JSON-serialized list of strings.

`redshift.db_name`
: **Type:** string.

  The name of the database to connect to.

`redshift.ssl_cert`, `redshift.ssl_key`, `redshift.ssl_mode`, `redshift.ssl_root_key`
: Configure SSL/TLS options. See the [Redshift documentation](https://docs.aws.amazon.com/redshift/latest/mgmt/connecting-ssl-support.html) for details.

`redshift.workgroup_name`
: **Type:** string.

  Specify the workgroup to use by its name.

### Bulk Ingest Options

`redshift.ingest.bucket`
: **Type:** string

  The S3 bucket to use as a staging area when ingesting data.

`redshift.ingest.geo_type`
: **Values:** `GEOMETRY`, `GEOGRAPHY`. **Default:** `GEOMETRY`.

  Whether GeoArrow columns (geoarrow.wkb, geoarrow.wkt) are ingested as GEOMETRY (default) or GEOGRAPHY.

`redshift.ingest.geoarrow_wkb_size`
: **Type:** integer. **Default:** 1048576

  The size of VARBYTE columns created during ingest, used as staging columns for GeoArrow WKB data.

`redshift.ingest.varbyte_size`
: **Type:** integer. **Default:** 65536

  The size of VARBYTE columns created during ingest.

## Caveats

- Temporary tables are shown in GetObjects, however, the order of the columns of these tables is not guaranteed to be correct. Also, less column/table metadata is returned.

## Previous Versions

To see documentation for previous versions of this driver, see the following:

- [v1.8.1](./v1.8.1.md)
- [v1.8.0](./v1.8.0.md)
- [v1.7.0](./v1.7.0.md)
- [v1.6.0](./v1.6.0.md)
- [v1.5.0](./v1.5.0.md)
- [v1.4.0](./v1.4.0.md)
- [v1.3.0](./v1.3.0.md)
- [v1.2.1](./v1.2.1.md)
- [v1.1.0](./v1.1.0.md)
- [v1.0.0](./v1.0.0.md)

[^1]: Redshift appears not to return the timezone; it is always +00
[^2]: null bytes in bind parameters will instead end the value (e.g. [A, 0x00, B] will instead get inserted as [A])
[^3]: The bind parameter must be converted with ST_GeogFromWKB, but the driver will convert the WKB to the hex string required by Redshift
[^4]: The bind parameter must be converted with ST_GeomFromWKB, but the driver will convert the WKB to the hex string required by Redshift
[^5]: The bind parameter must be converted with ST_GeogFromText
[^6]: The bind parameter must be converted with ST_GeomFromText
[^7]: precision is limited
[^8]: Timestamp will be rounded to microseconds
[^9]: arrow-go does not support writing binary view to Parquet
[^10]: Negative scales are not supported
[^11]: Redshift interprets the JSON data as a string, so the result will be unexpected.  Use struct/list data instead.
[^12]: Redshift cannot read Parquet files with fixed-size binary columns
[^13]: arrow-go does not support writing string view to Parquet
[^14]: Redshift raises an ASSERT

[redshift]: https://aws.amazon.com/redshift/
