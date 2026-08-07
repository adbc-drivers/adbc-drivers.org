// Copyright (c) 2026 ADBC Drivers Contributors
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//         http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

(() => {
  "use strict";

  if (
    typeof HTMLDialogElement === "undefined" ||
    typeof HTMLDialogElement.prototype.showModal !== "function"
  ) {
    return;
  }

  const cache = new Map();
  let requestId = 0;
  let trigger = null;

  const dialog = document.createElement("dialog");
  dialog.className = "quickstart-modal md-typeset";

  const closeButton = document.createElement("button");
  closeButton.className = "quickstart-modal__close";
  closeButton.type = "button";
  closeButton.setAttribute("aria-label", "Close quickstart");
  closeButton.textContent = "\u00d7";

  const content = document.createElement("div");
  content.className = "quickstart-modal__content";
  dialog.append(closeButton, content);
  document.body.append(dialog);

  const loadFragment = (url) => {
    if (!cache.has(url)) {
      const pending = fetch(url, { credentials: "same-origin" })
        .then((response) => {
          if (!response.ok) {
            throw new Error(`Could not load quickstart: ${response.status}`);
          }
          return response.text();
        })
        .then((html) => {
          const page = new DOMParser().parseFromString(html, "text/html");
          const fragment = page.querySelector("[data-quickstart-modal-content]");
          if (!fragment) {
            throw new Error("Quickstart page has no modal content");
          }
          return fragment;
        })
        .catch((error) => {
          cache.delete(url);
          throw error;
        });
      cache.set(url, pending);
    }
    return cache.get(url);
  };

  const fallbackCopy = (text) => {
    const textarea = document.createElement("textarea");
    textarea.value = text;
    textarea.className = "quickstart-modal__copy-source";
    document.body.append(textarea);
    textarea.select();
    const copied = document.execCommand("copy");
    textarea.remove();
    if (!copied) {
      throw new Error("Could not copy quickstart source");
    }
  };

  const copySource = async (text) => {
    if (navigator.clipboard && window.isSecureContext) {
      await navigator.clipboard.writeText(text);
      return;
    }
    fallbackCopy(text);
  };

  const renderFragment = (fragment) => {
    const imported = document.importNode(fragment, true);
    const source = imported.querySelector("pre");
    if (!source) {
      throw new Error("Quickstart page has no source listing");
    }

    const actions = document.createElement("div");
    actions.className = "quickstart-modal__actions";
    const githubLink = imported.querySelector("p");
    if (githubLink) {
      actions.append(githubLink);
    }

    const copyButton = document.createElement("button");
    copyButton.className = "quickstart-modal__copy";
    copyButton.type = "button";
    copyButton.textContent = "Copy code";
    copyButton.addEventListener("click", async () => {
      try {
        await copySource(source.textContent);
        copyButton.textContent = "Copied";
      } catch (_error) {
        copyButton.textContent = "Copy failed";
      }
      window.setTimeout(() => {
        copyButton.textContent = "Copy code";
      }, 2000);
    });
    actions.append(copyButton);
    content.replaceChildren(actions, imported);
  };

  const closeDialog = (afterClose) => {
    if (!dialog.open || dialog.classList.contains("quickstart-modal--closing")) {
      return;
    }
    dialog.classList.remove("quickstart-modal--visible");
    dialog.classList.add("quickstart-modal--closing");
    const delay = window.matchMedia("(prefers-reduced-motion: reduce)").matches
      ? 0
      : 125;
    window.setTimeout(() => {
      dialog.close();
      if (afterClose) {
        afterClose();
      }
    }, delay);
  };

  closeButton.addEventListener("click", () => closeDialog());
  dialog.addEventListener("click", (event) => {
    if (event.target === dialog) {
      closeDialog();
    }
  });
  dialog.addEventListener("cancel", (event) => {
    event.preventDefault();
    closeDialog();
  });
  dialog.addEventListener("close", () => {
    dialog.classList.remove("quickstart-modal--closing");
    requestId += 1;
    if (trigger) {
      trigger.focus();
      trigger = null;
    }
  });

  document.addEventListener("click", async (event) => {
    const link = event.target.closest("a.quickstart-modal-link");
    if (
      !link ||
      event.defaultPrevented ||
      event.button !== 0 ||
      event.metaKey ||
      event.ctrlKey ||
      event.shiftKey ||
      event.altKey
    ) {
      return;
    }

    const url = new URL(link.href, window.location.href);
    if (url.origin !== window.location.origin) {
      return;
    }

    event.preventDefault();
    trigger = link;
    const currentRequest = ++requestId;
    dialog.setAttribute(
      "aria-label",
      link.title || `${link.textContent.trim()} quickstart`,
    );
    content.innerHTML = '<p class="quickstart-modal__loading">Loading quickstart\u2026</p>';
    dialog.showModal();
    window.requestAnimationFrame(() => {
      if (dialog.open) {
        dialog.classList.add("quickstart-modal--visible");
      }
    });

    try {
      const fragment = await loadFragment(url.href);
      if (dialog.open && currentRequest === requestId) {
        renderFragment(fragment);
      }
    } catch (_error) {
      if (dialog.open && currentRequest === requestId) {
        closeDialog(() => window.location.assign(url.href));
      }
    }
  });
})();
