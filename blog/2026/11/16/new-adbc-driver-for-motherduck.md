---
blogpost: true
date: 2026-11-16
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

# Preview of a new ADBC driver for MotherDuck

An alpha release of a new ADBC driver for [MotherDuck](https://motherduck.com/) is available through [dbc](https://docs.columnar.tech/dbc/). Install version 0.1.0-alpha.1 with:

```console
$ dbc install --pre motherduck
```

The driver supports SQL query execution, bind parameters, table schema discovery, prepared statements, and transactions. See the [ADBC Driver for MotherDuck documentation](https://adbc-drivers.org/drivers/motherduck/). This is a preview release, and more features are actively being developed, so stay tuned. Bulk ingestion and COPY result reads are not supported in this release.

The driver was developed by the ADBC Driver Foundry, is implemented in C++, and is based on Apache Arrow ADBC's libpq-based PostgreSQL driver. It is a dedicated driver for MotherDuck and connects through MotherDuck's PostgreSQL protocol endpoint. It supports MotherDuck token authentication and verifies server certificates by default.

To get started, set the `MOTHERDUCK_TOKEN` environment variable to your MotherDuck token and provide a connection URI with a `motherduck://` scheme:

```text
motherduck:///my_db
```

Set `motherduck.region` to your account's region, which you can find with `md_user_info()`.

The driver can then be used like any other driver. For example, load it in Python with `adbc-driver-manager`, replacing the database name and region with your own:

```python
from adbc_driver_manager import dbapi

with (
    dbapi.connect(
        driver="motherduck",
        db_kwargs={
            "uri": "motherduck:///my_db",
            "motherduck.region": "us-east-1",
        },
    ) as con,
    con.cursor() as cursor,
):
    cursor.execute("SELECT 42")
    table = cursor.fetch_arrow_table()
```

Bug reports and feature requests are welcome through [GitHub Issues in the `motherduck` repository](https://github.com/adbc-drivers/motherduck/issues) in the ADBC Driver Foundry. You can also start a [Discussion](https://github.com/orgs/adbc-drivers/discussions) on GitHub or join the [Columnar Community Slack](https://join.slack.com/t/columnar-community/shared_invite/zt-3gt5cb69i-KRjJj~mjUZv5doVmpcVa4w).
