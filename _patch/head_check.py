import re, urllib.request
h=urllib.request.urlopen(urllib.request.Request('https://www.instrumentationblog.in/pressure-to-head-conversion/?nocache=1',headers={'User-Agent':'Mozilla/5.0 ib-patch'}),timeout=60).read().decode('utf8','ignore')
i=h.find("Asia/Singapore"); s=h.rfind('<script',0,i); e=h.find('</script>',i)+9
print('BEGIN'); print(h[s:e]); print('END')
print('COUNT_GA_CONFIG', h.count("G-R3NLR1WRYC"), 'clarity', h.count('u4fdvm7fxj'), 'adsense', h.count('ca-pub-3931314195561246'))
