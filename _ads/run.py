# Swap the old single ad unit for position units (and add multiplex) on existing posts.
import json, os, sys, base64, urllib.request, urllib.error, csv, datetime
sys.path.insert(0, os.path.dirname(__file__)); from slots import OLD, MULTI, QUOTE, MULTIPLEX, order
B = 'https://www.instrumentationblog.in/wp-json'
AUTH = 'Basic ' + base64.b64encode(f"{os.environ['U']}:{os.environ['P']}".encode()).decode()
def call(path, data=None):
    h = {'Authorization': AUTH, 'User-Agent': 'ib-ads/1.0', 'Content-Type': 'application/json'}
    rq = urllib.request.Request(B + path, data=json.dumps(data).encode() if data is not None else None, method='POST' if data is not None else 'GET', headers=h)
    with urllib.request.urlopen(rq, timeout=120) as r: return json.loads(r.read())
Q = '_ads/queue.json'
if not os.path.exists(Q):
    ids, pg = [], 1
    while True:
        try: b = call(f'/wp/v2/posts?per_page=100&page={pg}&status=publish&_fields=id,slug&orderby=id&order=asc')
        except urllib.error.HTTPError: break
        if not b: break
        ids += [{'id': x['id'], 'slug': x['slug'], 'status': 'todo'} for x in b]; pg += 1
    json.dump(ids, open(Q, 'w'), indent=0); print('queued', len(ids))
q = json.load(open(Q)); n = int(sys.argv[1]) if len(sys.argv) > 1 else 100
lw = csv.writer(open('_ads/log.csv', 'a', newline=''))
for it in [x for x in q if x['status'] == 'todo'][:n]:
    pid = it['id']
    try:
        try:
            w = call(f'/ib/v1/widgets/{pid}')['widgets']; mode = 'el'
        except urllib.error.HTTPError as e:
            if e.code != 404: raise
            raw = call(f'/wp/v2/posts/{pid}?context=edit&_fields=content')['content']['raw']; mode = 'classic'
        if mode == 'el':
            txt = ''.join(str(x['content']) for x in w)
            k = txt.count(OLD); ops = [{'find': OLD, 'mode': 'replace', 'html': f'data-ad-slot="{s}"'} for s in order(k)]
            if MULTI not in txt and QUOTE in txt: ops.append({'find': QUOTE, 'mode': 'before', 'html': MULTIPLEX})
            if ops:
                r = call('/ib/v1/patch', {'id': pid, 'ops': ops})
                bad = [x for x in r['report'] if not x.get('applied', True)]
                if bad: raise Exception('ops not applied: %s' % bad)
        else:
            from slots import rewrite
            new = rewrite(raw); k = raw.count(OLD)
            if new != raw: call(f'/wp/v2/posts/{pid}', {'content': new})
        it['status'] = 'done' if k else 'noads'; note = f'{mode} ads={k}'
    except Exception as e:
        it['status'] = 'failed'; note = str(e)[:150]
    lw.writerow([datetime.date.today().isoformat(), it['slug'], pid, it['status'], note]); print(it['slug'], it['status'], note)
json.dump(q, open(Q, 'w'), indent=0)
print('left', sum(x['status'] == 'todo' for x in q))
