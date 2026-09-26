# 03 · Budget and forecast

All inputs are estimates until Keyword Planner and two weeks of data replace them. Arithmetic is shown so you can change one number and see the effect.

## Inputs

| Input | Value used | Where it comes from |
|---|---|---|
| Blended CPC, French campaigns | 3.20 $ | FR keyword estimates 1.50–5.50 $, weighted to vehicle/terrace clusters |
| Blended CPC, English campaigns | 5.50 $ | EN keyword estimates 3–9.50 $ |
| Click → lead (call ≥45 s or form) | 7 % | 2026 cross-industry Search CVR 4.4 % (Digital Applied, Apr 2026); local services with click-to-call landing pages run higher; storage landing pages with a visible price convert better than quote-gated ones |
| Lead → booked job | 30 % | owner-operator answering the phone, price already known by the caller |
| Average winter booking value | 1,950 $ | 6 months Avantage 270 $ + delivery 300 $ + pickup 300 $ (on-site, within 15 km), taxes excluded |
| Average mobile/moving booking value | 1,200 $ | 3 months at 300 $ + 300 $ delivery |
| Terrace booking value | 2,100 $ | 6 months warehouse plan 289.75 $ + 2 movements |

## Three budget scenarios (peak month, October or November)

| Scenario | Budget/month | Clicks (÷ blended 3.60 $) | Leads (× 7 %) | Cost per lead | Bookings (× 30 %) | Revenue (× ~1,800 $ avg) | Return on ad spend |
|---|---|---|---|---|---|---|---|
| Lean | 3,000 $ | ~830 | ~58 | ~52 $ | ~17 | ~31,000 $ | ~10× |
| Recommended | 5,500 $ | ~1,530 | ~107 | ~51 $ | ~32 | ~58,000 $ | ~10× |
| Aggressive | 9,000 $ | ~2,500 | ~175 | ~51 $ | ~52 | ~94,000 $ | ~10× |

The return stays flat because CPC and conversion rate are assumed constant; in reality the aggressive scenario pays higher CPCs on generic terms and drops to roughly 6–7×. Capacity is the real ceiling: 52 bookings in a month is 52 container movements. **Check fleet availability before choosing Aggressive.**

## Recommended month-by-month plan (CAD, ad spend only)

| Month | Budget | Weight driver | Expected leads | Expected bookings |
|---|---|---|---|---|
| Oct 2026 | 5,500 $ | boat haul-out, terrace deadlines, first frost | ~105 | ~32 |
| Nov 2026 | 5,500 $ | terrace deadlines (Nov 1 / Nov 15 boroughs), first snow, winter-tire deadline Dec 1 | ~105 | ~32 |
| Dec 2026 | 3,000 $ | last cars, holiday declutter, moving Jan 1 | ~55 | ~16 |
| Jan 2027 | 1,800 $ | trough; brand, renovation, post-holiday | ~33 | ~10 |
| Feb 2027 | 1,800 $ | trough; snowmobile/ATV summer storage starts to search | ~33 | ~10 |
| Mar 2027 | 3,500 $ | spring returns, moving season pre-bookings, motoneige storage | ~65 | ~20 |
| **Season** | **21,100 $** | | **~400** | **~120** |

## Campaign split at peak (matches `scripts/google-ads/seasonal-budget-pacer.js` MONTHLY_CAP)

| Campaign | Peak month cap | Share |
|---|---|---|
| FR Vehicules hiver | 2,600 $ | 31 % |
| FR Terrasse commercial | 1,500 $ | 18 % |
| FR Entreposage mobile | 1,800 $ | 21 % |
| EN Winter vehicle | 700 $ | 8 % |
| EN Commercial patio | 400 $ | 5 % |
| EN Mobile storage | 600 $ | 7 % |
| Marque | 150 $ | 2 % |
| Concurrents | 400 $ | 5 % |
| PMax Saisonnier (phase 2) | 1,000 $ | (added on top when launched) |
| **Total Search** | **8,150 $ cap, ~5,500 $ expected spend** | |

Caps sit above expected spend so the impression-share guard has room during the deadline weeks.

## Targets to hold the team to

| Metric | Target | Why |
|---|---|---|
| Search top impression share, vehicle + terrace groups, weeks 43–48 | ≥ 75 % | the deadline weeks are the season |
| Cost per lead | ≤ 60 $ FR, ≤ 85 $ EN | at a 30 % close and 1,800 $ ticket, 60 $/lead is a 9× return |
| Call answer rate 8–20 h | ≥ 90 % | an unanswered call in November is a lost season |
| Speed to lead on forms | ≤ 15 min in business hours | |
| Search-term waste (spend on terms later negated) | ≤ 8 % of spend | miner script |
| Quality Score on core exact keywords | ≥ 7 | landing page relevance |

## Non-media costs to budget

| Item | Cost | Notes |
|---|---|---|
| Call tracking platform (optional, recommended from month 2) | 60–150 $/mo | dynamic number pool; Google forwarding numbers are free but give less |
| Gemini image generation | < 5 $ | 14 scenes at two sizes |
| Landing page hosting | 0–20 $/mo | static files, Vercel/Netlify/Cloudflare |
| Time | 3–4 h/week | reading scripts' reports, listening to calls, adjusting caps |
