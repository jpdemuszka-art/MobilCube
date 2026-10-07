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
    r"lanaudi[èe]re|laurentides|estrie|outaouais|mauricie|st[- ]j[ée]r[ôo]me|saint[- ]j[ée]r[ôo]me|ste[- ]foy|"
    r"ste[- ]agathe|st[- ]lin|st[- ]nicolas|st[- ]maurice|st[- ]agapit|mirabel|sorel|tracy|cowansville|bromont|sutton|"
    r"waterloo|bedford|acton vale|huntingdon|ormstown|lacolle|rigaud|coteau|sherbrooke|qu[ée]bec city|ville de qu[ée]bec|"
    r"qu[ée]bec$|l[ée]vis|gatineau|ottawa|toronto|drummondville|trois[- ]rivi[èe]res|victoriaville|joliette|st[- ]agathe|"
    r"furniture|cabinet|dresser|bookcase|desk|bed|headboard|nightstand|wardrobe|cover|covers|stand|tent|bag|box|boxes|"
    r"rack|lift|trailer|ottoman|bench|ideas|diy|how to|saaq|verges?|r[ée]cr[ée]atifs?|rvstorage|rv storage|shipping|freight|"
    r"compan(y|ies)|movers?|u storage|safe storage|st[- ]augustin|pont[- ]rouge|ste[- ]sophie|laurentiens|vallon|sauvegarde|"
    r"queen|15 nord|1215|logic|viens|mini maxi|storage mart|douville|plus|carex|a530|beaumont|tremblant|clocher|sainte[- ]sophie|"
    r"safe|un entrep[ôo]t|mini max|du nord|nord sud|bonneau|helmet|motorcycles for winter|tucson|uhaulpod|la prairie$|"
    r"bateaux?|boats?|marina|jet ?ski|sea-?doo|motomarine|chaloupe|kayak|archives?|documents?|vin|wine|"
    r"shelving|bins?|totes?|shed|garage door|container homes?|maison conteneur|à vendre)\b", re.I)

RIVE_SUD = re.compile(
    r"\b(rive[- ]sud|longueuil|brossard|boucherville|st[- ]?hubert|saint[- ]hubert|st[- ]lambert|saint[- ]lambert|greenfield|"
    r"la ?prairie|candiac|delson|st[- ]constant|saint[- ]constant|ste[- ]catherine|sainte[- ]catherine|ch[âa]teauguay|mercier|"
    r"chambly|carignan|st[- ]bruno|saint[- ]bruno|ste[- ]julie|sainte[- ]julie|varennes|beloeil|mont[- ]saint[- ]hilaire|"
    r"st[- ]hilaire|mcmasterville|otterburn|st[- ]basile|saint[- ]basile|st[- ]amable|saint[- ]amable|st[- ]mathieu|"
    r"south shore)\b", re.I)
MONTEREGIE = re.compile(
    r"\b(mont[ée]r[ée]gie|monteregie|st[- ]hyacinthe|saint[- ]hyacinthe|granby|valleyfield|salaberry|"
    r"vaudreuil|dorion|st[- ]lazare|saint[- ]lazare|hudson|pincourt|[iî]le[- ]perrot|c[èe]dres|"
    r"farnham|marieville|st[- ]c[ée]saire|saint[- ]c[ée]saire|st[- ]r[ée]mi|rougemont|ange[- ]gardien|st[- ]damase|"
    r"saint[- ]r[ée]mi|napierville|iberville|st[- ]jean|saint[- ]jean|contrecoeur|contrec[œo]eur|beauharnois|"
    r"st[- ]pie|saint[- ]pie|soulanges|ste[- ]martine|sainte[- ]martine|l[ée]ry|st[- ]isidore|verch[èe]res|"
    r"st[- ]denis|st[- ]charles|richelieu|ste[- ]madeleine|la pr[ée]sentation|st[- ]dominique|saint[- ]dominique)\b", re.I)
# Island of Montreal, Laval and the North Shore: in the owner's map since 2026-10-07. The self-storage chains bid
# 4-7 $ on most of these, so the bid ceiling filters out the expensive ones and keeps the cheap long tail.
MTL_NORTH = re.compile(r"\b(montr[ée]al|montreal|mtl|laval|west island|pointe[- ]claire|kirkland|dollard|beaconsfield|lachine|"
                       r"ndg|westmount|verdun|anjou|plateau|rosemont|ahuntsic|downtown|lasalle|saint[- ]laurent|st[- ]laurent|"
                       r"terrebonne|repentigny|mascouche|blainville|boisbriand|rosem[èe]re|ste[- ]th[ée]r[èe]se|sainte[- ]th[ée]r[èe]se|"
                       r"st[- ]eustache|saint[- ]eustache|deux[- ]montagnes|rive[- ]nord|north shore|lavaltrie|st[- ]sulpice|"
                       r"charlemagne|bois[- ]des[- ]filion|lorraine|dorval|c[ôo]te[- ]saint[- ]luc|pointe[- ]aux[- ]trembles|"
                       r"montr[ée]al[- ]nord|montreal[- ]est)\b", re.I)
