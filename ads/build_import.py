#!/usr/bin/env python3
"""Build Google Ads Editor import files for MobilCube from the keyword research + ad copy below.

Run:  python3 ads/build_import.py
Outputs: ads/google-ads-editor/*.csv, ads/keywords/*.csv, ads/negatives/*.csv, ads/copy/ad-copy.md
"""
import csv, json, re, sys, os
from collections import OrderedDict

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, 'google-ads-editor')
os.makedirs(OUT, exist_ok=True)

# Landing pages. LP_MODE=site (default) sends ads to pages that exist on mobilcube.com today.
# LP_MODE=lp sends them to the segment pages in landing/ once they are published (change LP_BASE to their host).
LP_MODE = os.environ.get('LP_MODE', 'site')
LP_BASE = os.environ.get('LP_BASE', 'https://offres.mobilcube.com')
if LP_MODE == 'lp':
    LP = {
        'fr-vehicule': f'{LP_BASE}/vehicules-hiver.html',
        'fr-terrasse': f'{LP_BASE}/terrasse-commerciale.html',
        'fr-mobile':   f'{LP_BASE}/entreposage-mobile.html',
        'fr-home':     f'{LP_BASE}/',
        'en-vehicle':  f'{LP_BASE}/en/winter-vehicle-storage.html',
        'en-patio':    f'{LP_BASE}/en/patio-storage.html',
        'en-mobile':   f'{LP_BASE}/en/mobile-storage.html',
        'en-home':     f'{LP_BASE}/en/',
    }
else:
    SITE = 'https://www.mobilcube.com'
    LP = {
        'fr-vehicule': f'{SITE}/fr/prix-location/',      # pricing page (hero shows a car stored in a unit)
        'fr-terrasse': f'{SITE}/fr/cas-usage/',          # use cases incl. surplus / seasonal / terrace furniture
        'fr-mobile':   f'{SITE}/fr/prix-location/',
        'fr-home':     f'{SITE}/fr/',
        'en-vehicle':  f'{SITE}/en/pricing/',
        'en-patio':    f'{SITE}/en/use-cases/',
        'en-mobile':   f'{SITE}/en/pricing/',
        'en-home':     f'{SITE}/en/',
    }

# ---------------------------------------------------------------- campaigns
# Launch budget: 5,000 $/month. Daily budgets below sum to 149 $/day = ~4,530 $/month; the remaining
# ~470 $ is headroom for the weather trigger and impression-share guard in scripts/google-ads/.
# Bidding at launch is Manual CPC: keyword bids below are hard ceilings and location bid adjustments work.
CAMPAIGNS = OrderedDict([
    ('FR | Search | Entreposage mobile',  dict(budget=50, cap=3.50, lang='fr', lp='fr-mobile')),
    ('FR | Search | Vehicules hiver',     dict(budget=45, cap=3.00, lang='fr', lp='fr-vehicule')),
    ('FR | Search | Terrasse commercial', dict(budget=12, cap=3.50, lang='fr', lp='fr-terrasse')),
    ('EN | Search | Mobile storage',      dict(budget=15, cap=5.00, lang='en', lp='en-mobile')),
    ('EN | Search | Winter vehicle',      dict(budget=12, cap=4.00, lang='en', lp='en-vehicle')),
    ('EN | Search | Commercial patio',    dict(budget=4,  cap=4.00, lang='en', lp='en-patio')),
    ('FR+EN | Search | Marque',           dict(budget=3,  cap=1.50, lang='fr', lp='fr-home')),
    ('FR+EN | Search | Concurrents',      dict(budget=8,  cap=2.50, lang='fr', lp='fr-mobile')),
])
# Per-ad-group ceilings below the campaign cap (single powersport vehicles are cheaper to store at a dealer or
# marina than in a 20 ft unit, so these clicks are worth less), and groups held back at launch.
AG_CAP = {'Moto hiver': 2.00, 'VTT': 2.00, 'Motoneige': 2.00, 'Remorque & équipement': 1.75,
          'Motorcycle & ATV': 2.50, 'Concurrents FR': 2.00, 'Competitors EN': 2.50}
PAUSED_AG = {'Motomarine & petit bateau', 'Boat & PWC'}

# ---------------------------------------------------------------- ad copy
# Each RSA: 15 headlines (<=30 chars), 4 descriptions (<=90), path1/path2 (<=15). pin1/pin2 = headline pinned to position 1/2.
H_FR_COMMON = ['Prix affichés, zéro surprise', 'Soumission en 60 secondes', 'Livraison 300 $, 15 km inclus',
               'MobilCube | Mini-entreposage', 'Rive-Sud, Montréal et Laval', 'Aucun frais d\'administration',
               'Appelez : réponse immédiate']
H_EN_COMMON = ['Prices Published, No Surprises', 'Get a Quote in 60 Seconds', 'Delivery $300, 15 km Included',
               'MobilCube | Mini-Storage', 'Montreal, West Island, Laval', 'No Monthly Admin Fees', 'Call Us, We Answer']

