# 08 · Launch analysis — September 30, 2026 (5,000 $/month)

This supersedes the budget and bidding sections of docs 02 and 03 for the launch. Everything below was checked today on the live sites unless marked *estimate*.

## 1. Bottom line

- **Do not spend a dollar until three site problems are fixed.** The site sometimes serves a "One moment, please…" bot-check page to Google's ad crawler. The tag-manager container has no tags at all, so no conversion can be measured. The About page gives two different addresses.
- **Fight where competitors are thin, not where they are rich.** Nine companies run Google Ads on generic "entreposage" searches in Montreal. Almost nobody advertises South Shore mobile-container, vehicle-at-home or terrace searches.
- **Your price is strong for cars, moving and terraces, and weak for boats and single powersport vehicles.** Boats and jet-skis are paused. Motorcycles and ATVs run at low bids.
- **Launch on Manual CPC with hard ceilings** that sit at 35–60 % of the break-even cost per click. You cannot overspend on a keyword, and budget moves to what produces calls.

## 2. What MobilCube sells (verified on mobilcube.com today)

| Item | Fact |
|---|---|
| Unit | One size: 20 ft CORTEN steel container, 19′4″ × 7′8″ × 7′9″ inside, door 7′8″ × 7′5″, 1,165 cu ft |
| On-site rent | 350 $/mo no commitment · 300 / 270 / 220 / 180 $/mo on 3 / 6 / 12 / 24 months |
| Warehouse rent (heated, Boucherville) | +19.75 $/mo on every plan, access by appointment in 2–3 business days |
| Transport | 300 $ per movement, 15 km from Boucherville included, then 2 $/km |
| Other | 200 $ deposit refunded · 150 $ early termination · 250 $ failed delivery · date-change fees 50–250 $ |
| Delivery constraint | 75 ft straight approach, 14 ft vertical clearance, stable level ground |
| Warehouse vehicles | Owner confirmed on 2026-09-30: cars, motorcycles, ATVs and snowmobiles can be stored inside their unit at the heated warehouse. Warehouse plan 289.75 $/mo on 6 months, no transport when the customer drives the vehicle in |

**What the delivery constraint means for targeting.** A 75-ft straight approach rarely exists in front of a Plateau or Rosemont triplex. Residential ads should therefore favour South Shore, east-end, Laval and West Island suburbs, and skip the dense central boroughs. Those boroughs stay in the terrace campaign, because restaurants can load from a street permit or a lot.

## 3. Website problems that cost money in Google Ads

