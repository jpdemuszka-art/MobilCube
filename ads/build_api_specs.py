#!/usr/bin/env python3
"""Turn the Google Ads Editor CSVs into one API payload per campaign (ads/api-specs/*.json).

These payloads create the campaigns, paused, in the MobilCube Google Ads account (1947684780)
through the Supermetrics connector (manage_campaign). Each file is the exact manage_campaign
create payload (minus ds_id/account_id); "after_create" holds what needs a second, update call once
ids exist: the ad schedule and which ad groups stay paused. Field names were checked against the API
on 2026-10-01: sitelinks take "url", the call asset goes in "calls", the RSA goes in ads[].creative,
campaigns and new ad groups/ads are always created paused. Run after ads/build_import.py:

    python3 ads/build_import.py && python3 ads/build_api_specs.py
"""
import csv, json, os, re
from collections import OrderedDict, defaultdict

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(ROOT, 'google-ads-editor')
OUT = os.path.join(ROOT, 'api-specs')
os.makedirs(OUT, exist_ok=True)

def rows(name):
    return list(csv.DictReader(open(os.path.join(SRC, name), encoding='utf-8-sig')))

WAREHOUSE = {'type': 'custom_location', 'key': '', 'name': '1215 rue Volta, Boucherville (45 km)',
             'latitude': 45.5685, 'longitude': -73.4441, 'radius': 45, 'distance_unit': 'kilometer', 'country': 'CA'}
CITY = lambda key, name: {'type': 'city', 'key': key, 'name': name, 'country': 'CA'}
TERRACE_GEO = [CITY('1002604', 'Montreal'), CITY('1002585', 'Longueuil'), CITY('1002579', 'Laval'),
               CITY('1002513', 'Brossard'), CITY('1002509', 'Boucherville')]
QUEBEC = [{'type': 'region', 'key': '20123', 'name': 'Quebec', 'country': 'CA'}]
# Montérégie (owner request 2026-10-07). Towns inside the 45 km circle are already covered by WAREHOUSE;
# these are the Montérégie towns beyond it (Google city targets, looked up with targeting_search).
MONTEREGIE_OUT = [CITY('1002550', 'Granby'), CITY('1002645', 'Sorel-Tracy'), CITY('1002638', 'Salaberry-de-Valleyfield'),
                  CITY('1002717', 'Vaudreuil-Dorion'), CITY('1002531', 'Cowansville'), CITY('1002511', 'Bromont'),
                  CITY('1002487', 'Acton Vale'), CITY('1002545', 'Farnham'), CITY('9224210', 'Saint-Lazare'),
                  CITY('1002553', 'Hudson'), CITY('9196122', 'Rigaud'), CITY('9047916', 'Pincourt'),
                  CITY('1002703', 'Sutton'), CITY('1002501', 'Bedford'), CITY('1002648', 'Saint-Alphonse-de-Granby')]
# Terrace campaigns target towns with restaurant strips, now including the main Montérégie centres.
TERRACE_MONTEREGIE = [CITY('1002662', 'Saint-Hyacinthe'), CITY('1002666', 'Saint-Jean-sur-Richelieu'), CITY('1002550', 'Granby'),
                      CITY('1002521', 'Chambly'), CITY('9047846', 'Beloeil'), CITY('1002600', 'Mont-Saint-Hilaire'),
                      CITY('1002698', 'Sainte-Julie'), CITY('1002516', 'Candiac'), CITY('1002565', 'La Prairie'),
                      CITY('1002670', 'Saint-Lambert'), CITY('1002716', 'Varennes'), CITY('1002654', 'Saint-Constant'),
                      CITY('1002717', 'Vaudreuil-Dorion'), CITY('1002638', 'Salaberry-de-Valleyfield'),
                      CITY('1002645', 'Sorel-Tracy'), CITY('9216451', 'Beauharnois'), CITY('1002511', 'Bromont'),
                      CITY('1002531', 'Cowansville')]

def geo_for(campaign):
    if 'Marque' in campaign: return QUEBEC
    if 'Terrasse' in campaign or 'Commercial patio' in campaign: return TERRACE_GEO + TERRACE_MONTEREGIE
    return [WAREHOUSE] + MONTEREGIE_OUT

def schedule_for(campaign):
    if 'Terrasse' in campaign or 'Commercial patio' in campaign:
        days = ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY']
        return [{'day_of_week': d, 'start_hour': 7, 'end_hour': 19} for d in days]
    days = ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY']
    return [{'day_of_week': d, 'start_hour': 6, 'end_hour': 23} for d in days]

