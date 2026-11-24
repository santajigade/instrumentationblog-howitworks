# Factual fixes approved by Santaji on 24 Nov 2026 (find and replace in live article HTML)
import json, os, base64, urllib.request
B = 'https://www.instrumentationblog.in/wp-json'
AUTH = 'Basic ' + base64.b64encode(f"{os.environ['U']}:{os.environ['P']}".encode()).decode()
def call(p, data=None):
    req = urllib.request.Request(B + p, data=data, method='POST' if data else 'GET',
          headers={'Authorization': AUTH, 'User-Agent': 'ib-anim/1.0', 'Content-Type': 'application/json'})
    with urllib.request.urlopen(req, timeout=120) as r: return json.loads(r.read())
FIX = {
 'what-is-reynolds-number': [
  ('Most differential pressure flow meters (orifice plates, venturis) are calibrated assuming turbulent flow at Re above 10,000. Below that Re, the discharge coefficient shifts and measurement error increases. At laminar Re, only Coriolis, positive displacement or magnetic meters (for conductive liquids) give reliable measurements.',
   'Orifice plates are calibrated for turbulent flow, typically above Re 5,000 to 10,000 depending on the beta ratio. Classical venturi tubes need Re of 200,000 or more to use the ISO 5167 discharge coefficient without calibration; below that they must be calibrated. At laminar Re, only Coriolis, positive displacement or magnetic meters give reliable readings.'),
  ('orifice plates and venturis need Re above 10,000-200,000 for accurate Cd.',
   'orifice plates need Re above about 10,000, and classical venturi tubes need Re of 200,000 or more, for an accurate Cd without calibration.')],
 'basics-of-differential-pressure-transmitter': [
  ('This closes the gap on the HP side (C1 increases) and opens it on the LP side (C2 decreases).',
   'This narrows the gap to the LP side plate (C1 increases) and widens the gap to the HP side plate (C2 decreases).')],
 'lighting-design-calculation': [
  ('For a 20 × 10 room at 2.5 m mounting height: RI = 200 / 75 = 2.67.',
   'For a 20 × 10 room with a 3.0 m ceiling and a 0.8 m working plane, Hm = 3.0 minus 0.8 = 2.2 m: RI = 200 / 66 = 3.03.'),
  ('Typical UF for RI 2.67, medium reflectance', 'Typical UF for RI 3.03, medium reflectance')],
 'mass-flow-controller-working-principle': [
  ('the four main MFC types', 'the five main MFC types')],
}
for slug, pairs in FIX.items():
    pid = call('/wp/v2/posts?slug=' + slug + '&_fields=id')[0]['id']
    ops = [{'find': a, 'mode': 'replace', 'html': b} for a, b in pairs]
    try: res = call('/ib/v1/patch', json.dumps({'id': pid, 'ops': ops}).encode())
    except Exception as e: res = {'error': str(e)[:200]}
    print('FIX', slug, pid, json.dumps(res)[:300])
    raw = call(f'/wp/v2/posts/{pid}?context=edit&_fields=content')['content']['raw']
    w = ' '.join(str(x.get('content', '')) for x in call(f'/ib/v1/widgets/{pid}').get('widgets', []))
    for a, b in pairs: print('CHECK', slug, 'widget new', b in w, 'old', a in w, '| raw new', b in raw, 'old', a in raw)
