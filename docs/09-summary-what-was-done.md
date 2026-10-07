# MobilCube Google Ads: what was done and what to expect

Prepared October 1, 2026; updated the same day after the campaigns were rebuilt in the new account with mini-storage ads. This file sums up the whole project in one place: the competitor analysis, how the keywords were chosen, what is now in your Google Ads account, and the results you can expect. Details sit in the other files in `docs/`.

## Update of October 7, 2026 (campaigns live)

You switched the campaigns on yourself. Sections 1 to 10 below describe the October 1 build. These are the changes since then, all applied in account 194-768-4780:

- **Keywords cleaned and expanded with real Keyword Planner data.**
  - **Removed:** 262 keywords that Google reported at 10 searches a month or fewer, which Google would not serve. Brand keywords were kept.
  - **Added:** 164 exact-match phrases of 20 or more searches a month, about 16,000 searches a month in total. Each bid is capped per ad group (1.50 $ to 3.50 $). 182 other phrases were left out because their low-range bid was above that cap.
  - **New ad groups:** 3 in FR Entreposage mobile ("Mini-entrepôt", "Grand Montréal (géo)", "Montérégie (géo)"). They were created paused and turned on at your request on October 7. Google approved their ads.
  - **Totals now:** 473 keywords (398 enabled), 38 ad groups, 38 ads. Rules and lists: `ads/keyword_expansion.py`, `ads/keywords/expansion-2026-10-07.json`.
- **Your map replaces the 45 km radius.**
  - **Cities:** the 93 cities in `ads/geo/zone-2026-10-07.json` are now targeted in 7 campaigns. They cover Montreal, Laval, the North Shore, Vaudreuil-Soulanges and the Montérégie out to Saint-Hyacinthe, Granby and Valleyfield. Marque keeps all of Quebec.
  - **Still to do by hand:** the connector can add locations but cannot delete a radius. The old 45 km circle is still on FR Entreposage mobile, FR Véhicules hiver, EN Mobile storage, EN Winter vehicle and Concurrents. FR Entreposage mobile also has a 1 km test circle around the warehouse; it adds no area, since Boucherville is already targeted. Run `scripts/google-ads/remove-radius.js` once to remove them all, or delete them in Campaigns → Locations.
  - **Presence:** the setting is on in all 9 campaigns.
- **Every ad now lands on the booking form:** `/fr/formulaire-reservation/` or `/en/booking-form/`. Sitelinks point to the prices, sizes, vehicles and patios pages.
- **New winter vehicle prices in the heated warehouse:** car 160 $/month, motorcycle 80 $/month, on a 6-month plan. Storage at home stays 270 $/month. A new French motorcycle ad was added.
- **Booking conversions are live.** The site now loads GTM-M69QW6VC, which fires "Réservation - formulaire" (AW-18484934240) when the WPForms booking form is sent. Call conversions are still to create: see `docs/10-suivi-conversions.md`.
- **Patio keywords have almost no measurable search volume.** Consider moving the 16 $/day of the two patio campaigns to retargeting.
- **Cross-platform marketing (Google retargeting, Facebook and Instagram, Microsoft Advertising):** what to switch on and in what order is in `docs/11-marketing-multiplateforme.md`.

## 1. In one minute

- **8 Search campaigns are built in your new Google Ads account (MobilCube, 194-768-4780, info@mobilcube.com), all paused.** Together they hold 35 ad groups, 571 keywords and 35 ads, with sitelinks, callouts, a call button, schedules and negative keywords. Nothing spends until you turn a campaign on.
- **The ads sell mobile mini-storage ("mini-entreposage mobile"), not containers.** Every ad says the unit is delivered to the customer's door. It then stays there with 24/7 access, or MobilCube stores it in its heated Boucherville warehouse, as PODS does.
- **Total budget: 149 $ a day, about 4,530 $ a month.** That leaves about 470 $ of your 5,000 $ for weather and deadline boosts.
- **The strategy:** fight where competitors are thin, not where they are strong. Nine companies already pay for "entreposage Montréal"-type searches. Almost nobody advertises mobile mini-storage on the South Shore, cars stored at home or in a heated unit, or restaurant terraces. Those are your first targets.
- **The first account (Mobil Cube, 209-245-0839) still holds the first 8 paused campaigns.** Remove them yourself (section 8): that account is no longer reachable from the current connection.
- **Expected first month:** about 1,500–2,000 clicks, 45–100 leads (calls and quote forms) and 14–30 bookings, worth roughly 25,000–55,000 $ in first-season revenue. These are estimates; real numbers come after two weeks of spend.
- **Before you turn anything on:** fix the first three items in section 8. Without conversion tracking, Google cannot tell which keyword brings calls, and you cannot either.

