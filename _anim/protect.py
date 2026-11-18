import json, os, re, base64, urllib.request
B = 'https://www.instrumentationblog.in/wp-json'
AUTH = 'Basic ' + base64.b64encode(f"{os.environ['U']}:{os.environ['P']}".encode()).decode()
def call(path, data=None):
    req = urllib.request.Request(B + path, data=data, method='POST' if data else 'GET', headers={'Authorization': AUTH, 'User-Agent': 'ib-anim/1.0', 'Content-Type': 'application/json'})
    with urllib.request.urlopen(req, timeout=120) as r: return json.loads(r.read())
for pid in [13246, 8734, 5949, 5098, 9065]:
    w = call(f'/ib/v1/widgets/{pid}')
    for x in w['widgets']:
        m = re.search(r'<figure class="ib-anim"[\s\S]*?</figure>', str(x['content']))
        if not m: continue
        f = m.group(0)
        if 'draggable' in f: print(pid, 'already'); break
        g = f.replace('loading="lazy" ', 'loading="lazy" draggable="false" oncontextmenu="return false" ', 1).replace('rgba(0,0,0,0.12);"', 'rgba(0,0,0,0.12);-webkit-user-drag:none;user-select:none;"', 1)
        print(pid, call('/ib/v1/patch', json.dumps({'id': pid, 'ops': [{'find': f, 'mode': 'replace', 'html': g}]}).encode())['report']); break
