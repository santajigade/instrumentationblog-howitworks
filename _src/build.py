import re, json, html, os, shutil
from content import PAGES as BASE_PAGES, GROUPS as BASE_GROUPS
from content_extra import EXTRA
from scenes import COMMON, S, K_TABLE
import importlib.util, pathlib as _pl

# Pages: the first 12 live in content.py / scenes.py; every new topic is one file in _src/pages/<slug>.py
# defining PAGE (same keys as content.py plus intro/uses/tips) and SCENE (canvas JS: upd, step, draw).
PAGES = []
for _p in BASE_PAGES:
    PAGES.append({**_p, **EXTRA.get(_p["slug"], {})})
for _f in sorted((_pl.Path(__file__).resolve().parent / "pages").glob("*.py")):
    _spec = importlib.util.spec_from_file_location(_f.stem.replace("-", "_"), _f)
    _m = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(_m)
    assert _m.PAGE["slug"] == _f.stem, _f
    PAGES.append(_m.PAGE); S[_m.PAGE["slug"]] = _m.SCENE
ORDER = ["Flow", "Level", "Pressure", "Temperature", "Control Valve", "Switches", "Analytical", "Signals", "PLC", "DCS", "SCADA", "Safety", "Electrical"]
GROUPS = [g for g in ORDER if any(p["grp"] == g for p in PAGES)] + sorted({p["grp"] for p in PAGES} - set(ORDER))

import pathlib
HERE = pathlib.Path(__file__).resolve().parent
OUT = str(HERE.parent / "site" / "how-it-works")
SITE = "https://instrumentationblog.in/"
BASE = SITE + "how-it-works/"
TODAY = "2026-11-15"
E = html.escape
PAL = ["--l:#eaf2fe;--d:#1e63b8;--b:#c9dcf8", "--l:#e8f7ef;--d:#1d7a46;--b:#c3e8d2", "--l:#fff4e0;--d:#a8620a;--b:#f5ddb0",
       "--l:#f3edfc;--d:#6b3fb0;--b:#ddd0f3", "--l:#e4f6f7;--d:#0f7b80;--b:#bfe6e8", "--l:#fdecf1;--d:#b02a52;--b:#f5ccd8"]
GP = {g: PAL[i % len(PAL)] for i, g in enumerate(GROUPS)}
GC = {"Flow": ("#1e63b8", "#0f2a52"), "Level": ("#1d7a46", "#0b3320"), "Pressure": ("#a8620a", "#4a2a04"),
      "Temperature": ("#b02a52", "#4a0f1f"), "Control Valve": ("#6b3fb0", "#2a1450"), "Switches": ("#0f7b80", "#06393b"),
      "Analytical": ("#5a7d12", "#263607"), "Signals": ("#3b4bb0", "#171f4f"), "PLC": ("#c2410c", "#4a1a05"),
      "DCS": ("#0e7490", "#063241"), "SCADA": ("#7c3aed", "#2e1065"), "Safety": ("#b91c1c", "#450a0a"), "Electrical": ("#a16207", "#422006")}
AD = '<div class="ibuc-ad"><div class="ibuc-adl">Advertisement</div><ins class="adsbygoogle" style="display:block" data-ad-client="ca-pub-3931314195561246" data-ad-slot="5950781970" data-ad-format="auto" data-full-width-responsive="true"></ins><script>(adsbygoogle = window.adsbygoogle || []).push({});</script></div>'