# Competitor and chain names: they go to the competitor campaign (curated list) or nowhere.
BRANDS = re.compile(r"\b(inc|lt[ée]e|depotium|libre entreposage|harwood|tremblay|stor ?wel|storagemart|u ?-?box|pods?|cubeit|cube it|"
                    r"go ?cube|bigsteelbox|big steel box|compact ?cube|access storage|public storage|smartstop|dymon|sentinel|"
                    r"maximum|volumax|mini[- ]entrep[ôo]ts? de l|entreposage domestique|dollard storage|lock ?it|stockage plus|"
                    r"mobile mini|willscot)\b", re.I)

FR_MOBILE, FR_VEH, FR_TER = 'FR | Search | Entreposage mobile', 'FR | Search | Vehicules hiver', 'FR | Search | Terrasse commercial'
EN_MOBILE, EN_VEH, EN_PATIO = 'EN | Search | Mobile storage', 'EN | Search | Winter vehicle', 'EN | Search | Commercial patio'

# Per-ad-group bid ceilings for NEW keywords (CAD). Kept at or below the launch ceilings in build_import.py.
CAP = {
    (FR_MOBILE, 'Mini-entrepôt'): 3.00, (FR_MOBILE, 'Mini-entreposage mobile'): 3.00, (FR_MOBILE, 'Entreposage mobile'): 3.00,
    (FR_MOBILE, "Conteneur d'entreposage"): 3.00, (FR_MOBILE, "Cube d'entreposage"): 3.00, (FR_MOBILE, 'Déménagement & rénovation'): 2.80,
    (FR_MOBILE, 'Rive-Sud (géo)'): 2.80, (FR_MOBILE, 'Montérégie (géo)'): 2.50, (FR_MOBILE, 'Grand Montréal (géo)'): 2.50,
    (FR_VEH, 'Auto hiver'): 2.60, (FR_VEH, 'Auto hiver chauffé'): 2.60, (FR_VEH, 'Voiture collection'): 2.60,
    (FR_VEH, 'Moto hiver'): 1.80, (FR_VEH, 'VTT'): 1.80, (FR_VEH, 'Motoneige'): 1.80, (FR_VEH, 'Remorque & équipement'): 1.50,
    (FR_TER, 'Mobilier de terrasse'): 2.80, (FR_TER, 'Restaurant & bar'): 2.80, (FR_TER, 'Commercial saisonnier & inventaire'): 2.80,
    (EN_MOBILE, 'Mobile storage'): 3.50, (EN_MOBILE, 'Portable container'): 3.50,
    (EN_VEH, 'Winter car storage'): 3.00, (EN_VEH, 'Heated car storage'): 3.00, (EN_VEH, 'Motorcycle & ATV'): 2.00,
    (EN_PATIO, 'Patio furniture'): 3.00, (EN_PATIO, 'Business seasonal'): 3.00,
}


COMPETITOR_TERMS = [('u box uhaul', 'Competitors EN'), ('uhaul ubox', 'Competitors EN'), ('pods canada', 'Competitors EN'),
                    ('pods rental', 'Competitors EN'), ('pods containers', 'Competitors EN'), ('pods storage', 'Competitors EN'),
                    ('pods cost', 'Competitors EN'), ('cube it storage', 'Competitors EN'), ('go cube rental', 'Competitors EN'),
                    ('ubox container', 'Competitors EN'), ('go cube prix', 'Concurrents FR'), ('gocube montreal', 'Concurrents FR')]


def route(kw, lang):
    """(campaign, ad group) for a candidate keyword, or None when it does not fit the offer."""
    k = kw.lower()
    if EXCLUDE.search(k) or BRANDS.search(k): return None
    # "location conteneur" alone means a dumpster in Quebec; keep containers only with a storage or moving word.
    if re.search(r"conteneur|container", k) and not re.search(r"entrepos|stockage|rangement|d[ée]m[ée]nag|storage|moving|portable|mobile", k):
        return None
    # "location / louer un entrepôt" is commercial warehouse space, not mini-storage.
    if re.search(r"(louer|location|loue|[àa] louer|commercial).*entrep[ôo]t|entrep[ôo]ts?.*(louer|location|commercial)|^entrep[ôo]t chauff", k) \
            and not re.search(r"\bmini", k):
        return None
    # "remiser / remisage" alone is the SAAQ plate-storage procedure; keep it only with a storage or winter word.
    if re.search(r"\bremis", k) and not re.search(r"hiver|entrepos|garage|chauff|int[ée]rieur", k): return None
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
        if MONTEREGIE.search(k): return FR_MOBILE, 'Montérégie (géo)'
        if MTL_NORTH.search(k): return FR_MOBILE, 'Grand Montréal (géo)'
        if RIVE_SUD.search(k): return FR_MOBILE, 'Rive-Sud (géo)'
        if re.search(r"d[ée]m[ée]nag|meubles?|r[ée]nov|temporaire|court terme|sinistre", k): return FR_MOBILE, 'Déménagement & rénovation'
        if re.search(r"\bmini\b.*\b(mobile|livr|domicile|portati)", k): return FR_MOBILE, 'Mini-entreposage mobile'
        if re.search(r"\bmini[- ]?entre|minientrepot|\bmini entreposage\b", k): return FR_MOBILE, 'Mini-entrepôt'
        if 'conteneur' in k or 'container' in k: return FR_MOBILE, "Conteneur d'entreposage"
        if 'cube' in k: return FR_MOBILE, "Cube d'entreposage"
        return FR_MOBILE, 'Entreposage mobile'
    # English
    if re.search(r"\b(car|cars|vehicle|vehicles|auto|automobile|automotive)\b", k):
        return (EN_VEH, 'Heated car storage') if re.search(r"heated|indoor", k) else (EN_VEH, 'Winter car storage')
    if re.search(r"motorcycle|motorbike|\bmoto\b|atv|snowmobile|sled|dirt bike", k): return EN_VEH, 'Motorcycle & ATV'
    if re.search(r"patio|terrace|restaurant|hotel", k): return EN_PATIO, 'Patio furniture'
    if re.search(r"commercial|business|inventory", k): return EN_PATIO, 'Business seasonal'
    if not re.search(r"storage|container|pods?|cube", k): return None
    if re.search(r"self storage|storage units? near me|storage unit prices", k): return None
    if MTL_NORTH.search(k) and not re.search(r"container|portable|mobile|pod|delivered", k): return None
    if re.search(r"container|portable|moving", k): return EN_MOBILE, 'Portable container'
    return EN_MOBILE, 'Mobile storage'


