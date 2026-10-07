# 12 · Remarketing : pas à pas

Préparé le 7 octobre 2026. Le remarketing montre de nouveau MobilCube aux gens qui ont visité le site sans réserver, sur YouTube, Gmail, Discover, et plus tard Facebook et Instagram.

## Où on en est

Google Ads a créé 4 listes : « All Users of Mobilcube », « Returning visitors », « New visitors » et « Purchasers of Mobilcube ». Le 7 octobre, **elles sont toutes à 0 personne**. Votre conteneur GTM-M69QW6VC n'a que la balise de conversion et le linker. La conversion compte les réservations, mais elle ne remplit pas les listes. Il faut d'abord brancher ça.

## Étape 1 : remplir les listes (15 min, aujourd'hui)

1. **Importez `tracking/gtm-import-remarketing.json` dans GTM-M69QW6VC** :
   - **Administration** → **Importer un conteneur** → espace de travail **Existant** → **Fusionner** → **Renommer les éléments en conflit**.
   - Le fichier ajoute 2 balises et 1 déclencheur. Il ne touche pas la balise de réservation.

   | Balise | Rôle |
   |---|---|
   | Google Ads - Balise Google (reciblage), AW-18484934240, sur toutes les pages | Ajoute chaque visiteur aux listes Google Ads |
   | GA4 - generate_lead, à l'envoi réussi du formulaire | Marque dans GA4 ceux qui ont réservé, pour les exclure du remarketing |

2. **Prévisualisez**, puis **publiez** le conteneur.
3. **Associez GA4 à Google Ads** : GA4 → **Admin** → **Associations de produits** → **Google Ads** → 194-768-4780, avec **Publicité personnalisée** activée.
4. **Activez Google Signals** : GA4 → **Admin** → **Collecte de données**.
5. **Activez le Google Consent Mode dans CookieYes.** Avec la Loi 25, seuls les visiteurs qui acceptent les témoins publicitaires entrent dans les listes. Votre politique de confidentialité doit mentionner le remarketing.

## Étape 2 : créer les bonnes audiences (10 min)

Dans GA4 → **Admin** → **Audiences** → **Nouvelle audience** → **Créer une audience personnalisée**. Une fois GA4 associé à Google Ads, les audiences GA4 sont partagées automatiquement avec Google Ads.

| Audience | Inclure | Exclure | Durée |
|---|---|---|---|
| Visiteurs sans réservation | Événement `session_start` | Événement `generate_lead` | 30 jours |
| A vu les prix | `page_view` dont `page_location` contient `prix-location` ou `pricing` | `generate_lead` | 30 jours |
| Ont réservé | Événement `generate_lead` | (aucune) | 540 jours |

La liste « Ont réservé » sert à exclure les clients des annonces de reciblage.

Google n'utilise une liste qu'à partir d'environ **100 utilisateurs actifs**. Avec votre budget actuel, comptez 1 à 2 semaines.

## Étape 3 : utiliser les listes dans Google Ads

**A. Sur les 8 campagnes de recherche, en mode Observation (5 min)**
1. Ouvrez une campagne → **Audiences** → **Modifier les segments d'audience** → **Observation (recommandé)**.
2. Choisissez « All Users of Mobilcube », « Visiteurs sans réservation » et « A vu les prix ».

En mode Observation, les annonces restent montrées à tout le monde. Google Ads compare simplement les résultats. Après 2 à 4 semaines, si ces listes réservent mieux, ajoutez +20 % aux enchères pour elles.

**B. Une campagne Demand Gen « Reciblage » (YouTube, Gmail, Discover), 5 à 8 $/jour**
- **Objectif** : Prospects. **Audience** : « Visiteurs sans réservation ». **Exclusion** : « Ont réservé ».
- **Matériel** : 3 à 5 photos en formats 1,91:1, 1:1 et 4:5 (cube livré dans une entrée, entrepôt chauffé, auto à l'intérieur), le logo et, si possible, une vidéo de 15 secondes.
- **Messages** :
  - « Vous comparez encore ? Livraison 300 $, 15 km inclus »
  - « Avant la première neige : auto 160 $/mois, moto 80 $/mois »
  - « Votre mini-entrepôt de 160 pi² livré chez vous »
- **Destination** : la page de réservation.
- **Lancement** : quand la liste dépasse 100 personnes.

## Étape 4 : Facebook et Instagram (facultatif, 5 à 7 $/jour)

- Installez le pixel Meta dans GTM : `PageView`, plus `Lead` à l'envoi du formulaire.
- Créez l'audience « Visiteurs du site, 30 jours, sans Lead ».
- Lancez une campagne avec l'objectif Prospects.

Le détail est dans `docs/11-marketing-multiplateforme.md`.

## Ce que je peux faire pour vous

- **Créer la campagne Demand Gen, en pause**, dès que vous m'envoyez les photos.
- **Ajouter les listes en Observation sur les 8 campagnes**, si le connecteur le permet. Sinon, c'est 5 minutes à la main (étape 3A).
- **Créer les campagnes Facebook et Instagram** : il faut d'abord connecter Meta Ads dans Supermetrics.