tpl = open(HERE / "template_page.html", encoding="utf-8").read()
HEAD = tpl[:tpl.find('<div class="ibuc" id="ibuc-app"')]
FOOT = tpl[tpl.find("</main>"):]
CSS = """<style>
.ibuc .hw-stage{max-width:780px;margin:0 auto;background:#fff;border:1px solid var(--b);border-radius:14px;overflow:hidden}
.ibuc .hw-stage canvas{display:block;width:100%}
.ibuc .hw-bar{display:flex;justify-content:space-between;align-items:center;gap:10px;flex-wrap:wrap;margin:12px auto 0;max-width:780px}
.ibuc button.hw-pp{background:var(--n) !important;color:#fff !important;border:0 !important;border-radius:999px !important;padding:8px 16px !important;font-size:14px;font-weight:700;cursor:pointer;line-height:1.2}
.ibuc .hw-note{font-size:13px;color:var(--m)}
.ibuc .hw-ctl{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:14px 22px;margin:18px 0 0}
.ibuc .hw-s label{display:flex;justify-content:space-between;font-size:14px;font-weight:700;color:var(--n);margin:0 0 6px}
.ibuc .hw-s label b{color:var(--gc);font-variant-numeric:tabular-nums}
.ibuc .hw-s input[type=range]{width:100%;accent-color:var(--gc);height:28px;margin:0}
.ibuc .hw-leg{list-style:none;padding:0;margin:16px 0 0;display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:8px 18px}
.ibuc .hw-leg li{display:flex;gap:10px;align-items:flex-start;font-size:14.5px}
.ibuc .hw-leg i{flex:0 0 24px;height:24px;border-radius:50%;background:#d9622b;color:#fff;font-style:normal;font-weight:700;font-size:13px;display:flex;align-items:center;justify-content:center}
.ibuc ol.hw-steps{list-style:none;counter-reset:s;padding:0;margin:0}
.ibuc ol.hw-steps li{counter-increment:s;position:relative;padding:0 0 14px 46px;margin:0}
.ibuc ol.hw-steps li:before{content:counter(s);position:absolute;left:0;top:-2px;width:32px;height:32px;border-radius:50%;background:var(--gc);color:#fff;font-weight:700;display:flex;align-items:center;justify-content:center}
.ibuc .hw-fig{margin:0;text-align:center}
.ibuc .hw-fig img{width:100%;max-width:780px;height:auto;border:1px solid var(--b);border-radius:12px}
.ibuc .hw-fig figcaption{font-size:14px;color:var(--m);margin:10px auto 0;max-width:780px;text-align:left}
.ibuc button.hw-dl{background:#fff !important;color:var(--n) !important;border:1.5px solid var(--n) !important}
.ibuc .hw-uses{display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:12px}
.ibuc .hw-use{background:var(--l);border:1px solid var(--b);border-left:4px solid var(--gc);border-radius:10px;padding:12px 14px}
.ibuc .hw-use b{display:block;color:var(--n);margin:0 0 4px}
.ibuc .hw-use span{font-size:14.5px;color:#334155}
.ibuc ul.hw-tips{list-style:none;padding:0;margin:0}
.ibuc ul.hw-tips li{position:relative;padding:0 0 10px 30px}
.ibuc ul.hw-tips li:before{content:"✓";position:absolute;left:0;top:0;width:20px;height:20px;border-radius:50%;background:var(--gc);color:#fff;font-size:12px;font-weight:700;display:flex;align-items:center;justify-content:center}
.ibuc .hw-f{background:#1a2333;color:#e6edf7;border-radius:12px;padding:16px 18px;font-family:'Courier New',monospace;font-size:15.5px;line-height:1.75;overflow-x:auto}
.ibuc .hw-f b{color:#fbbf24;font-weight:700}
</style>"""
STYLE_HUB = ""


IMG_W, IMG_H = 1560, 988


def img_name(slug):
    return f"{slug}-working-diagram.webp"


