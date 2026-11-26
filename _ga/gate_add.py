"""Gate GA4 and Clarity on a first-party file (/assets/ib-ok.js).
Bots whose asset requests are blocked by Cloudflare never load ib-ok.js, so they are not counted.
Usage: python3 _ga/gate_add.py <dir>   (writes changed.txt with the changed files)"""
import os, sys
GA_OLD = '<script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}(function(){var z="";try{z=Intl.DateTimeFormat().resolvedOptions().timeZone||""}catch(e){}if(z==="Asia/Singapore"||navigator.webdriver)return;gtag("js",new Date());gtag("config","G-R3NLR1WRYC",{traffic_type:"ib_verified"});var s=document.createElement("script");s.async=true;s.src="https://www.googletagmanager.com/gtag/js?id=G-R3NLR1WRYC";document.head.appendChild(s)})();</script>'
GA_NEW = '<script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}(function(){var z="";try{z=Intl.DateTimeFormat().resolvedOptions().timeZone||""}catch(e){}if(z==="Asia/Singapore"||navigator.webdriver)return;(window.__ibQ=window.__ibQ||[]).push(function(){gtag("js",new Date());gtag("config","G-R3NLR1WRYC",{traffic_type:"ib_verified"});var s=document.createElement("script");s.async=true;s.src="https://www.googletagmanager.com/gtag/js?id=G-R3NLR1WRYC";document.head.appendChild(s)})})();</script>'
CL_OLD = '<script>(function(){var z="";try{z=Intl.DateTimeFormat().resolvedOptions().timeZone||""}catch(e){}if(z==="Asia/Singapore"||navigator.webdriver)return;(function(c,l,a,r,i,t,y){c[a]=c[a]||function(){(c[a].q=c[a].q||[]).push(arguments)};t=l.createElement(r);t.async=1;t.src="https://www.clarity.ms/tag/"+i+"?ref=bwt";y=l.getElementsByTagName(r)[0];y.parentNode.insertBefore(t,y);})(window,document,"clarity","script","u4fdvm7fxj");})();</script>'
CL_NEW = '<script>(function(){var z="";try{z=Intl.DateTimeFormat().resolvedOptions().timeZone||""}catch(e){}if(z==="Asia/Singapore"||navigator.webdriver)return;(window.__ibQ=window.__ibQ||[]).push(function(){(function(c,l,a,r,i,t,y){c[a]=c[a]||function(){(c[a].q=c[a].q||[]).push(arguments)};t=l.createElement(r);t.async=1;t.src="https://www.clarity.ms/tag/"+i+"?ref=bwt";y=l.getElementsByTagName(r)[0];y.parentNode.insertBefore(t,y);})(window,document,"clarity","script","u4fdvm7fxj")})})();</script>'
OK = '<script async src="/assets/ib-ok.js"></script>'
def gate(h):
    if '__ibQ' in h: return h, 'done'
    if GA_OLD not in h: return h, 'unmatched'
    h = h.replace(GA_OLD, GA_NEW, 1)
    if CL_OLD in h: h = h.replace(CL_OLD, CL_NEW + OK, 1)
    else: h = h.replace(GA_NEW, GA_NEW + OK, 1)
    return h, 'changed'
if __name__ == '__main__':
    root = sys.argv[1]; st = {'changed': 0, 'done': 0, 'unmatched': 0}; ch = []
    for dp, _, fs in os.walk(root):
        for f in fs:
            if not f.endswith('.html'): continue
            p = os.path.join(dp, f); h = open(p, encoding='utf-8').read(); n, s = gate(h); st[s] += 1
            if s == 'unmatched': print('UNMATCHED', p)
            if s == 'changed': open(p, 'w', encoding='utf-8').write(n); ch.append(p)
    open('changed.txt', 'w').write('\n'.join(ch) + ('\n' if ch else ''))
    print('STATS', st)
