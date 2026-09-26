# 02 · Google Ads strategy — MobilCube, fall/winter 2026-2027

Goal: be in the top ad positions for the searches that matter in Greater Montreal, pay a fair price for it, and turn clicks into **answered phone calls and 60-second bookings**. The plan is Search-first, French-first, segment-by-segment, with automation that pushes budget toward the weeks when people actually store cars, boats and terraces.

## 1. The thesis in five lines

1. Competitors hide prices, ban vehicles, sit far from the South Shore and market in English first. MobilCube publishes prices, can take a car, sits in Boucherville and speaks French. Every ad says one of those four things.
2. Generic "entreposage Montréal" is an expensive auction against 24-location chains. We enter it only through the mobile, vehicle and terrace long tail, and through the brand.
3. Search campaigns until we have 30+ conversions a month; Performance Max only after that, with Gemini imagery.
4. Calls are the primary conversion. Nothing launches until call tracking works.
5. Budget follows the calendar: the money is spent between October 5 and December 1.

## 2. Account and campaign architecture

Google removes campaign-level language targeting for Search in September 2026 and matches on the language of the ad instead, so French and English live in separate campaigns with fully French or fully English ads and keywords.

| Campaign | Type | Language | Goal | Geo (presence only) | Launch budget/day | Bidding at launch |
|---|---|---|---|---|---|---|
| `FR \| Search \| Vehicules hiver` | Search | FR | Calls + forms | Montreal CMA core (see geo tiers) | 85 $ | Max clicks, cap 3.50 $ → tCPA |
| `FR \| Search \| Terrasse commercial` | Search | FR | Calls | CMA core, Mon–Fri 7–19 +15 % | 50 $ | Max clicks, cap 3.00 $ → tCPA |
| `FR \| Search \| Entreposage mobile` | Search | FR | Calls + forms + booking | CMA core | 60 $ | Max clicks, cap 4.50 $ → tCPA |
| `EN \| Search \| Winter vehicle` | Search | EN | Calls + forms | West Island, Westmount/NDG, Hampstead, CSL, Saint-Lambert, Hudson/Vaudreuil | 25 $ | Max clicks, cap 6.00 $ |
| `EN \| Search \| Commercial patio` | Search | EN | Calls | same EN geo + downtown | 15 $ | Max clicks, cap 5.00 $ |
| `EN \| Search \| Mobile storage` | Search | EN | Calls + forms | same EN geo | 20 $ | Max clicks, cap 6.00 $ |
| `FR+EN \| Search \| Marque` | Search | both | Booking | Quebec | 5 $ | Target impression share 90 % top |
| `FR+EN \| Search \| Concurrents` | Search | both | Calls | CMA core | 15 $ | Manual-style cap 2.50 $, exact only |
| `FR+EN \| PMax \| Saisonnier` | Performance Max | both | Calls + forms | CMA core | 0 → 35 $ (phase 2) | Max conversions |

Launch total: about **275 $/day (≈ 8,400 $/month)** at full peak; the pacer script scales each campaign down in the trough. A lean version at 100 $/day is in `03-budget-and-forecast.md`.

Ad groups (one theme each, 8–20 keywords, phrase + exact only at launch):

- Vehicules hiver: `Auto hiver` · `Voiture collection` · `Moto hiver` · `VTT` · `Motoneige (été)` · `Motomarine & petit bateau` · `Remorque & équipement`
- Terrasse commercial: `Mobilier de terrasse` · `Restaurant & bar` · `Hôtel & condo` · `Commercial saisonnier & inventaire` · `Paysagiste & équipement`
- Entreposage mobile: `Entreposage mobile` · `Conteneur d'entreposage` · `Cube d'entreposage` · `Déménagement & rénovation` · `Rive-Sud (géo)` · `Montréal & Laval (géo)`
- English mirrors: `Winter car storage` · `Motorcycle & ATV` · `Boat & PWC` · `Patio furniture` · `Business seasonal` · `Mobile storage` · `Portable container` · `Moving & renovation`
- Marque: `MobilCube` (mobilcube, mobil cube, mobilcube boucherville, mobilcube prix)
- Concurrents: `PODS` · `Cubeit` · `GoCube` · `U-Box` · `BigSteelBox` (keywords only; never the names in ad text)

