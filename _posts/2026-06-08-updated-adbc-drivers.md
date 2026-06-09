---
layout: blog
title: Updated ADBC drivers for ClickHouse and SQL Server
author: ADBC Drivers Contributors
---

Today the ADBC Drivers Contributors released updated drivers for Apache DataFusion, Exasol, and Trino, available immediately via [dbc](https://docs.columnar.tech/dbc/). To update, just `dbc install [datafusion|exasol|trino]` to get the latest version.

## Updated Drivers

**[Apache DataFusion driver](https://github.com/adbc-drivers/datafusion) version [0.25.0](https://docs.adbc-drivers.org/drivers/datafusion/v0.25.0)**

- Enable direct querying of HTTP/S3/etc. URIs in the same way that datafusion-cli does. Example:

  ```sql
  SELECT `Breed Name`, `Lifespan`
    FROM 'https://hyperparam-public.s3.amazonaws.com/bunnies.parquet'
    ORDER BY `Lifespan` DESC
    LIMIT 5;
  ```

**[Exasol driver](https://github.com/exasol-labs/exarrow-rs) version [0.12.6](https://docs.adbc-drivers.org/drivers/exasol/v0.12.6)**

- Update dependencies with security advisories
- Various bug fixes

**[Trino driver](https://github.com/adbc-drivers/trino) version [0.4.0](https://docs.adbc-drivers.org/drivers/trino/v0.4.0)**

- Add `trino.statement.last_query_id` option to retrieve the query ID
- Support GetStatistics and a target catalog/schema for bulk ingest

To learn more about how to use the drivers, check out the [documentation](https://docs.adbc-drivers.org/) and [quickstarts](https://github.com/columnar-tech/adbc-quickstarts).

Bug reports and feature requests are welcome at the repositories linked above. You can also start a [Discussion](https://github.com/orgs/adbc-drivers/discussions) on GitHub or join the [Columnar Community Slack](https://join.slack.com/t/columnar-community/shared_invite/zt-3gt5cb69i-KRjJj~mjUZv5doVmpcVa4w).
