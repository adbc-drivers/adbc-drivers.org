---
blogpost: true
date: 2026-09-02
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

# Updated ADBC Driver for Arrow Flight SQL

<p class="blog-post-meta">
  <time datetime="2026-09-02">September 2, 2026</time>
  <span class="blog-post-author">ADBC Drivers Contributors</span>
</p>

Version 1.12.2 of the ADBC driver for Apache Arrow Flight SQL is now in the [ADBC driver registry](https://dbc-cdn.columnar.tech) and installable immediately via [dbc](https://docs.columnar.tech/dbc/). To install or update, just run:

```console
$ dbc install flightsql
```


Version 1.12.2 bumps gRPC to address security vulnerabilities in the driver's dependencies. There are no other changes from version 1.12.1.

As with version 1.12.1, this release is a bit different from the driver updates we usually announce here. The Flight SQL driver is developed upstream in the [Apache Arrow ADBC](https://github.com/apache/arrow-adbc) repository rather than in the ADBC Driver Foundry, and the versions of it in the registry up through 1.12.0 were built from official Apache Software Foundation releases. Updates to it are normally announced on the [Apache Arrow blog](https://arrow.apache.org/blog/), not here. However, cutting a full upstream release just for a dependency patch would have meant a release candidate and vote covering every ADBC library and driver, including those with no changes. So to reduce the burden on the core ADBC maintainers and to get this patch release out with no delay, we implemented the fix on a branch based on version 1.12.0 and built versions 1.12.1 and 1.12.2 for the registry. Versions 1.12.1 and 1.12.2 are not official Apache Software Foundation releases, and are available only through the ADBC driver registry.[^versioning] The same fix is also in the upstream `main` branch, and the next official ADBC libraries release will include it.

To learn more about how to use the driver, check out the [documentation](https://arrow.apache.org/adbc/current/driver/flight_sql.html) and [quickstarts](https://github.com/columnar-tech/adbc-quickstarts).

Bug reports and feature requests for this driver are welcome through GitHub Issues in the [`apache/arrow-adbc` repository](https://github.com/apache/arrow-adbc). You can also start a [Discussion](https://github.com/orgs/adbc-drivers/discussions) on GitHub or join the [Columnar Community Slack](https://join.slack.com/t/columnar-community/shared_invite/zt-3gt5cb69i-KRjJj~mjUZv5doVmpcVa4w).

[^versioning]: Publishing this build downstream means the 1.12.1 and 1.12.2 version numbers are now taken outside of the upstream release sequence. If an official patch release for the 1.12 minor release happens later on, we will work with the ADBC maintainers on how best to handle the overlap.
