/**
 * Weather-triggered budget boost.
 * When the 72 h forecast for Montreal shows snowfall or a hard frost, storage demand for
 * cars, boats, ATVs and terraces spikes. This script boosts the seasonal campaigns' budgets
 * and labels them so the seasonal pacer and humans can see why.
 *
 * Uses Open-Meteo (free, no key). Schedule: every 6 hours.
 */
var DRY_RUN = true;
var SNOW_BOOST = 1.35;         // multiply daily budget by this while a trigger is active
var FROST_THRESHOLD_C = -3;    // hard frost
var SNOW_THRESHOLD_CM = 2;     // snowfall over 72 h
var LABEL = 'Weather boost';
var TARGET_CAMPAIGNS = [
  'FR | Search | Vehicules hiver',
  'EN | Search | Winter vehicle',
  'FR | Search | Terrasse commercial',
  'EN | Search | Commercial patio',
];

function forecast() {
  var url = 'https://api.open-meteo.com/v1/forecast?latitude=45.5019&longitude=-73.5674' +
    '&daily=snowfall_sum,temperature_2m_min&forecast_days=3&timezone=America%2FToronto';
  var res = UrlFetchApp.fetch(url, { muteHttpExceptions: true });
  var j = JSON.parse(res.getContentText());
  var snow = 0, tmin = 99;
  for (var i = 0; i < j.daily.time.length; i++) {
    snow += j.daily.snowfall_sum[i] || 0;
    tmin = Math.min(tmin, j.daily.temperature_2m_min[i]);
  }
  return { snowCm: snow, tmin: tmin };
}

function ensureLabel() {
  var it = AdsApp.labels().withCondition("Name = '" + LABEL + "'").get();
  if (!it.hasNext() && !DRY_RUN) AdsApp.createLabel(LABEL, 'Budget boosted by weather-trigger.js', '#2E86DE');
}

function main() {
  var f = forecast();
  var trigger = f.snowCm >= SNOW_THRESHOLD_CM || f.tmin <= FROST_THRESHOLD_C;
  Logger.log('72h snow ' + f.snowCm.toFixed(1) + ' cm, min temp ' + f.tmin + ' C -> trigger=' + trigger);
  ensureLabel();

  var it = AdsApp.campaigns().withCondition("Status = ENABLED").get();
  while (it.hasNext()) {
    var c = it.next();
    if (TARGET_CAMPAIGNS.indexOf(c.getName()) < 0) continue;
    var hasLabel = false;
    var labels = c.labels().get();
    while (labels.hasNext()) if (labels.next().getName() === LABEL) hasLabel = true;
    var budget = c.getBudget();
    var amount = budget.getAmount();
    if (trigger && !hasLabel) {
      Logger.log('BOOST ' + c.getName() + ' ' + amount + ' -> ' + (amount * SNOW_BOOST).toFixed(2));
      if (!DRY_RUN) { budget.setAmount(Math.round(amount * SNOW_BOOST * 100) / 100); c.applyLabel(LABEL); }
    } else if (!trigger && hasLabel) {
      Logger.log('REVERT ' + c.getName() + ' ' + amount + ' -> ' + (amount / SNOW_BOOST).toFixed(2));
      if (!DRY_RUN) { budget.setAmount(Math.round(amount / SNOW_BOOST * 100) / 100); c.removeLabel(LABEL); }
    }
  }
}