# Positioning (owner decision 2026-10-01): "mini-entreposage mobile" / "mobile mini-storage", a private mini-storage
# unit delivered to the customer, rather than "conteneur" / "container".
RSAS = {
 'fr-vehicule-chauffe': dict(
    pin1='Entreposage auto chauffé', pin2='Auto : 160 $/mois sur 6 mois',
    heads=['Moto : 80 $/mois sur 6 mois', 'Entrepôt chauffé, Boucherville', 'Votre auto, son mini-entrepôt', 'Aucun transport à payer',
           'Fini le sel et la neige', 'Fermé à clé, pour vous seul', 'Accès sur rendez-vous'] + H_FR_COMMON[:2] + H_FR_COMMON[3:],
    desc=["Déposez votre auto à Boucherville : elle passe l'hiver dans son mini-entrepôt chauffé.",
          'Auto 160 $/mois, moto 80 $/mois, sur 6 mois. Aucun transport à payer si vous l\'amenez.',
          "Mini-entrepôt d'acier fermé à clé, pour vous seul. Auto, moto, VTT, motoneige acceptés.",
          'Basés à Boucherville, près de la 20 et de la 30. Appelez-nous, on répond.'],
    path=('auto', 'chauffe')),
 'en-vehicle-heated': dict(
    pin1='Heated Car Storage', pin2='Car: $160/mo on 6 Months',
    heads=['Heated Warehouse, South Shore', 'Your Car, Its Own Mini-Storage', 'No Transport Fee to Pay',
           'Motorcycle: $80/mo, 6 Months', 'No Salt, No Snow, No Ice', 'Locked, Just for You', 'Access by Appointment'] + H_EN_COMMON[:2] + H_EN_COMMON[3:],
    desc=['Drop your car off in Boucherville: it spends winter in its own heated mini-storage unit.',
          'Car $160/mo, motorcycle $80/mo, on a 6-month plan. No transport fee when you drive in.',
          'A locked steel unit just for you. Cars, motorcycles, ATVs and snowmobiles welcome.',
          'Based in Boucherville, off Highways 20 and 30. Call us, we answer.'],
    path=('car', 'heated')),
 'fr-vehicule': dict(
    pin1='270 $/mois sur 6 mois', pin2='Votre auto à l\'abri cet hiver',
    heads=['Remisage hiver dans l\'entrée', 'Fini le sel et la neige', 'Moto, VTT, motoneige acceptés',
           'Mini-entrepôt pour votre auto', 'Entrepôt chauffé : 160 $/mois', 'Accès 24/7 dans votre entrée'] + H_FR_COMMON,
    desc=["Un mini-entrepôt d'acier livré chez vous : votre auto passe l'hiver à l'abri du sel.",
          '270 $/mois sur 6 mois, livraison 300 $ (15 km inclus). Soumission en ligne en 60 s.',
          'Moto, VTT, motoneige, motomarine ou auto : chargez au sol, accès 24/7 chez vous.',
          'Basés à Boucherville. Livraison Rive-Sud, Montréal, Laval. Appelez-nous, on répond.'],
    path=('entreposage', 'hiver')),
 'fr-vehicule-collection': dict(
    pin1='Voiture de collection protégée', pin2='270 $/mois sur 6 mois',
    heads=['Remisage hiver dans l\'entrée', 'Fini le sel et la neige', 'Mini-entrepôt privé et fermé',
           'Aucun trajet vers un entrepôt', 'Accès 24/7 dans votre entrée', 'Avant le 1er décembre'] + H_FR_COMMON,
    desc=["Votre voiture de collection passe l'hiver dans un mini-entrepôt d'acier privé, chez vous.",
          '270 $/mois sur 6 mois, livraison 300 $ (15 km inclus). Soumission en ligne en 60 s.',
          'Porte de 7 pi 5 po, plancher de bois marin, verrouillage renforcé. Chargez à votre rythme.',
          'Basés à Boucherville. Livraison Rive-Sud, Montréal, Laval. Appelez-nous, on répond.'],
    path=('remisage', 'collection')),
 'fr-vehicule-moto': dict(
    pin1='Entreposage moto chauffé', pin2='Moto : 80 $/mois sur 6 mois',
    heads=['Entrepôt chauffé, Boucherville', 'Aucun transport à payer', 'Fini le sel et la neige',
           'Accès sur rendez-vous', 'Ou chez vous : 270 $/mois', 'Libérez votre garage'] + H_FR_COMMON,
    desc=["Déposez votre moto à Boucherville : elle passe l'hiver au chaud, à l'abri du sel.",
          "80 $/mois sur 6 mois en entrepôt chauffé, sans transport si vous l'amenez. Devis en 60 s.",
          'Ou un mini-entrepôt livré chez vous : 270 $/mois sur 6 mois, livraison 300 $ (15 km).',
          'Basés à Boucherville, près de la 20 et de la 30. Appelez-nous, on répond.'],
    path=('moto', 'chauffe')),
 'fr-vehicule-powersports': dict(
    pin1='Moto, VTT, motoneige acceptés', pin2='270 $/mois sur 6 mois',
    heads=['Remisage hiver dans l\'entrée', 'Fini le sel et la neige', 'Mini-entrepôt livré chez vous',
           '2 VTT et la remorque entrent', 'Accès 24/7 dans votre entrée', 'Libérez votre garage'] + H_FR_COMMON,
    desc=["Moto, VTT, motoneige, motomarine : un mini-entrepôt d'acier livré chez vous cet hiver.",
          '270 $/mois sur 6 mois, livraison 300 $ (15 km inclus). Soumission en ligne en 60 s.',
          "1 165 pi³ : deux VTT, la remorque et l'équipement entrent. Chargez au niveau du sol.",
          'Basés à Boucherville. Livraison Rive-Sud, Montréal, Laval. Appelez-nous, on répond.'],
    path=('entreposage', 'vtt-moto')),
 'fr-terrasse': dict(
    pin1='Terrasse rangée en une journée', pin2='Restaurants, bars, hôtels',
    heads=['Tables, chaises, parasols', 'Retour livré au printemps', 'Chez vous ou entrepôt chauffé',
           'Facturation entreprise simple', 'Entreposage saisonnier pro', 'Réservez avant la date limite',
           'Entrepôt chauffé, Boucherville'] + H_FR_COMMON[:6],
    desc=['Un mini-entrepôt devant votre commerce : tables, chaises, parasols et chauffe-terrasses.',
          "Gardez-le sur place ou confiez-le à notre entrepôt chauffé jusqu'au printemps.",
          '289,75 $/mois sur 6 mois en entrepôt chauffé, transport 300 $ par déplacement. Devis 60 s.',
          'Restaurants, bars, cafés, hôtels : videz votre terrasse avant la date limite du quartier.'],
    path=('terrasse', 'commerce')),
 'fr-terrasse-condo': dict(
    pin1='Entreposage saisonnier pro', pin2='Chez vous ou entrepôt chauffé',
    heads=['Mobilier de piscine, bacs, BBQ', 'Retour livré au printemps', 'Facturation entreprise simple',
           'Mini-entrepôt privé de 160 pi²', 'Entrepôt chauffé, Boucherville', 'Surplus d\'inventaire à l\'abri'] + H_FR_COMMON,
    desc=["Condos, paysagistes, commerces : un mini-entrepôt privé pour meubles, bacs et équipement.",
          "Gardez-le sur place ou confiez-le à notre entrepôt chauffé jusqu'au printemps.",
          '289,75 $/mois sur 6 mois en entrepôt chauffé, transport 300 $ par déplacement. Devis 60 s.',
          'Basés à Boucherville. Livraison Rive-Sud, Montréal, Laval. Appelez-nous, on répond.'],
    path=('entreposage', 'commercial')),
 'fr-mobile': dict(
    pin1='Mini-entreposage mobile', pin2='Livré, rempli, entreposé',
    heads=['Mini-entrepôt privé de 160 pi²', 'Chez vous ou à notre entrepôt', 'On l\'entrepose pour vous',
           'Assez grand pour un 5 et demi', 'Dès 180 $/mois (24 mois)', 'Entrepôt chauffé, Boucherville'] + H_FR_COMMON,
    desc=['Un mini-entrepôt privé de 160 pi² livré chez vous. Remplissez-le au sol, à votre rythme.',
          "Gardez-le chez vous avec accès 24/7, ou on l'entrepose à notre entrepôt chauffé.",
          '350 $/mois sans engagement, 270 $/mois sur 6 mois, dès 180 $ sur 24 mois. Livraison 300 $.',
          'Basés à Boucherville. Livraison Rive-Sud, Montréal, Laval. Appelez-nous, on répond.'],
    path=('mini-entrepot', 'rive-sud')),
 'fr-mobile-demenagement': dict(
    pin1='Déménagez sans camion', pin2='Mini-entrepôt livré chez vous',
    heads=['Rénovation : meubles à l\'abri', 'Chargez à votre rythme', 'Chez vous ou à notre entrepôt',
           'Zéro double manutention', 'Assez grand pour un 5 et demi', 'Dès 180 $/mois (24 mois)'] + H_FR_COMMON,
    desc=['On livre votre mini-entrepôt, vous le remplissez, on le déplace à votre nouvelle adresse.',
          '350 $/mois sans engagement, 270 $/mois sur 6 mois. Livraison 300 $, 15 km inclus.',
          "Rénovation ? Vos meubles restent chez vous, à l'abri de la poussière, accessibles 24/7.",
          'Basés à Boucherville. Livraison Rive-Sud, Montréal, Laval. Appelez-nous, on répond.'],
    path=('demenagement', 'mini-entrepot')),
 'en-vehicle': dict(
    pin1='$270/mo on a 6-Month Plan', pin2='Your Car Safe All Winter',
    heads=['Winter Car Storage at Home', 'No Salt, No Snow, No Ice', 'Motorcycle, ATV, Snowmobile',
           'Mini-Storage in Your Driveway', 'Heated Warehouse: $160/mo', '24/7 Access in Your Driveway'] + H_EN_COMMON,
    desc=['A steel mini-storage unit delivered to your driveway: your car spends the winter inside.',
          '$270/mo on a 6-month plan, delivery $300 (15 km included). Online quote in 60 seconds.',
          'Motorcycle, ATV, snowmobile, jet ski or car: load at ground level, 24/7 access at home.',
          'Based in Boucherville. Delivery to Montreal, West Island and Laval. Call us, we answer.'],
    path=('storage', 'winter')),
 'en-vehicle-powersports': dict(
    pin1='Motorcycle, ATV, Snowmobile', pin2='$270/mo on a 6-Month Plan',
    heads=['Winter Storage at Home', 'No Salt, No Snow, No Ice', 'Mini-Storage in Your Driveway',
           'Two ATVs and the Trailer Fit', '24/7 Access in Your Driveway', 'Heated Motorcycle: $80/mo'] + H_EN_COMMON,
    desc=['Motorcycle, ATV, snowmobile, jet ski: a steel mini-storage unit delivered for winter.',
          '$270/mo on a 6-month plan, delivery $300 (15 km included). Online quote in 60 seconds.',
          'Motorcycle in our heated Boucherville warehouse: $80/mo on a 6-month plan.',
          'Based in Boucherville. Delivery to Montreal, West Island and Laval. Call us, we answer.'],
    path=('storage', 'atv-moto')),
 'en-patio': dict(
    pin1='Patio Packed Away in a Day', pin2='Restaurants, Bars, Hotels',
    heads=['Tables, Chairs, Heaters', 'Delivered Back in Spring', 'On Site or Heated Storage',
           'Simple Business Invoicing', 'Seasonal Business Storage', 'Book Before the Deadline',
           'Heated Warehouse, South Shore'] + H_EN_COMMON[:6],
    desc=['A mini-storage unit delivered to your door: tables, chairs, umbrellas and heaters go in.',
          'Keep it on site or send it to our heated Boucherville warehouse until spring.',
          '$289.75/mo on a 6-month heated plan, transport $300 per movement. Quote in 60 seconds.',
          'Restaurants, bars, cafés, hotels, condos: clear your terrace before the borough deadline.'],
    path=('patio', 'storage')),
 'en-mobile': dict(
    pin1='Mini-Storage in Montreal', pin2='Delivered, Loaded, Stored',
    heads=['Private Unit, 160 sq ft', 'At Home or in Our Warehouse', 'We Store It for You',
           'Room for a Whole Apartment', 'From $180/mo (24 Months)', 'Heated Warehouse, South Shore'] + H_EN_COMMON,
    desc=['A private 160 sq ft steel mini-storage unit delivered to you. Load at your own pace.',
          'Keep it at home with 24/7 access, or we store it in our heated Boucherville warehouse.',
          '$350/mo no commitment, $270/mo on 6 months, from $180 on 24 months. Delivery $300.',
          'Based in Boucherville. Delivery to Montreal, West Island and Laval. Call us, we answer.'],
    path=('mini-storage', 'montreal')),
 'en-mobile-moving': dict(
    pin1='Move Without a Truck', pin2='Mini-Storage at Your Door',
    heads=['Renovating? Furniture Safe', 'Load at Your Own Pace', 'At Home or in Our Warehouse',
           'Zero Double Handling', 'Room for a Whole Apartment', 'From $180/mo (24 Months)'] + H_EN_COMMON,
    desc=['We deliver your mini-storage unit, you load it, we move it to your new address.',
          '$350/mo no commitment, $270/mo on 6 months. Delivery $300 per movement, 15 km included.',
          'Renovating? Your furniture stays home, dust-free and accessible 24/7.',
          'Based in Boucherville. Delivery to Montreal, West Island and Laval. Call us, we answer.'],
    path=('moving', 'mini-storage')),
 'fr-marque': dict(
    pin1='MobilCube | Site officiel', pin2='Réservez votre MobilCube',
    heads=['Mini-entrepôt livré chez vous', 'Mini-entreposage mobile', 'Entrepôt chauffé, Boucherville',
           'Chez vous ou à notre entrepôt', 'Accès 24/7 dans votre entrée', 'Dès 180 $/mois (24 mois)'] + H_FR_COMMON,
    desc=['Site officiel MobilCube : prix affichés, soumission en ligne, livraison Grand Montréal.',
          '350 $/mois sans engagement, 270 $/mois sur 6 mois, dès 180 $ sur 24 mois. Livraison 300 $.',
          "Mini-entrepôt d'acier CORTEN de 160 pi². Chez vous ou dans notre entrepôt chauffé.",
          'Questions ? Appelez-nous : on répond en français et en anglais.'],
    path=('officiel', 'reservation')),
 'fr-concurrents': dict(
    pin1='Comparez : prix affichés', pin2='Une alternative locale',
    heads=['20 pi au lieu de petits cubes', 'Votre véhicule accepté', 'Entrepôt chauffé, Boucherville',
           'Mini-entrepôt livré chez vous', 'Chez vous ou à notre entrepôt', 'Dès 180 $/mois (24 mois)'] + H_FR_COMMON,
    desc=['Avant de réserver ailleurs : prix affichés, mini-entrepôt de 160 pi² et véhicule accepté.',
          '350 $/mois sans engagement, 270 $/mois sur 6 mois. Livraison 300 $, 15 km inclus.',
          'Entreprise de Boucherville. Entrepôt chauffé sur la Rive-Sud, livraison Montréal et Laval.',
          'Prix affichés sur le site et soumission en ligne en 60 secondes.'],
    path=('comparez', 'prix')),
 'en-competitors': dict(
    pin1='Compare: Prices Published', pin2='A Local Alternative',
    heads=['20 ft, Not Small Cubes', 'Your Vehicle Is Welcome', 'Heated Warehouse, South Shore',
           'Mini-Storage Delivered', 'At Home or in Our Warehouse', 'From $180/mo (24 Months)'] + H_EN_COMMON,
    desc=['Before you book elsewhere: prices published, a 160 sq ft unit, and your car is welcome.',
          '$350/mo no commitment, $270/mo on 6 months. Delivery $300 per movement, 15 km included.',
          'Boucherville company. Heated South Shore warehouse, delivery across Montreal and Laval.',
          'Prices published on our site and an online quote in 60 seconds.'],
    path=('compare', 'prices')),
}

