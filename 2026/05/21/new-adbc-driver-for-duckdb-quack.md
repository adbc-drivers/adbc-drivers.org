---
blogpost: true
date: 2026-05-21
author: ADBC Drivers Contributors
hide-toc: true
orphan: true
---

<!--
  Copyright (c) 2025-2026 ADBC Drivers Contributors

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

# Preview of a new ADBC driver for DuckDB Quack

<p class="blog-post-meta">
  <time datetime="2026-05-21">May 21, 2026</time>
  <span class="blog-post-author">ADBC Drivers Contributors</span>
</p>

A beta release of a new ADBC driver for [DuckDB's Quack protocol](https://duckdb.org/quack/) is now available via [dbc](https://docs.columnar.tech/dbc/). Run `dbc install quack --pre` to try it out today.

The driver supports query execution, bulk ingestion (create, append, and replace modes), catalog metadata retrieval, prepared statements, and transactions. Documentation can be found at [adbc-drivers.org](https://adbc-drivers.org/drivers/quack/). This is a preview release, and more features are actively being developed, so stay tuned.

The driver was developed by the ADBC Driver Foundry, is implemented in C++, and wraps DuckDB itself underneath for full compatibility. See our [blog post](https://columnar.tech/blog/announcing-quack-adbc-driver) for more details on how we built the driver.

To get started, provide a connection URI with a `quack://` scheme:

```
quack://host:port/?token=my-secret
```

The driver can then be used like any other driver. For example, load it in Python with `adbc-driver-manager`:

```
from adbc_driver_manager import dbapi

with (
    dbapi.connect("quack://localhost:9494/?token=quack-secret") as con,
    con.cursor() as cursor,
):
    cursor.execute("FROM range(0, 100, 2)")
    table = cursor.fetch_arrow_table()
```

Bug reports and feature requests are welcome through [GitHub Issues in the `quack` repository](https://github.com/adbc-drivers/quack/issues) in the ADBC Driver Foundry. You can also start a [Discussion](https://github.com/orgs/adbc-drivers/discussions) on GitHub or join the [Columnar Community Slack](https://join.slack.com/t/columnar-community/shared_invite/zt-3gt5cb69i-KRjJj~mjUZv5doVmpcVa4w).
