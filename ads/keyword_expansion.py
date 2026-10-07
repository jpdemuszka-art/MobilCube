#!/usr/bin/env python3
"""Keyword clean-up and exact-match expansion from Google Keyword Planner data (2026-10-07).

Input:  ads/keywords/planner-2026-10-07.json  - rows {keyword, lang, avg_monthly_searches, competition, low_bid, high_bid, source}
        (Keyword Planner via Supermetrics: volumes of the live keywords, ideas from seed sets, Montérégie city combinations
        and competitor pages).
Output: ads/keywords/expansion-2026-10-07.json - {"remove": [...], "add": [...]} read by build_import.py.

Rules
- A live keyword is "low volume" when Keyword Planner shows no data or 10 searches a month or fewer: Google marks
  those "Low search volume" and does not serve them. They are removed (brand terms excepted) and the ad group keeps
  a phrase-match head term that still catches those searches.
- New keywords are EXACT match, need 20+ searches a month, and must fit the offer (mobile mini-storage, moving,
  winter vehicles, terraces, Montérégie / South Shore towns). RVs, trailers-as-RV, data storage, products, jobs,
  dumpsters, chains' brand names and out-of-area towns are excluded.
- Bid = low top-of-page bid x 1.2, floored at 0.90 $ and capped per segment, so no keyword can cost more than its
  segment's ceiling. Keywords whose low top-of-page bid is already above the ceiling are skipped as too expensive.
"""
import json, os, re, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(ROOT, 'keywords', 'planner-2026-10-07.json')
OUT = os.path.join(ROOT, 'keywords', 'expansion-2026-10-07.json')
MIN_VOL_NEW = 20
LOW_VOL = 10

EXCLUDE = re.compile(
    r"\b(vr|v\.r\.|roulottes?|motoris[ée]s?|caravanes?|camping|pontons?|voiliers?|yachts?|rv|motorhomes?|campers?|"
    r"fifth wheel|travel trailer|u ?-?haul|storagemart|stor ?wel|depotium|public storage|entrep[ôo]ts? public|entreposage public|"
    r"access storage|smartstop|harwood|godepo|des prairies|de l ?est|sacrement|jarry|st[- ]l[ée]onard|st[- ]laurent|"
    r"frigorifique|r[ée]frig[ée]r|palettes?|racking|logistique|industriel|3pl|local|locaux|bureau|louer un entrep[ôo]t|"
    r"entrep[ôo]ts? [àa] louer|pas cher|cheap|cheapest|gratuit|free|emploi|job|jobs|vendre|vente|for sale|usag[ée]|used|"
    r"benne|d[ée]chets?|dumpster|junk|pneus?|tires?|donn[ée]es|cloud|data|ext[ée]rieur|outdoor parking|stationnement|parking|"
    r"lanaudi[èe]re|laurentides|estrie|outaouais|mauricie|st[- ]j[ée]r[ôo]me|saint[- ]j[ée]r[ôo]me|rive[- ]nord|ste[- ]foy|"
    r"ste[- ]agathe|st[- ]lin|st[- ]eustache|saint[- ]eustache|st[- ]sulpice|st[- ]nicolas|st[- ]maurice|st[- ]agapit|"
    r"mascouche|terrebonne|repentigny|blainville|mirabel|ste[- ]th[ée]r[èe]se|sherbrooke|qu[ée]bec city|ville de qu[ée]bec|"
    r"l[ée]vis|gatineau|ottawa|toronto|drummondville|trois[- ]rivi[èe]res|victoriaville|joliette|"
    r"bateaux?|boats?|marina|jet ?ski|sea-?doo|motomarine|chaloupe|kayak|archives?|documents?|vin|wine|"
    r"shelving|bins?|totes?|shed|garage door|container homes?|maison conteneur|à vendre)\b", re.I)

RIVE_SUD = re.compile(
    r"\b(rive[- ]sud|longueuil|brossard|boucherville|st[- ]?hubert|saint[- ]hubert|st[- ]lambert|saint[- ]lambert|greenfield|"
    r"la ?prairie|candiac|delson|st[- ]constant|saint[- ]constant|ste[- ]catherine|sainte[- ]catherine|ch[âa]teauguay|mercier|"
    r"chambly|carignan|st[- ]bruno|saint[- ]bruno|ste[- ]julie|sainte[- ]julie|varennes|beloeil|mont[- ]saint[- ]hilaire|"
    r"st[- ]hilaire|mcmasterville|otterburn|st[- ]basile|saint[- ]basile|st[- ]amable|saint[- ]amable|st[- ]mathieu|"
    r"south shore)\b", re.I)