SITELINKS = {
 'fr': [('Tarifs et offres', 'Liberté 350 $/mois', 'Avantage dès 180 $/mois', 'https://www.mobilcube.com/fr/prix-location/'),
        ('Soumission en 60 s', 'Formulaire rapide', 'On vous rappelle vite', 'https://www.mobilcube.com/fr/formulaire-reservation/'),
        ('Entreposage de véhicules', 'Auto, moto, VTT, motoneige', 'Chez vous ou entrepôt chauffé', LP['fr-vehicule']),
        ('Terrasses et commerces', 'Restaurants, bars, condos', 'Retour au printemps', LP['fr-terrasse'])],
 'en': [('Rates and Offers', 'Freedom $350/mo', 'Advantage from $180/mo', 'https://www.mobilcube.com/en/pricing/'),
        ('Quote in 60 Seconds', 'Short online form', 'We call you back fast', 'https://www.mobilcube.com/en/booking-form/'),
        ('Vehicle Storage', 'Car, motorcycle, ATV', 'Driveway or heated warehouse', LP['en-vehicle']),
        ('Patios and Businesses', 'Restaurants, bars, condos', 'Delivered back in spring', LP['en-patio'])],
}
CALLOUTS = {
 'fr': ['Entrepôt chauffé', 'Accès 24/7 sur place', 'Prix affichés', 'Dépôt remboursé', 'Rive-Sud, Montréal, Laval', 'Chez vous ou en entrepôt'],
 'en': ['Heated warehouse', '24/7 on-site access', 'Published prices', 'Deposit refunded', 'Greater Montreal delivery', 'Home or warehouse storage'],
}
SNIPPETS = {
 'fr': ('Services', ['Auto', 'Moto', 'VTT', 'Terrasse', 'Déménagement', 'Rénovation', 'Chantier']),
 'en': ('Services', ['Car', 'Motorcycle', 'ATV', 'Patio', 'Moving', 'Renovation', 'Jobsite']),
}

