(function (global) {
  "use strict";

  function pad2(n) {
    return String(n).padStart(2, "0");
  }

  function timestampLocal(d) {
    d = d || new Date();
    return (
      d.getFullYear() +
      "-" +
      pad2(d.getMonth() + 1) +
      "-" +
      pad2(d.getDate()) +
      " " +
      pad2(d.getHours()) +
      ":" +
      pad2(d.getMinutes())
    );
  }

  function escapeCell(value) {
    return String(value == null ? "" : value).replace(/\|/g, "\\|");
  }

  function buildExportHeader(meta) {
    meta = meta || {};
    var lines = ["## Human decisions", ""];
    lines.push("<!-- exported-from: " + (meta.exportedFrom || "unknown") + " -->");
    lines.push("<!-- exported-at: " + (meta.exportedAt || timestampLocal()) + " -->");
    if (meta.gate) lines.push("<!-- gate: " + meta.gate + " -->");
    if (meta.arc) lines.push("<!-- arc: " + meta.arc + " -->");
    if (meta.session != null && meta.session !== "") {
      lines.push("<!-- session: " + meta.session + " -->");
    }
    lines.push("");
    return lines.join("\n");
  }

  function buildMarkdownTable(headers, rows) {
    var out = [];
    out.push("| " + headers.join(" | ") + " |");
    out.push("| " + headers.map(function () { return ":----"; }).join(" | ") + " |");
    rows.forEach(function (row) {
      out.push("| " + row.map(escapeCell).join(" | ") + " |");
    });
    return out.join("\n");
  }

  function buildExport(meta, headers, rows, footerLines) {
    var parts = [buildExportHeader(meta)];
    if (headers && rows) parts.push(buildMarkdownTable(headers, rows));
    if (footerLines && footerLines.length) {
      parts.push("");
      parts.push(footerLines.join("\n"));
    }
    return parts.join("\n") + "\n";
  }

  function copyText(text) {
    if (navigator.clipboard && navigator.clipboard.writeText) {
      return navigator.clipboard.writeText(text);
    }
    return new Promise(function (resolve, reject) {
      var ta = document.createElement("textarea");
      ta.value = text;
      document.body.appendChild(ta);
      ta.select();
      try {
        document.execCommand("copy");
        document.body.removeChild(ta);
        resolve();
      } catch (err) {
        document.body.removeChild(ta);
        reject(err);
      }
    });
  }

  function showToast(message) {
    var el = document.getElementById("toast");
    if (!el) return;
    if (message) el.textContent = message;
    el.classList.add("show");
    setTimeout(function () { el.classList.remove("show"); }, 2000);
  }

  global.ViewsExport = {
    timestampLocal: timestampLocal,
    escapeCell: escapeCell,
    buildExportHeader: buildExportHeader,
    buildMarkdownTable: buildMarkdownTable,
    buildExport: buildExport,
    copyText: copyText,
    showToast: showToast,
  };
})(typeof window !== "undefined" ? window : globalThis);
