(function (global) {
  "use strict";

  function renderBreadcrumb(containerId, crumbs) {
    var el = document.getElementById(containerId);
    if (!el || !crumbs || !crumbs.length) return;
    el.innerHTML = crumbs
      .map(function (c, i) {
        if (i === crumbs.length - 1 || !c.href) {
          return "<span>" + escapeHtml(c.label) + "</span>";
        }
        return '<a href="' + escapeHtml(c.href) + '">' + escapeHtml(c.label) + "</a>";
      })
      .join(" / ");
  }

  function escapeHtml(s) {
    return String(s)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;");
  }

  function readPageData(id) {
    id = id || "page-data";
    var node = document.getElementById(id);
    if (!node) return {};
    try {
      return JSON.parse(node.textContent || "{}");
    } catch (e) {
      console.error("Invalid page-data JSON", e);
      return {};
    }
  }

  global.ViewsNav = { renderBreadcrumb: renderBreadcrumb, readPageData: readPageData };
})(typeof window !== "undefined" ? window : globalThis);
