import json, sys, math
sys.path.insert(0, '/home/claude/instrumentationblog-howitworks/_img')
from svglib import S
OUT = '/home/claude/instrumentationblog-howitworks/_img/changes'
CH = {}
def fig(slug, name, alt, caption, after, svg):
    CH.setdefault(slug, []).append(dict(name=name, alt=alt, caption=caption, after_h2=after, svg=svg))
INK = '#1a2b4a'; GREY = '#4b5563'

# ============ 1. Induction motor slip (orange) ============
A, A2, L = '#c2410c', '#9a3412', '#fff7ed'
slug = 'induction-motor-slip-explained'
s = S(500, 'Induction motor slip shown as the gap between stator field speed and rotor speed')
s.head('Induction Motor Slip: Field Speed vs Rotor Speed', A2)
cx, cy = 210, 270
s.raw(f'<circle cx="{cx}" cy="{cy}" r="160" fill="#f3f4f6" stroke="{INK}" stroke-width="3"/>')
s.raw(f'<circle cx="{cx}" cy="{cy}" r="125" fill="#ffffff" stroke="{INK}" stroke-width="2"/>')
for i in range(12):
    a = math.radians(i * 30)
    s.raw(f'<rect x="{cx-9}" y="{cy-158}" width="18" height="30" fill="#d1d5db" stroke="{INK}" stroke-width="1" transform="rotate({i*30} {cx} {cy})"/>')
s.raw(f'<circle cx="{cx}" cy="{cy}" r="85" fill="{L}" stroke="{A}" stroke-width="3"/>')
for i in range(8):
    s.raw(f'<line x1="{cx}" y1="{cy-82}" x2="{cx}" y2="{cy-50}" stroke="{A}" stroke-width="4" transform="rotate({i*45+22} {cx} {cy})"/>')
s.raw(f'<circle cx="{cx}" cy="{cy}" r="14" fill="{INK}"/>')
# field arrow arc (outer) and rotor arc (inner)
def arc(r, a1, a2, col, w):
    x1, y1 = cx + r*math.cos(math.radians(a1)), cy + r*math.sin(math.radians(a1))
    x2, y2 = cx + r*math.cos(math.radians(a2)), cy + r*math.sin(math.radians(a2))
    s.raw(f'<path d="M{x1:.1f} {y1:.1f} A{r} {r} 0 0 1 {x2:.1f} {y2:.1f}" fill="none" stroke="{col}" stroke-width="{w}" marker-end="url(#ah)"/>')
arc(108, 200, 300, '#2563eb', 4)
arc(68, 210, 290, A, 4)
s.t(cx, cy + 45, 'Rotor', 18, A2, 'bold')
s.t(cx, 82, 'Stator with rotating field', 18, INK, 'bold')
# right side panel
bx = 420
s.box(bx, 80, 350, 66, ['Field speed Ns = 120 × f ÷ P', '120 × 50 ÷ 4 = 1500 rpm'], '#eff6ff', '#2563eb', size=18)
s.box(bx, 160, 350, 66, ['Rotor speed Nr', '1470 rpm under load'], L, A, size=18)
s.box(bx, 240, 350, 66, ['Speed gap Ns − Nr', '1500 − 1470 = 30 rpm'], '#ffffff', INK, size=18)
s.box(bx, 320, 350, 66, ['Slip S = 30 ÷ 1500', '0.02, or 2 percent'], A, A2, '#ffffff', size=19)
s.box(bx, 400, 350, 66, ['Rotor frequency fr = S × f', '0.02 × 50 = 1 Hz'], '#ffffff', INK, size=18)
s.t(210, 470, 'Blue arrow: field at Ns. Orange arrow: rotor at Nr.', 17, GREY)
fig(slug, 'induction-motor-slip-stator-rotor-speed-diagram',
    'induction motor slip diagram showing stator field at 1500 rpm and rotor at 1470 rpm',
    'Diagram by Instrumentation Blog showing induction motor slip as the gap between the 1500 rpm stator field and the 1470 rpm rotor of a 4 pole 50 Hz motor.',
    'What Is Slip in an Induction Motor', s.svg())

s = S(590, 'Flowchart to calculate induction motor slip and find the operating mode')
s.head('How to Calculate Slip: Step by Step', A2)
steps = [['1. Read the nameplate', 'f = 50 Hz, P = 4 poles'],
         ['2. Synchronous speed', 'Ns = 120 × 50 ÷ 4 = 1500 rpm'],
         ['3. Measure rotor speed', 'Tachometer: Nr = 1470 rpm'],
         ['4. Apply the slip formula', '(1500 − 1470) ÷ 1500 × 100 = 2%']]
y = 62
for i, ls in enumerate(steps):
    s.box(40, y, 380, 74, ls, L if i % 2 == 0 else '#ffffff', A, size=18)
    if i < 3: s.ar(230, y + 76, 230, y + 96, A2)
    y += 98
