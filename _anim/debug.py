import json, os, base64, urllib.request
B = 'https://www.instrumentationblog.in/wp-json'
AUTH = 'Basic ' + base64.b64encode(f"{os.environ['U']}:{os.environ['P']}".encode()).decode()
def get(p):
    req = urllib.request.Request(B + p, headers={'Authorization': AUTH, 'User-Agent': 'ib-anim/1.0'})
    try:
        with urllib.request.urlopen(req, timeout=60) as r: return json.loads(r.read())
    except Exception as e: return {'ERR': str(e)}
r = get('/wp/v2/posts?slug=radar-type-level-transmitter&_fields=id,type,status'); print('posts', r)
r2 = get('/wp/v2/pages?slug=radar-type-level-transmitter&_fields=id,type'); print('pages', r2)
if isinstance(r, list) and r:
    pid = r[0]['id']; w = get(f'/ib/v1/widgets/{pid}'); print('widgets', str(w)[:300]); print('seo', str(get(f'/ib/v1/seo/{pid}'))[:300])
