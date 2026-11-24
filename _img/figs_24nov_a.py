import sys; sys.path.insert(0, '/home/claude/instrumentationblog-howitworks/_img')
from figs_24nov_common import *

GR = '#4b5563'

# ================= 1. Differential pressure transmitter =================
slug = 'basics-of-differential-pressure-transmitter'
A, A2, L = '#0f766e', '#134e4a', '#f0fdfa'
s = S(560, 'Differential pressure transmitter capacitance sensing cell cross section with HP and LP sides')
s.head('Inside a DP Transmitter Capacitance Cell', A2)
# body of the cell
s.raw(f'<rect x="190" y="90" width="420" height="250" rx="18" fill="{L}" stroke="#1a2b4a" stroke-width="2.5"/>')
# isolating diaphragms (wavy) on each side
s.raw(f'<path d="M190 140 q-14 15 0 30 q-14 15 0 30 q-14 15 0 30 q-14 15 0 30 q-14 15 0 30 q-14 15 0 30" fill="none" stroke="{A}" stroke-width="4"/>')
s.raw(f'<path d="M610 140 q14 15 0 30 q14 15 0 30 q14 15 0 30 q14 15 0 30 q14 15 0 30 q14 15 0 30" fill="none" stroke="{A}" stroke-width="4"/>')
# fill fluid channels
s.raw('<rect x="215" y="200" width="125" height="30" fill="#fde68a" stroke="#b45309" stroke-width="1.5"/>')
s.raw('<rect x="460" y="200" width="125" height="30" fill="#fde68a" stroke="#b45309" stroke-width="1.5"/>')
# fixed plates (curved electrodes)
s.raw('<path d="M350 120 Q372 215 350 310" fill="none" stroke="#1a2b4a" stroke-width="6"/>')
s.raw('<path d="M450 120 Q428 215 450 310" fill="none" stroke="#1a2b4a" stroke-width="6"/>')
# sensing diaphragm bowed toward LP (right)
s.raw(f'<path d="M400 112 Q432 215 400 318" fill="none" stroke="#dc2626" stroke-width="4"/>')
s.raw('<rect x="340" y="200" width="16" height="30" fill="#fde68a"/>')
s.raw('<rect x="444" y="200" width="16" height="30" fill="#fde68a"/>')
# arrows HP and LP
s.ar(60, 215, 172, 215, '#dc2626', 5); s.t(85, 195, 'HP', 22, '#dc2626', 'bold')
s.ar(740, 215, 628, 215, '#2563eb', 5); s.t(715, 195, 'LP', 22, '#2563eb', 'bold')
s.t(95, 250, 'higher', 17, GR); s.t(705, 250, 'lower', 17, GR)
# labels top
s.t(200, 78, 'Isolating diaphragm', 17, A2, 'bold')
s.t(600, 78, 'Isolating diaphragm', 17, A2, 'bold')
s.t(400, 78, 'Sensing diaphragm', 17, '#dc2626', 'bold')
s.ln(400, 84, 404, 110, '#dc2626', 1.5)
# labels below
s.t(277, 262, 'Silicone oil', 17, '#92400e', 'bold'); s.t(523, 262, 'Silicone oil', 17, '#92400e', 'bold')
s.box(205, 360, 190, 70, ['HP side plate', 'gap opens, C falls'], '#ffffff', A, size=17)
s.box(405, 360, 190, 70, ['LP side plate', 'gap closes, C rises'], '#ffffff', A, size=17)
s.ln(300, 360, 352, 300, '#9ca3af', 1.5); s.ln(500, 360, 448, 300, '#9ca3af', 1.5)
s.box(250, 450, 300, 54, ['Electronics: capacitance ratio', 'to 4 to 20 mA with HART'], A, A, '#ffffff', size=17)
s.t(400, 535, 'C = ε × A ÷ d, so a smaller gap d gives a larger capacitance', 18, '#1a2b4a', 'bold')
fig(slug, 'differential-pressure-transmitter-capacitance-cell-diagram',
    'differential pressure transmitter capacitance cell with isolating diaphragms, fill fluid and sensing diaphragm',
    'Diagram by Instrumentation Blog showing a DP transmitter capacitance cell: HP and LP isolating diaphragms, silicone oil fill and a sensing diaphragm moving between two fixed plates.',
    'How a DP Transmitter Works: The Sensing Cell Explained', s.svg())

s = S(560, 'DP transmitter manifold valve sequence for commissioning and taking out of service')
s.head('Equalising Valve Sequence on a DP Manifold', A2)
s.raw(f'<rect x="20" y="58" width="370" height="420" rx="14" fill="{L}" stroke="{A}" stroke-width="2"/>')
s.raw('<rect x="410" y="58" width="370" height="420" rx="14" fill="#fff7ed" stroke="#c2410c" stroke-width="2"/>')
s.t(205, 90, 'Commissioning', 21, A2, 'bold'); s.t(595, 90, 'Taking out of service', 21, '#9a3412', 'bold')
c1 = [['1. Open equalise', 'DP = 0'], ['2. Open HP block', ''], ['3. Open LP block', ''], ['4. Close equalise', 'slowly, live DP']]
c2 = [['1. Open equalise', 'DP goes to zero'], ['2. Close HP block', ''], ['3. Close LP block', ''], ['4. Close equalise', 'fully isolated']]
for i in range(4):
    y = 108 + i * 90
    l1 = [x for x in c1[i] if x]; l2 = [x for x in c2[i] if x]
    s.box(55, y, 300, 64, l1, '#ffffff', A, size=18)
    s.box(445, y, 300, 64, l2, '#ffffff', '#c2410c', size=18)
    if i < 3: s.ar(205, y + 64, 205, y + 88); s.ar(595, y + 64, 595, y + 88)
