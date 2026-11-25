---
blogpost: true
date: 2026-11-24
author: ADBC Drivers Contributors
hide-toc: true
orphan: true
---

<!--
  Copyright (c) 2026 ADBC Drivers Contributors

  Licensed under the Apache License, Version 2.0 (the "License");
  you may not use this file except in compliance with the License.
  You may obtain a copy of the License at

          http://www.apache.org/licenses/LICENSE-2.0

  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License.
-->

# Preview of a new ADBC driver for IBM Db2

A beta release of a new ADBC driver for [IBM Db2](https://www.ibm.com/products/db2) is available through [dbc](https://docs.columnar.tech/dbc/). Install version 0.1.0-beta.1 with:

```console
$ dbc install --pre db2
```

The driver supports SQL query execution, bulk ingestion, bind parameters, table schema discovery, prepared statements, and transactions. See the [ADBC Driver for IBM Db2 documentation](/drivers/db2/index.md). This is a preview release, and more features are actively being developed, so stay tuned.

The driver was developed by IBM with support from the ADBC Driver Foundry. It is implemented in C++, and is based on IBM's [CLI driver ("clidriver")](https://www.ibm.com/docs/en/db2/12.1.x?topic=drivers-data-server-driver-odbc-cli).

To get started, first install the clidriver and configure the shared library search path (see the {ref}`documentation <driver-db2-installing-clidriver>`), then provide a connection string:

```
DATABASE=testdb;HOSTNAME=localhost;PORT=50000;PROTOCOL=TCPIP;UID=db2inst1;PWD=password
```

The driver can then be used like any other driver. For example, load it in Python with `adbc-driver-manager`, replacing the database name and region with your own:

```python
from adbc_driver_manager import dbapi

with (
    dbapi.connect(
        driver="oracle",
        db_kwargs={
            "uri": "DATABASE=testdb;HOSTNAME=localhost;PORT=50000;PROTOCOL=TCPIP;UID=db2inst1;PWD=password",
        },
    ) as con,
    con.cursor() as cursor,
):
    cursor.execute("SELECT 42")
    table = cursor.fetch_arrow_table()
```

Bug reports and feature requests are welcome through [GitHub Issues in the `db2` repository](https://github.com/adbc-drivers/db2/issues) in the ADBC Driver Foundry. You can also start a [Discussion](https://github.com/orgs/adbc-drivers/discussions) on GitHub or join the [Columnar Community Slack](https://join.slack.com/t/columnar-community/shared_invite/zt-3gt5cb69i-KRjJj~mjUZv5doVmpcVa4w).