MONTEREGIE = re.compile(
    r"\b(mont[ée]r[ée]gie|st[- ]hyacinthe|saint[- ]hyacinthe|granby|bromont|cowansville|sorel|tracy|valleyfield|salaberry|"
    r"vaudreuil|dorion|st[- ]lazare|saint[- ]lazare|hudson|rigaud|pincourt|[iî]le[- ]perrot|coteau|c[èe]dres|huntingdon|"
    r"ormstown|farnham|marieville|st[- ]c[ée]saire|saint[- ]c[ée]saire|acton vale|sutton|waterloo|bedford|st[- ]r[ée]mi|"
    r"saint[- ]r[ée]mi|napierville|lacolle|iberville|st[- ]jean|saint[- ]jean|contrecoeur|contrec[œo]eur|beauharnois|"
    r"st[- ]pie|saint[- ]pie|soulanges)\b", re.I)
MTL_NORTH = re.compile(r"\b(montr[ée]al|montreal|laval|west island|pointe[- ]claire|kirkland|dollard|beaconsfield|lachine|"
                       r"ndg|westmount|verdun|anjou|plateau|rosemont|ahuntsic|downtown)\b", re.I)

FR_MOBILE, FR_VEH, FR_TER = 'FR | Search | Entreposage mobile', 'FR | Search | Vehicules hiver', 'FR | Search | Terrasse commercial'
EN_MOBILE, EN_VEH, EN_PATIO = 'EN | Search | Mobile storage', 'EN | Search | Winter vehicle', 'EN | Search | Commercial patio'

# Per-ad-group bid ceilings for NEW keywords (CAD). Kept at or below the launch ceilings in build_import.py.
CAP = {
    (FR_MOBILE, 'Mini-entrepôt'): 3.00, (FR_MOBILE, 'Mini-entreposage mobile'): 3.00, (FR_MOBILE, 'Entreposage mobile'): 3.00,
    (FR_MOBILE, "Conteneur d'entreposage"): 3.00, (FR_MOBILE, "Cube d'entreposage"): 3.00, (FR_MOBILE, 'Déménagement & rénovation'): 2.80,
    (FR_MOBILE, 'Rive-Sud (géo)'): 2.80, (FR_MOBILE, 'Montérégie (géo)'): 2.50,
    (FR_VEH, 'Auto hiver'): 2.60, (FR_VEH, 'Auto hiver chauffé'): 2.60, (FR_VEH, 'Voiture collection'): 2.60,
    (FR_VEH, 'Moto hiver'): 1.80, (FR_VEH, 'VTT'): 1.80, (FR_VEH, 'Motoneige'): 1.80, (FR_VEH, 'Remorque & équipement'): 1.50,
    (FR_TER, 'Mobilier de terrasse'): 2.80, (FR_TER, 'Restaurant & bar'): 2.80, (FR_TER, 'Commercial saisonnier & inventaire'): 2.80,
    (EN_MOBILE, 'Mobile storage'): 3.50, (EN_MOBILE, 'Portable container'): 3.50,
    (EN_VEH, 'Winter car storage'): 3.00, (EN_VEH, 'Heated car storage'): 3.00, (EN_VEH, 'Motorcycle & ATV'): 2.00,
    (EN_PATIO, 'Patio furniture'): 3.00, (EN_PATIO, 'Business seasonal'): 3.00,
}


