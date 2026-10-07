# 10 · Suivi des conversions : réservations et appels (guide pas à pas)

Préparé le 7 octobre 2026 pour le compte Google Ads MobilCube (194-768-4780). Mis à jour le même jour après une vérification du site et du compte. Temps restant : environ 20 minutes.

## Où on en est (vérifié le 7 octobre)

| Élément | État |
|---|---|
| Toutes les annonces mènent à la page de réservation : `/fr/formulaire-reservation/` en français, `/en/booking-form/` en anglais | ✅ |
| Bouton d'appel (450-641-6498) sur les 8 campagnes de recherche | ✅ |
| Option « Présence » sur les 9 campagnes : pas d'annonces aux gens hors des zones ciblées | ✅ |
| Conversion « Réservation - formulaire » dans Google Ads (ID 7827804857) | ✅ créée |
| Conteneur **GTM-M69QW6VC** publié sur le site (version 2) | ✅ |
| Dans ce conteneur : balise de conversion Réservation (AW-18484934240, libellé `cdedCLmly5QdEODspu5E`), déclenchée quand le formulaire WPForms est envoyé avec succès | ✅ en ligne |
| Dans ce conteneur : linker de conversion sur toutes les pages, et écouteur WPForms (événement `wpforms_envoi_reussi`) | ✅ en ligne |
| Conversion « Appel depuis l'annonce », avec rapports sur les appels | ❌ à créer (étape 2) |
| Conversion « Clic téléphone sur le site » et sa balise GTM | ❌ à créer (étape 3) |
| « Clicks to call » de la campagne intelligente en conversion secondaire | ❌ (étape 4) |
| Google Consent Mode dans CookieYes | à vérifier (étape 5) |

**Important :** le site ne charge plus l'ancien conteneur GTM-K3G9FKRW. N'importez pas `tracking/gtm-import-mobilcube-google-ads.json` dans GTM-M69QW6VC : ce fichier contient une deuxième balise de réservation, et chaque réservation serait comptée deux fois. Il ne sert plus que de modèle pour un conteneur vide.

Les 3 conversions visées :

| Conversion | Ce qui la déclenche | Valeur suggérée | Principale |
|---|---|---|---|
| Réservation - formulaire | Le formulaire de réservation (WPForms) est envoyé avec succès | 50 $ | Oui |
| Appel depuis l'annonce | Un appel de 45 secondes ou plus via le bouton d'appel d'une annonce | 60 $ | Oui |
| Clic téléphone sur le site | Un clic sur le numéro de téléphone du site (lien « tel: ») | 10 $ | Oui |

Je ne peux pas créer de conversions avec le connecteur Google Ads que j'utilise, et je n'ai pas accès à votre Tag Manager. Les étapes ci-dessous se font en quelques clics.

## Étape 1 : tester la conversion Réservation (5 min)

1. Ouvrez https://tagmanager.google.com, puis le conteneur **GTM-M69QW6VC**.
2. Cliquez sur **Prévisualiser**, entrez `https://www.mobilcube.com/fr/formulaire-reservation/` et envoyez une demande test (indiquez « TEST » dans le nom).
3. Dans la fenêtre de prévisualisation, la balise de conversion Google Ads doit apparaître sous **Tags Fired** juste après l'événement `wpforms_envoi_reussi`.
4. Dans Google Ads → **Objectifs** → **Conversions**, vérifiez que « Réservation - formulaire » compte **Une** conversion par clic et a une valeur (50 $ suggéré). Son état passe à **« Enregistrement des conversions »** dans les 24 à 48 h.

## Étape 2 : appels depuis l'annonce (5 min)

1. Google Ads → **Objectifs** → **Conversions** → **+ Créer une action de conversion** → **Appels téléphoniques** → **Appels depuis les annonces utilisant des composants Appel**.
2. Remplissez :
   - Nom : `Appel depuis l'annonce`
   - Durée minimale : **45 secondes**
   - Valeur : 60 $
   - Nombre : **Une**
3. Enregistrez. Aucune balise n'est nécessaire.
4. Activez les **rapports sur les appels** : **Admin** → **Paramètres du compte** → **Rapports sur les appels** → **Activés**. Google affiche alors un numéro de transfert gratuit sur le bouton d'appel, ce qui permet de mesurer la durée de chaque appel.

## Étape 3 : clic sur le numéro du site (10 min)

**Dans Google Ads**
1. **+ Créer une action de conversion** → **Appels téléphoniques** → **Clics sur votre numéro sur votre site Web mobile**.
2. Remplissez :
   - Nom : `Clic téléphone sur le site`
   - Valeur : 10 $
   - Nombre : **Une**
3. Enregistrez, choisissez **Utiliser Google Tag Manager**, puis notez le **libellé de conversion**. L'ID de conversion est le même que pour la réservation : 18484934240.

**Dans GTM-M69QW6VC**
1. **Variables** → **Configurer** → cochez **Click URL**.
2. **Balises** → **Nouvelle** → **Suivi des conversions Google Ads**.
   - ID de conversion : `18484934240`
   - Libellé : celui que vous venez de noter
3. Déclencheur : **Nouveau** → **Clic - Liens uniquement** → **Certains clics sur des liens** → `Click URL` **commence par** `tel:`.
4. Nommez la balise `Google Ads - Conversion - Clic téléphone`, puis enregistrez.
5. **Prévisualiser**, puis cliquez sur le numéro de téléphone du site : la balise doit apparaître sous **Tags Fired**.
6. **Envoyer** → **Publier**.

## Étape 4 : éviter de compter deux fois (1 min)

La campagne intelligente a créé « Clicks to call ». Cette conversion compte les clics sur le bouton d'appel, pas les appels réels. Une fois l'étape 2 faite, passez « Clicks to call » en **conversion secondaire** : **Objectifs** → **Conversions** → cliquez sur son nom → **Modifier les paramètres** → **Secondaire**.

## Étape 5 : consentement et Loi 25 (5 min)

Dans CookieYes, activez **Google Consent Mode (GCM)**, sous Paramètres de la bannière → Google Consent Mode. Les balises Google attendent alors le consentement du visiteur. Pour ceux qui refusent, Google estime les conversions sans déposer de témoin.

## Pourquoi ces choix

- **La page de réservation comme destination** : le visiteur arrive directement là où il convertit, et le numéro de téléphone y est visible. Ceux qui veulent comparer passent par les liens annexes : tarifs, dimensions, véhicules, terrasses.
- **Seulement les appels de 45 s et plus** : les faux numéros et les appels raccrochés ne comptent pas.
- **Les enchères restent manuelles** : après 15 à 20 conversions dans une campagne, on pourra passer à « Maximiser les conversions ». Sans suivi des conversions, cette option ne fonctionne pas.
