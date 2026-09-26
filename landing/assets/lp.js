// Landing page behaviour: form submit (AJAX to FORM_ENDPOINT), countdown to the segment deadline, UTM/gclid capture.
(function () {
  var cfg = window.LP_CONFIG || {};
  var form = document.querySelector('form[data-lead-form]');
  // Capture campaign parameters into hidden fields for the CRM / offline conversion import.
  var params = new URLSearchParams(location.search);
  ['utm_source', 'utm_medium', 'utm_campaign', 'utm_term', 'utm_content', 'gclid', 'wbraid', 'gbraid'].forEach(function (k) {
    var v = params.get(k);
    if (!v) return;
    try { sessionStorage.setItem(k, v); } catch (e) {}
  });
  if (form) {
    ['utm_source', 'utm_medium', 'utm_campaign', 'utm_term', 'utm_content', 'gclid', 'wbraid', 'gbraid'].forEach(function (k) {
      var f = form.querySelector('input[name="' + k + '"]');
      var v = null;
      try { v = sessionStorage.getItem(k); } catch (e) {}
      if (f && v && !f.value) f.value = v;
    });
    form.addEventListener('submit', function (e) {
      if (!cfg.formEndpoint) return; // plain POST fallback
      e.preventDefault();
      var btn = form.querySelector('button[type="submit"]');
      btn.disabled = true;
      fetch(cfg.formEndpoint, { method: 'POST', headers: { Accept: 'application/json' }, body: new FormData(form) })
        .then(function (r) { if (!r.ok) throw new Error('bad'); form.querySelector('.success').style.display = 'block'; form.querySelector('fieldset').style.display = 'none'; })
        .catch(function () { btn.disabled = false; alert(cfg.lang === 'en' ? 'Something went wrong. Please call us.' : 'Une erreur est survenue. Appelez-nous.'); });
    });
  }
  // Deadline countdown (days left) for seasonal urgency, driven by data-deadline="YYYY-MM-DD".
  document.querySelectorAll('[data-deadline]').forEach(function (el) {
    var d = new Date(el.getAttribute('data-deadline') + 'T23:59:59-05:00');
    var days = Math.ceil((d - new Date()) / 864e5);
    var out = el.querySelector('[data-days]');
    if (!out) return;
    if (days > 0) out.textContent = days; else el.style.display = 'none';
  });
})();
