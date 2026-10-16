---
blogpost: true
date: 2026-10-16
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

# Updated ADBC drivers for Apache Cassandra, Apache Spark, Amazon Redshift, BigQuery, Databricks, Microsoft SQL Server, MySQL/MariaDB, Presto, Snowflake, and Trino

The ADBC Drivers Contributors have released updates to drivers for Apache Cassandra, Apache Spark, Amazon Redshift, BigQuery, Databricks, Microsoft SQL Server, MySQL/MariaDB, Presto, Snowflake, and Trino. All are available now via [dbc](https://docs.columnar.tech/dbc/).

To update, run `dbc install <driver>`. For the Cassandra and Presto alpha releases, use `dbc install --pre <driver>`.

## Updated Drivers

**[ADBC Driver for Apache Cassandra](https://github.com/adbc-drivers/cassandra) version [0.1.0-alpha.3](/drivers/cassandra/v0.1.0-alpha.3.md)**

- Update dependencies to pick up CVE fixes

**[ADBC Driver for Apache Spark](https://github.com/adbc-drivers/spark) version [0.2.2](/drivers/spark/v0.2.2.md)**

- Map Spark Connect gRPC errors to the correct ADBC status codes
- Update dependencies to pick up CVE fixes

**[ADBC Driver for Amazon Redshift](https://github.com/adbc-drivers/redshift) version [1.8.0](/drivers/redshift/v1.8.0.md)**

- Include temporary tables in `GetObjects` results
- Support fetching a new IdP access token for each connection using a configurable token endpoint
- Fix IdP token authentication failing with a "failed to authenticate" error
- Update dependencies to pick up CVE fixes

**[BigQuery ADBC driver](https://github.com/adbc-drivers/bigquery) version [1.14.0](/drivers/bigquery/v1.14.0.md)**

- Add the `bigquery.user_agent` option to customize the user agent
- Add experimental support for optional job creation with Arrow result format
- Return additional BigQuery table metadata
- Map REST API 403 access denials to the UNAUTHORIZED status code
- Correct Arrow extension metadata for `ARRAY<GEOGRAPHY>` results
- Refresh impersonated credentials automatically when `bigquery.impersonate.lifetime` is unset
- Skip tables that return 404 errors in `GetObjects`
- Update dependencies to pick up CVE fixes

**[ADBC Driver for Databricks](https://github.com/adbc-drivers/databricks) version [0.2.0](/drivers/databricks/v0.2.0.md)**

- Support named query parameters
- Support decimal data types
- Update dependencies to pick up CVE fixes

**[ADBC Driver for Microsoft SQL Server](https://github.com/adbc-drivers/mssql) version [1.7.0](/drivers/mssql/v1.7.0.md)**

- Add the `mssql.query.datetimeoffset_type` option to return DATETIMEOFFSET as `arrow.timestamp_with_offset`, preserving the original UTC offset
- Add the `mssql.query.datetimeoffset_precision` option to choose between preserving the full date range and fractional-second precision
- Support binding and ingesting `arrow.timestamp_with_offset` as DATETIMEOFFSET (Fabric Data Warehouse does not support DATETIMEOFFSET columns)
- Restore support for querying DATETIMEOFFSET as `timestamp[us, tz=UTC]` by default
- Correct UUID byte order when reading, binding, and ingesting UNIQUEIDENTIFIER values
- Fix `GetObjects` metadata queries for other catalogs and avoid errors for inaccessible catalogs
- Honor `mssql.ingest.method` when set on a connection
- Update dependencies to pick up CVE fixes

**[ADBC Driver for MySQL/MariaDB](https://github.com/adbc-drivers/mysql) version [0.7.0](/drivers/mysql/v0.7.0.md)**

- Support reading `BIGINT UNSIGNED` values above the signed 64-bit maximum through prepared statements
- Accept the target database via the catalog option for bulk ingestion
- Update dependencies to pick up CVE fixes

**[ADBC Driver for Presto](https://github.com/adbc-drivers/presto) version [0.1.0-alpha.3](/drivers/presto/v0.1.0-alpha.3.md)**

- Default `presto://` connections to TLS
- Update dependencies to pick up CVE fixes

**[ADBC Driver for Snowflake](https://github.com/adbc-drivers/snowflake) version [1.15.0](/drivers/snowflake/v1.15.0.md)**

- Add the `adbc.connection.get_objects.match_exactly` option to disable wildcard matching in `GetObjects` filters
- Add the `adbc.snowflake.sql.client_option.max_retry_count` option to control the maximum number of retries per HTTP request
- Handle backslashes correctly in `GetObjects` filters
- Limit prefetching based on the number of unconsumed result streams
- Update dependencies to pick up CVE fixes

**[ADBC Driver for Trino](https://github.com/adbc-drivers/trino) versions [0.6.0](/drivers/trino/v0.6.0.md) and [0.6.1](/drivers/trino/v0.6.1.md)**

- Support transactions
- Update dependencies to pick up CVE fixes
- Bundle timezone data in shared libraries

To learn more about any of these drivers, check out the [documentation](/index.md) and [quickstarts](https://github.com/columnar-tech/adbc-quickstarts).

Bug reports and feature requests are welcome at the repositories linked above. You can also start a [Discussion](https://github.com/orgs/adbc-drivers/discussions) on GitHub or join the [Columnar Community Slack](https://join.slack.com/t/columnar-community/shared_invite/zt-3gt5cb69i-KRjJj~mjUZv5doVmpcVa4w).