## 2. What MobilCube sells (checked on mobilcube.com)

| Item | Fact |
|---|---|
| Unit | One 20 ft CORTEN steel container, 1,165 cu ft, about 160 sq ft |
| Rent at your place | 350 $/month with no commitment; 300 / 270 / 220 / 180 $/month on 3 / 6 / 12 / 24 months |
| Rent at the heated Boucherville warehouse | Same plans + 19.75 $/month (for example 289.75 $/month on 6 months) |
| Winter vehicles in the heated warehouse (since 2026-10-07) | Car 160 $/month, motorcycle 80 $/month, on 6 months, no transport fee when you drive in |
| Delivery | 300 $ per movement, 15 km included, then 2 $/km |
| Vehicles | Accepted in the unit at the customer's home or inside the unit at the heated warehouse |
| Deposit | 200 $, refunded |
| How the ads describe it | A private mini-storage unit ("mini-entrepôt privé"), delivered, loaded at ground level, then kept at the customer's place or stored at the heated warehouse |

## 3. Competitor analysis

### Who is paying for Google Ads today

I read the tags each competitor actually has set up on its website.

| Competitor | Pays for Google Ads | Tracks calls from its site | What it pushes now |
|---|---|---|---|
| Cubeit | Yes (4 accounts) | Yes | Free local delivery, ended Sept 30 |
| Depotium | Yes | Yes | Vehicle parking |
| Access Storage | Yes | Yes | Winter car storage |
| GoCube | Yes | Yes | Old promo, expired in March |
| PODS | Yes | No | Up to 30 % off, code DERNIERE30 |
| Montreal Mini-Storage | Yes | No | −50 % for up to 6 months, plus hidden fees |
| Public Storage | Yes | No | Boat and vehicle parking |
| StorageMart | Yes | No | Online discounts |
| U-Haul | Yes | No | 1-year price lock |
| SmartStop | No | No | Online discounts |

Cubeit, Depotium and Access belong to the same owner and share ad accounts. All nine bidders fight over generic searches like "entreposage montréal", "mini entrepôt" and "storage montreal". That is where clicks cost the most and where a delivered 20 ft container is least relevant.

### Where competitors are weak

- **They hide prices.** Cubeit, PODS and GoCube publish no rent. MobilCube does, so every ad shows a price.
- **Most refuse vehicles.** Cubeit, GoCube and U-Box ban vehicles. PODS takes cars only, at its Laval site, with no motorcycles or ATVs.
- **Their yards are far away.** Cubeit is in Vaudreuil and PODS in Laval. MobilCube's heated warehouse is in Boucherville, close to Longueuil and Brossard.
- **Their units are smaller.** Cubeit uses 16 ft, PODS 8–16 ft and GoCube 5×8 ft cubes. One 20 ft MobilCube replaces about three GoCube cubes.
- **They work in English first.** Their restaurant and terrace pages exist only in English, and nobody offers a delivered terrace container in French.
- **They have many reviews and you have none yet.** Cubeit has 4.8★ on 5,000+ reviews and Montreal Mini-Storage 4.7★ on 3,100. Ask every first customer for a Google review.

### Your price against the alternatives

| Use | What the customer pays elsewhere | MobilCube | Decision |
|---|---|---|---|
| Car, heated indoor | Toyota Montréal-Nord heated parking: 475–555 $/month | 160 $/month in the heated warehouse, about 70 % cheaper | **Push hardest** |
| Motorcycle, heated indoor | Dealers and lots, a few hundred $ a season | 80 $/month in the heated warehouse (480 $ for 6 months) | Push |
| Car at home | Rented garage: 165–350 $/month | About 370 $/month with 24/7 access | Push to people without a garage |
| Two vehicles, or a car plus summer gear | Two spots, or a garage plus a locker | Same price for everything | Strongest value, leads the vehicle ads |
| Moving, renovation | Cubeit and PODS hide prices | 350 $/month + 300 $ delivery | Push all year |
| Restaurant terrace | No French competitor | 6 months on site or heated | Push before the borough deadlines |
| One motorcycle, ATV or snowmobile | Dealers and lots, a few hundred $ a season | About 2,220 $ for 6 months | Low bids only |
| Boat or jet-ski | Marinas, 835–1,420 $ a season | More expensive, and big boats do not fit | **Paused** |

