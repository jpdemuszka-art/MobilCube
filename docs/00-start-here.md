# 00 · Start here

**What this is.** A complete, ready-to-import Google Ads program for MobilCube's fall/winter 2026-2027 season, built on a competitive analysis of the Montreal storage market done on 2026-09-26.

**The one-paragraph strategy.** Competitors (Cubeit, PODS, GoCube, Montreal Mini-Storage) hide their prices, ban or restrict vehicles, store far from the South Shore and market in English first. MobilCube publishes prices, can take a car, sits in Boucherville and speaks French. We run French-first Search campaigns split by segment (winter vehicles, commercial terraces, mobile storage) plus small English campaigns for the West Island, land every click on a segment page with a visible price and a call button, track calls as the primary conversion, and let scripts push budget into the six weeks between the first terrace deadline and the December 1 winter-tire deadline. Performance Max with Gemini imagery comes second, once Search has 30 conversions a month.

## Read in this order

- `09-summary-what-was-done.md`: **start here.** The whole project on one page: the competitor analysis, the keyword choice, the 8 campaigns now paused in the Google Ads account, and the results to expect.
0. `08-launch-analysis-2026-09-30.md` — **the launch plan at 5,000 $/month**: site blockers found on launch day, who is bidding today, price position by use case, verified keywords, bid ceilings and break-even math. It supersedes the budget and bidding parts of 02 and 03.
1. `01-competitive-analysis.md` — who you are up against, with prices and sources
2. `02-google-ads-strategy.md` — campaigns, keywords, copy rules, settings, bidding roadmap
3. `03-budget-and-forecast.md` — three budget scenarios and the arithmetic behind them
4. `04-seasonal-calendar.md` — week-by-week actions and the dates still to confirm
5. `05-campaign-wizard-answers.md` — exactly what to paste into the Google Ads wizard you have open
6. `06-compliance-quebec.md` — French-language, price-display, privacy and Google-policy rules

## Launch sequence (about two working days)

| Step | Where | Time |
|---|---|---|
| 1. Fix the site: one square-footage number, one delivery price, soften "fireproof/airtight", decide the vehicle policy | mobilcube.com | 2 h |
| 2. Publish the landing pages and privacy policy | `landing/` → any static host (or as pages on mobilcube.com) | 2 h |
| 3. Conversions: create the 5 actions, add the AW tag to GTM-K3G9FKRW, enable call reporting, test with a real call | `tracking/README.md` | 2 h |
| 4. Import campaigns | Google Ads Editor → `ads/google-ads-editor/` | 1 h |
| 5. Set locations, budgets, schedules, conversion goals; post | Google Ads web UI, `02-google-ads-strategy.md` §2–3 | 1 h |
| 6. Keyword Planner pass, adjust CPC caps | Google Ads | 1 h |
| 7. Generate and upload images | `tools/gemini-creatives/` (needs GEMINI_API_KEY) | 30 min |
| 8. Install the five scripts in DRY_RUN | `scripts/google-ads/` | 45 min |
| 9. Google Business Profile: categories, hours, photos, review requests | business.google.com | 1 h |
| 10. Day 7: read the miner and call reports, flip DRY_RUN off | scripts | 1 h |

## Decisions only MobilCube can make (blocking for some ads)

0. **Site fixes.** One square-footage number (148 or 160), one delivery price (300 $ + 2 $/km, remove the 395 $ block), one load figure (10 000 lb transport limit, not "20 000 lb"), and replace "ignifuge/fireproof" and "airtight" with "acier CORTEN soudé, étanche".
1. **Vehicle policy.** Decided on 2026-09-30: vehicles can go in the customer's driveway unit or inside their unit at the heated Boucherville warehouse. Update the site FAQ line that bans fuel at the warehouse so it matches the ads.
2. **Seasonal offer.** The ads quote the real plans (270 $/mo on 6 months, 300 $ delivery). A packaged "Forfait hiver" (6 months + delivery + pickup at one price) would convert better and is easy to add to the booking platform.
3. **Terrace dates.** Confirm the 2026 dismantling deadline for the boroughs your restaurant clients are in and put the date in the ad ("avant le 15 novembre").
4. **Call handling.** Who answers 8:00–20:00, seven days, from October 5 to November 30?

## What was verified and what was not

A separate fact-checking pass re-fetched the primary pages for eight decision-critical claims: six confirmed, two partially correct and corrected, none refuted (`docs/07-verification-log.md`).

Verified on primary sources on 2026-09-26: MobilCube prices and fees; Cubeit, PODS, BigSteelBox and Montreal Mini-Storage offers, promos and contract terms; Google's September 2026 removal of language targeting for Search; Google's US list of Local Services Ads categories (includes "Storage" and "Moving services"; Canadian eligibility to confirm); Gemini image model IDs and prices; Google image-asset specs; OQLF June 2025 signage rule.

Estimated, to validate in Keyword Planner and with two weeks of data: every search volume and CPC; conversion rates; the budget forecast.

Not verified (research session hit its rate limit): borough terrace deadlines for 2026; marina per-foot boat prices; GoCube's current price page (404); Depotium, Public Storage, SmartStop, StorageMart, Access, U-Box, Spaceful and Valet Dépôt deep-dives (light coverage from the initial scan only).
