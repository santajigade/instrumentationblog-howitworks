# Add Microsoft Clarity right after the tagged GA4 snippet in static pages (same Singapore/bot skip).
# Usage: python3 _ga/clarity_add.py <folder>   -> writes changed.txt, prints counts.
import sys, glob

CID = "u4fdvm7fxj"
CLARITY = ('<script>(function(){var z="";try{z=Intl.DateTimeFormat().resolvedOptions().timeZone||""}catch(e){}'
           'if(z==="Asia/Singapore"||navigator.webdriver)return;'
           '(function(c,l,a,r,i,t,y){c[a]=c[a]||function(){(c[a].q=c[a].q||[]).push(arguments)};'
           't=l.createElement(r);t.async=1;t.src="https://www.clarity.ms/tag/"+i+"?ref=bwt";'
           'y=l.getElementsByTagName(r)[0];y.parentNode.insertBefore(t,y);})(window,document,"clarity","script","' + CID + '");})();</script>')
ANCHOR = 'document.head.appendChild(s)})();</script>'   # end of the tagged GA4 snippet


def add(s):
    if CID in s:
        return s, "done"
    i = s.find(ANCHOR)
    if i < 0 or "ib_verified" not in s:
        return s, "unmatched"
    j = i + len(ANCHOR)
    return s[:j] + CLARITY + s[j:], "changed"


if __name__ == "__main__":
    root = sys.argv[1]
    changed, unmatched, stats = [], [], {"changed": 0, "done": 0, "unmatched": 0}
    for f in glob.glob(root + "/**/*.html", recursive=True):
        s = open(f, encoding="utf-8", errors="surrogateescape").read()
        t, st = add(s)
        stats[st] += 1
        if st == "changed":
            open(f, "w", encoding="utf-8", errors="surrogateescape").write(t); changed.append(f)
        elif st == "unmatched":
            unmatched.append(f)
    open("changed.txt", "w").write("\n".join(changed) + ("\n" if changed else ""))
    print("STATS", stats)
    for f in unmatched[:20]:
        print("UNMATCHED", f)