# ---------------------------------------------------------------- validation
def check_len(label, text, limit):
    if len(text) > limit:
        print(f'TOO LONG ({len(text)}>{limit}) {label}: {text}', file=sys.stderr)
        return False
    return True

ok = True
for key, r in RSAS.items():
    heads = [r['pin1'], r['pin2']] + r['heads']
    if len(heads) < 15:
        print(f'{key}: only {len(heads)} headlines', file=sys.stderr); ok = False
    if len(set(heads)) != len(heads):
        print(f'{key}: duplicate headline', file=sys.stderr); ok = False
    for h in heads: ok &= check_len(f'{key} headline', h, 30)
    for d in r['desc']: ok &= check_len(f'{key} description', d, 90)
    for p in r['path']: ok &= check_len(f'{key} path', p, 15)
    r['heads15'] = heads[:15]
for lang, sl in SITELINKS.items():
    for t, d1, d2, u in sl:
        ok &= check_len('sitelink', t, 25); ok &= check_len('sitelink d1', d1, 35); ok &= check_len('sitelink d2', d2, 35)
    for c in CALLOUTS[lang]: ok &= check_len('callout', c, 25)
    for v in SNIPPETS[lang][1]: ok &= check_len('snippet', v, 25)
if not ok:
    sys.exit('Fix the copy lengths above.')

# ---------------------------------------------------------------- keywords
def load(path):
    return json.load(open(path, encoding='utf-8'))

fr = load(os.path.join(ROOT, 'keywords', 'keywords-fr.research.json'))
en = load(os.path.join(ROOT, 'keywords', 'keywords-en.research.json'))
fr_kw = [t for t in fr['data_tables'] if 'universe' in t['title'].lower()][0]['rows']
en_kw = [t for t in en['data_tables'] if 'universe' in t['title'].lower()][0]['rows']
fr_neg = [t for t in fr['data_tables'] if 'negative' in t['title'].lower()][0]['rows']
en_neg = [t for t in en['data_tables'] if 'negative' in t['title'].lower()][0]['rows']

EXCLUDE_RE = re.compile(r'\b(vr|roulotte|motoris[ée]|caravane|camping-car|ponton|rv|motorhome|camper|trailer storage|fifth wheel|pontoon)\b', re.I)
BIG_BOAT_RE = re.compile(r'bateau|boat|voilier|yacht', re.I)
SMALL_BOAT_RE = re.compile(r'motomarine|jet ?ski|sea-?doo|pwc|chaloupe|petit bateau|pêche|jon boat', re.I)

def mid_cpc(s):
    nums = [float(x) for x in re.findall(r'\d+(?:\.\d+)?', s.replace(',', '.'))]
    return round(sum(nums) / len(nums), 2) if nums else None

def match_types(s, kw):
    if kw.startswith('['): return ['Exact']
    s = (s or '').lower()
    out = []
    if 'phrase' in s: out.append('Phrase')
    if 'exact' in s: out.append('Exact')
    if 'broad' in s and not out: out.append('Phrase')  # no broad at launch
    return out or ['Phrase']

def clean(kw):
    return kw.strip().strip('[]"').strip()

# "mini entrepôt mobile", "mini entreposage à domicile"... the positioning since 2026-10-01
MINI_RE = re.compile(r'\bmini\b.*\b(mobile|livr|domicile|portati)', re.I)

def map_fr(cluster, kw):
    k = kw.lower()
    if cluster.startswith('A'):
        camp = 'FR | Search | Entreposage mobile'
        if MINI_RE.search(k): return camp, 'Mini-entreposage mobile', 'fr-mobile', 'Enabled'
        ag = 'Cube d\'entreposage' if 'cube' in k else ('Conteneur d\'entreposage' if 'conteneur' in k else 'Entreposage mobile')
        return camp, ag, 'fr-mobile', 'Enabled'
    if cluster.startswith('B'):
        camp = 'FR | Search | Vehicules hiver'
        ag = 'Voiture collection' if 'collection' in k else 'Auto hiver'
        return camp, ag, 'fr-vehicule-collection' if 'collection' in k else 'fr-vehicule', 'Enabled'
    if cluster.startswith('C'):
        camp = 'FR | Search | Vehicules hiver'
        if EXCLUDE_RE.search(k): return None
        if 'motoneige' in k: return camp, 'Motoneige', 'fr-vehicule-powersports', 'Enabled'
        if re.search(r'\bvtt|quad|côte à côte|cote a cote|side by side', k): return camp, 'VTT', 'fr-vehicule-powersports', 'Enabled'
        if re.search(r'\bmoto\b|motocyclette|hivernage moto', k): return camp, 'Moto hiver', 'fr-vehicule-powersports', 'Enabled'
        if SMALL_BOAT_RE.search(k): return camp, 'Motomarine & petit bateau', 'fr-vehicule-powersports', 'Enabled'
        if BIG_BOAT_RE.search(k): return camp, 'Bateau (test, pausé)', 'fr-vehicule-powersports', 'Paused'
        if 'remorque' in k: return camp, 'Remorque & équipement', 'fr-vehicule-powersports', 'Enabled'
        return camp, 'Auto hiver', 'fr-vehicule', 'Enabled'
    if cluster.startswith('D'):
        camp = 'FR | Search | Terrasse commercial'
        if re.search(r'restaurant|bar\b|café|cafe|hôtel|hotel', k): return camp, 'Restaurant & bar', 'fr-terrasse', 'Enabled'
        if re.search(r'condo|piscine|immeuble', k): return camp, 'Hôtel & condo', 'fr-terrasse-condo', 'Enabled'
        if re.search(r'paysag|équipement|equipement|outil', k): return camp, 'Paysagiste & équipement', 'fr-terrasse-condo', 'Enabled'
        if re.search(r'inventaire|commercial|entreprise|saisonnier|stock', k): return camp, 'Commercial saisonnier & inventaire', 'fr-terrasse-condo', 'Enabled'
        return camp, 'Mobilier de terrasse', 'fr-terrasse', 'Enabled'
    if cluster.startswith('E'):
        return 'FR | Search | Entreposage mobile', 'Déménagement & rénovation', 'fr-mobile-demenagement', 'Enabled'
    if cluster.startswith('F'):
        camp = 'FR | Search | Entreposage mobile'
        if re.search(r'voiture|auto\b|véhicule|vehicule', k):
            return 'FR | Search | Vehicules hiver', 'Auto hiver', 'fr-vehicule', 'Enabled'
        if BIG_BOAT_RE.search(k):
            return 'FR | Search | Vehicules hiver', 'Bateau (test, pausé)', 'fr-vehicule-powersports', 'Paused'
        if MINI_RE.search(k): return camp, 'Mini-entreposage mobile', 'fr-mobile', 'Enabled'
        if re.search(r'mobile|conteneur|cube', k):
            return camp, 'Entreposage mobile', 'fr-mobile', 'Enabled'
        if re.search(r'rive-sud|rive sud|longueuil|brossard|boucherville|saint-hubert|st-hubert|sainte-julie|varennes|chambly|beloeil|saint-bruno|la prairie|candiac|montérégie', k):
            return camp, 'Rive-Sud (géo)', 'fr-mobile', 'Enabled'
        if re.search(r'près de moi|pres de moi|near me', k):
            return camp, 'Entreposage mobile', 'fr-mobile', 'Enabled'
        # Generic "entreposage <city>" outside the South Shore: 7+ funded self-storage chains bid here and most
        # searchers want a locker near home, not a 20 ft unit delivered from Boucherville. Held back at launch.
        return camp, 'Géo Montréal, Laval, couronnes (pausé)', 'fr-mobile', 'Paused'
    return None

