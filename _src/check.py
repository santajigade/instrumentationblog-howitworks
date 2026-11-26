"""Quality gate for site/how-it-works. Run after build.py, snap.js and webp.py.
Exit code 0 = OK to publish. Usage: python3 _src/check.py"""
import re, glob, html, json, os, sys, subprocess, pathlib
from html.parser import HTMLParser

ROOT = pathlib.Path(__file__).resolve().parent.parent
SITE = ROOT / "site" / "how-it-works"
SRC = ROOT / "_src"
sys.path.insert(0, str(SRC))
VALID = set(l.strip() for l in open(SRC / "valid_links.txt") if l.strip())
VALID |= set(l.strip() + "/" for l in open(SRC / "blog_slugs.txt") if l.strip())
VALID |= {"", "calculators/", "tools/", "glossary/", "compare/", "downloads/", "unit-converters/", "how-it-works/", "favicon.ico"}


class V(HTMLParser):
    def __init__(s):
        super().__init__(); s.t = []; s.k = 0
    def handle_starttag(s, t, a):
        if t in ("script", "style", "head"): s.k += 1
        for k, v in a:
            if k in ("placeholder", "aria-label", "alt", "title") and v: s.t.append(v)
    def handle_endtag(s, t):
        if t in ("script", "style", "head"): s.k -= 1
    def handle_data(s, d):
        if not s.k: s.t.append(d)


def main():
    import build
    errs = []
    kws = {}
    for p in build.PAGES:
        e = []
        for k in ("slug", "grp", "name", "kw", "title", "desc", "h1", "hero", "quick", "sliders", "outs", "legend", "steps", "formula", "parts", "pros", "cons", "faq", "cal", "glo", "cmp", "blog"):
            if k not in p: e.append("missing field " + k)
        if len(p.get("intro", [])) < 3: e.append("intro needs 3 paragraphs")
        if len(p.get("uses", [])) < 4: e.append("uses needs 4 items")
        if len(p.get("tips", [])) < 4: e.append("tips needs 4 items")
        if len(p.get("faq", [])) < 4: e.append("faq needs 4")
        if len(p.get("legend", [])) < 3: e.append("legend needs 3")
        if p["slug"] not in build.S: e.append("no SCENE")
        if len(p["slug"]) > 60: e.append("slug > 60")
        kl = p["kw"].lower()
        if kl in kws: e.append("duplicate keyword with " + kws[kl])
        kws[kl] = p["slug"]
        if p["blog"][0] + "/" not in VALID: e.append("blog slug not live: " + p["blog"][0])
        if e: errs.append((p["slug"], e))

    kws_by_slug = {v: k for k, v in kws.items()}
    for fp in sorted(SITE.glob("**/index.html")):
        s = fp.read_text(encoding="utf-8"); e = []
        rel = str(fp.parent.relative_to(SITE))
        t = html.unescape(re.search("<title>(.*?)</title>", s).group(1))
        d = html.unescape(re.search(r'<meta name="description" content="([^"]*)"', s).group(1))
        if len(t) > 65: e.append(f"title {len(t)} > 65")
        if not 120 <= len(d) <= 160: e.append(f"description {len(d)} not 120..160")
        if "-" in t + d: e.append("hyphen in title/description")
        if rel != ".":
            kw = kws_by_slug.get(rel)
            if kw and (kw not in t.lower() or kw not in d.lower()): e.append("keyword missing in title or description: " + kw)
            img = SITE / rel / f"{rel}-working-diagram.webp"
            if not img.exists(): e.append("diagram image missing (run snap.js + webp.py)")
        if len(re.findall(r'data-ad-slot="(7215194230|6552849252|7839764783|5046401284)"', s)) < 3 or "ca-pub-3931314195561246" not in s: e.append("AdSense")
        if "G-R3NLR1WRYC" not in s: e.append("GA4")
        if "/assets/ib-ok.js" not in s or "__ibQ" not in s: e.append("GA4 gate (ib-ok.js)")
        v = V(); v.feed(s); vis = " ".join(v.t)
        hy = re.findall(r".{0,18}[-‐-―].{0,18}", vis)
        if hy: e.append("dash in visible text: " + " | ".join(hy[:3]))
        for u in set(re.findall(r'href="https://(?:www\.)?instrumentationblog\.in/([^"#?]*)"', s)):
            if u.startswith("how-it-works/"):
                if not (SITE / u[len("how-it-works/"):] / "index.html").exists() and u != "how-it-works/": e.append("broken " + u)
            elif u not in VALID: e.append("unknown link " + u)
        if s.count("<div") != s.count("</div>"): e.append("div balance")
        if e: errs.append((rel, e))

    # runtime: every canvas animates, no JS errors
    r = subprocess.run(["node", str(SRC / "runtime.js")], capture_output=True, text=True)
    if r.returncode != 0: errs.append(("runtime", [r.stdout[-1500:] + r.stderr[-1500:]]))

    if errs:
        for s_, e in errs: print("FAIL", s_, e)
        sys.exit(1)
    print("OK", len(build.PAGES), "pages")


if __name__ == "__main__":
    main()
