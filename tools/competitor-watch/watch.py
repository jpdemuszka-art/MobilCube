#!/usr/bin/env python3
"""Free competitor watch for MobilCube. No API key, no paid tool, standard library only.

What it checks on each competitor site:
  - whether they run Google Ads (conversion IDs in the page or in their Google Tag Manager container)
  - call tracking for Google Ads, Meta pixel, Microsoft Ads (UET), TikTok, LinkedIn
  - promo lines (%, gratuit, rabais, offre, code, jusqu'au, save, free, off...)
  - prices shown on the page, phone numbers, page title
and writes a Markdown report with what CHANGED since the previous run.

Optional: --suggest pulls Google's autocomplete for seed phrases (real searches people type in Canada),
a free way to discover keywords.

Usage:
  python3 tools/competitor-watch/watch.py              # scan competitors, write report
  python3 tools/competitor-watch/watch.py --suggest    # also refresh keyword suggestions
Outputs:
  tools/competitor-watch/data/<date>.json      raw snapshot (kept for diffs)
  tools/competitor-watch/reports/<date>.md     human report
  tools/competitor-watch/reports/latest.md     copy of the newest report
"""
import argparse, datetime as dt, glob, html, json, os, re, ssl, sys, time, urllib.parse, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, 'data')
REPORTS = os.path.join(HERE, 'reports')
UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0 Safari/537.36'

def ssl_context():
    for bundle in (os.environ.get('SSL_CERT_FILE'), '/root/.ccr/ca-bundle.crt'):
        if bundle and os.path.exists(bundle):
            return ssl.create_default_context(cafile=bundle)
    return ssl.create_default_context()
CTX = ssl_context()

def fetch(url, timeout=25, tries=3):
    """GET a page; retry when a bot-check interstitial ('One moment, please') is served."""
    last = ''
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers={'User-Agent': UA, 'Accept-Language': 'fr-CA,fr;q=0.9,en;q=0.8'})
            with urllib.request.urlopen(req, timeout=timeout, context=CTX) as r:
                raw = r.read()
                enc = r.headers.get_content_charset() or 'utf-8'
            last = raw.decode(enc, errors='replace')
            if len(last) < 12000 and 'One moment, please' in last:
                time.sleep(2 + i * 3); continue
            return last, None
        except Exception as e:  # network errors are reported, never fatal
            last_err = f'{type(e).__name__}: {e}'
            time.sleep(1 + i)
    return last, ('bot-check page served every time' if last else last_err)

def visible_text(page):
    page = re.sub(r'(?is)<(script|style|noscript|svg)[^>]*>.*?</\1>', ' ', page)
    page = re.sub(r'(?s)<[^>]+>', '\n', page)
    page = html.unescape(page)
    lines = [re.sub(r'\s+', ' ', l).strip() for l in page.split('\n')]
    return [l for l in lines if l]

PROMO_RE = re.compile(r"(\d+\s?%|gratuit|rabais|économisez|economisez|offre|promo|code promo|jusqu[’']au|valable|"
                      r"\bfree\b|\bsave\b|\boff\b|special|spécial|limited|limitée|deal)", re.I)
PRICE_RE = re.compile(r'(?:\$\s?\d{1,3}(?:[,\s]\d{3})*(?:\.\d{2})?|\d{1,3}(?:[\s ]\d{3})*(?:,\d{2})?\s?\$)')
PHONE_RE = re.compile(r'tel:\+?([\d\-\s().]{10,20})')
# Every GTM container ships Google's library code, which mentions 'phone_conversion' and 'googleadservices'
# even when no tag is set up. So we read the tag TYPES the container really has configured ("function":"__xxx").
TAG_TYPES = {
    '__awct': 'Google Ads conversion tag', '__awcc': 'Google Ads website-call conversion', '__sp': 'Google Ads remarketing',
    '__awec': 'Google Ads enhanced conversions', '__awud': 'Google Ads user-provided data', '__gclidw': 'Conversion linker',
    '__baut': 'Microsoft Ads (UET)', '__flc': 'Floodlight (DV360/CM360)', '__ytl': 'YouTube tracking',
}
TRACKERS = {
    'meta_pixel': r'fbq\(|connect\.facebook\.net',
    'microsoft_uet_in_page': r'bat\.bing\.com/bat\.js',
    'tiktok': r'analytics\.tiktok\.com',
    'linkedin': r'snap\.licdn\.com|_linkedin_partner_id',
    'ga4': r'G-[A-Z0-9]{8,12}',
}
CALL_IN_PAGE = re.compile(r'phone_conversion_number[\'"]?\s*:\s*[\'"]\+?[\d\s().-]{7,}')