def map_en(cluster, kw):
    k = kw.lower()
    if EXCLUDE_RE.search(k): return None
    if cluster.startswith('A-core mobile'):
        camp = 'EN | Search | Mobile storage'
        ag = 'Portable container' if re.search(r'portable|container|pod', k) else 'Mobile storage'
        return camp, ag, 'en-mobile', 'Enabled'
    if cluster.startswith('A-core self'):
        return 'EN | Search | Mobile storage', 'Self storage alternative (test, paused)', 'en-mobile', 'Paused'
    if cluster.startswith('A-geo'):
        if re.search(r'mobile|container|portable|pod', k):
            return 'EN | Search | Mobile storage', 'Mobile storage', 'en-mobile', 'Enabled'
        # "storage west island", "storage ndg"... = generic self-storage intent where the chains bid 5-10 $.
        return 'EN | Search | Mobile storage', 'Generic geo (paused)', 'en-mobile', 'Paused'
    if cluster.startswith('B'):
        camp = 'EN | Search | Winter vehicle'
        if re.search(r'motorcycle|atv|snowmobile|dirt bike|sled', k): return camp, 'Motorcycle & ATV', 'en-vehicle-powersports', 'Enabled'
        if SMALL_BOAT_RE.search(k): return camp, 'Boat & PWC', 'en-vehicle-powersports', 'Enabled'
        if BIG_BOAT_RE.search(k): return camp, 'Boat (test, paused)', 'en-vehicle-powersports', 'Paused'
        return camp, 'Winter car storage', 'en-vehicle', 'Enabled'
    if cluster.startswith('C'):
        camp = 'EN | Search | Commercial patio'
        if re.search(r'patio|terrace|restaurant|bar\b|hotel|outdoor furniture', k): return camp, 'Patio furniture', 'en-patio', 'Enabled'
        return camp, 'Business seasonal', 'en-patio', 'Enabled'
    if cluster.startswith('D'):
        return 'FR+EN | Search | Concurrents', 'Competitors EN', 'en-competitors', 'Enabled'
    return None

kw_rows, kw_list_rows = [], []
seen = set()
LP_FOR = {'fr-vehicule-chauffe': 'fr-vehicule', 'en-vehicle-heated': 'en-vehicle', 'fr-vehicule-collection': 'fr-vehicule', 'fr-vehicule-powersports': 'fr-vehicule', 'fr-terrasse-condo': 'fr-terrasse',
          'fr-mobile-demenagement': 'fr-mobile', 'en-vehicle-powersports': 'en-vehicle', 'en-mobile-moving': 'en-mobile',
          'en-competitors': 'en-mobile', 'fr-marque': 'fr-home', 'fr-concurrents': 'fr-mobile'}
def lp_url(k):
    return LP[LP_FOR.get(k, k)]

# Owner decision 2026-09-30: vehicles may be stored inside a unit at the heated Boucherville warehouse.
# Heated-storage searches are now wanted; tire-only storage (40-50 $/season elsewhere) stays excluded.
HEATED_RE = re.compile(r'pneu|\btires?\b', re.I)

HEATED_KW = re.compile(r'chauff|heated|intérieur|interieur|indoor', re.I)

def add_kw(camp, ag, kw, mt, cpc, lp_key, status, lang, est_vol='', est_cpc='', cluster=''):
    if ('Vehicules' in camp or 'Winter vehicle' in camp) and HEATED_RE.search(kw): return
    if camp == 'FR | Search | Vehicules hiver' and ag in ('Auto hiver', 'Voiture collection') and HEATED_KW.search(kw):
        ag, lp_key = 'Auto hiver chauffé', 'fr-vehicule-chauffe'
    if camp == 'EN | Search | Winter vehicle' and ag == 'Winter car storage' and HEATED_KW.search(kw):
        ag, lp_key = 'Heated car storage', 'en-vehicle-heated'
    key = (camp, ag, kw.lower(), mt)
    if key in seen: return
    seen.add(key)
    if ag in PAUSED_AG: status = 'Paused'
    cap = min(CAMPAIGNS[camp]['cap'], AG_CAP.get(ag, 99))
    bid = min(cpc if cpc else cap * 0.8, cap)
    kw_rows.append([camp, ag, kw, mt, f'{bid:.2f}', lp_url(lp_key), status])
    kw_list_rows.append([lang, camp, ag, kw, mt, f'{bid:.2f}', est_vol, est_cpc, cluster])

for r in fr_kw:
    kw, cluster, mt_s, intent, vol, cpc_s = r[0], r[1], r[2], r[3], r[4], r[5]
    m = map_fr(cluster, clean(kw))
    if not m: continue
    camp, ag, lp_key, status = m
    cpc = mid_cpc(cpc_s)
    for mt in match_types(mt_s, kw):
        add_kw(camp, ag, clean(kw), mt, round(cpc * 0.9, 2) if cpc else None, lp_key, status, 'fr', vol, cpc_s, cluster)
for r in en_kw:
    kw, cluster, mt_s, intent, vol, cpc_s = r[0], r[1], r[2], r[3], r[4], r[5]
    m = map_en(cluster, clean(kw))
    if not m: continue
    camp, ag, lp_key, status = m
    cpc = mid_cpc(cpc_s)
    for mt in match_types(mt_s, kw):
        add_kw(camp, ag, clean(kw), mt, round(cpc * 0.9, 2) if cpc else None, lp_key, status, 'en', vol, cpc_s, cluster)