s.ar(230, 438, 230, 470, A2)
s.dia(230, 515, 280, 80, ['Where is S?'], '#fef3c7', A, 19)
s.pl([(370, 515), (470, 515)], A2, arrow=False)
outs = [(80, 'S between 0 and 1', 'Motoring (normal)', L), (200, 'S = 1', 'Standstill at start', '#ffffff'),
        (320, 'S negative', 'Induction generator', '#eff6ff'), (440, 'S greater than 1', 'Plugging or braking', '#fee2e2')]
# right column of outcomes
s.pl([(470, 515), (470, 117)], A2, arrow=False)
for yy, a1, a2, f in outs:
    s.ar(470, yy + 37, 495, yy + 37, A2)
    s.box(497, yy, 270, 74, [a1, a2], f, A, size=18)
fig(slug, 'induction-motor-slip-calculation-flowchart',
    'flowchart to calculate induction motor slip from nameplate frequency, poles and rotor speed',
    'Diagram by Instrumentation Blog showing the steps to calculate slip for a 4 pole 50 Hz motor running at 1470 rpm and how the slip value sets the operating mode.',
    'Worked Example: Calculating Slip', s.svg())

s = S(560, 'Induction motor slip values and modes with a slip percentage table')
s.head('What Each Slip Value Means', A2)
# number line from -1 to 2
x0, x1, yl = 80, 720, 150
def X(v): return x0 + (v + 1) / 3 * (x1 - x0)
s.raw(f'<rect x="{X(-1)}" y="{yl-30}" width="{X(0)-X(-1)}" height="60" fill="#dbeafe"/>')
s.raw(f'<rect x="{X(0)}" y="{yl-30}" width="{X(1)-X(0)}" height="60" fill="#ffedd5"/>')
s.raw(f'<rect x="{X(1)}" y="{yl-30}" width="{X(2)-X(1)}" height="60" fill="#fee2e2"/>')
s.t((X(-1)+X(0))/2, yl + 7, 'Generating', 19, '#1d4ed8', 'bold')
s.t((X(0)+X(1))/2, yl + 7, 'Motoring', 19, A2, 'bold')
s.t((X(1)+X(2))/2, yl + 7, 'Braking', 19, '#b91c1c', 'bold')
s.ln(x0, yl + 30, x1, yl + 30, INK, 2.5)
for v, lab in [(-1, 'minus 1'), (0, '0'), (1, '1'), (2, '2')]:
    s.ln(X(v), yl + 24, X(v), yl + 38, INK, 2.5); s.t(X(v), yl + 60, lab, 18, INK, 'bold')
s.t(X(0), yl + 84, 'Never reached', 17, GREY); s.t(X(1), yl + 84, 'Rotor at standstill', 17, GREY)
s.t(400, 92, 'Slip S = (Ns − Nr) ÷ Ns', 20, INK, 'bold')
# table
cols = ['Poles at 50 Hz', 'Ns (rpm)', 'Nr (rpm)', 'Slip', 'fr (Hz)']
rows = [['2', '3000', '2940', '2%', '1'], ['4', '1500', '1470', '2%', '1'], ['6', '1000', '960', '4%', '2'], ['8', '750', '720', '4%', '2']]
cw = [190, 130, 130, 110, 110]; tx = 65; ty = 290
x = tx
for c, w in zip(cols, cw):
    s.raw(f'<rect x="{x}" y="{ty}" width="{w}" height="44" fill="{A}" stroke="#ffffff"/>'); s.t(x + w/2, ty + 29, c, 18, '#ffffff', 'bold'); x += w
for r, row in enumerate(rows):
    x = tx; yy = ty + 44 + r*44
    for c, w in zip(row, cw):
        s.raw(f'<rect x="{x}" y="{yy}" width="{w}" height="44" fill="{L if r % 2 == 0 else "#ffffff"}" stroke="#fed7aa"/>'); s.t(x + w/2, yy + 29, c, 18, INK); x += w
s.t(400, 535, 'Rotor frequency fr = S × f. Slip rises as load rises.', 18, GREY)
fig(slug, 'induction-motor-slip-values-modes-infographic',
    'slip values chart with generating, motoring and braking modes and a 2 to 8 pole table',
    'Diagram by Instrumentation Blog showing what negative, zero, one and greater than one slip mean, with Ns, Nr, slip and rotor frequency for 2, 4, 6 and 8 pole motors.',
    'Why Slip Matters: What Each Value Means', s.svg())

