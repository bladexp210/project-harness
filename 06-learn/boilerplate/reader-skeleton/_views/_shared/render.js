(function (global) {
  "use strict";

  function renderTable(containerId, headers, rows) {
    var root = document.getElementById(containerId);
    if (!root) return;
    var html = ['<table class="views-table"><thead><tr>'];
    headers.forEach(function (h) { html.push("<th>" + h + "</th>"); });
    html.push("</tr></thead><tbody>");
    rows.forEach(function (row) {
      html.push("<tr>");
      row.forEach(function (cell) { html.push("<td>" + cell + "</td>"); });
      html.push("</tr>");
    });
    html.push("</tbody></table>");
    root.innerHTML = html.join("");
  }

  function renderMilestoneBar(containerId, milestones) {
    var root = document.getElementById(containerId);
    if (!root) return;
    root.innerHTML = milestones
      .map(function (m) {
        var cls = m.status === "done" ? "var(--promote)" : "var(--muted)";
        return '<div style="margin:0.25rem 0"><span style="color:' + cls + '">●</span> ' +
          m.name + " <span style=\"color:var(--muted)\">(" + (m.session || "—") + ")</span></div>";
      })
      .join("");
  }

  global.ViewsRender = { renderTable: renderTable, renderMilestoneBar: renderMilestoneBar };
})(typeof window !== "undefined" ? window : globalThis);
