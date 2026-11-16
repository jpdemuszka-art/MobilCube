# 16 · Weekly Google Ads review and 5-second exits (2026-11-16)

Owner's request (November 16): "build a schedule task for the ads campaign and see if we are wasting money on ads that don't have any clicks and conversions", plus the number of visitors who click an ad and leave the site within 5 seconds, every Monday at 8:00.

## 1. What the weekly review does

Every Monday at 7:58 (Montreal), Claude reads the Google Ads account through the Supermetrics connector and posts a report in the MobilCube Claude conversation, ready by 8:00. It never changes the account: every fix is a recommendation, applied only when the owner replies "apply".

It covers the Monday-to-Sunday week that just ended, compared with the week before:

| Part | Source | What it answers |
|---|---|---|
| Spend, clicks, cost per click, leads, cost per lead, per campaign | Google Ads | Are the 96 $/day buying leads, and is it better or worse than last week? |
| Searches that got clicks | Google Ads search terms | Is money going to people MobilCube cannot serve (movers, truck rental, sea containers, RV, jobs, other regions)? Each one comes with the exact negative keyword to add. |
| Keywords and ad groups with spend and no lead | Google Ads, last 14 days | Which ones to lower or pause, using the sample-size rule in §2. |
| Ads | Google Ads | Ads that are disapproved, or shown often but rarely clicked. |
| Visitors who leave within 5 seconds | Google Ads, once §3 is done | Which campaigns send people who do not stay on the page. |

**Limits of the free Supermetrics tier** (the trial ended October 15): each query returns at most 100 rows and only about the last 2 weeks, under a daily allowance. That is enough for a weekly review of this account. A paid plan lifts the limits. If the connector refuses a query, the report says so on its first line.

## 2. What counts as wasted money

- **A click on a search MobilCube cannot serve** is always waste. These are fixed with negative keywords, checked so they never block MobilCube's own keywords.
- **An ad that gets no click costs nothing.** On Search, Google charges per click, so an ad that is shown and not clicked is not wasted money. It only matters if it is shown often and almost never clicked (200 impressions or more with a CTR under 2 %), which means it does not match what people search.
- **A keyword that spent without a lead** is judged with care. From November 2 to 15 the account turned about 1 click in 100 into a lead (6 leads from 593 clicks). At that rate, most keywords show zero leads after two weeks by chance alone, and a keyword needs about 100 clicks (about 190 $) before "no lead" means something. The rule:

| Spend in the last 14 days, with 0 leads | Verdict |
|---|---|
| 100 $ or more | Lower the bid or pause |
| 40 to 100 $ | Watch |
| Under 40 $ | Not enough data; not called waste |

Leads are the primary conversions only: booking-form submissions and calls from the ads. Clicks on the site's phone number, "Clicks to call" and the "Local actions" rows (directions, profile visits) are reported apart.

## 3. Measuring visitors who leave within 5 seconds (owner, about 15 minutes)

Google Ads does not know how long a visitor stays on the site. Its "bounce rate" and "time on site" fields return 0 for this account because no Google Analytics property is linked to it. The simplest exact measure is a **secondary conversion that fires after 5 seconds on the page**. Google Ads then counts, per campaign and ad group, how many ad clicks stayed at least 5 seconds; the rest left sooner.

**A. Google Ads: create the action**
1. Goals → Conversions → Summary → **+ Create conversion action** → **Website** → enter `mobilcube.com` → Scan.
2. Choose **Add a conversion action manually**.
3. Category **Page view**. Name: **`Visite 5 s+`** (exactly this; the weekly review looks for it). Value: **Don't use a value**. Count: **One**. Keep the default windows. Save.
4. Open the new action → **Edit settings** → Action optimization → **Secondary action** (used for observation only). This is important: as a primary action it would count as a lead and distort the numbers and the bidding.
5. Choose **Use Google Tag Manager** and copy the **Conversion label**. The Conversion ID is the same as for the booking: `18484934240`.

**B. Tag Manager (container GTM-M69QW6VC)**
1. Triggers → New → **Timer**. Event name `gtm.timer`, Interval `5000`, Limit `1`. Enable this trigger when: **Page Hostname contains `mobilcube.com`**. Fires on: All timers. Name it `Timer - 5 s`.
2. Tags → New → **Google Ads Conversion Tracking**. Conversion ID `18484934240`, Conversion label from A5, no value. Trigger: `Timer - 5 s`. Name it `Google Ads - Conversion - Visite 5 s+`.
3. **Preview** → open `https://www.mobilcube.com/fr/formulaire-reservation/`, wait 6 seconds: the new tag must appear under Tags Fired. Close the tab before 5 seconds once: it must not fire.
4. **Submit** → Publish.

**How to read it.** Quick exits = 1 - (Visite 5 s+ ÷ clicks). Only visitors whose browser lets the tag run are counted (the cookie banner refuses ad cookies by default), so the real quick-exit rate is lower than the figure shown. Compare campaigns with each other and week to week rather than with an outside benchmark. A campaign that loses many more visitors in 5 seconds than the others is usually an ad promising something the page does not show (price, product) or a slow page on phones.

**Richer option, later:** connect Google Analytics 4 in Supermetrics and link it to Google Ads. GA4 gives time on page and pages per visit, but its own "bounce" uses a 10-second threshold, not 5.

## 4. First run, on November 2 to 15

A trial run on the 14 days the free tier allows (all figures from Google Ads):

| | |
|---|---|
| Spend | 1,134.17 $ (81 $/day, under the 96 $ budget) |
| Clicks | 593, at 1.91 $ each |
| Leads | 6: 2 booking forms, 4 calls from the ads |
| Cost per lead | 189 $ |

- **Irrelevant searches: almost none got clicks.** In the 100 searches with the most impressions, the off-target ones ("u haul storage", "depotium near me", "ats container services inc near me", "entrepot public near me") had 0 clicks and cost 0 $.
- **Car searches land in the mini-warehouse campaign.** "entreposage voiture hiver prix", "entreposage voiture prix" and "entreposage auto hiver" took 11 clicks (20.33 $) in FR Entreposage mobile through its "prix entreposage" and "location entreposage" keywords. That campaign has no car keyword, so the negatives `voiture` and `auto` (phrase) there send those searches to FR Vehicules hiver, whose ads quote the car price.
- **No keyword reached the 100 $ threshold without a lead.** The largest is [entreposage voiture hiver prix] at 56.44 $ for 29 clicks: watch. Ad groups to watch (40 to 100 $, no lead): Rive-Sud (géo) 93.80 $, Moto hiver 73.25 $, EN Winter car storage 56.19 $, Montérégie (géo) 55.25 $.
- **Ads:** all 23 that ran are enabled and approved; none was shown 200 times with a CTR under 2 %. The 5 ads with no click (Competitors EN, Motorcycle & ATV, Mini-entreposage mobile, Commercial saisonnier, Motoneige) cost 0 $.
- **Conclusion of the trial:** the money is going to the right searches. The weak point remains the share of clicks that become leads (about 1 in 100, docs/15 §1), which the booking-form fixes in docs/15 §2 address, and which the 5-second measure will help locate.

The keyword list in this trial was capped at 100 rows by the free tier (530 of the 593 clicks); the weekly review asks only for keywords with clicks, which stays under the cap.
