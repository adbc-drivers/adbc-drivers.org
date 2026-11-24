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

# Preview of a new ADBC driver for Oracle Database

A beta release of a new ADBC driver for [Oracle Database](https://www.oracle.com/database/) is available through [dbc](https://docs.columnar.tech/dbc/). Install version 0.8.0-beta.1 with:

```console
$ dbc install --pre oracle
```

The driver supports SQL query execution, bulk ingestion, bind parameters, table schema discovery, prepared statements, and transactions. See the [ADBC Driver for Oracle Database documentation](https://adbc-drivers.org/drivers/oracle/). This is a preview release, and more features are actively being developed, so stay tuned.

The driver was developed by Oracle with support from the ADBC Driver Foundry. It is implemented in Rust, and is based on Oracle's [rust-oracledb](https://github.com/oracle/rust-oracledb) crate.

To get started, provide a connection URI with an `oracle://` scheme:

```
oracle://user:password@localhost:1521/FREEPDB1
```

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

Bug reports and feature requests are welcome through [GitHub Issues in the `oracle` repository](https://github.com/adbc-drivers/oracle/issues) in the ADBC Driver Foundry. You can also start a [Discussion](https://github.com/orgs/adbc-drivers/discussions) on GitHub or join the [Columnar Community Slack](https://join.slack.com/t/columnar-community/shared_invite/zt-3gt5cb69i-KRjJj~mjUZv5doVmpcVa4w).

---

Note that Columnar previously provided a driver for Oracle Database built on the Oracle Instant Client. That driver is still available from the dbc CDN as version 0.7.1, but will no longer receive updates, and it is recommended to use the official driver described here and in the documentation. We are actively working on full feature parity in the new driver.
