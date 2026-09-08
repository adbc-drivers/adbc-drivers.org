---
# Copyright (c) 2026 ADBC Drivers Contributors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
{}
---

# Build System

:::{workinprogress}
:::

The Driver Foundry provides a common build wrapper that invokes the underlying build system, configures things to meet our [requirements](./shared-library-requirements.md) and performs various post-build checks against those requirements. While not required for driver projects, it is highly recommended for building the final binary to be distributed.

## Usage

Essentially:

1. Create a configuration file describing the driver build.
2. Run `pixi run make` (with various flags) to build the driver itself.

### Configuration

Create an `adbc-make.toml` file in the root of the driver. (For example, at the root of the repository, or in the `go/` or `rust/` subdirectory for multi-project driver repositories.)

The minimal configuration looks like this for Go:

```toml
driver = "myawesomedriver"

[lang]
lang = "go"
```

Or for Rust:

```toml
driver = "myawesomedriver"

[lang]
lang = "rust"
```

### Building

Just run `pixi run make` from the root of the driver. The driver will be built to `build/libadbc_driver_myawesomedriver.so` (or whatever the appropriate extension for the platform is).
