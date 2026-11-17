import json, os, glob, base64, urllib.request, csv, datetime
B = 'https://www.instrumentationblog.in/wp-json'
AUTH = 'Basic ' + base64.b64encode(f"{os.environ['U']}:{os.environ['P']}".encode()).decode()
BOX = ('<div style="border:2px solid #0186e0;border-left:8px solid #0186e0;background:#f3f9ff;border-radius:10px;padding:18px 22px;margin:24px 0;">'
       '<div style="font-weight:700;color:#0186e0;font-size:14px;letter-spacing:1px;text-transform:uppercase;margin-bottom:6px;">Quick Answer</div>'
       '<p style="font-size:22px;font-weight:700;line-height:1.35;margin:0 0 10px;color:#1a2b4a;">{q}</p>{body}</div>')
queue = json.load(open('_geo/queue.json')); qi = {x['slug']: x for x in queue}
log = open('_geo/log.csv', 'a', newline=''); lw = csv.writer(log); ok = 0
for f in sorted(glob.glob('_geo/answers/*.json')):
    a = json.load(open(f)); p = json.load(open(f"_geo/pages/{a['slug']}.json")); plan = p['plan']
    box = BOX.format(q=a['question'], body=a['body_html'])
    data = {'id': p['id']}
    if 'new_section' in plan: data['new_section'] = {'index': plan['new_section'], 'html': box}
    else: data['ops'] = [{'find': plan['find'], 'mode': 'before', 'html': box}]
    req = urllib.request.Request(B + '/ib/v1/patch', data=json.dumps(data).encode(), method='POST',
                                 headers={'Authorization': AUTH, 'Content-Type': 'application/json', 'User-Agent': 'ib-geo/1.0'})
    try:
        with urllib.request.urlopen(req, timeout=90) as r: res = json.loads(r.read())
        rep = res.get('report', []); good = all(x.get('applied', True) for x in rep)
    except Exception as e:
        res = {'error': str(e)[:150]}; good = False
    lw.writerow([datetime.date.today().isoformat(), a['slug'], p['id'], 'ok' if good else 'fail', a['question'], json.dumps(res)[:150]])
    if good:
        ok += 1; qi[a['slug']]['status'] = 'done'; os.replace(f, f.replace('/answers/', '/applied/'))
    else:
        qi[a['slug']]['status'] = 'failed'
json.dump(queue, open('_geo/queue.json', 'w'), indent=0)
print('applied', ok)
