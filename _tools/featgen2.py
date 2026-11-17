#!/usr/bin/env python3
"""Poster style featured images (v2) for instrumentationblog.in.
featgen2.py out.webp "Title" "Ribbon" "chip1,chip2,chip3" topic template(0-5)
"""
import sys, os, html as H
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from featgen import ill
from playwright.sync_api import sync_playwright
from PIL import Image

F = "/home/claude/fonts/node_modules/@fontsource"
FONTS = f"""
@font-face{{font-family:Anton;src:url(file://{F}/anton/files/anton-latin-400-normal.woff2)}}
@font-face{{font-family:Archivo;src:url(file://{F}/archivo-black/files/archivo-black-latin-400-normal.woff2)}}
@font-face{{font-family:Playfair;font-weight:700;src:url(file://{F}/playfair-display/files/playfair-display-latin-700-normal.woff2)}}
@font-face{{font-family:Playfair;font-weight:900;src:url(file://{F}/playfair-display/files/playfair-display-latin-900-normal.woff2)}}
@font-face{{font-family:Bebas;src:url(file://{F}/bebas-neue/files/bebas-neue-latin-400-normal.woff2)}}
@font-face{{font-family:Pop;font-weight:500;src:url(file://{F}/poppins/files/poppins-latin-500-normal.woff2)}}
@font-face{{font-family:Pop;font-weight:700;src:url(file://{F}/poppins/files/poppins-latin-700-normal.woff2)}}
@font-face{{font-family:Pop;font-weight:800;src:url(file://{F}/poppins/files/poppins-latin-800-normal.woff2)}}
*{{margin:0;padding:0;box-sizing:border-box}}body{{width:1200px;height:675px;overflow:hidden}}
.w{{position:relative;width:1200px;height:675px;overflow:hidden}}.a{{position:absolute}}
.logo{{display:flex;align-items:center;gap:10px;font:700 24px Pop}}.logo b{{border-radius:8px;padding:0 12px;font:800 28px Pop}}
.chips{{display:flex;gap:12px;flex-wrap:wrap}}.chips div{{border-radius:40px;padding:10px 24px;font:700 24px Pop}}
"""

def fit(title, base, maxch):
    n = len(title)
    return base if n <= maxch else int(base * (maxch / n) ** 0.5)

P = dict(  # palettes used by ill(): d,m,a,a2,t,h,p,r
    yellow=dict(d="#151515", m="#2a2a2a", a="#f5b700", a2="#38bdf8", t="#111", h="#111", p="#fff", r="#1b1b1b"),
    peach=dict(d="#1f2a44", m="#2d3d63", a="#ff7a3d", a2="#5aa9e6", t="#1f2a44", h="#ff7a3d", p="#fff", r="#1f2a44"),
    noir=dict(d="#0c0c0c", m="#1c1c1c", a="#e8e8e8", a2="#9aa4b2", t="#fff", h="#fff", p="#fff", r="#222"),
    green=dict(d="#14532d", m="#1f7a4a", a="#f2c14e", a2="#ffffff", t="#fff", h="#fff", p="#fff", r="#0f3d22"),
    tech=dict(d="#081a4a", m="#0f3aa8", a="#22d3ee", a2="#60a5fa", t="#fff", h="#22d3ee", p="#fff", r="#0b2a7a"),
    sepia=dict(d="#3b2f23", m="#5a4633", a="#a0522d", a2="#6b5b45", t="#2b2118", h="#8b3a1a", p="#fff", r="#3b2f23"),
)

def logo(fg, bg, bfg, pos="right:36px;top:30px"):
    return f'<div class="a logo" style="{pos};color:{fg}"><b style="background:{bg};color:{bfg}">ib</b>instrumentationblog.in</div>'