| Priority | Problem (seen today) | Why it costs money | Fix |
|---|---|---|---|
| P0 | A "One moment, please…" JavaScript challenge is served intermittently: 1 of 3 requests from AdsBot-Google, Googlebot and normal browsers got a 7 KB wait page | Google can disapprove ads for "destination not working", Quality Score drops, and real visitors wait 5 s before seeing anything | In the hosting panel, turn off the bot challenge or allow-list Google crawlers (AdsBot-Google, AdsBot-Google-Mobile, Googlebot, Google-InspectionTool) |
| P0 | Tag Manager container GTM-K3G9FKRW contains no tags; GA4 G-640H58NDHN is hard-coded; no Google Ads tag, no conversion linker, no consent setup | Smart Bidding can never learn, and you cannot tell which keyword produced a call | Add the Google Ads tag and conversion linker in GTM, then create the conversions in §7 |
| P0 | About page shows **1215 rue Volta** and **1250 rue Nobel** (1250 Nobel is J.L. Freeman's office) | Inconsistent address data weakens the Google Business Profile and the location asset, and hurts local-pack rankings | Pick the address customers visit, use it everywhere and on the Business Profile |
| P1 | The "Obtenir mon prix en 60 s" buttons lead to a form with 10 required fields and reCAPTCHA that ends with "nous vous recontacterons" | The ad promise ("price in 60 s") does not match the page, and long forms lose mobile visitors | Cut the form to name, phone, postal code, project, start month; ads now say "Soumission en 60 secondes" |
| P1 | FAQ still says fuel, solvents and gas cylinders are forbidden when a unit is at the warehouse | Contradicts the heated vehicle storage ads and will confuse callers | Add one line: vehicles are accepted in their unit at the warehouse |
| P1 | Delivery page still shows a second block at 395 $ + 3 $/km next to 300 $ + 2 $/km | Price in ad must match the page (Quebec consumer law, Google policy) | Delete the 395 $ block |
| P1 | 148 pi² vs 160 pi²; 10,000 lb vs 20,000 lb; "ignifuge" (fireproof) | Unprovable claims and contradictions lower trust and invite complaints | One number each; replace "ignifuge" with "acier CORTEN soudé, étanche" |
| P1 | No reviews yet; site says photos are AI-generated during launch | Lower click-through and conversion than 4.7–4.8★ competitors with thousands of reviews | Real photos of the first deliveries; ask every first customer for a Google review |
| P2 | No page for vehicles or terraces | Lower ad relevance and conversion for those groups | Publish `landing/vehicules-hiver.html` and `landing/terrasse-commerciale.html` on mobilcube.com, then set `LP_MODE=lp` |

A Booqable rental store (jl-free.booqable.com) exists behind the site but is not linked from any button. If you switch the booking buttons to it, Booqable's Google Ads app reports each paid order with its value. That needs the checkout on your own subdomain, such as reservation.mobilcube.com.

## 4. Competition: who is actually bidding

I read the tags each competitor actually has configured in its Google Tag Manager container today, plus the account IDs on its pages. The free tool in `tools/competitor-watch/` repeats this scan and reports changes.

| Competitor | Google Ads | Website-call tracking | Meta / Microsoft | Today's hook |
|---|---|---|---|---|
| Cubeit (StorageVault) | yes, 4 accounts, 7 conversion tags | yes | yes / yes | Free local delivery **ends today** (25 km) |
| Depotium (StorageVault) | yes, 3 accounts, two shared with Cubeit | yes | yes / yes | Vehicle parking pages |
| Access Storage (StorageVault) | yes, 3 accounts, remarketing, Floodlight | yes | yes / yes | Winter car storage page |
| GoCube | yes, 6 conversion tags | yes | yes / no | Promo banner expired March 31, 2026 |
| PODS | yes, 2 accounts, enhanced conversions | no | yes / yes | "Dernière vente de l'été", code DERNIERE30, up to 30 % |
| Montreal Mini-Storage | yes, 11 conversion tags | no | yes / yes | −50 % on up to 6 months, plus 29 $ + 18 $/mo fees |
| Public Storage Canada | yes, enhanced conversions | no | yes / no | Boat and vehicle parking |
| StorageMart | yes, 4 conversion tags, remarketing | no | yes / yes | Online discounts |
| U-Haul | yes, 5 conversion tags | no | no / no | 1-year price lock |
| SmartStop | no Google Ads tag found | no | no / yes | Online discounts |
| Mini-Entrepôts du Tremblay (Boucherville), Toyota Montréal-Nord winter storage, marinas | none | no | no / no | — |

An earlier version of this table said every competitor had call tracking. That was wrong: every Tag Manager container ships Google library code that mentions call tracking even when nothing is configured. The table above reads only configured tags.

**What that means:** "entreposage montréal", "mini entrepôt" and "storage montreal" have nine funded bidders, three of them under one owner sharing accounts. That is where CPCs are highest and where MobilCube's delivered 20 ft unit is least relevant. The South Shore long tail, the mobile-container terms, cars-at-home and terraces have few or no advertisers.

## 5. Price position by use case (where to push, where to hold back)

| Use case | Typical alternative, price found | MobilCube, 6 months on-site ≤15 km | Verdict |
|---|---|---|---|
| Car, heated indoor | Toyota Montréal-Nord heated underground parking: 475–555 $/mo | **Heated warehouse: 289.75 $/mo on 6 months, no transport = 1,738.50 $** | **Push hardest**: about 40 % cheaper than the heated alternative, in a locked unit of its own |
| Car, at home | Kijiji garages 165–350 $/mo | Driveway unit: 2,220 $ total ≈ 370 $/mo, 24/7 access | **Push** to people without a garage |
| Car, outdoor lot | Montreal Mini-Storage parking: 42–146 $/mo promo, 84–292 $ regular + fees; Kijiji garages 165–350 $/mo | ≈ 370 $/mo | **Push to owners of good cars**, not price shoppers; "pas cher" and "cheap" are negatives |
| Two vehicles, or a car plus summer gear | Two spots or a garage plus a locker | Same 2,220 $ | **Strongest value**; this message leads the vehicle ads |
| Single motorcycle, ATV, snowmobile | Dealers and lots, often a few hundred $ per season | 2,220 $ | **Low bids only** (cap 2.00 $); sell the "two ATVs plus trailer" and "free your garage" angle |
| Boat or jet-ski | Marina Daniel Viens 835–1,080 $ outdoor, 1,175–1,420 $ indoor per season; Sport Collette 20 $/ft; Marina d'Oka 44 $/ft | 2,220 $, and boats over ~16 ft on trailer do not fit | **Paused** |
| Moving, renovation | Cubeit and PODS hide prices; GoCube needs 3 small cubes for a 4½ | 350 $/mo, 300 $ delivery, one 20 ft unit | **Push**, core year-round demand |
| Restaurant terrace | No delivered-container competitor in French; PODS/BigSteelBox pages are English only | 2,220 $ on-site or 2,638.50 $ heated | **Push by phone**, low search volume but high ticket |

## 6. Keywords

Search volumes still need Keyword Planner or a Semrush connector. What I could verify today is which phrases people actually type in Canada, from Google's autocomplete. Everything below appears there unless marked *estimate*.

**Tier 1 — launch at full ceiling (highest intent, fewest advertisers)**

- Mobile container: entreposage mobile (prix) · conteneur d'entreposage à louer · conteneur entreposage mobile · location conteneur entreposage · location cube entreposage · cube entreposage mobile · location conteneur 20 pieds
- South Shore: entreposage boucherville · entreposage longueuil (prix) · entreposage rive sud (prix) · entreposage brossard · entreposage saint-hubert · entreposage sainte-julie · entreposage varennes · entreposage chambly
- Heated cars (new group): entreposage auto chauffé · entreposage voiture intérieur · entreposage chauffé · heated car storage montreal · indoor car storage montreal
- Cars: entreposage voiture hiver (prix) · entreposage auto hiver (prix) · entreposage voiture rive sud · entreposage auto hiver rive sud · entreposage voiture/auto longueuil · entreposage hivernal voiture · remisage voiture hiver
- English: storage container rental for driveway · storage container rental cost per month · portable storage containers for rent · mobile storage montreal · winter car storage montreal · car storage west island
- Brand: mobilcube, mobil cube

**Tier 2 — launch at reduced ceilings**

- Moving and renovation: entreposage meuble prix · entreposage déménagement · entreposage pendant rénovation
- Motorcycles, ATVs, snowmobiles: entreposage moto hiver (prix) · entreposage moto rive sud · entreposage vtt · entreposage motoneige
- Terraces and commercial (exact match, low volume, high value): entreposage terrasse restaurant · entreposage mobilier de terrasse · entreposage saisonnier commercial · restaurant patio storage montreal
- Competitor names, as keywords only: pods montréal · cubeit montréal · gocube prix · u-box montréal

**Tier 3 — paused at launch (built, ready to test)**

- Generic "entreposage montréal", "mini entrepot", "entreposage laval", "storage west island", "storage units near me": nine chains bid here, and searchers want a nearby locker.
- Boats, jet-skis, RVs and trailers: marinas are cheaper, and big boats and RVs do not fit.

**Negatives that matter most (from today's autocomplete):**

- "location conteneur" is dominated by dumpster rentals, so these are negatives: déchet, verges, benne.
- "storage container" is dominated by products, so these are negatives: bins, with lids, Walmart, Costco, Canadian Tire.
- "entreposage vtt" pulls French mountain-bike clubs, so club and vélo are negatives.
- "remisage voiture saaq" is paperwork, so saaq is a negative.
- Out-of-area cities appear in every seed, so Québec, Lévis, Saguenay, Sherbrooke, Gatineau, Toronto and others are negatives.
- Heated vehicle storage is offered at the Boucherville warehouse, so "chauffé" and "heated" are keywords (own ad groups), not negatives. Only tire storage is excluded.

**Totals:** 546 keywords are in `ads/google-ads-editor/03-keywords.csv`, 471 enabled and 75 paused, in 34 ad groups. There are 331 shared negatives and 118 campaign negatives, and none blocks an enabled keyword (checked by script).

## 7. Budget, ceilings and the math that prevents overspending

**Unit economics** (first season only, taxes excluded). The target ad cost is at most 25 % of first-season revenue. Assumptions: 30 % of leads book, and 5 % of clicks become leads (conservative for a new brand with no reviews).

| Segment | Revenue per booking | Max ad cost per booking | Break-even CPC | Launch ceiling |
|---|---|---|---|---|
| Cars (6 mo on-site) | 2,220 $ | 555 $ | 8.33 $ | 3.00 $ FR · 4.00 $ EN |
| Terrace (6 mo) | 2,220–2,638 $ | 555–660 $ | 8.30–9.90 $ | 3.50 $ FR · 4.00 $ EN |
| Moving / renovation | ~1,200 $ | 300 $ | 4.50 $ | 3.50 $ FR · 5.00 $ EN |
| Motorcycle / ATV / snowmobile | 2,220 $, but fewer buyers accept the price | — | — | 1.40–2.00 $ FR · 2.50 $ EN |

Break-even CPC is the maximum ad cost per booking × 30 % × 5 %. Even if only 2.5 % of clicks become leads, the car and terrace ceilings stay under break-even.

**Launch split (daily budgets in the import file):**

| Campaign | Daily | Month |
|---|---|---|
| FR Entreposage mobile (incl. South Shore, moving) | 50 $ | ~1,520 $ |
| FR Véhicules hiver | 45 $ | ~1,370 $ |
| FR Terrasse commercial | 12 $ | ~365 $ |
| EN Mobile storage | 15 $ | ~455 $ |
| EN Winter vehicle | 12 $ | ~365 $ |
| EN Commercial patio | 4 $ | ~120 $ |
| Brand | 3 $ | ~90 $ |
| Competitors | 8 $ | ~245 $ |
| **Total** | **149 $** | **~4,530 $**, plus ~470 $ reserve for weather and deadline boosts |

**Expected first month:** about 1,500–2,000 clicks, 45–100 leads and 14–30 bookings. That is roughly 25,000–55,000 $ of first-season revenue. These are estimates until two weeks of data exist. Some ad groups may run out of searches before they run out of budget, which is fine: unspent money is not overspending.

**Rules to go above 5,000 $:**

- **Scale:** if a campaign's cost per lead is at most 60 $ in French or 85 $ in English, and it loses more than 20 % impression share to budget, raise its budget 20 % per week.
- **Cut:** if an ad group has 150 or more clicks and fewer than 2 % became leads, lower bids 30 % or pause it.
- **Switch bidding:** after 15–20 tracked conversions, a campaign moves to Maximize conversions. At 30 conversions in 30 days it moves to target cost per lead.

## 8. Settings

| Setting | Choice | Why |
|---|---|---|
| Bidding at launch | **Manual CPC** (select the strategy directly) | Hard ceilings per keyword; location bid adjustments work; no conversion data yet |
| Networks | Search only; search partners off; Display off | No low-intent inventory |
| AI Max for Search, broad match | Off | Keep query control until conversions flow |
| Location option | Presence (people in the area) | No tourists, no out-of-province researchers |
| Residential geo (mobile + vehicle campaigns) | 0–15 km from Boucherville +25 %; 15–30 km 0 %; 30–45 km −25 %. Exclude Plateau-Mont-Royal, Ville-Marie, Rosemont–La Petite-Patrie, Villeray–Saint-Michel–Parc-Extension, Outremont, Le Sud-Ouest | The 75 ft delivery approach is rare in those boroughs |
| Terrace geo | All Montreal boroughs that allow terraces, plus Longueuil, Brossard, Boucherville, Laval | Restaurants are there |
| Ad schedule | 6:00–23:00; the terrace campaign runs Mon–Fri 7:00–19:00 | Business buyers call in business hours |
| Language | French ads in FR campaigns, English ads in EN campaigns | Google removed campaign language targeting for Search in September 2026 and now matches on ad language |
| Negative lists | "Negatives - FR" on FR and FR+EN campaigns; "Negatives - EN" on EN and FR+EN campaigns | Prevents cross-language blocking |

**Terrace deadlines** (Ville de Montréal, verified today). Most boroughs require terraces on public property to be removed by **November 15**. Côte-des-Neiges–NDG, Outremont and Lachine close **October 31**, and Mercier–Hochelaga-Maisonneuve closes **October 30**. Run terrace ads from now to November 15, with the heaviest spend October 15–31.

## 9. Conversions to create before launch

| Conversion | How | Primary? |
|---|---|---|
| Calls from ads | Call asset with Google forwarding number, calls ≥ 45 s | Yes |
| Calls from website | Google tag phone-number swap on 450-641-6498, ≥ 45 s | Yes |
| Quote form | WPForms confirmation → redirect to a thank-you page, conversion on that page view (or GTM listener on WPForms submit) | Yes |
| Tap on phone number | GTM click trigger on `tel:` links | No, observe only |
| Paid booking | Booqable Google Ads app if the checkout goes live on your subdomain | Yes, once live |

Consent Mode v2 must be in the same GTM container (Quebec Law 25); the snippet is in `tracking/gtag-snippet.html`.

## 10. Other channels checked

- **Local Services Ads (pay per lead).** A July 2026 guide lists 17 Canadian categories, including "Moving" but not "Storage". Google's own help page for this is the US version. Confirm in the account. It is not recommended at launch: movers' leads expect a full-service move.
- **Microsoft Ads.** Cubeit, PODS, Depotium, Access, Montreal Mini-Storage and Public Storage all run the Microsoft ads pixel. Import the Google campaigns into Microsoft Ads after two weeks, at about 10 % of budget.

## 11. What is still an estimate, and how to fix it

- **Search volume and CPC per keyword.** Semrush is connected, but the account has no API units left, so it returned no data. Buying more units at semrush.com/mcp-access would unlock volumes and competitors' paid keywords.
- **Supermetrics is connected to the Mobil Cube Google Ads account (2092450839).** Its Keyword Planner call ignored the Montreal and French filters: city, province and country returned identical numbers, and French terms showed 10 searches or fewer. Google also gives only rough volumes to a new account that has not spent yet. Treat those volumes as unusable. Keyword ideas it pulled from competitor pages were added to the campaigns: louer un conteneur prix, conteneur déménagement prix, location entreposage, prix entreposage, mini entrepôt longueuil and others. Reliable volumes come after a week of spend, or from the Keyword Planner screen with location Montreal and language French.
- **Mobile page speed.** Google's PageSpeed API quota was exhausted from this environment; run pagespeed.web.dev on the French home page yourself.

## Sources checked today

mobilcube.com (FR/EN home, prix-location, livraison-conteneur, formulaire-reservation, capacites-stockage, foire-aux-questions, a-propos), googletagmanager.com container GTM-K3G9FKRW; cubeit.ca/fr, pods.ca/fr, gocube.com, gocube.com/entreposage-rive-sud, montrealministorage.com/fr, depotium.com/fr, publicstoragecanada.com/fr, smartstopselfstorage.com/fr, storage-mart.com/fr-ca, accessstorage.ca/fr, uhaul.com/fr-ca and their GTM containers; minientrepotdutremblay.com; storageauto.ca/products/entreposage-auto-hiver; marinadanielviens.com/entreposage; sportcollette.com; marinaoka.com/tarifs; montreal.ca "Installer une terrasse commerciale sur le domaine public" and "Nouveau règlement sur les cafés-terrasses dans Ville-Marie"; support.google.com/google-ads/answer/1722078; playbookdigital.ca/google-local-services-ads-canada; help.booqable.com (Google Ads app); Google autocomplete (suggestqueries.google.com, gl=ca, hl=fr/en), 59 seeds.
