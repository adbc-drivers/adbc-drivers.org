---
blogpost: true
date: 2026-09-15
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

# Preview of a new ADBC driver for Apache Druid

<p class="blog-post-meta">
  <time datetime="2026-09-15">September 15, 2026</time>
  <span class="blog-post-author">ADBC Drivers Contributors</span>
</p>

An alpha release of a new ADBC driver for [Apache Druid](https://druid.apache.org/) is available through [dbc](https://docs.columnar.tech/dbc/). Install version 0.1.0-alpha.1 with:

```console
$ dbc install --pre druid
```

The driver supports SQL query execution, bind parameters, and table schema discovery. It has been tested with Apache Druid 37.0.0. See the [ADBC Driver for Apache Druid documentation](/drivers/druid/index.md). This is a preview release, and more features are actively being developed, so stay tuned.

The driver was developed by the ADBC Driver Foundry and is implemented in Rust. It uses the Apache Druid SQL API and supports HTTP and HTTPS connections, HTTP Basic authentication, custom CA certificates, and Druid SQL query-context parameters.

To get started, provide a connection URI with a `druid://` scheme:

```
druid://localhost:8888?tls=false
```

The driver can then be used like any other driver. For example, load it in Python with `adbc-driver-manager`:

```python
from adbc_driver_manager import dbapi

connection = dbapi.connect(
    driver="druid",
    db_kwargs={"uri": "druid://localhost:8888?tls=false"},
)
cursor = connection.cursor()
cursor.execute("SELECT channel, page, added FROM wikipedia LIMIT 10")
table = cursor.fetch_arrow_table()
```

Bug reports and feature requests are welcome through [GitHub Issues in the `druid` repository](https://github.com/adbc-drivers/druid/issues) in the ADBC Driver Foundry. You can also start a [Discussion](https://github.com/orgs/adbc-drivers/discussions) on GitHub or join the [Columnar Community Slack](https://join.slack.com/t/columnar-community/shared_invite/zt-3gt5cb69i-KRjJj~mjUZv5doVmpcVa4w).