s.raw('<rect x="20" y="490" width="760" height="58" rx="12" fill="#fef2f2" stroke="#dc2626" stroke-width="2"/>')
s.t(400, 514, 'Wrong order puts full process pressure on one side only', 18, '#991b1b', 'bold')
s.t(400, 538, 'and can over range or damage the sensing diaphragm.', 18, '#991b1b')
fig(slug, 'differential-pressure-transmitter-manifold-valve-sequence-flowchart',
    'DP transmitter manifold valve sequence for commissioning and isolation with equalise valve',
    'Diagram by Instrumentation Blog showing the correct manifold valve order for a DP transmitter: open equalise first when commissioning and when taking it out of service.',
    'Critical Installation Pitfalls: The Equalising Valve Sequence', s.svg())

s = S(520, 'DP transmitter 4 to 20 mA output formula with worked example of 30 kPa on a 0 to 50 kPa range')
s.head('DP to 4 to 20 mA: Worked Example', A2)
s.raw(f'<rect x="40" y="60" width="720" height="70" rx="14" fill="{A}"/>')
s.t(400, 104, 'I = 4 + [(DP minus LRV) ÷ (URV minus LRV)] × 16', 22, '#ffffff', 'bold')
steps = [('Range', '0 to 50 kPa'), ('Measured DP', '30 kPa'), ('Fraction', '30 ÷ 50 = 0.60'), ('Output', '4 + 9.6 = 13.6 mA')]
for i, (k, v) in enumerate(steps):
    x = 40 + i * 182
    s.raw(f'<rect x="{x}" y="150" width="172" height="100" rx="12" fill="{L if i % 2 == 0 else "#ffffff"}" stroke="{A}" stroke-width="2"/>')
    s.t(x + 86, 186, k, 18, A2, 'bold'); s.t(x + 86, 225, v, 18 if i == 2 or i == 3 else 20, '#1a2b4a', 'bold')
# bar
s.t(400, 290, 'Output on the span', 19, '#1a2b4a', 'bold')
s.raw(f'<rect x="80" y="310" width="640" height="40" rx="8" fill="#ffffff" stroke="#1a2b4a" stroke-width="2"/>')
s.raw(f'<rect x="80" y="310" width="384" height="40" rx="8" fill="{A}"/>')
s.t(272, 337, '60 percent of span', 18, '#ffffff', 'bold')
for frac, ma in [(0, '4 mA'), (0.5, '12 mA'), (1, '20 mA')]:
    x = 80 + 640 * frac
    s.ln(x, 350, x, 365, '#1a2b4a', 2); s.t(x, 388, ma, 18, '#1a2b4a', 'bold')
s.ln(464, 300, 464, 362, '#dc2626', 3); s.t(464, 410, '13.6 mA', 19, '#dc2626', 'bold')
s.t(80, 420, '0 kPa', 17, GR); s.t(720, 420, '50 kPa', 17, GR)
s.raw('<rect x="40" y="440" width="720" height="60" rx="12" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2"/>')
s.t(400, 466, 'HP equal to LP: 4 mA.  HP above LP: output rises toward 20 mA.', 18, '#1a2b4a')
s.t(400, 490, 'For flow, 25 percent of DP span gives 50 percent flow and 12 mA.', 18, '#1a2b4a')
fig(slug, 'differential-pressure-transmitter-4-20-ma-output-infographic',
    'differential pressure transmitter 4 to 20 mA formula with 30 kPa example giving 13.6 mA',
    'Diagram by Instrumentation Blog with the DP to 4 to 20 mA formula and the article example: 30 kPa on a 0 to 50 kPa range gives 13.6 mA.',
    'From Differential Pressure to 4-20 mA: The Output Signal', s.svg())

# ================= 2. Bonded and unbonded strain gauges =================
slug = 'bonded-and-unbonded-strain-gauges'
A, A2, L = '#b45309', '#78350f', '#fffbeb'
s = S(580, 'Bonded strain gauge diagram with foil grid, backing, adhesive, diaphragm and solder tabs')
s.head('Bonded Strain Gauge Diagram: Parts and Layout', A2)
# top view of foil grid
s.raw(f'<rect x="40" y="70" width="330" height="200" rx="8" fill="#fef3c7" stroke="#1a2b4a" stroke-width="2"/>')
pts = []
for i in range(8):
    x = 100 + i * 22
    pts += [(x, 100), (x, 240)] if i % 2 == 0 else [(x, 240), (x, 100)]
s.pl(pts, A, 3.5, False)
s.ln(100, 100, 100, 100)
s.raw('<rect x="270" y="86" width="44" height="34" fill="#9ca3af" stroke="#1a2b4a" stroke-width="1.5"/>')
s.raw('<rect x="270" y="220" width="44" height="34" fill="#9ca3af" stroke="#1a2b4a" stroke-width="1.5"/>')
s.ln(254, 100, 270, 103, A, 3.5); s.ln(100, 240, 100, 252, A, 3.5); s.pl([(100, 252), (240, 252), (270, 237)], A, 3.5, False)
s.ln(314, 103, 360, 103, '#1a2b4a', 2.5); s.ln(314, 237, 360, 237, '#1a2b4a', 2.5)
s.t(205, 296, 'Top view: zigzag sensing grid', 18, '#1a2b4a', 'bold')
s.t(292, 140, 'Solder', 17, GR); s.t(292, 160, 'tabs', 17, GR)
# cross section layers right
layers = [('Sensing grid', '#d97706', 12), ('Backing or carrier', '#fde68a', 18), ('Adhesive layer', '#e5e7eb', 14), ('Diaphragm or test surface', '#94a3b8', 40)]
y = 90
s.t(590, 78, 'Side view layers', 18, '#1a2b4a', 'bold')
for name, col, h in layers:
    s.raw(f'<rect x="400" y="{y}" width="120" height="{h}" fill="{col}" stroke="#1a2b4a" stroke-width="1.5"/>')
    s.ln(520, y + h / 2, 540, y + h / 2, '#9ca3af', 1.5)
    s.t(545, y + h / 2 + 6, name, 17, '#1a2b4a', 'normal', 'start')
    y += h + 14
