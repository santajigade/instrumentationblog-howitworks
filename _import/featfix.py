# Replace the featured image (and the figure under the intro box) of existing posts.
# Files: _import/featfix/<slug>.webp ; map slug -> post id in _import/featfix/map.json
import json, os, base64, urllib.request
B = 'https://www.instrumentationblog.in/wp-json'
AUTH = 'Basic ' + base64.b64encode(f"{os.environ['U']}:{os.environ['P']}".encode()).decode()
def call(path, data=None, h=None, method=None):
    hd = {'Authorization': AUTH, 'User-Agent': 'ib-import/1.0'}; hd.update(h or {})
    req = urllib.request.Request(B + path, data=data, method=method or ('POST' if data is not None else 'GET'), headers=hd)
    with urllib.request.urlopen(req, timeout=120) as r: return json.loads(r.read())
M = json.load(open('_import/featfix/map.json'))
for slug, pid in M.items():
    post = call(f'/wp/v2/posts/{pid}?context=edit&_fields=id,featured_media,rank_math_focus_keyword')
    old = call(f"/wp/v2/media/{post['featured_media']}?_fields=source_url")['source_url']
    kw = call(f'/ib/v1/seo/{pid}').get('rank_math_focus_keyword') or slug.replace('-', ' ')
    kw = kw.split(',')[0].strip()
    m = call('/wp/v2/media', open(f'_import/featfix/{slug}.webp', 'rb').read(), {'Content-Type': 'image/webp', 'Content-Disposition': f'attachment; filename="{slug}.webp"'})
    call(f"/wp/v2/media/{m['id']}", json.dumps({'alt_text': kw, 'title': kw}).encode(), {'Content-Type': 'application/json'})
    res = call('/ib/v1/patch', json.dumps({'id': pid, 'ops': [{'find': old, 'mode': 'replace', 'html': m['source_url']}]}).encode(), {'Content-Type': 'application/json'})
    call(f'/wp/v2/posts/{pid}', json.dumps({'featured_media': m['id']}).encode(), {'Content-Type': 'application/json'})
    print(slug, pid, 'old', old.split('/')[-1], 'new', m['source_url'].split('/')[-1], json.dumps(res.get('report', res))[:120])