def page(title, ribbon, chips, topic, t):
    T = H.escape(title); R = H.escape(ribbon)
    if t == 0:  # Yellow poster with hazard stripes, framed illustration card
        p = P["yellow"]; svg = ill(topic, p)
        body = f"""<div class="a" style="inset:0;background:#f5b700"></div>
<div class="a" style="inset:0;background:radial-gradient(circle at 20% 30%,rgba(255,255,255,.35),transparent 50%)"></div>
<div class="a" style="left:0;top:0;width:260px;height:44px;background:repeating-linear-gradient(-45deg,#111 0 22px,#f5b700 22px 44px)"></div>
<div class="a" style="right:0;bottom:0;width:420px;height:44px;background:repeating-linear-gradient(-45deg,#111 0 22px,#f5b700 22px 44px)"></div>
<div class="a" style="right:50px;top:70px;width:470px;height:500px;background:#1b1b1b;border-radius:18px;transform:rotate(3deg);box-shadow:0 30px 60px rgba(0,0,0,.35);overflow:hidden">
 <div class="a" style="left:-45px;top:-30px;transform:scale(1.0) rotate(-3deg)">{svg}</div></div>
<div class="a" style="left:60px;top:90px;width:600px;font:{fit(title,96,18)}px/1.02 Anton;color:#111;text-transform:uppercase">{T}</div>
<div class="a" style="left:60px;top:430px;width:560px;font:700 30px/1.25 Pop;color:#111">{R}</div>
<div class="a chips" style="left:60px;top:530px">{"".join(f'<div style="background:#111;color:#f5b700">{H.escape(c)}</div>' for c in chips)}</div>
{logo("#111","#111","#f5b700","left:60px;top:60px;display:none")}
<div class="a logo" style="left:300px;top:6px;color:#111"><b style="background:#111;color:#f5b700">ib</b>instrumentationblog.in</div>"""
    elif t == 1:  # Light flat illustration left, bold title right, orange pill
        p = P["peach"]; svg = ill(topic, p)
        body = f"""<div class="a" style="inset:0;background:#f4f6fb"></div>
<div class="a" style="left:-80px;top:60px;width:640px;height:560px;border-radius:48% 52% 46% 54%;background:#ffd9c7"></div>
<div class="a" style="left:40px;top:70px">{svg}</div>
<div class="a" style="right:60px;top:70px;display:grid;grid-template-columns:repeat(6,14px);gap:10px">{"".join('<i style="width:14px;height:14px;border-radius:50%;border:3px solid #ff7a3d;display:block"></i>' for _ in range(12))}</div>
<div class="a" style="left:640px;top:170px;width:520px;font:{fit(title,74,20)}px/1.05 Archivo;color:#2a3550;text-transform:uppercase">{T}</div>
<div class="a" style="left:640px;top:450px;max-width:520px;background:#ff7a3d;color:#fff;font:700 28px/1.25 Pop;padding:12px 24px;border-radius:10px">{R}</div>
<div class="a chips" style="left:640px;top:560px">{"".join(f'<div style="background:#fff;color:#2a3550;border:2px solid #d6dcea">{H.escape(c)}</div>' for c in chips)}</div>
{logo("#2a3550","#2a3550","#ff7a3d","right:36px;bottom:24px;top:auto;display:none")}
<div class="a logo" style="left:640px;top:90px;color:#2a3550"><b style="background:#2a3550;color:#ff7a3d">ib</b>instrumentationblog.in</div>"""
    elif t == 2:  # Black editorial, huge lowercase white title, mono illustration with grid
        p = P["noir"]; svg = ill(topic, p)
        body = f"""<div class="a" style="inset:0;background:#0c0c0c"></div>
<div class="a" style="right:0;top:0;width:560px;height:675px;background:linear-gradient(135deg,#2b2b2b,#0c0c0c)"></div>
<div class="a" style="right:0;top:0;width:560px;height:675px;background-image:linear-gradient(rgba(255,255,255,.07) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.07) 1px,transparent 1px);background-size:56px 56px"></div>
<div class="a" style="right:10px;top:70px;filter:grayscale(1) contrast(1.15)">{svg}</div>
<div class="a" style="left:60px;top:150px;width:640px;font:800 {fit(title,82,22)}px/1.02 Pop;color:#fff;text-transform:lowercase;letter-spacing:-2px">{T}</div>
<div class="a" style="left:60px;top:470px;width:600px;font:500 30px/1.3 Pop;color:#cfcfcf">{R}</div>
<div class="a chips" style="left:60px;top:570px">{"".join(f'<div style="background:transparent;color:#fff;border:2px solid #fff">{H.escape(c)}</div>' for c in chips)}</div>
<div class="a logo" style="left:60px;top:50px;color:#fff"><b style="background:#fff;color:#0c0c0c">ib</b>instrumentationblog.in</div>"""
    elif t == 3:  # Green playful, centred huge title with red ribbon, squiggles
        p = P["green"]; svg = ill(topic, p)
        sq = '<svg class="a" style="{}" width="160" height="80" viewBox="0 0 160 80"><path d="M5 40 q20 -35 40 0 t40 0 t40 0 t30 0" stroke="#f2c14e" stroke-width="9" fill="none" stroke-linecap="round"/></svg>'
        body = f"""<div class="a" style="inset:0;background:#2f9e6b"></div>
<div class="a" style="inset:0;background:radial-gradient(circle at 50% 40%,rgba(255,255,255,.18),transparent 60%)"></div>
{sq.format('left:40px;top:40px')}{sq.format('right:40px;bottom:50px;transform:rotate(180deg)')}
<div class="a" style="right:30px;top:180px;transform:scale(.72);transform-origin:right top;opacity:.95">{svg}</div>
<div class="a" style="left:60px;top:150px;width:720px;font:{fit(title,92,18)}px/1.0 Archivo;color:#fff;text-shadow:0 6px 0 #14532d;text-transform:uppercase">{T}</div>
<div class="a" style="left:60px;top:440px;background:#e5484d;color:#fff;font:700 30px/1.2 Pop;padding:14px 28px;transform:rotate(-1.5deg);box-shadow:0 8px 0 #9e2f33;max-width:700px">{R}</div>
<div class="a chips" style="left:60px;top:560px">{"".join(f'<div style="background:#f2c14e;color:#14532d">{H.escape(c)}</div>' for c in chips)}</div>
<div class="a logo" style="right:40px;top:40px;color:#fff"><b style="background:#fff;color:#2f9e6b">ib</b>instrumentationblog.in</div>"""
    elif t == 4:  # Tech blue gradient, glowing lines
        p = P["tech"]; svg = ill(topic, p)
        body = f"""<div class="a" style="inset:0;background:linear-gradient(115deg,#061445 0%,#0b2a7a 55%,#1556d6 100%)"></div>
<svg class="a" style="inset:0" width="1200" height="675"><g stroke="#22d3ee" stroke-width="2" fill="none" opacity=".35"><path d="M640 0 v120 h120 v80"/><path d="M1200 140 h-160 v120 h-80"/><path d="M700 675 v-90 h200 v-60"/><path d="M1200 520 h-120 v-80"/></g><g fill="#22d3ee" opacity=".7"><circle cx="760" cy="200" r="6"/><circle cx="960" cy="260" r="6"/><circle cx="900" cy="525" r="6"/><circle cx="1080" cy="440" r="6"/></g></svg>
<div class="a" style="right:30px;top:60px;width:600px;height:600px;border-radius:50%;background:radial-gradient(circle,rgba(34,211,238,.25),transparent 65%)"></div>
<div class="a" style="right:50px;top:70px">{svg}</div>
<div class="a" style="left:60px;top:150px;width:560px;font:800 {fit(title,68,22)}px/1.08 Pop;color:#fff">{T}</div>
<div class="a" style="left:60px;top:440px;font:800 22px Pop;letter-spacing:3px;color:#22d3ee;text-transform:uppercase">instrumentation guide</div>
<div class="a" style="left:60px;top:480px;width:560px;font:500 28px/1.3 Pop;color:#dbe7ff">{R}</div>
<div class="a chips" style="left:60px;top:580px">{"".join(f'<div style="background:rgba(34,211,238,.15);color:#fff;border:2px solid #22d3ee">{H.escape(c)}</div>' for c in chips)}</div>
<div class="a logo" style="left:60px;top:50px;color:#fff"><b style="background:#22d3ee;color:#061445">ib</b>instrumentationblog.in</div>"""
    else:  # 5 Vintage sketch, serif title in framed label
        p = P["sepia"]; svg = ill(topic, p)
        body = f"""<div class="a" style="inset:0;background:#efe4cf"></div>
<div class="a" style="inset:0;background:radial-gradient(circle at 50% 50%,transparent 55%,rgba(90,70,51,.35) 100%)"></div>
<div class="a" style="inset:22px;border:3px solid #5a4633"></div><div class="a" style="inset:32px;border:1px solid #5a4633"></div>
<div class="a" style="right:60px;top:70px;filter:sepia(1) saturate(.6) contrast(1.1);opacity:.9">{svg}</div>
<div class="a" style="left:70px;top:110px;width:600px;background:#f7f0e1;border:3px solid #3b2f23;padding:30px 34px;box-shadow:8px 8px 0 #3b2f23">
 <div style="font:900 {fit(title,64,22)}px/1.05 Playfair;color:#2b2118">{T}</div>
 <div style="height:3px;background:#8b3a1a;margin:18px 0 14px;width:120px"></div>
 <div style="font:700 26px/1.3 Pop;color:#5a4633">{R}</div></div>
<div class="a chips" style="left:70px;top:560px">{"".join(f'<div style="background:#3b2f23;color:#efe4cf">{H.escape(c)}</div>' for c in chips)}</div>
<div class="a logo" style="right:60px;top:50px;color:#3b2f23"><b style="background:#3b2f23;color:#efe4cf">ib</b>instrumentationblog.in</div>"""
    return f"<!DOCTYPE html><html><head><meta charset='utf-8'><style>{FONTS}</style></head><body><div class='w'>{body}</div></body></html>"

def render(out, title, ribbon, chips, topic, t):
    out = os.path.abspath(out); base = out.rsplit('.', 1)[0]
    open(base + '.featimg.html', 'w').write(page(title, ribbon, chips, topic, t))
    with sync_playwright() as pw:
        b = pw.chromium.launch(executable_path='/usr/bin/google-chrome', args=['--no-sandbox', '--allow-file-access-from-files'])
        pg = b.new_page(viewport={'width': 1200, 'height': 675}); pg.goto('file://' + base + '.featimg.html'); pg.wait_for_timeout(600)
        pg.screenshot(path=base + '.featimg.png'); b.close()
    Image.open(base + '.featimg.png').convert('RGB').save(out, 'WEBP', quality=84, method=6)

if __name__ == '__main__':
    a = sys.argv
    render(a[1], a[2], a[3], [c for c in a[4].split(',') if c], a[5], int(a[6]))
