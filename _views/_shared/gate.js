(function (global) {
  "use strict";

  function escapeHtml(s) {
    return String(s)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;");
  }

  function numberedList(items, prefix) {
    return (items || [])
      .map(function (item, i) {
        return (i + 1) + ". " + item;
      })
      .join("\n");
  }

  function init(options) {
    options = options || {};
    var data = ViewsNav.readPageData();

    ViewsNav.renderBreadcrumb("breadcrumb", options.breadcrumb || [
      { label: "Project", href: "../project/index.html" },
      { label: options.gateLabel || data.gate || "Gate", href: null }
    ]);

    renderEditableList("will-decide-list", data.willDecide || []);
    renderEditableList("will-not-decide-list", data.willNotDecide || []);
    renderQuestions(data.questions || []);
    renderEvidence(data.evidence || []);

    var ruleEl = document.getElementById("decision-rule");
    if (ruleEl) ruleEl.textContent = data.decisionRule || "";

    var signedEl = document.getElementById("scope-signed");
    var notSignedEl = document.getElementById("scope-not-signed");
    if (signedEl) {
      signedEl.value = numberedList(data.willDecide || []);
    }
    if (notSignedEl) {
      notSignedEl.value = numberedList(
        (data.willNotDecide || []).map(function (s) {
          return s + " (not approved)";
        })
      );
    }

    document.getElementById("copy").addEventListener("click", function () {
      var md = exportMarkdown(options.exportedFrom, data);
      ViewsExport.copyText(md).catch(function () {});
      ViewsExport.showToast("Copied to clipboard");
    });

    document.getElementById("previewBtn").addEventListener("click", function () {
      var pre = document.getElementById("preview");
      if (pre.style.display === "block") {
        pre.style.display = "none";
        return;
      }
      pre.textContent = exportMarkdown(options.exportedFrom, data);
      pre.style.display = "block";
    });
  }

  function renderEditableList(containerId, items) {
    var el = document.getElementById(containerId);
    if (!el) return;
    el.innerHTML = items
      .map(function (item, i) {
        return (
          '<li><textarea data-list="' + containerId + '" data-idx="' + i + '">' +
          escapeHtml(item) + "</textarea></li>"
        );
      })
      .join("");
  }

  function renderQuestions(questions) {
    var el = document.getElementById("questions-list");
    if (!el) return;
    el.innerHTML = questions
      .map(function (q, i) {
        return (
          '<li><span class="q-text">' + escapeHtml(q) + '</span>' +
          '<div class="gate-answer">' +
          '<label><input type="radio" name="q-' + i + '" value="yes" /> yes</label>' +
          '<label><input type="radio" name="q-' + i + '" value="no" checked /> no</label>' +
          '<label><input type="radio" name="q-' + i + '" value="na" /> n/a</label>' +
          "</div>" +
          '<textarea class="q-note" data-q="' + i + '" placeholder="Notes (optional)"></textarea></li>'
        );
      })
      .join("");
  }

  function renderEvidence(rows) {
    var tbody = document.getElementById("evidence-body");
    if (!tbody) return;
    tbody.innerHTML = rows
      .map(function (row, i) {
        return (
          "<tr>" +
          "<td>" + escapeHtml(row.question) + "</td>" +
          "<td>" + escapeHtml(row.where) + "</td>" +
          "<td>" + escapeHtml(row.passWhen) + "</td>" +
          '<td><div class="gate-answer">' +
          '<label><input type="radio" name="ev-' + i + '" value="pass" /> pass</label>' +
          '<label><input type="radio" name="ev-' + i + '" value="fail" checked /> fail</label>' +
          '<label><input type="radio" name="ev-' + i + '" value="na" /> n/a</label>' +
          "</div></td></tr>"
        );
      })
      .join("");
  }

  function readRadio(name) {
    var checked = document.querySelector('input[name="' + name + '"]:checked');
    return checked ? checked.value : "";
  }

  function collectQuestionRows(questions) {
    return questions.map(function (q, i) {
      var answer = readRadio("q-" + i);
      var noteEl = document.querySelector('.q-note[data-q="' + i + '"]');
      var note = noteEl ? noteEl.value.trim() : "";
      var cell = answer + (note ? " — " + note : "");
      return [q, cell];
    });
  }

  function exportMarkdown(exportedFrom, data) {
    var questions = data.questions || [];
    var rows = collectQuestionRows(questions);

    var approved = readRadio("gate-approved");
    rows.push(["Gate approved", approved]);

    var signedEl = document.getElementById("scope-signed");
    var notSignedEl = document.getElementById("scope-not-signed");
    var footer = [
      "## Scope confirmation",
      "",
      "You signed off that:",
      signedEl ? signedEl.value.trim() : "",
      "",
      "You did not sign off that:",
      notSignedEl ? notSignedEl.value.trim() : ""
    ];

    return ViewsExport.buildExport(
      {
        exportedFrom: exportedFrom,
        gate: data.gate,
        arc: data.arc,
        session: String(data.session != null ? data.session : "")
      },
      ["Question", "Answer"],
      rows,
      footer
    );
  }

  global.ViewsGate = { init: init, exportMarkdown: exportMarkdown };
})(typeof window !== "undefined" ? window : globalThis);