## 4. How the keywords were chosen

**Source of the keywords.** Real search phrases from Google's autocomplete in Canada (59 seed words, French and English), keyword ideas Google pulled from your site and competitors' sites, and the competitor analysis above. Google's search volumes were not usable: your account has not spent yet, so Google returns rough numbers only. Real volumes arrive after the first week of spend.

**Three tiers:**

| Tier | What | Status | Why |
|---|---|---|---|
| 1 | Mobile mini-storage ("mini entreposage mobile", "mini entrepôt livré", "mini entreposage à domicile", "mobile mini storage"), mobile storage and containers ("entreposage mobile", "conteneur d'entreposage à louer", "location cube entreposage"), South Shore towns ("entreposage boucherville / longueuil / brossard / rive sud"), cars ("entreposage voiture hiver", "entreposage auto chauffé"), English equivalents, your brand | On, highest bids | High intent, few advertisers |
| 2 | Moving and renovation, motorcycles, ATVs and snowmobiles, terraces and commercial, competitor names ("pods montréal", "cubeit prix") | On, lower bids | Good intent but lower value, or high value but rare searches |
| 3 | Generic city searches ("entreposage laval", "storage west island", "storage units near me"), boats and jet-skis | Built but paused | Nine chains bid there, or the offer does not fit |

**Result:** 571 keywords; 496 are on and 75 sit in paused ad groups, ready to test. 25 mini-storage keywords were added for the new positioning: 17 French ones in their own ad group, "Mini-entreposage mobile", and 8 English ones in "Mobile storage". "Mobile mini storage" can also be a search for the competitor Mobile Mini, so check it in the first week's search terms.

**Negative keywords (searches that will never show your ad):** 331 shared plus 118 per campaign. Examples:

- Jobs: emploi, salaire, job.
- Buying instead of renting: à vendre, usagé, kijiji.
- Dumpsters, which dominate "location conteneur": benne, déchets, verges.
- Plastic bins and shelves: bac, étagère, ikea, walmart.
- Data storage: cloud, disque dur.
- Out-of-area cities: Québec, Sherbrooke, Toronto.
- Bargain hunters: pas cher, gratuit.
- Brand-only competitor searches (for example "pods" alone).
- RVs and pontoons, in the vehicle campaigns.

A script checked that no negative blocks one of your own keywords.

## 5. What is in your Google Ads account now (all paused)

Account MobilCube, 194-768-4780. Each campaign was read back from Google after the upload and matches the files in `ads/api-specs/`: keywords, bids, negatives, ad text and assets.

| Campaign | Campaign ID | Daily budget | Where it shows | When | Ad groups | Keywords |
|---|---|---|---|---|---|---|
| FR, Entreposage mobile | 24315225772 | 50 $ | 45 km around Boucherville | Every day, 6:00–23:00 | 7 (1 paused) | 188 |
| FR, Véhicules hiver | 24304113837 | 45 $ | 45 km around Boucherville | Every day, 6:00–23:00 | 9 (2 paused: boats) | 128 |
| FR, Terrasse commercial | 24315194773 | 12 $ | Montréal, Longueuil, Laval, Brossard, Boucherville | Mon–Fri, 7:00–19:00 | 5 | 33 |
| EN, Mobile storage | 24304083066 | 15 $ | 45 km around Boucherville | Every day, 6:00–23:00 | 4 (2 paused) | 92 |
| EN, Winter vehicle | 24304069128 | 12 $ | 45 km around Boucherville | Every day, 6:00–23:00 | 5 (2 paused: boats) | 53 |
| EN, Commercial patio | 24315098317 | 4 $ | Same 5 cities as FR terrace | Mon–Fri, 7:00–19:00 | 2 | 32 |
| FR+EN, Marque (your brand) | 24315068830 | 3 $ | Province of Quebec | Every day, 6:00–23:00 | 1 | 18 |
| FR+EN, Concurrents (competitor names) | 24303994035 | 8 $ | 45 km around Boucherville | Every day, 6:00–23:00 | 2 | 27 |
| **Total** | | **149 $/day** | | | **35** | **571** |

