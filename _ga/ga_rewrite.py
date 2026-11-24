# Replace the plain GA4 snippet in static pages with the filtered, tagged one.
# Real visitors get traffic_type=ib_verified; a GA4 "include only" data filter then drops
# fake hits sent straight to Google, which never carry it.
# Usage: python3 _ga/ga_rewrite.py <folder>   -> writes changed.txt, prints counts.
import sys, os, glob, re

GA = "G-R3NLR1WRYC"
NEW = ('<script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}'
       '(function(){var z="";try{z=Intl.DateTimeFormat().resolvedOptions().timeZone||""}catch(e){}'
       'if(z==="Asia/Singapore"||navigator.webdriver)return;'
       'gtag("js",new Date());gtag("config","' + GA + '",{traffic_type:"ib_verified"});'
       'var s=document.createElement("script");s.async=true;'
       's.src="https://www.googletagmanager.com/gtag/js?id=' + GA + '";document.head.appendChild(s)})();</script>')

# Old snippet: loader tag + inline config, quotes and spacing may vary.
OLD = re.compile(
    r'<script\s+async\s+src=["\']https://www\.googletagmanager\.com/gtag/js\?id=' + GA + r'["\']\s*>\s*</script>\s*'
    r'<script>\s*window\.dataLayer\s*=\s*window\.dataLayer\s*\|\|\s*\[\];\s*'
    r'function\s+gtag\(\)\s*\{\s*dataLayer\.push\(arguments\);?\s*\}\s*'
    r'gtag\(\s*["\']js["\']\s*,\s*new Date\(\)\s*\);?\s*'
    r'gtag\(\s*["\']config["\']\s*,\s*["\']' + GA + r'["\']\s*\);?\s*</script>')


def rewrite(s):
    if "ib_verified" in s:
        return s, "done"
    t, n = OLD.subn(NEW, s, count=1)
    if n:
        return t, "changed"
    return s, ("unmatched" if GA in s else "nogA")


if __name__ == "__main__":
    root = sys.argv[1]
    changed, unmatched, stats = [], [], {"changed": 0, "done": 0, "unmatched": 0, "nogA": 0}
    for f in glob.glob(root + "/**/*.html", recursive=True):
        s = open(f, encoding="utf-8", errors="surrogateescape").read()
        t, st = rewrite(s)
        stats[st] += 1
        if st == "changed":
            open(f, "w", encoding="utf-8", errors="surrogateescape").write(t)
            changed.append(f)
        elif st == "unmatched":
            unmatched.append(f)
    open("changed.txt", "w").write("\n".join(changed))
    print("STATS", stats)
    for f in unmatched[:20]:
        print("UNMATCHED", f)
