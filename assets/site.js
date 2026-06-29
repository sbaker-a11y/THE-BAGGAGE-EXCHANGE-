/* THE Baggage Exchange — shared site behavior */
(function () {
  // Reveal on scroll
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) {
      if (e.isIntersecting) {
        e.target.classList.add('in');
        io.unobserve(e.target);
      }
    });
  }, { threshold: 0.14 });
  document.querySelectorAll('.reveal').forEach(function (el) { io.observe(el); });

  // Desktop dropdowns: open on hover (CSS) + click/keyboard for accessibility
  document.querySelectorAll('.nav .has-menu').forEach(function (group) {
    var btn = group.querySelector('button');
    if (!btn) return;
    btn.addEventListener('click', function (e) {
      e.preventDefault();
      var open = group.getAttribute('data-open') === 'true';
      document.querySelectorAll('.nav .has-menu[data-open="true"]').forEach(function (g) {
        if (g !== group) g.setAttribute('data-open', 'false');
      });
      group.setAttribute('data-open', open ? 'false' : 'true');
      btn.setAttribute('aria-expanded', open ? 'false' : 'true');
    });
  });
  document.addEventListener('click', function (e) {
    if (!e.target.closest('.nav .has-menu')) {
      document.querySelectorAll('.nav .has-menu[data-open="true"]').forEach(function (g) {
        g.setAttribute('data-open', 'false');
        var b = g.querySelector('button'); if (b) b.setAttribute('aria-expanded', 'false');
      });
    }
  });

  // Mobile menu toggle
  var menuBtn = document.querySelector('.menu-btn');
  var mobileNav = document.querySelector('.mobile-nav');
  if (menuBtn && mobileNav) {
    menuBtn.addEventListener('click', function () {
      var open = mobileNav.getAttribute('data-open') === 'true';
      mobileNav.setAttribute('data-open', open ? 'false' : 'true');
      menuBtn.setAttribute('aria-expanded', open ? 'false' : 'true');
      menuBtn.textContent = open ? '\u2630' : '\u2715';
      document.body.style.overflow = open ? '' : 'hidden';
    });
  }

  // Static forms: show a friendly confirmation, no fake backend claim
  document.querySelectorAll('form[data-static-form]').forEach(function (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var note = form.querySelector('.form-confirm');
      var mailto = form.getAttribute('data-mailto') || 'hello@thebaggageexchange.org';
      if (note) {
        note.hidden = false;
        note.textContent = 'Thank you. This form is not connected to a server yet. Please email us at ' + mailto + ' and we will respond personally.';
        note.focus && note.focus();
      } else {
        window.location.href = 'mailto:' + mailto;
      }
    });
  });
})();
