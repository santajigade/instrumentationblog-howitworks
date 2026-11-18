import json, os, glob, base64, urllib.request
B = 'https://www.instrumentationblog.in/wp-json'
AUTH = 'Basic ' + base64.b64encode(f"{os.environ['U']}:{os.environ['P']}".encode()).decode()
H = {'Authorization': AUTH, 'User-Agent': 'ib-import/1.0'}
def call(path, data, ctype):
    req = urllib.request.Request(B + path, data=data, method='POST', headers=dict(H, **ctype))
    with urllib.request.urlopen(req, timeout=120) as r: return json.loads(r.read())
out = []
for f in sorted(glob.glob('_upload/ibtmp-*/*.json')):
    d = json.load(open(f)); p = d['payload']; slug = p['slug']
    img = f[:-5] + '.webp'
    m = call('/wp/v2/media', open(img, 'rb').read(), {'Content-Type': 'image/webp', 'Content-Disposition': f'attachment; filename="{slug}.webp"'})
    kw = p['rank_math_focus_keyword']
    call(f"/wp/v2/media/{m['id']}", json.dumps({'alt_text': kw, 'title': kw}).encode(), {'Content-Type': 'application/json'})
    body = dict(p, html=d['html'].replace('{{IMG}}', m['source_url']), featured_media=m['id'])
    r = call('/ib/v1/article', json.dumps(body).encode(), {'Content-Type': 'application/json'})
    r['media'] = m['id']; r['slug'] = slug; out.append(r); print(json.dumps(r))
os.makedirs('_import/results', exist_ok=True)
json.dump(out, open('_import/results/last.json', 'w'), indent=1)
