# Upload 3 figures per post and insert them after the chosen H2s.
# _img/changes/<slug>.json = {"slug":..., "figs":[{"name":..., "alt":..., "caption":..., "after_h2": "<exact H2 text>", "svg": "<svg ...>"}]}
import json, os, re, glob, io, base64, urllib.request, csv, datetime, html
import cairosvg
from PIL import Image
B = 'https://www.instrumentationblog.in/wp-json'
AUTH = 'Basic ' + base64.b64encode(f"{os.environ['U']}:{os.environ['P']}".encode()).decode()
def call(path, data=None, h=None):
    hd = {'Authorization': AUTH, 'User-Agent': 'ib-img/1.0'}; hd.update(h or {})
    req = urllib.request.Request(B + path, data=data, method='POST' if data is not None else 'GET', headers=hd)
    with urllib.request.urlopen(req, timeout=120) as r: return json.loads(r.read())
def txt(s): return re.sub(r'\s+', ' ', html.unescape(re.sub('<[^>]+>', '', s))).strip()
queue = json.load(open('_img/queue.json')); qi = {x['slug']: x for x in queue}
lw = csv.writer(open('_img/log.csv', 'a', newline=''))
for f in sorted(glob.glob('_img/changes/*.json')):
    a = json.load(open(f)); p = json.load(open(f"_img/pages/{a['slug']}.json")); pid = p['id']
    try:
        if p['mode'] == 'elementor':
            w = call(f'/ib/v1/widgets/{pid}')['widgets']
            if 'ib-img' in json.dumps(w): raise Exception('already has ib-img figures')
        else:
            raw = call(f'/wp/v2/posts/{pid}?context=edit&_fields=content')['content']['raw']
            if 'ib-img' in raw: raise Exception('already has ib-img figures')
        ops, newsec, done = [], [], []
        for fg in a['figs']:
            png = cairosvg.svg2png(bytestring=fg['svg'].strip().encode(), output_width=1600)
            im = Image.open(io.BytesIO(png)).convert('RGB'); buf = io.BytesIO(); im.save(buf, 'WEBP', quality=86, method=6)
            open(f"_img/webp/{fg['name']}.webp", 'wb').write(buf.getvalue())
            m = call('/wp/v2/media', buf.getvalue(), {'Content-Type': 'image/webp', 'Content-Disposition': f'attachment; filename="{fg["name"]}.webp"'})
            call(f"/wp/v2/media/{m['id']}", json.dumps({'alt_text': fg['alt'], 'title': fg['alt'], 'caption': fg['caption']}).encode(), {'Content-Type': 'application/json'})
            hh = round(im.height * 1200 / im.width)
            fig = (f'<figure class="ib-img" style="text-align:center; margin:30px 0;"><img src="{m["source_url"]}" alt="{fg["alt"]}" title="{fg["alt"]}" width="1200" height="{hh}" loading="lazy" '
                   f'style="width:100%; max-width:820px; height:auto; border:1px solid #e5e7eb; border-radius:12px; box-shadow:0 4px 20px rgba(0,0,0,0.08);">'
                   f'<figcaption style="font-size:14px; color:#6b7280; font-style:italic; margin-top:8px;">{fg["caption"]}</figcaption></figure>')
            placed = False
            if p['mode'] == 'elementor':
                for x in w:
                    c = str(x['content'])
                    if x['type'] in ('html', 'text-editor'):
                        for h2 in re.finditer(r'<h2[^>]*>([\s\S]*?)</h2>', c):
                            if txt(h2.group(1)) == fg['after_h2'] and c.count(h2.group(0)) == 1:
                                # after the first paragraph that follows the heading, if any
                                rest = c[h2.end():]; pm = re.match(r'\s*<p[\s\S]*?</p>', rest)
                                anchor = h2.group(0) + (pm.group(0) if pm else '')
                                if c.count(anchor) == 1: ops.append({'find': anchor, 'mode': 'after', 'html': fig})
                                else: ops.append({'find': h2.group(0), 'mode': 'after', 'html': fig})
                                placed = True; break
                    elif x['type'] == 'heading' and txt(c) == fg['after_h2']:
                        newsec.append({'index': int(x['path'].split('.')[0]) + 1, 'html': fig}); placed = True
                    if placed: break
            else:
                for h2 in re.finditer(r'<h2[^>]*>([\s\S]*?)</h2>(\s*<!-- /wp:heading -->)?', raw):
                    if txt(h2.group(1)) == fg['after_h2']:
                        blk = ('\n<!-- wp:html -->\n' + fig + '\n<!-- /wp:html -->\n') if '<!-- wp:' in raw else fig
                        raw = raw[:h2.end()] + blk + raw[h2.end():]; placed = True; break
            if not placed: raise Exception('heading not found: ' + fg['after_h2'][:50])
            done.append(fg['name'])
        if p['mode'] == 'elementor':
            if ops: res = call('/ib/v1/patch', json.dumps({'id': pid, 'ops': ops}).encode(), {'Content-Type': 'application/json'}); assert all(r.get('applied', True) for r in res.get('report', [])), res
            for ns in sorted(newsec, key=lambda z: -z['index']):
                call('/ib/v1/patch', json.dumps({'id': pid, 'new_section': ns}).encode(), {'Content-Type': 'application/json'})
        else:
            call(f'/wp/v2/posts/{pid}', json.dumps({'content': raw}).encode(), {'Content-Type': 'application/json'})
        ok = True; note = '|'.join(done)
    except Exception as e:
        ok = False; note = str(e)[:150]
    lw.writerow([datetime.date.today().isoformat(), a['slug'], pid, 'ok' if ok else 'fail', note])
    qi[a['slug']]['status'] = 'done' if ok else 'failed'
    print(a['slug'], ok, note)
    if ok: os.replace(f, f.replace('/changes/', '/applied/'))
json.dump(queue, open('_img/queue.json', 'w'), indent=0)
