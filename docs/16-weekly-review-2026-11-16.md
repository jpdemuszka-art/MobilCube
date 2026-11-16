# 16 · Weekly Google Ads review, 5-second exits, and the return on the ads (2026-11-16)

Owner's requests on November 16:
- "Is there a way to see the conversions and see if the ads have a return?" (§5)
- "Build a schedule task for the ads campaign and see if we are wasting money on ads that don't have any clicks and conversions", plus the number of visitors who click an ad and leave within 5 seconds, every Monday at 8:00 (§1 to §4).

The figures, the weekly instructions and the 5-second guide were reviewed independently before the weekly task was created; the corrections are included.

## 1. The weekly review

Every Monday at 7:47 (Montreal), Claude reads the Google Ads account through Supermetrics and posts a report in the MobilCube Claude conversation around 8:00. The scheduled task is "MobilCube weekly Google Ads review" (id `trig_01HAKyHVLp5e4Lfn3eDa54UX`, created November 16, first run November 23). The old daily report (`trig_015Fw3ZJp7aJGEd4r7nTPURD`) has been off since November 2. It never changes the account: fixes are recommendations, applied only when the owner replies "apply".

| Part | What it answers |
|---|---|
| Spend, budget use, clicks, forms, calls, cost per lead, per campaign, against the week before | Are the 96 $/day buying leads, and which campaigns are capped by their budget? |
| Searches that got clicks | Is money going to people MobilCube cannot serve? Each one comes with the exact negative keyword, checked against the campaign's keywords. Competitor searches are labelled apart, not as waste. |
| Misrouted searches | Car searches served by the mini-warehouse campaign, and the reverse. |
| Keywords and ad groups that spend without a lead | Judged over all weeks so far, with the rule in §2. |
| Ads | Disapproved ads, or ads shown often and almost never clicked. |
| Visitors who leave within 5 seconds | Once §3 is done. |

**Ledger.** The free Supermetrics tier only returns about the last 14 days, and one bad week proves nothing at this volume. So each run appends the week's ad-group and keyword rows to `ads/weekly-review/ledger-adgroups.csv` and `ledger-keywords.csv`, commits them, and judges on the running total. The ledgers start with November 2 to 15.

**Free-tier limits** (the Supermetrics trial ended October 15): at most 100 rows per query, about 14 days back, a daily allowance, and the account check returns "no license", so the allowance could stop. If Supermetrics refuses, the report's first line says so with the fix (a paid plan, or reconnecting with the paying account). Google Ads can also email the same tables weekly by itself: Reports → open a report → Schedule.

## 2. What counts as wasted money

- **A click on a search MobilCube cannot serve** (movers, truck rental, sea containers, RV or boat storage, warehouse leasing, jobs, DIY, places outside the service area) is waste. It is fixed with a negative keyword.
- **A search MobilCube serves but in the wrong campaign** is "misrouted", not waste. Usually the right campaign was out of budget.
- **An ad that gets no click costs nothing.** Google charges per click on Search. An ad matters only if it is shown often and almost never clicked (200 impressions or more, CTR under 2 %).
- **A keyword that spends without a lead** is judged by the odds that it is just bad luck. From November 2 to 15 the account made 6 lead conversions from 593 clicks (about 1 in 100). At that rate, zero leads is common:

| Clicks with 0 leads | Chance it is bad luck (at 1 in 100) | Verdict |
|---:|---:|---|
| 50 | 60 % | not enough data |
| 100 | 36 % | watch |
| 175 | 17 % | watch |
| 230 | 10 % | watch |
| 300 | 5 % | lower the bid or pause |

The weekly run recomputes the account rate each week and applies: 50 % or more = not mentioned; 5 to 50 % = watch; under 5 % = lower the bid or pause. "Lower or pause" is never decided on one week. A fixed dollar rule (for example "100 $ with no lead") would have recommended pausing the account's two best keywords by chance.

**Leads** are booking forms and calls from the ads. "Calls from ads" counts every call, repeat calls included, so 4 calls can be fewer than 4 people; the report says "up to N people". Clicks on the site's phone number, "Clicks to call", "Local actions" and the 5-second action are shown apart, never as leads.

## 3. Visitors who leave within 5 seconds

**The limit.** Google Ads does not measure time on site, and its bounce and time-on-site fields return 0 for this account. Any Google tag (Google Ads or Google Analytics) is also bound by the cookie banner: under Law 25, CookieYes refuses ad and analytics cookies until the visitor clicks Accept, and Google only estimates the refusers above several hundred clicks a week, far more than this account gets. So a Google tag can count **who stayed at least 5 seconds among visitors who accepted cookies**, but it cannot say how many of all visitors left. Two options:

