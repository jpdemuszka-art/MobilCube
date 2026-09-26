# 06 · Quebec compliance for the ads, the landing pages and the follow-up

This is practical guidance, not legal advice. Confirm the two starred items with the OQLF or counsel before launch.

## French language (Charter of the French language, as amended by Bill 96)

| Rule | What it means for us | Status |
|---|---|---|
| Commercial advertising must be in French; another language may be used provided French is at least as prominent (Charter s. 52 for catalogues, brochures, websites; s. 58 for public signs and commercial advertising, where French must be **markedly predominant**). | Every French campaign is French only. English campaigns are served to people who search in English and land on English pages that have a French version one click away. Never run an English ad to a French query. | Built in: separate FR and EN campaigns, FR default site. |
| Since June 1, 2025, on exterior signage a non-French trademark or business name must be accompanied by French text occupying **at least twice the space** (OQLF, "Affichage des marques de commerce et des noms d'entreprises"). | This is a signage rule for the yard and the trucks; it does not govern a Google text ad. Keep the generic "entreposage mobile" next to "MobilCube" on trucks and the Boucherville sign. | Note for operations. |
| ★ Whether a Google Ads text ad shown in Quebec is "commercial advertising" under s. 58 (markedly predominant French) or a publication under s. 52 (French at least equivalent) | Our approach satisfies both: French ads for French searchers, bilingual site with French default, French-first images with no text. | Confirm with OQLF if you ever want a bilingual single ad. |
| Google removes campaign-level language targeting for Search from September 2026; ads match on the language of the ad itself (Google Ads Help 1722078). | Reinforces the structure: French ads and keywords in one campaign, English in another. Do not mix languages inside an ad group. | Built in. |

Do: accents in ad copy (entrepôt, véhicule), Quebec vocabulary (VTT, motoneige, roulotte, remisage), prices as "270 $/mois" (space before $), 24-hour times.
Don't: English words in French headlines except the brand; machine-translated English pages; images containing English text.

## Price display (Consumer Protection Act, s. 224 c) and Competition Act)

- An advertised price must be the **all-inclusive price** except sales taxes. "270 $/mois + taxes" is fine; "à partir de 180 $/mois" is fine only if a real customer can pay 180 $ (the 24-month Avantage plan) and the condition is visible next to it.
- Delivery is a separate, optional-by-distance charge; always show it beside the rent: "Livraison 300 $ par déplacement, 15 km inclus, puis 2 $/km".
- Promotions must state the conditions (dates, minimum term, new customers) in the ad or one click away.
- Performance claims need "adequate and proper" testing under the Competition Act. Use **"acier CORTEN soudé, étanche"** rather than "fireproof" or "airtight" unless there is a certificate. Avoid "the best" unless it is clearly opinion.
- Comparative claims against named competitors are allowed if true and provable at the time; prefer verifiable facts ("prix affichés", "livré chez vous") over naming PODS or Cubeit in ad text (trademark policy also blocks their names in headlines).

## Privacy (Law 25, in force in full since Sept 2024)

| Requirement | Implementation in this repo |
|---|---|
| Consent before non-essential cookies (Google Ads, GA4, Meta) | `tracking/gtag-snippet.html` sets Consent Mode v2 defaults to denied; `tracking/consent.js` shows a French-first banner with equal Accept/Refuse buttons. |
| Privacy policy naming the person responsible | `landing/confidentialite.html` and `landing/en/privacy.html` templates with placeholders for the name and contact. |
| Announce call recording | Script the greeting on the ad line: "Cet appel peut être enregistré à des fins de qualité." |
| Collect only what you need | Form fields: name, phone, email, postal code, what to store, dates. |
| Data leaving Quebec | Google and CallRail store data outside Quebec; the policy discloses it. Keep a one-page privacy impact note on file. |

## Anti-spam (CASL)

- A quote request creates **implied consent** to email or text that person about the request for 6 months. Marketing beyond that needs express consent (a checked, not pre-checked, box).
- Every marketing email or SMS: sender identity, mailing address, unsubscribe.

## Google Ads policies to watch

- Trademarks: you may bid on "pods", "cubeit", "gocube" as keywords, but do not put those names in headlines, descriptions or paths.
- Phone numbers only in call assets, never typed into headlines.
- Image assets: no text or logo overlays, no collages, no blurry images; only relevant photos (Google Ads Help 9566341).
- Prices in ads must match the landing page.
