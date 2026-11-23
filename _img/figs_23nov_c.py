import json, sys, os, math
sys.path.insert(0, '/home/claude/instrumentationblog-howitworks/_img')
from svglib import S
OUT = '/home/claude/instrumentationblog-howitworks/_img/changes'
CH = {}
WARN = []
_box = S.box
def _chk_box(self, x, y, w, h, lines, fill='#eef6ff', stroke='#1a2b4a', tc='#1a2b4a', size=18, bold_first=True, r=10):
    for ln in lines:
        if len(ln) * 0.55 * size > w - 14: WARN.append(('box', ln, w))
    if (len(lines) * (size + 6)) > h + 4: WARN.append(('boxh', lines[0], h))
    _box(self, x, y, w, h, lines, fill, stroke, tc, size, bold_first, r)
S.box = _chk_box
_dia = S.dia
def _chk_dia(self, cx, cy, w, h, lines, fill='#fff7e6', stroke='#1a2b4a', size=18):
    for ln in lines:
        if len(ln) * 0.58 * size > w * 0.62: WARN.append(('dia', ln, w))
    _dia(self, cx, cy, w, h, lines, fill, stroke, size)
S.dia = _chk_dia

def fig(slug, name, alt, caption, after, svg):
    CH.setdefault(slug, []).append(dict(name=name, alt=alt, caption=caption, after_h2=after, svg=svg))

