# Competitor watch (free)

A free replacement for the competitor part of paid SEO tools. It needs no API key and no account, only Python 3.

```bash
python3 tools/competitor-watch/watch.py            # scan competitors, write the report
python3 tools/competitor-watch/watch.py --suggest  # also pull Google's search suggestions for keyword ideas
```

The report lands in `tools/competitor-watch/reports/latest.md`. Each run is also saved by date, so the next run shows only what changed.

For every competitor in `competitors.json` it records:

| Check | How |
|---|---|
| Runs Google Ads? | Google Ads account IDs on the site, and Google Ads conversion or remarketing tags configured in their Google Tag Manager container |
| Tracks calls from its website? | A Google Ads website-call conversion tag configured in their container |
| Meta and Microsoft Ads | Meta pixel on the page, Microsoft Ads (UET) tag in the container |
| Promotions | Lines on their pages with %, gratuit, rabais, offre, code, jusqu'au, save, free… |
| Prices and phone numbers | Every price mention with its context, and every `tel:` number |
| Their actual ads | A direct link to Google's Ads Transparency Center for their domain in Canada |

With `--suggest`, it also collects what people actually type into Google in Canada for the seed phrases in `competitors.json`. That is the free way to find keywords.

## Add or remove a competitor

Edit `competitors.json`: a name and one to three URLs, such as the home page, the Montreal page and the promo page.

## Weekly automatic run

`.github/workflows/competitor-watch.yml` runs the scan every Monday at 7:00 (Montreal time) on GitHub, for free. It commits the new report to the repository. You can also start it by hand from the repository's **Actions** tab.

## Other free sources worth a weekly look

- **Google Ads Transparency Center:** the report gives a link per competitor. It shows every ad they run in Canada, with the text and the dates.
- **Auction Insights, inside Google Ads, once your campaigns run:** it shows who appears next to you, how often, and who outranks you. It is the most reliable free competitor data there is.
- **Meta Ad Library:** facebook.com/ads/library, country Canada, search the competitor's name.