def route(kw, lang):
    """(campaign, ad group) for a candidate keyword, or None when it does not fit the offer."""
    k = kw.lower()
    if EXCLUDE.search(k): return None
    if lang == 'fr':
        if re.search(r"\b(voitures?|autos?|automobiles?|v[ée]hicules?|remisage|camions?|vus|d[ée]capotable)\b", k):
            if re.search(r"collection|ancienne", k): return FR_VEH, 'Voiture collection'
            if re.search(r"chauff|int[ée]rieur", k): return FR_VEH, 'Auto hiver chauffé'
            return FR_VEH, 'Auto hiver'
        if re.search(r"\b(motos?|motocyclettes?)\b", k): return FR_VEH, 'Moto hiver'
        if re.search(r"\b(vtt|quad|c[ôo]te [àa] c[ôo]te)\b", k): return FR_VEH, 'VTT'
        if re.search(r"\bmotoneiges?\b", k): return FR_VEH, 'Motoneige'
        if re.search(r"\bremorques?\b", k): return FR_VEH, 'Remorque & équipement'
        if re.search(r"terrasse|patio|restaurant|\bbar\b|h[ôo]tel|mobilier ext", k): return FR_TER, 'Mobilier de terrasse' if not re.search(r"restaurant|\bbar\b", k) else 'Restaurant & bar'
        if re.search(r"commercial|entreprise|inventaire|saisonnier|commerce", k): return FR_TER, 'Commercial saisonnier & inventaire'
        if not re.search(r"entrepos|entrep[ôo]t|conteneur|container|cube|stockage|rangement", k): return None
        if MTL_NORTH.search(k): return None        # generic city searches outside Montérégie stay with the paused geo group
        if MONTEREGIE.search(k): return FR_MOBILE, 'Montérégie (géo)'
        if RIVE_SUD.search(k): return FR_MOBILE, 'Rive-Sud (géo)'
        if re.search(r"d[ée]m[ée]nag|meubles?|r[ée]nov|temporaire|court terme|sinistre", k): return FR_MOBILE, 'Déménagement & rénovation'
        if re.search(r"\bmini\b.*\b(mobile|livr|domicile|portati)", k): return FR_MOBILE, 'Mini-entreposage mobile'
        if re.search(r"\bmini[- ]?entre|minientrepot|\bmini entreposage\b", k): return FR_MOBILE, 'Mini-entrepôt'
        if 'conteneur' in k or 'container' in k: return FR_MOBILE, "Conteneur d'entreposage"
        if 'cube' in k: return FR_MOBILE, "Cube d'entreposage"
        return FR_MOBILE, 'Entreposage mobile'
    # English
    if re.search(r"\b(car|cars|vehicle|auto)\b", k):
        return (EN_VEH, 'Heated car storage') if re.search(r"heated|indoor", k) else (EN_VEH, 'Winter car storage')
    if re.search(r"motorcycle|atv|snowmobile|sled|dirt bike", k): return EN_VEH, 'Motorcycle & ATV'
    if re.search(r"patio|terrace|restaurant|hotel", k): return EN_PATIO, 'Patio furniture'
    if re.search(r"commercial|business|inventory", k): return EN_PATIO, 'Business seasonal'
    if not re.search(r"storage|container|pods?|cube", k): return None
    if re.search(r"self storage|storage units? near me|storage unit prices", k): return None
    if MTL_NORTH.search(k) and not re.search(r"container|portable|mobile|pod", k): return None
    if re.search(r"container|pods?|portable|moving", k): return EN_MOBILE, 'Portable container'
    return EN_MOBILE, 'Mobile storage'


def bid_for(row, cap):
    low = row.get('low_bid')
    if low is None: return round(min(cap, 1.50 if cap >= 1.5 else cap), 2)
    if low > cap: return None
    return round(min(cap, max(0.90, low * 1.2)), 2)


def main():
    rows = json.load(open(SRC, encoding='utf-8'))
    by_kw = {}
    for r in rows:
        k = r['keyword'].strip().lower()
        best = by_kw.get(k)
        if best is None or (r.get('avg_monthly_searches') or 0) > (best.get('avg_monthly_searches') or 0):
            by_kw[k] = r
    live = json.load(open(os.path.join(ROOT, 'keywords', 'live-keywords-2026-10-07.json'), encoding='utf-8'))
    remove, keep_heads = [], set()
    for kw in live:
        if kw['campaign'].endswith('Marque'): continue
        v = (by_kw.get(kw['text'].lower()) or {}).get('avg_monthly_searches')
        if v is None or v <= LOW_VOL:
            remove.append(dict(kw, volume=v))
    removed_texts = {r['text'].lower() for r in remove}
    live_keys = {(k['campaign'], k['ad_group'], k['text'].lower(), k['match_type']) for k in live}
    add, skipped = [], []
    for k, r in sorted(by_kw.items(), key=lambda x: -(x[1].get('avg_monthly_searches') or 0)):
        v = r.get('avg_monthly_searches') or 0
        if v < MIN_VOL_NEW: continue
        dest = route(k, r.get('lang', 'fr'))
        if not dest: continue
        cap = CAP.get(dest)
        if cap is None: continue
        b = bid_for(r, cap)
        if b is None:
            skipped.append({'text': k, 'volume': v, 'low_bid': r.get('low_bid'), 'cap': cap, 'why': 'low top-of-page bid above ceiling'}); continue
        if (dest[0], dest[1], k, 'EXACT') in live_keys and k not in removed_texts: continue
        add.append({'campaign': dest[0], 'ad_group': dest[1], 'text': k, 'match_type': 'EXACT', 'cpc_bid': b,
                    'volume': v, 'low_bid': r.get('low_bid'), 'high_bid': r.get('high_bid'), 'source': r.get('source')})
    json.dump({'remove': remove, 'add': add, 'skipped_expensive': skipped}, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(f'remove {len(remove)} low-volume keywords, add {len(add)} exact keywords, skip {len(skipped)} too expensive', file=sys.stderr)


if __name__ == '__main__':
    main()
