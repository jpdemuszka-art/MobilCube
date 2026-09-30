# MobilCube — Google Ads program for the fall/winter 2026-2027 season

A complete, import-ready Google Ads program for MobilCube (mobile self-storage, Boucherville / Greater Montreal), built on a competitive analysis of the Montreal storage market done on 2026-09-26.

**Launching now? Read [`docs/08-launch-analysis-2026-09-30.md`](docs/08-launch-analysis-2026-09-30.md) first** (5,000 $/month plan, site blockers, competitor ad scan, verified keywords). Then [`docs/00-start-here.md`](docs/00-start-here.md). In the Google Ads campaign wizard, use [`docs/05-campaign-wizard-answers.md`](docs/05-campaign-wizard-answers.md).

| Folder | What is inside |
|---|---|
| `docs/` | Competitive analysis with sources, the strategy, budget and forecast, seasonal calendar, wizard answers, Quebec compliance rules |
| `ads/google-ads-editor/` | Nine CSVs to bulk-import 8 campaigns, 32 ad groups, 482 keywords (405 enabled), 32 responsive search ads, 331 shared negatives and all assets with Google Ads Editor |
| `ads/keywords/`, `ads/negatives/`, `ads/copy/` | Full keyword universe (FR + EN, with estimated volumes and CPCs), negative lists, the ad copy deck |
| `ads/build_import.py` | Regenerates everything above and refuses copy that breaks Google's character limits |
| `landing/` | Bilingual (French-first) landing pages per segment: winter vehicles, commercial terraces, mobile storage, plus hub, thank-you and Law 25 privacy pages |
| `tracking/` | Google tag with Consent Mode v2, consent banner, conversion events, offline-conversion template, call-tracking setup |
| `scripts/google-ads/` | Five Google Ads Scripts: seasonal budget pacer, weather trigger, search-term miner, call-quality report, impression-share guard |
| `tools/gemini-creatives/` | Gemini image generator (`gemini-3.1-flash-image` by default) that produces every Google Ads image size from a 14-scene Montreal prompt library |

## The strategy in one paragraph

Competitors hide prices, ban or restrict vehicles, store far from the South Shore and market in English first. MobilCube publishes prices, can take a car, sits in Boucherville and speaks French. So: French-first Search campaigns split by segment (winter vehicles, commercial terraces, mobile storage) with small English campaigns for the West Island; every click lands on a segment page with a visible price and a call button; calls are the primary conversion; scripts push budget into the six weeks between the first terrace deadline and the December 1 winter-tire deadline; Performance Max with Gemini imagery only after Search reaches 30 conversions a month.

## Quick start

```bash
# campaign files
python3 ads/build_import.py

# ad images (needs GEMINI_API_KEY in tools/gemini-creatives/.env)
cd tools/gemini-creatives && npm install && npm run gen:all && npm run check
```

Then follow the launch sequence in `docs/00-start-here.md`.
