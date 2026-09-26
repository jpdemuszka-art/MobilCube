# Landing pages

Static, dependency-free, French-first pages built for the Google Ads campaigns in `ads/`. Each ad group sends traffic to its own segment page; nothing lands on the home page.

| Page (FR) | Page (EN) | Campaigns |
|---|---|---|
| `vehicules-hiver.html` | `en/winter-vehicle-storage.html` | Vehicules hiver / Winter vehicle |
| `terrasse-commerciale.html` | `en/patio-storage.html` | Terrasse commercial / Commercial patio |
| `entreposage-mobile.html` | `en/mobile-storage.html` | Entreposage mobile / Mobile storage / Concurrents |
| `index.html` | `en/index.html` | Marque (hub with the three segments) |
| `merci.html`, `confidentialite.html` | `en/thank-you.html`, `en/privacy.html` | conversion page, Law 25 policy |

What every page has: a sticky mobile call bar, a call button in the header and hero, a five-field quote form with hidden GCLID/UTM capture, the real MobilCube prices next to the transport fee (Quebec all-inclusive price display), a comparison table against the alternatives the searcher is weighing, an FAQ that answers the objections heard on the phone, a seasonal countdown, a Consent Mode v2 banner, and a `hreflang` link to the other language.

## Deploy

Any static host works (Cloudflare Pages, Netlify, Vercel, or a folder on the mobilcube.com server). The ads assume `https://offres.mobilcube.com/`; if you use another host, change `LP_BASE` in `ads/build_import.py` and re-run it.

Before going live, replace in every page:

1. `<!-- Google tag: paste tracking/gtag-snippet.html here -->` with the real snippet (AW- and G- IDs, call conversion label).
2. `window.LP_CONFIG.formEndpoint` with the URL that receives the form (Formspree, Make/Zapier webhook, your CRM). Left empty, the form does a normal POST to the thank-you page, which still fires the conversion but does not store the lead.
3. The review line "insérez votre note et votre nombre d'avis" with the real Google rating and count.
4. The `[Nom du responsable]` placeholders in the privacy policies.
5. The two deadline dates (`data-deadline`): Dec 1 is the winter-tire law; Nov 15 for terraces is a planning assumption to confirm per borough.

## Test

Open each page on a phone: the call bar must be visible, the form must submit to the thank-you page, and the consent banner must appear once. In Google Tag Assistant, confirm `click_to_call`, `quote_started` and `generate_lead` fire and that no ad cookie is set before consent.
