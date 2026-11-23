import json, sys, os, re
sys.path.insert(0, '/home/claude/instrumentationblog-howitworks/_img')
from svglib import S as _S
OUT = '/home/claude/instrumentationblog-howitworks/_img/changes'
CH = {}
WARN = []

class S(_S):
    """svglib S with rough overflow checks (0.55 x size per char, bold 0.6)."""
    def t(self, x, y, s, size=18, fill='#1a2b4a', weight='normal', anchor='middle'):
        w = len(s) * size * (0.6 if weight == 'bold' else 0.53)
        x0 = x - w / 2 if anchor == 'middle' else (x if anchor == 'start' else x - w)
        if x0 < 4 or x0 + w > self.w - 4 or y > self.h - 2 or y < 14:
            WARN.append(f'canvas: {s!r} x0={x0:.0f} x1={x0+w:.0f} y={y}')
        if size < 17: WARN.append(f'small text {size}: {s!r}')
        if re.search('[-–—]', s): WARN.append(f'dash in text: {s!r}')
        super().t(x, y, s, size, fill, weight, anchor)
    def box(self, x, y, w, h, lines, fill='#eef6ff', stroke='#1a2b4a', tc='#1a2b4a', size=18, bold_first=True, r=10):
        for i, ln in enumerate(lines):
            tw = len(ln) * size * (0.6 if (bold_first and i == 0) else 0.53)
            if tw > w - 12: WARN.append(f'box overflow: {ln!r} {tw:.0f} > {w-12}')
        if len(lines) * (size + 6) > h: WARN.append(f'box too short: {lines}')
        super().box(x, y, w, h, lines, fill, stroke, tc, size, bold_first, r)
    def dia(self, cx, cy, w, h, lines, fill='#fff7e6', stroke='#1a2b4a', size=18):
        for ln in lines:
            if len(ln) * size * 0.6 > w * 0.62: WARN.append(f'diamond overflow: {ln!r}')
        super().dia(cx, cy, w, h, lines, fill, stroke, size)

def fig(slug, name, alt, caption, after, svg):
    for k, v in (('alt', alt), ('caption', caption)):
        if re.search('[–—]', v) or (k == 'caption' and '-' in v): WARN.append(f'dash in {k}: {name}')
    assert len(name) <= 70 and name.endswith(('diagram', 'flowchart', 'infographic', 'chart')), name
    assert 6 <= len(alt.split()) <= 16, (name, len(alt.split()))
    assert caption.startswith('Diagram by Instrumentation Blog') and 12 <= len(caption.split()) <= 35, (name, len(caption.split()))
    h2s = [h['text'] for h in json.load(open(f'/home/claude/instrumentationblog-howitworks/_img/pages/{slug}.json'))['h2s']]
    assert after in h2s, (slug, after)
    CH.setdefault(slug, []).append(dict(name=name, alt=alt, caption=caption, after_h2=after, svg=svg))

