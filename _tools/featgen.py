#!/usr/bin/env python3
"""Featured image generator for instrumentationblog.in.
Usage: featgen.py out.webp "Main title" "Ribbon text" "chip1,chip2,chip3" topic [variant_index]
topic: plc dcs scada hmi flow pressure level temperature valve electrical electronics calibration safety network generic
"""
import sys, hashlib, html as H
from playwright.sync_api import sync_playwright
from PIL import Image

PAL = [  # bg_dark, bg_mid, accent, accent2, title_color, title_hl, panel
    dict(d="#0b1a33", m="#16407a", a="#f5a300", a2="#3fa9ff", t="#0b1a33", h="#0e4c92", p="#ffffff", r="#0e2a52"),
    dict(d="#062a2c", m="#0c5b5e", a="#ffb020", a2="#3fe0d0", t="#06323a", h="#0a7d7f", p="#f4fbfb", r="#0a4b50"),
    dict(d="#1a0f3a", m="#3b237a", a="#22d3ee", a2="#a78bfa", t="#1a0f3a", h="#5b3cc4", p="#f8f6ff", r="#2e1a66"),
    dict(d="#0d2416", m="#1d5a35", a="#f5c400", a2="#4ade80", t="#0d2416", h="#1d7a46", p="#f5fbf6", r="#174a2c"),
    dict(d="#1c1c22", m="#45232a", a="#ff6b35", a2="#ffd166", t="#1c1c22", h="#c0392b", p="#fbf7f5", r="#3a1d22"),
    dict(d="#071d3a", m="#0b4fa3", a="#ffe600", a2="#5ec8ff", t="#071d3a", h="#0b5ed7", p="#f4f8ff", r="#0b3470"),
]

