# 05 · What to type into the Google Ads campaign wizard

You are in the flow that starts with "Describe your business to get better campaign suggestions". Google uses that text to generate headlines, descriptions and images and to pick audiences, so it should read like a factual brief, not a slogan. Below: exactly what to paste, then the settings to choose on the following screens.

## Screen 1 — "Describe what makes your business unique" (max 3,000 characters)

Paste the French version if the wizard's campaign language is French (recommended for the first campaign), the English version for the English campaign. Do not paste both into one campaign.

### French (1,907 characters)

```
MobilCube est une entreprise d'entreposage mobile basée à Boucherville, sur la Rive-Sud de Montréal. Nous livrons un conteneur d'entreposage en acier CORTEN de 20 pieds (environ 160 pi², 1 165 pi³, soit le contenu d'un appartement 5 ½) directement dans l'entrée du client ou sur son site commercial, partout dans le Grand Montréal (Longueuil, Brossard, Saint-Hubert, Sainte-Julie, Varennes, Montréal, Laval, Rive-Nord) et ailleurs au Québec. Le client charge au niveau du sol, à son rythme, sans double manutention. Il garde ensuite l'unité chez lui avec accès 24 h sur 24, ou nous la transportons dans notre entrepôt chauffé et sécurisé de Boucherville.

Nos prix sont affichés : 350 $ par mois sans engagement, ou 300 $, 270 $, 220 $ et 180 $ par mois avec engagement de 3, 6, 12 ou 24 mois; entreposage en entrepôt chauffé à 19,75 $ de plus par mois; livraison ou ramassage 300 $ par déplacement, 15 km inclus à partir de Boucherville. Réservation et prix exact en ligne en moins de 60 secondes, sans créer de compte. Dépôt de 200 $ remboursé après inspection. Aucun frais d'administration mensuel.

Services : entreposage mobile résidentiel (déménagement, rénovation, sinistre), entreposage hivernal de véhicules dans votre entrée (voiture, voiture de collection, moto, VTT, motoneige, motomarine, remorque), entreposage saisonnier pour commerces (mobilier de terrasse de restaurants, bars, cafés et hôtels, chauffe-terrasses, parasols, bacs à fleurs, mobilier de piscine de condos, surplus d'inventaire), conteneurs de chantier pour entrepreneurs, logistique de plateaux de tournage. Service en français et en anglais. Ce qui nous distingue des autres : un seul grand conteneur de 20 pieds au lieu de plusieurs petits cubes, des prix publiés, un entrepôt chauffé sur la Rive-Sud, l'accès 24/7 à vos biens chez vous et la possibilité d'entreposer un véhicule, ce que la plupart des concurrents refusent.
```

### English (1,668 characters)

```
MobilCube is a mobile self-storage company based in Boucherville on Montreal's South Shore. We deliver a 20-foot CORTEN steel storage container (about 160 sq ft, 1,165 cu ft, the contents of a 5 ½ apartment) to the customer's driveway or business site across Greater Montreal (Longueuil, Brossard, Saint-Hubert, Montreal, West Island, Laval, North Shore) and elsewhere in Quebec. Customers load at ground level, at their own pace, with no double handling. They keep the unit on site with 24/7 access, or we move it to our heated, secure warehouse in Boucherville.

Our prices are published: $350 per month with no commitment, or $300, $270, $220 and $180 per month with a 3, 6, 12 or 24-month commitment; heated warehouse storage for $19.75 more per month; delivery or pickup $300 per movement including 15 km from Boucherville. Exact price and booking online in under 60 seconds, no account needed. $200 deposit refunded after inspection. No monthly administration fee.

Services: residential mobile storage (moving, renovation, post-disaster), winter vehicle storage in your own driveway (cars, collector cars, motorcycles, ATVs, snowmobiles, personal watercraft, trailers), seasonal storage for businesses (restaurant, bar, café and hotel patio furniture, patio heaters, umbrellas, planters, condo pool furniture, inventory overflow), jobsite containers for contractors, film-set logistics. Service in French and English. What sets us apart: one large 20-foot container instead of several small cubes, published prices, a heated warehouse on the South Shore, 24/7 access to your belongings at home, and the ability to store a vehicle, which most competitors refuse.
```

Why this replaces your draft: it removes claims that need proof ("fireproof", "airtight", "revolutionize"), adds the words people actually search (entreposage mobile, conteneur, hiver, moto, VTT, terrasse, Rive-Sud, Longueuil, Brossard), states the prices Google can turn into assets, and names the four differentiators competitors cannot copy. Keep "160 sq ft" only after you settle the 148 vs 160 inconsistency on the site.

## Screen 1 — "What specific products or services are you advertising?" (up to 20)

French campaign:
```
entreposage mobile
conteneur d'entreposage livré
location de conteneur 20 pieds
entreposage hiver voiture
remisage voiture de collection
entreposage moto hiver
entreposage VTT
entreposage motoneige
entreposage motomarine
entreposage mobilier de terrasse
entreposage saisonnier commercial
entreposage d'inventaire
conteneur de chantier
entreposage déménagement
entreposage rénovation
entreposage chauffé Boucherville
entreposage Rive-Sud
entreposage Longueuil Brossard
entreposage Montréal
entreposage Laval
```

English campaign:
```
mobile storage rental
portable storage container
20 ft storage container rental
winter car storage
classic car storage
motorcycle storage
ATV storage
snowmobile storage
jet ski storage
patio furniture storage
restaurant terrace storage
commercial seasonal storage
inventory storage
jobsite storage container
moving container
renovation storage
heated storage Boucherville
South Shore storage
West Island storage
Montreal storage
```

## Screen 1 — "Select web pages to get relevant image suggestions"

Use only your own pages; Google cannot pull usable imagery from Instagram or Facebook and those links add nothing:
```
https://www.mobilcube.com/fr/
https://www.mobilcube.com/fr/prix-location/
https://www.mobilcube.com/fr/capacites-stockage/
https://www.mobilcube.com/fr/cas-usage/
```
Then upload the Gemini images from `tools/gemini-creatives/out/` (1200×1200 and 1200×628) instead of relying on the suggestions.

## Following screens — choose these

| Screen | Choose | Not this |
|---|---|---|
| Campaign objective | **Leads** | Sales, Website traffic |
| Conversion goals | Calls from ads, Website calls, Submit lead form (Quote form), Booking | Page views, clicks |
| Campaign type | **Search** | Performance Max (the wizard pushes it; keep for phase 2) |
| Ways to reach goal | Phone calls + Website visits | App |
| Bidding | Clicks, with **max CPC bid limit** 3.50 $ (FR vehicle) / 4.50 $ (FR mobile) / 6.00 $ (EN) | Conversions (no data yet) |
| Networks | Google Search only | Search partners, Display Network |
| Locations | Add the municipalities in `02-google-ads-strategy.md` §3; option **Presence** | Radius around Canada, "presence or interest" |
| Languages | leave as suggested; write ads in the campaign's language only | mixing FR and EN in one campaign |
| Audience segments | Observation only | Targeting |
| AI Max / broad match | **Off** | On |
| Keywords | paste from `ads/keywords/` in phrase and exact form | Google's suggested broad list |
| Ads | paste the RSA for that ad group from `ads/copy/` | let Google generate |
| Assets | sitelinks, callouts, call, location, price, images | skip |
| Budget | 85 $/day vehicle FR, 50 $ terrace FR, 60 $ mobile FR, 25/15/20 $ EN | Google's "recommended" figure |

Faster route: skip the wizard entirely, import `ads/google-ads-editor/*.csv` with Google Ads Editor, then only set conversions, locations and budgets in the web UI.
