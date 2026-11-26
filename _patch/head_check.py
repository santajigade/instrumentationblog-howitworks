import re, urllib.request
for s in ['scr-triggering-methods-gate-triggering','instrument-junction-box-design','vibration-analysis-questions-and-answers']:
    try:
        rq=urllib.request.Request(f'https://www.instrumentationblog.in/{s}/', headers={'User-Agent':'Mozilla/5.0 ib-patch'})
        h=urllib.request.urlopen(rq,timeout=60).read().decode('utf8','ignore')
        rob=re.findall(r'<meta name="robots" content="([^"]+)"',h); ogw=re.findall(r'og:image:width" content="(\d+)"',h)
        auth=re.findall(r'"author":\{[^}]{0,200}',h)[:1]; ld='"@type":"Person"' in h
        print(s, '| robots:', rob, '| og:image:width', ogw, '| Person schema', ld, '| byline', bool(re.search(r'class="[^"]*(author|byline)',h)))
    except Exception as e: print(s,'ERR',getattr(e,'code',e))