# four gauges arrangement on diaphragm
s.raw(f'<circle cx="200" cy="440" r="95" fill="{L}" stroke="#1a2b4a" stroke-width="2.5"/>')
for (x, y0, w, h) in [(185, 405, 30, 22), (185, 453, 30, 22), (112, 428, 22, 26), (266, 428, 22, 26)]:
    s.raw(f'<rect x="{x}" y="{y0}" width="{w}" height="{h}" fill="{A}" stroke="#1a2b4a" stroke-width="1.5"/>')
s.t(200, 558, 'Diaphragm with four gauges', 17, '#1a2b4a', 'bold')
s.box(330, 360, 440, 80, ['2 near the centre', 'tangential strain'], '#ffffff', A, size=18)
s.box(330, 455, 440, 80, ['2 near the edge', 'radial strain, opposite sign'], '#ffffff', A, size=18)
s.ln(215, 416, 330, 400, '#9ca3af', 1.5); s.ln(288, 440, 330, 495, '#9ca3af', 1.5)
fig(slug, 'bonded-and-unbonded-strain-gauges-bonded-gauge-parts-diagram',
    'bonded strain gauge diagram showing foil grid, backing, adhesive, diaphragm and four gauge layout',
    'Diagram by Instrumentation Blog showing a bonded strain gauge: zigzag foil grid, solder tabs, backing, adhesive, diaphragm and the centre and edge placement of four gauges.',
    'Bonded Strain Gauge Diagram: Parts and Layout', s.svg())

s = S(520, 'How a strain gauge works from applied pressure to a reading through a Wheatstone bridge')
s.head('How a Strain Gauge Turns Pressure into a Reading', A2)
row1 = [['Pressure', 'or force'], ['Element', 'stretches'], ['Longer and', 'thinner'], ['Resistance', 'increases']]
x = 30
for i, ls in enumerate(row1):
    s.box(x, 80, 170, 90, ls, L if i % 2 == 0 else '#ffffff', A, size=18)
    if i < 3: s.ar(x + 172, 125, x + 192, 125, A, 2.5)
    x += 192
s.pl([(683, 172), (683, 220), (115, 220), (115, 250)], A, 2.5)
row2 = [['Wheatstone', 'bridge unbalance'], ['Millivolt', 'output'], ['Electronics', 'temp, zero, span'], ['Pressure or', 'strain reading']]
x = 30
for i, ls in enumerate(row2):
    s.box(x, 252, 170, 90, ls, '#ffffff' if i % 2 == 0 else L, A, size=17)
    if i < 3: s.ar(x + 172, 297, x + 192, 297, A, 2.5)
    x += 192
s.raw(f'<rect x="30" y="370" width="740" height="120" rx="14" fill="{L}" stroke="{A}" stroke-width="2"/>')
s.t(400, 404, 'Gauge factor GF = (ΔR ÷ R) ÷ strain', 21, A2, 'bold')
s.t(400, 440, 'Metal foil: GF about 2, so 1000 microstrain gives about 0.2 percent ΔR', 18, '#1a2b4a')
s.t(400, 470, 'Compression does the opposite: shorter, thicker, lower resistance.', 18, GR)
fig(slug, 'bonded-and-unbonded-strain-gauges-working-flowchart',
    'strain gauge working flowchart from stretching to resistance change and Wheatstone bridge output',
    'Diagram by Instrumentation Blog showing how a strain gauge works: stretching raises resistance, the Wheatstone bridge unbalances and electronics turn the millivolt signal into a reading.',
    'How Does a Strain Gauge Work?', s.svg())

s = S(580, 'Bonded vs unbonded strain gauge comparison of construction, shock resistance and overpressure protection')
s.head('Bonded vs Unbonded Strain Gauges', A2)
# unbonded sketch
s.raw(f'<rect x="30" y="60" width="360" height="190" rx="14" fill="#ffffff" stroke="{A}" stroke-width="2"/>')
s.raw(f'<rect x="410" y="60" width="360" height="190" rx="14" fill="#ffffff" stroke="{A}" stroke-width="2"/>')
s.t(210, 90, 'Unbonded', 21, A2, 'bold'); s.t(590, 90, 'Bonded', 21, A2, 'bold')
s.raw('<rect x="60" y="110" width="40" height="110" fill="#94a3b8" stroke="#1a2b4a" stroke-width="2"/>')
s.raw(f'<rect x="250" y="130" width="40" height="70" fill="{A}" stroke="#1a2b4a" stroke-width="2"/>')
for yy in (125, 205): s.raw(f'<circle cx="100" cy="{yy}" r="6" fill="#1a2b4a"/>')
for yy in (140, 190): s.raw(f'<circle cx="250" cy="{yy}" r="6" fill="#1a2b4a"/>')
s.ln(100, 125, 250, 190, '#1a2b4a', 2); s.ln(100, 205, 250, 140, '#1a2b4a', 2)
s.ar(300, 165, 360, 165, '#dc2626', 3)
s.t(80, 240, 'fixed', 17, GR); s.t(270, 222, 'movable', 17, GR); s.t(335, 150, 'force', 17, '#dc2626')
s.t(175, 108, 'fine wires on posts', 17, GR)
# bonded sketch
s.raw('<path d="M450 160 Q590 125 730 160 L730 190 Q590 155 450 190 Z" fill="#94a3b8" stroke="#1a2b4a" stroke-width="2"/>')
s.raw(f'<path d="M530 150 Q590 133 650 150 L650 142 Q590 125 530 142 Z" fill="{A}" stroke="#1a2b4a" stroke-width="1.5"/>')
s.ar(590, 238, 590, 182, '#dc2626', 3); s.t(640, 228, 'pressure', 17, '#dc2626')
s.t(590, 110, 'foil glued to diaphragm', 17, GR)
rows = [('Construction', 'wire on frame and posts', 'foil on a diaphragm'), ('Shock resistance', 'poor', 'good'),
        ('Overpressure', 'overtravel stops', 'limited'), ('Size', 'larger, frame', 'compact, light'),
        ('Moving parts', 'movable frame', 'none'), ('Cost', 'often lower', 'generally higher')]
