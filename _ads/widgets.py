# Sidebar ads (Custom HTML widgets): 2 = top, 5 = middle, 4 = bottom.
# Top and bottom become Multiplex (3541747929), middle uses IB_Sidebar display unit (6904203044).
import json, os, re, base64, urllib.request
B = 'https://www.instrumentationblog.in/wp-json'
AUTH = 'Basic ' + base64.b64encode(f"{os.environ['U']}:{os.environ['P']}".encode()).decode()
def call(path, data=None):
    h = {'Authorization': AUTH, 'User-Agent': 'ib-ads/1.0', 'Content-Type': 'application/json'}
    rq = urllib.request.Request(B + path, data=json.dumps(data).encode() if data is not None else None, method='POST' if data is not None else 'GET', headers=h)
    with urllib.request.urlopen(rq, timeout=120) as r: return json.loads(r.read())
C = 'ca-pub-3931314195561246'
MULTI = f'<ins class="adsbygoogle" style="display:block" data-ad-format="autorelaxed" data-ad-client="{C}" data-ad-slot="3541747929"></ins>'
SIDE = f'<ins class="adsbygoogle" style="display:block" data-ad-client="{C}" data-ad-slot="6904203044" data-ad-format="auto" data-full-width-responsive="true"></ins>'
for n, tag in ((2, SIDE), (4, SIDE)):
    w = call(f'/wp/v2/widgets/custom_html-{n}?context=edit')
    raw = w['instance']['raw']; c = raw.get('content', '')
    new = re.sub(r'<ins class="adsbygoogle"[^>]*></ins>', tag, c, count=1)
    print(n, 'before:', re.findall(r'data-ad-slot="(\d+)"', c), 'after:', re.findall(r'data-ad-slot="(\d+)"', new))
    if new != c:
        raw['content'] = new
        call(f'/wp/v2/widgets/custom_html-{n}', {'instance': {'raw': raw}})
print(call('/ib/v1/patch', {'id': 21492})['id'], 'sidebar cache cleared')
