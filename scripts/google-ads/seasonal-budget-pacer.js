/**
 * Seasonal budget pacer for a Montreal mobile self-storage account.
 * Sets daily campaign budgets from a week-by-week weighting so peak weeks
 * (terrace teardown, boat haul-out, first snow, winter-tire deadline) get more
 * and the January-February trough gets less, while respecting a monthly cap.
 *
 * Schedule: daily, 06:00 America/Toronto.
 */
var DRY_RUN = true;

// Monthly cap per campaign name pattern (CAD). Campaign names come from ads/google-ads-editor.
var MONTHLY_CAP = {
  'FR | Search | Vehicules hiver': 2600,
  'EN | Search | Winter vehicle': 700,
  'FR | Search | Terrasse commercial': 1500,
  'EN | Search | Commercial patio': 400,
  'FR | Search | Entreposage mobile': 1800,
  'EN | Search | Mobile storage': 600,
  'FR+EN | Search | Marque': 150,
  'FR+EN | Search | Concurrents': 400,
  'FR+EN | PMax | Saisonnier': 1000,
};

// ISO week weights (1.0 = average week of the month). Peak weeks push budget forward.
// Weeks are keyed by "YYYY-Www". Unlisted weeks use 1.0.
var CALENDAR = {
  '2026-W40': 1.10, // late Sept: boat haul-out starts, terrace season ending
  '2026-W41': 1.20, // Thanksgiving (CA) week, marinas busy
  '2026-W42': 1.30, // Oct 12-18: boroughs' terrace deadlines approach
  '2026-W43': 1.40, // Oct 19-25
  '2026-W44': 1.50, // Oct 26-Nov 1: most terrace removal deadlines
  '2026-W45': 1.45, // Nov 2-8: first frost / snow risk
  '2026-W46': 1.35, // Nov 9-15: second terrace deadline wave (Nov 15 boroughs)
  '2026-W47': 1.20,
  '2026-W48': 1.10, // Dec 1 winter-tire deadline: last cars stored
  '2026-W49': 0.90,
  '2026-W50': 0.70,
  '2026-W51': 0.50,
  '2026-W52': 0.40,
  '2027-W01': 0.45,
  '2027-W02': 0.50,
  '2027-W03': 0.55,
  '2027-W04': 0.60,
  '2027-W05': 0.60,
  '2027-W06': 0.65,
  '2027-W07': 0.70,
  '2027-W08': 0.75,
  '2027-W09': 0.80,
  '2027-W10': 0.90,
  '2027-W11': 1.00,
  '2027-W12': 1.10,
  '2027-W13': 1.20, // late March: spring retrievals + moving season starts
};

function isoWeek(d) {
  var date = new Date(Date.UTC(d.getFullYear(), d.getMonth(), d.getDate()));
  var day = date.getUTCDay() || 7;
  date.setUTCDate(date.getUTCDate() + 4 - day);
  var yearStart = new Date(Date.UTC(date.getUTCFullYear(), 0, 1));
  var week = Math.ceil(((date - yearStart) / 86400000 + 1) / 7);
  return date.getUTCFullYear() + '-W' + (week < 10 ? '0' + week : week);
}

function daysInMonth(d) {
  return new Date(d.getFullYear(), d.getMonth() + 1, 0).getDate();
}

function main() {
  var tz = AdsApp.currentAccount().getTimeZone();
  var now = new Date(Utilities.formatDate(new Date(), tz, 'yyyy-MM-dd HH:mm:ss'));
  var week = isoWeek(now);
  var weight = CALENDAR[week] || 1.0;
  var dim = daysInMonth(now);
  Logger.log('Week ' + week + ' weight ' + weight + ' (' + dim + ' days this month)');

  var it = AdsApp.campaigns().withCondition("Status = ENABLED").get();
  while (it.hasNext()) {
    var c = it.next();
    var cap = MONTHLY_CAP[c.getName()];
    if (!cap) continue;
    var spentMtd = c.getStatsFor('THIS_MONTH').getCost();
    var remaining = Math.max(cap - spentMtd, 0);
    var daysLeft = dim - now.getDate() + 1;
    var evenDaily = remaining / daysLeft;
    var target = Math.round(evenDaily * weight * 100) / 100;
    // Never exceed 2x the even pace (Google can spend up to 2x daily budget on a given day).
    target = Math.min(target, Math.round(evenDaily * 2 * 100) / 100);
    var current = c.getBudget().getAmount();
    Logger.log(c.getName() + ': spent ' + spentMtd.toFixed(0) + '/' + cap + ', daily ' + current + ' -> ' + target);
    if (!DRY_RUN && Math.abs(current - target) >= 1) c.getBudget().setAmount(target);
  }
}
