---
blogpost: true
date: 2026-08-25
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

# Preview of a new ADBC driver for Apache Cassandra

<p class="blog-post-meta">
  <time datetime="2026-08-25">August 25, 2026</time>
  <span class="blog-post-author">ADBC Drivers Contributors</span>
</p>

An alpha release of a new ADBC driver for [Apache Cassandra](https://cassandra.apache.org/) is available through [dbc](https://docs.columnar.tech/dbc/). Install version 0.1.0-alpha.1 with:

```
dbc install --pre cassandra
```

The driver supports query execution, bind parameters, bulk ingestion (create, append, create-or-append, and replace modes), table schema discovery, and prepared statements. It has been tested with Apache Cassandra 5.0 and DataStax Enterprise 6.9. Documentation can be found at [adbc-drivers.org](https://adbc-drivers.org/drivers/cassandra/). This is a preview release, and more features are actively being developed, so stay tuned.

The driver was developed by the ADBC Driver Foundry, is implemented in Go, and is built on the [Apache Cassandra GoCQL driver](https://github.com/apache/cassandra-gocql-driver). It supports authentication, multiple contact points, configurable consistency and paging, and TLS connections, including custom CA certificates and mutual TLS.

To get started, provide a connection URI with a `cassandra://` scheme:

```
cassandra://host:9042/keyspace
```

The driver can then be used like any other driver. For example, load it in Python with `adbc-driver-manager`:

```python
from adbc_driver_manager import dbapi

with (
    dbapi.connect(
        driver="cassandra",
        db_kwargs={"uri": "cassandra://localhost:9042/my_keyspace"},
    ) as con,
    con.cursor() as cursor,
):
    cursor.execute("SELECT * FROM my_table")
    table = cursor.fetch_arrow_table()
```

Bug reports and feature requests are welcome through [GitHub Issues in the `cassandra` repository](https://github.com/adbc-drivers/cassandra/issues) in the ADBC Driver Foundry. You can also start a [Discussion](https://github.com/orgs/adbc-drivers/discussions) on GitHub or join the [Columnar Community Slack](https://join.slack.com/t/columnar-community/shared_invite/zt-3gt5cb69i-KRjJj~mjUZv5doVmpcVa4w).