**Option A: "Visite 5 s+" in Google Ads (owner, about 20 minutes, a lower bound).** Gives, per campaign, the share of website clicks confirmed to stay 5 seconds. Useful week to week; not a true bounce rate.

*Google Ads*
1. Goals → Conversions → Summary → **+ Create conversion action** → **Conversions on a website** → `mobilcube.com` → Scan.
2. Category **Page view** → **+ Create conversion** → **Google tag** → **Manually using code**. Never choose "Automatically without code": it would count every page load as a stay.
3. Settings: Action optimization **Secondary (observe only)**; Name **`Visite 5 s+`** (exactly; the weekly review looks for it); Value **Don't use a value**; Count **One**; Click-through window **1 day**; Attribution **Last click**; Enhanced conversions off. Done → Save and continue.
4. Tag setup → **Use Google Tag Manager** → copy the **Conversion label**. The Conversion ID is `18484934240`.
5. Check in Goals → Summary that "Visite 5 s+" shows as Secondary. If it were Primary it would count as a lead everywhere; the weekly review warns if that happens.

*Tag Manager (container GTM-M69QW6VC)*
1. Variables → New: **1st-Party Cookie**, cookie name `cookieyes-consent`, named `Cookie - CookieYes`. Then **Custom JavaScript** `function(){return Math.round(performance.now());}` named `JS - ms depuis chargement`, and **Custom JavaScript** `function(){return document.visibilityState;}` named `JS - onglet visible`.
2. Triggers → New → **Timer**: event name `gtm.timer`, interval `1000`, limit `60`; enable when Page Hostname contains `mobilcube.com`; fires on **Some timers** when all three hold: `JS - ms depuis chargement` greater than or equal to `5000`; `Cookie - CookieYes` contains `advertisement:yes`; `JS - onglet visible` equals `visible`. Name it `Timer - 5 s visible + pub acceptée`. This counts 5 seconds from the start of the page load, ignores tabs opened in the background, and still fires when the visitor accepts the banner after 5 seconds.
3. Tags → New → **Google Ads Conversion Tracking**: ID `18484934240`, the label from A4, no value, trigger from B2. Advanced settings → Tag firing options **Once per page**. Consent settings **No additional consent required** (the trigger already requires the accepted cookie). Name it `Google Ads - Conversion - Visite 5 s+`.
4. **Preview**, in a private window, on `https://www.mobilcube.com/fr/formulaire-reservation/?gclid=TEST123`:
   - On the first event, the Consent tab must show ad_storage and ad_user_data **denied** by default. If it is empty, turn on Google Consent Mode in CookieYes first (docs/10 étape 5).
   - Do not touch the banner for 10 s: the tag must stay under Tags Not Fired.
   - New private window, accept at about 2 s: the tag fires after 5 s.
   - New private window, accept at about 8 s: the tag fires at the next second.
   - New private window, accept, then leave for another page within 3 s: no firing on the first page.
   - Repeat on `/en/booking-form/`. If the cookie name differs on the site, use the one shown in the browser's cookies.
5. **Submit** → Publish. Google Ads shows "Recording conversions" for the action after 2 to 3 days.

The weekly review then reports *confirmed stays = Visite 5 s+ ÷ website clicks* (call, direction and Business Profile clicks excluded), and quick exits only as "at most 1 − confirmed stays". If the action records almost nothing it says the tag is not working rather than printing a false 100 % exit rate.

**Option B: an exact count without cookies (a developer, about half a day).** A small script on the booking pages sends one anonymous signal when an ad visitor's page loads and another after 5 seconds in a visible tab, to a counter on mobilcube.com that stores only daily totals per campaign and ad group (no cookie, no identifier, no IP address). Campaign and ad group come from an account-level Final URL suffix (`mc_c={campaignid}&mc_g={adgroupid}`). Quick exits = 1 − (5-second signals ÷ page loads), for every visitor. It needs the owner's and the privacy officer's agreement and a line in the privacy policy. Claude can write the script and the counter on request; installing them is website work.

Google Analytics 4 is not a shortcut: it has the same cookie gap, and its own "engaged session" starts at 10 seconds, not 5.

## 4. Trial run on November 2 to 15

| | |
|---|---|
| Spend | 1,134.17 $ |
| Clicks | 593, at 1.91 $ each |
| Lead conversions | 6: 2 booking forms, 4 calls from the ads (up to 4 people) |
| Cost per lead conversion | 189 $ (up to 378 $ per person if the calls came from 2 people) |
| Forms per click | 0.34 % |

