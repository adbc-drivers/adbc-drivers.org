---
blogpost: true
date: 2026-04-03
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

# Preview of a new ADBC driver for SingleStore

<p class="blog-post-meta">
  <time datetime="2026-04-03">April 03, 2026</time>
  <span class="blog-post-author">ADBC Drivers Contributors</span>
</p>

A beta release of a new ADBC driver for [SingleStore](https://www.singlestore.com/) is now available via [dbc](https://docs.columnar.tech/dbc/). If you have [dbc 0.2.0](https://columnar.tech/blog/announcing-dbc-0.2.0) or newer installed, run `dbc install singlestore --pre` to try it out today.

The driver supports query execution, bulk ingestion (create, append, and replace modes), catalog metadata retrieval, prepared statements, and transactions. Documentation can be found at [adbc-drivers.org](https://adbc-drivers.org/drivers/singlestore/). This is a beta release, and more features are actively being developed, so stay tuned.

The driver was developed by SingleStore, is implemented in Go, and uses the MySQL wire protocol to connect. To get started, provide a connection URI using the [Go MySQL Driver DSN format](https://pkg.go.dev/github.com/go-sql-driver/mysql#readme-dsn-data-source-name) with a `singlestore://` scheme:

```
singlestore://user:password@tcp(host:3306)/database
```

Bulk ingestion uses `LOAD DATA LOCAL INFILE` under the hood. The driver includes comprehensive type mappings between SingleStore and Arrow types, covering integers, floating-point numbers, decimals, temporal types (DATE, DATETIME, TIME, TIMESTAMP), strings, binary data, and JSON.

The ADBC Quickstarts have [runnable examples demonstrating the SingleStore driver](https://github.com/columnar-tech/adbc-quickstarts/tree/by-database/singlestore) in C++, Go, Java, Python, R, and Rust.

Please submit bug reports and feature requests directly to the [`singlestore-adbc-connector` repository](https://github.com/singlestore-labs/singlestore-adbc-connector). You can also start a [Discussion](https://github.com/orgs/adbc-drivers/discussions) on GitHub or join the [Columnar Community Slack](https://join.slack.com/t/columnar-community/shared_invite/zt-3gt5cb69i-KRjJj~mjUZv5doVmpcVa4w).
