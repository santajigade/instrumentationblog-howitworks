# Swap the sidebar ad unit inside Custom HTML widgets 2, 4, 5, then clear the sidebar cache.
import json, os, base64, urllib.request
B = 'https://www.instrumentationblog.in/wp-json'
AUTH = 'Basic ' + base64.b64encode(f"{os.environ['U']}:{os.environ['P']}".encode()).decode()
def call(path, data=None):
    h = {'Authorization': AUTH, 'User-Agent': 'ib-ads/1.0', 'Content-Type': 'application/json'}
    rq = urllib.request.Request(B + path, data=json.dumps(data).encode() if data is not None else None, method='POST' if data is not None else 'GET', headers=h)
    with urllib.request.urlopen(rq, timeout=120) as r: return json.loads(r.read())
for n in (2, 4, 5):
    w = call(f'/wp/v2/widgets/custom_html-{n}?context=edit')
    raw = w['instance']['raw']; c = raw.get('content', '')
    print(n, 'old' if '5950781970' in c else 'no-old', c.count('6904203044'))
    if '5950781970' in c:
        raw['content'] = c.replace('5950781970', '6904203044')
        r = call(f'/wp/v2/widgets/custom_html-{n}', {'instance': {'raw': raw}})
        print(n, 'updated', '6904203044' in json.dumps(r))
# any post save clears the ibsb_v* transients (snippet hook on save_post_post)
print(call('/ib/v1/patch', {'id': 21492})['id'], 'cache cleared')