y = 270
s.raw(f'<rect x="30" y="{y}" width="740" height="38" fill="{A}"/>')
s.t(140, y + 26, 'Feature', 18, '#ffffff', 'bold'); s.t(390, y + 26, 'Unbonded', 18, '#ffffff', 'bold'); s.t(640, y + 26, 'Bonded', 18, '#ffffff', 'bold')
for i, (a, b, c) in enumerate(rows):
    yy = y + 38 + i * 40
    s.raw(f'<rect x="30" y="{yy}" width="740" height="40" fill="{L if i % 2 == 0 else "#ffffff"}" stroke="#fcd34d" stroke-width="1"/>')
    s.t(140, yy + 27, a, 18, '#1a2b4a', 'bold'); s.t(390, yy + 27, b, 18, '#1a2b4a'); s.t(640, yy + 27, c, 18, '#1a2b4a')
fig(slug, 'bonded-and-unbonded-strain-gauges-comparison-infographic',
    'bonded and unbonded strain gauges comparison of construction, shock resistance, overpressure and cost',
    'Diagram by Instrumentation Blog comparing unbonded strain gauges with wire on a movable frame against bonded foil gauges glued to a diaphragm, with a feature table.',
    'Comparison Table: Bonded vs. Unbonded Strain Gauges', s.svg())

# ================= 3. Bourdon tube pressure gauges =================
import math
slug = 'bourdon-tube-pressure-gauges'
A, A2, L = '#be123c', '#881337', '#fff1f2'
def P(cx, cy, r, deg): return (cx + r * math.cos(math.radians(deg)), cy + r * math.sin(math.radians(deg)))
s = S(580, 'Construction of a Bourdon tube pressure gauge with tube, socket, link, sector, pinion, pointer and dial')
s.head('Construction of a Bourdon Tube Pressure Gauge', A2)
cx, cy = 250, 300
s.raw(f'<circle cx="{cx}" cy="{cy}" r="205" fill="#ffffff" stroke="#1a2b4a" stroke-width="3"/>')
for d in range(135, 406, 15):
    x1, y1 = P(cx, cy, 186, d); x2, y2 = P(cx, cy, 200 if d % 45 == 0 else 194, d)
    s.ln(round(x1, 1), round(y1, 1), round(x2, 1), round(y2, 1), '#1a2b4a', 2)
# socket
s.raw('<rect x="222" y="462" width="56" height="90" rx="4" fill="#9ca3af" stroke="#1a2b4a" stroke-width="2"/>')
s.ar(250, 575, 250, 556, '#dc2626', 3)
# C tube
x0, y0 = P(cx, cy, 160, 90); xt, yt = P(cx, cy, 160, 340)
s.raw(f'<path d="M{x0:.1f} {y0:.1f} A160 160 0 1 1 {xt:.1f} {yt:.1f}" fill="none" stroke="{A}" stroke-width="14" stroke-linecap="round"/>')
s.raw(f'<path d="M{x0:.1f} {y0:.1f} A160 160 0 1 1 {xt:.1f} {yt:.1f}" fill="none" stroke="#fecdd3" stroke-width="6"/>')
s.raw(f'<circle cx="{xt:.1f}" cy="{yt:.1f}" r="9" fill="{A2}"/>')
# sector and pinion
px, py = 310, 370
fa, fb = P(px, py, 80, 209), P(px, py, 80, 249)
s.raw(f'<path d="M{px} {py} L{fa[0]:.1f} {fa[1]:.1f} A80 80 0 0 1 {fb[0]:.1f} {fb[1]:.1f} Z" fill="#fde68a" stroke="#1a2b4a" stroke-width="2"/>')
tx, ty = P(px, py, 55, 45)
s.ln(px, py, round(tx, 1), round(ty, 1), '#1a2b4a', 5)
s.raw(f'<circle cx="{px}" cy="{py}" r="6" fill="#1a2b4a"/>')
s.ln(round(xt, 1), round(yt, 1), round(tx, 1), round(ty, 1), '#2563eb', 4)
s.raw(f'<circle cx="{cx}" cy="{cy}" r="13" fill="#fde68a" stroke="#1a2b4a" stroke-width="2"/>')
# pointer
pe = P(cx, cy, 165, 300); pb = P(cx, cy, 30, 120)
s.ln(round(pb[0], 1), round(pb[1], 1), round(pe[0], 1), round(pe[1], 1), '#111827', 5)
s.raw(f'<circle cx="{cx}" cy="{cy}" r="5" fill="#111827"/>')
# numbered markers
mks = [(1, P(cx, cy, 160, 190)), (2, (250, 520)), (3, (xt + 24, yt - 10)), (4, (372, 318)), (5, (268, 375)), (6, (222, 318)), (7, P(cx, cy, 120, 300)), (8, P(cx, cy, 186, 140))]
for n, (x, y) in mks: num(s, round(x), round(y), n, '#1a2b4a', 15)
labs = ['C shaped Bourdon tube', 'Socket, fixed end', 'Free end (tip)', 'Link', 'Sector gear', 'Pinion', 'Pointer', 'Dial']
for i, lab in enumerate(labs):
    y = 88 + i * 34
    num(s, 488, y, i + 1, A, 14); s.t(512, y + 6, lab, 18, '#1a2b4a', 'normal', 'start')
