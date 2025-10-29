(function() {
  'use strict';

  // Get current theme from localStorage or default to 'auto'
  function getCurrentTheme() {
    return localStorage.getItem('theme') || 'auto';
  }

  // Apply theme to the document
  function applyTheme(theme) {
    if (theme === 'auto') {
      document.documentElement.removeAttribute('data-theme');
    } else {
      document.documentElement.setAttribute('data-theme', theme);
    }
  }

  // Update active button state
  function updateActiveButton(theme) {
    const buttons = document.querySelectorAll('.theme-btn');
    buttons.forEach(btn => {
      if (btn.dataset.theme === theme) {
        btn.classList.add('active');
      } else {
        btn.classList.remove('active');
      }
    });
  }

  // Set theme and save to localStorage
  function setTheme(theme) {
    localStorage.setItem('theme', theme);
    applyTheme(theme);
    updateActiveButton(theme);
  }

  // Initialize theme switcher on page load
  function init() {
    const currentTheme = getCurrentTheme();
    updateActiveButton(currentTheme);

    // Add click handlers to all theme buttons
    const buttons = document.querySelectorAll('.theme-btn');
    buttons.forEach(btn => {
      btn.addEventListener('click', function() {
        const theme = this.dataset.theme;
        setTheme(theme);
      });
    });
  }

  // Run initialization when DOM is ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