def num(s, x, y, n, c, r=17):
    s.raw(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{c}"/>'); s.t(x, y + 6, str(n), 18, '#ffffff', 'bold')

# ================= 1. Pressure gauge accuracy classes =================
slug = 'pressure-gauge-accuracy-classes'
A, A2, L = '#4338ca', '#312e81', '#eef2ff'
s = S(520, 'Grade A pressure gauge dial with three accuracy zones on a 0 to 300 psi scale')
s.head('Three Zone Accuracy on a Grade A Gauge', A2)
cx, cy, r = 220, 285, 150
def P(f, rr):
    th = math.radians(225 - 270 * f); return cx + rr * math.cos(th), cy - rr * math.sin(th)
def arc(f1, f2, col, rr=r, wdt=30):
    x1, y1 = P(f1, rr); x2, y2 = P(f2, rr); large = 1 if (f2 - f1) * 270 > 180 else 0
    s.raw(f'<path d="M{x1:.1f} {y1:.1f} A{rr} {rr} 0 {large} 1 {x2:.1f} {y2:.1f}" fill="none" stroke="{col}" stroke-width="{wdt}"/>')
s.raw(f'<circle cx="{cx}" cy="{cy}" r="{r+30}" fill="#ffffff" stroke="#1a2b4a" stroke-width="3"/>')
arc(0, 0.25, '#f59e0b'); arc(0.25, 0.75, '#16a34a'); arc(0.75, 1, '#f59e0b')
for i, v in enumerate([0, 75, 150, 225, 300]):
    f = i / 4; xa, ya = P(f, r - 16); xb, yb = P(f, r + 16); s.ln(xa, ya, xb, yb, '#1a2b4a', 3)
    xt, yt = P(f, r - 42); s.t(xt, yt + 6, str(v), 17, '#1a2b4a', 'bold')
for f, lab in [(0.125, '2%'), (0.5, '1%'), (0.875, '2%')]:
    xt, yt = P(f, r - 80); s.t(xt, yt + 7, lab, 20, A2, 'bold')
xp, yp = P(0.62, r - 30); s.ln(cx, cy, xp, yp, '#dc2626', 5); s.raw(f'<circle cx="{cx}" cy="{cy}" r="10" fill="#1a2b4a"/>')
s.t(cx, cy + 70, 'psi', 18, '#4b5563', 'bold')
rows = [('#f59e0b', 'Lower 1/4: 0 to 75 psi', '2% of span = ±6 psi'),
        ('#16a34a', 'Middle 1/2: 75 to 225 psi', '1% of span = ±3 psi'),
        ('#f59e0b', 'Upper 1/4: 225 to 300 psi', '2% of span = ±6 psi')]
for i, (c, a, b) in enumerate(rows):
    y = 80 + i * 95
    s.raw(f'<rect x="440" y="{y}" width="330" height="80" rx="10" fill="#ffffff" stroke="{c}" stroke-width="3"/>')
    s.raw(f'<rect x="440" y="{y}" width="14" height="80" rx="4" fill="{c}"/>')
    s.t(468, y + 33, a, 18, '#1a2b4a', 'bold', 'start'); s.t(468, y + 60, b, 18, A2, 'normal', 'start')
s.box(440, 375, 330, 110, ['Compare: Grade 2A', 'one flat value, ±0.5% of span', '= ±1.5 psi everywhere'], L, A, size=18)
fig(slug, 'pressure-gauge-accuracy-classes-three-zone-dial-diagram',
    'Grade A pressure gauge dial with 2 1 2 percent accuracy zones on 300 psi scale',
    'Diagram by Instrumentation Blog showing how ASME B40.100 Grade A allows 2% of span in the lower and upper quarters and 1% in the middle half, compared with flat Grade 2A.',
    'Two Ways ASME B40.100 Defines Error', s.svg())

s = S(580, 'Pressure gauge accuracy grade selection flowchart by application')
s.head('Choosing a Pressure Gauge Accuracy Grade', A2)
qs = [(['Test gauge or', 'calibration standard?'], 'Grade 3A or 4A', '4A needs 8.5 in dial'),
      (['Critical process or', 'custody transfer?'], 'Grade 2A', '±0.5% of span'),
      (['General process', 'monitoring?'], 'Grade 1A or A', 'balance of cost and accuracy')]
y = 62
for i, (q, ans, why) in enumerate(qs):
    s.dia(210, y + 50, 320, 96, q, L, size=17)
    s.ar(372, y + 50, 440, y + 50, A); s.t(405, y + 40, 'Yes', 17, A2, 'bold')
    s.box(445, y + 15, 325, 70, [ans, why], '#ffffff', A, size=18)
    s.ar(210, y + 99, 210, y + 114); s.t(232, y + 112, 'No', 17, '#4b5563', 'bold')
    y += 116
s.box(60, y, 300, 66, ['Grade B, C or D', 'utility, non critical use'], '#ffffff', A, size=18)
s.box(40, 488, 720, 84, ['Then check the real error in psi or bar', 'Friction error and about ±0.3% of span per 18 °F away from 23 °C', 'sit outside the grade rating'], '#fef3c7', '#b45309', size=17)
s.ar(210, y + 68, 210, 486, '#b45309')
fig(slug, 'pressure-gauge-accuracy-classes-grade-selection-flowchart',
    'flowchart for choosing ASME B40.100 pressure gauge accuracy grade by application',
    'Diagram by Instrumentation Blog showing how to pick Grade 4A or 3A for test gauges, 2A for critical process, 1A or A for general use and B, C or D for utility service.',
    'Choosing the Right Accuracy Grade for the Application', s.svg())

s = S(560, 'Pressure gauge permissible error formula with Grade 2A worked example and grade list')
s.head('Percent of Span Formula and Worked Example', A2)
s.box(40, 58, 720, 70, ['Allowable Error = (Grade % / 100) × Full Scale Span'], A, A, '#ffffff', 22)
st = [('Gauge', '4.5 inch dial, Grade 2A'), ('Range', '0 to 300 psi, span = 300 psi'),
      ('Calculate', '(0.5 / 100) × 300 psi'), ('Result', '±1.5 psi at any point on the dial')]
for i, (k, v) in enumerate(st):
    y = 145 + i * 50
    num(s, 64, y + 20, i + 1, A)
    s.t(95, y + 27, k, 19, A2, 'bold', 'start'); s.t(215, y + 27, v, 19, '#1a2b4a', 'normal', 'start')
s.t(400, 370, 'ASME B40.100 grades, % of span (lower / middle / upper)', 18, '#1a2b4a', 'bold')
gr = [('4A', '0.1'), ('3A', '0.25'), ('2A', '0.5'), ('1A', '1.0'), ('A', '2 / 1 / 2'), ('B', '3 / 2 / 3'), ('C', '4 / 3 / 4'), ('D', '5 / 5 / 5')]
for i, (g, v) in enumerate(gr):
    x = 40 + (i % 4) * 182; y = 390 + (i // 4) * 82
    hl = g == '2A'
    s.raw(f'<rect x="{x}" y="{y}" width="170" height="70" rx="10" fill="{A if hl else L}" stroke="{A}" stroke-width="2"/>')
    s.t(x + 85, y + 30, 'Grade ' + g, 19, '#ffffff' if hl else A2, 'bold'); s.t(x + 85, y + 56, v + ' %', 18, '#ffffff' if hl else '#1a2b4a')
fig(slug, 'pressure-gauge-accuracy-classes-percent-of-span-infographic',
    'pressure gauge accuracy classes formula card with Grade 2A 0 to 300 psi example',
    'Diagram by Instrumentation Blog showing the percent of span formula, the Grade 2A example of 0.5% of 300 psi giving 1.5 psi, and all eight ASME grades.',
    'Percent of Span Formula and Worked Example', s.svg())

# ================= 2. Pressure tappings in orifice plate =================
slug = 'pressure-tappings-in-orifice-plate'
A, A2, L = '#0f766e', '#134e4a', '#f0fdfa'
s = S(580, 'Pressure tapping locations for flange, corner, radius, vena contracta and pipe taps')
s.head('Where Each Orifice Pressure Tap Is Located', A2)
PX, D = 320, 50
rows = [('Flange taps', [(-14, ''), (14, '')], '1 inch each side'),
        ('Corner taps', [(-5, ''), (5, '')], 'at the plate faces'),
        ('Radius taps', [(-D, '1D'), (D / 2, '0.5D')], ''),
        ('Vena contracta', [(-D, '1D'), (D / 2, 'min pressure')], ''),
        ('Pipe taps', [(-2.5 * D, '2.5D'), (8 * D, '8D')], '')]
for i, (nm, taps, note) in enumerate(rows):
    y = 100 + i * 82
    s.t(20, y + 22, nm, 18, A2, 'bold', 'start')
    s.raw(f'<rect x="185" y="{y+8}" width="550" height="26" fill="{L}" stroke="#1a2b4a" stroke-width="2"/>')
    s.raw(f'<rect x="{PX-3}" y="{y}" width="6" height="16" fill="#1a2b4a"/><rect x="{PX-3}" y="{y+26}" width="6" height="16" fill="#1a2b4a"/>')
    for k, (dx, lab) in enumerate(taps):
        x = PX + dx; c = '#2563eb' if k == 0 else '#dc2626'
        s.ln(x, y + 8, x, y - 6, c, 3); s.raw(f'<circle cx="{x}" cy="{y-8}" r="5" fill="{c}"/>')
        if lab: s.t(x, y + 58, lab, 17, c, 'bold')
    if note: s.t(PX + 40, y + 58, note, 17, '#1a2b4a', 'bold', 'start')
s.ar(200, 84, 270, 84, A); s.t(235, 74, 'Flow', 17, A2, 'bold')
s.ar(PX, 500, PX, 474, '#1a2b4a'); s.t(PX, 520, 'orifice plate', 17, '#1a2b4a', 'bold')
s.raw(f'<circle cx="440" cy="528" r="6" fill="#2563eb"/>'); s.t(454, 534, 'High pressure tap', 17, '#1a2b4a', 'normal', 'start')
s.raw(f'<circle cx="610" cy="528" r="6" fill="#dc2626"/>'); s.t(624, 534, 'Low pressure tap', 17, '#1a2b4a', 'normal', 'start')
s.t(20, 534, 'D = pipe inside dia.', 17, '#4b5563', 'normal', 'start')
s.t(400, 565, 'Elbow taps need no plate: pressure is taken across a pipe elbow', 17, '#4b5563')
fig(slug, 'pressure-tappings-in-orifice-plate-tap-locations-diagram',
    'pressure tappings in orifice plate locations for flange, corner, radius, vena contracta and pipe taps',
    'Diagram by Instrumentation Blog showing tap positions: flange taps 1 inch each side, corner taps at the faces, radius taps 1D and 0.5D, pipe taps 2.5D and 8D.',
    'Types of Pressure Tappings in Orifice Plate', s.svg())

s = S(560, 'Orifice plate pressure tapping selection flowchart by pipe size and accuracy')
s.head('How to Select an Orifice Pressure Tapping', A2)
s.box(250, 58, 300, 56, ['Know pipe size, standard, accuracy'], L, A, size=17)
s.ar(400, 116, 400, 136, A)
s.dia(400, 192, 300, 108, ['Pipe below', '2 inches?'], L, size=18)
s.ar(552, 192, 590, 192, A); s.t(570, 180, 'Yes', 17, A2, 'bold')
s.box(595, 157, 180, 70, ['Corner taps', 'at plate faces'], '#ffffff', A, size=17)
s.ar(400, 248, 400, 268, A); s.t(422, 264, 'No', 17, '#4b5563', 'bold')
s.dia(400, 330, 300, 116, ['Above 6 inches and', 'high accuracy?'], L, size=17)
s.ar(552, 330, 590, 330, A); s.t(570, 318, 'Yes', 17, A2, 'bold')
s.box(595, 295, 180, 70, ['Radius taps', '1D and 0.5D'], '#ffffff', A, size=17)
s.pl([(248, 330), (140, 330), (140, 380)], A); s.t(195, 318, 'No', 17, '#4b5563', 'bold')
s.box(30, 385, 220, 70, ['Flange taps', '1 inch each side'], '#ffffff', A, size=17)
s.box(290, 410, 480, 120, ['Before you finalise', 'ISO 5167: tap type must match the constants', 'Changing tap type changes the discharge', 'coefficient, so recalculate the flow'], '#fef3c7', '#b45309', size=17)
s.ar(252, 430, 288, 450, '#b45309')
fig(slug, 'pressure-tappings-in-orifice-plate-selection-flowchart',
    'flowchart to select corner, radius or flange pressure taps by pipe size and accuracy',
    'Diagram by Instrumentation Blog showing how pipe size and accuracy decide between corner, radius and flange taps, and why a change of tap type needs a new flow calculation.',
    'How to Select the Right Pressure Tapping?', s.svg())

s = S(560, 'Comparison of six orifice pressure tapping types infographic')
s.head('Comparison of Orifice Pressure Tappings', A2)
cards = [('Flange taps', '1 inch upstream and downstream', 'most common, well standardised'),
         ('Corner taps', 'at upstream and downstream faces', 'best for small pipes below 2 in'),
         ('Radius taps', '1D upstream, 0.5D downstream', '6 inch and larger lines'),
         ('Vena contracta taps', '1D upstream, min pressure point', 'maximum DP, less standardised'),
         ('Pipe taps', '2.5D upstream, 8D downstream', 'older design, more variation'),
         ('Elbow taps', 'outer and inner wall of an elbow', 'low cost, lower accuracy')]
for i, (h, a, b) in enumerate(cards):
    x = 30 + (i % 2) * 380; y = 62 + (i // 2) * 162
    s.raw(f'<rect x="{x}" y="{y}" width="360" height="146" rx="12" fill="{L if i in (0,3,4) else "#ffffff"}" stroke="{A}" stroke-width="2"/>')
    num(s, x + 32, y + 34, i + 1, A)
    s.t(x + 60, y + 41, h, 20, A2, 'bold', 'start')
    s.t(x + 20, y + 84, a, 17, '#1a2b4a', 'normal', 'start')
    s.t(x + 20, y + 118, b, 17, '#4b5563', 'bold', 'start')
fig(slug, 'pressure-tappings-in-orifice-plate-comparison-infographic',
    'comparison of pressure tapping types with location and best use for each',
    'Diagram by Instrumentation Blog comparing flange, corner, radius, vena contracta, pipe and elbow taps by tap location and where each type is best used.',
    'Comparison of Pressure Tappings in Orifice Plate', s.svg())

# ================= 3. SCADA communication problems =================
slug = 'scada-communication-problems'
A, A2, L = '#be123c', '#881337', '#fff1f2'
s = S(560, 'SCADA network diagram showing where common communication problems occur')
s.head('Where SCADA Communication Problems Happen', A2)
s.box(30, 80, 170, 70, ['PLC 1', 'fixed IP'], L, A, size=18)
s.box(30, 200, 170, 70, ['PLC 2', 'Modbus master'], L, A, size=18)
s.box(290, 140, 190, 70, ['Industrial switch', 'automation VLAN'], '#ffffff', A, size=17)
s.box(560, 80, 210, 80, ['SCADA server', 'driver, tags, historian'], L, A, size=17)
s.box(560, 200, 95, 56, ['UPS'], '#ffffff', A, size=18)
s.box(675, 200, 95, 56, ['Firewall'], '#ffffff', A, size=17)
s.box(560, 300, 95, 66, ['Client', 'PC 1'], '#ffffff', A, size=17)
s.box(675, 300, 95, 66, ['Client', 'PC 2'], '#ffffff', A, size=17)
s.pl([(200, 115), (245, 115), (245, 165), (290, 165)], '#1a2b4a', 3, arrow=False)
s.pl([(200, 235), (245, 235), (245, 185), (290, 185)], '#1a2b4a', 3, arrow=False)
s.pl([(480, 175), (520, 175), (520, 120), (560, 120)], '#1a2b4a', 3, arrow=False)
s.ln(607, 160, 607, 200, '#1a2b4a', 3); s.ln(722, 160, 722, 200, '#1a2b4a', 3)
s.ln(722, 256, 722, 300, '#1a2b4a', 3); s.pl([(722, 280), (607, 280), (607, 300)], '#1a2b4a', 3, arrow=False)
# RS485 bus
s.ln(115, 270, 115, 420, '#1a2b4a', 3)
s.ln(60, 420, 470, 420, '#7c3aed', 4); s.t(80, 448, 'RS 485 bus, A and B', 17, '#7c3aed', 'bold', 'start')
for x, lab in [(230, 'ID 1'), (360, 'ID 2')]:
    s.ln(x, 420, x, 385, '#7c3aed', 3); s.box(x - 48, 340, 96, 46, ['Slave ' + lab], '#f5f3ff', '#7c3aed', size=17)
s.raw('<rect x="470" y="405" width="40" height="30" fill="#ffffff" stroke="#7c3aed" stroke-width="2.5"/>'); s.t(490, 466, 'end resistor', 17, '#7c3aed', 'bold')
# problem badges
for x, y, n in [(222, 90, 1), (385, 126, 2), (30, 80, 5), (142, 320, 6), (750, 200, 7), (560, 200, 9), (770, 80, 4)]:
    num(s, x, y, n, A, 15)
s.box(560, 400, 210, 150, ['Problem numbers', '1, 2 cable or switch', '4 timeout, polling', '5 duplicate IP', '6 Modbus settings', '7 firewall, 9 no UPS'], '#ffffff', A, size=17, bold_first=True)
fig(slug, 'scada-communication-problems-network-map-diagram',
    'SCADA network diagram with PLC, switch, server, firewall, clients and Modbus RS 485 bus',
    'Diagram by Instrumentation Blog mapping common SCADA communication problems to the network: cables and switch, IP conflicts, Modbus settings, timeouts, firewall ports and missing UPS.',
    '1. SCADA Is Not Updating Values from PLC', s.svg())

s = S(590, 'SCADA communication troubleshooting flowchart: network first, PLC second, SCADA last')
s.head('Troubleshooting Order: Network, PLC, SCADA', A2)
s.box(200, 55, 300, 54, ['Values frozen or bad quality'], A, A, '#ffffff', 18)
s.ar(350, 111, 350, 130, A)
s.dia(350, 182, 300, 100, ['Ping the PLC IP', 'OK from SCADA PC?'], L, size=17)
s.ar(502, 182, 545, 182, A); s.t(522, 170, 'No', 17, A2, 'bold')
s.box(550, 140, 230, 84, ['Network first', 'cable, switch LEDs,', 'duplicate IP'], '#ffffff', A, size=17)
s.ar(350, 232, 350, 254, A); s.t(372, 250, 'Yes', 17, '#4b5563', 'bold')
s.dia(350, 306, 300, 100, ['Raw PLC value', 'equals SCADA tag?'], L, size=17)
s.ar(502, 306, 545, 306, A); s.t(522, 294, 'No', 17, A2, 'bold')
s.box(550, 264, 230, 84, ['PLC second', 'register map, tag', 'address, scaling'], '#ffffff', A, size=17)
s.ar(350, 356, 350, 378, A); s.t(372, 374, 'Yes', 17, '#4b5563', 'bold')
s.dia(350, 430, 300, 100, ['Only client', 'PCs fail?'], L, size=17)
s.ar(502, 430, 545, 430, A); s.t(522, 418, 'Yes', 17, A2, 'bold')
s.box(550, 388, 230, 84, ['Firewall ports,', 'OPC security,', 'client licensing'], '#ffffff', A, size=17, bold_first=False)
s.ar(350, 480, 350, 500, A); s.t(372, 496, 'No', 17, '#4b5563', 'bold')
s.box(150, 503, 400, 74, ['SCADA last', 'driver, timeout, polling rate, tags'], '#fef3c7', '#b45309', size=17)
s.t(20, 190, 'Step 1', 18, A2, 'bold', 'start'); s.t(20, 314, 'Step 2', 18, A2, 'bold', 'start'); s.t(20, 438, 'Step 3', 18, A2, 'bold', 'start')
fig(slug, 'scada-communication-problems-troubleshooting-flowchart',
    'SCADA communication problems troubleshooting flowchart checking network, then PLC, then SCADA',
    'Diagram by Instrumentation Blog showing the field rule for SCADA faults: ping and check the network first, compare raw PLC values second, then check client and SCADA settings last.',
    'Most Common Root Causes of SCADA Communication Problems (From Field Experience)', s.svg())

s = S(500, 'SCADA shows wrong value while PLC is correct: 50 bar vs 35 bar checks')
s.head('PLC Shows 50 bar, SCADA Shows 35 bar', A2)
for x, lab, v, c in [(60, 'PLC value', '50 bar', '#16a34a'), (480, 'SCADA screen', '35 bar', A)]:
    s.raw(f'<rect x="{x}" y="70" width="260" height="120" rx="14" fill="#111827" stroke="{c}" stroke-width="4"/>')
    s.t(x + 130, 108, lab, 18, '#e5e7eb', 'bold'); s.t(x + 130, 162, v, 36, c, 'bold')
s.ar(325, 130, 474, 130, A, 3, '8 5'); s.t(400, 118, 'tag', 17, A2, 'bold')
s.t(400, 222, 'Raw PLC value is correct, so the error is in SCADA mapping', 18, '#1a2b4a', 'bold')
chk = [('Verify PLC register mapping', 'tag linked to the right memory address'),
       ('Recheck the scaling formula', 'same engineering unit range both sides'),
       ('Compare raw vs displayed value', 'not only the final engineering value')]
for i, (h, d) in enumerate(chk):
    y = 248 + i * 80
    s.raw(f'<rect x="60" y="{y}" width="680" height="68" rx="10" fill="{L}" stroke="{A}" stroke-width="2"/>')
    num(s, 95, y + 34, i + 1, A)
    s.t(128, y + 28, h, 19, A2, 'bold', 'start'); s.t(128, y + 54, d, 17, '#1a2b4a', 'normal', 'start')
fig(slug, 'scada-communication-problems-wrong-value-check-infographic',
    'SCADA showing 35 bar while PLC shows 50 bar with scaling and address checks',
    'Diagram by Instrumentation Blog showing the wrong value case where the PLC reads 50 bar but SCADA shows 35 bar, and the mapping, scaling and raw value checks that find it.',
    '3. SCADA Shows Wrong Values (But PLC Is Correct)', s.svg())

# ================= 4. Strainer and filter =================
slug = 'strainer-and-filter-difference'
A, A2, L = '#15803d', '#14532d', '#f0fdf4'
s = S(520, 'Pipeline with strainer before the pump and filter with differential pressure gauge before equipment')
s.head('Where a Strainer and a Filter Go in a Line', A2)
Y = 200
s.raw(f'<rect x="25" y="110" width="90" height="140" rx="8" fill="#e0f2fe" stroke="#1a2b4a" stroke-width="2.5"/>'); s.t(70, 275, 'Tank', 18, '#1a2b4a', 'bold')
s.ln(115, Y, 170, Y, '#1a2b4a', 5)
s.raw(f'<rect x="170" y="{Y-45}" width="90" height="90" rx="8" fill="{L}" stroke="{A}" stroke-width="3"/>')
for k in range(6): s.ln(185 + k * 12, Y - 30, 185 + k * 12, Y + 30, A, 2)
s.t(215, Y - 58, 'Strainer', 18, A2, 'bold')
s.ln(260, Y, 320, Y, '#1a2b4a', 5)
s.raw(f'<circle cx="355" cy="{Y}" r="35" fill="#ffffff" stroke="#1a2b4a" stroke-width="3"/>'); s.raw(f'<polygon points="340,{Y-18} 375,{Y} 340,{Y+18}" fill="#1a2b4a"/>')
s.t(355, Y + 60, 'Pump', 18, '#1a2b4a', 'bold')
s.ln(390, Y, 460, Y, '#1a2b4a', 5)
s.raw(f'<rect x="460" y="{Y-55}" width="80" height="110" rx="14" fill="#ffffff" stroke="#b45309" stroke-width="3"/>')
s.raw(f'<rect x="482" y="{Y-40}" width="36" height="80" rx="4" fill="#fde68a" stroke="#b45309" stroke-width="2"/>')
s.t(500, Y + 80, 'Filter', 18, '#92400e', 'bold')
s.ln(540, Y, 640, Y, '#1a2b4a', 5)
s.pl([(445, Y), (445, 95), (480, 95)], '#1a2b4a', 2, arrow=False); s.pl([(555, Y), (555, 95), (520, 95)], '#1a2b4a', 2, arrow=False)
s.raw('<circle cx="500" cy="95" r="22" fill="#ffffff" stroke="#1a2b4a" stroke-width="2.5"/>'); s.t(500, 101, 'DP', 17, '#1a2b4a', 'bold')
s.t(590, 88, 'DP gauge', 17, '#1a2b4a', 'bold', 'start')
s.raw('<rect x="640" y="150" width="140" height="100" rx="10" fill="#e5e7eb" stroke="#1a2b4a" stroke-width="2.5"/>')
s.t(710, 192, 'Hydraulic or', 17, '#1a2b4a', 'bold'); s.t(710, 216, 'precision use', 17, '#1a2b4a', 'bold')
for x in (140, 290, 425, 600): s.raw(f'<polygon points="{x-8},{Y-8} {x+6},{Y} {x-8},{Y+8}" fill="{A}"/>')
s.box(30, 310, 360, 190, ['Strainer: protects equipment', 'metal screen or perforated plate', 'stops particles over 75 to 100 µm', 'low pressure drop', 'cleaned and reused'], L, A, size=17)
s.box(410, 310, 360, 190, ['Filter: cleans the fluid', 'paper, fiber, sintered metal', 'down to 25, 10, 5 µm or less', 'higher pressure drop, DP alarm', 'element often replaced'], '#fffbeb', '#b45309', size=17)
fig(slug, 'strainer-and-filter-pipeline-location-diagram',
    'strainer before a pump and filter with DP gauge before hydraulic equipment in a pipeline',
    'Diagram by Instrumentation Blog showing a strainer protecting the pump from large debris and a fine filter with a DP gauge cleaning the fluid before precision equipment.',
    'Difference in Purpose', s.svg())

s = S(540, 'Strainer or filter selection flowchart with common selection mistakes')
s.head('Strainer or Filter? A Simple Selection Flow', A2)
s.dia(400, 120, 380, 110, ['Goal is to protect equipment', 'from large debris?'], L, size=17)
s.pl([(210, 120), (105, 120), (105, 145)], A); s.t(160, 108, 'Yes', 17, A2, 'bold')
s.box(20, 150, 170, 66, ['Use a strainer', 'low pressure drop'], '#ffffff', A, size=17)
s.ar(400, 177, 400, 200, A); s.t(420, 195, 'No', 17, '#4b5563', 'bold')
s.dia(400, 258, 380, 110, ['Fine particles cause wear,', 'blockage or errors?'], '#fffbeb', size=17)
s.pl([(590, 258), (680, 258), (680, 320)], '#b45309'); s.t(640, 246, 'Yes', 17, '#92400e', 'bold')
s.box(590, 325, 180, 70, ['Use a filter', 'add a DP alarm'], '#ffffff', '#b45309', size=17)
s.ar(400, 315, 400, 338, A); s.t(420, 333, 'No', 17, '#4b5563', 'bold')
s.box(260, 342, 280, 56, ['A strainer is enough'], '#ffffff', A, size=17)
s.box(30, 420, 360, 100, ['Mistake 1', 'strainer where a filter is needed:', 'wear, valve sticking'], '#fee2e2', '#b91c1c', size=17)
s.box(410, 420, 360, 100, ['Mistake 2', 'fine filter where a strainer is', 'enough: pressure loss, cost'], '#fee2e2', '#b91c1c', size=17)
fig(slug, 'strainer-and-filter-selection-flowchart',
    'strainer and filter selection flowchart by equipment protection or fluid cleanliness goal',
    'Diagram by Instrumentation Blog showing the field rule: use a strainer for equipment protection, a filter when fine particles matter, and the two common selection mistakes.',
    'Common Selection Mistakes', s.svg())

s = S(480, 'Particle size removal range of strainer and filter on a micron scale')
s.head('Particle Size: Strainer vs Filter', A2)
x0, x1 = 80, 740
def X(v): return x0 + (math.log10(v) + 1) * (x1 - x0) / 4
s.ln(x0, 250, x1, 250, '#1a2b4a', 3)
for v, lab in [(0.1, '0.1'), (1, '1'), (5, '5'), (10, '10'), (25, '25'), (100, '100'), (1000, '1000')]:
    s.ln(X(v), 242, X(v), 258, '#1a2b4a', 2.5); s.t(X(v), 282, lab, 17, '#1a2b4a', 'bold')
s.t(410, 312, 'Particle size in microns (log scale)', 18, '#1a2b4a', 'bold')
s.raw(f'<rect x="{X(0.1):.0f}" y="170" width="{X(25)-X(0.1):.0f}" height="50" rx="8" fill="#f59e0b"/>')
s.t((X(0.1) + X(25)) / 2, 202, 'Filter ratings: 25 µm to sub micron', 18, '#ffffff', 'bold')
s.raw(f'<rect x="{X(75):.0f}" y="100" width="{x1-X(75):.0f}" height="50" rx="8" fill="{A}"/>')
s.t((X(75) + x1) / 2, 132, 'Strainer', 18, '#ffffff', 'bold')
s.ln(X(75), 150, X(75), 242, A, 2, '6 4'); s.t(X(75) - 6, 92, 'catches over 75 to 100 µm', 17, A2, 'bold', 'end')
tiles = [('Element', 'screen vs fine media'), ('Pressure drop', 'low vs higher'), ('Maintenance', 'clean vs replace')]
for i, (h, d) in enumerate(tiles):
    x = 40 + i * 245
    s.box(x, 345, 230, 100, [h, d], L if i % 2 == 0 else '#fffbeb', A, size=18)
fig(slug, 'strainer-and-filter-particle-size-infographic',
    'strainer and filter particle size removal range in microns on a log scale',
    'Diagram by Instrumentation Blog comparing particle size removal: strainers stop particles above about 75 to 100 microns while filters remove 25, 10, 5 microns and sub micron particles.',
    'Difference in Particle Size Removal', s.svg())

# ================= 5. 2oo3 voting logic =================
slug = 'what-is-2oo3-voting-logic'
A, A2, L = '#7c3aed', '#4c1d95', '#f5f3ff'
s = S(500, '2oo3 voting logic with three pressure transmitters, 100 bar trip comparators and voter')
s.head('2oo3 Voting with a 100 bar Trip Setting', A2)
pts = [('PT1', '105 bar', 'HIGH', '1', '#dc2626'), ('PT2', '103 bar', 'HIGH', '1', '#dc2626'), ('PT3', '92 bar', 'NORMAL', '0', '#16a34a')]
for i, (n, v, st_, b, c) in enumerate(pts):
    y = 80 + i * 120
    s.box(30, y, 150, 80, [n, v], L, A, size=19)
    s.ar(182, y + 40, 228, y + 40, A)
    s.box(232, y, 180, 80, ['Above 100 bar?', st_], '#ffffff', c, size=18)
    s.ar(414, y + 40, 471, 240 + (i - 1) * 40, A)
    s.t(436, y + 28 if i == 0 else (y + 30 if i == 1 else y + 68), b, 20, c, 'bold')
s.box(475, 180, 140, 120, ['2oo3', 'voter', '2 of 3 high'], A, A, '#ffffff', 19)
s.ar(617, 240, 650, 240, '#dc2626')
s.box(655, 190, 125, 100, ['TRIP', 'shutdown'], '#fee2e2', '#dc2626', '#b91c1c', 20)
s.box(30, 430, 750, 54, ['Two transmitters agree on high pressure, so the condition is real and the system trips'], '#fef3c7', '#b45309', size=17, bold_first=False)
fig(slug, '2oo3-voting-logic-transmitter-voter-diagram',
    '2oo3 voting logic diagram with three transmitters tripping at 100 bar',
    'Diagram by Instrumentation Blog showing three pressure transmitters compared with a 100 bar trip setting, where two high readings make the 2oo3 voter trip the plant.',
    'How 2oo3 Voting Logic works in real systems', s.svg())

s = S(540, '2oo3 voting logic decision flowchart counting transmitters above the trip setting')
s.head('How a 2oo3 Voter Decides', A2)
s.box(200, 58, 400, 56, ['PT1, PT2, PT3 measure the same pressure'], L, A, size=17, bold_first=False)
s.ar(400, 116, 400, 138, A)
s.box(200, 140, 400, 56, ['Compare each reading with the trip setting'], L, A, size=17, bold_first=False)
s.ar(400, 198, 400, 220, A)
s.dia(400, 280, 340, 116, ['How many above', 'the setting?'], '#ffffff', size=18)
s.pl([(230, 280), (130, 280), (130, 360)], A); s.t(175, 268, '0', 20, A2, 'bold')
s.ar(400, 338, 400, 360, A); s.t(418, 356, '1', 20, A2, 'bold')
s.pl([(570, 280), (670, 280), (670, 360)], '#dc2626'); s.t(625, 268, '2 or 3', 18, '#b91c1c', 'bold')
s.box(30, 365, 200, 90, ['Normal', 'keep running'], '#dcfce7', '#16a34a', size=18)
s.box(285, 365, 230, 90, ['Ignore it', 'one faulty sensor', 'cannot trip'], '#fef3c7', '#b45309', size=17)
s.box(570, 365, 200, 90, ['Real condition', 'system trips'], '#fee2e2', '#dc2626', '#b91c1c', 18)
s.t(400, 500, 'Fewer false trips, and one sensor can be under maintenance', 18, A2, 'bold')
fig(slug, '2oo3-voting-logic-trip-decision-flowchart',
    '2oo3 voting logic flowchart showing no trip for one high sensor and trip for two',
    'Diagram by Instrumentation Blog showing the 2oo3 decision: no high readings keep running, one high reading is ignored as a faulty sensor, and two or three high readings trip.',
    'Key understanding of 2oo3 Voting Logic', s.svg())

s = S(580, '2oo3 voting logic truth table for three sensors')
s.head('2oo3 Truth Table (1 = sensor above trip)', A2)
cols = [('PT1', 70), ('PT2', 160), ('PT3', 250), ('High votes', 360), ('Action', 480)]
s.raw(f'<rect x="30" y="58" width="500" height="44" rx="6" fill="{A}"/>')
for h, x in cols: s.t(x, 87, h, 18, '#ffffff', 'bold')
for i in range(8):
    a, b, c = (i >> 2) & 1, (i >> 1) & 1, i & 1; v = a + b + c; y = 102 + i * 54
    trip = v >= 2
    s.raw(f'<rect x="30" y="{y}" width="500" height="54" fill="{"#fee2e2" if trip else ("#ffffff" if i % 2 else L)}" stroke="#ddd6fe" stroke-width="1.5"/>')
    for val, (h, x) in zip([a, b, c, v], cols): s.t(x, y + 34, str(val), 19, '#1a2b4a', 'bold')
    s.t(480, y + 34, 'TRIP' if trip else 'no trip', 18, '#b91c1c' if trip else '#4b5563', 'bold')
s.box(555, 102, 225, 130, ['One sensor fails', 'the other two', 'still decide'], L, A, size=17)
s.box(555, 250, 225, 130, ['Two agree', 'the system', 'takes action'], '#fee2e2', '#dc2626', size=17)
s.box(555, 398, 225, 130, ['Used in', 'ESD, BMS, HIPPS,', 'reactor protection'], '#ffffff', A, size=17)
fig(slug, '2oo3-voting-logic-truth-table-infographic',
    '2oo3 voting logic truth table showing trip when two or three sensors are high',
    'Diagram by Instrumentation Blog listing all eight 2oo3 sensor combinations, with a trip only when two or three of the three transmitters are above the trip setting.',
    'Understanding 2oo3 Voting Logic in simple terms', s.svg())

# ================= 6. Sensor linearity =================
slug = 'what-is-sensor-linearity'
A, A2, L = '#0369a1', '#0c4a6e', '#f0f9ff'
s = S(520, 'Sensor linearity error as maximum deviation of real output from best fit straight line')
s.head('Sensor Linearity Error from a Reference Line', A2)
gx0, gy0, gx1, gy1 = 100, 440, 520, 70
s.ln(gx0, gy0, gx1 + 10, gy0, '#1a2b4a', 2.5); s.ln(gx0, gy0, gx0, gy1 - 10, '#1a2b4a', 2.5)
s.t(310, 480, 'Input (0 to 100 % of range)', 18, '#1a2b4a', 'bold')
s.raw(f'<text x="45" y="255" font-size="18" fill="#1a2b4a" font-weight="bold" text-anchor="middle" transform="rotate(270 45 255)">Output</text>')
def G(u, o): return gx0 + u * (gx1 - gx0), gy0 - o * (gy0 - gy1)
s.ln(*G(0, 0.0), *G(1, 1.0), A, 3, '9 6')
pts = []
for k in range(41):
    u = k / 40; o = u + 0.1 * math.sin(2 * math.pi * u)
    pts.append(G(u, o))
s.pl(pts, '#dc2626', 3.5, arrow=False)
for k in range(0, 41, 8): s.raw(f'<circle cx="{pts[k][0]:.1f}" cy="{pts[k][1]:.1f}" r="6" fill="#dc2626"/>')
xa, ya = G(0.25, 0.25); xb, yb = G(0.25, 0.35)
s.ln(xa, ya, xb, yb, '#1a2b4a', 2.5); s.raw(f'<line x1="{xb}" y1="{yb}" x2="{xa}" y2="{ya}" stroke="#1a2b4a" stroke-width="2.5" marker-end="url(#ah)" marker-start="url(#ah)"/>')
s.t(xa + 12, (ya + yb) / 2 + 30, 'max deviation', 17, '#1a2b4a', 'bold', 'start')
s.box(560, 80, 220, 90, ['Dashed line', 'best fit straight', 'line (BFSL)'], L, A, size=17)
s.box(560, 190, 220, 90, ['Red curve', 'actual sensor', 'output points'], '#fee2e2', '#dc2626', size=17)
s.box(560, 300, 220, 130, ['Linearity error', 'largest deviation', 'from the line, as', '± % of FSO'], '#ffffff', A, size=17)
fig(slug, 'sensor-linearity-error-best-fit-line-diagram',
    'sensor linearity graph with actual output curve, best fit straight line and maximum deviation',
    'Diagram by Instrumentation Blog showing sensor linearity error as the largest deviation between the real output curve and the best fit straight line over the full input range.',
    'What Is Sensor Linearity Error or Non-Linearity?', s.svg())

s = S(590, 'Sensor linearity test and specification flowchart')
s.head('How Sensor Linearity Is Tested and Specified', A2)
steps = [['Apply known inputs', 'across the full range'], ['Record the output', 'at each point'],
         ['Choose a reference line', 'end point, zero based or BFSL'], ['Fit BFSL by least squares', 'balances plus and minus deviations'],
         ['Find the largest deviation', 'from that line']]
for i, ls in enumerate(steps):
    y = 56 + i * 82
    s.box(200, y, 400, 66, ls, L if i % 2 == 0 else '#ffffff', A, size=17)
    num(s, 170, y + 33, i + 1, A)
    s.ar(400, y + 68, 400, y + 80, A) if i < 4 else None
s.ar(400, 446, 400, 458, A)
s.dia(400, 500, 280, 80, ['Unipolar output?'], '#fef3c7', size=17)
s.pl([(260, 500), (130, 500), (130, 530)], A); s.t(195, 490, 'Yes', 17, A2, 'bold')
s.pl([(540, 500), (670, 500), (670, 530)], A); s.t(605, 490, 'No', 17, A2, 'bold')
s.box(20, 532, 220, 50, ['± % of FSO'], '#ffffff', A, size=18)
s.box(560, 532, 220, 50, ['± % of FRO'], '#ffffff', A, size=18)
fig(slug, 'sensor-linearity-test-and-specification-flowchart',
    'flowchart for testing sensor linearity with best fit straight line and FSO or FRO rating',
    'Diagram by Instrumentation Blog showing how linearity is tested: apply known inputs, record outputs, fit a reference line, find the largest deviation, then quote it as % of FSO or FRO.',
    'How Sensor Linearity Is Specified', s.svg())

s = S(520, 'Sensor linearity worked example: 0 to 2 inch sensor, 0 to 10 V, 0.25 percent FSO')
s.head('Sensor Linearity Worked Example', A2)
given = [('Range', '0 to 2 inches'), ('Output', '0 to 10 V DC'), ('Linearity', '±0.25 % of FSO')]
for i, (k, v) in enumerate(given):
    x = 30 + i * 252
    s.box(x, 58, 236, 84, [k, v], L, A, size=19)
st = [('Full Scale Output', '10 V'), ('Linearity error', '0.25 % × 10 V = ±25 mV'),
      ('Scale factor', '10 V / 2 in = 5 V per inch'), ('Displacement error', '25 mV / 5 V per inch = ±0.005 in')]
for i, (k, v) in enumerate(st):
    y = 165 + i * 72
    s.raw(f'<rect x="30" y="{y}" width="740" height="60" rx="10" fill="{"#ffffff" if i < 3 else A}" stroke="{A}" stroke-width="2"/>')
    num(s, 64, y + 30, i + 1, A if i < 3 else '#0c4a6e')
    c1 = A2 if i < 3 else '#ffffff'; c2 = '#1a2b4a' if i < 3 else '#ffffff'
    s.t(96, y + 37, k, 19, c1, 'bold', 'start'); s.t(330, y + 37, v, 19, c2, 'bold' if i == 3 else 'normal', 'start')
s.t(400, 480, 'Linearity error becomes a real measurement error in inches', 18, A2, 'bold')
fig(slug, 'sensor-linearity-worked-example-infographic',
    'sensor linearity worked example converting 0.25 percent FSO into 25 mV and 0.005 inch error',
    'Diagram by Instrumentation Blog working the article example: a 0 to 2 inch, 0 to 10 V sensor with 0.25% FSO linearity has 25 mV or 0.005 inch error.',
    'Practical Example of Sensor Linearity', s.svg())

if __name__ == '__main__':
    import cairosvg, re
    out = sys.argv[1] if len(sys.argv) > 1 else None
    for slug, figs in CH.items():
        page = json.load(open(f'/home/claude/instrumentationblog-howitworks/_img/pages/{slug}.json'))
        h2 = [h['text'] for h in page['h2s']]
        for f in figs:
            assert f['after_h2'] in h2, (slug, f['after_h2'])
            txt = ' '.join(re.findall(r'>([^<]*)<', f['svg'])) + f['alt'] + f['caption']
            for ch in '-–—':
                if ch in txt: WARN.append(('dash', f['name'], txt[max(0, txt.index(ch)-30):txt.index(ch)+10]))
            if not f['caption'].startswith('Diagram by Instrumentation Blog'): WARN.append(('cap', f['name']))
            nw = len(f['caption'].split()); aw = len(f['alt'].split())
            if not (12 <= nw <= 35) or not (6 <= aw <= 16): WARN.append(('len', f['name'], nw, aw))
            if len(f['name']) > 70: WARN.append(('namelen', f['name']))
        assert len(set(f['after_h2'] for f in figs)) == 3
        json.dump({'slug': slug, 'figs': figs}, open(os.path.join(OUT, slug + '.json'), 'w'), ensure_ascii=False, indent=1)
        if out:
            for f in figs: cairosvg.svg2png(bytestring=f['svg'].encode(), write_to=os.path.join(out, f['name'] + '.png'), output_width=800)
    for w in WARN: print('WARN', w)
    print({k: [f['name'] for f in v] for k, v in CH.items()})
