/**
 * One-off: removes every radius (proximity) target from the Search campaigns,
 * so only the city list stays targeted (93 cities from the owner's map, or
 * all of Quebec for Marque).
 * A campaign is skipped when it has no city or region target left, so a
 * campaign can never end up targeting the whole world.
 * Run once: Preview first (shows what would be removed, changes nothing), then Run.
 */
var NAME_CONTAINS = '| Search |';

function main() {
  var campaigns = AdsApp.campaigns()
      .withCondition("campaign.status != REMOVED")
      .withCondition("campaign.name CONTAINS '" + NAME_CONTAINS + "'")
      .get();
  var removed = 0;
  while (campaigns.hasNext()) {
    var campaign = campaigns.next();
    var name = campaign.getName();
    var cities = campaign.targeting().targetedLocations().get().totalNumEntities();
    var radii = campaign.targeting().targetedProximities().get();
    if (!radii.hasNext()) {
      Logger.log(name + ': no radius, ' + cities + ' locations targeted');
      continue;
    }
    if (cities === 0) {
      Logger.log(name + ': SKIPPED, no city targeted, the radius is its only location');
      continue;
    }
    while (radii.hasNext()) {
      var radius = radii.next();
      Logger.log(name + ': removing ' + radius.getRadius() + ' ' + radius.getRadiusUnits() +
          ' around ' + radius.getLatitude() + ', ' + radius.getLongitude() +
          ' (' + cities + ' locations stay targeted)');
      radius.remove();
      removed++;
    }
  }
  Logger.log('Radius targets removed: ' + removed);
}
