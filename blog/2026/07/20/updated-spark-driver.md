---
blogpost: true
date: 2026-07-20
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

# Updated ADBC driver for Apache Spark

<p class="blog-post-meta">
  <time datetime="2026-07-20">July 20, 2026</time>
  <span class="blog-post-author">ADBC Drivers Contributors</span>
</p>

Today the ADBC Drivers Contributors released an updated driver for Apache Spark, version 0.1.0, available immediately via [dbc](https://docs.columnar.tech/dbc/). To update, just `dbc install spark` to get the latest version — no `--pre` flag needed, as this is the driver's first release out of alpha/beta.

Version 0.1.0 implements GetTableSchema and adds an option to set the catalog on initial connect, along with other bug fixes.

For more details, see the [full changelog](https://adbc-drivers.org/drivers/spark/changelog#v0-1-0-2026-07-20). To learn more about how to use the driver, check out the [documentation](https://adbc-drivers.org/drivers/spark/v0.1.0) and [quickstarts](https://github.com/columnar-tech/adbc-quickstarts).

Bug reports and feature requests are welcome through GitHub Issues in the [`adbc-drivers/spark` repository](https://github.com/adbc-drivers/spark). You can also start a [Discussion](https://github.com/orgs/adbc-drivers/discussions) on GitHub or join the [Columnar Community Slack](https://join.slack.com/t/columnar-community/shared_invite/zt-3gt5cb69i-KRjJj~mjUZv5doVmpcVa4w).
