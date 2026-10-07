# 11 · Marketing multiplateforme : quoi activer pour maximiser les conversions

Préparé le 7 octobre 2026 pour MobilCube.

La plupart des gens ne réservent pas à la première visite. Ils comparent un prix, en parlent à la maison, puis reviennent. Le marketing multiplateforme sert à revoir ces personnes sur Facebook, Instagram, YouTube et Gmail, avec la même offre que dans l'annonce Google, jusqu'à ce qu'elles réservent ou appellent. Pour y arriver, il faut 3 choses :

1. **Les mêmes balises sur le site pour chaque plateforme.** Chaque plateforme doit savoir qui a visité le site et qui a réservé.
2. **Des audiences partagées.** Par exemple : les visiteurs qui n'ont pas réservé, les clients actuels, les gens qui ont vu une vidéo.
3. **Une seule mesure.** Toutes les réservations sont comptées dans GA4 et Google Ads, pour savoir quelle plateforme rapporte vraiment.

## Ce que vous avez déjà (vérifié le 7 octobre)

| Élément | État |
|---|---|
| 8 campagnes Google Ads (recherche) en ligne, annonces vers la page de réservation | ✅ |
| Conversion « Réservation - formulaire » qui fonctionne (GTM-M69QW6VC) | ✅ |
| 4 listes de reciblage créées automatiquement dans Google Ads : « All Users of Mobilcube », « Returning visitors », « New visitors », « Purchasers of Mobilcube » | ✅ créées, mais vides pour l'instant : elles se remplissent avec les visites |
| Google Analytics 4 (G-640H58NDHN) sur le site | ✅ |
| Page Facebook (facebook.com/MobilCube) et Instagram (@mobilcube_canada), liées depuis le site | ✅ |
| Pixel Meta (Facebook/Instagram) sur le site | ❌ absent |
| Balise Microsoft Advertising (UET) sur le site | ❌ absente |
| Meta Ads et Microsoft Advertising connectés à Supermetrics | ❌ seul Google Ads est connecté |

## Ce qu'il faut activer, dans cet ordre

### 1. Mesure commune (cette semaine, gratuit)

1. **Terminez le suivi des appels** : étapes 2 à 5 de `docs/10-suivi-conversions.md`. Ça prend 20 minutes.
2. **Liez GA4 à Google Ads** : GA4 → **Admin** → **Associations de produits** → **Google Ads** → associez 194-768-4780, et activez **Publicité personnalisée**. Les audiences GA4 deviennent alors utilisables dans Google Ads.
3. **Activez Google Signals** : GA4 → **Admin** → **Collecte de données**. Une personne qui voit l'annonce sur son cellulaire puis réserve sur son ordinateur est comptée comme une seule personne.
4. **Ajoutez des UTM sur tous les liens hors Google** (bio Instagram, publications Facebook, courriels), par exemple `?utm_source=instagram&utm_medium=social&utm_campaign=hiver-auto`. GA4 attribue alors chaque réservation à la bonne source.
5. **Configurez CookieYes** : activez Google Consent Mode et classez le pixel Meta et la balise Microsoft dans la catégorie **Publicité**. Avec la Loi 25, ces balises ne se déclenchent qu'après consentement.

### 2. Reciblage Google (semaine 2, 5 à 8 $/jour)