def head(title, desc, url, img=None, alt=""):
    h = HEAD
    if img:
        h = h.replace('<meta name="twitter:card" content="summary">',
                      f'<meta property="og:image" content="{img}">\n<meta property="og:image:width" content="{IMG_W}">\n<meta property="og:image:height" content="{IMG_H}">\n<meta property="og:image:alt" content="{E(alt)}">\n<meta name="twitter:card" content="summary_large_image">\n<meta name="twitter:image" content="{img}">', 1)
    h = re.sub(r"<title>.*?</title>", "<title>" + E(title, False) + "</title>", h, 1)
    for pat, val in [(r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{E(desc)}">'),
                     (r'<link rel="canonical" href="[^"]*">', f'<link rel="canonical" href="{url}">'),
                     (r'<meta property="og:title" content="[^"]*">', f'<meta property="og:title" content="{E(title)}">'),
                     (r'<meta property="og:description" content="[^"]*">', f'<meta property="og:description" content="{E(desc)}">'),
                     (r'<meta property="og:url" content="[^"]*">', f'<meta property="og:url" content="{url}">')]:
        h, n = re.subn(pat, val, h, 1)
        assert n == 1, pat
    return h.replace('<main class="ibs-main">', '<main class="ibs-main">' + CSS, 1)


def card(url, tag, title, sub, pal):
    return f'<a class="ibx-card" style="{pal}" href="{url}"><span class="ibx-t">{E(tag)}</span><span class="ibx-h">{E(title)}</span><span class="ibx-s">{E(sub)}</span></a>'


def page(p, others):
    url = BASE + p["slug"] + "/"
    c1, c2 = GC[p["grp"]]
    grad = f"linear-gradient(135deg,{c1} 0%,{c2} 100%)"
    sl = "".join(f'<div class="hw-s"><label for="hw-{k}">{E(lab)} <b id="hw-{k}-v"></b></label><input type="range" id="hw-{k}" data-k="{k}" min="{lo}" max="{hi}" step="{st}" value="{dv}" data-d="{dec}" data-u="{E(u)}"></div>'
                 for k, lab, lo, hi, dv, st, dec, u in p["sliders"])
    outs = "".join(f'<div class="ibuc-o{" main" if i == 1 else ""}"><span>{E(lbl)}</span><b id="hw-o-{k}">…</b></div>' for i, (k, lbl) in enumerate(p["outs"]))
    leg = "".join(f"<li><i>{i+1}</i><span>{E(x)}</span></li>" for i, x in enumerate(p["legend"]))
    steps = "".join(f"<li>{E(x)}</li>" for x in p["steps"])
    form = "<br>".join(("<b>" + E(x) + "</b>") if i == 0 else E(x) for i, x in enumerate(p["formula"]))
    parts = "".join(f'<tr><td>{E(a)}</td><td data-l="What it does">{E(b)}</td></tr>' for a, b in p["parts"])
    rel = []
    for path, t in p["cal"]:
        rel.append(card(SITE + "calculators/" + path + "/", "Calculator", t, "Free online calculator with formula and worked example.", PAL[1]))
    for path, t in p.get("tool", []):
        rel.append(card(SITE + path + "/", "Tool", t, "Step by step interactive troubleshooting.", PAL[4]))
    for s_, t in p["glo"]:
        rel.append(card(SITE + "glossary/" + s_ + "/", "Glossary", t, "Definition, formula and example.", PAL[2]))
    for s_, t in p["cmp"]:
        rel.append(card(SITE + "compare/" + s_ + "/", "Compare", t, "Side by side comparison table.", PAL[3]))
    if p.get("dl"):
        rel.append(card(SITE + p["dl"][0] + "/", "Download", p["dl"][1], "Free reference table.", PAL[5]))
    faq = "".join(f"<details{' open' if i == 0 else ''}><summary>{E(q)}</summary><p>{E(a)}</p></details>" for i, (q, a) in enumerate(p["faq"]))
    more = "".join(card(BASE + o["slug"] + "/", o["grp"], o["h1"],
                        o["quick"].split(". ")[0][:96].rstrip(",") + "…", GP[o["grp"]]) for o in others)
    nm = p["name"]
    art = "an" if nm[0] in "AEIOU" else "a"
    subj = nm if nm.startswith("DP") else f"{art} {nm}"
    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE},
            {"@type": "ListItem", "position": 2, "name": "How It Works", "item": BASE},
            {"@type": "ListItem", "position": 3, "name": p["h1"], "item": url}]},
        {"@type": "ImageObject", "contentUrl": url + img_name(p["slug"]), "name": p["h1"], "caption": "Labelled diagram showing " + p["kw"].lower(), "width": IMG_W, "height": IMG_H},
        {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in p["faq"]]}]}
    intro = "".join(f"<p>{E(x)}</p>" for x in p.get("intro", []))
    uses = "".join(f'<div class="hw-use"><b>{E(a)}</b><span>{E(b)}</span></div>' for a, b in p.get("uses", []))
    tips = "".join(f"<li>{E(x)}</li>" for x in p.get("tips", []))
    q = "What Is " + subj + "?"
    alt = "Labelled diagram showing " + p["kw"].lower()
    cap = "Numbered parts: " + "; ".join(f"{i+1} {x.lower()}" for i, x in enumerate(p["legend"])) + "."
    js = COMMON.replace("@@SCENE@@", S[p["slug"]].replace("@@K@@", K_TABLE))
    body = f"""<div class="ibuc" id="ibuc-app" style="--gc:{c1}">
<nav class="ibuc-crumb" aria-label="Breadcrumb"><a href="{SITE}">Home</a> › <a href="{BASE}">How It Works</a> › {E(nm)}</nav>
<header class="ibuc-hero" style="background:{grad}">
  <div class="ibuc-eye">{E(p['grp'])} · How It Works</div>
  <h1>{E(p['h1'])}</h1>
  <p>{E(p['hero'])}</p>
  <div class="ibuc-pills"><span class="ibuc-pill">Live animation</span><span class="ibuc-pill">Adjustable sliders</span><span class="ibuc-pill">Formula and example</span></div>
</header>
<p class="cmp-verdict"><b>Quick answer:</b> {E(p['quick'])}</p>
{f'<section class="ibuc-card"><h2>{E(q)}</h2>{intro}</section>' if intro else ''}
{AD}
<section class="ibuc-card"><h2>{E(p['h1'])}: Interactive Animation</h2>
<div class="hw-stage"><canvas id="hw-cv" role="img" aria-label="Animated diagram showing {E(p['kw'].lower())}"></canvas></div>
<div class="hw-bar"><span><button type="button" class="hw-pp" id="hw-pp">Pause animation</button> <button type="button" class="hw-pp hw-dl" id="hw-dl" data-name="{p['slug']}-working-diagram.png" data-title="{E(p['h1'])}">Download diagram</button></span><span class="hw-note">Numbered markers match the parts list below.</span></div>
<div class="hw-ctl" id="hw-ctl">{sl}</div>
<div class="ibuc-out">{outs}</div>
<ol class="hw-leg">{leg}</ol>
</section>
<section class="ibuc-card"><h2>{E(nm)} Working Principle Step by Step</h2><ol class="hw-steps">{steps}</ol></section>
<section class="ibuc-card"><h2>{E(nm)} Labelled Diagram</h2><figure class="hw-fig"><img src="{url}{img_name(p['slug'])}" alt="{E(alt)}" title="{E(p['h1'])}" width="{IMG_W}" height="{IMG_H}" loading="lazy" decoding="async"><figcaption>{E(cap)}</figcaption></figure></section>
{AD}
<section class="ibuc-card"><h2>{E(nm)} Formula</h2><div class="hw-f">{form}</div></section>
<section class="ibuc-card"><h2>Main Parts of {E(subj)}</h2><div class="cmp-wrap"><table class="cmp-t"><thead><tr><th>Part</th><th>What it does</th></tr></thead><tbody>{parts}</tbody></table></div></section>
{f'<section class="ibuc-card"><h2>Where {E(subj)} Is Used</h2><div class="hw-uses">{uses}</div></section>' if uses else ''}
<div class="cmp-two"><div class="cmp-box" style="{PAL[1]}"><h3>Advantages</h3><ul>{''.join('<li>' + E(x) + '</li>' for x in p['pros'])}</ul></div><div class="cmp-box" style="{PAL[5]}"><h3>Limitations</h3><ul>{''.join('<li>' + E(x) + '</li>' for x in p['cons'])}</ul></div></div>
{f'<section class="ibuc-card"><h2>{E(nm)} Field Tips and Common Problems</h2><ul class="hw-tips">{tips}</ul></section>' if tips else ''}
{AD}
<section class="ibuc-card"><h2>Related Calculators and Tools</h2><div class="ibx-grid">{''.join(rel)}</div></section>
<section class="ibuc-card"><h2>Frequently Asked Questions</h2>{faq}</section>
<div class="ibuc-ymal" style="background:{grad}"><div class="ibuc-eye">You May Also Like</div><h3>Learn more on the blog</h3><p class="ibuc-yt">{E(p['blog'][1])}</p><p>A practical guide on instrumentationblog.in that goes deeper into this topic with field examples.</p><a class="ibuc-go" href="{SITE}{p['blog'][0]}/">Read Full Article</a></div>
<section class="ibuc-card"><h2>More How It Works</h2><div class="ibx-grid">{more}</div></section>
<p style="text-align:center;margin:0 0 22px"><a href="{BASE}"><b>All How It Works animations</b></a> · <a href="{SITE}glossary/"><b>Instrumentation glossary</b></a> · <a href="{SITE}compare/"><b>Comparisons</b></a></p>
{AD}
</div>
<script>{js}</script>
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False, separators=(',', ':'))}</script>"""
    os.makedirs(f"{OUT}/{p['slug']}", exist_ok=True)
    open(f"{OUT}/{p['slug']}/index.html", "w", encoding="utf-8").write(head(p["title"], p["desc"], url, url + img_name(p["slug"]), "Labelled diagram showing " + p["kw"].lower()) + body + FOOT)


