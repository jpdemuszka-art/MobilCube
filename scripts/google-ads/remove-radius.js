/**
 * One-off: removes every radius (proximity) target from the account's campaigns,
 * so only the city list stays targeted (93 cities from the owner's map, or
 * all of Quebec for Marque).
 * A campaign is skipped when it has no city or region target left, so a
 * campaign can never end up targeting the whole world.
 * No selector condition: campaigns are filtered in code, and every step is logged.
 * Preview logs what would be removed and changes nothing; Run applies it.
 */
function main() {
  Logger.log('Début du script');
  var campaigns = AdsApp.campaigns().get();
  var seen = 0, removed = 0;
  while (campaigns.hasNext()) {
    var campaign = campaigns.next();
    if (campaign.isRemoved()) continue;
    seen++;
    var name = campaign.getName();
    var radii = [];
    var it = campaign.targeting().targetedProximities().get();
    while (it.hasNext()) radii.push(it.next());
    var places = campaign.targeting().targetedLocations().get().totalNumEntities();
    Logger.log(name + ' : ' + places + ' villes ou régions, ' + radii.length + ' rayon(s)');
    if (radii.length === 0) continue;
    if (places === 0) {
      Logger.log('  -> ignorée : le rayon est sa seule zone ciblée');
      continue;
    }
    for (var i = 0; i < radii.length; i++) {
      var label = radii[i].getRadius() + ' ' + radii[i].getRadiusUnits();
      try {
        radii[i].remove();
        removed++;
        Logger.log('  -> rayon de ' + label + ' retiré');
      } catch (e) {
        Logger.log('  -> ERREUR sur le rayon de ' + label + ' : ' + e);
      }
    }
  }
  Logger.log('Campagnes lues : ' + seen + ' | rayons retirés : ' + removed);
  if (AdsApp.getExecutionInfo().isPreview()) {
    Logger.log('MODE APERÇU : rien n\'a été modifié. Cliquez sur « Exécuter » pour appliquer.');
  }
}