Settings that matter:
- Networks: Google Search only. **Untick search partners and Display expansion.**
- Location option: **Presence** (people in or regularly in), never "presence or interest".
- Devices: no adjustment at launch; expect 65–75 % mobile.
- Ad rotation: optimize. Ad schedule: 6:00–23:00 all campaigns; calls routed to a person 8:00–20:00, voicemail-to-SMS callback outside.
- Conversion goals per campaign: `Call from ads`, `Call from website`, `Quote form`, `Booking completed`. `Click to call` is secondary.
- Auto-applied recommendations: off. AI Max / broad match expansion: off at launch, revisit with 50+ conversions.
- Shared negative lists: `Negatives - FR` and `Negatives - EN` (from `ads/negatives/`) on every campaign, plus `Negatives - Auto` filled by the script.

## 3. Geo tiers (delivery cost drives margin)

Delivery is 300 $ per movement with 15 km included from Boucherville, then 2 $/km. Bid where the margin is.

| Tier | Areas | Bid adjustment |
|---|---|---|
| A | Boucherville, Longueuil, Saint-Hubert, Saint-Lambert, Brossard, Sainte-Julie, Varennes, Saint-Bruno | +20 % |
| B | Montreal island east of Décarie, Beloeil, Chambly, La Prairie, Candiac | 0 % |
| C | West Island, Laval, Repentigny, Terrebonne, Châteauguay, Vaudreuil | −15 % (EN campaigns already targeted here; keep 0 % there) |
| D | Rest of Quebec (brand campaign only) | −40 % |

## 4. Keywords (summary; full lists in `ads/keywords/`)

The FR list has 136 keywords in 6 clusters and the EN list 95 in 4 clusters. All volumes and CPCs are **estimates** calibrated from published US/Canadian benchmarks; the first job on day one is to paste them into Keyword Planner (Montréal CMA, 12 months) and re-rank. Head terms and expected CPC (CAD):

| Cluster | Examples | Match | Est. CPC |
|---|---|---|---|
| Mobile core FR | entreposage mobile, conteneur d'entreposage, cube d'entreposage, entreposage mobile montréal / rive-sud / longueuil, location conteneur entreposage | phrase + exact | 2.50–5.50 |
| Vehicle FR | entreposage hiver voiture, entreposage auto hiver montréal, remisage voiture hiver, entreposage moto hiver, entreposage VTT, entreposage motoneige, entreposage motomarine, hivernage bateau (small only) | phrase + exact | 1.50–3.50 |
| Terrace FR | entreposage mobilier de terrasse, entreposage terrasse restaurant, rangement mobilier extérieur commercial, entreposage saisonnier commercial, entreposage inventaire montréal | phrase + exact | 1.50–3.00 |
| Moving FR | conteneur déménagement, entreposage déménagement montréal, entreposage rénovation | phrase | 2.50–4.50 |
| Mobile core EN | mobile storage montreal, portable storage montreal, storage container rental montreal, moving container montreal | phrase + exact | 5.00–9.50 |
| Vehicle EN | winter car storage montreal, motorcycle storage montreal, atv storage, jet ski storage, boat storage west island | phrase + exact | 3.00–6.00 |
| Commercial EN | patio furniture storage, restaurant patio storage montreal, business storage montreal, seasonal inventory storage | exact | 3.00–6.00 |

Rules: accented spelling is canonical (close variants cover the rest); negatives need singular **and** plural; never negate the bare word "québec"; exclude RV/roulotte/motorisé and boats over 16 ft (they do not fit a 20 ft unit) unless a yard-parking product exists.

## 5. Ad copy principles (full RSAs in `ads/copy/` and the import CSV)

Each RSA carries 15 headlines and 4 descriptions. Pin one price headline in position 1 for the vehicle and terrace groups, one brand/location headline in position 2, leave the rest unpinned.

Headline building blocks (≤30 characters each):
- Proof: `Prix affichés, aucun frais caché` · `270 $/mois sur 6 mois` · `Livraison 300 $, 15 km inclus`
- Product: `Conteneur 20 pi livré chez vous` · `160 pi² d'acier CORTEN` · `Entrepôt chauffé à Boucherville`
- Vehicle: `Votre auto à l'abri tout l'hiver` · `Moto, VTT, motoneige acceptés` · `Fini le sel et la neige`
- Terrace: `Rangez votre terrasse en 1 jour` · `Chaises, tables, chauffe-terrasse` · `Retour livré au printemps`
- Action: `Réservez en 60 secondes` · `Appelez : réponse immédiate` · `Livraison Rive-Sud et Montréal`