# Hand-added keywords the research tables did not carry
EXTRA = [
 ('FR+EN | Search | Marque', 'MobilCube', 'fr-home', 'fr', ['mobilcube', 'mobil cube', 'mobilcube boucherville', 'mobilcube prix', 'mobilcube avis', 'mobilcube entreposage', 'mobilcube storage', 'mobilcube reviews', 'mobil cube montreal'], ['Exact', 'Phrase']),
 ('FR+EN | Search | Concurrents', 'Concurrents FR', 'fr-mobile', 'fr', ['pods montréal', 'pods entreposage', 'conteneur pods', 'pods prix', 'cubeit montréal', 'cubeit prix', 'cube it entreposage', 'gocube prix', 'go cube montréal', 'gocube entreposage', 'u-box montréal', 'ubox entreposage', 'bigsteelbox montréal'], ['Exact']),
 ('FR | Search | Vehicules hiver', 'Auto hiver', 'fr-vehicule', 'fr', ['entreposage auto hiver rive-sud', 'entreposage voiture hiver longueuil', 'entreposage voiture hiver brossard', 'remisage auto hiver montréal', 'où entreposer sa voiture l\'hiver', 'entreposage véhicule hiver boucherville'], ['Phrase', 'Exact']),
 ('FR | Search | Vehicules hiver', 'Motomarine & petit bateau', 'fr-vehicule-powersports', 'fr', ['entreposage motomarine hiver', 'entreposage sea-doo hiver', 'entreposage jet ski montréal', 'entreposage petit bateau hiver', 'entreposage chaloupe hiver'], ['Phrase', 'Exact']),
 ('FR | Search | Terrasse commercial', 'Restaurant & bar', 'fr-terrasse', 'fr', ['entreposage terrasse restaurant montréal', 'rangement terrasse restaurant hiver', 'entreposage mobilier restaurant', 'entreposage chauffe-terrasse', 'où entreposer mobilier de terrasse', 'entreposage terrasse bar'], ['Phrase', 'Exact']),
 ('EN | Search | Winter vehicle', 'Winter car storage', 'en-vehicle', 'en', ['winter car storage west island', 'winter car storage south shore', 'car storage container montreal', 'where to store car for winter montreal'], ['Phrase', 'Exact']),
 ('EN | Search | Commercial patio', 'Patio furniture', 'en-patio', 'en', ['restaurant patio storage montreal', 'terrace furniture winter storage', 'patio heater storage montreal', 'where to store patio furniture montreal'], ['Phrase', 'Exact']),
 # --- Added 2026-09-30: queries Google autocomplete returns for Canada today (real searches, see docs/08) ---
 ('FR | Search | Entreposage mobile', 'Entreposage mobile', 'fr-mobile', 'fr', ['entreposage mobile prix', 'entreposage mobile', 'entreposage mobile rive-sud', 'entreposage mobile longueuil', 'entreposage mobile boucherville'], ['Phrase', 'Exact']),
 ('FR | Search | Entreposage mobile', "Conteneur d'entreposage", 'fr-mobile', 'fr', ["conteneur d'entreposage à louer", 'conteneur entreposage à louer', 'conteneur entreposage mobile', "conteneur d'entreposage mobile", 'location conteneur entreposage', "location conteneur d'entreposage", 'location conteneur 20 pieds', 'conteneur 20 pieds à louer', 'location conteneur maritime 20 pieds'], ['Phrase', 'Exact']),
 ('FR | Search | Entreposage mobile', "Cube d'entreposage", 'fr-mobile', 'fr', ['location cube entreposage', 'cube entreposage mobile', 'cube entreposage'], ['Phrase', 'Exact']),
 ('FR | Search | Entreposage mobile', 'Rive-Sud (géo)', 'fr-mobile', 'fr', ['entreposage boucherville', 'entreposage à boucherville', 'mini entreposage boucherville', 'entreposage longueuil', 'entreposage longueuil prix', 'mini entreposage longueuil', 'entreposage rive sud', 'entreposage rive sud prix', 'entreposage rive sud de montréal', 'entreposage brossard', 'mini entreposage brossard', 'entreposage saint-hubert', 'entreposage sainte-julie', 'entreposage varennes', 'entreposage chambly', 'entreposage saint-bruno', 'entreposage saint-lambert', 'entreposage la prairie', 'entreposage candiac', 'entreposage beloeil'], ['Phrase', 'Exact']),
 ('FR | Search | Entreposage mobile', 'Déménagement & rénovation', 'fr-mobile-demenagement', 'fr', ['entreposage meuble prix', 'entreposage meubles', 'entreposage meubles montréal', 'entreposage déménagement', 'entreposage pendant rénovation', 'entreposage meubles rénovation', 'entreposage meubles longueuil'], ['Phrase', 'Exact']),
 ('FR | Search | Vehicules hiver', 'Auto hiver', 'fr-vehicule', 'fr', ['entreposage voiture hiver prix', 'entreposage auto hiver prix', 'prix entreposage voiture', 'entreposage voiture rive sud', 'entreposage auto rive sud', 'entreposage auto hiver rive sud', 'entreposage voiture longueuil', 'entreposage auto longueuil', 'entreposage voiture boucherville', 'entreposage auto boucherville', 'entreposage hivernal voiture', 'entreposage hivernal pour auto', 'remisage voiture hiver', 'remisage auto hiver'], ['Phrase', 'Exact']),
 ('FR | Search | Vehicules hiver', 'Moto hiver', 'fr-vehicule-powersports', 'fr', ['entreposage moto hiver prix', 'entreposage moto rive sud', 'entreposage moto longueuil', 'entreposage moto hiver', 'entreposage hiver moto', 'entreposage chauffé pour moto', 'entreposage moto chauffé'], ['Phrase', 'Exact']),
 ('EN | Search | Mobile storage', 'Portable container', 'en-mobile', 'en', ['storage container rental for driveway', 'storage container rental cost per month', 'storage container rental prices', 'portable storage containers for rent', 'storage container rental near me', 'mobile storage units near me', 'moving containers near me', 'moving container rental near me'], ['Phrase', 'Exact']),
 ('EN | Search | Winter vehicle', 'Winter car storage', 'en-vehicle', 'en', ['winter car storage montreal', 'car storage montreal', 'car storage west island', 'winter car storage near me', 'car storage south shore montreal'], ['Phrase', 'Exact']),
 # --- Added after owner confirmed heated warehouse storage for vehicles ---
 ('FR | Search | Vehicules hiver', 'Auto hiver chauffé', 'fr-vehicule-chauffe', 'fr', ['entreposage auto chauffé', 'entreposage voiture chauffé', 'entreposage chauffé pour auto', 'entreposage auto hiver chauffé', 'entreposage voiture intérieur', 'entreposage intérieur voiture', 'entreposage auto intérieur chauffé', 'entreposage chauffé rive sud', 'entreposage chauffé', 'garage chauffé à louer hiver'], ['Phrase', 'Exact']),
 ('EN | Search | Winter vehicle', 'Heated car storage', 'en-vehicle-heated', 'en', ['heated car storage montreal', 'indoor car storage montreal', 'heated car storage', 'indoor winter car storage', 'heated winter car storage', 'heated motorcycle storage'], ['Phrase', 'Exact']),
 # --- Keyword Planner ideas from competitor pages (Cubeit Montreal, GoCube Rive-Sud), 2026-09-30 ---
 ('FR | Search | Entreposage mobile', "Conteneur d'entreposage", 'fr-mobile', 'fr', ['conteneur à louer pour entreposage', 'louer un conteneur prix', 'location container prix', 'conteneur déménagement', 'conteneur déménagement prix', 'entrepot mobile'], ['Phrase', 'Exact']),
 ('FR | Search | Entreposage mobile', 'Entreposage mobile', 'fr-mobile', 'fr', ['location entreposage', 'prix entreposage', 'prix pour entreposage', 'espace entreposage', 'cube entreposage prix'], ['Phrase', 'Exact']),
 ('FR | Search | Entreposage mobile', 'Rive-Sud (géo)', 'fr-mobile', 'fr', ['entreposage st jean sur richelieu', 'mini entrepot st hubert', 'mini entrepôt longueuil'], ['Phrase', 'Exact']),
 ('FR | Search | Entreposage mobile', 'Déménagement & rénovation', 'fr-mobile-demenagement', 'fr', ['déménagement et entreposage', 'déménagement entreposage'], ['Phrase', 'Exact']),
 # --- Added 2026-10-01: "mini-entreposage mobile" positioning ---
 ('FR | Search | Entreposage mobile', 'Mini-entreposage mobile', 'fr-mobile', 'fr', ['mini entreposage mobile', 'mini entrepôt mobile', 'mini entrepot mobile', 'mini entrepôt livré', 'mini entreposage livré', 'mini entreposage à domicile', 'mini entrepôt à domicile', 'mini entrepôt portatif', 'location mini entrepôt mobile'], ['Phrase', 'Exact']),
 ('EN | Search | Mobile storage', 'Mobile storage', 'en-mobile', 'en', ['mobile mini storage', 'mini storage delivered', 'mini storage unit delivered', 'portable mini storage'], ['Phrase', 'Exact']),
]

