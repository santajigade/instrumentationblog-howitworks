# fetch: save raw content of posts listed in _patch/wp/slugs.txt to _patch/wp/<slug>.raw.html
# apply: for each slug with _patch/wp/<slug>.add.html and <slug>.anchor.txt, insert the addition right before
#        the first occurrence of the anchor text in the raw content and update the post.
import json, os, sys, base64, urllib.request, urllib.error
B = 'https://www.instrumentationblog.in/wp-json/wp/v2'
AUTH = 'Basic ' + base64.b64encode(f"{os.environ['U']}:{os.environ['P']}".encode()).decode()
def call(path, data=None):
    h = {'Authorization': AUTH, 'User-Agent': 'ib-patch/1.0', 'Content-Type': 'application/json'}
    rq = urllib.request.Request(B + path, data=json.dumps(data).encode() if data is not None else None,
                                method='POST' if data is not None else 'GET', headers=h)
    try:
        with urllib.request.urlopen(rq, timeout=120) as r: return json.loads(r.read())
    except urllib.error.HTTPError as e:
        b = e.read()[:400]
        print('HTTPERR', e.code, path, 'server=', e.headers.get('server'), 'cf-mitigated=', e.headers.get('cf-mitigated'), b)
        raise
mode = sys.argv[1]
for slug in open('_patch/wp/slugs.txt').read().split():
    posts = call(f'/posts?slug={slug}&context=edit')
    if not posts: print('NOTFOUND', slug); continue
    p = posts[0]; raw = p['content']['raw']
    if mode == 'fetch':
        open(f'_patch/wp/{slug}.raw.html', 'w').write(raw); print('FETCHED', slug, p['id'], len(raw))
    else:
        add_f, anc_f = f'_patch/wp/{slug}.add.html', f'_patch/wp/{slug}.anchor.txt'
        if not os.path.exists(add_f): continue
        add, anchor = open(add_f).read().strip(), open(anc_f).read().strip()
        if add[:80] in raw: print('ALREADY', slug); continue
        i = raw.find(anchor)
        if i < 0: print('ANCHOR_MISSING', slug); continue
        new = raw[:i] + add + '\n\n' + raw[i:]
        r = call(f"/posts/{p['id']}", {'content': new})
        print('UPDATED', slug, p['id'], len(raw), '->', len(r['content']['raw']) if 'raw' in r['content'] else 'ok')
