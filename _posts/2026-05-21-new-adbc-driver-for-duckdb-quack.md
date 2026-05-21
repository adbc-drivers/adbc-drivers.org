---
layout: blog
title: Preview of a new ADBC driver for DuckDB Quack
author: ADBC Drivers Contributors
---

A beta release of a new ADBC driver for [DuckDB's Quack protocol]() is now available via [dbc](https://docs.columnar.tech/dbc/). Run `dbc install quack --pre` to try it out today.

The driver supports query execution, bulk ingestion (create, append, and replace modes), catalog metadata retrieval, prepared statements, and transactions. Documentation can be found at [docs.adbc-drivers.org](https://docs.adbc-drivers.org/drivers/quack/). This is a preview release, and more features are actively being developed, so stay tuned.

The driver was developed by the ADBC Driver Foundry, is implemented in C++, and wraps DuckDB itself underneath for full compatibility. See our [blog post]() for more details on how we built the driver.

To get started, provide a connection URI with a `quack://` scheme:

```
quack://host:port/?token=my-secret
```

The driver can then be used like any other driver. For example, load it in Python with `adbc-driver-manager`:

```
from adbc_driver_manager import dbapi

with (
    dbapi.connect("quack://localhost:9494/?token=quack-secret") as con,
    con.cursor() as cursor,
):
    cursor.execute("FROM range(0, 100, 2)")
    table = cursor.fetch_arrow_table()
```

Bug reports and feature requests are welcome through [GitHub Issues in the `quack` repository](https://github.com/adbc-drivers/quack/issues) in the ADBC Driver Foundry. You can also start a [Discussion](https://github.com/orgs/adbc-drivers/discussions) on GitHub or join the [Columnar Community Slack](https://join.slack.com/t/columnar-community/shared_invite/zt-3gt5cb69i-KRjJj~mjUZv5doVmpcVa4w).
