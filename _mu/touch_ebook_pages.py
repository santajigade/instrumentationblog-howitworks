# Re-save the eBook shop page and its child pages so LiteSpeed purges their cached HTML.
import json, os, base64, urllib.request
B = 'https://www.instrumentationblog.in/wp-json'
A = 'Basic ' + base64.b64encode(f"{os.environ['WU']}:{os.environ['WP']}".encode()).decode()
def call(p, d=None):
    rq = urllib.request.Request(B + p, data=json.dumps(d).encode() if d is not None else None, method='POST' if d is not None else 'GET', headers={'Authorization': A, 'User-Agent': 'ib-mu/1.0', 'Content-Type': 'application/json'})
    with urllib.request.urlopen(rq, timeout=120) as r: return json.loads(r.read())
shop = call('/wp/v2/pages?slug=instrumentation-ebooks&_fields=id')[0]['id']
ids = [shop] + [p['id'] for p in call(f'/wp/v2/pages?parent={shop}&per_page=100&_fields=id')]
for i in ids:
    try: call('/ib/v1/patch', {'id': i}); print('touched', i)
    except Exception as e: print('fail', i, e)