import unicodedata
STOP = {'de', 'du', 'des', 'd', 'la', 'le', 'les', 'l', 'un', 'une', 'pour', 'a', 'au', 'aux', 'en', 'the', 'for', 'of', 'a', 'an', 'to', 'in'}
def variant_key(kw):
    t = unicodedata.normalize('NFKD', kw.lower()).encode('ascii', 'ignore').decode()
    t = re.sub(r"[-'’]", ' ', t)
    words = [w[:-1] if len(w) > 3 and w[-1] in 'sx' else w for w in t.split() if w not in STOP]
    return ' '.join(sorted(words))


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
    # never empty an ad group: if every keyword of a group is low volume, keep them and report the group
    by_group = {}
    for k in live: by_group.setdefault((k['campaign'], k['ad_group']), []).append(k)
    rem_by_group = {}
    for r in remove: rem_by_group.setdefault((r['campaign'], r['ad_group']), []).append(r)
    dead_groups = [g for g, rs in rem_by_group.items() if len(rs) == len(by_group[g])]
    remove = [r for r in remove if (r['campaign'], r['ad_group']) not in dead_groups]
    removed_texts = {r['text'].lower() for r in remove}
    live_keys = {(k['campaign'], k['ad_group'], k['text'].lower(), k['match_type']) for k in live}
    kept_variants = {variant_key(k['text']) for k in live if k['text'].lower() not in removed_texts}
    seen_variants = set(kept_variants)
    add, skipped = [], []
    for k, r in sorted(by_kw.items(), key=lambda x: -(x[1].get('avg_monthly_searches') or 0)):
        v = r.get('avg_monthly_searches') or 0
        if v < MIN_VOL_NEW: continue
        if r.get('segment') in ('exclude', 'competitor_brand') or r.get('fit') in ('none', 'low'): continue
        dest = route(k, r.get('lang', 'fr'))
        if not dest: continue
        cap = CAP.get(dest)
        if cap is None: continue
        b = bid_for(r, cap)
        if b is None:
            skipped.append({'text': k, 'volume': v, 'low_bid': r.get('low_bid'), 'cap': cap, 'why': 'low top-of-page bid above ceiling'}); continue
        if (dest[0], dest[1], k, 'EXACT') in live_keys and k not in removed_texts: continue
        vk = variant_key(k)
        if vk in seen_variants: continue
        seen_variants.add(vk)
        add.append({'campaign': dest[0], 'ad_group': dest[1], 'text': k, 'match_type': 'EXACT', 'cpc_bid': b,
                    'volume': v, 'low_bid': r.get('low_bid'), 'high_bid': r.get('high_bid'), 'source': r.get('source')})
    # competitor brand + modifier terms (bare brand names stay negative), from the competitor research
    by = lambda t: by_kw.get(t, {})
    for t, grp in COMPETITOR_TERMS:
        r = by(t); v = r.get('avg_monthly_searches') or 0
        cap = 2.50 if grp == 'Competitors EN' else 2.00
        b = bid_for(r, cap) if r else None
        if v < MIN_VOL_NEW or b is None: continue
        add.append({'campaign': 'FR+EN | Search | Concurrents', 'ad_group': grp, 'text': t, 'match_type': 'EXACT', 'cpc_bid': b,
                    'volume': v, 'low_bid': r.get('low_bid'), 'high_bid': r.get('high_bid'), 'source': 'competitors'})
    json.dump({'remove': remove, 'add': add, 'skipped_expensive': skipped, 'dead_groups_kept': [list(g) for g in dead_groups]},
              open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(f'remove {len(remove)} low-volume keywords, add {len(add)} exact keywords, skip {len(skipped)} too expensive', file=sys.stderr)


if __name__ == '__main__':
    main()