def led(x, y, c, r=4.5):
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{c}" filter="url(#gl)"/>'

def ill(topic, P):
    a, a2 = P["a"], P["a2"]
    g = ""
    if topic in ("dcs",):
        g += '<rect x="30" y="20" width="330" height="520" rx="10" fill="#2f3b4a" stroke="#5a6b80" stroke-width="3"/>'
        for ri, y in enumerate((45, 205, 365)):
            g += f'<rect x="50" y="{y}" width="290" height="140" rx="6" fill="#1b232d"/>'
            for i in range(8):
                x = 60 + i * 35
                spare = i == 7
                g += f'<rect x="{x}" y="{y+10}" width="28" height="120" rx="3" fill="{"#eef2f7" if spare else "#d5dde8"}" {"stroke=\"%s\" stroke-dasharray=\"4 3\" stroke-width=\"2\"" % a if spare else ""}/>'
                for k in range(4):
                    g += led(x + 14, y + 45 + k * 20, a if (i + k + ri) % 5 == 0 else "#36d399")
        tags = ["AI", "AO", "DI", "DO", "PT A", "PT B"]
        for i, t in enumerate(tags):
            y = 70 + i * 84
            g += f'<path d="M360 {y+40} C430 {y+40} 430 {y+18} 470 {y+18}" stroke="{a if i%2 else a2}" stroke-width="5" fill="none" filter="url(#gl)"/>'
            g += f'<rect x="470" y="{y}" width="90" height="42" rx="8" fill="{P["r"]}" stroke="{a if i%2 else a2}" stroke-width="2"/><text x="515" y="{y+29}" text-anchor="middle" class="sv">{t}</text>'
    elif topic == "plc":
        g += '<rect x="20" y="60" width="520" height="190" rx="10" fill="#2f3b4a" stroke="#5a6b80" stroke-width="3"/>'
        g += '<rect x="40" y="80" width="110" height="150" rx="6" fill="#d5dde8"/><rect x="52" y="95" width="86" height="40" rx="4" fill="#1b232d"/>'
        g += led(70, 160, "#36d399") + led(90, 160, a) + led(110, 160, "#36d399")
        for i in range(7):
            x = 165 + i * 52
            g += f'<rect x="{x}" y="80" width="44" height="150" rx="5" fill="#cfd7e2"/><rect x="{x+6}" y="88" width="32" height="10" fill="{P["h"]}"/>'
            for k in range(5):
                g += led(x + 22, 115 + k * 22, "#36d399" if (i + k) % 4 else a, 4)
        # ladder
        g += f'<g stroke="{a2}" stroke-width="5" fill="none" filter="url(#gl)"><line x1="40" y1="300" x2="40" y2="530"/><line x1="520" y1="300" x2="520" y2="530"/>'
        for y in (330, 410, 490):
            g += f'<line x1="40" y1="{y}" x2="150" y2="{y}"/><line x1="150" y1="{y-18}" x2="150" y2="{y+18}"/><line x1="172" y1="{y-18}" x2="172" y2="{y+18}"/><line x1="172" y1="{y}" x2="400" y2="{y}"/><circle cx="430" cy="{y}" r="28"/><line x1="458" y1="{y}" x2="520" y2="{y}"/>'
        g += '</g>'
        g += f'<path d="M260 392 v36 M240 410 h40" stroke="{a}" stroke-width="5"/>'
    elif topic in ("scada", "hmi"):
        g += '<rect x="20" y="40" width="520" height="330" rx="14" fill="#1b232d" stroke="#5a6b80" stroke-width="4"/><rect x="40" y="60" width="480" height="290" rx="6" fill="#0e1a2b"/>'
        g += f'<rect x="60" y="110" width="70" height="150" rx="8" fill="none" stroke="{a2}" stroke-width="4"/><rect x="64" y="180" width="62" height="76" fill="{a2}" opacity=".5"/>'
        g += f'<path d="M130 230 H220 M220 230 V170 H300" stroke="#cfd7e2" stroke-width="5" fill="none"/><circle cx="230" cy="230" r="18" fill="none" stroke="{a}" stroke-width="4"/><path d="M300 150 l30 20 l-30 20z" fill="{a}"/>'
        g += f'<polyline points="340,320 370,280 400,300 430,240 460,260 500,200" stroke="#36d399" stroke-width="4" fill="none" filter="url(#gl)"/>'
        g += f'<rect x="60" y="290" width="70" height="40" rx="6" fill="#c0392b"/><text x="95" y="316" text-anchor="middle" class="sv" font-size="30">ALARM</text>'
        g += '<rect x="250" y="370" width="60" height="70" fill="#2f3b4a"/><rect x="190" y="440" width="180" height="16" rx="8" fill="#2f3b4a"/>'
        if topic == "scada":
            for i, x in enumerate((60, 230, 400)):
                g += f'<rect x="{x}" y="480" width="110" height="60" rx="8" fill="#2f3b4a" stroke="{a2 if i!=1 else a}" stroke-width="3"/><text x="{x+55}" y="517" text-anchor="middle" class="sv">{["PLC","RTU","PLC"][i]}</text>'
            g += f'<path d="M115 480 V460 H455 V480 M285 460 V456" stroke="{a2}" stroke-width="4" fill="none" stroke-dasharray="8 6"/>'
    elif topic == "flow":
        g += f'<rect x="0" y="300" width="560" height="90" fill="#9aa8b8"/><rect x="0" y="315" width="560" height="60" fill="{a2}" opacity=".35"/>'
        g += '<rect x="200" y="280" width="160" height="130" rx="10" fill="#cfd7e2"/><rect x="240" y="160" width="80" height="120" fill="#2f3b4a"/><circle cx="280" cy="140" r="70" fill="#d5dde8" stroke="#5a6b80" stroke-width="5"/>'
        g += f'<circle cx="280" cy="140" r="50" fill="#0e1a2b"/><text x="280" y="150" text-anchor="middle" class="sv" font-size="30" fill="#36d399">42.6</text>'
        for x in (60, 120, 420, 480):
            g += f'<path d="M{x} 345 l25 0 m-10 -10 l10 10 l-10 10" stroke="{a}" stroke-width="5" fill="none"/>'
    elif topic == "pressure":
        g += '<circle cx="280" cy="240" r="190" fill="#d5dde8" stroke="#5a6b80" stroke-width="8"/><circle cx="280" cy="240" r="165" fill="#fff"/>'
        import math
        for i in range(11):
            ang = math.radians(135 + i * 27)
            x1, y1 = 280 + 150 * math.cos(ang), 240 + 150 * math.sin(ang)
            x2, y2 = 280 + 125 * math.cos(ang), 240 + 125 * math.sin(ang)
            g += f'<line x1="{x1:.0f}" y1="{y1:.0f}" x2="{x2:.0f}" y2="{y2:.0f}" stroke="#1b232d" stroke-width="5"/>'
        g += f'<path d="M150 330 A160 160 0 0 1 120 200" stroke="#36d399" stroke-width="14" fill="none"/><path d="M440 200 A160 160 0 0 1 410 330" stroke="#c0392b" stroke-width="14" fill="none"/>'
        g += f'<line x1="280" y1="240" x2="380" y2="150" stroke="{a}" stroke-width="10" stroke-linecap="round"/><circle cx="280" cy="240" r="16" fill="#1b232d"/>'
        g += '<rect x="250" y="430" width="60" height="70" fill="#9aa8b8"/><rect x="230" y="500" width="100" height="30" fill="#5a6b80"/>'
    elif topic == "level":
        g += f'<rect x="80" y="90" width="300" height="420" rx="30" fill="#cfd7e2" stroke="#5a6b80" stroke-width="5"/><rect x="95" y="260" width="270" height="235" rx="20" fill="{a2}" opacity=".6"/>'
        g += f'<path d="M95 260 q35 -14 68 0 t68 0 t68 0 t66 0" stroke="#fff" stroke-width="4" fill="none"/>'
        g += f'<rect x="200" y="40" width="60" height="50" fill="#2f3b4a"/><path d="M230 90 L230 250" stroke="{a}" stroke-width="4" stroke-dasharray="10 8"/><path d="M215 235 l15 20 l15 -20" fill="{a}"/>'
        for i, y in enumerate((150, 250, 350, 450)):
            g += f'<line x1="400" y1="{y}" x2="440" y2="{y}" stroke="#cfd7e2" stroke-width="4"/><text x="455" y="{y+8}" class="sv" fill="#cfd7e2">{100-i*25}%</text>'
    elif topic == "temperature":
        g += f'<rect x="230" y="40" width="100" height="380" rx="50" fill="#d5dde8" stroke="#5a6b80" stroke-width="5"/><rect x="260" y="160" width="40" height="280" rx="20" fill="{a}"/><circle cx="280" cy="460" r="75" fill="{a}" stroke="#5a6b80" stroke-width="6"/>'
        for i in range(8):
            g += f'<line x1="340" y1="{80+i*40}" x2="{380 if i%2==0 else 365}" y2="{80+i*40}" stroke="#cfd7e2" stroke-width="4"/>'
        g += f'<path d="M60 520 q60 -80 0 -160 q-60 -80 0 -160" stroke="{a2}" stroke-width="6" fill="none" filter="url(#gl)"/>'
    elif topic == "valve":
        g += '<rect x="0" y="380" width="560" height="80" fill="#9aa8b8"/><path d="M170 340 L280 420 L170 500Z M390 340 L280 420 L390 500Z" fill="#5a6b80"/>'
        g += f'<rect x="270" y="200" width="20" height="200" fill="#2f3b4a"/><path d="M140 200 Q280 40 420 200Z" fill="{P["h"]}" stroke="#cfd7e2" stroke-width="4"/><rect x="250" y="250" width="60" height="40" rx="4" fill="{a}"/>'
    elif topic == "electrical":
        g += '<rect x="40" y="40" width="300" height="500" rx="12" fill="#cfd7e2" stroke="#5a6b80" stroke-width="4"/>'
        for i in range(4):
            y = 80 + i * 110
            g += f'<rect x="70" y="{y}" width="240" height="80" rx="6" fill="#2f3b4a"/>'
            for k in range(4):
                g += f'<rect x="{85+k*55}" y="{y+12}" width="40" height="56" rx="4" fill="#eef2f7"/><rect x="{97+k*55}" y="{y+22}" width="16" height="24" rx="3" fill="{a if (i+k)%3 else "#36d399"}"/>'
        g += f'<path d="M370 300 q30 -120 60 0 t60 0" stroke="{a2}" stroke-width="6" fill="none" filter="url(#gl)"/><path d="M450 120 l-30 70 h30 l-20 70 l60 -90 h-32 l24 -50z" fill="{a}"/>'
    elif topic == "electronics":
        g += f'<rect x="30" y="50" width="500" height="460" rx="20" fill="#14532d" stroke="#5a6b80" stroke-width="4"/>'
        for i in range(10):
            g += f'<path d="M{60+i*45} 70 V{150+(i%3)*30} H{200+(i%4)*20}" stroke="{a}" stroke-width="3" fill="none" opacity=".8"/>'
        g += '<rect x="180" y="200" width="200" height="160" rx="10" fill="#1b232d"/>'
        for k in range(8):
            g += f'<rect x="{192+k*23}" y="186" width="10" height="14" fill="#cfd7e2"/><rect x="{192+k*23}" y="360" width="10" height="14" fill="#cfd7e2"/>'
        g += f'<text x="280" y="290" text-anchor="middle" class="sv" font-size="30" fill="{a2}">MCU</text>'
        g += f'<rect x="80" y="400" width="70" height="30" rx="6" fill="#d97706"/><rect x="420" y="400" width="40" height="70" rx="20" fill="#2563eb"/>'
    elif topic == "safety":
        g += f'<path d="M280 40 L470 110 V270 C470 400 380 480 280 520 C180 480 90 400 90 270 V110Z" fill="{P["r"]}" stroke="{a}" stroke-width="8"/>'
        g += f'<path d="M190 280 l60 60 l120 -130" stroke="#36d399" stroke-width="22" fill="none" stroke-linecap="round" stroke-linejoin="round" filter="url(#gl)"/>'
        for i,t in enumerate(["PL a","PL b","PL c","PL d","PL e"]):
            g += f'<rect x="{30+i*104}" y="515" width="94" height="40" rx="20" fill="{a if i==3 else "#2f3b4a"}"/><text x="{77+i*104}" y="543" text-anchor="middle" class="sv" font-size="30">{t}</text>'
    elif topic == "ai":
        import math
        g += '<path d="M60 520 L140 300 L220 520 M80 470 H200 M100 410 H180 M120 350 H160" stroke="#9aa8b8" stroke-width="6" fill="none"/>'
        g += f'<path d="M300 520 h220 M350 520 v-90 h120 v90 M410 430 l-60 -60 l120 0z" stroke="#9aa8b8" stroke-width="6" fill="none"/>'
        nodes=[(180,90),(180,170),(180,250),(320,60),(320,140),(320,220),(320,300),(460,130),(460,230)]
        for i,(x1,y1) in enumerate(nodes[:3]):
            for (x2,y2) in nodes[3:7]: g += f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{a2}" stroke-width="2" opacity=".6"/>'
        for (x1,y1) in nodes[3:7]:
            for (x2,y2) in nodes[7:]: g += f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{a}" stroke-width="2" opacity=".6"/>'
        for i,(x,y) in enumerate(nodes): g += f'<circle cx="{x}" cy="{y}" r="16" fill="{P["r"]}" stroke="{a if i>6 else a2}" stroke-width="5" filter="url(#gl)"/>'
    elif topic == "analytical":
        g += f'<rect x="150" y="160" width="220" height="360" rx="16" fill="#d5dde8" opacity=".35" stroke="#cfd7e2" stroke-width="5"/><rect x="160" y="300" width="200" height="210" rx="10" fill="{a2}" opacity=".45"/>'
        for (x,y) in [(200,360),(260,420),(310,350),(230,470),(300,480),(190,430)]:
            g += f'<circle cx="{x}" cy="{y}" r="7" fill="#fff" opacity=".8"/>'
        g += f'<rect x="20" y="370" width="120" height="50" rx="10" fill="#2f3b4a"/><path d="M140 395 H380" stroke="{a}" stroke-width="10" filter="url(#gl)"/><path d="M260 395 L330 330 M260 395 L340 450" stroke="{a}" stroke-width="5" opacity=".7"/>'
        g += f'<rect x="380" y="360" width="150" height="70" rx="10" fill="{P["r"]}" stroke="{a}" stroke-width="3"/><text x="455" y="405" text-anchor="middle" class="sv">NTU</text>'
        g += f'<rect x="230" y="60" width="60" height="100" rx="8" fill="#2f3b4a"/>'
    else:
        g += f'<circle cx="280" cy="280" r="200" fill="none" stroke="{a2}" stroke-width="6" filter="url(#gl)"/><circle cx="280" cy="280" r="120" fill="none" stroke="{a}" stroke-width="6"/>'
        for i in range(8):
            import math
            ang = math.radians(i * 45)
            g += f'<circle cx="{280+200*math.cos(ang):.0f}" cy="{280+200*math.sin(ang):.0f}" r="18" fill="{P["r"]}" stroke="{a}" stroke-width="4"/>'
    return f'''<svg width="560" height="560" viewBox="0 0 560 560"><defs><filter id="gl"><feGaussianBlur stdDeviation="3" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter></defs><style>.sv{{font:700 24px Poppins;fill:#fff}}</style>{g}</svg>'''

CSS_BASE = """*{margin:0;padding:0;box-sizing:border-box}body{width:1200px;height:675px;overflow:hidden;font-family:Poppins,sans-serif}
.w{position:relative;width:1200px;height:675px;overflow:hidden}.abs{position:absolute}
.logo{display:flex;align-items:center;gap:8px;font-weight:800;font-size:24px}.logo b{border-radius:8px;padding:2px 12px;font-size:26px}
.chips{display:flex;gap:12px}.chips div{border-radius:30px;padding:10px 24px;font-weight:700;font-size:26px}"""

def page(title, ribbon, chips, topic, v):
    P = PAL[v % len(PAL)]
    L = (v // len(PAL) + v) % 4
    words = title.split()
    # highlight the last word(s)
    hl = " ".join(words[len(words)//2:]); lead = " ".join(words[:len(words)//2])
    tsize = 64 if len(title) <= 22 else (56 if len(title) <= 32 else 48)
    chips_h = "".join(f"<div>{H.escape(c)}</div>" for c in chips if c)
    svg = ill(topic, P)
    grid = f"background-image:linear-gradient(rgba(255,255,255,.05) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.05) 1px,transparent 1px);background-size:40px 40px"
    if L == 0:  # split: illustration left, light angled panel right
        body = f"""<div class="abs" style="inset:0;background:radial-gradient(circle at 25% 40%,{P['m']} 0%,{P['d']} 60%)"></div><div class="abs" style="inset:0;{grid}"></div>
<div class="abs" style="left:40px;top:40px">{svg}</div>
<div class="abs" style="right:560px;top:0;width:60px;height:675px;background:{P['a']};clip-path:polygon(70% 0,100% 0,30% 50%,100% 100%,70% 100%,0 50%)"></div>
<div class="abs" style="right:-60px;top:0;width:640px;height:675px;background:{P['p']};clip-path:polygon(16% 0,100% 0,100% 100%,0 100%,9% 50%)"></div>
<div class="abs logo" style="right:30px;top:24px;color:{P['r']}"><b style="background:{P['r']};color:{P['a']}">ib</b>instrumentationblog.in</div>
<div class="abs" style="left:715px;top:95px;width:460px;color:{P['t']};font-weight:800;font-size:{tsize}px;line-height:1.08">{H.escape(lead)}<br><span style="color:{P['h']}">{H.escape(hl)}</span></div>
<div class="abs" style="left:640px;top:395px;width:560px;padding:22px 30px 22px 60px;background:{P['r']};color:#fff;font-weight:700;font-size:32px;line-height:1.2;clip-path:polygon(6% 0,100% 0,100% 100%,0 100%);border-left:10px solid {P['a']}">{H.escape(ribbon)}</div>
<div class="abs chips" style="left:700px;top:560px">{chips_h.replace('<div>',f'<div style="background:#fff;color:{P["r"]};border:2px solid {P["h"]}33">')}</div>
<svg class="abs" style="left:0;bottom:-2px" width="1200" height="90" viewBox="0 0 1200 90" preserveAspectRatio="none"><path d="M0 50 C300 0 600 100 900 40 C1050 10 1150 30 1200 20 L1200 90 L0 90Z" fill="{P['a']}"/><path d="M0 70 C300 25 600 110 900 60 C1050 35 1150 50 1200 45 L1200 90 L0 90Z" fill="{P['d']}"/></svg>"""
    elif L == 1:  # dark full: title left, illustration right in glow circle
        body = f"""<div class="abs" style="inset:0;background:linear-gradient(120deg,{P['d']} 0%,{P['m']} 100%)"></div><div class="abs" style="inset:0;{grid}"></div>
<div class="abs" style="right:-40px;top:40px;width:640px;height:640px;border-radius:50%;background:radial-gradient(circle,{P['a2']}33 0%,transparent 65%)"></div>
<div class="abs" style="right:40px;top:60px;transform:scale(1.0)">{svg}</div>
<div class="abs logo" style="left:60px;top:40px;color:#fff"><b style="background:{P['a']};color:{P['d']}">ib</b>instrumentationblog.in</div>
<div class="abs" style="left:60px;top:150px;width:560px;color:#fff;font-weight:800;font-size:{tsize}px;line-height:1.08">{H.escape(lead)} <span style="color:{P['a']}">{H.escape(hl)}</span></div>
<div class="abs" style="left:60px;top:390px;width:90px;height:8px;border-radius:4px;background:{P['a']}"></div>
<div class="abs" style="left:60px;top:420px;width:540px;color:#e6eefb;font-weight:600;font-size:32px;line-height:1.25">{H.escape(ribbon)}</div>
<div class="abs chips" style="left:60px;top:560px">{chips_h.replace('<div>',f'<div style="background:{P["a"]}22;color:#fff;border:2px solid {P["a"]}">')}</div>"""
    elif L == 2:  # light card: illustration right on dark block, title left on light
        body = f"""<div class="abs" style="inset:0;background:{P['p']}"></div>
<div class="abs" style="right:0;top:0;width:620px;height:675px;background:radial-gradient(circle at 50% 45%,{P['m']} 0%,{P['d']} 70%);clip-path:polygon(12% 0,100% 0,100% 100%,0 100%)"></div>
<div class="abs" style="right:0;top:0;width:620px;height:675px;{grid};clip-path:polygon(12% 0,100% 0,100% 100%,0 100%)"></div>
<div class="abs" style="right:20px;top:60px">{svg}</div>
<div class="abs" style="left:0;top:0;width:14px;height:675px;background:{P['a']}"></div>
<div class="abs logo" style="left:60px;top:40px;color:{P['r']}"><b style="background:{P['r']};color:{P['a']}">ib</b>instrumentationblog.in</div>
<div class="abs" style="left:60px;top:140px;width:540px;color:{P['t']};font-weight:800;font-size:{tsize}px;line-height:1.08">{H.escape(lead)}<br><span style="color:{P['h']}">{H.escape(hl)}</span></div>
<div class="abs" style="left:60px;top:400px;padding:16px 26px;background:{P['a']};color:{P['d']};font-weight:700;font-size:28px;line-height:1.2;border-radius:12px;max-width:540px">{H.escape(ribbon)}</div>
<div class="abs chips" style="left:60px;top:560px">{chips_h.replace('<div>',f'<div style="background:#fff;color:{P["r"]};border:2px solid {P["r"]}44">')}</div>"""
    else:  # L==3 centered banner
        ch = 190 if len(title) <= 22 else 300
        rt = 110 + ch + 30
        body = f"""<div class="abs" style="inset:0;background:linear-gradient(180deg,{P['m']} 0%,{P['d']} 100%)"></div><div class="abs" style="inset:0;{grid}"></div>
<div class="abs" style="left:20px;top:80px;transform:scale(.92);transform-origin:left top">{svg}</div>
<div class="abs" style="left:560px;top:110px;width:620px;height:{ch}px;background:{P['p']};border-radius:24px;box-shadow:0 20px 50px rgba(0,0,0,.35)"></div>
<div class="abs" style="left:560px;top:110px;width:620px;height:12px;border-radius:24px 24px 0 0;background:{P['a']}"></div>
<div class="abs" style="left:600px;top:150px;width:550px;color:{P['t']};font-weight:800;font-size:{min(tsize,58)}px;line-height:1.08">{H.escape(lead)} <span style="color:{P['h']}">{H.escape(hl)}</span></div>
<div class="abs" style="left:560px;top:{rt}px;width:620px;color:#fff;font-weight:700;font-size:34px;line-height:1.25">{H.escape(ribbon)}</div>
<div class="abs chips" style="left:560px;top:{rt+130 if ch>200 else rt+140}px">{chips_h.replace('<div>',f'<div style="background:{P["a"]};color:{P["d"]}">')}</div>
<div class="abs logo" style="right:30px;top:30px;color:#fff"><b style="background:{P['a']};color:{P['d']}">ib</b>instrumentationblog.in</div>"""
    return f"<!DOCTYPE html><html><head><meta charset='utf-8'><style>{CSS_BASE}</style></head><body><div class='w'>{body}</div></body></html>"

def render(out, title, ribbon, chips, topic, v=None):
    if v is None:
        v = int(hashlib.md5(title.encode()).hexdigest(), 16) % 24
    import os; out = os.path.abspath(out); htmlp = out.rsplit('.', 1)[0] + '.featimg.html'
    open(htmlp, 'w').write(page(title, ribbon, chips, topic, v))
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path='/usr/bin/google-chrome', args=['--no-sandbox'])
        pg = b.new_page(viewport={'width': 1200, 'height': 675}); pg.goto('file://' + htmlp); pg.wait_for_timeout(300)
        png = out.rsplit('.', 1)[0] + '.featimg.png'; pg.screenshot(path=png); b.close()
    Image.open(png).convert('RGB').save(out, 'WEBP', quality=82, method=6)

if __name__ == '__main__':
    a = sys.argv
    render(a[1], a[2], a[3], a[4].split(','), a[5], int(a[6]) if len(a) > 6 else None)
