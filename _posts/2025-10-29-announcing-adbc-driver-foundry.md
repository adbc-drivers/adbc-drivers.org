---
layout: blog
title: Announcing the ADBC Driver Foundry
author: ADBC Drivers Contributors
---

ADBC (Arrow Database Connectivity) is at an inflection point. Launched in 2022 as a subproject of Apache Arrow, ADBC is a modern data connectivity standard built to accelerate and simplify data access for analytics applications. Leading companies including Databricks, dbt Labs, Microsoft, and Snowflake are building with ADBC.

Today, the project is a bustling construction site. The foundations—ADBC’s core specifications and libraries—have solidified. The focus has shifted to building the superstructure: the drivers that connect ADBC to a wide array of databases, query engines, and data platforms. But as driver development has scaled up, there has been little scaffolding to support contributors. Driver work has funneled through the same central repository that houses ADBC’s core components, straining the small group of Apache Arrow maintainers who can review and merge contributions. The result has been slow reviews, mounting frustration, and a mismatch between the centralized privilege model of Apache projects and the inherently federated nature of driver development.

To give current and future driver developers the scaffolding they need, today we’re launching the ADBC Driver Foundry, an open source hub for federated driver development hosted at [github.com/adbc-drivers](http://github.com/adbc-drivers). This effort brings together contributors from [Columnar](https://columnar.tech), [Databricks](https://www.databricks.com), [dbt Labs](https://www.getdbt.com), [Improving](https://www.improving.com), [Microsoft](https://www.microsoft.com/), [Snowflake](https://www.snowflake.com/), and the broader [Apache Arrow](https://arrow.apache.org) developer community. The Foundry strikes a balance between autonomy and shared support, providing a scalable structure that empowers contributors while ensuring consistency across the ecosystem.

For driver developers, the Foundry offers per-project repositories with independently managed commit privileges, along with templates and guides for building new drivers. It also provides shared resources for testing, validation, benchmarking, packaging, distribution, and documentation.

For driver users and downstream developers, nothing changes immediately. In the coming months, as drivers begin to be distributed from the Foundry, we’ll update some package names and class names. Stay tuned for more details in future posts.

With strong foundations—and now strong scaffolding—ADBC is ready for its next stage of growth. To learn more or get involved, visit [adbc-drivers.org](https://adbc-drivers.org) or email us at [hello@adbc-drivers.org](mailto:hello@adbc-drivers.org).