Descriptions (≤90 characters): state the offer, the geography, the proof and the action, in that order. Example: `Conteneur de 20 pi livré dans votre entrée. 270 $/mois sur 6 mois, livraison 300 $. Réservez en ligne en 60 s.`

Assets on every campaign: 4 sitelinks (Tarifs, Réserver en 60 s, Entreposage de véhicules, Terrasses et commerces), 6 callouts (Entrepôt chauffé · Accès 24/7 sur place · Prix affichés · Dépôt remboursé · Rive-Sud, Montréal, Laval · Réservation en ligne), structured snippet "Services: Auto, Moto, VTT, Terrasse, Déménagement, Rénovation", call asset with a Google forwarding number, location asset (Google Business Profile), price asset (3 plans), image assets from `tools/gemini-creatives`.

## 6. Landing pages (built in `landing/`)

One page per segment, French default with an English mirror, same structure: sticky call button, price block that matches the ad, 5-field quote form, "how it works" in three steps, comparison table against the alternatives the searcher is considering, FAQ, reviews. Ads for a segment always land on that segment's page, never on the home page.

## 7. Measurement (details in `tracking/`)

1. Create the Google Ads conversion actions and add the AW- tag to GTM-K3G9FKRW (MobilCube already has GTM and GA4).
2. Website-call conversion with number swap on every page; call assets with call reporting; minimum call length 45 s.
3. Booking completion: the booking platform is a partner domain — add the same Google tag there or pass the GCLID and import bookings weekly as offline conversions (`tracking/offline-conversions-template.csv`).
4. Consent Mode v2 defaults denied (Law 25) so modelled conversions still flow when people refuse cookies.
5. Weekly: search-term miner report, call-quality report, impression-share guard log.

## 8. Bidding roadmap

| Stage | Trigger | Bidding |
|---|---|---|
| Launch (weeks 1–3) | none | Maximize clicks with max CPC caps per campaign; goal is data and top-of-page presence on core terms |
| Learning | 15–20 conversions in the campaign | Maximize conversions, no target |
| Efficiency | 30 conversions in 30 days | Target CPA: vehicle 45 $, terrace 70 $, mobile 60 $, EN +30 % |
| Peak weeks | pacer weight ≥ 1.3 | Raise tCPA 15–20 % and let the impression-share guard lift budgets; never lose top-of-page on vehicle terms in weeks 43–48 |
| Trough (Dec 15–Feb 28) | pacer weight ≤ 0.6 | Pause EN commercial, keep FR vehicle at 30 %, keep brand |

## 9. Performance Max (phase 2, from ~Nov 10 if Search delivers 30+ conversions)

One PMax campaign, seasonal asset groups (Véhicules, Terrasses, Général), Gemini images in 1.91:1, 1:1 and 4:5, French text assets, audience signals built from the site's converters and in-market "Moving & Relocation" / "Vehicle storage" segments, final URL expansion off, brand exclusions on. Budget 35 $/day, judged on incremental calls only.

## 10. Local Services Ads / pay-per-lead

Google lists **"Storage"** and **"Moving services"** among eligible Local Services Ads categories, and Local Services Ads are migrating into Performance Max with pay-per-lead goals from August 2026. Check eligibility for Boucherville in Google Ads → Local Services; if eligible, this is the cheapest call channel of all (pay per valid call, not per click). Requires business verification and insurance documents.

## 11. First 30 days checklist

- [ ] Fix the two site inconsistencies (148 vs 160 pi²; 300 $/2 $ vs 395 $/3 $ delivery) and soften "fireproof/airtight" wording
- [ ] Decide the vehicle policy (on-site only, or warehouse with ¼ tank and battery disconnected) and write it on the vehicle page
- [ ] Publish the three landing pages, privacy policy, consent banner
- [ ] Conversion actions, AW tag, call tracking, forwarding numbers live and tested with a real call
- [ ] Import `ads/google-ads-editor/*.csv` in Google Ads Editor; review, then post
- [ ] Keyword Planner pass; adjust caps
- [ ] Google Business Profile: categories, hours, photos, first 20 reviews requested from past customers
- [ ] Scripts installed in DRY_RUN; after one week, set DRY_RUN = false
- [ ] Day 7, 14, 30 reviews: search terms, call recordings, impression share, cost per call by campaign
