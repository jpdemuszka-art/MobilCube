# MobilCube Google Ads: efficiency audit, 2026-10-08

Account 194-768-4780 (Supermetrics `AW` / 1947684780). Data: 2026-10-07 09:00 to 2026-10-08 about 09:05 Montréal time. This was a read-only audit: nothing was changed in the account. All amounts are CAD.

## Applied since the audit

| Date | Fix | What changed in the account | Still open |
|---|---|---|---|
| 2026-10-08 | F1 | FR Entreposage mobile > Déménagement & rénovation: the PHRASE keywords "déménagement et entreposage" and "déménagement entreposage" were removed (the connector cannot pause a keyword; re-add them to undo). Their EXACT versions stay. The 27 movers and trucks negatives of list A were added at campaign level (215 → 242 negatives). The 93 cities, budget, bids, schedule and assets were checked unchanged after the write. | The 3 U-Haul entries of list A (`u haul`, `u-haul`, `uhaul`) wait for the owner's U-Haul decision. |

---

## 1. Verdict

1. **Spend so far: 115.73 $, 488 impressions, 47 clicks, average CPC 2.46 $.** On Google Search alone the CPC was 3.22 $. Prices per click are below the plan (3.60 $ blended) and well below the US storage median (about 10.30 $ CAD). Price per click is not the problem.
2. **Clearly irrelevant traffic: 14.69 $, or 12.7% of spend.** That is 22% of the 65.36 $ whose search terms Google shows. It breaks down as movers and truck rental 12.48 $ and buying a 20 ft container 2.21 $. Another 4.97 $ ("u haul storage boxes") is ambiguous: it can mean cardboard boxes or U-Haul's U-Box, which is the same product type as MobilCube. The blocks below do not overlap and add up to the 115.73 $ spent:

   | Network | Clear waste | Ambiguous (U-Haul) | Relevant, wrong campaign | Relevant, right campaign | Hidden terms | Total |
   |---|---:|---:|---:|---:|---:|---:|
   | Google Search | 8.68 $ | 4.97 $ | 8.68 $ | 24.59 $ | 30.37 $ | 77.29 $ |
   | Search partners | 6.01 $ | 0 $ | 5.95 $ | 6.48 $ | 20.00 $ | 38.44 $ |
   | **Total** | **14.69 $** (12.7%) | **4.97 $** (4.3%) | **14.63 $** (12.6%) | **31.07 $** (26.8%) | **50.37 $** (43.5%) | **115.73 $** |

   Search partners (38.44 $, 33% of spend) are on, although the plan says they should be off. They cut across every block. The hidden spend can be attributed by keyword (keyword cost minus visible search-term cost). Half of it sits under one keyword:

   | Keyword (campaign) | Hidden spend |
   |---|---:|
   | location d'entreposage (FR Entreposage mobile) | 25.04 $ |
   | entreposage pour entreprise (FR Terrasse commercial, F3) | 11.29 $ |
   | rent storage container (EN Mobile storage) | 4.28 $ |
   | location cube entreposage, EXACT (FR Entreposage mobile) | 3.50 $ |
   | déménagement et entreposage (FR Entreposage mobile, F1) | 3.45 $ |
   | espace d'entreposage à louer (FR Entreposage mobile) | 2.81 $ |
   | **Total** | **50.37 $** |

3. **Conversions: 0 form leads and 0 calls** (70 call impressions). GTM holds a booking tag and a second tag for tel: clicks. Both are wired, but neither has been tested end to end (M1).
4. **Overall: about 1 dollar in 8 is clearly wasted, and the cause is fixable today.** The fix is to pause three PHRASE keywords (two in F1, one in F3) and add the missing negatives.
   - Three PHRASE keywords took 62.53 $, or 54% of all spend: "location d'entreposage" 26.22 $, "entreposage pour entreprise" 20.38 $ (F3) and "déménagement et entreposage" 15.93 $ (F1).
   - The largest, "location d'entreposage", is not paused. 25.04 $ of its cost is hidden and 16.27 $ came from partners, so F2 and the watch list handle it.
   - Search partners are a separate problem: they are on against the plan, and their value is unknown.
   - The best seasonal campaign, FR Vehicules hiver, is under-delivering. It spent 9.51 $ of its 45 $/day budget and lost 75% of impressions to ad rank.
5. **Caveat: the sample is small.** It covers about 17 serving hours (12 for the two terrace/patio campaigns) and 24 Google Search clicks. Even at a normal 4.65% lead rate, 0 leads in 24 Google clicks happens 32% of the time (48% at 3%). Today's verdicts therefore rest on **search intent**, not on cost per lead. Cost per lead (ROI) can be judged once a segment has spent about 3× its allowable cost per lead on Google Search (§6). For the account that is about 10-10 to 10-12, and for FR Entreposage mobile about 10-12 to 10-14.

---

## 2. Fix now

"Monthly effect" says whether money is **saved** or only **redirected**. FR Entreposage mobile and EN Mobile storage run out of budget every day (68% and 67% of impressions lost to budget). Money removed from bad searches there is spent on other searches, not saved.

The "$ wasted so far" column uses the same classes as the §1 table, so its clear-waste figures add up to the 14.69 $ headline: 12.48 $ (F1) + 2.21 $ (F4).

