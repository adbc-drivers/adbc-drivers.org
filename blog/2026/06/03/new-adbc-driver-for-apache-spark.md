---
blogpost: true
date: 2026-06-03
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

# Preview of a new ADBC driver for Apache Spark

<p class="blog-post-meta">
  <time datetime="2026-06-03">June 03, 2026</time>
  <span class="blog-post-author">ADBC Drivers Contributors</span>
</p>

A beta release of a new ADBC driver for [Apache Spark](https://spark.apache.org) is now available via [dbc](https://docs.columnar.tech/dbc/). Run `dbc install spark --pre` to try it out today.

The driver supports query execution, bulk ingestion, and catalog metadata retrieval. It can connect via the HiveServer2 Thrift protocol (either over TCP, or HTTP/HTTPS), Spark Connect, or Apache Livy. Documentation can be found at [adbc-drivers.org](https://adbc-drivers.org/drivers/spark/). This is a preview release, and more features are actively being developed, so stay tuned.

The driver was developed by the ADBC Driver Foundry and is implemented in Go.

To get started, provide a connection URI with a `spark://` scheme:

```
spark://host:port/?api=connect&auth=token
```

The driver can then be used like any other driver. For example, load it in Python with `adbc-driver-manager`:

```
from adbc_driver_manager import dbapi

with (
    dbapi.connect("spark://localhost:15002?auth_type=none&api=connect") as con,
    con.cursor() as cursor,
):
    cursor.execute("SELECT * FROM mytable")
    table = cursor.fetch_arrow_table()
```

Bug reports and feature requests are welcome through [GitHub Issues in the `spark` repository](https://github.com/adbc-drivers/spark/issues) in the ADBC Driver Foundry. You can also start a [Discussion](https://github.com/orgs/adbc-drivers/discussions) on GitHub or join the [Columnar Community Slack](https://join.slack.com/t/columnar-community/shared_invite/zt-3gt5cb69i-KRjJj~mjUZv5doVmpcVa4w).
