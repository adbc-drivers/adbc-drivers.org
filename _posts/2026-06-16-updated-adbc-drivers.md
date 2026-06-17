---
layout: blog
title: Updated ADBC drivers for Exasol and Snowflake
author: ADBC Drivers Contributors
---

Today the ADBC Drivers Contributors released updated drivers for Exasol and Snowflake, available immediately via [dbc](https://docs.columnar.tech/dbc/). To update, just `dbc install [exasol|snowflake]` to get the latest version.

## Updated Drivers

**[Exasol driver](https://github.com/exasol-labs/exarrow-rs) version [0.12.7](https://docs.adbc-drivers.org/drivers/exasol/v0.12.7)**

- Fix empty result sets not carrying the expected schema

**[Snowflake driver](https://github.com/adbc-drivers/snowflake) version [1.11.0](https://docs.adbc-drivers.org/drivers/snowflake/v1.11.0)**

- Convert between GeoArrow types and GEOMETRY/GEOGRAPHY for both querying and ingest
- Support more Arrow types in bulk ingest as well as specifying the target catalog/schema and compression codec for Parquet files
- Implement GetStatistics
- Support queries that invoke stored procedures via `CALL`
- Improve GetObjects performance
- Various bug fixes

To learn more about how to use the drivers, check out the [documentation](https://docs.adbc-drivers.org/) and [quickstarts](https://github.com/columnar-tech/adbc-quickstarts).

Bug reports and feature requests are welcome at the repositories linked above. You can also start a [Discussion](https://github.com/orgs/adbc-drivers/discussions) on GitHub or join the [Columnar Community Slack](https://join.slack.com/t/columnar-community/shared_invite/zt-3gt5cb69i-KRjJj~mjUZv5doVmpcVa4w).
