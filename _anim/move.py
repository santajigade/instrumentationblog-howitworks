import json, os, re, base64, urllib.request, html as H
B = 'https://www.instrumentationblog.in/wp-json'
AUTH = 'Basic ' + base64.b64encode(f"{os.environ['U']}:{os.environ['P']}".encode()).decode()
def call(path, data=None):
    req = urllib.request.Request(B + path, data=data, method='POST' if data else 'GET', headers={'Authorization': AUTH, 'User-Agent': 'ib-anim/1.0', 'Content-Type': 'application/json'})
    with urllib.request.urlopen(req, timeout=120) as r: return json.loads(r.read())
def txt(s): return re.sub(r'\s+', ' ', H.unescape(re.sub('<[^>]+>', '', s))).strip()
import urllib.parse
MOVES = {'maximum-power-transfer-theorem': ('What Is the Maximum Power Transfer Theorem?', 'after'), '7-segment-display-decoder': ('BCD to 7 Segment Decoder ICs', 'after'), 'time-of-flight-sensor-working': ('How a Time of Flight Sensor Measures Distance', 'after'), 'cathode-ray-oscilloscope-cro-explained': ('Cathode Ray Oscilloscope (CRO)', 'after')}
for slug, (target, mode) in MOVES.items():
    pid = call('/wp/v2/posts?slug=' + urllib.parse.quote(slug) + '&_fields=id')[0]['id']
    w = call(f'/ib/v1/widgets/{pid}')
    fig = None
    for x in w['widgets']:
        m = re.search(r'<figure class="ib-anim"[\s\S]*?</figure>', str(x['content']))
        if m: fig = m.group(0); break
    if not fig: print(pid, 'no figure'); continue
    plan = None
    for x in w['widgets']:
        c = str(x['content'])
        if x['type'] in ('html', 'text-editor'):
            for h in re.finditer(r'<h2[^>]*>([\s\S]*?)</h2>', c):
                if txt(h.group(1)) == target and c.count(h.group(0)) == 1:
                    plan = {'ops': [{'find': fig, 'mode': 'replace', 'html': ' '}, {'find': h.group(0), 'mode': mode, 'html': fig}]}
        elif x['type'] == 'heading' and txt(c) == target:
            plan = {'ops': [{'find': fig, 'mode': 'replace', 'html': ' '}], 'new_section': {'index': int(x['path'].split('.')[0]) + 1, 'html': fig}}
        if plan: break
    if not plan: print(pid, 'target not found', [ (x['type'], txt(str(x['content']))[:50]) for x in w['widgets'] if x['type']=='heading'][:12]); continue
    res = call('/ib/v1/patch', json.dumps(dict(id=pid, **plan)).encode())
    print(pid, res)