# ============ 2. NAMUR NE43 (purple) ============
A, A2, L = '#6d28d9', '#5b21b6', '#f5f3ff'
slug = 'namur-ne43-standard-explained'
s = S(520, 'NAMUR NE43 loop from smart transmitter to PLC or DCS analog input with fault actions')
s.head('NAMUR NE43 in a 4 to 20 mA Loop', A2)
s.box(30, 90, 150, 90, ['Sensor', 'pressure, flow', 'or level'], '#ffffff', INK, size=17)
s.ar(182, 135, 222, 135, INK)
s.box(225, 80, 230, 110, ['Smart transmitter', 'self diagnostics', 'detects faults'], L, A, size=18)
s.box(560, 80, 210, 110, ['PLC or DCS', 'analog input', 'reads 0 to 22 mA'], '#eef6ff', INK, size=18)
# loop wires
s.ln(455, 110, 560, 110, A, 3); s.ln(455, 160, 560, 160, A, 3)
s.ar(500, 110, 540, 110, A, 3); s.ar(540, 160, 500, 160, A, 3)
s.t(507, 96, 'loop', 17, A2, 'bold'); s.t(507, 185, 'current', 17, A2, 'bold')
# fail mode boxes
s.t(225, 234, 'Fail mode on a hardware fault', 18, A2, 'bold', 'start')
s.box(225, 245, 110, 70, ['Upscale', '21 mA'], '#fee2e2', '#b91c1c', size=18)
s.box(340, 245, 105, 70, ['Downscale', '3.6 mA'], '#fef3c7', '#b45309', size=18)
s.ln(340, 190, 340, 214, A, 2, '6 4')
s.box(30, 340, 360, 110, ['2 wire transmitter: use upscale', 'Loop powered device needs a', 'minimum current to operate'], '#ffffff', A, size=17)
s.box(30, 460, 360, 46, ['4 wire transmitter: either mode works'], '#ffffff', A, size=17)
# actions
s.ar(665, 192, 665, 240, INK)
s.t(665, 262, 'On a confirmed fault', 19, INK, 'bold')
for i, a in enumerate(['Trigger alarm, call maintenance', 'Switch loop to manual mode', 'Adjust or stop production']):
    s.box(475, 280 + i*72, 300, 60, [a], '#eef6ff', INK, size=17, bold_first=False)
fig(slug, 'namur-ne43-standard-loop-fail-mode-diagram',
    'NAMUR NE43 loop diagram with smart transmitter fail modes and DCS fault actions',
    'Diagram by Instrumentation Blog showing a NAMUR NE43 loop where a smart transmitter drives 21 mA or 3.6 mA on a fault and the PLC or DCS raises alarms.',
    'Fail-Safe Modes in Transmitters', s.svg())

s = S(600, 'Flowchart of PLC or DCS interpretation of NAMUR NE43 signal levels')
s.head('How a PLC or DCS Reads a NAMUR NE43 Signal', A2)
s.box(290, 58, 220, 50, ['Read loop current I'], L, A, size=19)
s.ar(400, 110, 400, 132)
s.dia(400, 180, 330, 92, ['I at or below 3.6 mA', 'or at or above 21 mA?'], '#fee2e2', '#b91c1c', 18)
s.t(588, 206, 'Yes', 18, '#b91c1c', 'bold')
s.ar(565, 180, 610, 180)
s.box(612, 140, 170, 80, ['Persists 4 s', 'and 2 scans?'], '#fff7ed', '#b45309', size=18)
s.ar(697, 222, 697, 270); s.t(718, 252, 'Yes', 18, '#b91c1c', 'bold')
s.box(612, 272, 170, 110, ['Hardware fault', 'alarm, manual', 'mode, act'], '#b91c1c', '#7f1d1d', '#ffffff', size=18)
s.pl([(697, 138), (697, 83), (512, 83)], GREY, 2, dash='6 4')
s.t(640, 74, 'No, keep reading', 17, GREY, 'bold')
s.t(420, 248, 'No', 18, INK, 'bold')
s.ar(400, 227, 400, 268)
s.dia(400, 318, 300, 92, ['I between', '4 and 20 mA?'], '#ecfdf5', '#047857', 18)
s.ar(250, 318, 200, 318); s.t(225, 305, 'Yes', 18, '#047857', 'bold')
s.box(20, 278, 178, 80, ['Normal', 'valid value'], '#047857', '#065f46', '#ffffff', size=19)
s.ar(400, 365, 400, 400); s.t(420, 390, 'No', 18, INK, 'bold')
s.dia(400, 450, 320, 92, ['3.8 to 4 mA or', '20 to 20.5 mA?'], '#fef3c7', '#b45309', 18)
s.ar(240, 450, 200, 450); s.t(220, 437, 'Yes', 18, '#b45309', 'bold')
s.box(20, 405, 178, 90, ['Saturation', 'process out', 'of range'], '#fef3c7', '#b45309', size=18)
s.ar(400, 497, 400, 520); s.t(420, 515, 'No', 18, INK, 'bold')
s.box(220, 522, 360, 64, ['Undefined zone', 'treat as a valid measurement'], L, A, size=18)
fig(slug, 'namur-ne43-standard-dcs-interpretation-flowchart',
    'flowchart showing how a PLC or DCS sorts NAMUR NE43 normal, saturation and fault signals',
    'Diagram by Instrumentation Blog showing the NAMUR NE43 decision logic in a PLC or DCS: normal range, saturation, undefined zones and a fault confirmed after 4 seconds and two scans.',
    'Interpretation by PLC and DCS Systems', s.svg())

s = S(470, 'NAMUR NE43 signal zones from fault low to fault high')
s.head('NAMUR NE43 Signal Zones (not to scale)', A2)
ws = [(85, '#fecaca', '#b91c1c', ['Fault', 'low']), (95, '#e5e7eb', GREY, ['Undefined', 'zone']), (110, '#fde68a', '#b45309', ['Saturation', 'zone']),
      (140, '#bbf7d0', '#047857', ['Normal', 'measurement']), (110, '#fde68a', '#b45309', ['Saturation', 'zone']), (95, '#e5e7eb', GREY, ['Undefined', 'zone']), (85, '#fecaca', '#b91c1c', ['Fault', 'high'])]
