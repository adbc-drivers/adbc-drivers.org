---
layout: blog
title: Faster ADBC drivers for BigQuery, MySQL, SQL Server, and Trino
author: ADBC Drivers Contributors
---

Today the ADBC Drivers Contributors released updated drivers for four database systems, available immediately via [dbc](https://docs.columnar.tech/dbc/). To update, just `dbc install <driver>` to get the latest version.

## Updated Drivers

The main highlight for all drivers is improved performance.

### Google BigQuery driver version 1.11.0

- Improved query performance by identifying and patching an issue in the Google BigQuery SDK for Go. [#102](https://github.com/adbc-drivers/bigquery/pull/102)
- Added experimental support for bulk ingest via the Storage Write API, instead of by uploading Parquet files. This is still a work in progress and is not recommended for production use. [#105](https://github.com/adbc-drivers/bigquery/pull/105)

### MySQL driver version 0.3.0

- Improved bulk ingest performance. [#66](https://github.com/adbc-drivers/mysql/pull/66)

### Microsoft SQL Server driver version 1.3.0

- Improved query performance by identifying and submitting fixes for [microsoft/go-mssqldb](https://github.com/microsoft/go-mssqldb).

### Trino driver version 0.3.0

- Improved bulk ingest performance. [#58](https://github.com/adbc-drivers/trino/pull/58)

## Benchmarks

Query benchmarks measure the time to retrieve a PyArrow Table, while ingest benchmarks measure the time to write a PyArrow Table.  The benchmark harness in all cases uses Python.

### Querying Data

| Database | Data Size | ADBC Before (s) | ADBC After (s) | Competitor (s) | Relative Time[^speedup] |
| :-- | :-- | --: | --: | --: | --: |
| BigQuery | 6 million rows | 95.2 ± 2.34 | **31.0 ± 2.1** | 56.4 ± 1.3[^bigquery] | 0.55x |
| Microsoft SQL Server | 1.2 million rows | 9.6 ± 0.1 | 3.3 ± 0.0 | **3.0 ± 0.2**[^mssql] | 1.1x |

[^bigquery]: python-bigquery-sqlalchemy with Storage Read API enabled
[^mssql]: turbodbc 5.1.2 + msodbcsql 18.6.1.1-1
[^speedup]: Lower is better.

### Ingesting Data

| Database | Data Size | ADBC Before (s) | ADBC After (s) | Competitor (s) | Relative Time[^speedup] |
| :-- | :-- | --: | --: | --: | --: |
| MySQL | 600k rows | 467.8 ± 17.9 | **6.7 ± 0.3** | 13.1 ± 0.7[^mysql] | 0.51x |
| Trino | 60k rows | 1962.8 ± 182.2 | **52.2 ± 8.2** | 2061.8 ± 15.1[^trino] | 0.03x |

[^mysql]: mysql-connector-python using DuckDB to convert Arrow data to Python objects; using PyArrow `Table.to_pylist` instead, timing was 15.31 ± 0.59s
[^trino]: trino-python-client
