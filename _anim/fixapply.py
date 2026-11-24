# Apply factual contradiction fixes from _anim/fixes/changes/<slug>.json (see _anim/fixes/RULES.md)
import json, os, glob, csv, datetime, base64, urllib.request, urllib.parse
B = 'https://www.instrumentationblog.in/wp-json'
AUTH = 'Basic ' + base64.b64encode(f"{os.environ['U']}:{os.environ['P']}".encode()).decode()
def call(p, data=None):
    req = urllib.request.Request(B + p, data=data, method='POST' if data else 'GET',
          headers={'Authorization': AUTH, 'User-Agent': 'ib-anim/1.0', 'Content-Type': 'application/json'})
    with urllib.request.urlopen(req, timeout=120) as r: return json.loads(r.read())
lw = csv.writer(open('_anim/fixes/log.csv', 'a', newline=''))
for f in sorted(glob.glob('_anim/fixes/changes/*.json')):
    a = json.load(open(f)); slug = a['slug']
    try:
        pid = call('/wp/v2/posts?slug=' + urllib.parse.quote(slug) + '&_fields=id')[0]['id']
        ops = [{'find': o, 'mode': 'replace', 'html': n} for o, n in a['pairs']]
        res = call('/ib/v1/patch', json.dumps({'id': pid, 'ops': ops}).encode())
        w = ' '.join(str(x.get('content', '')) for x in call(f'/ib/v1/widgets/{pid}').get('widgets', []))
        good = all(n in w for o, n in a['pairs']) and all(x.get('applied', True) for x in res.get('report', []))
    except Exception as e:
        pid, res, good = '', {'error': str(e)[:150]}, False
    lw.writerow([datetime.date.today().isoformat(), slug, pid, 'ok' if good else 'fail', a.get('reason', ''), json.dumps(res)[:150]])
    print('FIX', slug, 'ok' if good else 'fail', json.dumps(res)[:200])
    if good: os.replace(f, f.replace('/changes/', '/applied/'))
