---
blogpost: true
date: 2026-11-25
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

# New ADBC driver for Kinetica

A new ADBC driver for [Kinetica](https://www.kinetica.com/), [version 7.2.1](https://github.com/adbc-drivers/kinetica/releases/tag/rust%2Fv7.2.1), is now available through [dbc](https://docs.columnar.tech/dbc/). Install it with:

```console
$ dbc install kinetica
```

The driver supports SQL query execution, bind parameters, bulk ingestion, catalog and table schema discovery, table statistics, and partitioned reads. It requires Kinetica 7.2.3.24 or later. See the [ADBC Driver for Kinetica documentation](https://adbc-drivers.org/drivers/kinetica/).

The driver is developed by Kinetica DB, Inc. and built and distributed by the ADBC Driver Foundry. It is implemented in Rust, reads Arrow results returned by Kinetica, and routes bulk ingestion to the cluster's worker ranks. Connections support password and OAuth authentication, TLS, and failover between clusters in an HA ring.

To get started, provide a connection URI with a `kinetica://` scheme. Connections use HTTPS by default; append `?tls=false` when connecting to a local server configured for HTTP.

For example, load the driver in Python with `adbc-driver-manager`, replacing the server address and credentials with your own:

```python
from adbc_driver_manager import dbapi

with (
    dbapi.connect(
        driver="kinetica",
        db_kwargs={
            "uri": "kinetica://kinetica.example.com:9191",
            "username": "your_username",
            "password": "your_password",
        },
        autocommit=True,
    ) as con,
    con.cursor() as cursor,
):
    cursor.execute("SELECT 42 AS answer")
    table = cursor.fetch_arrow_table()
```

Bug reports and feature requests are welcome through [GitHub Issues in the `kinetica` repository](https://github.com/adbc-drivers/kinetica/issues) in the ADBC Driver Foundry. You can also start a [Discussion](https://github.com/orgs/adbc-drivers/discussions) on GitHub or join the [Columnar Community Slack](https://join.slack.com/t/columnar-community/shared_invite/zt-3gt5cb69i-KRjJj~mjUZv5doVmpcVa4w).