The account also holds "MobilCube" (24303770370), the Smart campaign the setup wizard created. It is paused. Leave it paused or remove it: it would compete with the Search campaigns for the same searches.

**Every campaign has:**

- Search only (no Display, no partner sites).
- Manual bids with a maximum cost per click on every keyword.
- Ads shown only to people located in the area.
- 4 sitelinks: quote, prices, vehicles, terraces.
- 6 callouts and a "Services" snippet.
- A call button to 450-641-6498.
- Tracking tags on every click.

French campaigns carry French ads, English campaigns English ads.

**Turning a campaign on:** in Google Ads, set the campaign to "Enabled". Its ad groups and ads are already on, except the paused tests (boats, generic city searches).

**Problems found and fixed during the uploads:**

- The French competitor ad group had English ads, because of a bug in the file generator. It now has French ads.
- Google refused the French headline "Le contenu d'un 5 ½ entier". It was replaced by "Assez grand pour un 5 et demi".
- In the new account Google also refused the English headline "Fits a Whole 5 ½ Apartment". It was replaced by "Room for a Whole Apartment". Avoid the "½" sign in future ads.
- The first English headline, "Mobile Mini-Storage Montreal", became "Mini-Storage in Montreal", because Mobile Mini is a competitor's brand name.

## 6. Bids and budget: why you will not overspend

Every keyword has a maximum bid, so Google can never charge more per click than the number below. The budgets are spread across 8 campaigns, so no single segment can eat the month.

| Segment | Revenue per booking | Highest ad cost you can afford (25 %) | Break-even cost per click | Maximum bids set |
|---|---|---|---|---|
| Cars, 6 months | 2,220 $ | 555 $ | 8.33 $ | 1.35–2.70 $ FR · 3.20–4.00 $ EN |
| Terraces, 6 months | 2,220–2,638 $ | 555–660 $ | 8.30–9.90 $ | 2.02–3.50 $ FR · 3.20–4.00 $ EN |
| Moving, renovation, containers | ~1,200 $ | 300 $ | 4.50 $ | 2.02–3.50 $ FR · 4.00–5.00 $ EN |
| Motorcycle, ATV, snowmobile | 2,220 $, fewer buyers | — | — | 1.57–2.00 $ FR · 2.50 $ EN |
| Competitor names | — | — | — | 1.60 $ FR · 1.80–2.50 $ EN |
| Your brand | — | — | — | 1.20 $ |

The break-even assumes 5 % of clicks become a lead and 30 % of leads book. Even if only half as many clicks become leads, the car and terrace bids stay under break-even.

**The one bid to watch:** English mobile-storage keywords can bid up to 5.00 $. That is above the 4.50 $ break-even for a short moving booking, and it was kept because English container renters often book longer plans. If their cost per lead goes over 85 $ in the first two weeks, lower those bids to 4.00 $.

## 7. Results you can expect

**First month at about 4,530 $** (estimate):

| | Low | Middle | High |
|---|---|---|---|
| Clicks | 1,500 | 1,750 | 2,000 |
| Leads (calls ≥ 45 s and quote forms) | 45 | 70 | 100 |
| Bookings (30 % of leads) | 14 | 21 | 30 |
| First-season revenue | ~25,000 $ | ~38,000 $ | ~55,000 $ |
| Cost per lead | ~100 $ | ~65 $ | ~45 $ |

**Break-even point:** about 3 bookings a month repay the ad spend in revenue (4,530 $ ÷ ~1,800 $ average booking). Everything above that is the return.

**Targets to judge the campaigns by:**

| Metric | Target |
|---|---|
| Cost per lead | 60 $ or less in French, 85 $ or less in English |
| Calls answered from 8:00 to 20:00 | 90 % or more |
| Quote forms called back | Within 15 minutes during business hours |
| Ad position on vehicle and terrace searches, mid-October to end of November | Top of page 75 % of the time |

