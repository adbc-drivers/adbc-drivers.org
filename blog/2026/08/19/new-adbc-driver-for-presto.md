---
blogpost: true
date: 2026-08-19
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

# Preview of a new ADBC driver for Presto

<p class="blog-post-meta">
  <time datetime="2026-08-19">August 19, 2026</time>
  <span class="blog-post-author">ADBC Drivers Contributors</span>
</p>

An alpha release of a new ADBC driver for [Presto](https://prestodb.io/) is now available via [dbc](https://docs.columnar.tech/dbc/). Run `dbc install --pre presto` to try version 0.1.0-alpha.1 today.

The driver supports query execution, bind parameters, bulk ingestion (create, append, create-or-append, and replace modes), catalog metadata retrieval, table schema discovery, and prepared statements. Documentation can be found at [adbc-drivers.org](https://adbc-drivers.org/drivers/presto/). This is a preview release, and more features are actively being developed, so stay tuned.

The driver was developed by the ADBC Driver Foundry, is implemented in Go, and is built on the [Presto Go client](https://github.com/prestodb/presto-go-client). It supports HTTP and HTTPS connections, including custom CA certificates and mutual TLS, and passes unrecognized connection parameters to Presto as session properties.

To get started, provide a connection URI with a `presto://` scheme:

```
presto://user:password@host:8080/catalog/schema
```

The driver can then be used like any other driver. For example, load it in Python with `adbc-driver-manager`:

```python
from adbc_driver_manager import dbapi

with (
    dbapi.connect(
        driver="presto",
        db_kwargs={"uri": "presto://user@localhost:8080/tpch/tiny"},
        autocommit=True,
    ) as con,
    con.cursor() as cursor,
):
    cursor.execute("SELECT * FROM nation")
    table = cursor.fetch_arrow_table()
```

Bug reports and feature requests are welcome through [GitHub Issues in the `presto` repository](https://github.com/adbc-drivers/presto/issues) in the ADBC Driver Foundry. You can also start a [Discussion](https://github.com/orgs/adbc-drivers/discussions) on GitHub or join the [Columnar Community Slack](https://join.slack.com/t/columnar-community/shared_invite/zt-3gt5cb69i-KRjJj~mjUZv5doVmpcVa4w).