def num(s, x, y, n, c, r=17):
    s.raw(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{c}"/>'); s.o.append(f'<text x="{x}" y="{y+6}" font-size="18" fill="#ffffff" font-weight="bold" text-anchor="middle">{n}</text>')

def arrowc(s, x1, y1, x2, y2, c, w=4):
    s.raw(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{c}" stroke-width="{w}" marker-end="url(#ah)"/>')

# ================= 1. Fleming's left hand rule =================
slug = 'flemings-left-hand-rule-motor'
A, A2, L = '#7c3aed', '#5b21b6', '#f5f3ff'
s = S(500, "Fleming's left hand rule three fingers and force on a conductor between magnet poles")
s.head("Fleming's Left Hand Rule: Three Fingers", A2)
s.raw(f'<rect x="20" y="58" width="370" height="400" rx="14" fill="{L}" stroke="{A}" stroke-width="2"/>')
ox, oy = 190, 280
s.raw(f'<circle cx="{ox}" cy="{oy}" r="7" fill="#1a2b4a"/>')
arrowc(s, ox, oy, ox, 130, '#dc2626', 5)
s.t(ox + 14, 120, 'Thumb: Force F', 19, '#dc2626', 'bold', 'start')
arrowc(s, ox, oy, 350, oy, '#2563eb', 5)
s.t(300, 312, 'Forefinger:', 18, '#2563eb', 'bold')
s.t(300, 336, 'Field B, N to S', 18, '#2563eb', 'bold')
arrowc(s, ox, oy, 95, 375, '#16a34a', 5)
s.t(40, 405, 'Middle finger: Current I', 18, '#16a34a', 'bold', 'start')
s.t(40, 430, '(toward you, out of page)', 17, '#4b5563', 'normal', 'start')
s.t(205, 90, 'All three at right angles', 17, A2, 'bold')
# poles view
s.raw('<rect x="420" y="110" width="60" height="250" rx="6" fill="#dc2626" stroke="#1a2b4a" stroke-width="2"/>')
s.raw('<rect x="710" y="110" width="60" height="250" rx="6" fill="#2563eb" stroke="#1a2b4a" stroke-width="2"/>')
s.t(450, 244, 'N', 26, '#ffffff', 'bold'); s.t(740, 244, 'S', 26, '#ffffff', 'bold')
for yy in (150, 195, 290, 335):
    s.ar(486, yy, 702, yy, '#93c5fd', 2)
cx, cy = 595, 242
s.raw(f'<circle cx="{cx}" cy="{cy}" r="24" fill="#ffffff" stroke="#16a34a" stroke-width="4"/>')
s.raw(f'<circle cx="{cx}" cy="{cy}" r="6" fill="#16a34a"/>')
arrowc(s, cx, cy - 28, cx, 78, '#dc2626', 5)
s.t(cx + 14, 96, 'Force up', 18, '#dc2626', 'bold', 'start')
s.t(595, 392, 'Field from N to S', 18, '#2563eb', 'bold')
s.t(595, 418, 'Dot: current out of page', 18, '#16a34a', 'bold')
s.t(400, 486, 'Remember FBI: thumb Force, forefinger B field, middle finger current I', 18, '#1a2b4a', 'bold')
fig(slug, 'flemings-left-hand-rule-three-fingers-diagram',
    "Flemings left hand rule diagram with thumb force, forefinger field and middle finger current",
    "Diagram by Instrumentation Blog showing Fleming's left hand rule: forefinger along the field from N to S, middle finger along current, thumb giving the force on the conductor.",
    "What Is Fleming's Left Hand Rule?", s.svg())

s = S(600, "Steps to apply Fleming's left hand rule and effect of reversing current or field")
s.head('Applying the Left Hand Rule Step by Step', A2)
steps = [('Find the field', 'mark it from the north pole to the south pole'),
         ('Find the current', 'mark conventional current, positive to negative'),
         ('Set the fingers', 'forefinger on the field, middle finger on the current'),
         ('Read the thumb', 'the thumb now points along the force')]
y = 58
for i, (h, d) in enumerate(steps):
    s.raw(f'<rect x="120" y="{y}" width="560" height="66" rx="12" fill="{L if i % 2 == 0 else "#ffffff"}" stroke="{A}" stroke-width="2"/>')
    num(s, 156, y + 33, i + 1, A)
    s.t(190, y + 27, h, 19, A2, 'bold', 'start'); s.t(190, y + 52, d, 17, '#1a2b4a', 'normal', 'start')
    if i < 3: s.ar(400, y + 66, 400, y + 80, A)
    y += 82
s.ar(400, 380, 400, 398, A)
s.dia(400, 452, 360, 104, ['Reverse current', 'or field?'], '#fef3c7', size=19)
s.pl([(220, 452), (140, 452), (140, 498)], A, 2.5); s.t(150, 438, 'Only one', 17, A2, 'bold')
s.pl([(580, 452), (660, 452), (660, 498)], A, 2.5); s.t(650, 438, 'Both', 17, A2, 'bold')
s.box(20, 502, 250, 80, ['Force reverses', 'the wire moves the', 'opposite way'], '#ffffff', A, size=17)
s.box(530, 502, 250, 80, ['Force unchanged', 'why a DC series motor', 'keeps its direction'], '#ffffff', A, size=17)
fig(slug, 'flemings-left-hand-rule-step-by-step-flowchart',
    'step by step flowchart to apply the left hand rule and reverse motor force',
    'Diagram by Instrumentation Blog showing the four steps of the motor rule, then how reversing current or field reverses the force while reversing both leaves it unchanged.',
    'How to Apply the Rule Step by Step', s.svg())

s = S(540, 'Force F = BIL sin theta and coil torque worked examples')
s.head('Motor Force and Coil Torque: Worked Examples', A2)
for x, ttl, form, rows, res in (
        (25, 'Force on a conductor', 'F = B × I × L × sin θ',
         ['B = 0.5 T, I = 10 A', 'L = 0.2 m, θ = 90°', 'F = 0.5 × 10 × 0.2 × 1'], 'F = 1 N'),
        (410, 'Torque on a motor coil', 'F = N × B × I × L',
         ['N = 50 turns, B = 0.4 T', 'I = 2 A, L = 0.05 m', 'F = 50 × 0.4 × 2 × 0.05 = 2 N',
          'Torque = 2 × 0.04 m'], 'T = 0.08 N m')):
    s.raw(f'<rect x="{x}" y="60" width="365" height="340" rx="14" fill="{L}" stroke="{A}" stroke-width="2.5"/>')
    s.t(x + 182, 95, ttl, 20, A2, 'bold')
    s.raw(f'<rect x="{x+25}" y="112" width="315" height="48" rx="10" fill="{A}"/>')
    s.t(x + 182, 144, form, 20, '#ffffff', 'bold')
    for j, r in enumerate(rows): s.t(x + 182, 196 + j * 34, r, 18)
    s.raw(f'<rect x="{x+70}" y="335" width="225" height="48" rx="10" fill="#ffffff" stroke="{A}" stroke-width="2.5"/>')
    s.t(x + 182, 367, res, 22, A2, 'bold')
s.box(25, 420, 365, 96, ['θ = 90°', 'current across the field,', 'sin 90° = 1, maximum force'], '#ffffff', '#16a34a', size=17)
s.box(410, 420, 365, 96, ['θ = 0°', 'current parallel to the field,', 'sin 0° = 0, no force'], '#ffffff', '#dc2626', size=17)
fig(slug, 'flemings-left-hand-rule-force-torque-infographic',
    'F equals BIL sin theta worked example giving 1 newton force and coil torque',
    'Diagram by Instrumentation Blog with the worked examples: 0.5 T, 10 A and 0.2 m give a 1 N force, and a 50 turn coil at 0.4 T and 2 A gives 0.08 N m.',
    'Force on a Conductor: F = BIL sin θ', s.svg())

# ================= 2. Gas groups =================
slug = 'gas-groups-iia-iib-iic-what-is-the-difference'
A, A2, L = '#b91c1c', '#7f1d1d', '#fef2f2'
s = S(500, 'Gas group classification tree: Group I mining and Group II with IIA, IIB, IIC')
s.head('Gas Group Classification (ATEX and IECEx)', A2)
s.box(250, 58, 300, 60, ['Gas groups', 'by ignition energy'], A, A2, '#ffffff', size=18)
s.pl([(400, 118), (400, 140), (200, 140), (200, 160)], A, 2.5)
s.pl([(400, 140), (600, 140), (600, 160)], A, 2.5)
s.box(60, 162, 280, 74, ['Group I', 'mining: methane, coal dust'], '#ffffff', A, size=17)
s.box(460, 162, 280, 74, ['Group II', 'all other industrial areas'], L, A, size=17)
s.pl([(600, 236), (600, 256), (140, 256), (140, 276)], A, 2.5)
s.ar(400, 256, 400, 276, A)
s.pl([(600, 256), (660, 256), (660, 276)], A, 2.5)
cols = [('IIA', 'Least explosive', 'Propane, acetone,', 'ammonia', '#fde68a'),
        ('IIB', 'Moderately explosive', 'Ethylene,', 'coke oven gas', '#fdba74'),
        ('IIC', 'Most easily ignited', 'Hydrogen, acetylene,', 'carbon disulfide', '#fca5a5')]
for i, (g, d, e1, e2, c) in enumerate(cols):
    x = 20 + i * 260
    s.raw(f'<rect x="{x}" y="280" width="240" height="150" rx="12" fill="{c}" stroke="{A2}" stroke-width="2"/>')
    s.t(x + 120, 314, g, 26, A2, 'bold'); s.t(x + 120, 344, d, 18, '#1a2b4a', 'bold')
    s.t(x + 120, 378, e1, 17); s.t(x + 120, 402, e2, 17)
s.ar(60, 462, 740, 462, A2, 3)
s.t(400, 490, 'Lower ignition energy needed, more dangerous gas', 18, A2, 'bold')
fig(slug, 'gas-groups-classification-tree-diagram',
    'gas groups classification tree with Group I mining and Group II IIA IIB IIC gases',
    'Diagram by Instrumentation Blog showing gas groups: Group I for mining and Group II split into IIA, IIB and IIC by how easily the gas ignites, with example gases.',
    'What Are Gas Groups?', s.svg())

s = S(570, 'IIA IIB IIC comparison of ignition energy, gases and flame path gap')
s.head('IIA vs IIB vs IIC at a Glance', A2)
rows = [('Ignition energy', ['High, least', 'Medium', 'Very low, most'], ['sensitive', '', 'sensitive']),
        ('Example gases', ['Propane, acetone,', 'Ethylene, coke', 'Hydrogen,'], ['ammonia', 'oven gas', 'acetylene, CS2'])]
hx = [190, 390, 590]
for i, g in enumerate(['IIA', 'IIB', 'IIC']):
    s.raw(f'<rect x="{hx[i]}" y="58" width="190" height="46" rx="8" fill="{["#f59e0b", "#ea580c", A][i]}"/>')
    s.t(hx[i] + 95, 89, g, 22, '#ffffff', 'bold')
for r, (lab, l1, l2) in enumerate(rows):
    y = 114 + r * 92
    s.raw(f'<rect x="20" y="{y}" width="760" height="82" rx="8" fill="{L if r % 2 == 0 else "#ffffff"}" stroke="#fecaca" stroke-width="1.5"/>')
    s.t(30, y + 47, lab, 18, A2, 'bold', 'start')
    for i in range(3):
        s.t(hx[i] + 95, y + (34 if l2[i] else 47), l1[i], 17)
        if l2[i]: s.t(hx[i] + 95, y + 60, l2[i], 17)
y = 302
s.raw(f'<rect x="20" y="{y}" width="760" height="168" rx="8" fill="{L}" stroke="#fecaca" stroke-width="1.5"/>')
s.t(30, y + 66, 'Flame path', 18, A2, 'bold', 'start'); s.t(30, y + 90, 'gap', 18, A2, 'bold', 'start')
for i, (gap, lab) in enumerate([(26, 'Wide'), (15, 'Medium'), (6, 'Narrowest')]):
    x = hx[i] + 35
    s.raw(f'<rect x="{x}" y="{y+18}" width="120" height="38" fill="#9ca3af" stroke="#1a2b4a" stroke-width="2"/>')
    s.raw(f'<rect x="{x}" y="{y+56+gap}" width="120" height="38" fill="#9ca3af" stroke="#1a2b4a" stroke-width="2"/>')
    s.t(x + 60, y + 152, lab, 18, A2, 'bold')
s.box(20, 486, 760, 60, ['More explosive gas needs a tighter joint to contain an explosion'], '#ffffff', A, size=18)
fig(slug, 'gas-groups-iia-iib-iic-comparison-infographic',
    'gas group IIA IIB IIC difference in ignition energy, example gases and flame path gap',
    'Diagram by Instrumentation Blog comparing IIA, IIB and IIC gas groups by ignition energy, example gases and flame path gap, which gets narrower as the gas gets more explosive.',
    'Difference Between IIA, IIB, IIC Gas Group', s.svg())

s = S(580, 'Flowchart to choose equipment gas group rating for a hazardous area')
s.head('Is the Equipment Rated for This Gas?', A2)
s.box(250, 56, 300, 56, ['Identify the flammable gas'], L, A, size=18)
s.ar(400, 112, 400, 132, A)
s.dia(400, 190, 330, 110, ['Gas group of', 'the area?'], '#fef3c7', size=19)
s.pl([(235, 190), (130, 190), (130, 272)], A, 2.5); s.t(180, 178, 'IIA', 18, A2, 'bold')
s.ar(400, 245, 400, 272, A); s.t(412, 266, 'IIB', 18, A2, 'bold', 'start')
s.pl([(565, 190), (670, 190), (670, 272)], A, 2.5); s.t(620, 178, 'IIC', 18, A2, 'bold')
for x, lines, c in ((20, ['IIA area', 'IIA, IIB or IIC', 'equipment'], '#fde68a'),
                    (290, ['IIB area', 'IIB or IIC', 'equipment'], '#fdba74'),
                    (560, ['IIC area', 'IIC equipment', 'only'], '#fca5a5')):
    s.box(x, 276, 220, 100, lines, c, A2, size=18)
for x in (130, 400, 670): s.ar(x, 376, x, 398, A)
s.box(40, 400, 720, 70, ['Then also match the zone, protection type', 'and temperature class'], '#ffffff', A, size=18)
s.box(40, 490, 720, 70, ['IIC rated transmitters fit every Group II area', 'and avoid wrong gas group installations'], A, A2, '#ffffff', size=18)
fig(slug, 'gas-groups-equipment-selection-flowchart',
    'flowchart to select IIA IIB or IIC rated equipment for the gas in the area',
    'Diagram by Instrumentation Blog showing how to match equipment to the gas group: IIC equipment fits IIA, IIB and IIC areas, while a IIA area accepts any Group II rating.',
    'Why Does Gas Groups Matter?', s.svg())

# ================= 3. IO-Link =================
slug = 'how-does-io-link-works'
A, A2, L = '#0f766e', '#134e4a', '#f0fdfa'
s = S(560, 'IO Link system architecture with PLC, fieldbus, master ports and 3 wire devices')
s.head('IO Link System: Controller, Master and Devices', A2)
s.box(270, 56, 260, 58, ['PLC, DCS or SCADA'], '#ffffff', A2, size=19)
s.ln(400, 114, 400, 176, A2, 4)
s.t(415, 140, 'Fieldbus or Ethernet', 17, A2, 'bold', 'start')
s.t(415, 164, 'PROFINET, EtherNet/IP, Modbus', 17, '#4b5563', 'normal', 'start')
s.raw(f'<rect x="100" y="178" width="600" height="80" rx="12" fill="{A}" stroke="{A2}" stroke-width="2"/>')
s.t(400, 212, 'IO Link Master', 22, '#ffffff', 'bold')
s.t(400, 240, 'one port, one device, no addresses', 17, '#ffffff')
devs = ['Pressure', 'Temperature', 'Optical', 'Valve']
for i, d in enumerate(devs):
    x = 175 + i * 150
    s.raw(f'<rect x="{x-22}" y="258" width="44" height="22" rx="4" fill="#ffffff" stroke="{A2}" stroke-width="2"/>')
    s.t(x, 275, f'P{i+1}', 17, A2, 'bold')
    for k, c in enumerate(['#b45309', '#1a2b4a', '#2563eb']):
        s.ln(x - 10 + k * 10, 280, x - 10 + k * 10, 370, c, 2.5)
    s.box(x - 68, 372, 136, 56, [d, 'sensor' if i < 3 else 'actuator'], L, A, size=17)
s.t(250, 316, '3 wire cable', 17, A2, 'bold'); s.t(250, 340, 'max 20 m', 17, A2, 'bold')
s.raw(f'<rect x="40" y="448" width="720" height="96" rx="12" fill="#ffffff" stroke="{A}" stroke-width="2"/>')
s.t(400, 476, 'Standard unshielded 3 wire M12 sensor cable', 18, A2, 'bold')
for i, (lab, c) in enumerate([('Pin 1: +24 V DC', '#b45309'), ('Pin 3: 0 V', '#1a2b4a'), ('Pin 4: C/Q data', '#2563eb')]):
    x = 70 + i * 235
    s.ln(x, 512, x + 34, 512, c, 5); s.t(x + 44, 518, lab, 18, c, 'bold', 'start')
fig(slug, 'io-link-master-device-3-wire-diagram',
    'IO-Link system diagram with master ports, point to point sensors and M12 3 wire pins',
    'Diagram by Instrumentation Blog showing an IO Link master linking each port to one sensor or actuator over a 3 wire M12 cable up to 20 m, and to the PLC over fieldbus.',
    'How IO-Link Works: Master, Device and the 3-Wire Connection', s.svg())

s = S(600, 'IO Link port operating mode selection flowchart COM SIO DI DO')
s.head('Which Mode Does the IO Link Port Run?', A2)
s.box(250, 56, 300, 56, ['Device on master port'], L, A, size=19)
s.ar(400, 112, 400, 130, A)
s.dia(400, 188, 340, 110, ['IO Link capable', 'device?'], '#fef3c7', size=19)
s.pl([(230, 188), (140, 188), (140, 256)], A, 2.5); s.t(190, 176, 'Yes', 18, A2, 'bold')
s.pl([(570, 188), (660, 188), (660, 256)], A, 2.5); s.t(612, 176, 'No', 18, A2, 'bold')
s.box(20, 260, 250, 100, ['IO Link (COM) mode', 'COM1 4.8, COM2 38.4,', 'COM3 230.4 kbps'], A, A2, '#ffffff', size=17)
s.ar(145, 360, 145, 384, A)
s.box(20, 388, 250, 128, ['Master reads IODD', 'exchanges process,', 'service and device', 'data plus events'], '#ffffff', A, size=17)
s.dia(660, 316, 250, 104, ['Sensor or', 'actuator?'], '#fef3c7', size=18)
s.pl([(660, 368), (660, 386), (560, 386), (560, 404)], A, 2.5); s.t(585, 380, 'Sensor', 17, A2, 'bold', 'end')
s.pl([(660, 386), (720, 386), (720, 404)], A, 2.5); s.t(712, 378, 'Actuator', 17, A2, 'bold')
s.box(440, 408, 200, 108, ['SIO or DI mode', 'C/Q works as a', 'standard digital', 'input'], L, A, size=17)
s.box(650, 408, 140, 108, ['DO mode', 'C/Q drives', 'lamp, valve', 'or actuator'], L, A, size=17)
s.t(400, 556, 'Old NPN or PNP sensors still work on an IO Link master port', 18, A2, 'bold')
fig(slug, 'io-link-operating-mode-selection-flowchart',
    'IO Link port operating modes flowchart for COM, SIO, DI and DO mode',
    'Diagram by Instrumentation Blog showing how an IO Link master port runs COM mode for a smart device, or SIO, DI and DO modes for conventional sensors and actuators.',
    'IO-Link Four Operating Modes: From Simple Digital to Full Smart Communication', s.svg())

s = S(540, 'Four types of IO Link data: process, service, device and events')
s.head('Four Types of IO Link Data', A2)
cards = [('Process data', ['measured value in digital form', 'sent every cycle, no request', 'up to 32 bytes, 400 µs at COM3'], A),
         ('Service data', ['parameters read or written', 'units, switch point, damping', 'backup and restore after a swap'], '#0369a1'),
         ('Device data', ['manufacturer and device name', 'serial number, hardware and', 'firmware version'], '#7c3aed'),
         ('Events', ['sent at once when abnormal', 'contamination, low supply,', 'calibration overdue'], '#b45309')]
for i, (h, ls, c) in enumerate(cards):
    x = 25 + (i % 2) * 385; y = 62 + (i // 2) * 220
    s.raw(f'<rect x="{x}" y="{y}" width="365" height="200" rx="14" fill="#ffffff" stroke="{c}" stroke-width="2.5"/>')
    s.raw(f'<rect x="{x}" y="{y}" width="365" height="52" rx="14" fill="{c}"/>')
    s.raw(f'<rect x="{x}" y="{y+38}" width="365" height="14" fill="{c}"/>')
    num(s, x + 32, y + 26, i + 1, '#ffffff'); s.o[-1] = s.o[-1].replace('fill="#ffffff"', f'fill="{c}"')
    s.t(x + 62, y + 34, h, 21, '#ffffff', 'bold', 'start')
    for j, l in enumerate(ls): s.t(x + 22, y + 92 + j * 34, l, 18, '#1a2b4a', 'normal', 'start')
s.t(400, 520, 'Process data every cycle, events at once', 17, A2, 'bold')
fig(slug, 'io-link-four-data-types-infographic',
    'IO Link process data, service data, device data and events explained',
    'Diagram by Instrumentation Blog listing the four IO Link data types: cyclic process data up to 32 bytes, service parameters, device identification and instant diagnostic events.',
    'IO-Link Four Types of Data Transmitted', s.svg())

# ================= 4. Level transmitter 5 point calibration =================
slug = 'level-transmitter-5-point-calibration'
A, A2, L = '#1d4ed8', '#1e3a8a', '#eff6ff'
s = S(520, 'DP level transmitter calibration setup with hand pump, vented LP side and loop calibrator')
s.head('DP Level Transmitter Calibration Setup', A2)
s.raw(f'<rect x="290" y="190" width="220" height="130" rx="14" fill="{L}" stroke="{A}" stroke-width="2.5"/>')
s.t(400, 240, 'DP level', 20, A2, 'bold'); s.t(400, 266, 'transmitter', 20, A2, 'bold')
s.raw(f'<rect x="262" y="235" width="28" height="40" fill="#cbd5e1" stroke="#1a2b4a" stroke-width="2"/>')
s.raw(f'<rect x="510" y="235" width="28" height="40" fill="#cbd5e1" stroke="#1a2b4a" stroke-width="2"/>')
s.t(276, 300, 'H', 18, '#1a2b4a', 'bold'); s.t(524, 300, 'L', 18, '#1a2b4a', 'bold')
s.box(20, 215, 170, 80, ['Hand pump', 'known DP input'], '#ffffff', A, size=17)
s.ln(190, 255, 262, 255, '#1a2b4a', 5)
s.ar(538, 255, 600, 255, '#64748b', 2.5)
s.t(612, 248, 'LP vented to', 17, '#1a2b4a', 'bold', 'start'); s.t(612, 272, 'atmosphere', 17, '#1a2b4a', 'bold', 'start')
s.raw('<circle cx="365" cy="190" r="7" fill="#dc2626"/><circle cx="435" cy="190" r="7" fill="#1a2b4a"/>')
s.pl([(365, 183), (365, 100), (560, 100)], '#dc2626', 3, arrow=False)
s.pl([(435, 183), (435, 140), (560, 140)], '#1a2b4a', 3, arrow=False)
s.box(560, 66, 220, 104, ['Loop calibrator', 'in series, powers', 'loop, reads mA'], '#ffffff', A, size=17)
s.t(462, 90, '4 to 20 mA loop', 18, A2, 'bold')
s.box(40, 350, 720, 64, ['DP at 100% level = fluid density × g × vessel height'], A, A2, '#ffffff', size=19)
s.box(40, 430, 720, 70, ['Apply 0%, 25%, 50%, 75%, 100% of span upscale then downscale', 'and record the mA at each point before any adjustment'], '#ffffff', A, size=17, bold_first=False)
fig(slug, 'level-transmitter-dp-calibration-setup-diagram',
    'level transmitter calibration setup with hand pump on HP side and loop calibrator in series',
    'Diagram by Instrumentation Blog showing a DP level transmitter on the bench: hand pump on the high side, low side vented and a loop calibrator in series reading the mA output.',
    'Before You Start: Equipment and Preparation', s.svg())

s = S(600, 'Five point as found and as left level transmitter calibration flowchart')
s.head('5 Point Calibration: As Found to As Left', A2)
left = [['1. Check record', 'tag, LRV, URV, limit'], ['2. Isolate and vent', 'under permit'],
        ['3. Connect source', 'and mA meter in series'], ['4. Record as found', '5 points, up and down']]
y = 58
for i, ls in enumerate(left):
    s.box(30, y, 300, 70, ls, L if i % 2 == 0 else '#ffffff', A, size=17)
    if i < 3: s.ar(180, y + 70, 180, y + 88, A)
    y += 90
s.pl([(330, 363), (400, 363), (400, 100), (440, 100)], A, 2.5)
s.dia(610, 110, 320, 110, ['All points within', '±0.5% of span?'], '#fef3c7', size=18)
s.ar(610, 165, 610, 210, A); s.t(632, 196, 'No', 18, A2, 'bold', 'start')
s.box(460, 214, 300, 70, ['Raise NCR, then trim', 'zero and span'], '#fee2e2', '#b91c1c', size=17)
s.ar(610, 284, 610, 304, A)
s.box(460, 308, 300, 70, ['Repeat all 5 points', 'record as left'], '#ffffff', A, size=17)
s.ar(610, 378, 610, 398, A)
s.dia(610, 450, 320, 100, ['As left within', 'the limit?'], '#fef3c7', size=18)
s.pl([(450, 450), (420, 450), (420, 249), (460, 249)], A, 2.5); s.t(412, 438, 'No', 17, A2, 'bold', 'end')
s.ar(610, 500, 610, 522, A); s.t(632, 516, 'Yes', 18, A2, 'bold', 'start')
s.pl([(770, 110), (790, 110), (790, 556), (762, 556)], A, 2.5)
s.t(765, 142, 'Yes', 18, A2, 'bold')
s.box(460, 526, 300, 60, ['Sign record, restore', 'valves, check DCS'], A, A2, '#ffffff', size=17)
s.box(30, 440, 300, 96, ['Never adjust before', 'all as found readings', 'are recorded'], '#ffffff', '#b91c1c', size=17)
fig(slug, 'level-transmitter-as-found-as-left-flowchart',
    'level transmitter 5 point calibration flowchart with as found check, trim and as left record',
    'Diagram by Instrumentation Blog showing the 5 point procedure: record as found, compare with the plus or minus 0.5% limit, raise NCR and trim if needed, then record as left.',
    '5-Point Level Transmitter Calibration Procedure', s.svg())

s = S(560, 'Expected mA at 0, 25, 50, 75 and 100 percent of span with tolerance')
s.head('Expected mA at Each Calibration Point', A2)
x0, x1, y0, y1 = 110, 520, 470, 80
def PX(p): return x0 + p * (x1 - x0) / 100
def PY(m): return y0 - (m - 4) * (y0 - y1) / 16
for m in (4, 8, 12, 16, 20):
    s.ln(x0, PY(m), x1, PY(m), '#e5e7eb', 1.5); s.t(x0 - 12, PY(m) + 6, f'{m}', 17, '#4b5563', 'normal', 'end')
for p in (0, 25, 50, 75, 100):
    s.t(PX(p), y0 + 28, f'{p}%', 17, '#4b5563')
s.ln(x0, y0, x1, y0, '#1a2b4a', 2); s.ln(x0, y0, x0, y1 - 10, '#1a2b4a', 2)
s.pl([(PX(0), PY(4)), (PX(100), PY(20))], A, 3, arrow=False)
for p in (0, 25, 50, 75, 100):
    m = 4 + p / 100 * 16
    s.raw(f'<circle cx="{PX(p)}" cy="{PY(m)}" r="8" fill="{A}" stroke="#ffffff" stroke-width="2"/>')
s.t(315, 545, '% of calibrated span', 18, '#1a2b4a', 'bold')
s.raw(f'<text x="34" y="275" font-size="18" fill="#1a2b4a" font-weight="bold" text-anchor="middle" transform="rotate(-90 34 275)">Output mA</text>')
s.raw(f'<rect x="555" y="72" width="225" height="250" rx="12" fill="{L}" stroke="{A}" stroke-width="2"/>')
s.t(667, 104, 'mA = 4 + % × 16', 19, A2, 'bold')
for j, (p, m) in enumerate([(0, '4.00'), (25, '8.00'), (50, '12.00'), (75, '16.00'), (100, '20.00')]):
    s.t(590, 142 + j * 36, f'{p}%', 18, '#1a2b4a', 'bold', 'start'); s.t(745, 142 + j * 36, f'{m} mA', 18, '#1a2b4a', 'normal', 'end')
s.raw(f'<rect x="555" y="338" width="225" height="150" rx="12" fill="#ffffff" stroke="#16a34a" stroke-width="2"/>')
s.t(667, 368, 'Limit ±0.5% of span', 18, '#166534', 'bold')
s.t(667, 396, '= ±0.08 mA', 18, '#166534')
s.t(667, 432, 'Pass at 50%:', 18, '#1a2b4a', 'bold'); s.t(667, 460, '11.92 to 12.08 mA', 18)
s.t(400, 526, '', 17) if False else None
fig(slug, 'level-transmitter-expected-ma-calibration-chart',
    'expected mA at 0 25 50 75 and 100 percent span for level transmitter calibration',
    'Diagram by Instrumentation Blog plotting expected output of 4, 8, 12, 16 and 20 mA at the five points, with the plus or minus 0.08 mA limit and 11.92 to 12.08 mA pass band.',
    'Expected mA at Each Calibration Point', s.svg())

# ================= 5. Measurement uncertainty =================
slug = 'measurement-uncertainty-in-calibration'
A, A2, L = '#b45309', '#78350f', '#fffbeb'
s = S(560, 'Type A and Type B uncertainty components combined into uc and expanded uncertainty U')
s.head('Where Calibration Uncertainty Comes From', A2)
s.raw(f'<rect x="20" y="58" width="250" height="300" rx="14" fill="{L}" stroke="{A}" stroke-width="2.5"/>')
s.t(145, 90, 'Type A', 22, A2, 'bold'); s.t(145, 116, 'statistics of', 17); s.t(145, 138, 'repeated readings', 17)
s.box(40, 160, 210, 86, ['Ua', 'repeatability', 'S / √n'], '#ffffff', A, size=17)
s.t(145, 290, 'normal spread', 17, '#4b5563'); s.t(145, 314, 'of the readings', 17, '#4b5563')
s.raw(f'<rect x="290" y="58" width="490" height="300" rx="14" fill="#ffffff" stroke="{A}" stroke-width="2.5"/>')
s.t(535, 90, 'Type B', 22, A2, 'bold'); s.t(535, 116, 'certificates, specs, prior knowledge', 17)
tb = [('Ub1', 'certificate', 'U / k'), ('Ub2', 'accuracy', 'value / √3'), ('Ub3', 'resolution', '(res / 2) / √3'),
      ('Ub4', 'hysteresis', 'diff / √3'), ('Ub5', 'zero error', 'zero / √3')]
for i, (h, d, f) in enumerate(tb):
    x = 305 + (i % 3) * 157; y = 136 + (i // 3) * 110
    if i >= 3: x += 78
    s.box(x, y, 145, 96, [h, d, f], L, A, size=17)
s.pl([(145, 358), (145, 390), (400, 390), (400, 404)], A2, 2.5)
s.pl([(535, 358), (535, 390), (400, 390)], A2, 2.5, arrow=False)
s.box(170, 406, 460, 62, ['uc = √(Ua² + Ub1² + ... + Ub5²)'], A, A2, '#ffffff', size=19)
s.ar(400, 468, 400, 486, A2)
s.box(170, 488, 460, 56, ['U = k × uc, k = 2 for about 95%'], '#ffffff', A2, size=19)
fig(slug, 'measurement-uncertainty-in-calibration-type-a-type-b-diagram',
    'measurement uncertainty in calibration Type A and Type B components combined by root sum of squares',
    'Diagram by Instrumentation Blog showing Type A repeatability and five Type B components, each turned into a standard uncertainty, combined by root sum of squares and expanded with k.',
    'Type A and Type B Uncertainty: The Fundamental Division', s.svg())

s = S(600, 'Step by step uncertainty calculation at the 4 bar point of a 0 to 10 bar gauge')
s.head('Uncertainty at the 4 Bar Point, Step by Step', A2)
steps = [('Readings', 'up 4.006, down 4.004 bar'), ('Ua repeatability', '0.001414 / √2 = 0.001'),
         ('Ub1 certificate', '0.01 / 2 = 0.005'), ('Ub2 accuracy', '0.004 / √3 = 0.002309'),
         ('Ub3 resolution', '0.0005 / √3 = 0.000289'), ('Ub4 hysteresis', '0.002 / √3 = 0.001155'),
         ('Ub5 zero error', '0 / √3 = 0'), ('Combined uc', 'RSS = 0.00572 bar')]
for i, (h, d) in enumerate(steps):
    col = i // 4; row = i % 4
    x = 40 + col * 380; y = 66 + row * 100
    s.box(x, y, 330, 78, [h, d], L if i % 2 == 0 else '#ffffff', A, size=18)
    if row < 3: s.ar(x + 165, y + 78, x + 165, y + 98, A)
s.pl([(205, 444), (205, 458), (385, 458), (385, 52), (585, 52), (585, 64)], A, 2.5)
s.ar(585, 444, 585, 480, A)
s.box(380, 484, 400, 96, ['Expanded U = 2 × 0.00572', '= 0.011 bar at k = 2', 'about 95% confidence'], A, A2, '#ffffff', size=18)
s.box(40, 484, 320, 96, ['All values in bar', 'reference: 0 to 40 bar,', '0.1% of reading'], '#ffffff', '#94a3b8', size=17)
fig(slug, 'measurement-uncertainty-in-calibration-4-bar-flowchart',
    'step by step uncertainty calculation flowchart at 4 bar from Ua to expanded uncertainty',
    'Diagram by Instrumentation Blog working the 4 bar point: Ua 0.001, Ub1 0.005, Ub2 0.002309, Ub3 0.000289, Ub4 0.001155 give uc 0.00572 bar and U 0.011 bar.',
    'Combined Standard Uncertainty (uc)', s.svg())

s = S(520, 'Uncertainty budget bar chart at 4 bar showing the dominant contributor')
s.head('Uncertainty Budget at 4 Bar', A2)
comps = [('Ub1 certificate', 0.005), ('Ub2 accuracy', 0.002309), ('Ub4 hysteresis', 0.001155),
         ('Ua repeatability', 0.001), ('Ub3 resolution', 0.000289), ('Ub5 zero error', 0.0)]
bx, bw = 240, 360
for i, (lab, v) in enumerate(comps):
    y = 70 + i * 52
    s.t(225, y + 26, lab, 18, '#1a2b4a', 'bold', 'end')
    s.raw(f'<rect x="{bx}" y="{y+4}" width="{bw}" height="30" rx="6" fill="#f3f4f6"/>')
    if v: s.raw(f'<rect x="{bx}" y="{y+4}" width="{bw * v / 0.005:.0f}" height="30" rx="6" fill="{A if i == 0 else "#f59e0b"}"/>')
    s.t(bx + bw + 12, y + 26, f'{v:.6f}'.rstrip('0').rstrip('.') if v else '0', 18, '#1a2b4a', 'normal', 'start')
s.box(40, 392, 350, 104, ['Dominant term', 'Ub1, the reference', 'certificate, 0.005 bar'], L, A, size=18)
s.box(410, 392, 350, 104, ['Result at 4 bar', 'uc = 0.00572 bar', 'U = 0.011 bar, k = 2'], A, A2, '#ffffff', size=18)
fig(slug, 'measurement-uncertainty-in-calibration-budget-chart',
    'uncertainty budget chart at 4 bar with reference certificate as dominant contributor',
    'Diagram by Instrumentation Blog ranking the 4 bar uncertainty budget: the reference certificate term of 0.005 bar dominates, giving uc of 0.00572 bar and U of 0.011 bar.',
    'The Uncertainty Budget: Identifying the Dominant Contributors', s.svg())

# ================= 6. Point to point vs multidrop =================
slug = 'point-to-point-connection-multidrop-connection'
A, A2, L = '#15803d', '#14532d', '#f0fdf4'
s = S(520, 'Point to point wiring vs multidrop shared line wiring diagram')
s.head('Point to Point vs Multidrop Wiring', A2)
s.raw(f'<rect x="15" y="56" width="375" height="440" rx="14" fill="{L}" stroke="{A}" stroke-width="2"/>')
s.raw(f'<rect x="410" y="56" width="375" height="440" rx="14" fill="#ffffff" stroke="{A}" stroke-width="2"/>')
s.t(202, 88, 'Point to point', 21, A2, 'bold'); s.t(597, 88, 'Multidrop', 21, A2, 'bold')
s.box(40, 230, 120, 70, ['PLC'], '#ffffff', A2, size=20)
for i, d in enumerate(['Device 1', 'Device 2', 'Device 3']):
    y = 120 + i * 110
    s.box(250, y, 120, 60, [d], '#ffffff', A, size=17)
    xb = [185, 205, 225][i]
    ey = [245, 260, 280][i]
    s.pl([(160, ey), (xb, ey), (xb, y + 30), (250, y + 30)], A2, 3, arrow=False)
s.t(202, 450, 'One dedicated cable', 17, A2, 'bold'); s.t(202, 474, 'per device', 17, A2, 'bold')
s.box(435, 110, 130, 60, ['Master'], '#ffffff', A2, size=20)
s.ln(500, 170, 500, 420, A2, 5)
for i, d in enumerate(['Address 1', 'Address 2', 'Address 3']):
    y = 195 + i * 80
    s.ln(500, y + 28, 600, y + 28, A2, 3)
    s.box(600, y, 160, 56, [d], L, A, size=17)
s.t(597, 450, 'One shared line,', 17, A2, 'bold'); s.t(597, 474, 'each device has an address', 17, A2, 'bold')
fig(slug, 'point-to-point-connection-vs-multidrop-wiring-diagram',
    'point to point connection vs multidrop connection wiring with dedicated and shared lines',
    'Diagram by Instrumentation Blog comparing point to point wiring, with one dedicated cable per device, against multidrop wiring, where addressed devices share one line.',
    'The Definition of a Point to Point Connection', s.svg())

s = S(580, 'How a multidrop network delivers a broadcast packet by address')
s.head('Multidrop: How a Packet Finds Its Device', A2)
steps = [['Sender broadcasts', 'the data packet'], ['Every device on', 'the line receives it'], ['Each device reads', 'the destination address']]
y = 58
for i, ls in enumerate(steps):
    s.box(220, y, 360, 70, ls, L if i % 2 == 0 else '#ffffff', A, size=18)
    s.ar(400, y + 70, 400, y + 92, A)
    y += 94
s.dia(400, 386, 360, 104, ['Address matches', 'its own?'], '#fef3c7', size=19)
s.pl([(220, 386), (130, 386), (130, 460)], A, 2.5); s.t(170, 374, 'Yes', 18, A2, 'bold')
s.pl([(580, 386), (670, 386), (670, 460)], A, 2.5); s.t(630, 374, 'No', 18, A2, 'bold')
s.box(20, 464, 240, 92, ['Accept', 'and process', 'the data'], A, A2, '#ffffff', size=18)
s.box(540, 464, 240, 92, ['Ignore', 'the packet'], '#ffffff', '#94a3b8', size=18)
fig(slug, 'point-to-point-connection-multidrop-addressing-flowchart',
    'multidrop connection flowchart of broadcast packet and address check by each device',
    'Diagram by Instrumentation Blog showing multidrop communication: the sender broadcasts, every device receives and checks the address, and only the matching device accepts the data.',
    'The Definition of MultiPoint (Multidrop) Connection Communication', s.svg())

s = S(560, 'Point to point vs multipoint communication comparison infographic')
s.head('Point to Point vs Multipoint at a Glance', A2)
s.raw(f'<rect x="250" y="58" width="260" height="46" rx="8" fill="{A}"/>'); s.t(380, 89, 'Point to point', 20, '#ffffff', 'bold')
s.raw(f'<rect x="520" y="58" width="260" height="46" rx="8" fill="#0f766e"/>'); s.t(650, 89, 'Multipoint', 20, '#ffffff', 'bold')
rows = [('Devices on link', 'Two only', 'Many on one line'),
        ('Transmitter and receiver', 'One to one', 'One to many'),
        ('Bandwidth', 'Reserved for the pair', 'Shared by all'),
        ('Addressing', 'Not needed', 'Each device checks'),
        ('Cabling', 'One cable per device', 'Less cable, one trunk'),
        ('Security', 'Better, not shared', 'Lower, shared channel')]
for i, (k, a, b) in enumerate(rows):
    y = 114 + i * 70
    s.raw(f'<rect x="20" y="{y}" width="760" height="62" rx="8" fill="{L if i % 2 == 0 else "#ffffff"}" stroke="#bbf7d0" stroke-width="1.5"/>')
    s.t(32, y + 38, k, 17, A2, 'bold', 'start')
    s.t(380, y + 38, a, 17); s.t(650, y + 38, b, 17)
fig(slug, 'point-to-point-connection-vs-multipoint-comparison-infographic',
    'point to point communication vs multipoint communication comparison of bandwidth, cabling and security',
    'Diagram by Instrumentation Blog comparing point to point and multipoint links by number of devices, bandwidth, addressing, cabling and security.',
    'Point to Point Communication vs Multipoint Communication', s.svg())

if __name__ == '__main__':
    import cairosvg
    out = sys.argv[1] if len(sys.argv) > 1 else None
    for slug, figs in CH.items():
        assert len(figs) == 3 and len({f['after_h2'] for f in figs}) == 3, slug
        json.dump({'slug': slug, 'figs': figs}, open(os.path.join(OUT, slug + '.json'), 'w'), ensure_ascii=False, indent=1)
        if out:
            for f in figs: cairosvg.svg2png(bytestring=f['svg'].encode(), write_to=os.path.join(out, f['name'] + '.png'), output_width=800)
    print('\n'.join(WARN))
    print({k: [f['name'] for f in v] for k, v in CH.items()})
