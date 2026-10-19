// Keep text on the notebook lines: round the height of boxes that are not made of text lines
// (tables, search boxes, headers that wrap) up to a whole number of ruled lines.
(function () {
  var sel = ".top, .wordmark, .tablewrap, .ufilters, .founder .initials, .stack table.cmp tr, .invite, .btn-block";
  function lh() { return parseFloat(getComputedStyle(document.documentElement).fontSize) * 2; }
  function snap() {
    var L = lh();
    Array.prototype.forEach.call(document.querySelectorAll(sel), function (el) {
      el.style.marginBottom = "";
      var cs = getComputedStyle(el), base = parseFloat(cs.marginBottom) || 0;
      var h = el.getBoundingClientRect().height, extra = (L - (h % L)) % L;
      if (extra > 0.5) el.style.marginBottom = (base + extra) + "px";
    });
  }
  window.addEventListener("load", snap);
  window.addEventListener("resize", function () { clearTimeout(snap.t); snap.t = setTimeout(snap, 150); });
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(snap);
  document.addEventListener("biswapath:rendered", snap);
})();
