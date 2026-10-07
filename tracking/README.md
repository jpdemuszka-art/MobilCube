# Tracking setup (calls + forms + Quebec Law 25 consent)

**Account 194-768-4780, 2026-10-07:** the site already loads GTM-K3G9FKRW (empty), GA4 G-640H58NDHN and CookieYes. The booking form is WPForms (AJAX, no thank-you page). Use `gtm-import-mobilcube-google-ads.json` (Google tag, conversion linker, WPForms success listener, booking and phone-click conversions) and follow the French step-by-step in `docs/10-suivi-conversions.md`. The `gtag-snippet.html` route below is the alternative for a site without GTM.

Goal: every call and quote request is a conversion Google Ads can bid on, and nothing fires before consent in Quebec.

## 1. Conversion actions to create in Google Ads (Goals → Conversions)

| Name | Type | Value | Count | Category | Primary? |
|---|---|---|---|---|---|
| `Call from ads` | Calls from ads using call assets, min 45 s | 60 CAD | Every | Phone call lead | Yes |
| `Call from website` | Calls to a number on your website (Google forwarding number swap), min 45 s | 60 CAD | Every | Phone call lead | Yes |
| `Quote form` | Website event `generate_lead` (GA4 import or tag) | 40 CAD | One | Submit lead form | Yes |
| `Click to call (mobile)` | Website event `click_to_call` | 5 CAD | Every | Contact | No (secondary, observe only) |
| `Booked job` | Offline import (upload from CRM/sheet by GCLID) | actual revenue | Every | Purchase | Yes once >15/month |

Why: calls are the highest-intent action for storage. Bidding on `click_to_call` as primary trains Smart Bidding on cheap, low-quality taps; keep it secondary. Use the 45-second minimum so wrong numbers do not count.

## 2. Tags

Use one Google tag (`gtag.js`) with the Google Ads and GA4 destinations. `gtag-snippet.html` is the exact head snippet with **Consent Mode v2 defaults set to denied for Quebec** before the tag loads, then `consent.js` updates consent when the visitor accepts. That is what Law 25 requires for non-essential cookies, and Consent Mode keeps modelled conversions flowing in Google Ads even when people decline.

Order in `<head>`:
1. Consent default (`gtag('consent','default',{...})`) – must run first.
2. `gtag.js` load.
3. `gtag('config', 'AW-XXXXXXXXX')` and `gtag('config', 'G-XXXXXXXXXX')`.
4. Phone number swap for website-call conversions (`gtag('config','AW-XXXXXXXXX/yyyy',{phone_conversion_number:'+1 514 000 0000'})`).

`events.js` fires: `click_to_call` on any `tel:` link, `generate_lead` on quote-form submit (with segment and vehicle type as parameters), `quote_started` when a visitor focuses the first form field.

## 3. Call tracking

Minimum: Google forwarding numbers on call assets + the website number swap (free, gives call duration and campaign). Recommended once spend passes ~3,000 CAD/month: a call-tracking platform (CallRail, WhatConverts) with a dynamic number pool so every landing page visit gets a unique number and calls are matched to keyword + GCLID, recorded, and scored. Import scored calls back to Google Ads as `Booked job` offline conversions.

Answer rate matters more than tracking: a missed call during the terrace deadline week is a lost season. Route ad calls to a line that is answered 7 days a week during October and November, with voicemail-to-SMS callback within 5 minutes.

## 4. Offline conversion import

`offline-conversions-template.csv` is the sheet format. Store the GCLID with every lead (the form script writes it into a hidden field), then upload weekly: Goals → Conversions → Uploads. This lets bidding learn which keywords produce booked jobs, not just calls.

## 5. Law 25 checklist (Quebec privacy)

- Consent banner in French first (English toggle), no pre-ticked boxes, refuse as easy as accept.
- Privacy policy page in French naming the person responsible for personal information (the owner by default) and listing Google Ads / GA4 / call recording.
- Announce call recording at the start of recorded calls.
- Keep the form to what you need (name, phone, email, segment, dates, postal code).
