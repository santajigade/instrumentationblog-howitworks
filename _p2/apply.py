import json, os, glob, base64, urllib.request, csv, datetime
B = 'https://www.instrumentationblog.in/wp-json'
AUTH = 'Basic ' + base64.b64encode(f"{os.environ['U']}:{os.environ['P']}".encode()).decode()
os.makedirs('_p2/applied', exist_ok=True); os.makedirs('_p2/changes', exist_ok=True)
queue = json.load(open('_p2/queue.json')); qi = {x['slug']: x for x in queue}
lw = csv.writer(open('_p2/log.csv', 'a', newline='')); ok = 0
for f in sorted(glob.glob('_p2/changes/*.json')):
    a = json.load(open(f)); p = json.load(open(f"_p2/pages/{a['slug']}.json")); plan = p['plan']
    data = {'id': p['id']}
    if 'new_section' in plan: data['new_section'] = {'index': plan['new_section'], 'html': a['html']}
    else: data['ops'] = [{'find': plan['find'], 'mode': 'before', 'html': a['html']}]
    req = urllib.request.Request(B + '/ib/v1/patch', data=json.dumps(data).encode(), method='POST',
          headers={'Authorization': AUTH, 'Content-Type': 'application/json', 'User-Agent': 'ib-p2/1.0'})
    try:
        with urllib.request.urlopen(req, timeout=90) as r: res = json.loads(r.read())
        good = all(x.get('applied', True) for x in res.get('report', []))
    except Exception as e:
        res = {'error': str(e)[:150]}; good = False
    lw.writerow([datetime.date.today().isoformat(), a['slug'], p['id'], 'ok' if good else 'fail', '|'.join(a.get('targets', [])), json.dumps(res)[:150]])
    qi[a['slug']]['status'] = 'done' if good else 'failed'
    if good: ok += 1; os.replace(f, f.replace('/changes/', '/applied/'))
json.dump(queue, open('_p2/queue.json', 'w'), indent=1)
print('applied', ok)
