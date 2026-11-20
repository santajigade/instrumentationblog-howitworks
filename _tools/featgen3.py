#!/usr/bin/env python3
"""More poster designs (6+). featgen3.py out.webp "Title" "Ribbon" "c1,c2,c3" topic template"""
import sys, os, html as H
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import featgen2 as g
from featgen import ill
fit = g.fit
PAL = dict(
    blue=dict(d="#e8f1ff", m="#9cc3ff", a="#ffffff", a2="#7dd3fc", t="#fff", h="#fff", p="#0b2545", r="#13315c"),
    swiss=dict(d="#1d1d1f", m="#3a3a3c", a="#e63946", a2="#457b9d", t="#1d1d1f", h="#e63946", p="#fff", r="#1d1d1f"),
    neon=dict(d="#1a1033", m="#3b2a6b", a="#f472b6", a2="#22d3ee", t="#fff", h="#f472b6", p="#fff", r="#2a1a55"),
)
_ill = ill
def body(title, ribbon, chips, topic, t):
    global ill
    ill = (lambda tp, p: _ill(tp, p).replace('NTU', 'pH')) if 'pH' in title else _ill
    T = H.escape(title); R = H.escape(ribbon)
    if t == 6:  # Blueprint spec sheet
        svg = ill(topic, PAL['blue'])
        return f"""<div class="a" style="inset:0;background:#0b3d91"></div>
<div class="a" style="inset:0;background-image:linear-gradient(rgba(255,255,255,.10) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.10) 1px,transparent 1px),linear-gradient(rgba(255,255,255,.05) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.05) 1px,transparent 1px);background-size:100px 100px,100px 100px,20px 20px,20px 20px"></div>
<div class="a" style="inset:26px;border:2px solid rgba(255,255,255,.8)"></div>
<div class="a" style="right:60px;top:80px;width:460px;height:470px;border:2px dashed rgba(255,255,255,.7);overflow:hidden"><div class="a" style="left:-30px;top:-20px;filter:brightness(1.6) saturate(.4)">{svg}</div></div>
<div class="a" style="right:60px;top:560px;font:400 26px Bebas;letter-spacing:4px;color:#cfe3ff">FIG. 1 &nbsp; SCHEMATIC VIEW</div>
<div class="a" style="left:66px;top:70px;font:400 28px Bebas;letter-spacing:6px;color:#9cc3ff">TECHNICAL SPEC SHEET</div>
<div class="a" style="left:66px;top:120px;width:600px;font:400 {fit(title,104,16,590,0.42)}px/0.98 Bebas;color:#fff;letter-spacing:1px">{T}</div>
<div class="a" style="left:66px;top:430px;width:580px;border-left:6px solid #7dd3fc;padding-left:18px;font:700 28px/1.25 Pop;color:#e8f1ff">{R}</div>
<div class="a chips" style="left:66px;top:540px">{"".join(f'<div style="background:transparent;color:#fff;border:2px dashed #fff;border-radius:4px">{H.escape(c)}</div>' for c in chips)}</div>
<div class="a" style="left:66px;top:612px;font:500 18px Pop;color:#cfe3ff;letter-spacing:2px">DWG NO. IB-2026 &nbsp;|&nbsp; REV A</div>
<div class="a logo" style="right:60px;top:36px;color:#fff"><b style="background:#fff;color:#0b3d91">ib</b>instrumentationblog.in</div>"""
    if t == 7:  # Swiss red column
        svg = ill(topic, PAL['swiss'])
        return f"""<div class="a" style="inset:0;background:#f5f5f2"></div>
<div class="a" style="left:0;top:0;width:150px;height:675px;background:#e63946"></div>
<div class="a" style="left:28px;top:610px;transform:rotate(-90deg);transform-origin:left top;font:400 46px Bebas;letter-spacing:8px;color:#fff;white-space:nowrap">FIELD GUIDE</div>
<div class="a" style="right:40px;top:90px;width:470px;height:470px;border-radius:50%;background:#e9e9e4;overflow:hidden"><div class="a" style="left:-20px;top:-10px">{svg}</div></div>
<div class="a" style="right:40px;top:90px;width:470px;height:470px;border-radius:50%;border:10px solid #1d1d1f"></div>
<div class="a" style="left:190px;top:110px;width:500px;font:{fit(title,70,18,500,0.62)}px/1.04 Archivo;color:#1d1d1f;letter-spacing:-1px">{T}</div>
<div class="a" style="left:190px;top:440px;width:40px;height:8px;background:#e63946"></div>
<div class="a" style="left:190px;top:462px;width:470px;font:700 28px/1.25 Pop;color:#1d1d1f">{R}</div>
<div class="a chips" style="left:190px;top:560px">{"".join(f'<div style="background:#1d1d1f;color:#fff;border-radius:0">{H.escape(c)}</div>' for c in chips)}</div>
<div class="a logo" style="left:190px;top:40px;color:#1d1d1f"><b style="background:#e63946;color:#fff">ib</b>instrumentationblog.in</div>"""
    if t == 9:  # Lime diagonal split
        svg = ill(topic, dict(d="#1c1f24", m="#3a3f47", a="#1c1f24", a2="#4b5563", t="#1c1f24", h="#1c1f24", p="#c6f432", r="#1c1f24"))
        return f"""<div class="a" style="inset:0;background:#1c1f24"></div>
<div class="a" style="inset:0;background:#c6f432;clip-path:polygon(58% 0,100% 0,100% 100%,40% 100%)"></div>
<div class="a" style="right:30px;top:80px">{svg}</div>
<div class="a" style="left:60px;top:60px;font:400 30px Bebas;letter-spacing:6px;color:#c6f432">ENGINEERING NOTES</div>
<div class="a" style="left:60px;top:120px;width:520px;font:{fit(title,74,18,500,0.78)}px/1.02 Archivo;color:#fff">{T}</div>
<div class="a" style="left:60px;top:440px;width:470px;font:700 28px/1.25 Pop;color:#c6f432">{R}</div>
<div class="a chips" style="left:60px;top:530px;width:560px">{"".join(f'<div style="background:#2c313a;color:#fff">{H.escape(c)}</div>' for c in chips)}</div>
<div class="a logo" style="right:40px;bottom:30px;color:#1c1f24"><b style="background:#1c1f24;color:#c6f432">ib</b>instrumentationblog.in</div>"""
    if t == 10:  # Bauhaus shapes
        svg = ill(topic, dict(d="#111", m="#333", a="#f2b705", a2="#1d4ed8", t="#111", h="#d62828", p="#fff", r="#111"))
        return f"""<div class="a" style="inset:0;background:#f3ead8"></div>
<div class="a" style="right:-60px;top:-80px;width:420px;height:420px;border-radius:50%;background:#f2b705"></div>
<div class="a" style="right:300px;bottom:-40px;width:200px;height:200px;background:#1d4ed8;transform:rotate(12deg)"></div>
<div class="a" style="left:0;bottom:0;width:0;height:0;border-left:220px solid #d62828;border-top:220px solid transparent"></div>
<div class="a" style="right:40px;top:110px;background:#fff;border:5px solid #111;border-radius:6px;overflow:hidden;width:470px;height:420px"><div class="a" style="left:-30px;top:-20px">{svg}</div></div>
<div class="a" style="left:60px;top:110px;width:600px;font:400 {fit(title,108,16,590,0.42)}px/0.95 Bebas;color:#111">{T}</div>
<div class="a" style="left:60px;top:420px;background:#111;color:#f3ead8;font:700 28px/1.25 Pop;padding:12px 22px;max-width:580px">{R}</div>
<div class="a chips" style="left:240px;top:560px">{"".join(f'<div style="background:#fff;color:#111;border:3px solid #111;border-radius:0">{H.escape(c)}</div>' for c in chips)}</div>
<div class="a logo" style="left:60px;top:40px;color:#111"><b style="background:#d62828;color:#fff">ib</b>instrumentationblog.in</div>"""
    if t == 11:  # Sunset gradient with white card
        svg = ill(topic, dict(d="#1e1b4b", m="#3730a3", a="#fb7185", a2="#f59e0b", t="#1e1b4b", h="#e11d48", p="#fff", r="#1e1b4b"))
        return f"""<div class="a" style="inset:0;background:linear-gradient(135deg,#ff8a00 0%,#ff4d6d 50%,#a21caf 100%)"></div>
<div class="a" style="left:40px;top:100px;width:680px;height:500px;background:#fff;border-radius:26px;box-shadow:0 30px 60px rgba(60,0,60,.35)"></div>
<div class="a" style="right:30px;top:60px;width:460px;height:560px;border-radius:26px;background:rgba(255,255,255,.18);border:2px solid rgba(255,255,255,.6);overflow:hidden"><div class="a" style="left:-40px;top:30px">{svg}</div></div>
<div class="a" style="left:80px;top:140px;width:560px;font:800 {fit(title,64,20,550,0.62)}px/1.06 Pop;color:#1e1b4b">{T}</div>
<div class="a" style="left:80px;top:400px;width:560px;font:600 26px/1.3 Pop;color:#e11d48">{R}</div>
<div class="a chips" style="left:80px;top:500px">{"".join(f'<div style="background:#fff1f2;color:#9f1239;border:2px solid #fecdd3">{H.escape(c)}</div>' for c in chips)}</div>
<div class="a logo" style="left:40px;top:36px;color:#fff"><b style="background:#fff;color:#e11d48">ib</b>instrumentationblog.in</div>"""
    if t == 12:  # Retro terminal
        svg = ill(topic, dict(d="#03140a", m="#0a3b1f", a="#39ff88", a2="#16a34a", t="#39ff88", h="#39ff88", p="#03140a", r="#062b16"))
        return f"""<div class="a" style="inset:0;background:#020a05"></div>
<div class="a" style="inset:30px;border-radius:30px;background:radial-gradient(ellipse at center,#06260f 0%,#020a05 80%);box-shadow:inset 0 0 80px rgba(57,255,136,.25);border:3px solid #1f6f3f"></div>
<div class="a" style="inset:30px;border-radius:30px;background:repeating-linear-gradient(0deg,rgba(0,0,0,.25) 0 2px,transparent 2px 5px)"></div>
<div class="a" style="right:70px;top:110px;opacity:.9;filter:drop-shadow(0 0 8px rgba(57,255,136,.6))">{svg}</div>
<div class="a" style="left:80px;top:80px;font:700 24px 'DejaVu Sans Mono',monospace;color:#39ff88">C:\\IB&gt; run guide.exe<span style="background:#39ff88;color:#020a05">_</span></div>
<div class="a" style="left:80px;top:140px;width:600px;font:700 {fit(title,64,20,590,0.62)}px/1.1 'DejaVu Sans Mono',monospace;color:#39ff88;text-shadow:0 0 12px rgba(57,255,136,.7)">{T}</div>
<div class="a" style="left:80px;top:430px;width:560px;font:500 26px/1.3 'DejaVu Sans Mono',monospace;color:#a7f3c5">// {R}</div>
<div class="a chips" style="left:80px;top:530px">{"".join(f'<div style="background:transparent;color:#39ff88;border:2px solid #39ff88;border-radius:4px;font-family:DejaVu Sans Mono,monospace">[{H.escape(c)}]</div>' for c in chips)}</div>
<div class="a logo" style="right:70px;top:60px;color:#39ff88"><b style="background:#39ff88;color:#020a05">ib</b>instrumentationblog.in</div>"""
    if t == 13:  # Magazine cover
        svg = ill(topic, dict(d="#111", m="#444", a="#c8102e", a2="#0f4c81", t="#111", h="#c8102e", p="#fff", r="#111"))
        return f"""<div class="a" style="inset:0;background:#fbfaf7"></div>
<div class="a" style="left:0;top:0;width:1200px;height:120px;background:#c8102e"></div>
<div class="a" style="left:50px;top:4px;font:400 118px/1 Bebas;letter-spacing:10px;color:#fff">ELECTRONICS</div>
<div class="a" style="right:50px;top:24px;text-align:right;font:700 20px/1.3 Pop;color:#fff">BENCH SERIES<br>2026 EDITION</div>
<div class="a" style="right:30px;top:150px;transform:scale(1.05);transform-origin:right top">{svg}</div>
<div class="a" style="left:50px;top:160px;width:600px;font:900 {fit(title,76,20,590,0.6)}px/1.02 Playfair;color:#111">{T}</div>
<div class="a" style="left:50px;top:430px;width:540px;font:700 italic 28px/1.25 Playfair;color:#c8102e">{R}</div>
<div class="a chips" style="left:50px;top:520px">{"".join(f'<div style="background:#111;color:#fbfaf7;border-radius:0;font:700 22px Pop;letter-spacing:1px;text-transform:uppercase">{H.escape(c)}</div>' for c in chips)}</div>
<div class="a logo" style="left:50px;bottom:28px;color:#111"><b style="background:#c8102e;color:#fff">ib</b>instrumentationblog.in</div>"""
    if t == 14:  # Oscilloscope teal with outlined title
        svg = ill(topic, dict(d="#0b2b2b", m="#134e4a", a="#fb7185", a2="#5eead4", t="#fff", h="#fb7185", p="#0b2b2b", r="#0f3d3d"))
        wave = ''.join(f'{x},{round(337-150*min(1,max(-1,(((x%300)/75)-2))) if (x%300)<150 else 337+150*min(1,max(-1,((((x%300)-150)/75)-1))))} ' for x in range(0,1201,10))
        return f"""<div class="a" style="inset:0;background:#0b2b2b"></div>
<div class="a" style="inset:0;background-image:linear-gradient(rgba(94,234,212,.12) 1px,transparent 1px),linear-gradient(90deg,rgba(94,234,212,.12) 1px,transparent 1px);background-size:75px 75px"></div>
<svg class="a" style="inset:0;opacity:.35" width="1200" height="675"><polyline points="{wave}" fill="none" stroke="#5eead4" stroke-width="4"/></svg>
<div class="a" style="right:40px;top:90px;width:460px;height:470px;border-radius:24px;background:#0f3d3d;border:3px solid #5eead4;overflow:hidden"><div class="a" style="left:-30px;top:-10px">{svg}</div></div>
<div class="a" style="left:60px;top:120px;width:600px;font:{fit(title,84,18,590,0.72)}px/1.0 Archivo;color:transparent;-webkit-text-stroke:2.5px #5eead4;text-transform:uppercase">{T}</div>
<div class="a" style="left:60px;top:440px;background:#fb7185;color:#0b2b2b;font:800 26px/1.25 Pop;padding:12px 22px;border-radius:40px;max-width:600px">{R}</div>
<div class="a chips" style="left:60px;top:550px">{"".join(f'<div style="background:#134e4a;color:#5eead4;border:2px solid #5eead4">{H.escape(c)}</div>' for c in chips)}</div>
<div class="a logo" style="left:60px;top:50px;color:#fff"><b style="background:#5eead4;color:#0b2b2b">ib</b>instrumentationblog.in</div>"""
    # 8 Neon glass
    svg = ill(topic, PAL['neon'])
    return f"""<div class="a" style="inset:0;background:radial-gradient(circle at 80% 20%,#5b21b6 0%,#1a1033 55%,#0d0820 100%)"></div>
<div class="a" style="left:-120px;bottom:-160px;width:520px;height:520px;border-radius:50%;background:radial-gradient(circle,rgba(244,114,182,.45),transparent 65%)"></div>
<div class="a" style="right:50px;top:70px;width:500px;height:520px;border-radius:28px;background:rgba(255,255,255,.08);border:1px solid rgba(255,255,255,.25);box-shadow:0 0 60px rgba(34,211,238,.25);overflow:hidden"><div class="a" style="left:-10px;top:0">{svg}</div></div>
<div class="a" style="left:60px;top:140px;width:580px;font:800 {fit(title,72,20,570,0.62)}px/1.05 Pop;background:linear-gradient(90deg,#f472b6,#a78bfa,#22d3ee);-webkit-background-clip:text;color:transparent">{T}</div>
<div class="a" style="left:60px;top:450px;width:570px;font:500 28px/1.3 Pop;color:#e9e3ff">{R}</div>
<div class="a chips" style="left:60px;top:560px">{"".join(f'<div style="background:rgba(244,114,182,.15);color:#fff;border:2px solid #f472b6;box-shadow:0 0 14px rgba(244,114,182,.5)">{H.escape(c)}</div>' for c in chips)}</div>
<div class="a logo" style="left:60px;top:50px;color:#fff"><b style="background:linear-gradient(90deg,#f472b6,#22d3ee);color:#1a1033">ib</b>instrumentationblog.in</div>"""
def page(title, ribbon, chips, topic, t):
    return f"<!DOCTYPE html><html><head><meta charset='utf-8'><style>{g.FONTS}</style></head><body><div class='w'>{body(title, ribbon, chips, topic, t)}</div></body></html>"
g.page_orig = g.page
def page_any(title, ribbon, chips, topic, t):
    return page(title, ribbon, chips, topic, t) if t >= 6 else g.page_orig(title, ribbon, chips, topic, t)
g.page = page_any
if __name__ == '__main__':
    a = sys.argv
    g.render(a[1], a[2], a[3], [c for c in a[4].split(',') if c], a[5], int(a[6]))
