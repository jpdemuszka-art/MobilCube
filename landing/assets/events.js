// Conversion events for the landing pages. Include before </body>.
(function () {
  function send(name, params) { if (typeof gtag === 'function') gtag('event', name, params || {}); }
  // GCLID capture for offline conversion import (stored 90 days, written to hidden form fields).
  try {
    var m = location.search.match(/[?&]gclid=([^&]+)/);
    if (m) localStorage.setItem('gclid', JSON.stringify({ v: m[1], t: Date.now() }));
    var g = JSON.parse(localStorage.getItem('gclid') || 'null');
    if (g && Date.now() - g.t < 90 * 864e5) {
      document.querySelectorAll('input[name="gclid"]').forEach(function (i) { i.value = g.v; });
    }
  } catch (e) {}
  // Click-to-call (secondary conversion)
  document.addEventListener('click', function (e) {
    var a = e.target.closest && e.target.closest('a[href^="tel:"]');
    if (a) send('click_to_call', { segment: document.body.dataset.segment || '', placement: a.dataset.placement || '' });
  });
  // Quote form
  var form = document.querySelector('form[data-lead-form]');
  if (form) {
    var started = false;
    form.addEventListener('focusin', function () { if (!started) { started = true; send('quote_started', { segment: form.dataset.segment || '' }); } });
    form.addEventListener('submit', function () {
      var fd = new FormData(form);
      send('generate_lead', {
        segment: form.dataset.segment || '',
        item_type: fd.get('item_type') || '',
        city: fd.get('city') || '',
        start_month: fd.get('start_date') || ''
      });
    });
  }
})();
