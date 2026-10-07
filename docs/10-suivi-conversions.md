# 10 · Suivi des conversions : réservations et appels (guide pas à pas)

Préparé le 7 octobre 2026 pour le compte Google Ads MobilCube (194-768-4780). Durée totale : environ 30 minutes.

## Ce qui est déjà fait dans le compte

- **Toutes les annonces mènent à la page de réservation** : `https://www.mobilcube.com/fr/formulaire-reservation/` en français, `https://www.mobilcube.com/en/booking-form/` en anglais. Le numéro de téléphone est affiché sur cette page.
- **Bouton d'appel (450-641-6498) sur les 8 campagnes.** Sur mobile, l'annonce affiche « Appeler ».
- **Liens annexes** vers les tarifs, les dimensions, les véhicules et les terrasses, pour ceux qui veulent lire avant de réserver.
- **Option « Présence » activée sur les 9 campagnes.** Seules les personnes qui se trouvent dans les zones ciblées, ou y passent régulièrement, voient les annonces. Une personne hors du Québec ou du Canada qui cherche « entreposage Montréal » ne les voit pas.

## Ce qui manque : le « pixel », c'est-à-dire la balise de conversion

Le site a déjà Google Tag Manager (GTM-K3G9FKRW), mais le conteneur est vide. Le site a aussi Google Analytics 4 (G-640H58NDHN) et la bannière de consentement CookieYes. Aucune conversion Google Ads n'existe pour les campagnes de recherche : le compte n'a que celles créées automatiquement pour la campagne intelligente.

Une fois les étapes ci-dessous faites, Google Ads comptera 3 conversions :

| Conversion | Ce qui la déclenche | Valeur | Principale |
|---|---|---|---|
| Réservation - formulaire | Le formulaire de réservation (WPForms) est envoyé avec succès | 50 $ | Oui |
| Appel depuis l'annonce | Un appel de 45 secondes ou plus via le bouton d'appel d'une annonce | 60 $ | Oui |
| Clic téléphone sur le site | Un clic sur le numéro de téléphone du site (lien « tel: ») | 10 $ | Oui |

Je ne peux pas créer ces conversions moi-même : le connecteur Google Ads que j'utilise ne permet pas de créer des actions de conversion, et je n'ai pas accès à votre Tag Manager. Tout le reste est prêt, notamment le fichier d'import GTM `tracking/gtm-import-mobilcube-google-ads.json`.

## Étape 1 : créer les conversions dans Google Ads (10 min)

**A. Réservation - formulaire**
1. Google Ads → **Objectifs** (icône trophée) → **Conversions** → **Récapitulatif** → **+ Créer une action de conversion**.
2. Choisissez **Site Web**, entrez `https://www.mobilcube.com`, cliquez sur **Analyser**.
3. En bas, choisissez **+ Ajouter une action de conversion manuellement**.
4. Remplissez :
   - Objectif et catégorie : **Envoi de formulaire pour prospects**
   - Nom : `Réservation - formulaire`
   - Valeur : **Utiliser la même valeur pour chaque conversion**, 50 $
   - Nombre : **Une**
5. Cliquez sur **Terminé** → **Enregistrer et continuer**.
6. À l'écran de la balise, choisissez **Utiliser Google Tag Manager**. Notez les deux valeurs affichées :
   - **ID de conversion** : des chiffres, par exemple 123456789. C'est aussi votre balise AW-123456789.
   - **Libellé de conversion** : une suite de lettres et de chiffres.

**B. Clic téléphone sur le site**
1. **+ Créer une action de conversion** → **Appels téléphoniques** → **Clics sur votre numéro sur votre site Web mobile**.
2. Remplissez :
   - Nom : `Clic téléphone sur le site`
   - Valeur : 10 $
   - Nombre : **Une**
3. Enregistrez, choisissez **Utiliser Google Tag Manager**, puis notez le **libellé de conversion**. L'ID de conversion est le même qu'en A.

**C. Appel depuis l'annonce**
1. **+ Créer une action de conversion** → **Appels téléphoniques** → **Appels depuis les annonces utilisant des composants Appel**.
2. Remplissez :
   - Nom : `Appel depuis l'annonce`
   - Durée minimale : **45 secondes**
   - Valeur : 60 $
   - Nombre : **Une**
