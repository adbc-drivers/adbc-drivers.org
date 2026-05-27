---
layout: blog
title: New ADBC driver for Apache DataFusion
author: ADBC Drivers Contributors
---

A new ADBC driver for [Apache DataFusion](https://datafusion.apache.org) is now available via [dbc](https://docs.columnar.tech/dbc/). Run `dbc install datafusion` to try it out today.

The driver supports query execution, bulk ingestion (create, append, and replace modes), catalog metadata retrieval, and prepared statements. Documentation can be found at [docs.adbc-drivers.org](https://docs.adbc-drivers.org/drivers/datafusion/). The driver was developed in Rust by the ADBC Driver Foundry based on the driver originally available from `apache/arrow-adbc`, but has been extended with new features and bug fixes.

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