# section inset
s.raw(f'<rect x="470" y="380" width="310" height="180" rx="12" fill="{L}" stroke="{A}" stroke-width="2"/>')
s.t(625, 408, 'Tube cross section', 18, A2, 'bold')
s.raw(f'<ellipse cx="560" cy="470" rx="45" ry="20" fill="#ffffff" stroke="{A}" stroke-width="4"/>')
s.ar(615, 470, 650, 470)
s.raw(f'<ellipse cx="700" cy="470" rx="38" ry="30" fill="#ffffff" stroke="{A}" stroke-width="4" stroke-dasharray="6 4"/>')
s.t(560, 520, 'elliptical', 17, GR); s.t(700, 520, 'pressure', 17, GR)
s.t(625, 546, 'tube straightens, tip moves', 17, '#1a2b4a', 'bold')
fig(slug, 'bourdon-tube-pressure-gauges-construction-diagram',
    'Bourdon tube pressure gauge construction showing C tube, socket, link, sector gear, pinion and pointer',
    'Diagram by Instrumentation Blog showing the parts of a Bourdon tube pressure gauge: C shaped tube, socket, free end, link, sector gear, pinion, pointer and dial.',
    'Construction of a Bourdon Tube Pressure Gauge', s.svg())

s = S(600, 'Flowchart to choose a Bourdon tube type and a dry or liquid filled case')
s.head('How to Choose a Bourdon Tube Gauge', A2)
s.box(200, 58, 400, 56, ['Check maximum working pressure', 'normal reading in the middle of the dial'], L, A, size=17)
s.ar(400, 114, 400, 134)
s.dia(400, 184, 330, 96, ['Very high pressure', 'or overpressure?'], '#ffffff', A, size=17)
s.ar(565, 184, 615, 184); s.t(590, 174, 'Yes', 17, A2, 'bold')
s.box(615, 154, 165, 60, ['Helical', 'type'], A, A, '#ffffff', size=18)
s.ar(400, 232, 400, 256); s.t(420, 250, 'No', 17, A2, 'bold', 'start')
s.dia(400, 306, 330, 96, ['Fine resolution', 'at low pressure?'], '#ffffff', A, size=17)
s.ar(565, 306, 615, 306); s.t(590, 296, 'Yes', 17, A2, 'bold')
s.box(615, 276, 165, 60, ['Spiral', 'type'], A, A, '#ffffff', size=18)
s.ar(235, 306, 185, 306); s.t(210, 296, 'No', 17, A2, 'bold')
s.box(20, 276, 165, 60, ['C type', 'general service'], A2, A2, '#ffffff', size=17)
s.pl([(102, 336), (102, 380), (300, 380)], '#1a2b4a', 2.5, False)
s.pl([(697, 214), (697, 240), (790, 240), (790, 380), (500, 380)], '#1a2b4a', 2.5, False)
s.pl([(697, 336), (697, 380)], '#1a2b4a', 2.5, False)
s.ar(400, 380, 400, 400)
s.ln(300, 380, 500, 380, '#1a2b4a', 2.5)
s.dia(400, 448, 330, 92, ['Vibration or', 'pulsation?'], '#ffffff', A, size=17)
s.ar(565, 448, 600, 448); s.t(583, 438, 'Yes', 17, A2, 'bold')
s.box(600, 418, 190, 60, ['Liquid filled', 'glycerin or oil'], L, A, size=17)
s.ar(235, 448, 200, 448); s.t(218, 438, 'No', 17, A2, 'bold')
s.box(10, 418, 190, 60, ['Dry gauge', 'steady service'], L, A, size=17)
s.raw(f'<rect x="60" y="510" width="680" height="70" rx="12" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2"/>')
s.t(400, 538, 'Last step: pick a tube material such as brass, phosphor', 18, '#1a2b4a')
s.t(400, 564, 'bronze or beryllium copper that suits the process fluid.', 18, '#1a2b4a')
fig(slug, 'bourdon-tube-pressure-gauges-selection-flowchart',
    'flowchart to choose C type, spiral or helical Bourdon tube and dry or liquid filled gauge',
    'Diagram by Instrumentation Blog showing how to choose a Bourdon tube gauge: helical for very high pressure, spiral for fine low pressure, C type otherwise, then dry or liquid filled.',
    'Types of Bourdon Tube Compared: C Type, Spiral and Helical', s.svg())

s = S(560, 'Three types of Bourdon tube: C type, spiral and helical with pressure range and key feature')
s.head('Three Types of Bourdon Tube', A2)
cols = [('C type', 'Low to medium', ['Single arc of', 'about 250 to 270°', 'most common']),
        ('Spiral', 'Lower ranges', ['Turns in one', 'flat plane, better', 'sensitivity']),
        ('Helical', 'Very high pressure', ['Turns like a coil', 'spring, resists', 'overpressure'])]
for i, (nm, rg, ls) in enumerate(cols):
    x = 30 + i * 253
    s.raw(f'<rect x="{x}" y="58" width="235" height="400" rx="14" fill="{L if i != 1 else "#ffffff"}" stroke="{A}" stroke-width="2.5"/>')
    s.t(x + 117, 92, nm, 22, A2, 'bold')
    gx, gy = x + 117, 190
    if i == 0:
        a0 = P(gx, gy, 62, 100); a1 = P(gx, gy, 62, 100 + 260)
        s.raw(f'<path d="M{a0[0]:.1f} {a0[1]:.1f} A62 62 0 1 1 {a1[0]:.1f} {a1[1]:.1f}" fill="none" stroke="{A}" stroke-width="10" stroke-linecap="round"/>')
    elif i == 1:
        pts = []
        for k in range(0, 721 + 360, 12):
            r = 14 + k * 0.045; pts.append(P(gx, gy, r, k))
        s.pl([(round(a, 1), round(b, 1)) for a, b in pts], A, 6, False)
    else:
        for k in range(5):
            s.raw(f'<ellipse cx="{gx}" cy="{130 + k * 28}" rx="55" ry="14" fill="none" stroke="{A}" stroke-width="6"/>')
    s.raw(f'<rect x="{x + 15}" y="285" width="205" height="40" rx="8" fill="{A}"/>')
    s.t(x + 117, 312, rg, 17, '#ffffff', 'bold')
    for j, l in enumerate(ls): s.t(x + 117, 362 + j * 28, l, 17, '#1a2b4a')
