/**
 * Weekly call quality report: calls by campaign, short calls, missed calls by hour.
 * Requires call reporting enabled on the call asset (Google forwarding number).
 * Schedule: weekly, Monday 08:00.
 */
var RECIPIENTS = ['you@example.com'];
var SHORT_CALL_SECONDS = 30;

function main() {
  var rows = AdsApp.report(
    "SELECT campaign.name, call_view.start_call_date_time, call_view.call_duration_seconds, call_view.call_status, call_view.type " +
    "FROM call_view WHERE segments.date DURING LAST_7_DAYS"
  ).rows();
  var byCampaign = {}, missedByHour = {}, total = 0, shortCalls = 0, missed = 0;
  while (rows.hasNext()) {
    var r = rows.next();
    total++;
    var c = r['campaign.name'];
    byCampaign[c] = byCampaign[c] || { calls: 0, received: 0, avg: 0, dur: 0 };
    byCampaign[c].calls++;
    var dur = Number(r['call_view.call_duration_seconds']);
    if (r['call_view.call_status'] === 'RECEIVED') { byCampaign[c].received++; byCampaign[c].dur += dur; }
    if (dur > 0 && dur < SHORT_CALL_SECONDS) shortCalls++;
    if (r['call_view.call_status'] === 'MISSED') {
      missed++;
      var hour = String(r['call_view.start_call_date_time']).substr(11, 2);
      missedByHour[hour] = (missedByHour[hour] || 0) + 1;
    }
  }
  var lines = ['Calls last 7 days: ' + total + ' | missed: ' + missed + ' | under ' + SHORT_CALL_SECONDS + 's: ' + shortCalls, ''];
  for (var k in byCampaign) {
    var b = byCampaign[k];
    lines.push(k + ': ' + b.calls + ' calls, ' + b.received + ' answered, avg ' + (b.received ? Math.round(b.dur / b.received) : 0) + 's');
  }
  lines.push('', 'Missed calls by hour (fix staffing or ad schedule):');
  Object.keys(missedByHour).sort().forEach(function (h) { lines.push('  ' + h + ':00  ' + missedByHour[h]); });
  var body = lines.join('\n');
  Logger.log(body);
  if (RECIPIENTS[0] !== 'you@example.com') MailApp.sendEmail(RECIPIENTS.join(','), 'Google Ads: weekly call quality', body);
}
