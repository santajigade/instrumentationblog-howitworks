import json, os, sys, base64, urllib.request
B = 'https://www.instrumentationblog.in/wp-json'
AUTH = 'Basic ' + base64.b64encode(f"{os.environ['U']}:{os.environ['P']}".encode()).decode()
for i in sys.argv[1].split(','):
    req = urllib.request.Request(f"{B}/wp/v2/posts/{i}", data=json.dumps({'status': 'publish'}).encode(), method='POST',
          headers={'Authorization': AUTH, 'Content-Type': 'application/json', 'User-Agent': 'ib-import/1.0'})
    with urllib.request.urlopen(req, timeout=120) as r: d = json.loads(r.read())
    print(i, d['status'], d['link'])
