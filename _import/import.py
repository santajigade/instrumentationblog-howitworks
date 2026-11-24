import sys as _s, os as _o; _s.path.insert(0, _o.path.join(_o.path.dirname(_o.path.abspath(__file__)), '..', '_ads'))
from slots import rewrite as rewrite_ads
import json, os, re, glob, base64, urllib.request
B = 'https://www.instrumentationblog.in/wp-json'
AUTH = 'Basic ' + base64.b64encode(f"{os.environ['U']}:{os.environ['P']}".encode()).decode()
H = {'Authorization': AUTH, 'User-Agent': 'ib-import/1.0'}
def call(path, data, ctype):
    req = urllib.request.Request(B + path, data=data, method='POST', headers=dict(H, **ctype))
    with urllib.request.urlopen(req, timeout=120) as r: return json.loads(r.read())
out = []
for f in sorted(glob.glob('_upload/ibtmp-*/*.json')):
    d = json.load(open(f)); p = d['payload']; slug = p['slug']
    if any(isinstance(c, str) for c in p.get('categories', [])):
        ids = []
        for c in p['categories']:
            if isinstance(c, str):
                rq = urllib.request.Request(B + '/wp/v2/categories?slug=' + c, headers=H)
                with urllib.request.urlopen(rq, timeout=60) as r: c = json.loads(r.read())[0]['id']
            ids.append(c)
        p['categories'] = ids
    img = f[:-5] + '.webp'
    m = call('/wp/v2/media', open(img, 'rb').read(), {'Content-Type': 'image/webp', 'Content-Disposition': f'attachment; filename="{slug}.webp"'})
    kw = p['rank_math_focus_keyword']
    call(f"/wp/v2/media/{m['id']}", json.dumps({'alt_text': kw, 'title': kw}).encode(), {'Content-Type': 'application/json'})
    html = d['html'].replace('{{IMG}}', m['source_url'])
    # Article figures (VERSION 10): {{IMG:<name>.webp}} placeholders, files sit next to the json
    for fn in sorted(set(re.findall(r'\{\{IMG:([a-z0-9-]+\.webp)\}\}', html))):
        fp = os.path.join(os.path.dirname(f), fn)
        am = re.search(r'\{\{IMG:' + re.escape(fn) + r'\}\}" alt="([^"]*)"', html)
        a_alt = am.group(1) if am else fn[:-5].replace('-', ' ')
        mi = call('/wp/v2/media', open(fp, 'rb').read(), {'Content-Type': 'image/webp', 'Content-Disposition': f'attachment; filename="{fn}"'})
        call(f"/wp/v2/media/{mi['id']}", json.dumps({'alt_text': a_alt, 'title': a_alt, 'caption': a_alt}).encode(), {'Content-Type': 'application/json'})
        html = html.replace('{{IMG:' + fn + '}}', mi['source_url'])
    assert '{{IMG' not in html, slug
    html = rewrite_ads(html)
    body = dict(p, html=html, featured_media=m['id'])
    r = call('/ib/v1/article', json.dumps(body).encode(), {'Content-Type': 'application/json'})
    r['media'] = m['id']; r['slug'] = slug; out.append(r); print(json.dumps(r))
os.makedirs('_import/results', exist_ok=True)
json.dump(out, open('_import/results/last.json', 'w'), indent=1)