x = 40; edges = []
for w, f, c, ls in ws:
    s.raw(f'<rect x="{x}" y="90" width="{w}" height="100" fill="{f}" stroke="#ffffff" stroke-width="2"/>')
    s.t(x + w/2, 133, ls[0], 17, c, 'bold'); s.t(x + w/2, 158, ls[1], 17, c, 'bold')
    x += w; edges.append(x)
for x, lab in zip(edges[:6], ['3.6', '3.8', '4', '20', '20.5', '21']):
    s.ln(x, 190, x, 208, INK, 2.5); s.t(x, 230, lab, 18, INK, 'bold')
s.t(400, 256, 'Loop current in mA', 18, GREY)
cards = [('#047857', '#ecfdf5', ['4 to 20 mA', 'Healthy transmitter,', 'value in range']),
         ('#b45309', '#fffbeb', ['3.8 to 4, 20 to 20.5', 'Instrument works,', 'process out of range']),
         ('#b91c1c', '#fef2f2', ['3.6 or below, 21 or above', 'Transmitter itself', 'has failed'])]
for i, (c, f, ls) in enumerate(cards):
    s.box(30 + i*250, 285, 240, 110, ls, f, c, size=17)
s.t(400, 435, 'A fault must persist at least 4 s and two scan cycles before it is confirmed.', 17, GREY)
fig(slug, 'namur-ne43-standard-signal-zones-infographic',
    'NAMUR NE43 standard signal zones chart for 4 to 20 mA normal, saturation and fault levels',
    'Diagram by Instrumentation Blog showing the NAMUR NE43 current zones: fault at 3.6 mA or below, saturation to 3.8 and 20.5 mA, normal 4 to 20 mA and fault at 21 mA.',
    'Signal Zones Defined by NAMUR NE43', s.svg())

# ============ 3. RTD resistance to temperature (teal) ============
A, A2, L = '#0f766e', '#115e59', '#f0fdfa'
slug = 'rtd-resistance-to-temperature-calculator'
s = S(500, 'Two wire RTD lead resistance error with 50 m of 1.5 mm2 copper cable')
s.head('Lead Wire Error in a 2 Wire PT100', A2)
# RTD element left
s.raw(f'<rect x="60" y="150" width="60" height="170" rx="8" fill="{L}" stroke="{A}" stroke-width="3"/>')
s.raw(f'<polyline points="90,165 75,180 105,195 75,210 105,225 75,240 105,255 75,270 105,285 90,300" fill="none" stroke="{A2}" stroke-width="3"/>')
s.t(90, 140, 'PT100', 19, A2, 'bold'); s.t(90, 345, 'Rt', 19, A2, 'bold')
# leads
for y, lab in [(165, 'Lead 1: 50 m × 0.0119 = 0.595 Ω'), (305, 'Lead 2: 50 m × 0.0119 = 0.595 Ω')]:
    s.ln(120, y, 560, y, '#b45309', 4)
    s.raw(f'<rect x="270" y="{y-12}" width="70" height="24" fill="#fef3c7" stroke="#b45309" stroke-width="2"/>')
    s.t(340, y - 22 if y < 200 else y + 38, lab, 18, '#92400e', 'bold')
s.box(560, 130, 210, 210, ['Transmitter', 'measures', 'Rt + 1.19 Ω'], '#eef6ff', INK, size=19)
s.t(250, 240, 'Field', 18, GREY, 'bold'); s.t(470, 240, '50 m cable', 18, GREY, 'bold')
s.box(40, 395, 350, 80, ['PT100 error', '1.19 ÷ 0.385 = +3.1 °C high'], '#fee2e2', '#b91c1c', size=18)
s.box(410, 395, 350, 80, ['PT1000 error', '1.19 ÷ 3.851 = 0.31 °C'], L, A, size=18)
fig(slug, 'rtd-resistance-to-temperature-lead-wire-error-diagram',
    'two wire PT100 circuit showing 1.19 ohm lead resistance adding a 3.1 degree error',
    'Diagram by Instrumentation Blog showing how 50 m of 1.5 mm2 copper adds 1.19 ohm to a 2 wire RTD, reading 3.1 °C high on a PT100 but 0.31 °C on a PT1000.',
    'Lead Wire Resistance Error: Why 2-Wire RTDs Give Wrong Readings', s.svg())