- **Budgets.** FR Entreposage mobile (38.89 $/day against 35 $) and FR Vehicules hiver (33.34 $/day against 30 $) both spent 111 % of budget: they are capped, and together they took 89 % of spend and 5 of the 6 conversions. About 16 $/day sits unused in Terrasse (5 $ budget, nothing spent), EN Commercial patio (2 $, nothing), Concurrents (3 $, 0.14 $/day) and EN Mobile storage (10 $, 3.42 $/day); Marque's 3 $ also went unspent. Moving part of it to FR Vehicules hiver is the first thing to consider (applied only on the owner's word).
- **Searches.** Only the 100 searches with the most impressions could be read (52 of them got clicks: 155 of the 593 clicks, 26 %). Among those, none was a search MobilCube cannot serve. "u haul storage", "depotium near me" and "entrepot public near me" are competitor searches with 0 clicks. The weekly review reads all searches with clicks, so its coverage will be higher.
- **Misrouted car searches.** "entreposage voiture hiver prix", "entreposage voiture prix" and "entreposage auto hiver" took 11 clicks (20.33 $) in FR Entreposage mobile through its "prix entreposage" and "location entreposage" keywords. FR Vehicules hiver has exact keywords for these searches but was out of budget. A negative in FR Entreposage mobile would leave these searches with no MobilCube ad during those hours. Better: give FR Vehicules hiver more budget first. If negatives are wanted later, use the narrow phrases "entreposage voiture", "voiture hiver" and "auto hiver", never "auto" alone (it blocks "auto-entreposage").
- **Keywords and ad groups without a lead.** With the §2 rule, none reaches "watch" yet. The largest is Rive-Sud (géo), 48 clicks and 93.80 $ with no lead: a 61 % chance of bad luck. The largest keyword is [entreposage voiture hiver prix], 29 clicks and 56.44 $: 74 %.
- **Ads.** All 23 ads that ran are enabled and approved. None was shown 200 times with a CTR under 2 %. The 5 ads with no click cost 0 $.
- **What the trial says.** No money was found going to searches MobilCube cannot serve, and no keyword or ad group has spent enough to judge. The weak point is still turning clicks into leads: 0.34 % in forms, 0.5 to 1 % counting calls.

## 5. Seeing the conversions and the return on the ads

**Where to see conversions (free, full history since October 7).** In Google Ads: Campaigns, with the columns Conversions, Cost / conv. and All conv.; Segment → Conversions → Conversion action shows forms and calls separately. Goals → Summary shows each action and whether it is primary or secondary. For calls, the **Call details** report (Reports → Report editor) lists each call with time, length, campaign and usually the caller's number: the best way to check who the 4 calls were.

**Why Google cannot show the return.** The values in the account are placeholders: 50 $ per form and 1 $ per call. That makes Google's "return on ad spend" 0.09, which means nothing. Google does not know who signed. Only the customer list knows.

**What a return needs, with the repo's own targets** (docs/13 §4c: ad cost at most 25 % of first-season revenue, 30 % of leads booking):

| | Target cost per lead | Actual, Nov 2–15 |
|---|---:|---:|
| Heated car (160 $ × 6) | 72 $ | 189 to 378 $ |
| Mini-warehouse (docs/13: 3 months + delivery + pickup) | 124 $ | 189 to 378 $ |

The 1,134 $ spent in those two weeks pays back on revenue alone with about 1 mini-warehouse rental or 2 cars. It meets the repo's 25 % target with about 3 mini-warehouse rentals or 5 cars. The mini-warehouse figure is an estimate: the 160 $ promotion has no published term, and the repo's values assume 6 months plus 300 $ delivery and 300 $ pickup (1,560 $). These are revenue, not profit.

**What to do, simplest first:**
1. **A lead log** (one row per lead: date, source, phone or name, product, quote, signed yes/no, monthly price, months). Ask every caller "Comment nous avez-vous trouvés ?". Each Monday, reply to the weekly report with the number of new customers from the ads and their value; Claude tracks the return in the report.
2. **Check the call conversion.** "Calls from ads" (every call counted, 1 $ value) recorded the 4 calls; the intended action "Appel depuis l'annonce" (45 seconds or more, one per click, 60 $) recorded none. In Google Ads, set "Appel depuis l'annonce" as the action of the call asset (or the account's default call action) and make "Calls from ads" secondary.
3. **Find where the booking-form emails go.** They do not reach the owner's Gmail, and WPForms Lite keeps no copy of the entries. A form lead nobody sees is a lost sale.
4. **Later, to let Google see real sales:** add a hidden `gclid` field to both WPForms forms (docs/13 M7: the live forms have none), create an import action named "Booked job", and upload signed customers weekly with `tracking/offline-conversions-template.csv`. Calls can be imported by caller number and call time without a gclid.