s.raw('<rect x="30" y="476" width="740" height="66" rx="12" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2"/>')
s.t(400, 502, 'Patented 1849 by Edward Bourdon.  Range 0.6 to 7,000 bar.', 18, '#1a2b4a', 'bold')
s.t(400, 528, 'Tip moves only about 1/8 inch; the linkage magnifies it.', 18, '#1a2b4a')
fig(slug, 'bourdon-tube-pressure-gauges-types-infographic',
    'Bourdon tube pressure gauges types C type, spiral and helical with pressure ranges',
    'Diagram by Instrumentation Blog comparing C type, spiral and helical Bourdon tubes by shape, pressure range and key feature, with key numbers from the article.',
    'Types of Bourdon Tube Pressure Gauges', s.svg())

# ================= 4. Types of pressure transmitters =================
slug = 'types-of-pressure-transmitters'
A, A2, L = '#15803d', '#14532d', '#f0fdf4'
s = S(580, 'Sensing references of gauge, absolute, differential and multivariable pressure transmitters')
s.head('Four Types of Pressure Transmitters', A2)
def capsule(x, y, left, right, rcol='#ffffff'):
    s.raw(f'<rect x="{x}" y="{y}" width="150" height="90" rx="10" fill="{L}" stroke="#1a2b4a" stroke-width="2"/>')
    s.raw(f'<rect x="{x + 80}" y="{y + 8}" width="62" height="74" rx="6" fill="{rcol}" stroke="#9ca3af" stroke-width="1.5"/>')
    s.raw(f'<path d="M{x + 75} {y + 6} Q{x + 88} {y + 45} {x + 75} {y + 84}" fill="none" stroke="#dc2626" stroke-width="4"/>')
