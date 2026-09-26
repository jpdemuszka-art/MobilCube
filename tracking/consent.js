// Minimal Law 25 consent banner (French first). Include after the gtag snippet, before </body>.
(function () {
  var KEY = 'consent-v1';
  var saved = null;
  try { saved = localStorage.getItem(KEY); } catch (e) {}
  function apply(granted) {
    var v = granted ? 'granted' : 'denied';
    gtag('consent', 'update', { ad_storage: v, ad_user_data: v, ad_personalization: v, analytics_storage: v });
  }
  if (saved === 'yes') { apply(true); return; }
  if (saved === 'no') { apply(false); return; }
  var fr = (document.documentElement.lang || 'fr').indexOf('en') !== 0;
  var box = document.createElement('div');
  box.id = 'consent-banner';
  box.setAttribute('role', 'dialog');
  box.innerHTML =
    '<p>' + (fr
      ? 'Nous utilisons des témoins (cookies) pour mesurer nos publicités et améliorer le site. Vous pouvez refuser sans perdre de fonctionnalités. <a href="/confidentialite.html">Politique de confidentialité</a>'
      : 'We use cookies to measure our ads and improve the site. You can decline without losing any features. <a href="/en/privacy.html">Privacy policy</a>') + '</p>' +
    '<div><button type="button" data-c="no">' + (fr ? 'Refuser' : 'Decline') + '</button>' +
    '<button type="button" data-c="yes" class="primary">' + (fr ? 'Accepter' : 'Accept') + '</button></div>';
  box.addEventListener('click', function (e) {
    var c = e.target && e.target.getAttribute('data-c');
    if (!c) return;
    try { localStorage.setItem(KEY, c); } catch (err) {}
    apply(c === 'yes');
    box.remove();
  });
  document.body.appendChild(box);
})();
