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

# IBM Db2

:::{toctree}
:maxdepth: 1
:hidden:

Changelog <changelog.md>
v0.1.0-beta.1 <v0.1.0-beta.1.md>
:::

[{badge-primary}`Driver Version|0.1.0-beta.1`](#driver-db2-0.1.0-beta.1 "Permalink") {badge-secondary}`Release Date|2026-11-23` {badge-success}`Tested With|Db2 latest`

This driver provides access to IBM Db2 through the Db2 CLI.

(driver-db2-installing-clidriver)=
## Installing the Db2 CLI driver

The driver needs IBM's Db2 CLI driver (the "clidriver") at run time. Download it
from IBM, then tell your system where its libraries are.

### Download

1. Open IBM's download page:
   <https://public.dhe.ibm.com/ibmdl/export/pub/software/data/db2/drivers/odbc_cli/>
2. Open the folder for the version you want (for example `v12.1.0`) and download
   the file for your platform:

   | Platform       | File                        |
   | -------------- | --------------------------- |
   | Linux x86-64   | `linuxx64_odbc_cli.tar.gz`  |
   | macOS arm64    | `macarm64_odbc_cli.tar.gz`  |
   | Windows x86-64 | `ntx64_odbc_cli.zip`        |

3. Unpack the file. It contains a folder named `clidriver`. Keep the whole
   folder; do not copy only the `libdb2` library out of it.

To download from a terminal instead (Linux x86-64 shown; change the file name
for other platforms):

```bash
mkdir -p "$HOME/db2" && cd "$HOME/db2"
curl -fLO https://public.dhe.ibm.com/ibmdl/export/pub/software/data/db2/drivers/odbc_cli/v12.1.0/linuxx64_odbc_cli.tar.gz
tar xzf linuxx64_odbc_cli.tar.gz
```

On macOS, a file downloaded through a browser may be quarantined and the system
may refuse to load `libdb2.dylib`. Downloading with `curl`, or running
`xattr -dr com.apple.quarantine clidriver` on the unpacked folder, avoids this.

### Tell the system where the libraries are

Set the variable for your platform in the same shell that starts your program,
before it starts. Replace `$HOME/db2` with the folder you unpacked into.

| Platform | Variable            | Value                           |
| -------- | ------------------- | ------------------------------- |
| Linux    | `LD_LIBRARY_PATH`   | `$HOME/db2/clidriver/lib`       |
| macOS    | `DYLD_LIBRARY_PATH` | `$HOME/db2/clidriver/lib`       |
| Windows  | `PATH`              | `<unpack folder>\clidriver\bin` |

For example, on Linux:

```bash
export LD_LIBRARY_PATH="$HOME/db2/clidriver/lib${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}"
```

## Connecting

Provide a Db2 CLI connection string as the `uri` database option. The driver
passes the string unchanged to the Db2 CLI function `SQLDriverConnect`, so it
uses Db2 CLI `KEYWORD=value;` syntax. It is not parsed as a URL.

```python
import os

from adbc_driver_manager import dbapi

with dbapi.connect(
    driver="db2",
    db_kwargs={
        "uri": "DATABASE=testdb;HOSTNAME=localhost;PORT=50000;PROTOCOL=TCPIP;"
        f"UID=db2inst1;PWD={os.environ['DB2_PASSWORD']}",
    },
) as connection:
    pass
```

Keep the password out of your source code, for example by reading it from an
environment variable as above.

| Keyword    | Meaning                                              |
| ---------- | ---------------------------------------------------- |
| `DATABASE` | Name of the database to connect to                   |
| `HOSTNAME` | Host name or IP address of the Db2 server            |
| `PORT`     | Port the Db2 server listens on                       |
| `PROTOCOL` | Communication protocol; use `TCPIP`                  |
| `UID`      | User name                                            |
| `PWD`      | Password                                             |

Any other Db2 CLI keyword can be added to the string in the same way.

### Connecting with SSL

SSL needs a port on which the server accepts SSL connections; ask your database
administrator for it. Add `SECURITY=SSL` to the connection string:

```text
DATABASE=testdb;HOSTNAME=db2.example.com;PORT=50001;PROTOCOL=TCPIP;UID=db2inst1;PWD=...;SECURITY=SSL
```

Which other settings you need depends on the server certificate:

- **Certificate signed by a widely used certificate authority.** Per IBM's
  documentation, the Db2 CLI driver ships a default set of root certificates, so
  `SECURITY=SSL` alone is normally enough.
- **Self-signed or private certificate.** Give the driver the server certificate
  file (`.arm`) with `SSLServerCertificate`:

  ```text
  ...;SECURITY=SSL;SSLServerCertificate=/path/to/server.arm
  ```

- **Your own client key database.** Use `SSLClientKeystoredb` (the `.kdb` file)
  and `SSLClientKeystash` (the `.sth` file that holds its password).

SSL uses IBM's GSKit libraries, which ship inside the `clidriver` folder, so keep
the folder intact.

You can set these in the connection string as shown, or as separate database
options. The driver adds an option's keyword to the connection string only when
that keyword (in the same capitalization) is not already in it, so use one method
per setting.

| Database option              | Connection string keyword | Meaning                           |
| ---------------------------- | ------------------------- | --------------------------------- |
| `db2.ssl.security`           | `SECURITY`                | `SSL` turns on SSL                |
| `db2.ssl.client_keystoredb`  | `SSLClientKeystoredb`     | Client key database (`.kdb`)      |
| `db2.ssl.client_keystash`    | `SSLClientKeystash`       | Stash file (`.sth`) with password |
| `db2.ssl.server_certificate` | `SSLServerCertificate`    | Server certificate (`.arm`)       |

```python
import os

from adbc_driver_manager import dbapi

with dbapi.connect(
    driver="db2",
    db_kwargs={
        "uri": "DATABASE=testdb;HOSTNAME=db2.example.com;PORT=50001;PROTOCOL=TCPIP;"
        f"UID=db2inst1;PWD={os.environ['DB2_PASSWORD']}",
        "db2.ssl.security": "SSL",
        "db2.ssl.server_certificate": "/path/to/server.arm",
    },
) as connection:
    pass
```

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
      <th style="text-align: center;">Db2</th>
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
      <td colspan="1" style="text-align: center;">❌</td>
    </tr>
    <tr>
      <td>Target Catalog</td>
      <td colspan="1" style="text-align: center;">❌</td>
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
<th style="text-align: center;">Db2</th>
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

string [^1]

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

time32[s] ⚠️ [^2]

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

TIMESTAMP(0)

</td>
<td style="text-align: center;">

timestamp[s]

</td>
</tr>
<tr>
<td style="text-align: left;">

TIMESTAMP(p) (1 &lt;= p &lt;= 3)

</td>
<td style="text-align: center;">

timestamp[ms]

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

TIMESTAMP(p) (7 &lt;= p &lt;= 9)

</td>
<td style="text-align: center;">

timestamp[ns]

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
<th colspan="2" style="text-align: center;">Db2 Type</th>
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
<tr class="row-with-cell-borders">
<td style="text-align: left;">

bool

</td>
<td style="text-align: center;">

BOOLEAN

</td>
<td style="text-align: center;">

SMALLINT [^3]

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

NUMERIC [^1]

</td>
<td style="text-align: center;">

DECIMAL [^4]

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

❌

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
<tr class="row-with-cell-borders">
<td style="text-align: left;">

string_view

</td>
<td style="text-align: center;">

❌

</td>
<td style="text-align: center;">

VARCHAR

</td>
</tr>
<tr>
<td style="text-align: left;">

time32[ms]

</td>
<td colspan="2" style="text-align: center;">

TIME ⚠️ [^2]

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

TIME ⚠️ [^2]

</td>
</tr>
<tr>
<td style="text-align: left;">

time64[us]

</td>
<td colspan="2" style="text-align: center;">

TIME ⚠️ [^2]

</td>
</tr>
<tr>
<td style="text-align: left;">

timestamp[ms]

</td>
<td colspan="2" style="text-align: center;">

TIMESTAMP(3)

</td>
</tr>
<tr>
<td style="text-align: left;">

timestamp[ns]

</td>
<td colspan="2" style="text-align: center;">

TIMESTAMP(9)

</td>
</tr>
<tr>
<td style="text-align: left;">

timestamp[s]

</td>
<td colspan="2" style="text-align: center;">

TIMESTAMP(0)

</td>
</tr>
<tr>
<td style="text-align: left;">

timestamp[us]

</td>
<td colspan="2" style="text-align: center;">

TIMESTAMP(6)

</td>
</tr>
</tbody>
</table>

## Compatibility

This driver was tested on:

- DB2/LINUXX8664 `12.01.0500`

[^1]: The driver returns DECIMAL values as exact UTF-8 strings.
[^2]: Db2 TIME stores whole seconds; fractional seconds are truncated.
[^3]: The driver ingests booleans as SMALLINT: true is 1 and false is 0.
[^4]: The driver ingests decimals into DECIMAL(31,8) and returns exact UTF-8 strings.