MT = {'Exact': 'EXACT', 'Phrase': 'PHRASE', 'Broad': 'BROAD', 'Negative Exact': 'EXACT', 'Negative Phrase': 'PHRASE', 'Negative Broad': 'BROAD'}
URL_TAGS = 'utm_source=google&utm_medium=cpc&utm_campaign={campaignid}&utm_content={adgroupid}&utm_term={keyword}'

campaigns = rows('01-campaigns.csv')
adgroups = rows('02-ad-groups.csv')
keywords = rows('03-keywords.csv')
rsas = rows('04-responsive-search-ads.csv')
shared_neg = rows('05-negative-keyword-lists.csv')
camp_neg = rows('06-campaign-negatives.csv')
sitelinks = rows('07-sitelinks.csv')
callouts = rows('08-callouts.csv')
snippets = rows('09-structured-snippets.csv')

def lists_for(c):
    if c.startswith('FR |'): return {'Negatives - FR'}
    if c.startswith('EN |'): return {'Negatives - EN'}
    return {'Negatives - FR', 'Negatives - EN'}

index = []
for c in campaigns:
    name = c['Campaign']
    negs = OrderedDict()
    for n in shared_neg:
        if n['Negative Keyword List'] in lists_for(name):
            negs[(n['Keyword'].lower(), MT[n['Criterion Type']])] = {'text': n['Keyword'], 'match_type': MT[n['Criterion Type']]}
    for n in camp_neg:
        if n['Campaign'] == name:
            negs[(n['Keyword'].lower(), MT[n['Criterion Type']])] = {'text': n['Keyword'], 'match_type': MT[n['Criterion Type']]}
    ext = {
        'sitelinks': [{'link_text': s['Sitelink text'], 'description1': s['Sitelink description 1'],
                       'description2': s['Sitelink description 2'], 'url': s['Sitelink final URL']}
                      for s in sitelinks if s['Campaign'] == name],
        'callouts': [x['Callout text'] for x in callouts if x['Campaign'] == name],
        'structured_snippets': [{'header': x['Header'], 'values': x['Values'].split(';')} for x in snippets if x['Campaign'] == name],
        'calls': [{'phone_number': '+14506416498', 'country_code': 'CA'}],
    }
    groups, paused = [], []
    for g in adgroups:
        if g['Campaign'] != name: continue
        ag = g['Ad Group']
        kws = [{'text': k['Keyword'], 'match_type': MT[k['Criterion Type']], 'cpc_bid': float(k['Max CPC'])}
               for k in keywords if k['Campaign'] == name and k['Ad Group'] == ag]
        ad = next(r for r in rsas if r['Campaign'] == name and r['Ad Group'] == ag)
        groups.append({
            'name': ag,
            'platform_settings': {'type': 'SEARCH_STANDARD', 'cpc_bid': float(g['Max CPC'])},
            'targeting': {'keywords': kws},
            'ads': [{
                'name': f'RSA | {ag}',
                'creative': {
                    'headlines': [ad[f'Headline {i}'] for i in range(1, 16)],
                    'descriptions': [ad[f'Description {i}'] for i in range(1, 5)],
                    'final_urls': [ad['Final URL']],
                    'path1': ad['Path 1'], 'path2': ad['Path 2'],
                },
            }],
        })
        if g['Ad Group Status'] == 'Paused':
            paused.append(ag)
    spec = {
        'name': name,
        'budget_amount': float(c['Budget']), 'budget_type': 'DAILY',
        'bidding_strategy': 'MANUAL_CPC',
        'platform_settings': {'campaign_type': 'SEARCH', 'geo_target_type': 'PRESENCE',
                              'network_settings': {'search': True, 'display': False}},
        'contains_eu_political_ads': False,
        'url_tags': URL_TAGS,
        'targeting': {'location_details': geo_for(name), 'negative_keywords': list(negs.values())},
        'extensions': ext,
        'ad_groups': groups,
        'after_create': {'ad_schedule': schedule_for(name), 'keep_paused': paused},
    }
    slug = re.sub(r'[^a-z0-9]+', '-', name.lower()).strip('-')
    path = os.path.join(OUT, f'{slug}.json')
    json.dump(spec, open(path, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    index.append({'campaign': name, 'file': os.path.relpath(path, ROOT), 'ad_groups': len(groups),
                  'keywords': sum(len(g['targeting']['keywords']) for g in groups), 'negatives': len(negs),
                  'paused_ad_groups': paused})
json.dump(index, open(os.path.join(OUT, 'index.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
for i in index:
    print(f"{i['campaign']:40s} groups={i['ad_groups']:2d} kw={i['keywords']:3d} neg={i['negatives']:3d} paused={i['paused_ad_groups']}")
