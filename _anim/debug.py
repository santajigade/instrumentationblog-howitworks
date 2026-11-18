import json, os, re, base64, urllib.request
B = 'https://www.instrumentationblog.in/wp-json'
AUTH = 'Basic ' + base64.b64encode(f"{os.environ['U']}:{os.environ['P']}".encode()).decode()
def get(p):
    req = urllib.request.Request(B + p, headers={'Authorization': AUTH, 'User-Agent': 'ib-anim/1.0'})
    try:
        with urllib.request.urlopen(req, timeout=60) as r: return json.loads(r.read())
    except Exception as e: return {'ERR': str(e)}
for slug in ['mutual-inductance-coupling-coefficient','varactor-diode-working-principle','open-loop-and-closed-loop-control-system','npn-and-pnp-proximity-sensors','digital-pressure-gauge-working']:
    r = get('/wp/v2/posts?slug=' + slug + '&_fields=id')
    pid = r[0]['id']; w = get(f'/ib/v1/widgets/{pid}')
    allc = ' '.join(str(x.get('content','')) for x in w.get('widgets', []))
    i = allc.find('ib-anim')
    prev = [re.sub('<[^>]+>','',h) for h in re.findall(r'<h[23][^>]*>([\s\S]*?)</h[23]>', allc[:i])]
    nxt = [re.sub('<[^>]+>','',h) for h in re.findall(r'<h[23][^>]*>([\s\S]*?)</h[23]>', allc[i:])]
    print('PLACE', slug, 'found' if i >= 0 else 'MISSING', '| after:', prev[-1:] , '| before:', nxt[:1])
