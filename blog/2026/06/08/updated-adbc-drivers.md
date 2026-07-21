---
blogpost: true
date: 2026-06-08
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

# Updated ADBC drivers for Apache DataFusion, Exasol, and Trino

<p class="blog-post-meta">
  <time datetime="2026-06-08">June 08, 2026</time>
  <span class="blog-post-author">ADBC Drivers Contributors</span>
</p>

Today the ADBC Drivers Contributors released updated drivers for Apache DataFusion, Exasol, and Trino, available immediately via [dbc](https://docs.columnar.tech/dbc/). To update, just `dbc install [datafusion|exasol|trino]` to get the latest version.

## Updated Drivers

**[Apache DataFusion driver](https://github.com/adbc-drivers/datafusion) version [0.25.0](https://adbc-drivers.org/drivers/datafusion/v0.25.0)**

- Enable direct querying of HTTP/S3/etc. URIs and local files and directories in the same way that datafusion-cli does. Example:

  ```sql
  SELECT `Breed Name`, `Lifespan`
    FROM 'https://hyperparam-public.s3.amazonaws.com/bunnies.parquet'
    ORDER BY `Lifespan` DESC
    LIMIT 5;
  ```

**[Exasol driver](https://github.com/exasol-labs/exarrow-rs) version [0.12.6](https://adbc-drivers.org/drivers/exasol/v0.12.6)**

- Update dependencies with security advisories
- Various bug fixes

**[Trino driver](https://github.com/adbc-drivers/trino) version [0.4.0](https://adbc-drivers.org/drivers/trino/v0.4.0)**

- Add `trino.statement.last_query_id` option to retrieve the query ID
- Support GetStatistics and a target catalog/schema for bulk ingest

To learn more about how to use the drivers, check out the [documentation](https://adbc-drivers.org/) and [quickstarts](https://github.com/columnar-tech/adbc-quickstarts).

Bug reports and feature requests are welcome at the repositories linked above. You can also start a [Discussion](https://github.com/orgs/adbc-drivers/discussions) on GitHub or join the [Columnar Community Slack](https://join.slack.com/t/columnar-community/shared_invite/zt-3gt5cb69i-KRjJj~mjUZv5doVmpcVa4w).