def scan(comp):
    out = {'name': comp['name'], 'pages': {}, 'errors': [], 'gtm': [], 'ads_ids': [], 'trackers': {},
           'promos': [], 'prices': [], 'phones': [], 'titles': {}}
    blob = ''
    for url in comp['urls']:
        page, err = fetch(url)
        if err: out['errors'].append(f'{url}: {err}')
        if not page: continue
        blob += page
        m = re.search(r'(?is)<title[^>]*>(.*?)</title>', page)
        out['titles'][url] = html.unescape(re.sub(r'\s+', ' ', m.group(1))).strip()[:140] if m else ''
        lines = visible_text(page)
        for l in lines:
            if 15 <= len(l) <= 220 and PROMO_RE.search(l): out['promos'].append(l)
        for m in PRICE_RE.finditer(' '.join(lines)):
            s = max(0, m.start() - 45); ctx = ' '.join(lines)[s:m.end() + 25]
            out['prices'].append(re.sub(r'\s+', ' ', ctx).strip())
        out['phones'] += [re.sub(r'[^\d]', '', p)[-10:] for p in PHONE_RE.findall(page)]
    out['gtm'] = sorted(set(re.findall(r'GTM-[A-Z0-9]{5,8}', blob)))
    ads = set(re.findall(r'AW-\d{8,11}', blob))
    tag_types = {}
    for g in out['gtm']:
        js, err = fetch(f'https://www.googletagmanager.com/gtm.js?id={g}', tries=1)
        if js:
            blob += js
            ads |= set(re.findall(r'AW-\d{8,11}', js))
            for fn in re.findall(r'"function":"(__[a-z_]+)"', js):
                if fn in TAG_TYPES: tag_types[fn] = tag_types.get(fn, 0) + 1
    out['ads_ids'] = sorted(ads)
    out['tag_types'] = {TAG_TYPES[k]: v for k, v in sorted(tag_types.items())}
    out['trackers'] = {k: bool(re.search(v, blob)) for k, v in TRACKERS.items()}
    out['trackers']['google_ads'] = bool(ads) or any(k in tag_types for k in ('__awct', '__sp', '__awec'))
    out['trackers']['google_ads_call_tracking'] = '__awcc' in tag_types or bool(CALL_IN_PAGE.search(blob))
    out['trackers']['microsoft_uet'] = '__baut' in tag_types or out['trackers'].pop('microsoft_uet_in_page')
    out['promos'] = list(dict.fromkeys(out['promos']))[:15]
    out['prices'] = list(dict.fromkeys(out['prices']))[:25]
    out['phones'] = sorted(set(p for p in out['phones'] if len(p) == 10))
    domain = urllib.parse.urlparse(comp['urls'][0]).netloc.replace('www.', '')
    out['ads_transparency'] = f'https://adstransparency.google.com/?region=CA&domain={domain}'
    return out

def suggest(seeds, lang):
    res = {}
    for s in seeds:
        found = []
        for suffix in ['', ' ', ' a', ' p', ' m', ' r']:
            u = 'https://suggestqueries.google.com/complete/search?' + urllib.parse.urlencode({'client': 'firefox', 'hl': lang, 'gl': 'ca', 'q': s + suffix})
            try:
                with urllib.request.urlopen(urllib.request.Request(u, headers={'User-Agent': UA}), timeout=15, context=CTX) as r:
                    raw = r.read()
                try: data = json.loads(raw.decode('utf-8'))
                except UnicodeDecodeError: data = json.loads(raw.decode('latin-1'))
                found += data[1]
            except Exception:
                break
            time.sleep(0.25)
        res[s] = list(dict.fromkeys(found))
    return res

def previous_snapshot(today):
    files = sorted(f for f in glob.glob(os.path.join(DATA, '*.json')) if not f.endswith(f'{today}.json'))
    return json.load(open(files[-1], encoding='utf-8')) if files else None