**Season pattern:** October and November are the peak (terrace deadlines, first snow, the December 1 winter-tire deadline). Spend drops in December and January, then rises again in March for spring moves and snowmobile storage.

**Why it is a range and not one number:** search volumes and click costs for Montreal are unknown until you spend. Your site has no reviews yet. Conversion tracking is not installed. After two weeks of data, these numbers can be replaced with real ones.

## 8. Before you turn the campaigns on

**Must fix (P0):**

1. **Bot-check page.** The site sometimes shows a "One moment, please…" page to Google's ad checker and to visitors. Turn it off, or allow Google's crawlers, in your hosting panel. Otherwise ads can be refused for "destination not working".
2. **Conversion tracking.** Your Tag Manager container is empty. Create the conversions in the new account first:
   - calls from ads, 45 s or longer;
   - calls from the website;
   - quote form sent.

   Then add the new account's Google tag (AW-…, shown in Google Ads under Goals → Conversions → Google tag) and the conversion linker to Tag Manager. Do not use AW-18092496528: it belongs to the first account. The setup is in `tracking/README.md`.
3. **One address.** The About page shows both 1215 rue Volta and 1250 rue Nobel. Use one everywhere, including Google Business Profile.
4. **Clean up the first account (209-245-0839).** Remove its 8 paused campaigns, so that nobody turns on a copy by mistake. In that account, select all campaigns, then Edit → Remove. Paused campaigns cost nothing, so this can wait a few days.

**Should fix (P1):**

- Shorten the quote form (name, phone, postal code, project, start month).
- Delete the old 395 $ delivery block.
- Use one size (148 or 160 sq ft) everywhere.
- Replace "ignifuge" with "acier CORTEN soudé, étanche".
- Add a FAQ line saying vehicles are accepted at the warehouse.

**Optional in the Google Ads screen (about 10 minutes):**

- Exclude the dense central boroughs from the residential campaigns. A delivery truck needs a 75 ft straight approach, which those streets rarely have. The boroughs are Plateau-Mont-Royal, Ville-Marie, Rosemont–La Petite-Patrie, Villeray–Saint-Michel–Parc-Extension, Outremont and Le Sud-Ouest.
- Add the display paths under each ad's URL (for example /entreposage/hiver). The upload tool could not set them.

**Suggested order to turn campaigns on:**

1. Marque and FR Véhicules hiver.
2. FR Terrasse commercial, which is time-sensitive: most boroughs require terraces removed by November 15, and some by October 30–31.
3. FR Entreposage mobile.
4. The English campaigns and Concurrents a few days later.

## 9. The first 30 days

- **Days 1–7:**
  - Every two days, read the search terms that triggered your ads, and add the bad ones as negatives.
  - Listen to the calls.
  - Install the five Google Ads scripts in test mode (`scripts/google-ads/`).
- **Scale a campaign** when its cost per lead is on target and it misses more than 20 % of searches for lack of budget. Raise its budget 20 % per week.
- **Cut an ad group** when it has 150 clicks or more and fewer than 2 % became leads. Lower its bids 30 % or pause it.
- **Change bidding** after 15–20 tracked conversions in a campaign: switch to "Maximize conversions". At 30 conversions in 30 days, switch to a target cost per lead.
- **After two weeks:** copy the campaigns into Microsoft Ads at about 10 % of budget. Six competitors already advertise there.

## 10. Everything that was built

| What | Where |
|---|---|
| Full competitor analysis with sources | `docs/01-competitive-analysis.md`, `docs/08-launch-analysis-2026-09-30.md` |
| Strategy, budget, seasonal calendar, Quebec rules | `docs/02` to `docs/06` |
| The 8 campaigns as Google Ads Editor files (backup or re-import) | `ads/google-ads-editor/` |
| The same campaigns as the files that were uploaded | `ads/api-specs/` |
| French and English landing pages: vehicles, terraces, mobile storage | `landing/` |
| Tracking setup (Google tag, Consent Mode for Law 25, conversions) | `tracking/` |
| Five automatic Google Ads scripts (budget pacing, weather, search terms, calls, ad position) | `scripts/google-ads/` |
| Free competitor watcher, runs every Monday on GitHub | `tools/competitor-watch/` |
| Ad image generator with Gemini, all Google image sizes | `tools/gemini-creatives/` |
