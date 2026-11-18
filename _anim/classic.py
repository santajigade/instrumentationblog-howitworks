# Embed animation into a non-Elementor post by editing post content directly.
import json, os, re, glob, base64, urllib.request, urllib.parse, csv, datetime
B = 'https://www.instrumentationblog.in/wp-json'
AUTH = 'Basic ' + base64.b64encode(f"{os.environ['U']}:{os.environ['P']}".encode()).decode()
def call(path, data=None, ctype='application/json', fname=None):
    h = {'Authorization': AUTH, 'User-Agent': 'ib-anim/1.0'}
    if data is not None: h['Content-Type'] = ctype
    if fname: h['Content-Disposition'] = f'attachment; filename="{fname}"'
    req = urllib.request.Request(B + path, data=data, method='POST' if data is not None else 'GET', headers=h)
    with urllib.request.urlopen(req, timeout=120) as r: return json.loads(r.read())
BAD = re.compile(r'(faq|question|watch|video|reference|download|further reading)', re.I)
WORK = re.compile(r'(work|principle|operation)', re.I)
for f in sorted(glob.glob('_anim/todo/*.json')):
    a = json.load(open(f))
    pid = call('/wp/v2/posts?slug=' + urllib.parse.quote(a['blog']) + '&_fields=id')[0]['id']
    post = call(f'/wp/v2/posts/{pid}?context=edit&_fields=content')
    raw = post['content']['raw']
    if 'ib-anim' in raw: print('already'); continue
    fk = (call(f'/ib/v1/seo/{pid}').get('rank_math_focus_keyword') or a['blog']).split(',')[0].strip()
    alt = fk + ' animation'
    m = call('/wp/v2/media', open('_anim/' + a['file'], 'rb').read(), 'image/webp', re.sub(r'[^a-z0-9]+', '-', fk.lower()).strip('-') + '-animation.webp')
    call(f"/wp/v2/media/{m['id']}", json.dumps({'alt_text': alt, 'title': alt, 'caption': alt}).encode())
    fig = re.sub(r'alt="[^"]*" title="[^"]*"', f'alt="{alt}" title="{alt}"', a['html']).replace('{{IMG}}', m['source_url']).replace('<figure ', '<figure class="ib-anim" ', 1)
    if '<!-- wp:' in raw: fig = '\n<!-- wp:html -->\n' + fig + '\n<!-- /wp:html -->\n'
    hs = [h for h in re.finditer(r'<h2[^>]*>([\s\S]*?)</h2>(\s*<!-- /wp:heading -->)?', raw) if not BAD.search(re.sub('<[^>]+>', '', h.group(1)))]
    pick = next((h for h in hs if WORK.search(re.sub('<[^>]+>', '', h.group(1)))), hs[1] if len(hs) > 1 else hs[0])
    new = raw[:pick.end()] + fig + raw[pick.end():]
    res = call(f'/wp/v2/posts/{pid}', json.dumps({'content': new}).encode())
    print(a['blog'], pid, 'ok', re.sub('<[^>]+>', '', pick.group(1))[:60], res.get('link'))
    os.makedirs('_anim/done', exist_ok=True); os.replace(f, f.replace('/todo/', '/done/'))
