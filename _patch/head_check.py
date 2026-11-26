import json, os, base64, urllib.request, re
AUTH='Basic '+base64.b64encode(f"{os.environ['U']}:{os.environ['P']}".encode()).decode()
rq=urllib.request.Request('https://www.instrumentationblog.in/wp-json/wp/v2/pages/1283', data=json.dumps({'status':'draft'}).encode(), method='POST', headers={'Authorization':AUTH,'User-Agent':'ib-patch/1.0','Content-Type':'application/json'})
d=json.loads(urllib.request.urlopen(rq,timeout=60).read()); print('PAGE', d['id'], d['slug'], d['status'])
class NR(urllib.request.HTTPRedirectHandler):
    def redirect_request(self,*a,**k): return None
op=urllib.request.build_opener(NR)
try: op.open(urllib.request.Request('https://www.instrumentationblog.in/home-03/',headers={'User-Agent':'Mozilla/5.0 ib-patch'}),timeout=60); print('NO REDIRECT')
except urllib.error.HTTPError as e: print('REDIRECT', e.code, e.headers.get('location'))