panels = [('Gauge', 'reference: atmosphere'), ('Absolute', 'reference: sealed vacuum'), ('Differential', 'HP minus LP'), ('Multivariable', 'DP, static P and temperature')]
for i, (nm, sub) in enumerate(panels):
    x = 20 + (i % 2) * 390; y = 58 + (i // 2) * 255
    s.raw(f'<rect x="{x}" y="{y}" width="370" height="240" rx="14" fill="#ffffff" stroke="{A}" stroke-width="2.5"/>')
    s.t(x + 185, y + 32, nm, 22, A2, 'bold'); s.t(x + 185, y + 60, sub, 17, GR)
    cx0, cy0 = x + 110, y + 90
    if i == 0:
        capsule(cx0, cy0, 'P', 'atm')
        s.ar(cx0 - 80, cy0 + 45, cx0 - 4, cy0 + 45, '#dc2626', 4); s.t(cx0 - 45, cy0 + 30, 'process', 17, '#dc2626', 'end')
        s.ln(cx0 + 150, cy0 + 45, cx0 + 200, cy0 + 45, '#1a2b4a', 2.5); s.t(cx0 + 200, cy0 + 30, 'vent', 17, '#1a2b4a', 'end')
        s.t(cx0 + 75, cy0 + 120, 'reads 0 at atmosphere', 17, '#1a2b4a')
    elif i == 1:
        capsule(cx0, cy0, 'P', 'vac', '#e5e7eb')
        s.ar(cx0 - 80, cy0 + 45, cx0 - 4, cy0 + 45, '#dc2626', 4); s.t(cx0 - 45, cy0 + 30, 'process', 17, '#dc2626', 'end')
        s.t(cx0 + 160, cy0 + 40, 'sealed', 17, '#1a2b4a', 'normal', 'start'); s.t(cx0 + 160, cy0 + 62, 'vacuum', 17, '#1a2b4a', 'normal', 'start')
        s.t(cx0 + 75, cy0 + 120, 'weather and altitude proof', 17, '#1a2b4a')
    elif i == 2:
        capsule(cx0, cy0, 'HP', 'LP')
        s.ar(cx0 - 80, cy0 + 45, cx0 - 4, cy0 + 45, '#dc2626', 4); s.t(cx0 - 45, cy0 + 30, 'HP', 18, '#dc2626', 'end')
        s.ar(cx0 + 220, cy0 + 45, cx0 + 154, cy0 + 45, '#2563eb', 4); s.t(cx0 + 200, cy0 + 30, 'LP', 18, '#2563eb', 'end')
        s.t(cx0 + 75, cy0 + 120, 'flow, level, filter drop', 17, '#1a2b4a')
    else:
        for j, lab in enumerate(['DP', 'Static P', 'Temp']):
            s.box(x + 20, y + 80 + j * 48, 110, 40, [lab], L, A, size=17)
            s.ar(x + 132, y + 100 + j * 48, x + 175, y + 128 + j * 20, A, 2)
        s.box(x + 178, y + 118, 170, 60, ['Microprocessor', 'compensates'], A, A, '#ffffff', size=17)
        s.t(x + 263, y + 210, 'mass and energy flow', 17, '#1a2b4a')
fig(slug, 'types-of-pressure-transmitters-sensing-reference-diagram',
    'types of pressure transmitters gauge, absolute, differential and multivariable sensing references',
    'Diagram by Instrumentation Blog showing the four types of pressure transmitters and what each sensing diaphragm is referenced to: atmosphere, vacuum, LP port or several sensors.',
    'Comparison of the Four Types of Pressure Transmitters', s.svg())

s = S(540, 'Gauge and absolute pressure scale with atmospheric pressure and perfect vacuum reference')
s.head('Gauge vs Absolute Pressure Reference', A2)
x0 = 330
s.ln(x0, 470, x0, 70, '#1a2b4a', 3)
s.ln(x0 - 20, 470, x0 + 430, 470, '#1a2b4a', 3); s.t(x0 - 30, 476, 'Perfect vacuum', 18, '#1a2b4a', 'bold', 'end')
s.t(x0 - 30, 500, '0 bar absolute', 17, GR, 'normal', 'end')
s.ln(x0 - 20, 400, x0 + 430, 400, '#2563eb', 3, '8 6'); s.t(x0 - 30, 406, 'Atmosphere', 18, '#2563eb', 'bold', 'end')
s.t(x0 - 30, 430, 'about 1.013 bar abs', 17, GR, 'normal', 'end')
s.ln(x0 - 20, 110, x0 + 430, 110, '#dc2626', 3); s.t(x0 - 30, 116, 'Pump discharge', 18, '#dc2626', 'bold', 'end')
s.ar(430, 400, 430, 114, A, 5); s.t(445, 250, '6 bar gauge', 19, A, 'bold', 'start')
s.t(445, 276, 'measured from', 17, '#1a2b4a', 'normal', 'start'); s.t(445, 298, 'atmosphere', 17, '#1a2b4a', 'normal', 'start')
s.ar(580, 470, 580, 114, '#6d28d9', 5); s.t(595, 250, 'about 7 bar', 19, '#6d28d9', 'bold', 'start')
s.t(595, 276, 'absolute, from', 17, '#1a2b4a', 'normal', 'start'); s.t(595, 298, 'vacuum', 17, '#1a2b4a', 'normal', 'start')
s.raw('<rect x="30" y="150" width="250" height="150" rx="12" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2"/>')
s.t(155, 184, 'Absolute =', 18, '#1a2b4a', 'bold'); s.t(155, 212, 'gauge + atmospheric', 18, '#1a2b4a', 'bold')
s.t(155, 248, '6 + 1.013', 18, '#1a2b4a'); s.t(155, 276, '= 7.013 bar abs', 18, '#1a2b4a')
s.t(420, 525, 'Below the atmosphere line a gauge transmitter reads vacuum.', 17, GR)
fig(slug, 'types-of-pressure-transmitters-gauge-absolute-chart',
    'gauge vs absolute pressure chart with 6 bar gauge pump discharge example',
    'Diagram by Instrumentation Blog showing gauge pressure measured from atmosphere and absolute pressure measured from perfect vacuum, using the 6 bar pump discharge example.',
    '1. Gauge Pressure Transmitter', s.svg())

s = S(600, 'Flowchart to select a gauge, absolute, differential or multivariable pressure transmitter')
s.head('Which Pressure Transmitter Do You Need?', A2)
qs = [(['Pressure relative', 'to atmosphere?'], ['Gauge', 'pumps, water, air']),
      (['True pressure or', 'vacuum needed?'], ['Absolute', 'vacuum, barometric']),
      (['Difference between', 'two points?'], ['Differential', 'flow, level, filter']),
      (['Compensated mass or', 'energy flow?'], ['Multivariable', 'steam, gas, energy'])]
for i, (q, a) in enumerate(qs):
    y = 100 + i * 100
    s.dia(230, y, 330, 86, q, '#ffffff', A, size=17)
    s.ar(395, y, 470, y); s.t(432, y - 10, 'Yes', 17, A2, 'bold')
    s.box(470, y - 33, 210, 66, a, A if i % 2 == 0 else A2, A, '#ffffff', size=17)
    if i < 3: s.ar(230, y + 43, 230, y + 57); s.t(250, y + 56, 'No', 17, A2, 'bold', 'start')
s.raw(f'<rect x="30" y="470" width="740" height="112" rx="12" fill="{L}" stroke="{A}" stroke-width="2"/>')
s.t(400, 498, 'Then check for every type:', 18, A2, 'bold')
s.t(400, 526, 'pressure range, process temperature, fluid, accuracy, response,', 17, '#1a2b4a')
s.t(400, 552, 'vibration and humidity, hazardous area, output signal and protocol', 17, '#1a2b4a')
fig(slug, 'types-of-pressure-transmitters-selection-flowchart',
    'flowchart to select gauge, absolute, differential or multivariable pressure transmitter',
    'Diagram by Instrumentation Blog showing how to choose between gauge, absolute, differential and multivariable pressure transmitters, followed by the selection checks from the article.',
    'Key Points to Consider While Selecting a Pressure Transmitter', s.svg())

# ================= 5. Square root extraction =================
slug = 'square-root-extraction-dp-flow'
A, A2, L = '#4338ca', '#312e81', '#eef2ff'
s = S(500, 'Square root extraction loop from orifice plate and DP transmitter to flow indicator')
s.head('Where Square Root Extraction Sits in a DP Flow Loop', A2)
s.raw('<rect x="20" y="100" width="300" height="60" fill="#e0f2fe" stroke="#1a2b4a" stroke-width="2.5"/>')
s.ln(170, 92, 170, 120, '#1a2b4a', 6); s.ln(170, 140, 170, 168, '#1a2b4a', 6)
s.ar(40, 130, 120, 130, '#0369a1', 4); s.ar(210, 130, 300, 130, '#0369a1', 4)
s.t(60, 88, 'Q', 20, '#0369a1', 'bold'); s.t(170, 82, 'Orifice plate', 17, '#1a2b4a', 'bold')
s.ln(145, 160, 145, 250, '#dc2626', 3); s.ln(200, 160, 200, 250, '#2563eb', 3); s.t(132, 215, 'HP', 17, '#dc2626', 'bold', 'end'); s.t(212, 215, 'LP', 17, '#2563eb', 'bold', 'start')
s.box(120, 250, 150, 70, ['DP', 'transmitter'], L, A, size=18)
s.t(195, 350, 'ΔP is proportional to Q²', 17, '#1a2b4a', 'bold')
s.ar(272, 285, 330, 285, A, 3); s.t(300, 270, 'mA', 17, GR)
s.box(330, 240, 180, 90, ['Square root', 'extractor', 'takes √ΔP'], A, A, '#ffffff', size=17)
s.ar(512, 285, 560, 285, A, 3)
s.box(560, 240, 220, 90, ['Indicator, recorder,', 'controller, totaliser', 'linear in flow'], '#ffffff', A, size=17)
s.raw('<rect x="330" y="80" width="450" height="110" rx="12" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2"/>')
s.t(555, 112, 'Flow doubles, ΔP rises four times', 18, '#1a2b4a', 'bold')
s.t(555, 142, 'Q = k × √ΔP', 20, A2, 'bold')
s.t(555, 172, 'Electronic or pneumatic device', 17, GR)
s.raw(f'<rect x="20" y="390" width="760" height="90" rx="12" fill="{L}" stroke="{A}" stroke-width="2"/>')
s.t(400, 424, 'Today the square root function is done inside the DP transmitter,', 18, '#1a2b4a')
s.t(400, 452, 'a flow computer or the control system instead of a separate box.', 18, '#1a2b4a')
fig(slug, 'square-root-extraction-dp-flow-loop-diagram',
    'square root extraction in a DP flow loop with orifice plate, transmitter and extractor',
    'Diagram by Instrumentation Blog showing a DP flow loop: orifice plate, DP transmitter, square root extractor and a linear flow indicator or controller.',
    'What Is a Square Root Extractor?', s.svg())

s = S(560, 'Square root extraction calculation steps from linear mA to flow mA')
s.head('Square Root Extraction Step by Step', A2)
steps = [('1', 'Read linear DP signal', '8 mA'), ('2', 'Percent of DP span', '(8 minus 4) ÷ 16 = 0.25'),
         ('3', 'Take the square root', '√0.25 = 0.50'), ('4', 'Scale back to mA', '4 + 16 × 0.50 = 12 mA'),
         ('5', 'Read flow', '50 percent of full flow')]
for i, (n, a, b) in enumerate(steps):
    y = 62 + i * 84
    s.raw(f'<rect x="60" y="{y}" width="680" height="66" rx="12" fill="{L if i % 2 == 0 else "#ffffff"}" stroke="{A}" stroke-width="2"/>')
    num(s, 100, y + 33, n, A, 20)
    s.t(140, y + 41, a, 19, A2, 'bold', 'start'); s.t(715, y + 41, b, 19, '#1a2b4a', 'bold', 'end')
    if i < 4: s.ar(400, y + 66, 400, y + 82)
s.raw('<rect x="60" y="490" width="680" height="54" rx="12" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2"/>')
s.t(400, 524, 'Output mA = 4 + 16 × √[(input mA minus 4) ÷ 16]', 19, '#1a2b4a', 'bold')
fig(slug, 'square-root-extraction-dp-flow-calculation-flowchart',
    'square root extraction calculation from 8 mA DP signal to 12 mA flow signal',
    'Diagram by Instrumentation Blog showing square root extraction in five steps: 8 mA is 25 percent of DP span, its square root is 0.50, giving 12 mA and 50 percent flow.',
    'Square Root Extraction Formula', s.svg())

s = S(560, 'Square root extraction chart of linear DP mA against square root flow mA from 4 to 20 mA')
s.head('Square Root Extraction Table as a Chart', A2)
ox, oy, W, H = 110, 470, 620, 380
def X(v): return ox + (v - 4) / 16 * W
def Y(v): return oy - (v - 4) / 16 * H
for v in range(4, 21, 4):
    s.ln(round(X(v), 1), oy, round(X(v), 1), oy - H, '#e5e7eb', 1); s.ln(ox, round(Y(v), 1), ox + W, round(Y(v), 1), '#e5e7eb', 1)
    s.t(round(X(v), 1), oy + 26, str(v), 17, '#1a2b4a'); s.t(ox - 12, round(Y(v), 1) + 6, str(v), 17, '#1a2b4a', 'normal', 'end')
s.ln(ox, oy, ox + W, oy, '#1a2b4a', 2.5); s.ln(ox, oy, ox, oy - H, '#1a2b4a', 2.5)
tbl = [(4, 4.00), (5, 8.00), (6, 9.66), (7, 10.93), (8, 12.00), (9, 12.94), (10, 13.80), (11, 14.58), (12, 15.31), (13, 16.00),
       (14, 16.65), (15, 17.27), (16, 17.86), (17, 18.42), (18, 18.97), (19, 19.49), (20, 20.00)]
s.pl([(round(X(a), 1), round(Y(b), 1)) for a, b in tbl], A, 4, False)
s.ln(ox, oy, ox + W, oy - H, '#9ca3af', 2.5, '8 6')
for a, b in tbl: s.raw(f'<circle cx="{X(a):.1f}" cy="{Y(b):.1f}" r="5" fill="{A}"/>')
for a, b, dx in [(5, 8.00, 14), (8, 12.00, 14), (12, 15.31, 14)]:
    s.raw(f'<circle cx="{X(a):.1f}" cy="{Y(b):.1f}" r="9" fill="none" stroke="#dc2626" stroke-width="3"/>')
    s.t(round(X(a) + dx, 1), round(Y(b) + 30, 1), f'{a} to {b:.2f} mA', 17, '#dc2626', 'bold', 'start')
s.t(ox + W / 2, oy + 60, 'Linear DP signal (mA)', 18, '#1a2b4a', 'bold')
s.raw(f'<text x="36" y="{oy - H / 2}" font-size="18" fill="#1a2b4a" font-weight="bold" text-anchor="middle" transform="rotate(-90 36 {oy - H / 2})">Square root output (mA)</text>')
s.t(610, 380, 'dashed: no extraction', 17, GR)
fig(slug, 'square-root-extraction-dp-flow-table-chart',
    'square root extraction chart of linear mA against square root mA from the table',
    'Diagram by Instrumentation Blog plotting the square root extraction table from 4 to 20 mA, showing that 5 mA becomes 8 mA and 12 mA becomes 15.31 mA.',
    'Square root extraction table', s.svg())

if __name__ == '__main__': main()