| # | Action | Why (evidence) | $ wasted so far | Monthly effect | Where / how | Reversible |
|---|---|---|---|---|---|---|
| F1 | **FR Entreposage mobile > Déménagement & rénovation: PAUSE the PHRASE keywords "déménagement et entreposage" (3.50 $) and "déménagement entreposage" (2.80 $).** Keep both EXACT versions (2.80 $). Then add negative list A (§3). | "déménagement et entreposage" PHRASE: 117 impr / 7 clicks / 15.93 $ (25.5% of the campaign). All 6 visible clicks were movers or trucks (uber déménagement 3.48, camion de déménagement 3.49, demenageur st jean 1.71, …). 59–61 of 64 visible impressions were movers or trucks. MobilCube is not a mover. | **12.48 $** visible. The keyword's full cost is 15.93 $, of which 3.45 $ is in hidden terms. | About 300 $/mo (range 150–450) of a capped budget **redirected** to storage searches. Not cash saved. | API: keyword status + campaign negatives | Yes |
| F2 | **Turn off Google search partners on all 8 Search campaigns.** Start with FR Entreposage mobile and FR Terrasse commercial, which carry 36.23 $ of the 38.44 $. | Partners: 72 impr / 23 clicks / 38.44 $ (33% of spend), CTR 31.9% vs 5.8% on Google Search. The plan says partners are off (docs/02 l.41, docs/09 l.138), but the API spec cannot express this setting, so partners stayed on by default. Among visible terms, partner traffic is not clearly worse than Google: 33% of visible partner spend was clear waste, against 19% on Google (29% if the U-Haul click counts). On 11 and 15 visible clicks that gap is not significant (Fisher p ≈ 0.4). The case for turning partners off rests on the plan and the 32% CTR anomaly, not on search-term quality. | 38.44 $ of **unknown** value (0 conversions on both networks; not proven waste). It overlaps F1 (3.80 $), F3 (5.95 $) and F4 (2.21 $), so do not add these figures together. | **About 0 $ net saving.** About 37 $/day (about 1,050–1,100 $/mo) moves to Google Search at about 2× CPC: fewer clicks, from searches you can see. | **UI only:** Campaign > Settings > Networks > untick "Include Google search partners". In Editor: select the 8 campaigns, untick, Post. Not possible via `manage_campaign`. | Yes |
| F3 | **FR Terrasse commercial > Commercial saisonnier & inventaire: PAUSE the PHRASE keyword "entreposage pour entreprise" (3.15 $).** Do not add an EXACT version (no Planner volume). Add negative lists C, B and F (§3). Keep the 12 $/day budget. | This keyword produced 100% of the campaign's cost (45 impr / 8 clicks / 20.38 $). None of the 21 visible impressions had terrace, restaurant or business intent: they were near-me storage searches ("entrepôt à proximité"), warehouse leasing, RV and Shawinigan searches. The 4 visible clicks (9.09 $) were consumer near-me and mini-storage searches. They are real prospects for the mobile-storage offer, but they were shown the terrace ad. | **0 $** clear waste. 9.09 $ of visible spend was misrouted (in §1 it is counted as "relevant, wrong campaign"). The keyword's full cost is 20.38 $, of which 11.29 $ is hidden. | Up to about 150–220 $/mo stops being spent on non-B2B searches (upper bound). The near-me searches move to FR Entreposage mobile. The terrace keywords keep their budget for the Nov 1 and Nov 15 deadlines. | API | Yes |
| F4 | **EN junk negatives:** lists D and E (§3). | "price of 20 ft container" cost 2.21 $, all of EN Commercial patio's spend, from a partner. "u haul storage boxes" cost 4.97 $ (28.7% of EN Mobile storage), because the existing "storage box" negative does not match the plural. That search is ambiguous (cardboard boxes or U-Box). List D therefore negates it as EXACT only, which hands U-Haul searches to the owner's decision in §3 instead of a 5.00 $ bid. | **2.21 $** clear waste, plus 4.97 $ ambiguous | Too few clicks to project | API | Yes |
| F5 | **RV/boat, sea-container and far-town negatives:** lists B and F (§3). | 13 impressions on RV/boat searches ("entreposage vr intérieur", "entreposage bateau prix", …) in FR Entreposage mobile and Terrasse, which have no RV negatives. EN Mobile storage and EN Commercial patio have none either; EN Winter vehicle does. 2 impressions on sea-container searches ("conteneur maritime 10 pieds", "sea container with side doors"). The owner's rule is that MobilCube does not sell or rent sea containers. 15 impressions on out-of-area towns, including Sorel-Tracy, Bromont, Waterloo and Lanoraie, which the delivery campaigns cannot serve. MobilCube stores no RVs or boats. | 0 $ | Not measurable (0 clicks). This is hygiene ahead of the RV peak. | API | Yes |
| F6 | **Delete the leftover ad-group negative "granby" (PHRASE) in 23 ad groups.** It is in all 9 FR Vehicules hiver groups, all 5 Terrasse groups, the 7 original FR Entreposage mobile groups and both Concurrents groups. FR+EN Marque also carries it, at campaign level and in its one ad group. **Delete only that row.** Each ad-group list also holds full copies of the campaign negatives, which must stay. | Granby has been a targeted city since 10-07 (build_import.py dropped this negative on purpose), so the leftover blocks every Granby search, e.g. "entreposage voiture hiver granby", in FR Vehicules hiver and Terrasse. Source: live structure pull of 10-08 PM (`audit-2026-10-08/live-structure-pm/`). In the five campaigns saved verbatim, the campaign-level lists match the api-specs exactly and contain no "granby". EN Mobile storage and EN Commercial patio carry no "granby" at any level. | 0 $ (blocked searches never show in reports) | Re-opens a served city | UI or Editor (removing a negative) | Yes |
| F7 | **Fix "entrepôt à louer", which blocks "mini entrepôt à louer".** (a) Now, via API: add [mini entrepot a louer] EXACT at 2.41 $ in Mini-entrepôt. (b) In the UI: remove only the **campaign-level** PHRASE "entrepôt à louer" and keep its ad-group copies in the 7 original groups. In the same session, add list G (§3):<br>• the campaign EXACT negatives;<br>• the 3 missing PHRASE variants in the 7 original groups;<br>• all 4 PHRASE variants in Grand Montréal (géo) and Montérégie (géo), which have no ad-group negatives at all.<br>Then add [mini entrepôt à louer] EXACT at 2.41 $. Only Mini-entrepôt stays without these negatives. | A phrase negative blocks every search containing those words, so "mini entrepôt à louer" (140 searches/mo) can never show. Without the campaign-level negative, Grand Montréal and Montérégie would lose all protection against leasing searches. EXACT geo keywords do catch those searches as close variants: EN [storage longueuil] served "entrepôt à louer longueuil". Unaccented leasing searches ("entrepot a louer terrebonne", "entrepot longueuil a louer") still get through today. | 0 $ | Re-opens about 140 core searches/mo. The unaccented "mini entrepot a louer" (70/mo) already serves, as a close variant of "espace d'entreposage à louer". | API (adds) + UI (removal) | Yes |
| F8 | **FR Vehicules hiver: raise the core car bids by +0.40–0.45 $, capped at 2.85 $** (table §4b). **In the same week, replace 3 "Auto hiver" headlines** with "Entreposage auto hiver" (22 characters), "Entreposage voiture l'hiver" (27) and "Prix entreposage auto hiver" (27). They replace "Mini-entrepôt pour votre auto", "Moto, VTT, motoneige acceptés" and "Aucun frais d'administration". Keep "Entrepôt chauffé : 160 $/mois". | Impression share 25%: 75% lost to rank, 0% to budget. The campaign spends 9.51 $ of 45 $/day in peak season. QS is 3, with ad relevance Below average, on the 2 main car keywords, and no Auto hiver headline contains "entreposage auto/voiture". The ad group "Auto hiver chauffé", whose headline contains the keyword, rates Above average. | 0 $ | **Growth, not saving.** Puts the idle ~35 $/day to work on car searches. Every bid stays ≤ 2.85 $, under the 2.88 $ heated-car break-even at the 4% planning case (§4c). The cap assumes every car lead takes the cheaper warehouse plan. "Auto hiver" leads with the at-home 270 $ offer (break-even 6.66 $ at 4%), so the cap is conservative for that group. | Bids: API. RSA: UI, or recreate the ad as on 10-07 | Yes |
| F9 | **Route car searches to the vehicle ad.** Phase 1, now, together with F8: add list H1 (§3, 9 narrow car phrases) to FR Entreposage mobile, and add the FR Vehicules hiver keywords in §4d. Phase 2, about 10-12, and only if FR Vehicules hiver impression share has risen: add list H2 (broad vehicle words). | 9 car searches (12 impr / 2 clicks / 5.54 $) were served the 350/270 $ mobile-storage ad instead of the vehicle ad. At least 3 of them already match FR Vehicules hiver keywords:<br>• "entreposage auto hiver montréal" and "… rive nord" match PHRASE "entreposage auto hiver" (2.25 $), and "rive nord" is also an EXACT keyword at 2.60 $;<br>• "entreposage voiture hiver prix" is an EXACT and PHRASE keyword (2.40 $).<br>They went to FR Entreposage mobile because its PHRASE keywords bid 2.80–3.50 $ and win on ad rank. After F8 the vehicle bids stay ≤ 2.85 $, so new vehicle keywords alone will not route these searches. Raising vehicle bids to 3.50 $ would pass the heated-car break-even, so negatives are the routing tool. Trade-off: until F8 lifts FR Vehicules hiver's rank, some of these searches will show no MobilCube ad (12 impressions in 1.5 days). | 5.54 $ sent to the wrong campaign (not waste) | About 0 $. Better ad and price match for car searches. The freed FR Entreposage mobile budget goes to storage searches. | API | Yes |
| F10 | **Add the volume-backed EXACT keywords in §4d** (≥20 searches/mo, all seen in the data). | High-intent searches that currently match only through broad phrase keywords or land in the wrong campaign | 0 $ | Small | API | Yes |
| F11 | **Booking page (owner, WordPress):**<br>(1) Show "Pressé ? Appelez-nous : 450-641-6498" as a visible tel: link above the form.<br>(2) Change the phone field from Number to Single Line Text so it accepts "514-555-5555", and keep it optional.<br>(3) Offer start months Octobre 2026 → Septembre 2027 plus "Je ne sais pas" (the list now starts at Juillet 2026).<br>(4) Remove the "confirm email" field.<br>(5) Label the count choices 1/2/3/4+ (they are now "Choice 1…").<br>(6) Remove "conteneur/container" from both booking pages and use "mini-entrepôt / MobilCube unit" instead (list below the table).<br>(7) Add "Véhicule (auto/moto) – entrepôt chauffé" and "Mobilier de terrasse commerciale" to "Quel est votre projet ?", plus a vehicle price line (auto 160 $/mois, moto 80 $/mois, 6 mois, sans livraison).<br>(8) Replace the reCAPTCHA v2 checkbox with an invisible Turnstile or reCAPTCHA v3 (both available in WPForms Lite).<br>**After any form edit, re-test both GTM conversion tags (M1).** | 35 of 47 clicks come from phones. The form has 10 required inputs and a captcha checkbox, and the phone field rejects formatted numbers. The phone number never appears as visible text. Landing-page experience is "Below average" on 11 of 12 keywords with a QS. Vehicle and patio ads land on a page with no vehicle or patio option. The owner's rule bans "conteneur". | 0 $ | Main conversion-rate lever (not measurable yet) | Website (WPForms Lite + theme) | Yes |
| F12 | **Verify tracking and count real leads before judging ROI** (§5 steps 1–4) | 0 conversions cannot be read until the tags are proven to fire | — | Gate for every ROI decision | GTM Preview + owner | n/a |
| F13 | **Lower two vehicle bids that sit above break-even.**<br>• EN Winter vehicle > Heated car storage: [indoor car storage montreal] EXACT and PHRASE, 4.00 → 2.85 $.<br>• FR Vehicules hiver > Moto hiver: "entreposage moto hiver" (EXACT and PHRASE) and [remisage moto], 2.00 → 1.80 $. | Both ads sell only the warehouse plan (car 160 $, moto 80 $). Break-even is 3.60 / 2.88 $ for a heated car and 1.80 / 1.44 $ for a moto, at 5% / 4% (§4c). The moto cap of 1.80 $ assumes 5%; re-check it after 15–20 moto clicks (§6). Two groups stay as they are because their ads lead with the at-home 270 $ offer: EN Winter car storage (4.00 $) and EN Motorcycle & ATV (2.50 $). For those, a car at home breaks even at 6.66 $ (4%), and a 50/50 at-home/warehouse mix at about 4.77 $. | 0 $ (1 and 5 impressions, 0 clicks) | Prevents overpaying once these groups get clicks. Moto will win fewer auctions (it already loses ≈90% to rank). | API | Yes |