1. **Ajoutez les listes de reciblage aux 8 campagnes de recherche, en mode Observation.** Observation ne limite pas la diffusion. Elle montre si les anciens visiteurs réservent davantage. Si oui, on augmente l'enchère de 20 à 30 % pour eux. Je peux le faire pour vous.
2. **Créez une campagne Demand Gen « Reciblage »** sur YouTube (Shorts), Discover et Gmail :
   - **Audience** : « All Users of Mobilcube », sans les personnes qui ont déjà réservé.
   - **Matériel** : 3 à 5 photos (cube livré dans une entrée, entrepôt chauffé, auto à l'intérieur) en formats 1,91:1, 1:1 et 4:5. Une vidéo de 15 secondes est un plus.
   - **Messages** : « Vous comparez encore ? Livraison 300 $, 15 km inclus » et, cet automne, « Avant la première neige : auto 160 $/mois, moto 80 $/mois ».

   Google exige une centaine d'utilisateurs actifs dans une liste avant de s'en servir. À 50 $/jour sur l'entreposage mobile, ce minimum devrait être atteint en quelques jours.

### 3. Facebook et Instagram (semaines 2 à 3, 10 à 15 $/jour)

1. **Créez le pixel** dans Meta Business Suite : **Gestionnaire d'événements** → **Connecter des données** → **Web** → **Pixel**.
2. **Installez-le dans GTM-M69QW6VC**, avec le modèle « Facebook Pixel » de la galerie de modèles GTM :
   - `PageView` sur toutes les pages ;
   - `ViewContent` sur la page des prix ;
   - `Lead` sur l'événement `wpforms_envoi_reussi`, c'est-à-dire le formulaire envoyé ;
   - `Contact` sur un clic sur un lien `tel:`.

   Je peux vous préparer ces balises dans un fichier d'import GTM sans doublon avec la réservation déjà en place.
3. **Créez les audiences** :
   - visiteurs du site des 30 derniers jours, sans ceux qui ont réservé ;
   - personnes qui ont interagi avec la page Facebook ou le compte Instagram (90 jours) ;
   - personnes qui ont vu au moins la moitié de vos vidéos ;
   - plus tard, une audience similaire (« lookalike ») de 1 % au Québec, à partir de votre liste de clients. À faire seulement si votre politique de confidentialité le permet (Loi 25).
4. **Lancez 2 campagnes avec l'objectif Prospects**, optimisées sur l'événement `Lead` :
   - **Reciblage** (5 à 7 $/jour) : les audiences ci-dessus, avec les prix et le bouton « Réserver ».
   - **Prospection locale** (5 à 8 $/jour) : les mêmes villes que Google, 25 à 65 ans, en Reels 9:16 (livraison d'un cube) et en carrousel de prix. Thème actuel : entreposage d'auto et de moto pour l'hiver.
5. **Plus tard : l'API Conversions de Meta.** Elle récupère les réservations que les bloqueurs de publicités cachent au pixel. On l'ajoute quand le pixel fonctionne et que les premières réservations arrivent.

### 4. Microsoft Advertising, ou Bing (semaine 3, 3 à 5 $/jour)

1. **Importez vos campagnes Google** : Microsoft Advertising → **Importer** → **Google Ads**, avec une synchronisation hebdomadaire. Les mots-clés, annonces et villes sont repris.
2. **Ajoutez la balise UET dans GTM-M69QW6VC** et un objectif « Réservation » sur l'événement `wpforms_envoi_reussi`.

Bing représente une petite part des recherches, surtout sur ordinateur, mais ses clics coûtent souvent moins cher que sur Google.

### 5. Présence locale (en continu, gratuit)

- **Liez votre fiche Google Business Profile à Google Ads** (Composants → Lieu). L'adresse et la carte s'affichent alors dans les annonces. La conversion « Local actions - Directions » existe déjà dans le compte.
- **Demandez un avis Google après chaque livraison**, par un lien envoyé par texto. Les étoiles aident à la fois les annonces et la recherche locale.

### 6. Vos contacts : courriel et texto (mois 2)

- **Relancez les demandes qui n'ont pas abouti** : un courriel le lendemain, puis un autre une semaine plus tard, avec l'offre de la saison.
- **Rappelez la saison à vos anciens clients** en septembre (auto et moto en hiver) et en avril (déménagement du 1er juillet, rénovations).
- **Importez votre liste de clients** dans Google (Customer Match, si le compte y est admissible) et dans Meta (audience personnalisée). Ça permet de les exclure des annonces de prospection ou de trouver des profils semblables. À faire seulement avec le consentement prévu par votre politique de confidentialité.
- **Plus tard : importez les contrats signés dans Google Ads** (« conversions améliorées pour les prospects »). Google apprend alors à viser les gens qui signent vraiment, pas seulement ceux qui remplissent le formulaire.

## Le même message partout, selon la saison

| Période | Thème | Google | Facebook et Instagram |
|---|---|---|---|
| Octobre à mi-décembre | Auto et moto en entrepôt chauffé : 160 $ et 80 $/mois | Véhicules hiver (recherche), plus reciblage Demand Gen | Reels « votre auto au chaud », reciblage des visiteurs de la page des prix |
| Avril à juin | Déménagement du 1er juillet et rénovations | Entreposage mobile (recherche) | Prospection locale, plus reciblage |
| Toute l'année | Mini-entrepôt livré chez vous | Entreposage mobile (recherche) | Reciblage seulement |

## Budget de départ

Les terrasses n'ont presque aucune recherche (voir l'analyse des mots-clés du 7 octobre). Leurs 16 $/jour, soit 12 $ en français et 4 $ en anglais, peuvent financer le démarrage sans augmenter le budget total :

| Canal | Budget par jour |
|---|---|
| Reciblage Google (Demand Gen) | 5 à 8 $ |
| Facebook et Instagram (reciblage, puis prospection) | 10 à 15 $ |
| Microsoft Advertising | 3 à 5 $ |

Après 4 semaines, comparez le coût par réservation dans Google Ads, Meta et GA4. Augmentez le budget du canal le moins cher et réduisez celui des autres.

## Ce que je peux faire pour vous

- **Google, dès maintenant** : ajouter les listes de reciblage en Observation aux 8 campagnes. Je peux aussi créer la campagne Demand Gen en pause dès que vous m'envoyez 3 à 5 photos.
- **Meta et Microsoft** : connectez-les dans Supermetrics (https://hub.supermetrics.com/token-management?team_id=1244765). Je pourrai alors créer les campagnes en pause et suivre les résultats des 3 plateformes dans un seul rapport.
- **GTM** : préparer un fichier d'import avec le pixel Meta et la balise UET, sans toucher à la balise de réservation déjà en ligne.
