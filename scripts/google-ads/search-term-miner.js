/**
 * Search-term miner: auto-negatives for junk and a list of converting terms to promote.
 * Schedule: daily 07:00. Emails a report to RECIPIENTS.
 */
var DRY_RUN = true;
var RECIPIENTS = ['you@example.com'];
var NEG_LIST_NAME = 'Negatives - Auto';
var LOOKBACK = 'LAST_30_DAYS';
var MIN_COST_NO_CONV = 12;   // CAD spent with zero conversions before we act
var MIN_CLICKS_NO_CONV = 6;

// Junk intent patterns (FR + EN). Matched against the whole search term, case-insensitive.
var JUNK = [
  /\b(emploi|emplois|job|jobs|carri[eè]re|salaire|recrut|embauche|hiring)\b/i,
  /\b(gratuit|free)\b/i,
  /\b(vente|acheter|achat|à vendre|a vendre|buy|for sale|sale)\b.*\b(conteneur|container)\b/i,
  /\b(conteneur|container)\b.*\b(vente|acheter|achat|à vendre|a vendre|buy|for sale|sale)\b/i,
  /\b(maritime|shipping|d[ée]chets|waste|dumpster|poubelle|recyclage)\b/i,
  /\b(plan|plans|diy|construire|fabriquer|build|how to|comment faire)\b/i,
  /\b(ikea|amazon|costco|canadian tire|walmart|home depot|rona|kijiji|marketplace)\b/i,
  /\b(garde-?meuble|garde meuble)\b.*\b(paris|france|belgique|bruxelles)\b/i,
  /\b(toronto|ottawa|qu[ée]bec city|ville de qu[ée]bec|sherbrooke|trois-rivi[eè]res|gatineau|vancouver|calgary)\b/i,
  /\b(logiciel|software|app|application|api)\b/i,
  /\b(d[ée]finition|definition|wikipedia|c'est quoi|what is)\b/i,
  /\b(cours|formation|training|certification)\b/i,
];

function gaql(q) { return AdsApp.report(q).rows(); }

function main() {
  var rows = gaql(
    "SELECT campaign.name, ad_group.name, search_term_view.search_term, metrics.clicks, metrics.cost_micros, metrics.conversions, metrics.all_conversions " +
    "FROM search_term_view WHERE segments.date DURING " + LOOKBACK + " AND campaign.advertising_channel_type = 'SEARCH'"
  );
  var toNeg = {}, converting = [], wasteful = [];
  while (rows.hasNext()) {
    var r = rows.next();
    var term = r['search_term_view.search_term'];
    var cost = Number(r['metrics.cost_micros']) / 1e6;
    var clicks = Number(r['metrics.clicks']);
    var conv = Number(r['metrics.conversions']) + Number(r['metrics.all_conversions']);
    if (conv > 0) { converting.push({ term: term, cost: cost, conv: conv, campaign: r['campaign.name'] }); continue; }
    var junk = JUNK.some(function (re) { return re.test(term); });
    if (junk) toNeg[term] = (toNeg[term] || 0) + cost;
    else if (cost >= MIN_COST_NO_CONV && clicks >= MIN_CLICKS_NO_CONV) wasteful.push({ term: term, cost: cost, clicks: clicks, campaign: r['campaign.name'] });
  }

  var list = getOrCreateList();
  var added = [];
  for (var t in toNeg) {
    added.push(t + ' (' + toNeg[t].toFixed(2) + ' CAD)');
    if (!DRY_RUN && list) list.addNegativeKeyword('[' + t + ']');
  }
  wasteful.sort(function (a, b) { return b.cost - a.cost; });
  converting.sort(function (a, b) { return b.conv - a.conv; });

  var body = 'Search term miner (' + LOOKBACK + ')' + (DRY_RUN ? ' [DRY RUN]' : '') + '\n\n' +
    'ADDED AS EXACT NEGATIVES (junk patterns):\n' + (added.join('\n') || 'none') + '\n\n' +
    'REVIEW: spend with no conversions (consider negatives):\n' +
    wasteful.slice(0, 40).map(function (w) { return w.cost.toFixed(2) + ' CAD, ' + w.clicks + ' clicks | ' + w.term + ' | ' + w.campaign; }).join('\n') + '\n\n' +
    'PROMOTE: converting search terms (add as exact keywords in the right ad group):\n' +
    converting.slice(0, 40).map(function (c) { return c.conv + ' conv, ' + c.cost.toFixed(2) + ' CAD | ' + c.term + ' | ' + c.campaign; }).join('\n');
  Logger.log(body);
  if (RECIPIENTS[0] !== 'you@example.com') MailApp.sendEmail(RECIPIENTS.join(','), 'Google Ads: search term miner', body);
}

function getOrCreateList() {
  var it = AdsApp.negativeKeywordLists().withCondition("Name = '" + NEG_LIST_NAME + "'").get();
  if (it.hasNext()) return it.next();
  if (DRY_RUN) return null;
  var list = AdsApp.newNegativeKeywordListBuilder().withName(NEG_LIST_NAME).build().getResult();
  var camps = AdsApp.campaigns().withCondition("Status = ENABLED").get();
  while (camps.hasNext()) camps.next().addNegativeKeywordList(list);
  return list;
}