3. Enregistrez. Aucune balise n'est nécessaire.
4. Vérifiez ensuite que les **rapports sur les appels** sont activés : **Admin** → **Paramètres du compte** → **Rapports sur les appels** → **Activés**. Google remplace alors le numéro du bouton d'appel par un numéro de transfert gratuit, ce qui mesure la durée de chaque appel.

**D. Éviter de compter deux fois**
La campagne intelligente a créé « Clicks to call ». Cette conversion compte les clics sur le bouton d'appel, pas les appels. Une fois C créée, passez « Clicks to call » en **conversion secondaire** : **Objectifs** → **Conversions** → cliquez sur son nom → **Modifier les paramètres** → **Secondaire**.

## Étape 2 : importer le conteneur dans Google Tag Manager (10 min)

1. Ouvrez https://tagmanager.google.com, puis le conteneur **GTM-K3G9FKRW**.
2. **Administration** → **Importer un conteneur**, puis :
   - Fichier : `tracking/gtm-import-mobilcube-google-ads.json`, téléchargeable depuis le dépôt.
   - Espace de travail : **Existant** (Default Workspace).
   - Option : **Fusionner** → **Renommer les balises, déclencheurs et variables en conflit**.
   - Confirmez.
3. Dans **Variables**, remplacez les 4 constantes par vos valeurs :

| Variable | Exemple | Où la trouver |
|---|---|---|
| Google Ads - ID (AW-) | `AW-123456789` | « AW- » + l'ID de conversion (étape 1A) |
| Google Ads - ID numérique | `123456789` | ID de conversion (étape 1A) |
| Google Ads - Label réservation | `AbC-dEfGhIjK` | Libellé de l'étape 1A |
| Google Ads - Label clic téléphone | `XyZ-123abc` | Libellé de l'étape 1B |

Le conteneur importé contient 5 balises :

| Balise | Se déclenche |
|---|---|
| Google Ads - Balise Google | Sur toutes les pages |
| Google Ads - Linker de conversion | Sur toutes les pages. Garde la trace du clic sur l'annonce. |
| Écouteur - formulaire WPForms envoyé | Sur toutes les pages. Le formulaire de réservation s'envoie sans changer de page, et cet écouteur prévient GTM quand l'envoi réussit. |
| Google Ads - Conversion - Réservation (formulaire) | À l'envoi réussi du formulaire |
| Google Ads - Conversion - Clic téléphone | Au clic sur un lien `tel:` |

4. Cliquez sur **Prévisualiser**, entrez `https://www.mobilcube.com/fr/formulaire-reservation/`, puis :
   - envoyez une demande test. « Google Ads - Conversion - Réservation » doit apparaître dans **Tags Fired** ;
   - cliquez sur le numéro de téléphone du site. « Google Ads - Conversion - Clic téléphone » doit apparaître.
5. Cliquez sur **Envoyer** → **Publier**.

## Étape 3 : consentement, Loi 25 (5 min)

Dans CookieYes, activez **Google Consent Mode (GCM)**, sous Paramètres de la bannière → Google Consent Mode. Les balises Google Ads attendent alors le consentement du visiteur. Google estime ensuite les conversions des visiteurs qui refusent, sans déposer de témoin.

## Étape 4 : vérifier (24 à 48 h plus tard)

Dans **Objectifs** → **Conversions**, l'état des deux conversions du site passe de « Non vérifiée » à **« Enregistrement des conversions »** après la première vraie conversion. Envoyez-moi l'ID AW- et les deux libellés : je les note dans le dépôt et je vérifie les chiffres de la première semaine.

## Pourquoi ces choix

- **La page de réservation comme destination** : le visiteur arrive directement là où il convertit, avec le numéro de téléphone visible. Ceux qui veulent comparer passent par les liens annexes : tarifs, dimensions, véhicules, terrasses.
- **Les appels de 45 s et plus seulement** : les faux numéros et les appels raccrochés ne comptent pas.
- **Les enchères restent manuelles** : après 15 à 20 conversions dans une campagne, on pourra passer à « Maximiser les conversions ». Sans ce suivi, cette option n'est pas possible.
