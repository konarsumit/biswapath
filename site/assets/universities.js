(function () {
  var t = U.t, list = document.getElementById("ulist"), q = document.getElementById("uq"), c = document.getElementById("uc");
  function esc(s) { return String(s || "").replace(/[&<>"]/g, function (m) { return {"&":"&amp;","<":"&lt;",">":"&gt;","\"":"&quot;"}[m]; }); }
  function norm(s) { return String(s || "").toLowerCase().normalize("NFD").replace(/[̀-ͯ]/g, ""); }
  function links(s, label) { // turn "Label: https://..." | "..." into links
    var n = 0, many = (String(s || "").match(/https?:/g) || []).length > 1;
    return esc(s).replace(/(https?:\/\/[^\s|;]+)/g, function (u) { n++;
      var text = label ? label + (many ? " " + n : "") : u.replace(/^https?:\/\/(www\.)?/, "").split("/")[0];
      return '<a href="' + u + '" target="_blank" rel="noopener">' + text + '</a>'; }).replace(/ \| /g, "<br>");
  }
  function row(label, val) { return val ? '<dt>' + label + '</dt><dd>' + val + '</dd>' : ""; }
  var order = ["UK", "Germany", "Sweden", "USA", "Canada", "Australia", "UAE"];
  var unis = U.unis.slice().sort(function (a, b) { return order.indexOf(a.country) - order.indexOf(b.country) || a.name.localeCompare(b.name); });
  function render() {
    var k = norm(q.value.trim()), cc = c.value, h = "", last = "";
    var rows = unis.filter(function (u) { return (!cc || u.country === cc) && (!k || norm(u.name + " " + u.city + " " + u.country).indexOf(k) >= 0); });
    if (!rows.length) { list.innerHTML = '<p class="empty">' + t.none + '</p>'; return; }
    rows.forEach(function (u) {
      if (u.country !== last) { var C = U.country[u.country]; h += '<h2 class="ucountry">' + esc(u.country) + '</h2><p class="unote"><b>' + t.ug + ':</b> ' + esc(C.ug_route) + ' · ' + esc(C.ug_fee) + '. ' + esc(C.ug_deadline) + (C.tuition ? '<br>' + esc(C.tuition) : '') + '<br><b>' + t.phd + ':</b> ' + esc(U.phd[u.country]) + '</p>'; last = u.country; }
      h += '<section class="ucard"><h3>' + esc(u.name) + ' <span class="ucity">' + esc(u.city || "") + '</span></h3><dl>' +
        row(t.web, links(u.web)) + row(t.qs, esc(u.qs)) + row(t.fee, esc(u.pg_fee)) + row(t.deadline, esc(u.pg_deadline)) + row(t.tuition, esc(u.pg_tuition)) +
        row(t.sch, esc(u.scholarship)) + row(t.chat, u.chat ? links(u.chat, t.chat_link) + (u.chat_note ? ' <span class="ucity">(' + esc(u.chat_note) + ')</span>' : '') : '') +
        row(t.soc, links(u.society)) + row(t.src, links([u.pg_src, u.scholarship_src].filter(Boolean).join(" | ").replace(/ ; /g, " | "), t.src_link)) + '</dl></section>';
    });
    list.innerHTML = h;
    document.dispatchEvent(new Event("biswapath:rendered"));
  }
  q.addEventListener("input", render); c.addEventListener("change", render); render();
})();