# Negatives added 2026-09-30 from autocomplete: waste-dumpster rentals dominate "location conteneur", product
# searches dominate "storage container", and out-of-area cities show up in every seed.
NEG_ADD_FR = ['déchet', 'déchets', 'dechet', 'dechets', 'verges', 'verge', 'benne', 'bennes', 'vidange', 'rebuts',
              'à vendre', 'a vendre', 'vente', 'achat', 'acheter', 'usagé', 'usagés', 'occasion', 'saaq', 'assurance',
              'définition', 'definition', 'club', 'vélo', 'velo', 'pneu', 'pneus', 'herger', 'palette', 'palettes',
              'tunisie', 'maroc', 'paris', 'france', 'genève', 'lyon', 'belgique', 'suisse', 'ville de québec', 'québec city',
              'lévis', 'levis', 'saguenay', 'sherbrooke', 'drummondville', 'trois-rivières', 'trois rivieres', 'gatineau',
              'granby', 'rimouski', 'victoriaville', 'joliette', 'rouyn', 'pas cher', 'gratuit', 'rack', 'support', 'lift',
              'toile', 'housse', 'étagère', 'organisateur', 'amazon', 'walmart', 'costco', 'canadian tire', 'ikea',
              'home depot', 'rona', 'princess auto', 'emploi', 'emplois', 'job']
NEG_ADD_EN = ['dumpster', 'junk', 'waste', 'bin rental', 'for sale', 'buy', 'used', 'amazon', 'walmart', 'costco',
              'canadian tire', 'ikea', 'home depot', 'princess auto', 'shed', 'rack', 'lift', 'cabinet', 'cart', 'bins',
              'organizer', 'shelves', 'with lids', 'app', 'phone', 'android', 'iphone', 'azure', 'arc raiders', 'cheap',
              'cheapest', 'free', 'calgary', 'edmonton', 'toronto', 'ottawa', 'vancouver', 'winnipeg', 'ontario', 'alberta',
              'auckland', 'adelaide', 'job', 'jobs', 'auction', 'auctions']
for camp, ag, lp_key, lang, kws, mts in EXTRA:
    for kw in kws:
        for mt in mts:
            add_kw(camp, ag, kw, mt, None, lp_key, 'Enabled', lang, '', '', 'hand-added')

# ---------------------------------------------------------------- write CSVs
def w(name, header, rows):
    p = os.path.join(OUT, name)
    with open(p, 'w', newline='', encoding='utf-8-sig') as f:
        cw = csv.writer(f); cw.writerow(header); cw.writerows(rows)
    print(f'{name}: {len(rows)} rows')

w('01-campaigns.csv',
  ['Campaign', 'Campaign Type', 'Networks', 'Budget', 'Budget type', 'Bid Strategy Type', 'Max CPC bid limit', 'Location', 'Ad Schedule', 'Campaign Status'],
  [[c, 'Search', 'Google search', f'{v["budget"]:.2f}', 'Daily', 'Manual CPC', f'{v["cap"]:.2f} (keyword ceiling)', 'set in UI (see docs/08 §4)', 'Mon-Sun 06:00-23:00', 'Paused'] for c, v in CAMPAIGNS.items()])

ad_groups = OrderedDict()
for row in kw_rows:
    ad_groups.setdefault((row[0], row[1]), row[6])
w('02-ad-groups.csv', ['Campaign', 'Ad Group', 'Ad Group Type', 'Max CPC', 'Ad Group Status'],
  [[c, ag, 'Standard', f'{min(CAMPAIGNS[c]["cap"], AG_CAP.get(ag, 99)) * 0.8:.2f}',
    'Paused' if ('paus' in ag.lower() or ag in PAUSED_AG) else 'Enabled'] for (c, ag) in ad_groups])

w('03-keywords.csv', ['Campaign', 'Ad Group', 'Keyword', 'Criterion Type', 'Max CPC', 'Final URL', 'Status'], kw_rows)

# RSA per ad group
AG_RSA = {}
for row in kw_list_rows:
    lang, camp, ag = row[0], row[1], row[2]
    key = None
    for r in fr_kw + en_kw: pass
    AG_RSA.setdefault((camp, ag), None)
def rsa_for(camp, ag):
    a = ag.lower()
    if camp.endswith('Marque'): return 'fr-marque'
    if camp.endswith('Concurrents'): return 'en-competitors' if a.startswith('competitors') else 'fr-concurrents'
    if camp.startswith('FR | Search | Vehicules'):
        if 'chauff' in a: return 'fr-vehicule-chauffe'
        if 'collection' in a: return 'fr-vehicule-collection'
        if a.startswith('auto'): return 'fr-vehicule'
        if a == 'moto hiver': return 'fr-vehicule-moto'
        return 'fr-vehicule-powersports'
    if camp.startswith('FR | Search | Terrasse'):
        return 'fr-terrasse' if ('restaurant' in a or 'mobilier' in a) else 'fr-terrasse-condo'
    if camp.startswith('FR | Search | Entreposage'):
        return 'fr-mobile-demenagement' if 'ménagement' in a else 'fr-mobile'
    if camp.startswith('EN | Search | Winter'):
        if 'heated' in a: return 'en-vehicle-heated'
        return 'en-vehicle' if 'car' in a else 'en-vehicle-powersports'
    if camp.startswith('EN | Search | Commercial'): return 'en-patio'
    if camp.startswith('EN | Search | Mobile'): return 'en-mobile'
    return 'fr-mobile'

rsa_header = ['Campaign', 'Ad Group', 'Ad type'] + [f'Headline {i}' for i in range(1, 16)] + ['Headline 1 position', 'Headline 2 position'] + [f'Description {i}' for i in range(1, 5)] + ['Path 1', 'Path 2', 'Final URL', 'Status']
rsa_rows = []
lp_by_ag = {}
for row in kw_rows: lp_by_ag.setdefault((row[0], row[1]), row[5])
for (camp, ag) in ad_groups:
    r = RSAS[rsa_for(camp, ag)]
    rsa_rows.append([camp, ag, 'Responsive search ad'] + r['heads15'] + ['1', '2'] + r['desc'] + [r['path'][0], r['path'][1], lp_by_ag[(camp, ag)], 'Enabled'])