s = S(600, 'Flowchart to convert RTD resistance to temperature with linear or Callendar Van Dusen formula')
s.head('Which RTD Formula Should You Use?', A2)
s.box(260, 58, 280, 54, ['Measured resistance Rt'], L, A, size=19)
s.ar(400, 114, 400, 136)
s.dia(400, 180, 300, 84, ['Sensor type?'], '#fef3c7', '#b45309', 19)
s.box(20, 150, 180, 60, ['PT100', 'R0 = 100 Ω'], '#ffffff', A, size=18); s.ar(250, 180, 202, 180)
s.box(600, 150, 180, 60, ['PT1000', 'R0 = 1000 Ω'], '#ffffff', A, size=18); s.ar(550, 180, 598, 180)
s.ar(400, 224, 400, 250)
s.dia(400, 300, 380, 96, ['Between minus 50 °C', 'and 150 °C?'], '#fef3c7', '#b45309', 19)
s.pl([(210, 300), (210, 345)], A2); s.t(180, 290, 'Yes', 18, A2, 'bold')
s.pl([(590, 300), (590, 345)], '#b91c1c'); s.t(625, 290, 'No', 18, '#b91c1c', 'bold')
s.box(30, 348, 360, 110, ['Linear formula', 'T = (Rt − R0) ÷ (α × R0)', 'α = 0.00385, error under 0.5 °C'], '#ecfdf5', A, size=18)
s.box(410, 348, 360, 110, ['Callendar Van Dusen', 'R0(1 + AT + BT²) = Rt for T ≥ 0 °C', 'A = 0.0039083, B = −0.0000005775'], '#fef2f2', '#b91c1c', size=18)
s.box(30, 478, 360, 100, ['Example: 119.40 Ω', '19.40 ÷ 0.385 = 50.39 °C'], '#ffffff', A, size=18)
s.box(410, 478, 360, 100, ['Example: 175.00 Ω', 'CVD 197.7 °C, linear 194.8 °C'], '#ffffff', '#b91c1c', size=18)
fig(slug, 'rtd-resistance-to-temperature-formula-flowchart',
    'flowchart for choosing the linear RTD formula or Callendar Van Dusen equation',
    'Diagram by Instrumentation Blog showing when to use the linear RTD formula and when to use the Callendar Van Dusen equation, with the 119.40 and 175 ohm worked examples.',
    'The Callendar-Van Dusen Equation: Accurate Calculation for Wide Ranges', s.svg())

s = S(540, 'PT100 resistance versus temperature chart from IEC 60751 table values')
s.head('PT100 Resistance vs Temperature (IEC 60751)', A2)
pts = [(-200, 18.52), (-100, 60.26), (-50, 80.31), (0, 100.0), (50, 119.40), (100, 138.51), (150, 157.33), (200, 175.86), (300, 212.05), (400, 247.09), (500, 280.98), (600, 313.71)]
gx0, gx1, gy0, gy1 = 110, 520, 450, 80
def PX(t): return gx0 + (t + 200) / 800 * (gx1 - gx0)
def PY(r): return gy0 - r / 350 * (gy0 - gy1)
for r in range(0, 351, 50):
    s.ln(gx0, PY(r), gx1, PY(r), '#e5e7eb', 1); s.t(gx0 - 10, PY(r) + 6, str(r), 17, GREY, 'normal', 'end')
for t, lab in [(-200, 'minus 200'), (0, '0'), (200, '200'), (400, '400'), (600, '600')]:
    s.ln(PX(t), gy0, PX(t), gy0 + 8, INK, 2); s.t(PX(t), gy0 + 30, lab, 17, GREY)
s.ln(gx0, gy0, gx1, gy0, INK, 2); s.ln(gx0, gy0, gx0, gy1, INK, 2)
s.t(315, gy0 + 60, 'Temperature in °C', 18, INK, 'bold')
s.raw(f'<text x="40" y="265" font-size="18" fill="{INK}" font-weight="bold" text-anchor="middle" transform="rotate(-90 40 265)">Resistance in Ω</text>')
s.pl([(PX(t), PY(r)) for t, r in pts], A, 3.5, arrow=False)
for t, r in pts: s.raw(f'<circle cx="{PX(t):.1f}" cy="{PY(r):.1f}" r="5" fill="{A2}"/>')
s.raw(f'<circle cx="{PX(0):.1f}" cy="{PY(100):.1f}" r="8" fill="none" stroke="#b91c1c" stroke-width="3"/>')
cards = [['0 °C', '100.00 Ω'], ['100 °C', '138.51 Ω'], ['200 °C', '175.86 Ω'], ['600 °C', '313.71 Ω']]
for i, c in enumerate(cards):
    s.box(560, 80 + i*84, 210, 70, c, L if i % 2 == 0 else '#ffffff', A, size=19)
s.box(560, 420, 210, 70, ['PT1000', '10 × these values'], '#fff7ed', '#b45309', size=18)
fig(slug, 'rtd-resistance-to-temperature-pt100-curve-chart',
    'RTD resistance to temperature curve for PT100 from minus 200 to 600 degrees Celsius',
    'Diagram by Instrumentation Blog plotting PT100 resistance against temperature from the IEC 60751 table, from 18.52 ohm at minus 200 °C to 313.71 ohm at 600 °C.',
    'PT100 Resistance Reference Table (IEC 60751)', s.svg())

