/*
 * Copyright (c) 2026 ADBC Drivers Contributors
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *         http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

/*
 * Traffic is also proxied through Cloudflare, where Redirect Rules perform
 * these redirects first. Keep this client-side redirect as a backup / second
 * line of defense while preserving the full URL.
 */
(() => {
  if (window.location.hostname !== "docs.adbc-drivers.org") {
    return;
  }

  const destination = new URL(window.location.href);
  destination.protocol = "https:";
  destination.hostname = "adbc-drivers.org";
  destination.port = "";
  window.location.replace(destination.toString());
})();
