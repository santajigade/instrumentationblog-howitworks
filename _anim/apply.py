import json, os, re, glob, base64, urllib.request, urllib.parse, csv, datetime
B = 'https://www.instrumentationblog.in/wp-json'
AUTH = 'Basic ' + base64.b64encode(f"{os.environ['U']}:{os.environ['P']}".encode()).decode()
H = {'Authorization': AUTH, 'User-Agent': 'ib-anim/1.0'}
def call(path, data=None, ctype='application/json', method=None):
    req = urllib.request.Request(B + path, data=data, method=method or ('POST' if data else 'GET'), headers=dict(H, **({'Content-Type': ctype} if data else {})))
    if ctype.startswith('image'): req.add_header('Content-Disposition', f'attachment; filename="{os.path.basename(path_file)}"')
    with urllib.request.urlopen(req, timeout=120) as r: return json.loads(r.read())
WORK = re.compile(r'(work|principle|how .* works|operation)', re.I)
lw = csv.writer(open('_anim/log.csv', 'a', newline=''))
for f in sorted(glob.glob('_anim/todo/*.json')):
    a = json.load(open(f)); path_file = '_anim/' + a['file']
    try:
        posts = call('/wp/v2/posts?slug=' + urllib.parse.quote(a['blog']) + '&_fields=id')
        pid = posts[0]['id']; w = call(f'/ib/v1/widgets/{pid}')
        if 'class="ib-anim"' in json.dumps(w): raise Exception('already has animation')
        m = call('/wp/v2/media', open(path_file, 'rb').read(), 'image/webp')
        call(f"/wp/v2/media/{m['id']}", json.dumps({'alt_text': a['alt'], 'title': a['alt'], 'caption': a['alt']}).encode())
        html = a['html'].replace('{{IMG}}', m['source_url']).replace('<figure ', '<figure class="ib-anim" ', 1)
        data = {'id': pid}; plan = None
        for x in w.get('widgets', []):
            c = str(x['content']); hs = list(re.finditer(r'<h2[^>]*>([\s\S]*?)</h2>', c))
            if not hs: continue
            pick = next((h for h in hs[1:] if WORK.search(re.sub('<[^>]+>', '', h.group(1)))), hs[1] if len(hs) > 1 else hs[0])
            tag = pick.group(0)
            if c.count(tag) == 1: plan = {'ops': [{'find': tag, 'mode': 'after', 'html': html}]}; break
        if not plan:
            idx = next((int(x['path'].split('.')[0]) + 1 for x in w['widgets'] if x['type'] == 'text-editor'), 1)
            plan = {'new_section': {'index': idx, 'html': html}}
        data.update(plan)
        res = call('/ib/v1/patch', json.dumps(data).encode())
        ok = all(r.get('applied', True) for r in res.get('report', []))
    except Exception as e:
        res = {'error': str(e)[:150]}; ok = False
    lw.writerow([datetime.date.today().isoformat(), a['blog'], 'ok' if ok else 'fail', json.dumps(res)[:200]])
    print(a['blog'], ok, json.dumps(res)[:200])
    if ok: os.replace(f, f.replace('/todo/', '/done/'))