# ============ 4. Star delta transformation (blue) ============
A, A2, L = '#1d4ed8', '#1e3a8a', '#eff6ff'
slug = 'star-delta-transformation-formula'
def res(x1, y1, x2, y2, lab, lx, ly, col=A):
    # resistor as a rotated rectangle on the line midpoint
    mx, my = (x1 + x2)/2, (y1 + y2)/2
    ang = math.degrees(math.atan2(y2 - y1, x2 - x1))
    s.ln(x1, y1, x2, y2, INK, 2.5)
    s.raw(f'<rect x="{mx-30}" y="{my-11}" width="60" height="22" fill="#ffffff" stroke="{col}" stroke-width="3" transform="rotate({ang:.1f} {mx} {my})"/>')
    s.t(lx, ly, lab, 18, A2, 'bold')
def node(x, y, lab, dx=0, dy=-16):
    s.raw(f'<circle cx="{x}" cy="{y}" r="7" fill="{INK}"/>'); s.t(x + dx, y + dy, lab, 20, INK, 'bold')
s = S(520, 'Delta to star conversion with 500, 300 and 400 ohm example')
s.head('Delta to Star Conversion Example', A2)
# delta left: A top, B bottom left, C bottom right
Ax, Ay, Bx, By, Cx, Cy = 200, 100, 70, 330, 330, 330
res(Ax, Ay, Bx, By, 'RAB 500 Ω', 70, 205)
res(Bx, By, Cx, Cy, 'RBC 300 Ω', 200, 370)
res(Cx, Cy, Ax, Ay, 'RCA 400 Ω', 335, 205)
node(Ax, Ay, 'A'); node(Bx, By, 'B', -22, 8); node(Cx, Cy, 'C', 22, 8)
s.ar(380, 230, 440, 230, A, 4)
# star right
Ax2, Ay2, Bx2, By2, Cx2, Cy2, Ox, Oy = 600, 100, 470, 330, 730, 330, 600, 245
res(Ax2, Ay2, Ox, Oy, 'RA 166.67 Ω', 690, 165)
res(Bx2, By2, Ox, Oy, 'RB 125 Ω', 470, 270)
res(Cx2, Cy2, Ox, Oy, 'RC 100 Ω', 735, 270)
node(Ax2, Ay2, 'A'); node(Bx2, By2, 'B', -22, 8); node(Cx2, Cy2, 'C', 22, 8)
s.raw(f'<circle cx="{Ox}" cy="{Oy}" r="6" fill="{A}"/>')
s.t(200, 405, 'Delta (Δ)', 20, INK, 'bold'); s.t(600, 405, 'Star (Y)', 20, INK, 'bold')
s.box(40, 425, 720, 80, ['Sum = 500 + 300 + 400 = 1200 Ω', 'RA = 500 × 400 ÷ 1200, RB = 500 × 300 ÷ 1200, RC = 300 × 400 ÷ 1200'], L, A, size=18)
fig(slug, 'star-delta-transformation-delta-to-star-diagram',
    'star delta transformation diagram converting a 500, 300 and 400 ohm delta to a star',
    'Diagram by Instrumentation Blog showing a delta of 500, 300 and 400 ohm converted to an equivalent star of 166.67, 125 and 100 ohm using product over sum.',
    'Delta to Star Conversion Formula', s.svg())

s = S(580, 'Six step flowchart to solve an unbalanced bridge network with star delta transformation')
s.head('6 Steps to Solve a Bridge Network', A2)
steps = [('1', 'Label nodes', 'A top, D bottom, B and C sides'),
         ('2', 'Pick a delta', 'Upper triangle 20, 30, 50 Ω'),
         ('3', 'Convert', 'RA 6 Ω, RB 10 Ω, RC 15 Ω'),
         ('4', 'Redraw', 'Star replaces the upper delta'),
         ('5', 'Reduce', '40 Ω parallel 40 Ω, plus 6 = 26 Ω'),
         ('6', 'Back solve', '26 V ÷ 26 Ω = 1 A supply current')]
for i, (n, h, d) in enumerate(steps):
    col, row = i // 3, i % 3
    x = 40 + col * 380; y = 70 + row * 160
    s.raw(f'<rect x="{x}" y="{y}" width="340" height="120" rx="12" fill="{L if (i % 2 == 0) else "#ffffff"}" stroke="{A}" stroke-width="2.5"/>')
    s.raw(f'<circle cx="{x+38}" cy="{y+38}" r="22" fill="{A}"/>'); s.t(x + 38, y + 45, n, 20, '#ffffff', 'bold')
    s.t(x + 72, y + 45, h, 21, A2, 'bold', 'start')
    s.t(x + 170, y + 92, d, 17, INK)
    if row < 2: s.ar(x + 170, y + 122, x + 170, y + 156, A2)
s.pl([(380, 450), (400, 450), (400, 130), (418, 130)], A2)
fig(slug, 'star-delta-transformation-bridge-steps-flowchart',
    'six step flowchart to solve an unbalanced bridge using star delta transformation',
    'Diagram by Instrumentation Blog showing the six steps to solve a bridge network: label nodes, pick a delta, convert, redraw, reduce and back solve with the worked example values.',
    '6 Steps to Solve a Bridge Network', s.svg())

