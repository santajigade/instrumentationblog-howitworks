import json, os, base64, urllib.request
AUTH = 'Basic ' + base64.b64encode(f"{os.environ['U']}:{os.environ['P']}".encode()).decode()
req = urllib.request.Request('https://www.instrumentationblog.in/wp-json/rankmath/v1/toolsAction', data=json.dumps({'action': 'update_seo_score'}).encode(), method='POST',
      headers={'Authorization': AUTH, 'Content-Type': 'application/json', 'User-Agent': 'ib-import/1.0'})
try:
    with urllib.request.urlopen(req, timeout=300) as r: print(r.status, r.read()[:300])
except urllib.error.HTTPError as e: print(e.code, e.read()[:300])
