# 04 · Seasonal calendar — what happens each week and what the account does

Weights are the values in `scripts/google-ads/seasonal-budget-pacer.js` (1.0 = the month's even pace). Dates marked ★ still need confirmation from a primary source; treat them as planning assumptions, not facts to print in an ad.

| ISO week | Dates | Demand triggers | Weight | Account actions |
|---|---|---|---|---|
| 2026-W40 | Sep 28 – Oct 4 | Cubeit free-delivery promo ends Sep 30; PODS LAST30 ends Sep 29; marinas begin haul-outs; restaurant terraces still open | 1.10 | **Launch Oct 1.** Search campaigns live, seasonal offer live, call tracking tested. Post GBP offer. |
| 2026-W41 | Oct 5 – 11 | Thanksgiving weekend (Oct 12); cottage close-ups; first boats winterized | 1.20 | Keyword Planner pass; first search-term review Oct 8. |
| 2026-W42 | Oct 12 – 18 | ★ Earliest borough terrace deadlines (mid-October); first frost risk | 1.30 | Raise terrace budget; weather trigger armed; add converting terms as exact. |
| 2026-W43 | Oct 19 – 25 | Boat storage peak; motorcycle season ends | 1.40 | Vehicle tCPA +15 % if conversions ≥ 20; call staffing 7 days. |
| 2026-W44 | Oct 26 – Nov 1 | ★ Nov 1 terrace deadlines in several boroughs; Halloween weekend; clocks change Nov 1 | 1.50 | Peak spend. Impression-share guard active; daily check of lost IS (budget). |
| 2026-W45 | Nov 2 – 8 | First snow risk; patio heaters and planters come in | 1.45 | Keep peak. Launch PMax if Search has 30+ conversions. |
| 2026-W46 | Nov 9 – 15 | ★ Nov 15 terrace deadlines (downtown boroughs); winter-tire installs start | 1.35 | Second terrace push; email past commercial leads. |
| 2026-W47 | Nov 16 – 22 | Last collector cars parked; Grey Cup weekend | 1.20 | Shift vehicle copy to "dernière chance avant la neige". |
| 2026-W48 | Nov 23 – 29 | Black Friday; **Dec 1 winter-tire deadline** (Quebec law) | 1.10 | "Avant le 1er décembre" headline on vehicle groups. |
| 2026-W49 | Nov 30 – Dec 6 | Post-deadline; holiday declutter begins | 0.90 | Reduce vehicle bids 20 %; keep terrace for late restaurants. |
| 2026-W50 | Dec 7 – 13 | Holiday moves, renovation planning | 0.70 | Pause EN commercial. |
| 2026-W51 | Dec 14 – 20 | | 0.50 | Vehicle campaigns at 30 %. |
| 2026-W52 | Dec 21 – 27 | Holidays | 0.40 | Brand + mobile only; scripts keep running. |
| 2027-W01 | Dec 28 – Jan 3 | Jan 1 moves | 0.45 | Moving/renovation ad group up. |
| 2027-W02–W05 | Jan 4 – Jan 31 | Trough; post-holiday declutter; renovation quotes | 0.50–0.60 | Lowest budgets; build reviews, refresh creatives, prepare spring pages. |
| 2027-W06–W08 | Feb 1 – 21 | Snowmobile/ATV owners start planning summer storage; spring-move planning | 0.65–0.75 | Reactivate "motoneige été" and "VTT" groups. |
| 2027-W09–W10 | Feb 22 – Mar 7 | Mar 15 end of winter-tire period approaches | 0.80–0.90 | Spring return messaging to winter customers (retention, not ads). |
| 2027-W11–W13 | Mar 8 – Apr 4 | Snow melt; boats prepared; moving-season pre-bookings; terrace furniture returns in April | 1.00–1.20 | Second season: "retour de terrasse en avril" campaign; renovation season. |

## Demand shape by segment

| Segment | Search starts | Peak | Ends | Notes |
|---|---|---|---|---|
| Cars / collector cars | late Sep | Oct 20 – Nov 30 | Dec 1 | Winter-tire law date is a hard psychological deadline |
| Motorcycles | late Sep | Oct 15 – Nov 15 | Nov 30 | Dealers also offer storage; our edge is the driveway unit |
| Boats / PWC | mid Sep | Oct 1 – Oct 31 | Nov 15 | Only PWC and boats ≤ 16 ft on trailer fit a 20 ft unit |
| ATV / snowmobile | ATVs Oct–Nov; snowmobiles Mar–Apr (summer storage) | | | Two seasons, opposite directions |
| Restaurant / bar / hotel terraces | Oct 1 | Oct 15 – Nov 15 (borough deadlines ★) | Nov 30 | B2B: weekday hours, call-first |
| Condo buildings / landscapers | Oct 10 | Oct 25 – Nov 15 | Nov 30 | Pool furniture, planters, equipment |
| Moving / renovation | all year | Jun 15 – Jul 15 and Jan 1 | | Base load, not seasonal budget |

## Weather triggers (automated)

`scripts/google-ads/weather-trigger.js` reads Open-Meteo for Montreal every 6 hours. When 72-hour snowfall ≥ 2 cm or minimum temperature ≤ −3 °C is forecast, vehicle and terrace campaign budgets rise 35 % and a label is applied; when the forecast clears, budgets revert.

## Dates to confirm before printing them in ads (★)

- Terrace dismantling deadlines per borough for 2026 (Ville-Marie, Plateau-Mont-Royal, Rosemont–La Petite-Patrie, Le Sud-Ouest, Verdun, Villeray, Mercier–Hochelaga-Maisonneuve, Longueuil, Laval). Ask three restaurant clients or read each borough's café-terrasse permit page.
- Average first measurable snowfall for Montreal (Environment Canada normals) if you want to use "avant la première neige : ~date".
- Marina haul-out cut-off dates for Lake Saint-Louis and Lake of Two Mountains marinas.

Verified: Quebec winter tires are mandatory Dec 1 to Mar 15 (Highway Safety Code). Cubeit and PODS promo end dates were read on their sites on 2026-09-26.
