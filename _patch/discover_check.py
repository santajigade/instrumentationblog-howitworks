import json, os, re, base64, urllib.request, urllib.parse
B='https://www.instrumentationblog.in/wp-json'
AUTH='Basic '+base64.b64encode(f"{os.environ['U']}:{os.environ['P']}".encode()).decode()
def get(p, raw=False):
    rq=urllib.request.Request(B+p, headers={'Authorization':AUTH,'User-Agent':'ib-patch/1.0'})
    with urllib.request.urlopen(rq, timeout=120) as r: d=r.read(); return d if raw else json.loads(d)
top=['plc-and-automation-questions-and-answers','free-training-electrical-control-drawings','instrument-junction-box-design','diaphragm-pressure-gauge-working','non-inverting-amplifier-gain','artificial-intelligence-machine-learning','gas-pressure-switch-burner']
rec=[p['slug'] for p in get('/wp/v2/posts?per_page=15&_fields=slug')]
def chk(s):
    p=get(f'/wp/v2/posts?slug={s}&context=edit&_fields=id,date,meta,featured_media,author,content')
    if not p: return f'{s}: NOTFOUND'
    p=p[0]; w=h=0; fm=''
    if p['featured_media']:
        m=get(f"/wp/v2/media/{p['featured_media']}?_fields=media_details,source_url")
        w=m['media_details'].get('width',0); h=m['media_details'].get('height',0); fm=m['source_url'].split('/')[-1]
    meta=p.get('meta',{}) or {}
    rob=meta.get('rank_math_robots') or ''
    adv=meta.get('rank_math_advanced_robots') or ''
    head=''
    try:
        hd=get('/rankmath/v1/getHead?url='+urllib.parse.quote(f'https://www.instrumentationblog.in/{s}/'))
        head=hd.get('head','') if isinstance(hd,dict) else ''
    except Exception as e: head='ERR'+str(getattr(e,'code',''))
    mr=re.search(r'name="robots" content="([^"]+)"',head)
    imgs=re.findall(r'<img[^>]+width="(\d+)"',p['content']['raw'])
    return f"{s[:48]:48} {p['date'][:10]} feat={w}x{h} {fm[-35:]} robots={(mr.group(1) if mr else head[:20])} metaRobots={rob} adv={adv} maxBodyImgW={max(map(int,imgs)) if imgs else 0}"
print('TOP DISCOVER')
for s in top: print(chk(s))
print('RECENT')
for s in rec: print(chk(s))
