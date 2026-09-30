/**
 * Impression-share guard for the money campaigns during peak weeks.
 * Reports top-of-page rate and lost impression share (budget / rank). During peak weeks,
 * if IS lost to budget exceeds MAX_LOST_IS_BUDGET, raises the campaign budget by STEP (bounded).
 * Schedule: daily 09:00.
 */
var DRY_RUN = true;
var MAX_LOST_IS_BUDGET = 0.20;    // 20 %
var STEP = 1.15;                  // +15 % per day at most
// Ceilings for the 5,000 $/month launch (about 1.5x the launch daily budget). The pacer's monthly caps still apply.
var HARD_CAP_DAILY = { 'FR | Search | Entreposage mobile': 75, 'FR | Search | Vehicules hiver': 70, 'FR | Search | Terrasse commercial': 20, 'EN | Search | Winter vehicle': 18, 'EN | Search | Commercial patio': 6 };
var PEAK_WEEKS = ['2026-W42', '2026-W43', '2026-W44', '2026-W45', '2026-W46', '2026-W47', '2026-W48'];

function isoWeek(d) {
  var date = new Date(Date.UTC(d.getFullYear(), d.getMonth(), d.getDate()));
  var day = date.getUTCDay() || 7;
  date.setUTCDate(date.getUTCDate() + 4 - day);
  var yearStart = new Date(Date.UTC(date.getUTCFullYear(), 0, 1));
  var week = Math.ceil(((date - yearStart) / 86400000 + 1) / 7);
  return date.getUTCFullYear() + '-W' + (week < 10 ? '0' + week : week);
}

function main() {
  var week = isoWeek(new Date());
  var peak = PEAK_WEEKS.indexOf(week) >= 0;
  var rows = AdsApp.report(
    "SELECT campaign.name, metrics.search_impression_share, metrics.search_top_impression_share, metrics.search_absolute_top_impression_share, " +
    "metrics.search_budget_lost_impression_share, metrics.search_rank_lost_impression_share, metrics.cost_micros, metrics.conversions " +
    "FROM campaign WHERE segments.date DURING LAST_7_DAYS AND campaign.status = 'ENABLED' AND campaign.advertising_channel_type = 'SEARCH'"
  ).rows();
  while (rows.hasNext()) {
    var r = rows.next();
    var name = r['campaign.name'];
    var lostBudget = Number(r['metrics.search_budget_lost_impression_share']);
    var lostRank = Number(r['metrics.search_rank_lost_impression_share']);
    Logger.log(name + ' | IS ' + pct(r['metrics.search_impression_share']) + ' top ' + pct(r['metrics.search_top_impression_share']) +
      ' abs-top ' + pct(r['metrics.search_absolute_top_impression_share']) + ' | lost budget ' + pct(lostBudget) + ' lost rank ' + pct(lostRank) +
      ' | cost ' + (Number(r['metrics.cost_micros']) / 1e6).toFixed(0) + ' conv ' + r['metrics.conversions']);
    if (!peak || !(name in HARD_CAP_DAILY)) continue;
    if (lostBudget > MAX_LOST_IS_BUDGET) {
      var camp = AdsApp.campaigns().withCondition("Name = '" + name + "'").get().next();
      var cur = camp.getBudget().getAmount();
      var next = Math.min(Math.round(cur * STEP * 100) / 100, HARD_CAP_DAILY[name]);
      Logger.log('  -> peak week and lost IS (budget) ' + pct(lostBudget) + ': budget ' + cur + ' -> ' + next);
      if (!DRY_RUN && next > cur) camp.getBudget().setAmount(next);
    }
    if (lostRank > 0.4) Logger.log('  -> lost IS (rank) is high: improve ad strength / landing page or raise tCPA, not budget.');
  }
}
function pct(v) { var n = Number(v); return isNaN(n) ? 'n/a' : (n * 100).toFixed(0) + '%'; }
