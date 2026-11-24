# Probe raw HTML around phrases that need factual fixes (24 Nov 2026)
import json, os, re, base64, urllib.request, urllib.parse
B = 'https://www.instrumentationblog.in/wp-json'
AUTH = 'Basic ' + base64.b64encode(f"{os.environ['U']}:{os.environ['P']}".encode()).decode()
def call(p):
    req = urllib.request.Request(B + p, headers={'Authorization': AUTH, 'User-Agent': 'ib-anim/1.0'})
    with urllib.request.urlopen(req, timeout=120) as r: return json.loads(r.read())
T = {'what-is-reynolds-number': [r'above 10,000', r'10,000.{0,3}200,000', r'200,000\+'],
     'basics-of-differential-pressure-transmitter': [r'closes the gap'],
     'lighting-design-calculation': [r'2\.5 m mounting', r'RI 2\.67'],
     'mass-flow-controller-working-principle': [r'four main MFC']}
for slug, pats in T.items():
    pid = call('/wp/v2/posts?slug=' + slug + '&_fields=id')[0]['id']
    raw = call(f'/wp/v2/posts/{pid}?context=edit&_fields=content')['content']['raw']
    try: w = call(f'/ib/v1/widgets/{pid}').get('widgets', [])
    except Exception as e: w = []; print('NOWIDGETS', slug, e)
    print('POST', slug, pid, 'rawlen', len(raw), 'widgets', len(w))
    for p in pats:
        for m in re.finditer(p, raw): print('RAW', slug, repr(raw[max(0, m.start()-300):m.end()+300]))
        for x in w:
            c = str(x.get('content', ''))
            for m in re.finditer(p, c): print('WID', slug, x.get('path'), x.get('type'), repr(c[max(0, m.start()-300):m.end()+300]))
