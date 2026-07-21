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

/* The theme's sidebar templates bypass Sphinx's external-link translator. */
(() => {
  const selector = [
    '.md-sidebar--primary .md-nav__link[href^="http://"]',
    '.md-sidebar--primary .md-nav__link[href^="https://"]',
  ].join(", ");

  for (const link of document.querySelectorAll(selector)) {
    const destination = new URL(link.href, window.location.href);
    if (destination.origin === window.location.origin) {
      continue;
    }

    link.target = "_blank";
    link.rel = "noopener noreferrer";
  }
})();
