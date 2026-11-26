import re, json, os, base64, urllib.request
AUTH='Basic '+base64.b64encode(f"{os.environ['U']}:{os.environ['P']}".encode()).decode()
def api(p):
    rq=urllib.request.Request('https://www.instrumentationblog.in/wp-json'+p, headers={'Authorization':AUTH,'User-Agent':'ib-patch/1.0'})
    return json.loads(urllib.request.urlopen(rq,timeout=60).read())
s=api('/wp/v2/settings'); print('show_on_front', s.get('show_on_front'), 'page_on_front', s.get('page_on_front'), 'page_for_posts', s.get('page_for_posts'))
for pg in api('/wp/v2/pages?slug=home-03&context=edit&status=any&_fields=id,status,date,modified,link,template,parent'): print('home-03 page', pg)
for pg in api('/wp/v2/pages?per_page=100&_fields=id,slug,status&context=edit&status=any'):
    if 'home' in pg['slug'] or pg['id']==s.get('page_on_front'): print('page', pg)
for u in ['https://www.instrumentationblog.in/home-03/','https://www.instrumentationblog.in/']:
    try:
        rq=urllib.request.Request(u, headers={'User-Agent':'Mozilla/5.0 ib-patch'})
        r=urllib.request.urlopen(rq,timeout=60); h=r.read().decode('utf8','ignore')
        print(u,'final',r.geturl(),'robots',re.findall(r'<meta name="robots" content="([^"]+)"',h),'canonical',re.findall(r'<link rel="canonical" href="([^"]+)"',h),'title',re.findall(r'<title>([^<]+)',h)[:1])
    except Exception as e: print(u,'ERR',getattr(e,'code',e))
try:
    sm=urllib.request.urlopen(urllib.request.Request('https://www.instrumentationblog.in/page-sitemap.xml',headers={'User-Agent':'Mozilla/5.0 ib-patch'}),timeout=60).read().decode()
    print('in page-sitemap:', 'home-03' in sm)
except Exception as e: print('sitemap ERR', getattr(e,'code',e))
