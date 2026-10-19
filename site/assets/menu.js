// Header menus: one open at a time; close on outside click or Escape.
(function () {
  var menus = Array.prototype.slice.call(document.querySelectorAll('details.menu'));
  menus.forEach(function (m) {
    m.addEventListener('toggle', function () {
      if (m.open) menus.forEach(function (o) { if (o !== m) o.open = false; });
    });
  });
  document.addEventListener('click', function (e) {
    menus.forEach(function (m) { if (!m.contains(e.target)) m.open = false; });
  });
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') menus.forEach(function (m) {
      if (m.open) { m.open = false; m.querySelector('summary').focus(); }
    });
  });
})();
