import json, os, glob, base64, urllib.request, csv, datetime
B = 'https://www.instrumentationblog.in/wp-json'
AUTH = 'Basic ' + base64.b64encode(f"{os.environ['U']}:{os.environ['P']}".encode()).decode()
os.makedirs('_seo/applied', exist_ok=True); os.makedirs('_seo/changes', exist_ok=True)
queue = json.load(open('_seo/ctr_queue.json')); qi = {x['slug']: x for x in queue}
lw = csv.writer(open('_seo/log.csv', 'a', newline='')); ok = 0
for f in sorted(glob.glob('_seo/changes/*.json')):
    c = json.load(open(f)); p = json.load(open(f"_seo/pages/{c['slug']}.json"))
    t, d = c['rank_math_title'], c['rank_math_description']
    if len(t) > 60 or not (120 <= len(d) <= 160):
        lw.writerow([datetime.date.today().isoformat(), c['slug'], p['id'], 'rejected_length', len(t), len(d), '', '']); continue
    req = urllib.request.Request(B + '/ib/v1/patch', data=json.dumps({'id': p['id'], 'rank_math_title': t, 'rank_math_description': d}).encode(),
                                 method='POST', headers={'Authorization': AUTH, 'Content-Type': 'application/json', 'User-Agent': 'ib-seo/1.0'})
    try:
        with urllib.request.urlopen(req, timeout=90) as r: json.loads(r.read()); good = True
    except Exception as e:
        good = False; err = str(e)[:120]
    lw.writerow([datetime.date.today().isoformat(), c['slug'], p['id'], 'ok' if good else 'fail', p['rank_math_title'], p['rank_math_description'], t, d])
    if good:
        ok += 1; qi[c['slug']]['status'] = 'done'; os.replace(f, f.replace('/changes/', '/applied/'))
    else: qi[c['slug']]['status'] = 'failed'
json.dump(queue, open('_seo/ctr_queue.json', 'w'), indent=0)
print('applied', ok)