w('04-responsive-search-ads.csv', rsa_header, rsa_rows)

# Negative keyword lists (shared) + campaign-level negatives
neg_rows = []
# Research negatives that turned out to block real rental intent ("location conteneur 20 pieds" is exactly the product;
# "rangement terrasse restaurant" is a target query). Replaced by narrower product/purchase negatives.
DROP_NEG = {'conteneur 20 pieds', 'conteneur maritime', 'rangement'}
NEG_ADD_FR += ['bac de rangement', 'bacs de rangement', 'meuble de rangement', 'boîte de rangement', 'boite de rangement',
               'étagère de rangement', 'idée rangement', 'idées rangement', 'rangement garage', 'afrique', 'expédition',
               'conteneur maritime à vendre', 'conteneur maritime usagé']
for r in fr_neg:
    kw, mt = r[0], (r[2] if len(r) > 2 else 'phrase')
    if kw.lower() in DROP_NEG: continue
    neg_rows.append(['Negatives - FR', kw, 'Negative Exact' if 'exact' in mt.lower() else 'Negative Phrase'])
for r in en_neg:
    kw, mt = r[0], (r[2] if len(r) > 2 else 'phrase')
    neg_rows.append(['Negatives - EN', kw, 'Negative Exact' if 'exact' in mt.lower() else 'Negative Phrase'])
have = {(l, k.lower()) for l, k, _ in neg_rows}
positive = {row[2].lower() for row in kw_rows if row[6] == 'Enabled'}
for lst, words in [('Negatives - FR', NEG_ADD_FR), ('Negatives - EN', NEG_ADD_EN)]:
    for n in words:
        if (lst, n.lower()) in have: continue
        # never add a negative that would block an enabled keyword
        if any(re.search(r'(^|\s)' + re.escape(n.lower()) + r'($|\s)', p) for p in positive):
            print(f'skip negative "{n}": blocks an enabled keyword', file=sys.stderr); continue
        neg_rows.append([lst, n, 'Negative Phrase']); have.add((lst, n.lower()))
w('05-negative-keyword-lists.csv', ['Negative Keyword List', 'Keyword', 'Criterion Type'], neg_rows)

camp_neg = []
VEH_NEG = ['vr', 'roulotte', 'roulottes', 'motorisé', 'motorisés', 'caravane', 'camping-car', 'ponton', 'pontons', 'voilier', 'yacht', 'rv', 'motorhome', 'camper', 'pontoon', 'sailboat', 'fifth wheel', 'stationnement', 'parking', 'saaq', 'assurance', 'insurance', 'pneus d\'hiver', 'winter tires', 'antigel', 'huile', 'mécanique', 'mechanic',
           'pneu', 'pneus', 'tire', 'tires']
for c in ['FR | Search | Vehicules hiver', 'EN | Search | Winter vehicle']:
    for n in VEH_NEG: camp_neg.append([c, n, 'Negative Phrase'])
TER_NEG = ['achat', 'acheter', 'à vendre', 'a vendre', 'vente', 'buy', 'for sale', 'ikea', 'costco', 'canadian tire', 'rona', 'housse', 'cover', 'toile', 'construction de terrasse', 'deck builder', 'permis', 'permit', 'emploi', 'job']
for c in ['FR | Search | Terrasse commercial', 'EN | Search | Commercial patio']:
    for n in TER_NEG: camp_neg.append([c, n, 'Negative Phrase'])
BRAND_NEG = ['mobilcube', 'mobil cube']
for c in CAMPAIGNS:
    if 'Marque' in c: continue
    for n in BRAND_NEG: camp_neg.append([c, n, 'Negative Exact'])
w('06-campaign-negatives.csv', ['Campaign', 'Keyword', 'Criterion Type'], camp_neg)

# Assets
sl_rows, co_rows, sn_rows = [], [], []
for c, v in CAMPAIGNS.items():
    lang = 'en' if c.startswith('EN') else 'fr'
    for t, d1, d2, u in SITELINKS[lang]: sl_rows.append([c, t, d1, d2, u])
    for t in CALLOUTS[lang]: co_rows.append([c, t])
    h, vals = SNIPPETS[lang]; sn_rows.append([c, h, ';'.join(vals)])
w('07-sitelinks.csv', ['Campaign', 'Sitelink text', 'Sitelink description 1', 'Sitelink description 2', 'Sitelink final URL'], sl_rows)
w('08-callouts.csv', ['Campaign', 'Callout text'], co_rows)
w('09-structured-snippets.csv', ['Campaign', 'Header', 'Values'], sn_rows)

# Readable keyword & negative lists
os.makedirs(os.path.join(ROOT, 'keywords'), exist_ok=True); os.makedirs(os.path.join(ROOT, 'negatives'), exist_ok=True)
with open(os.path.join(ROOT, 'keywords', 'keywords-all.csv'), 'w', newline='', encoding='utf-8-sig') as f:
    cw = csv.writer(f); cw.writerow(['language', 'campaign', 'ad group', 'keyword', 'match type', 'launch max cpc (CAD)', 'est. monthly searches (estimate)', 'est. CPC range (estimate)', 'research cluster']); cw.writerows(kw_list_rows)
for lang, rows, cols in [('fr', fr_neg, fr['data_tables'][[i for i, t in enumerate(fr['data_tables']) if 'negative' in t['title'].lower()][0]]['columns']),
                         ('en', en_neg, en['data_tables'][[i for i, t in enumerate(en['data_tables']) if 'negative' in t['title'].lower()][0]]['columns'])]:
    with open(os.path.join(ROOT, 'negatives', f'negatives-{lang}.csv'), 'w', newline='', encoding='utf-8-sig') as f:
        cw = csv.writer(f); cw.writerow(cols); cw.writerows(rows)

# Copy deck
os.makedirs(os.path.join(ROOT, 'copy'), exist_ok=True)
with open(os.path.join(ROOT, 'copy', 'ad-copy.md'), 'w', encoding='utf-8') as f:
    f.write('# Ad copy deck (responsive search ads)\n\nAll headlines ≤ 30 characters, descriptions ≤ 90. Headline 1 and 2 are pinned. Generated by `ads/build_import.py`.\n\n')
    for key, r in RSAS.items():
        f.write(f'## {key}\n\n**Pinned 1:** {r["pin1"]}  \n**Pinned 2:** {r["pin2"]}\n\nHeadlines:\n')
        for h in r['heads15'][2:]: f.write(f'- {h} ({len(h)})\n')
        f.write('\nDescriptions:\n')
        for d in r['desc']: f.write(f'- {d} ({len(d)})\n')
        f.write(f'\nPath: /{r["path"][0]}/{r["path"][1]}\n\n')
    f.write('## Sitelinks, callouts, snippets\n\n')
    for lang in ['fr', 'en']:
        f.write(f'### {lang.upper()}\n')
        for t, d1, d2, u in SITELINKS[lang]: f.write(f'- {t} — {d1} / {d2} → {u}\n')
        f.write('- Callouts: ' + ' · '.join(CALLOUTS[lang]) + '\n')
        f.write(f'- Snippet {SNIPPETS[lang][0]}: ' + ', '.join(SNIPPETS[lang][1]) + '\n\n')
print('copy deck written')
