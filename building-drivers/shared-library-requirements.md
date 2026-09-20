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

# Shared Library Requirements

Driver shared libraries distributed by the Driver Foundry should meet these requirements:

**The driver must be statically linked.**

Exceptions:
- Platform libraries (glibc, MSVC redistributables, macOS system frameworks)
- Third party dependencies that we cannot redistribute (this should be a last resort)

**The driver must export `AdbcDriverInit`.**

This is the fallback symbol used by driver managers.

**The driver must export `AdbcDriverFoobarInit`.**

This is the primary entrypoint used by driver managers. The name of the driver library itself should be `libadbc_driver_foobar.{dll,so,dylib}` in this case. There should be no intermediate capitalization (e.g. it should be `AdbcDriverBigqueryInit` and not `AdbcDriverBigQueryInit`), because the name of the symbol is [derived mechanically from the filename](https://github.com/apache/arrow-adbc/blob/86667c4d7fea767b7aeceb5639147cc6c4861f54/c/driver_manager/adbc_driver_manager_driver_loading.cc#L780-L841).

**The filename should be `libadbc_driver_foobar.{dll,so,dylib}`.**

See the above point. This is not strictly required, but a convention that our libraries follow.

**The driver should not export other symbols that do not begin with `Adbc`.**

This is to minimize the chance of conflicts with other shared libraries. (Driver managers do not generally use mitigations like `RTLD_DEEPBIND` due to limited support.)

**The driver should support older operating system versions.**

- Linux: support the equivalent of [`manylinux2014`](https://github.com/pypa/manylinux#manylinux2014-centos-7-based-glibc-217), i.e. glibc 2.17/CentOS 7.
  - It is permissible to go up to [`manylinux2_28`](https://github.com/pypa/manylinux#manylinux_2_28-almalinux-8-based), i.e. glibc 2.28, if needed for your toolchain.
- macOS: support macOS 13 or newer.
  - This is derived from Go's support: the latest release, Go 1.27, requires macOS 13.
- Windows: we currently don't have a well-defined definition of our Windows target.