def hub():
    src = open(HERE / "template_hub.html", encoding="utf-8").read()
    title = "How It Works: Animated Instrumentation Diagrams"
    desc = "How It Works: 12 animated instrumentation diagrams with sliders. See how orifice plates, magmeters, radar, displacers, thermocouples and positioners work."
    h = head(title, desc, BASE, BASE + "orifice-plate/" + img_name("orifice-plate"), "Labelled diagram showing how an orifice plate works")
    b0 = src.find('<div class="ibuc" id="ibuc-app">')
    body = src[b0:src.find("</main>")]
    body = body.replace('› Compare</nav>', '› How It Works</nav>', 1)
    hero = f"""<header class="ibuc-hero" style="background:linear-gradient(135deg,#0f7b80 0%,#1a2333 100%)">
  <div class="ibuc-eye">Learn · How It Works</div>
  <h1>How It Works: Animated Instrumentation</h1>
  <p>See instruments working instead of just reading about them. Each page has a live animation with sliders, the working principle step by step, the key formula with an example, and links to calculators and articles.</p>
  <div class="ibuc-stats"><div><b>{len(PAGES)}</b><span>animations</span></div><div><b>{len(GROUPS)}</b><span>topics</span></div></div>
</header>"""
    body = re.sub(r'<header class="ibuc-hero".*?</header>', hero, body, 1, flags=re.S)
    s0 = body.find('<section class="ibuc-card"><h2>All Comparisons</h2>')
    s1 = body.find("</script></section>", s0) + len("</script></section>")
    old = body[s0:s1]
    script = re.search(r'<script>\(function\(\)\{var U=.*?</script>', old, re.S).group(0).replace('var U=["comparison","comparisons"]', 'var U=["animation","animations"]') + "</section>"
    n = len(PAGES)
    chips = f'<button type="button" class="ibx-chip on" data-t="">All<b>{n}</b></button>'
    grps = ""
    for g in GROUPS:
        items = [p for p in PAGES if p["grp"] == g]
        chips += f'<button type="button" class="ibx-chip" style="{GP[g]}" data-t="{E(g)}">{E(g)}<b>{len(items)}</b></button>'
        cards = "".join(f'<a class="ibx-card" style="{GP[g]}" href="{BASE}{p["slug"]}/" data-t="{E(g)}" data-s="{E((p["h1"] + " " + p["quick"] + " " + g).lower())}"><span class="ibx-t">{E(g)}</span><span class="ibx-h">{E(p["h1"])}</span><span class="ibx-s">{E(p["hero"].split(". ")[0][:100])}…</span></a>' for p in items)
        grps += f'<div class="ibx-grp" data-t="{E(g)}" style="{GP[g]}"><h3 class="ibx-gh">{E(g)}<small>{len(items)}</small></h3><div class="ibx-grid">{cards}</div></div>'
    new = f'<section class="ibuc-card"><h2>All Animations</h2><div class="ibx-bar"><input type="search" class="ibx-q" id="ibx-q" placeholder="Search animations" aria-label="Search"><span class="ibx-n" id="ibx-n">{n} animations</span></div><div class="ibx-chips" role="group" aria-label="Filter by topic">{chips}</div><div class="ibx-none" id="ibx-none">Nothing matches your search. Try another word or pick All.</div><div id="ibx-list">{grps}</div>\n{script}'
    f0 = body.find('<section class="ibuc-card"><h2>Frequently Asked Questions</h2>')
    assert s0 > 0 and f0 > s0
    body = body[:s0] + new + "\n" + AD + "\n" + body[f0:]
    faqs = [("What are these How It Works pages?", "Animated diagrams of common process instruments. Move the sliders to change flow, level, pressure or temperature and watch the instrument respond, with the formula and the main parts explained."),
            ("Are the numbers real?", "The formulas are standard engineering relations and the thermocouple page uses the IEC 60584 type K table. Some animations exaggerate small effects so they are easy to see; the pages say where."),
            ("Do the animations work on mobile?", "Yes. They run in any modern browser, pause when scrolled out of view, and respect the reduced motion setting.")]
    fq = "".join(f"<details{' open' if i == 0 else ''}><summary>{E(q)}</summary><p>{E(a)}</p></details>" for i, (q, a) in enumerate(faqs))
    body, k = re.subn(r'<section class="ibuc-card"><h2>Frequently Asked Questions</h2>.*?</section>', f'<section class="ibuc-card"><h2>Frequently Asked Questions</h2>{fq}</section>', body, 1, flags=re.S)
    assert k == 1
    ex = '<a class="ibx-card" style="--l:#eaf2fe;--d:#1e63b8;--b:#c9dcf8" href="https://instrumentationblog.in/glossary/">'
    assert ex in body
    body = body.replace(ex, card(SITE + "compare/", "Compare", "Instrumentation Comparisons", "Side by side comparisons of sensors, meters and valves.", PAL[4]) + ex, 1)
    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Home", "item": SITE},
                                                        {"@type": "ListItem", "position": 2, "name": "How It Works", "item": BASE}]},
        {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs]},
        {"@type": "ItemList", "name": "How It Works", "numberOfItems": n, "itemListElement": [{"@type": "ListItem", "position": i + 1, "url": BASE + p["slug"] + "/", "name": p["h1"]} for i, p in enumerate(PAGES)]}]}
    body, k = re.subn(r'<script type="application/ld\+json">.*?</script>', '<script type="application/ld+json">' + json.dumps(ld, ensure_ascii=False, separators=(",", ":")) + "</script>", body, 1, flags=re.S)
    assert k == 1
    open(f"{OUT}/index.html", "w", encoding="utf-8").write(h + body + FOOT)


def sitemap():
    u = [BASE] + [BASE + p["slug"] + "/" for p in PAGES]
    s = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(f"<url><loc>{x}</loc><lastmod>{TODAY}</lastmod></url>\n" for x in u) + "</urlset>\n"
    open(f"{OUT}/sitemap.xml", "w").write(s)


if __name__ == "__main__":
    # keep existing diagram images; only HTML and sitemap are regenerated
    os.makedirs(OUT, exist_ok=True)
    for old in pathlib.Path(OUT).glob("**/index.html"):
        old.unlink()
    for p in PAGES:
        same = [o for o in PAGES if o is not p and o["grp"] == p["grp"]]
        rest = [o for o in PAGES if o is not p and o["grp"] != p["grp"]]
        page(p, (same + rest)[:8])
    hub()
    sitemap()
    print("built", len(PAGES))
