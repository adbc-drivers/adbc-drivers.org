---
blogpost: true
date: 2026-10-12
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

# New ADBC driver for Firebolt

The first Foundry release of the ADBC driver for [Firebolt](https://www.firebolt.io/) is available through [dbc](https://docs.columnar.tech/dbc/). Install version 0.2.0 with:

```console
$ dbc install firebolt
```

The driver supports query execution, bind parameters, bulk ingestion (create, append, create-or-append, and replace modes), catalog metadata retrieval, table schema discovery, prepared statements, and transactions. See the [ADBC Driver for Firebolt documentation](/drivers/firebolt/index.md).

The driver is part of the ADBC Driver Foundry and is implemented in C++. It uses Firebolt's HTTP query interface with native Apache Arrow support and supports HTTP and HTTPS connections, bearer token authentication, and custom CA certificates.

To get started, provide a connection URI with a `firebolt://` scheme:

```
firebolt://localhost:3473
```

The driver can then be used like any other driver. For example, load it in Python with `adbc-driver-manager`:

```python
from adbc_driver_manager import dbapi

with (
    dbapi.connect("firebolt://localhost:3473") as con,
    con.cursor() as cursor,
):
    cursor.execute("SELECT * FROM my_table")
    table = cursor.fetch_arrow_table()
```

Bug reports and feature requests are welcome through [GitHub Issues in the `firebolt` repository](https://github.com/adbc-drivers/firebolt/issues) in the ADBC Driver Foundry. You can also start a [Discussion](https://github.com/orgs/adbc-drivers/discussions) on GitHub or join the [Columnar Community Slack](https://join.slack.com/t/columnar-community/shared_invite/zt-3gt5cb69i-KRjJj~mjUZv5doVmpcVa4w).
