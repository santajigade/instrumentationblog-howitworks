import json, os, re, base64, urllib.request
B = 'https://www.instrumentationblog.in/wp-json'
AUTH = 'Basic ' + base64.b64encode(f"{os.environ['U']}:{os.environ['P']}".encode()).decode()
def call(path, data=None):
    req = urllib.request.Request(B + path, data=data, method='POST' if data else 'GET', headers={'Authorization': AUTH, 'User-Agent': 'ib-anim/1.0', 'Content-Type': 'application/json'})
    with urllib.request.urlopen(req, timeout=120) as r: return json.loads(r.read())
pid = 13246
w = call(f'/ib/v1/widgets/{pid}')
figs = []
for x in w['widgets']:
    figs += re.findall(r'<figure class="ib-anim"[\s\S]*?</figure>', str(x['content']))
print('found', len(figs))
if len(figs) > 1:
    res = call('/ib/v1/patch', json.dumps({'id': pid, 'ops': [{'find': figs[-1], 'mode': 'replace', 'html': ' '}]}).encode())
    print(res)
w = call(f'/ib/v1/widgets/{pid}')
print('now', sum(len(re.findall(r'<figure class="ib-anim"', str(x['content']))) for x in w['widgets']))