**F11 (6): where "conteneur/container" appears on the booking pages**
- The EN `<title>`, og:title and meta description: "Mobile Storage Container Rental : Book Your MobilCube" / "Easily book your mobile storage container…".
- The storage-mode radio options: "Le conteneur reste sur mon terrain", "Je viens remplir mon conteneur…" / "The container stays on my property", "I will pack my container…".
- The count question: "De combien de conteneurs… / How many containers…".
- The footer disclaimer: "Nos conteneurs réels respectent… / Our physical containers…".
- The logo alt text, which describes a heron carrying a "20-foot shipping container".

The same disclaimer says "nos visuels sont générés par IA / our visuals are AI-generated". The line is honest, but on the page where a prospect decides to book it can lower trust. The fix is real photos of the unit; drop the line once the AI visuals are gone, not before.

**Not doing now, on purpose** (the reviewers refuted or weakened these):
- No pause of "location d'entreposage". Its junk is mostly partner traffic and is covered by F2 and F5; 25.04 $ of its 26.22 $ is hidden, so judge it on Google rows after F2.
- No bid cut on "espace d'entreposage à louer": its only Google click was the best one, "mini entrepot beloeil".
- No cut to EN Mobile storage's 5.00 $ bids before the docs/09 trigger (§6).
- No budget cuts on Terrasse or patio before Nov 15.
- No cuts to car bids in groups that lead with the at-home 270 $ offer (FR Auto hiver, EN Winter car storage, EN Motorcycle & ATV). The only vehicle cuts are the two warehouse-only groups in F13.
- No device or hour adjustments.

---

## 3. Negative keywords to add (consolidated and checked)

**Check performed** (script `fix/negcheck2.py` in the audit session scratchpad, not in the repo):
- 141 unique keyword/match pairs (250 campaign and ad-group placements) were tested against:
  - all 473 rows of `ads/google-ads-editor/03-keywords.csv` (enabled and paused);
  - the 12 keywords added in §4d;
  - the 331 live keywords of the five campaigns saved in `live-structure-pm/`;
  - the live/api-spec negatives;
  - the 93 city names in `ads/geo/zone-2026-10-07.json`.
- Matching was raw, accent-folded, and accent- plus plural-folded.
- **Result: 0 conflicts with a positive keyword, 0 duplicates of an existing negative, 0 city conflicts.** An independent reviewer check (`critic/negcheck.py`, `critic/addcheck.py`) found the same for the first version of the lists.
- Applied to the search-term report, the lists together with the F1 pause cover all 7 clearly wasted clicks (14.69 $) and the ambiguous U-Haul click (4.97 $).
- The relevant searches the lists remove from a campaign are all re-routes on purpose:
  - near-me searches out of Terrasse;
  - car searches out of Entreposage mobile (H1 now, H2 in phase 2);
  - French searches out of EN;
  - "mini entrepot a louer" from the Entreposage mobile ad group to Mini-entrepôt.

Negatives do not match accents, plurals or close variants, which is why variants are listed one by one.

### A. FR | Search | Entreposage mobile: movers and trucks (campaign level, with F1)

| Match | Keywords |
|---|---|
| PHRASE | déménageur, déménageurs, demenageur, demenageurs, compagnie de déménagement, compagnie de demenagement, camion de déménagement, camion de demenagement, camions de déménagement, camions de demenagement, location camion, location de camion, location de camions, camion à louer, camion a louer, louer un camion, déménagement camion, demenagement camion, uber, simulateur, longue distance, clan panneton, déménagement tout compris, demenagement tout compris, déménagement piano, demenagement piano, déménageur piano, u haul, u-haul, uhaul |

The existing EXACT `u-haul` and `uhaul` become redundant and can stay. In French, the U-Haul searches seen were truck and cube-van rental ("location cube uhaul", "u haul lanoraie").

*Optional:* if mover searches still show 3–5 days after the F1 pause, add the specific ones as EXACT, e.g. [déménagement], [demenagement], [prix demenagement], [demenagement laval], [tarif déménagement].

### B. RV, boat and sea container

| Campaign(s) | Match | Keywords |
|---|---|---|
| FR Entreposage mobile **and** FR Terrasse commercial | PHRASE | vr, roulotte, roulottes, motorisé, motorisés, motorise, véhicule récréatif, vehicule recreatif, véhicules récréatifs, caravane, camping-car, bateau, bateaux, ponton, pontons, voilier, yacht |
| FR Entreposage mobile, FR Terrasse commercial, EN Mobile storage, EN Commercial patio, FR+EN Concurrents | PHRASE | conteneur maritime, conteneurs maritimes, sea container, sea containers, shipping container, shipping containers |
| EN Mobile storage **and** EN Commercial patio | PHRASE | rv, rvs, motorhome, camper, boat, boats, pontoon, sailboat, yacht |

The owner's rule is that MobilCube does not sell or rent shipping or sea containers. Today only "container maritime", "conteneur sea can", "seacan", "sea can", "shipping container home" and the purchase variants (à vendre, usagé) are negated. The new PHRASE "conteneur maritime" makes the first draft's EXACT [conteneur maritime 10 pieds] unnecessary.

EN Winter vehicle already has rv/motorhome/camper/pontoon/sailboat/yacht. It keeps "boat" open because of its paused Boat & PWC groups.

Size words (20 ft, 20 pieds, 10 pieds, m3) stay open because they block real keywords (see "Do NOT add").

### C. FR | Search | Terrasse commercial: consumer near-me searches and warehouse leasing

