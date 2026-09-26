# Google Ads Scripts (automation)

Paste each file into **Google Ads → Tools → Bulk actions → Scripts**, authorize, preview, then schedule.
All scripts are read-mostly and log what they would change; set `DRY_RUN = false` to apply.

| Script | Schedule | What it does |
|---|---|---|
| `seasonal-budget-pacer.js` | Daily 06:00 | Sets each campaign's daily budget from the week-by-week seasonal calendar in `CALENDAR`, capped by the monthly budget in `MONTHLY_CAP`. Keeps you from overspending in the trough and underspending during the terrace / boat / first-snow peaks. |
| `weather-trigger.js` | Every 6 hours | Reads the Open-Meteo forecast for Montreal (no API key). When snow or hard frost is forecast within 72 h, boosts the vehicle and terrace campaigns' budgets by `SNOW_BOOST` and applies a label so you can see why. Reverts when the forecast clears. |
| `search-term-miner.js` | Daily 07:00 | Finds search terms with spend and zero conversions over the last 30 days that match a junk pattern (jobs, DIY, buy container, etc.) and adds them to the shared negative list `Negatives - Auto`. Also lists converting search terms not yet in the account so you can promote them to exact match. Emails a report. |
| `call-quality-report.js` | Weekly Monday | Reports calls by campaign, calls under 30 s (likely wrong numbers or missed), missed calls by hour so you can fix ad schedule and staffing. |
| `impression-share-guard.js` | Daily 09:00 | For the money ad groups (vehicle + terrace), reports search top impression share and lost IS (budget vs rank), and raises tCPA / budget within bounds when lost IS (budget) exceeds `MAX_LOST_IS_BUDGET` during peak weeks. |

Notes:
- Scripts use the current `AdsApp` API (Google Ads scripts). Reports use GAQL.
- Times are America/Toronto (Montreal). Set the account time zone to that before scheduling.
- Keep `DRY_RUN = true` for the first week and read the logs.
