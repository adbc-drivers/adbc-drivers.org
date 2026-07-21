---
blogpost: true
date: 2026-05-27
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

# New ADBC driver for Apache DataFusion

<p class="blog-post-meta">
  <time datetime="2026-05-27">May 27, 2026</time>
  <span class="blog-post-author">ADBC Drivers Contributors</span>
</p>

A new ADBC driver for [Apache DataFusion](https://datafusion.apache.org) is now available via [dbc](https://docs.columnar.tech/dbc/). Run `dbc install datafusion` to try it out today.

The driver supports query execution, bulk ingestion (create, append, and replace modes), catalog metadata retrieval, and prepared statements. Documentation can be found at [adbc-drivers.org](https://adbc-drivers.org/drivers/datafusion/). The driver was developed in Rust by the ADBC Driver Foundry based on the driver originally available from `apache/arrow-adbc`, but has been extended with new features and bug fixes.

As DataFusion is embedded, you can use the driver without any need for a connection string. For example, load it in Python with `adbc-driver-manager`:

```python
from adbc_driver_manager import dbapi

with (
    dbapi.connect("datafusion") as con,
    con.cursor() as cursor,
):
    cursor.execute("SELECT 42")
    table = cursor.fetch_arrow_table()
```

Bug reports and feature requests are welcome through [GitHub Issues in the `datafusion` repository](https://github.com/adbc-drivers/datafusion/issues) in the ADBC Driver Foundry. You can also start a [Discussion](https://github.com/orgs/adbc-drivers/discussions) on GitHub or join the [Columnar Community Slack](https://join.slack.com/t/columnar-community/shared_invite/zt-3gt5cb69i-KRjJj~mjUZv5doVmpcVa4w).