| Match | Keywords |
|---|---|
| PHRASE | à proximité, a proximité, a proximite, autour de moi, mini entrepot, mini entrepôt, mini entrepots, mini entrepôts, entrepot a louer, entrepot à louer, entrepôt a louer, location entrepot, location entrepôt, location d entrepôt, location d entrepot |
| EXACT | [location d'entrepôt], [entrepot location] |

The near-me searches then fall to FR Entreposage mobile, where the mini-storage ad and price fit them.

### D. EN | Search | Mobile storage

| Match | Keywords |
|---|---|
| PHRASE | moving boxes, cardboard boxes, crates, refrigerated, reefer, side doors, warehouse for rent, warehouse for lease, entrepot, entrepôt, entreposage, prix, à louer, a louer |
| EXACT | [u haul storage boxes], [container price], [container prices], [pods com], [pods.com] |

The French words keep French searches on the French ads (the docs/06 rule). They also block "entrepôt à louer longueuil", which EN [storage longueuil] served as a close variant.

The first draft's PHRASE "storage boxes" is dropped: it would also block searches such as "portable storage boxes", a product-type search. The first draft's EXACT [sea container with side doors] is now covered by list B.

### E. EN | Search | Commercial patio

| Match | Keywords |
|---|---|
| PHRASE | cushions, cushion, refrigerated, side doors, warehouse for rent, warehouse for lease |
| EXACT | [price of 20 ft container] |

### F. Out-of-area towns

| Campaign(s) | Match | Keywords |
|---|---|---|
| All 7 non-brand: FR Entreposage mobile, FR Vehicules hiver, FR Terrasse commercial, EN Mobile storage, EN Winter vehicle, EN Commercial patio, FR+EN Concurrents | PHRASE | shawinigan, malbaie, lachute |
| The 4 delivery campaigns: FR Entreposage mobile, FR Terrasse commercial, EN Mobile storage, EN Commercial patio | PHRASE | sorel, tracy, bromont, waterloo, lanoraie |
| EN Mobile storage, EN Winter vehicle, EN Commercial patio (the FR lists already have these) | PHRASE | sherbrooke, drummondville, trois-rivières, trois-rivieres, trois rivieres, joliette |

None of the five border-town words appears in any keyword or in the 93 cities. They replace the first draft's EXACT [entreposage sorel], [mini entrepot bromont] and [entrepot a louer waterloo].

They stay open in FR Vehicules hiver and EN Winter vehicle, because a vehicle owner can drive to the Boucherville warehouse.

### G. FR | Search | Entreposage mobile: "entrepôt à louer" (with F7, in the same UI session as the removal of the campaign-level PHRASE)

| Level | Match | Keywords |
|---|---|---|
| Campaign | EXACT | [entrepôt à louer], [entrepot a louer], [entrepot à louer], [entrepôt a louer] |
| Ad group: the 7 original groups (Conteneur d'entreposage, Cube d'entreposage, Entreposage mobile, Mini-entreposage mobile, Rive-Sud (géo), Déménagement & rénovation, Géo Montréal Laval couronnes) | PHRASE | entrepot a louer, entrepot à louer, entrepôt a louer (they already hold "entrepôt à louer") |
| Ad group: Grand Montréal (géo) and Montérégie (géo) (no ad-group negatives today) | PHRASE | entrepôt à louer, entrepot a louer, entrepot à louer, entrepôt a louer |

Do not add these to Mini-entrepôt, which must be able to serve [mini entrepot a louer] and [mini entrepôt à louer].

### H. FR | Search | Entreposage mobile: vehicles

| Phase | Match | Keywords |
|---|---|---|
| **H1, phase 1 (now, with F8)** | PHRASE | entreposage auto, entrepot auto, entreposage voiture, entreposage de voiture, entreposage automobile, auto hiver, voiture hiver, voiture pour l hiver, pour auto |
| **H2, phase 2** (about 10-12, only after F8 + F9 phase 1 show higher FR Vehicules hiver impression share) | PHRASE | voiture, voitures, automobile, automobiles, véhicule, vehicule, véhicules, vehicules, moto, motos, garage chauffé, garage chauffe |

H1 covers 8 of the 9 misrouted car searches; H2 adds "garage chauffé à louer rive sud".

### Do NOT add (each would block customers)

| Proposed somewhere | Why not |
|---|---|
| bare `camion`, `camions` | Blocks "déménager sans camion", the ad group's own pitch, and pickup-truck winter storage |
| bare `piano`, `tout compris` | Blocks "entreposage piano" and all-inclusive-price storage searches |
| bare `déménagement` / `demenagement` | Kills the 15-keyword moving segment ("entreposage déménagement", …) |
| bare `auto` | Blocks "auto-entreposage", the Quebec word for self-storage |
| `20 ft`, `20ft`, `20 pieds`, `10 pieds`, `m3`, `price of` | The unit is 20 ft (33.5 m³). "20 ft storage container rental" and "price of storage" are keywords. |
| bare `boxes`, or `storage boxes` as PHRASE | Would block searches such as "portable storage boxes" (a product-type search; it is not a keyword in 03-keywords.csv) |
| `pods` PHRASE | Blocks the keywords "storage pods", "storage pod rental" and "storage pods montreal" |
| `u haul` / `uhaul` PHRASE in **Concurrents** | Blocks its keywords "u box uhaul" and "uhaul ubox" |
| `farnham`, `estrie`, `drummond`, `lanaudière` | Farnham is served. Granby and Farnham have been in the Estrie region since 2021. Rue Drummond is in Montréal, and "drummondville" is already negated. Repentigny, Terrebonne, Mascouche and Lavaltrie are in Lanaudière. |
| `sorel`, `tracy`, `bromont`, `waterloo`, `lanoraie` in FR Vehicules hiver / EN Winter vehicle | A vehicle owner can drive to Boucherville. Revisit if these searches get clicks with no leads (§6). |
| `bateau` in FR Vehicules hiver | Would block the keywords of its paused boat groups |

**Owner decision: U-Haul/PODS in EN Mobile storage.** PHRASE `u haul`, `uhaul`, `u-haul` and EXACT [pods] are checked: they block no keyword. But "rental pods", "pod rental" and "u haul storage" are buyers of the same product type. Recommended order:
1. Add PHRASE "u haul storage" and "uhaul storage" in FR+EN Concurrents > Competitors EN, at 1.60–2.00 $.
2. Then add the negatives.

Until then, list D catches the supply searches seen so far: [u haul storage boxes], "moving boxes", "cardboard boxes" and "crates" (the last one catches "uhaul crates for moving").

---

## 4. Budget and bid changes

### 4a. Daily budgets (CAD/day). The total stays at 149 $ at every step.

| Campaign | Now | Step 2 (≈10-11 to 10-13, conditional) | Step 3 (after Nov 15, conditional) |
|---|---:|---:|---:|
| FR Entreposage mobile | 50 | **54** | **63** |
| FR Vehicules hiver | 45 | 45 | 45 |
| FR Terrasse commercial | 12 | 12 | **5** |
| EN Mobile storage | 15 | 15 | 15 |
| EN Winter vehicle | 12 | 12 | 12 |
| EN Commercial patio | 4 | 4 | **2** |
| FR+EN Concurrents | 8 | **4** | 4 |
| FR+EN Marque | 3 | 3 | 3 |
| **Total** | **149** | **149** | **149** |

- **Now: no budget change.** First fix the traffic (F1–F5). Unused Manual-CPC budget costs nothing.
- **Caps are not spend.**
  - Concurrents spends about 0 $/day and EN Commercial patio about 2 $/day, while FR Entreposage mobile always spends its full cap.
  - So Step 2 raises real spend by about 4 $/day, and Steps 2 + 3 together by about 6 $/day, even though the caps still add up to 149 $.
- **Pacing.** Google may spend up to 2× a daily budget on one day, but not more than 30.4× it in a month.
  - On 10-07 Terrasse spent 17.48 $ on a 12 $ budget (146%), FR Entreposage mobile 113% and EN Mobile storage 115%.
  - The morning report paces month-to-date spend per campaign against 30.4 × its daily budget (account: 4,530 $/month).
- **Step 2:** apply only if, after 3–5 days with partners off and F1 done, all of these hold:
  - FR Entreposage mobile still loses more than 30% of impressions to budget on Google Search;
  - its search terms are clean;
  - it has at least 1 lead, or has not yet hit its 180 $ alarm checkpoint (§6).
- **Step 3:** apply only if the terrace and restaurant keywords still have about 0 impressions after the Nov 15 borough deadline.
- **If FR Vehicules hiver starts hitting its 45 $ cap** after F8, protect it first and take the money from FR Entreposage mobile.

### 4b. Bid changes (Manual CPC, max CPC in CAD)

| Campaign > Ad group | Keyword | Match | Now | New |
|---|---|---|---:|---:|
| FR Entreposage mobile > Déménagement & rénovation | déménagement et entreposage | PHRASE | 3.50 | **Paused** (EXACT stays at 2.80) |
| FR Entreposage mobile > Déménagement & rénovation | déménagement entreposage | PHRASE | 2.80 | **Paused** (EXACT stays at 2.80) |
| FR Terrasse commercial > Commercial saisonnier & inventaire | entreposage pour entreprise | PHRASE | 3.15 | **Paused** |
| FR Vehicules hiver > Auto hiver | entreposage voiture hiver prix | EXACT + PHRASE | 2.40 | **2.85** |
| FR Vehicules hiver > Auto hiver | entreposage auto hiver | EXACT + PHRASE | 2.25 | **2.65** |
| FR Vehicules hiver > Auto hiver | entreposage voiture hiver | EXACT + PHRASE | 2.25 | **2.65** |
| FR Vehicules hiver > Auto hiver | entreposage voiture | EXACT | 2.34 | **2.74** |
| FR Vehicules hiver > Auto hiver | entreposage auto | EXACT | 1.75 | **2.20** |
| FR Vehicules hiver > Auto hiver | remisage auto | EXACT | 2.02 | **2.42** |
| FR Vehicules hiver > Auto hiver chauffé | entreposage auto chauffé | EXACT / PHRASE | 2.40 / 2.48 | **2.80 / 2.85** (+0.40 / +0.37, capped) |
| FR Vehicules hiver > Moto hiver (F13) | entreposage moto hiver | EXACT + PHRASE | 2.00 | **1.80** |
| FR Vehicules hiver > Moto hiver (F13) | remisage moto | EXACT | 2.00 | **1.80** |
| EN Winter vehicle > Heated car storage (F13) | indoor car storage montreal | EXACT + PHRASE | 4.00 | **2.85** |

**Unchanged on purpose:**
- "location d'entreposage" PHRASE 3.50 and "espace d'entreposage à louer" PHRASE 3.50 (watch list).
- The EN Mobile storage 5.00 $ bids, until the docs/09 trigger around 10-21.
- EN Winter car storage 4.00 $ and EN Motorcycle & ATV 2.50 $. Their ads lead with the at-home 270 $ offer. Do not raise them.
- The other FR moto bids (1.34–1.80 $; no clicks to judge).
- Concurrents and Marque.
- The 150 new exact keywords that have not served yet (budget, not bids, is the limit; re-check 10-15).
- prix entreposage voiture (30 searches/mo), remisage auto hiver (50) and entreposage auto hiver prix (70): too little volume to move.

### 4c. Break-even reference

Rule: ad cost ≤ 25% of first-season revenue, and 30% of leads book.

| Product | Booking value | Max cost per lead | Break-even CPC at 5% / 4% click→lead |
|---|---:|---:|---:|
| Mobile / moving unit, 3 months (350 $ × 3 + 300 $ delivery) | 1,350 $ | 101 $ | 5.06 $ / 4.05 $ |
| Same, counting pickup (+300 $), as the at-home car and terrace rows do | 1,650 $ | 124 $ | 6.19 $ / 4.95 $ |
| Car, heated warehouse (160 $ × 6) | 960 $ | 72 $ | 3.60 $ / 2.88 $ |
| Motorcycle, warehouse (80 $ × 6) | 480 $ | 36 $ | 1.80 $ / 1.44 $ |
| Car at home (270 $ × 6 + 300 $ delivery + 300 $ pickup) | 2,220 $ | 166.50 $ | 8.33 $ / 6.66 $ |
| Terrace (289.75 $ × 6 + 2 × 300 $) | 2,338.50 $ | 175 $ | 8.77 $ / 7.02 $ |

- **Mobile value.** The first draft used docs/03's 1,200 $ mobile value ("3 months at 300 $ + 300 $ delivery"). No 300 $/month price exists any more (350 / 270 / from 180 $). The §6 thresholds use the conservative 101 $ row.
- **Click→lead rate.** docs/03 planned 7% click→lead. This report plans at 4% (5% base): the 2025 storage benchmark is 4.65%, and the booking form is long (F11). At 7%, every break-even CPC would be 75% higher than at 4%.
- **Stale docs.** docs/09 §6 and docs/08 §7 still give 8.33 $ for every car. They need the warehouse rows added and the mobile value updated.

### 4d. Keywords to add (API)

| Campaign > Ad group | Keyword | Match | Max CPC | Searches/mo |
|---|---|---|---:|---:|
| FR Vehicules hiver > Auto hiver | entreposage auto | PHRASE | 2.20 | covers "entreposage auto greater montréal" etc. |
| FR Vehicules hiver > Auto hiver | entreposage voiture | PHRASE | 2.40 | covers "entreposage voiture à proximité" etc. |
| FR Vehicules hiver > Auto hiver | entreposage de voiture pour l hiver | EXACT | 2.40 | 50 |
| FR Vehicules hiver > Auto hiver | entreposage de voiture | EXACT | 2.40 | 50 |
| FR Vehicules hiver > Auto hiver | entreposage auto hiver montréal | EXACT | 2.40 | 20 |
| FR Entreposage mobile > Mini-entrepôt | mini entrepot a louer | EXACT | 2.41 | 70 |
| FR Entreposage mobile > Mini-entrepôt | mini entrepôt à louer | EXACT | 2.41 | 140 (after the F7 UI step) |
| FR Entreposage mobile > Mini-entrepôt | prix location mini entrepot | EXACT | 2.41 | 140 |
| FR Entreposage mobile > Rive-Sud (géo) | mini entrepot beloeil | EXACT | 2.80 | 40 |
| FR Entreposage mobile > Grand Montréal (géo) | entreposage repentigny prix | EXACT | 2.50 | 40 |
| FR Entreposage mobile > Conteneur d'entreposage | location conteneur entreposage prix | EXACT | 2.08 | 20 |
| FR Entreposage mobile > Entreposage mobile | location d'entreposage | EXACT | 2.80 | 30 (prepares a possible pause of the PHRASE) |

All 12 were checked: none already exists with that match type, and none is blocked by an existing or proposed negative, except [mini entrepôt à louer]. That one is blocked by the existing campaign PHRASE "entrepôt à louer" until the F7 UI step.

**Not added on purpose:**
- "remiser un véhicule": in Quebec this mostly means the SAAQ registration procedure.
- "cube de déménagement à louer": usually means a cube-truck rental.
- "heated car storage" and other terms at 10/mo or with no Planner data: they were removed on 10-07 for low volume.

---

## 5. Measurement gaps that prevent judging ROI

| # | Gap | Steps |
|---|---|---|
| M1 | **Booking and tel: conversions have not been tested end to end.** GTM v3 holds two Google Ads conversion tags:<br>• "Réservation" (AW-18484934240 / cdedCLmly5QdEODspu5E on `wpforms_envoi_reussi`);<br>• a tel: click tag (label xBaTCPXe1ZQdEODspu5E on `gtm.linkClick` when the click URL starts with `tel:`).<br>Both booking pages carry tel: links (the header phone icon and the footer call button). 0 conversions cannot yet be told apart from a broken tag. | 1. In GTM > Versions, note when v3 was published and compare it with the first ad click (10-07 about 09:00). Clicks before publication could not convert.<br>2. Open `/fr/formulaire-reservation/` **directly** (never through an ad) in GTM Preview / Tag Assistant. Accept cookies and submit a "TEST" request.<br>3. Confirm the Réservation tag fires after `wpforms_envoi_reussi`, and that the Network tab shows a `googleadservices.com/pagead/conversion/18484934240` request carrying label `cdedCLmly5QdEODspu5E`.<br>4. Tap the header phone icon and the footer button: the tel: tag must fire with label `xBaTCPXe1ZQdEODspu5E`. In Goals > Conversions, confirm that this label belongs to "Clic téléphone sur le site" (7827976053). The API lists that action as type CLICK_TO_CALL and does not show its label.<br>5. Repeat on `/en/booking-form/`.<br>6. Tell the owner to ignore the TEST email.<br>7. In Goals > Conversions, only "Unverified / Inactive / Misconfigured" are red flags. "No recent conversions" is normal until a real ad lead arrives. |
| M2 | **No independent lead count.** The site runs WPForms Lite, which has no Entries list. | Owner: count the form-notification emails (spam folder included) and the calls on 450-641-6498 since 2026-10-07 09:00. Note the time and page of each, and ask callers how they found MobilCube. If the owner reports 0 emails and 0 calls by 10-10, raise the warning early. |
| M3 | **Calls.** 70 call impressions and 0 ad-call clicks. Call reporting cannot be confirmed through the API. The site number is fixed (no forwarding swap). The call asset has no schedule. It is attached to all 8 Search campaigns, EN Commercial patio included (live pull). 0 call impressions on that campaign's 3 impressions prove nothing. | 1. Confirm Admin > Account settings > Call reporting is ON, and that "Appel depuis l'annonce" uses 45 s and 60 $.<br>2. Add a call-asset schedule for staffed hours (e.g. 8:00–20:00).<br>3. Optional: website call tracking with a number swap. It needs the owner's agreement, and under denied-by-default consent it reaches few visitors. |
| M4 | **Conversion-action hygiene.** 9 actions are enabled, and their primary/secondary status cannot be read through the API. | In Goals > Conversions:<br>• Keep **Primary**: "Réservation - formulaire" and "Appel depuis l'annonce".<br>• Check in the UI whether "Clic téléphone sur le site" (a tel: tap) is Primary or Secondary, and set it to **Secondary**: taps are reported as call intent, not optimised as leads.<br>• Set "Clicks to call" (Google-hosted, many-per-click) and "Local actions - Directions" to **Secondary**.<br>• Leave the 4 Smart-campaign actions as they are: they record nothing while the Smart campaign is paused. |
| M5 | **Consent Mode undercount.** CookieYes denies everything by default (correct for Law 25), and URL passthrough is off in both CookieYes and the GTM Conversion Linker. Visitors who refuse cookies are not observed, and the account is far too small for Google to model them. | 1. Read the CookieYes accept rate.<br>2. Treat URL passthrough as an owner / privacy-officer decision (and a line in the privacy policy). If approved, switch it on in **one** place only.<br>3. Correct cost per lead with the ratio of owner-counted leads (M2) to tracked leads. |
| M6 | **No engagement data in the report.** The GA4 source (GAWA) is not authenticated in Supermetrics. GA4 G-640H58NDHN is loaded twice, so page views are doubled. CookieYes loads twice and Clarity three times. | 1. Authenticate GA4 in Supermetrics and confirm the GA4 ↔ Ads link.<br>2. Keep one Google tag, removing either the MonsterInsights copy or the manual one.<br>3. Remove the manual CookieYes script and keep the plugin copy, which follows `_ckyGcm`.<br>4. Keep one Clarity, loaded after consent.<br>5. Re-test both AW tags afterwards. Do not import GA4 key events as Primary. |
| M7 | **No gclid on the form** (needed later for an offline "booked job" import). | Later: add a Single Line Text field, hidden with CSS and filled by JavaScript from `gclid` (LiteSpeed caches the page, so it must be client side). Mention the click ID in the privacy policy first. |
| M8 | **The docs contradict the account.** docs/09 says partners are off, the break-even table is stale, and docs/03 still uses the 1,200 $ mobile value and a 7% click→lead rate. | 1. After F2, correct docs/09 l.138 and §6, docs/08 §7 (§4c values) and docs/03 (inputs table).<br>2. Add "untick search partners" as a manual step after any future API recreation. |

**Audiences and recommendations (pulled, nothing to act on yet):**
- All 7 remarketing lists have size 0. Consent is denied by default and the tag is one day old, and Search lists need 1,000 users before they can be used.
- Google shows no recommendations for the account.

**What the morning report counts as a lead:** form submissions plus ad calls of at least 45 s. tel: taps are shown on a separate line as call intent. CPC, conversion rate and cost per lead are computed on **Google Search only**. Budget pacing is month-to-date spend per campaign against 30.4 × its daily budget.

---

## 6. Watch list (too early to judge)

**Two checkpoints per segment, counted on Google Search spend only:**
- **Alarm** = 3× the docs target cost per lead with 0 leads. At the alarm, stop adding budget and audit the form and tags.
- **Wasting (95%)** = spend of at least the allowable cost per lead × 3.0 / 4.7 / 6.3 / 7.8 / 9.2 for 0 / 1 / 2 / 3 / 4 leads. When reached, lower that **ad group's** bids by 30% (docs/09 rule). Do not pause the campaign. For mobile storage the allowable cost per lead is 101 $ (124 $ if pickup is counted, which moves the 0-lead threshold from 304 $ to 371 $).

| Segment | Alarm (0 leads) | Wasting (0 leads) | Expected date |
|---|---:|---:|---|
| Account | — | 304 $ (≈94 Google clicks at 3.22 $) | ≈10-10 to 10-12 |
| FR Entreposage mobile / generic storage | 180 $ | 304 $ | ≈10-12 to 10-14 |
| FR Vehicules hiver, car (alarm at campaign level) | 216 $ | by ad group, see the next two rows | ≈10-20 to 10-30 at 10–20 $/day after F8 |
| Heated-warehouse car groups (Auto hiver chauffé + EN Heated car storage, pooled) | — | 216 $ | November |
| At-home car, ATV and snowmobile groups (incl. EN Winter car storage, EN Motorcycle & ATV) | — | ≈500 $ | November |
| Moto hiver | — | 108 $ | weeks |
| EN Mobile storage | 255 $ | 304 $ | ≈10-21 to 10-26 |
| True terrace searches | — | ≈525 $ | after Nov 15 |

**Plan targets (docs/03) against the first 1.5 days:**

| docs/03 target | Target | Now | Note |
|---|---|---|---|
| Search-term waste (spend on terms later negated) | ≤ 8% of spend | 12.7% clear waste; 17% counting the U-Haul click that list D negates | F1, F3, F4 |
| Search top impression share, vehicle + terrace groups, weeks 43–48 (from Oct 19) | ≥ 75% | FR Vehicules hiver 20%, FR Terrasse commercial 14% (campaign level) | The target window opens Oct 19. F8 is the lever for vehicles. |
| Quality Score on core exact keywords | ≥ 7 | Highest seen is 5 (11 keywords have a QS, from 1 to 5) | Landing page "Below average" on 11 of 12 (F11) |
| Click → lead | 7% (plan) | Not measurable yet; this report plans at 4% (5% base) | §4c |
| Cost per lead | ≤ 60 $ FR, ≤ 85 $ EN | No leads yet | Alarms at 3× (180 $ / 255 $) |

| Item | Now | Threshold → action | Re-check |
|---|---|---|---|
| "entreposage déménagement" PHRASE 2.80 $ (it can absorb mover matches after F1) | kept | >50% of its visible search terms are movers → pause the PHRASE, keep the EXACT | 10-11 |
| "location d'entreposage" PHRASE 3.50 $ | 83 impr / 13 clicks / 26.22 $. 10 of 13 clicks came from partners (keyword × network pull, `keywords_by_network_fresh.txt`). 25.04 $ of its cost is in hidden terms. About 57% of visible impressions were relevant. | On Google Search rows after F2 and F5: <50% relevant, or cost per lead >85 $ → pause the PHRASE (the EXACT is added in §4d) | 10-15 |
| "espace d'entreposage à louer" PHRASE 3.50 $ | 32 impr / 4 clicks / 7.79 $; its only Google click was "mini entrepot beloeil" | Google CPC >3 $ **and** off-target >30% → 2.80 $ | 10-15 |
| EN Mobile storage 5.00 $ bids (7 keywords) | 4 clicks, CPC 4.33 $. 5.00 $ is at break-even at 5% without pickup (5.06 $) and at 4% with pickup (4.95 $). It is above break-even at the 4% planning case without pickup (4.05 $). | docs/09 rule: cost per lead >85 $, or 0 leads at about 255–304 $ → 4.00 $, which is under break-even in every case. The owner may cap at 4.05 $ earlier as a budget stretch. | 10-21 |
| EN PHRASE "portable storage containers", "moving and storage containers", "storage pod rental" | 3–10 impr each | Decide pause or EXACT only after about 100 impressions each with list D in place | 10-22 |
| 150 of 164 new EXACT keywords not serving yet | FR Entreposage mobile budget goes to phrase keywords | Mini-entrepôt <50 impr/week → [mini entrepôt]/[minientrepot] 3.00 → 3.50 $. A geo group <20 impr/week → +0.30 $ on its keywords with ≥140 searches/mo. | 10-15 |
| FR Vehicules hiver after F8 and H1 | IS 25%, rank-lost 75% | Campaign-level IS and rank-lost improve → apply list H2 (phase 2). If not, review bids against Planner ranges, not top-of-page estimates (unreliable at this volume). | 10-12, then 10-15 |
| Terrasse's remaining PHRASE keywords ("entreposage commercial montréal" 3.50, "entreposage inventaire", "entreposage saisonnier", "conteneur entreposage commercial") | quiet | Picking up "entrepôt à proximité"-type searches → add negatives. Terrace keywords ~0 impr after Nov 15 → budget Step 3. | 10-13; Nov 16 |
| Search partners (after F2) | off | Compare Google-only cost per form. Re-test partners only as an experiment after 30 or more conversions. | 10-22 |
| Border towns in the vehicle campaigns (sorel/tracy, bromont, waterloo, lanoraie, estrie in FR Vehicules hiver / EN Winter vehicle) | 0 $, open on purpose (the delivery campaigns now negate them, list F) | Clicks with no leads → PHRASE negatives in the vehicle campaigns too | 10-14 |
| Named facilities (bluebird, mini entrepôts du tremblay, b c g m, chemin larocque, farnham route 104) | 0 $ | Add an EXACT negative only once one gets a click | 10-14 |
| Size searches ("conteneur 10 pieds", "conteneur 20 pieds volume en m3") | 0 $, kept open (size words block real keywords; sea-container searches are now negated, list B) | A click → EXACT negative for that exact search | 10-14 |
| Off-target close variants of EXACT keywords: "remiser un véhicule" (SAAQ) on [remisage auto] | 1 impr, 0 $ | A click → EXACT [remiser un véhicule] and [remiser un vehicule] in FR Vehicules hiver | 10-15 |
| "stationnement" / "parking" negatives in FR Vehicules hiver / EN Winter vehicle (they block "stationnement intérieur chauffé hiver") | deferred | Planner ≥20 searches/mo for a winter/heated parking term → narrow the negatives at campaign level and in all 9 ad-group copies | after the first conversions |
| Motorcycle bids (FR up to 1.80 $ after F13; EN Motorcycle & ATV 2.50 $; ≈90% lost to rank) | 0 clicks | After 15–20 moto clicks: if the moto click→lead rate is under 5%, cap FR at 1.44 $ (4% break-even). The EN group sells at-home storage at 270 $ first, so judge it with the at-home groups (≈500 $). | November |
| EN Winter car storage 4.00 $ (at-home offer first) | 1 click at 3.77 $; EN Winter vehicle spends ≈4 $/day | Judge it with the at-home car groups: ≈500 $ of Google spend with 0 leads → 3.50 $. EN Heated car storage drops to 2.85 $ in F13 and is pooled with the FR heated-car groups (216 $). | November |
| Concurrents (1 impr), Marque (0) | Idle, costs nothing. Concurrents is idle for a visible reason. Its campaign EXACT negatives block the bare competitor names (u-haul, uhaul, cubeit, gocube, go cube, pods, public storage, depotium). Its 18 keywords are long-tail, 17 of them EXACT, at 1.13–2.50 $. | <20 impr/week → decide whether competitor bidding is worth testing. A test would need PHRASE competitor keywords and higher bids. | 10-22 |
| FR Entreposage mobile Google CTR 4.3% | noise | At ≈1,000 Google impressions, check by ad group. If "Déménagement & rénovation" is <5%, test a "350 $/mois sans engagement" headline there. | ≈10-13 |
| Ad copy: Rive-Sud / Grand Montréal geo RSAs (ad relevance Below average); Conteneur / Portable container headlines; 160 $ vs 270 $ lead headline; "motomarine / jet ski" in 6 vehicle ads | low volume | New geo RSAs, all headlines ≤30 characters (e.g. "Mini-entrepôt Rive-Sud", "Entreposage à Longueuil", "Varennes, Brossard, Longueuil"). Ask the owner whether jet skis are accepted. | 10-22 |
| 12 clicks (32.67 $) that did not land on the booking form: 11 sitelink clicks (31.23 $) to the pricing and capacity pages, plus 1 click (1.44 $, "simulateur prix déménagement") on removed ad 826607307838, whose final URL was /fr/prix-location/ | not waste | Make sure a "Réserver / Book now" button sits above the fold; judge after 2 weeks | 10-22 |
| Device, hour and border-town location leakage (L'Épiphanie, Sainte-Anne-des-Plaines, Mirabel: 2.89 $) | normal | Revisit after 4 weeks and 30 conversions | 11-05 |
| Duplicates: "conteneur déménagement" PHRASE and [entrepot mobile] EXACT also sit in Conteneur d'entreposage | housekeeping | Remove those two copies | any time |

---

## 7. What is working (keep or scale)

- **Click prices.**
  - Blended CPC is 2.46 $; Google-only CPC is 2.96 $ FR (plan 3.20 $) and 4.22 $ EN (plan 5.50 $).
  - The max-CPC caps hold even where Google's top-of-page estimates run 13–38 $.
  - Invalid clicks: 3.
- **[entreposage voiture hiver prix] EXACT is the best keyword:** 9 impressions, 3 clicks (33% CTR), 7.16 $, all on Google Search, about 390 searches/mo. **Scale it (F8).**
- **A keyword in the headline works.**
  - "Auto hiver chauffé" (headline "Entreposage auto chauffé") gets ad relevance Above average and QS 5.
  - EN "Winter car storage" also rates Above average.
  - The price headlines "Entrepôt chauffé : 160 $/mois" and "Heated Warehouse: $160/mo" get the vehicle clicks.
- **Exact match is mostly clean, not perfectly.**
  - The 31 EXACT keyword rows had 61 impressions, 8 clicks and 22.00 $.
  - Their visible search terms include at least 2 off-target close variants: "entrepôt à louer longueuil" (warehouse leasing) on EN [storage longueuil], now blocked by list D, and "remiser un véhicule" (the SAAQ procedure, §4d) on [remisage auto]. The same EN keyword also served the French "entrepot longueuil".
  - The new geo EXACT keywords matched the local searches they target (entreposage longueuil prix, mini entrepôt boucherville / longueuil, entreposage varennes / valleyfield / terrebonne).
  - The first draft's "1 of 74 visible impressions" counted the 49 search-term rows with an exact-type match (74 impressions, 20.24 $). Many of those are close variants of PHRASE keywords.
- **Existing negatives work.** None of the 188 search-term rows shows jobs, buying or used, DIY, data storage, plastic bins or dumpster intent.
- **Location targeting works:** 97.5% of spend (112.84 $) came from inside the 93 towns, with no traffic from outside Quebec.
- **Ads comply.**
  - A live pull on 10-08 PM lists 38 RSAs: all 31 enabled and all 7 paused ones are Approved. 19 of the enabled ones served; `ads.txt` covers only ads with impressions (those 19 plus 4 removed ones). The 12 that have not served include Marque's.
  - No ad text says "conteneur/container". `04-responsive-search-ads.csv` has no hits outside the ad-group names "Conteneur d'entreposage" and "Portable container", and the 38 live RSAs were checked separately (0 hits).
  - Every price in the live ads matches the brief (350/270/180 $, 160/80 $, 289.75 $, delivery 300 $ with 15 km included).
- **Delivery is as planned.**
  - Ad schedules are respected and no Display traffic appears. Six campaigns run 6:00–23:00 every day; Terrasse and EN Commercial patio run 7:00–19:00 on weekdays.
  - On Google Search, phones and computers both show a 5.7% CTR at about 3.15 $ CPC.
  - 74% of clicks come from phones, as planned.
- **Tracking foundations exist.**
  - The GTM booking tag is wired correctly, and GTM v3 also holds a tel: click tag (label xBaTCPXe1ZQdEODspu5E).
  - "Appel depuis l'annonce" and "Clic téléphone sur le site" already exist.
  - The call asset is attached to all 8 Search campaigns.
  - Consent Mode v2 defaults are set before GTM loads (Law 25).
- **FR Entreposage mobile has unmet demand.** It got 307 impressions at under 10% impression share, with 68% lost to budget. It is the first campaign to scale once leads are confirmed (Step 2/3 budgets).

---

## 8. Method and data window

- **Data:** read-only Supermetrics pulls on 2026-10-08, about 09:05–09:15 Montréal time. Range 2026-10-01..10-08, timezone America/Toronto.
  - Nothing served before 2026-10-07 around 09:00. 10-08 covers 06:00–08:59 only.
  - Six campaigns had about 17 scheduled serving hours: 10-07 09:00–23:00 and 10-08 06:00–09:00. FR Entreposage mobile and EN Mobile storage stopped early on 10-07 because their budgets ran out (at 20:00 and 15:00).
  - Terrasse and EN Commercial patio run 7:00–19:00 on weekdays only, so they had about 12 hours: 10-07 09:00–19:00 and 10-08 07:00–09:00.
  - Reports pulled: campaign, daily, hourly, keyword (with QS), search terms (with and without network), device × network, user location, landing page, ads/assets, conversion actions, calls, audiences, recommendations.
  - Added in the critic round (10-08, about 11:00–11:15; still read-only):
    - a keyword × network pull (`keywords_by_network_fresh.txt`, made about 09:20, a later snapshot: 121 vs 117 impressions on "déménagement et entreposage");
    - a live structure pull: ads with status and text, ad-group negatives, keywords and bids, schedules and call assets (`live-structure-pm/`).
  - Raw files: `audit-2026-10-08/` in the audit session scratchpad (not in the repo). Its README lists every file.
  - A fresh pull while this was written showed 49 clicks / 118.68 $. The figures here use the frozen 47 / 115.73 $ snapshot.
- **Coverage:** visible search terms cover 26 of 47 clicks (65.36 of 115.73 $). The rest falls under Google's low-volume privacy threshold and is attributed by keyword in §1.
- **Audiences and recommendations:** all 7 remarketing lists have size 0, and Google shows no recommendations (§5).
- **Process:** 7 dimension analysts (search terms, keywords and QS, networks/devices/geo/hours, budget and bidding, tracking and landing page, ads and CTR, benchmarks) produced 68 findings.
  - Each finding was re-checked against the raw files by 2 independent reviewers. Their corrected actions were applied; no findings were dropped.
  - A third review (26 points) was applied on 10-08 PM; see the Reviewer notes.
  - Where reviewers disagreed, this report takes the option that blocks fewer prospects and changes less on thin data. Examples: no bare `camion` or `auto` negatives, no budget cuts before Nov 15, and broad vehicle negatives (H2) only after the vehicle campaign can win those searches. The first draft also kept sea-container searches open; the owner's rule overrides that.
  - Every waste figure that rested on 0–2 clicks was dropped or marked as not measurable.
- **Negative-list check:** the session-scratchpad script `fix/negcheck2.py` uses phrase-token and exact matching: raw, accent-folded, and accent- plus plural-folded. It tests the negatives against:
  - 03-keywords.csv (473 rows);
  - the §4d keyword adds;
  - the live keywords of five campaigns;
  - the api-spec negatives. Live campaign-level negatives match the specs exactly; the ad-group copies and "granby" are the exceptions;
  - `ads/geo/zone-2026-10-07.json`.
- **Statistics:**
  - Binomial chance of 0 leads in n Google Search clicks: 0.9535^24 = 31.9%; 0.97^24 = 48.1%. The first draft used all 47 clicks (10.7% / 23.9%), but conversion rate is measured on Google Search only.
  - Rule of three: with 0 events, the 95% upper bound on the rate is 3/n.
  - Poisson 95% stop rule: 3.0/4.7/6.3/7.8/9.2 × the allowable cost per lead for 0–4 leads.
  - The partner vs Google CTR gap (23/72 vs 24/415) is significant (p < 1e-8), but its value is unknown. The gap in visible waste share between partners and Google is not significant (Fisher p ≈ 0.4).
  - Keyword-level impression share, QS and asset CTR from 1–10 impressions were treated as noise.
- **Benchmarks (US, converted at 1.38 USD/CAD):**
  - LocaliQ 2025 Home Services, Storage: CTR 8.32%, CPC 7.46 USD, conversion rate 4.65%, cost per lead 120.30 USD.
  - LocaliQ 2026, all industries: CTR 6.64%, CPC 5.42 USD.
  - No Quebec-specific storage benchmark was found.
  - Planning case for the morning report: 4% click→lead (5% base), 30% lead→booking. docs/03 planned 7%; see §4c. Replace with the account's own rate after about 15 leads.
- **No change was made to the account.** Every action above is for the owner to approve. "API" means the change can be made through the connector; "UI" means it needs the Google Ads web interface or Editor.

---

## Reviewer notes

A third reviewer raised 26 points on 10-08 PM. Each was re-checked against the raw files, the repo and a new read-only live pull before it was applied.

**Applied as raised:** points 1, 2, 3, 5, 6, 8, 10, 13, 14, 15, 16, 17, 19, 20, 21, 22, 23, 24 and 25.

- **Point 5 (F3 classification):** F3 is now "0 $ waste, 9.09 $ misrouted", which matches §1.
- **Point 18 (call asset):** applied, and settled rather than deferred to a UI check. The live pull shows the call asset attached to EN Commercial patio, so the "missing" claim is removed.
- **Point 26:** it confirms the figures and needs no change.

**Applied with an adjustment:**
- **Point 4 (network split).** The table is applied, with one more column for the ambiguous U-Haul click (point 7).
  - With that click moved out of Google's waste, the visible waste share is 19% on Google and 33% on partners, not 29% vs 33%.
  - On 15 and 11 visible clicks the gap is not significant (Fisher p ≈ 0.4). So the reviewer's conclusion stands: the case for turning partners off rests on the plan and the CTR anomaly.
- **Point 7 (U-Haul click).** The reviewer offered two options; both are applied.
  - The 4.97 $ is marked ambiguous, so clear waste is 14.69 $ (12.7%).
  - List D uses [u haul storage boxes] EXACT plus "moving boxes" and "cardboard boxes" instead of PHRASE "storage boxes".
- **Point 9 (account threshold).** Superseded by point 10. The account threshold is now 304 $, about 94 Google clicks at 3.22 $. The reviewer's 84-click figure was right for 270 $.
- **Point 11 (vehicle bids).**
  - The F8 cap is 2.85 $, and remisage auto goes to 2.42 $ (+0.40).
  - EN Heated car storage (4.00 → 2.85 $) and the two FR moto bids at 2.00 $ (→ 1.80 $) are flagged and cut in F13. Their ads sell only the warehouse plan.
  - EN Winter car storage (4.00 $) and EN Motorcycle & ATV (2.50 $) are justified by their at-home 270 $ lead offer and kept.
- **Point 12 (car searches).** The core point is right and is applied: phase-1 list H1 now covers 8 of the 9 car searches. The count needs one correction.
  - 3 of the 9 car searches match FR Vehicules hiver keywords syntactically ("… hiver montréal", "… hiver rive nord", "entreposage voiture hiver prix").
  - The fourth search the reviewer lists, "entreposage auto hiver estrie", is not one of the 9. It is classed out of area, and it matched both campaigns.
  - One of the 9, "entreposage de voiture pour l hiver", was also served once by FR Vehicules hiver, as a close variant.

**Small inaccuracies in the review (no effect on the actions):**
- **Point 1:** besides "container maritime", "seacan" and "sea can", the live lists also hold "conteneur sea can", "shipping container home" and the "à vendre / usagé" variants. None of them is a plain "conteneur maritime" or "sea container" PHRASE, so the addition stands.
- **Point 2:** the five border-town negatives are applied to the four delivery campaigns as asked. They are not applied to Concurrents. It is idle, and its competitor keywords mix delivery and warehouse intent.

**Not applied:** none. No point was found to be invalid.

Check scripts: `fix/negcheck2.py`, `fix/agneg.py`, `fix/v1.py` in the audit session scratchpad. The reviewer's own scripts are in `critic/`.