s = S(560, 'Solved unbalanced bridge example using star delta transformation')
s.head('Worked Example: Unbalanced Bridge Solved', A2)
# reduced circuit: A top, star centre O, B branch and C branch to D
Ax, Ay, Ox, Oy = 210, 80, 210, 170
Bx, By, Cx, Cy, Dx, Dy = 110, 260, 310, 260, 210, 440
res(Ax, Ay, Ox, Oy, 'RA 6 Ω', 130, 130)
s.ln(Ox, Oy, Bx, Oy + 20, INK, 2.5); s.ln(Ox, Oy, Cx, Oy + 20, INK, 2.5)
res(Bx, 190, Bx, 260, '', 0, 0); s.t(50, 232, 'RB 10 Ω', 18, A2, 'bold')
res(Cx, 190, Cx, 260, '', 0, 0); s.t(370, 232, 'RC 15 Ω', 18, A2, 'bold')
res(Bx, 260, Bx, 400, '', 0, 0); s.t(45, 336, 'RBD 30 Ω', 18, A2, 'bold')
res(Cx, 260, Cx, 400, '', 0, 0); s.t(372, 336, 'RCD 25 Ω', 18, A2, 'bold')
s.ln(Bx, 400, Cx, 400, INK, 2.5); s.ln(Dx, 400, Dx, Dy, INK, 2.5)
node(Ax, Ay, 'A', 22, 6); node(Dx, Dy, 'D', 22, 8)
node(Bx, 260, 'B', 22, 26); node(Cx, 260, 'C', -22, 26)
s.t(210, 495, '26 V supply across A and D', 18, GREY)
# results panel
rows = [['Upper delta sum', '20 + 30 + 50 = 100 Ω'], ['Each branch', '10 + 30 = 15 + 25 = 40 Ω'], ['Total RAD', '6 + (40 parallel 40) = 26 Ω'],
        ['Supply current', '26 ÷ 26 = 1 A, 0.5 A per arm'], ['Node voltages', 'VB = 15 V, VC = 12.5 V'], ['Bridge current', '(15 − 12.5) ÷ 50 = 0.05 A']]
for i, (h, v) in enumerate(rows):
    y = 70 + i * 76
    s.raw(f'<rect x="435" y="{y}" width="345" height="66" rx="10" fill="{A if i == 5 else (L if i % 2 == 0 else "#ffffff")}" stroke="{A}" stroke-width="2"/>')
    tc = '#ffffff' if i == 5 else INK
    s.t(607, y + 26, h, 18, tc, 'bold'); s.t(607, y + 52, v, 18, tc)
fig(slug, 'star-delta-transformation-bridge-example-infographic',
    'solved bridge network example with star equivalent, 26 ohm total and 0.05 A bridge current',
    'Diagram by Instrumentation Blog showing the unbalanced bridge solved by star delta transformation: 26 ohm total, 1 A supply current and 0.05 A in the 50 ohm bridge resistor.',
    'Worked Example: Unbalanced Bridge', s.svg())

# ============ 5. Temperature sensor response time (red) ============
A, A2, L = '#b91c1c', '#991b1b', '#fef2f2'
slug = 'temperature-sensor-response-time'
s = S(520, 'Heat path from process fluid through thermowell and air gap into the temperature sensor')
s.head('Why a Thermowell Slows Response Time', A2)
# pipe flow band
s.raw('<rect x="40" y="300" width="420" height="170" fill="#dbeafe" stroke="#1d4ed8" stroke-width="2"/>')
for y in (340, 390, 440): s.ar(60, y, 150, y, '#1d4ed8', 3)
s.t(100, 325, 'Hot fluid', 18, '#1d4ed8', 'bold')
s.raw('<rect x="40" y="280" width="420" height="20" fill="#9ca3af"/>')
# thermowell
s.raw(f'<path d="M190 70 L190 430 Q250 470 310 430 L310 70 Z" fill="#d1d5db" stroke="{INK}" stroke-width="2.5"/>')
s.raw(f'<path d="M215 70 L215 418 Q250 444 285 418 L285 70 Z" fill="#ffffff" stroke="{INK}" stroke-width="1.5"/>')
s.raw(f'<rect x="232" y="70" width="36" height="338" rx="12" fill="#f3f4f6" stroke="{A}" stroke-width="2.5"/>')
s.raw(f'<rect x="240" y="350" width="20" height="48" rx="6" fill="{A}"/>')
# heat arrows into well
for y in (360, 400): s.ar(160, y, 186, y, A, 3)
labels = [(120, 'Thermowell wall', 298), (170, 'Air gap', 278), (220, 'Sensor sheath', 268), (360, 'Sensing element', 260)]
for y, lab, xe in labels:
    s.t(470, y + 6, lab, 18, INK, 'bold', 'start'); s.ln(465, y, xe, y, '#9ca3af', 1.5)
s.box(470, 245, 310, 85, ['Heat must cross every', 'layer, so each one', 'adds lag'], L, A, size=17)
s.box(470, 392, 310, 116, ['Typical t90', 'Fast RTD direct: 1.5 s', 'Sheathed RTD: 9.5 s', 'In thermowell: 40 s'], '#ffffff', A, size=17)
s.t(250, 500, 'Fill the air gap with conductive paste', 17, GREY)
fig(slug, 'temperature-sensor-response-time-thermowell-diagram',
    'thermowell cross section showing heat path through wall, air gap and sheath to the sensor',
    'Diagram by Instrumentation Blog showing heat passing from the process fluid through the thermowell wall, air gap and sheath, which raises RTD t90 from 9.5 s to about 40 s.',
    'Real Response Times: Sensor to Thermowell', s.svg())

