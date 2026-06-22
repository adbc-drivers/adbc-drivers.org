---
layout: blog
title: Updated ADBC drivers for BigQuery and Oracle Database
author: ADBC Drivers Contributors
---

Today the ADBC Drivers Contributors released updated drivers for BigQuery and Oracle Database, available immediately via [dbc](https://docs.columnar.tech/dbc/). To update, just `dbc install [bigquery|oracle]` to get the latest version[^trial].

## Updated Drivers

**[BigQuery driver](https://github.com/adbc-drivers/bigquery) version [1.12.0](https://docs.adbc-drivers.org/drivers/bigquery/v1.12.0)**

- Make option names more consistent (allow `bigquery.foo` in addition to `adbc.bigquery.sql.foo`)
- Add query statistics to the schema metadata of the result
- Implement GetStatistics
- Add the SRID to returned GeoArrow metadata
- Allow binding Arrow time[ns] values by truncating
- Auto-detect the credential type from JSON credentials
- Improve error handling around authentication
- Handle dry-run queries properly instead of erroring

**Oracle Database driver version [0.6.0](https://docs.columnar.tech/drivers/oracle/v0.6.0)**

{: .admonition.note }
The default execution mode will become `batch` in the next minor version (v0.7.0) and the `row` option will be removed the following minor version (v0.8.0).

- Support querying/bulk ingesting interval types
- Support retrieving the value of OUT bind parameters as columns of the result set
- Add an option to control the Arrow type of NUMBER types without a precision/scale
- Support querying and ingesting SDO_GEOMETRY columns as GeoArrow extension types
- Retrieve the result of `DBMS_SQL.RETURN_RESULT`
- Allow setting various options on initial connection

To learn more about how to use the drivers, check out the [documentation](https://docs.adbc-drivers.org/) and [quickstarts](https://github.com/columnar-tech/adbc-quickstarts).

Bug reports and feature requests are welcome at the repositories linked above. You can also start a [Discussion](https://github.com/orgs/adbc-drivers/discussions) on GitHub or join the [Columnar Community Slack](https://join.slack.com/t/columnar-community/shared_invite/zt-3gt5cb69i-KRjJj~mjUZv5doVmpcVa4w).

[^trial]: For the Oracle Database driver, you will need to log in with `dbc auth login` first.
