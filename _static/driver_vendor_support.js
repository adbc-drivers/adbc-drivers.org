/* Copyright (c) 2026 ADBC Drivers Contributors
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

(() => {
    const badges = document.querySelectorAll(".driver-vendor-support");

    for (const badge of badges) {
        const trigger = badge.querySelector(".driver-vendor-support-badge");
        const tooltip = badge.querySelector(".driver-vendor-support-tooltip");

        const position = () => {
            tooltip.style.left = "0px";
            const rect = tooltip.getBoundingClientRect();
            const offset = Math.max(
                16 - rect.left,
                Math.min(0, window.innerWidth - 16 - rect.right),
            );
            tooltip.style.left = `${offset}px`;
        };
        const show = () => {
            badge.classList.remove("is-dismissed");
            position();
        };
        const reset = () => badge.classList.remove("is-open", "is-dismissed");

        badge.addEventListener("mouseenter", show);
        badge.addEventListener("focusin", show);
        badge.addEventListener("mouseleave", reset);
        badge.addEventListener("focusout", (event) => {
            if (!badge.contains(event.relatedTarget)) reset();
        });
        trigger.addEventListener("click", () => {
            const open = !badge.classList.contains("is-open");
            show();
            badge.classList.toggle("is-open", open);
            badge.classList.toggle("is-dismissed", !open);
        });
        window.addEventListener("resize", position);
    }

    document.addEventListener("keydown", (event) => {
        if (event.key !== "Escape") return;
        for (const badge of badges) {
            if (badge.contains(document.activeElement)) {
                badge.querySelector(".driver-vendor-support-badge").focus();
            }
            badge.classList.remove("is-open");
            badge.classList.add("is-dismissed");
        }
    });
    document.addEventListener("pointerdown", (event) => {
        for (const badge of badges) {
            if (!badge.contains(event.target)) {
                badge.classList.remove("is-open");
                badge.classList.add("is-dismissed");
            }
        }
    });
})();