s = S(560, 'Flowchart comparing the plunge test and LCSR method for response time testing')
s.head('Plunge Test vs LCSR: Test Sequence', A2)
cols = [(40, 'Plunge test (lab)', '#1d4ed8', '#eff6ff', ['Remove sensor', 'from the process', ], ['Plunge into water', 'at set velocity'], ['Record the', 'step response'], ['Time to 63.2%', 'gives τ']),
        (420, 'LCSR (in service)', A, L, ['Sensor stays', 'installed'], ['Current step self', 'heats the element'], ['Record heating and', 'cooling transient'], ['Gives installed', 'response time'])]
for x, h, c, f, *steps in cols:
    s.raw(f'<rect x="{x}" y="62" width="340" height="50" rx="10" fill="{c}"/>'); s.t(x + 170, 95, h, 21, '#ffffff', 'bold')
    for i, ls in enumerate(steps):
        y = 128 + i * 90
        s.box(x + 30, y, 280, 68, ls, f, c, size=18, bold_first=False)
        if i < 3: s.ar(x + 170, y + 70, x + 170, y + 88, c)
s.box(140, 515 - 20, 520, 52, ['LCSR results agree with plunge tests within about 10%'], '#ffffff', INK, size=17, bold_first=False)
fig(slug, 'temperature-sensor-response-time-plunge-lcsr-flowchart',
    'flowchart comparing plunge test and LCSR loop current step response testing of RTD sensors',
    'Diagram by Instrumentation Blog comparing the plunge test done in a lab with the in service LCSR method that self heats the RTD element to measure installed response time.',
    'Plunge Test vs LCSR: How Response Time Is Actually Measured', s.svg())

s = S(540, 'Temperature sensor step response curve with t50, time constant and t90 for tau of 10 seconds')
s.head('Temperature Sensor Response Time: τ = 10 s', A2)
gx0, gx1, gy0, gy1 = 90, 500, 440, 90
T = 40
def RX(t): return gx0 + t / T * (gx1 - gx0)
def RY(p): return gy0 - p / 100 * (gy0 - gy1)
for p in (0, 25, 50, 75, 100):
    s.ln(gx0, RY(p), gx1, RY(p), '#e5e7eb', 1); s.t(gx0 - 10, RY(p) + 6, f'{p}%', 17, GREY, 'normal', 'end')
for t in (0, 10, 20, 30, 40):
    s.t(RX(t), gy0 + 28, str(t), 17, GREY)
s.ln(gx0, gy0, gx1, gy0, INK, 2); s.ln(gx0, gy0, gx0, gy1, INK, 2)
s.t(295, gy0 + 58, 'Time in seconds', 18, INK, 'bold')
pts = [(RX(t/4), RY(100*(1-math.exp(-(t/4)/10)))) for t in range(0, 161)]
s.pl(pts, A, 3.5, arrow=False)
for t, p, lab, dy in [(6.93, 50, 't50 6.93 s', -12), (10, 63.2, 'τ 10 s', -12), (23.03, 90, 't90 23.0 s', -14)]:
    s.ln(RX(t), gy0, RX(t), RY(p), '#9ca3af', 1.5, '5 4'); s.ln(gx0, RY(p), RX(t), RY(p), '#9ca3af', 1.5, '5 4')
    s.raw(f'<circle cx="{RX(t):.1f}" cy="{RY(p):.1f}" r="6" fill="{A2}"/>')
    s.t(RX(t) + 12, RY(p) + 24, lab, 17, A2, 'bold', 'start')
s.box(530, 85, 245, 90, ['Time constant', 'τ = ρVCp ÷ hA'], L, A, size=19)
s.box(530, 190, 245, 70, ['t50 = 0.693 τ', '= 6.93 s'], '#ffffff', A, size=18)
s.box(530, 275, 245, 70, ['t63.2 = 1.000 τ', '= 10 s'], '#ffffff', A, size=18)
s.box(530, 360, 245, 70, ['t90 = 2.303 τ', '= 23.0 s'], A, A2, '#ffffff', size=18)
s.t(400, 520, 'Same exponential law as an RC circuit: output = step × (1 − e^(−t/τ))', 17, GREY)
fig(slug, 'temperature-sensor-response-time-step-response-chart',
    'temperature sensor response time curve showing t50, time constant and t90 for tau 10 seconds',
    'Diagram by Instrumentation Blog plotting a sensor step response with a 10 second time constant, marking t50 at 6.93 s, 63.2 percent at 10 s and t90 at 23.0 s.',
    'The Thermal Time Constant Formula', s.svg())

for slug, figs in CH.items():
    json.dump({'slug': slug, 'figs': figs}, open(f'{OUT}/{slug}.json', 'w'), ensure_ascii=False, indent=1)
print('ok', {k: len(v) for k, v in CH.items()})