def diff(new, old, key):
    a, b = set(new.get(key, [])), set(old.get(key, [])) if old else set()
    return sorted(a - b), sorted(b - a)

def report(snap, prev, today):
    L = [f'# Competitor watch — {today}', '',
         'Free scan of competitor websites (no API key). "Google Ads: yes" means a Google Ads conversion tag or account ID is configured on their site, the strongest public sign that they bid on Google. "Call tracking: yes" means a Google Ads website-call conversion tag is set up.',
         'For the ads themselves, open each Ads Transparency link (Google\'s free official library of every ad a domain runs in Canada).', '']
    L += ['## Summary', '', '| Competitor | Google Ads | Call tracking | Meta | Microsoft | Promos found | Changes since last run |', '|---|---|---|---|---|---|---|']
    for c in snap['competitors']:
        old = next((o for o in (prev or {}).get('competitors', []) if o['name'] == c['name']), None)
        changes = sum(len(x) for k in ('ads_ids', 'promos', 'prices', 'phones') for x in diff(c, old, k)) if old else 'first run'
        t = c['trackers']
        L.append(f"| {c['name']} | {'yes' if t.get('google_ads') else 'no'} | {'yes' if t.get('google_ads_call_tracking') else 'no'} | "
                 f"{'yes' if t.get('meta_pixel') else 'no'} | {'yes' if t.get('microsoft_uet') else 'no'} | {len(c['promos'])} | {changes} |")
    L.append('')
    for c in snap['competitors']:
        old = next((o for o in (prev or {}).get('competitors', []) if o['name'] == c['name']), None)
        L += [f"## {c['name']}", '', f"- Ads Transparency Center: {c['ads_transparency']}",
              f"- Google Ads IDs: {', '.join(c['ads_ids']) or 'none found'}",
              f"- Tags configured in their Tag Manager: {', '.join(f'{k} x{v}' for k, v in c.get('tag_types', {}).items()) or 'none of the ad tags'}",
              f"- Phones on site: {', '.join(c['phones']) or 'none'}"]
        if c['errors']: L.append(f"- Fetch problems: {'; '.join(c['errors'])}")
        if old:
            for key, label in (('promos', 'promo lines'), ('prices', 'price mentions'), ('ads_ids', 'Google Ads IDs'), ('phones', 'phone numbers')):
                added, removed = diff(c, old, key)
                if added: L += [f'- **New {label}:**'] + [f'  - {x}' for x in added[:10]]
                if removed: L += [f'- **Gone {label}:**'] + [f'  - {x}' for x in removed[:10]]
        L += ['', '**Promo lines on the site now:**'] + ([f'- {p}' for p in c['promos']] or ['- none found'])
        L += ['', '**Price mentions:**'] + ([f'- {p}' for p in c['prices'][:12]] or ['- none found']) + ['']
    if snap.get('suggestions'):
        L += ['## Keyword ideas from Google autocomplete (real searches, Canada)', '']
        for lang, seeds in snap['suggestions'].items():
            for seed, sug in seeds.items():
                L.append(f"- **{seed}** ({lang}): " + ' · '.join(sug[:15]))
        L.append('')
    return '\n'.join(L)

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--suggest', action='store_true', help='also pull Google autocomplete for the seed phrases')
    ap.add_argument('--config', default=os.path.join(HERE, 'competitors.json'))
    a = ap.parse_args()
    cfg = json.load(open(a.config, encoding='utf-8'))
    today = dt.date.today().isoformat()
    os.makedirs(DATA, exist_ok=True); os.makedirs(REPORTS, exist_ok=True)
    snap = {'date': today, 'competitors': []}
    for comp in cfg['competitors']:
        print(f"scanning {comp['name']}…", file=sys.stderr)
        snap['competitors'].append(scan(comp))
    if a.suggest:
        snap['suggestions'] = {lang: suggest(seeds, lang) for lang, seeds in cfg.get('suggest_seeds', {}).items()}
    prev = previous_snapshot(today)
    json.dump(snap, open(os.path.join(DATA, f'{today}.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    md = report(snap, prev, today)
    for name in (f'{today}.md', 'latest.md'):
        open(os.path.join(REPORTS, name), 'w', encoding='utf-8').write(md)
    print(os.path.join(REPORTS, f'{today}.md'))

if __name__ == '__main__':
    main()
