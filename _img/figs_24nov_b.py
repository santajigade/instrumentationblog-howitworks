import sys; sys.path.insert(0, '/home/claude/instrumentationblog-howitworks/_img'); from figs_24nov_common import *
import math

def res_h(s, x1, x2, y, c, n=6, a=12):
    """horizontal zigzag resistor from x1 to x2"""
    lead = (x2 - x1) * 0.15; xa, xb = x1 + lead, x2 - lead
    pts = [(x1, y), (xa, y)]
    st = (xb - xa) / n
    for i in range(n):
        pts.append((xa + st * (i + 0.5), y + (a if i % 2 == 0 else -a)))
    pts += [(xb, y), (x2, y)]
    s.pl(pts, c, 3, False)
def gnd(s, x, y, c='#1a2b4a'):
    s.ln(x - 18, y, x + 18, y, c, 3); s.ln(x - 11, y + 7, x + 11, y + 7, c, 3); s.ln(x - 4, y + 14, x + 4, y + 14, c, 3)
def dim(s, x, y1, y2, c='#1a2b4a'):
    m = (y1 + y2) / 2; s.ar(x, m, x, y1 + 2, c, 2); s.ar(x, m, x, y2 - 2, c, 2)

# ================= 1. Logic gates =================
slug = 'digital-logic-gates-explained'
A, A2, L = '#4f46e5', '#312e81', '#eef2ff'
def nor(s, x, y, lab):
    s.raw(f'<path d="M{x} {y-32} Q{x+26} {y} {x} {y+32} Q{x+52} {y+32} {x+84} {y} Q{x+52} {y-32} {x} {y-32} Z" fill="{L}" stroke="{A2}" stroke-width="2.5"/>')
    s.raw(f'<circle cx="{x+91}" cy="{y}" r="7" fill="#ffffff" stroke="{A2}" stroke-width="2.5"/>')
    s.t(x + 40, y - 42, lab, 17, A2, 'bold')
s = S(520, 'AND gate built from three NOR gates')
s.head('Making an AND Gate From Three NOR Gates', A2)
nor(s, 220, 150, 'NOR 1'); nor(s, 220, 340, 'NOR 2'); nor(s, 470, 245, 'NOR 3')
for y, lab in [(150, 'A'), (340, 'B')]:
    s.t(50, y + 7, lab, 22, A2, 'bold')
    s.ln(70, y, 150, y, '#1a2b4a', 2.5)
    s.raw(f'<circle cx="150" cy="{y}" r="5" fill="#1a2b4a"/>')
    s.pl([(150, y), (150, y - 15), (230, y - 15)], '#1a2b4a', 2.5, False)
    s.pl([(150, y), (150, y + 15), (230, y + 15)], '#1a2b4a', 2.5, False)
s.pl([(318, 150), (400, 150), (400, 230), (480, 230)], A, 3, False); s.t(350, 140, "A'", 20, A, 'bold')
s.pl([(318, 340), (400, 340), (400, 260), (480, 260)], A, 3, False); s.t(350, 330, "B'", 20, A, 'bold')
s.ar(568, 245, 650, 245, A2, 3); s.t(665, 252, 'Y = A·B', 22, A2, 'bold', 'start')
s.t(120, 210, 'Both inputs tied: NOT A', 17, '#4b5563', 'normal', 'start')
s.t(120, 400, 'Both inputs tied: NOT B', 17, '#4b5563', 'normal', 'start')
s.t(400, 445, "(A' + B')' = A·B by De Morgan's theorem", 19, '#1a2b4a', 'bold')
for i, (ab, y) in enumerate([('00', '0'), ('01', '0'), ('10', '0'), ('11', '1')]):
    x = 130 + i * 140
    s.raw(f'<rect x="{x}" y="465" width="120" height="40" rx="8" fill="{A if y == "1" else "#ffffff"}" stroke="{A}" stroke-width="2"/>')
    s.t(x + 60, 492, f'AB {ab}: Y {y}', 17, '#ffffff' if y == '1' else A2, 'bold')
fig(slug, 'logic-gates-and-gate-from-three-nor-gates-diagram',
    'logic gates diagram showing an AND gate built from three NOR gates',
    'Diagram by Instrumentation Blog showing how three NOR gates make an AND gate: two NOR gates invert A and B, and the third NORs them to give A·B.',
    'XAND Gate Meaning and How to Make AND Using NOR Gates', s.svg())

s = S(600, 'Flowchart to identify a logic gate from its truth table')
s.head('Identify the Gate From Its Truth Table', A2)
s.box(200, 50, 260, 42, ['Read the truth table'], L, A, size=18)
qs = [('One input only?', 'NOT: Ā'), ('Out 1 only when inputs differ?', 'XOR'),
      ('Out 1 only when inputs match?', 'XNOR'), ('Out 1 only when all inputs are 1?', 'AND: A·B'),
      ('Out 0 only when all inputs are 1?', 'NAND'), ('Out 1 only when all inputs are 0?', 'NOR')]
s.ar(330, 92, 330, 104)
for i, (q, r) in enumerate(qs):
    cy = 134 + i * 72
    s.dia(330, cy, 460, 58, [q], '#ffffff', A, 17)
    s.ar(560, cy, 612, cy, A, 2.5); s.t(586, cy - 8, 'Yes', 17, A, 'bold')
    s.box(614, cy - 22, 166, 44, [r], A if i % 2 == 0 else A2, A2, '#ffffff', size=18)
    if i < 5:
        s.ar(330, cy + 29, 330, cy + 43); s.t(345, cy + 42, 'No', 17, '#4b5563', 'normal', 'start')
s.ar(330, 134 + 5 * 72 + 29, 330, 538)
s.box(220, 538, 220, 44, ['Otherwise: OR'], L, A, size=18)
s.t(615, 565, 'NAND and NOR', 17, '#4b5563', 'bold', 'start'); s.t(615, 588, 'are universal', 17, '#4b5563', 'bold', 'start')
fig(slug, 'logic-gates-identify-from-truth-table-flowchart',
    'flowchart to identify AND, OR, NOT, NAND, NOR, XOR or XNOR from a truth table',
    'Diagram by Instrumentation Blog showing a decision flow that names a gate from its truth table by checking when the output is 1 or 0.',
    'Comparison of Basic Logic Gates', s.svg())

s = S(480, 'Truth table of all two input basic logic gates')
s.head('Truth Tables of the Basic Gates at a Glance', A2)
cols = ['A', 'B', 'AND', 'OR', 'NAND', 'NOR', 'XOR', 'XNOR']
rows = [(0, 0), (0, 1), (1, 0), (1, 1)]
f = {'AND': lambda a, b: a & b, 'OR': lambda a, b: a | b, 'NAND': lambda a, b: 1 - (a & b), 'NOR': lambda a, b: 1 - (a | b),
     'XOR': lambda a, b: a ^ b, 'XNOR': lambda a, b: 1 - (a ^ b)}
x0, cw, y0, rh = 40, 90, 64, 52
for j, c in enumerate(cols):
    s.raw(f'<rect x="{x0 + j*cw}" y="{y0}" width="{cw}" height="{rh}" fill="{A2 if j > 1 else "#475569"}" stroke="#ffffff" stroke-width="2"/>')
    s.t(x0 + j * cw + cw / 2, y0 + 33, c, 19, '#ffffff', 'bold')
for i, (a, b) in enumerate(rows):
    y = y0 + rh * (i + 1)
    for j, c in enumerate(cols):
        v = a if c == 'A' else b if c == 'B' else f[c](a, b)
        fill = '#f1f5f9' if j < 2 else (A if v else '#ffffff')
        s.raw(f'<rect x="{x0 + j*cw}" y="{y}" width="{cw}" height="{rh}" fill="{fill}" stroke="#c7d2fe" stroke-width="2"/>')
        s.t(x0 + j * cw + cw / 2, y + 34, str(v), 22, '#ffffff' if (j > 1 and v) else '#1a2b4a', 'bold')
s.raw(f'<rect x="40" y="345" width="220" height="110" rx="12" fill="{L}" stroke="{A}" stroke-width="2"/>')
s.t(150, 375, 'NOT gate', 19, A2, 'bold'); s.t(150, 405, 'A = 0 gives 1', 18); s.t(150, 433, 'A = 1 gives 0', 18)
s.raw(f'<rect x="280" y="345" width="480" height="110" rx="12" fill="#ffffff" stroke="{A}" stroke-width="2"/>')
s.t(520, 375, 'Shaded cells are output 1', 19, A2, 'bold')
s.t(520, 405, 'XNOR is XOR with the output inverted', 18)
s.t(520, 433, 'NAND and NOR invert AND and OR', 18)
fig(slug, 'logic-gates-truth-table-summary-infographic',
    'logic gates truth table for AND, OR, NAND, NOR, XOR and XNOR with NOT gate',
    'Diagram by Instrumentation Blog summarising the truth tables of the seven basic logic gates, with every output 1 cell shaded for quick comparison.',
    'The Seven Basic Logic Gates', s.svg())

# ================= 2. Inverting amplifier gain =================
slug = 'inverting-amplifier-gain-formula'
A, A2, L = '#059669', '#065f46', '#ecfdf5'
s = S(500, 'Inverting amplifier circuit with Rin 10 kilohm and Rf 100 kilohm')
s.head('Inverting Amplifier: Solved Example 1 Circuit', A2)
s.raw(f'<polygon points="430,190 430,330 560,260" fill="{L}" stroke="{A2}" stroke-width="3"/>')
s.t(447, 232, '−', 26, A2, 'bold'); s.t(447, 302, '+', 24, A2, 'bold')
s.raw('<circle cx="90" cy="225" r="7" fill="#ffffff" stroke="#1a2b4a" stroke-width="2.5"/>')
s.t(90, 200, 'Vin = 0.2 V', 18, '#1a2b4a', 'bold')
s.ln(97, 225, 150, 225); res_h(s, 150, 290, 225, A); s.t(220, 265, 'Rin = 10 kΩ', 18, A2, 'bold')
s.ln(290, 225, 430, 225)
s.raw('<circle cx="340" cy="225" r="6" fill="#1a2b4a"/>')
s.pl([(340, 225), (340, 120), (420, 120)], '#1a2b4a', 2.5, False); res_h(s, 420, 580, 120, A)
s.pl([(580, 120), (640, 120), (640, 260)], '#1a2b4a', 2.5, False); s.t(500, 92, 'Rf = 100 kΩ', 18, A2, 'bold')
s.ln(560, 260, 700, 260); s.raw('<circle cx="640" cy="260" r="6" fill="#1a2b4a"/>')
s.raw('<circle cx="707" cy="260" r="7" fill="#ffffff" stroke="#1a2b4a" stroke-width="2.5"/>')
s.t(700, 300, 'Vout =', 18, '#1a2b4a', 'bold'); s.t(700, 324, 'minus 2.0 V', 18, '#1a2b4a', 'bold')
s.pl([(430, 295), (390, 295), (390, 340)], '#1a2b4a', 2.5, False); gnd(s, 390, 340)
s.box(170, 300, 190, 60, ['Virtual ground', 'about 0 V'], '#ffffff', A, size=17)
s.ln(300, 300, 336, 232, '#9ca3af', 1.5, '4 4')
s.ar(160, 175, 270, 175, A, 2.5); s.t(215, 163, 'I = 20 µA', 17, A2, 'bold')
s.t(400, 420, 'Av = minus Rf ÷ Rin = minus 100 ÷ 10 = minus 10 (20 dB)', 19, '#1a2b4a', 'bold')
s.t(400, 452, 'Input impedance = Rin = 10 kΩ, output shifted by 180°', 18, '#4b5563')
fig(slug, 'inverting-amplifier-gain-virtual-ground-circuit-diagram',
    'inverting amplifier gain circuit with 10 kilohm Rin, 100 kilohm Rf and virtual ground',
    'Diagram by Instrumentation Blog showing the inverting op amp from Solved Example 1: Rin 10 kilohm, Rf 100 kilohm, 0.2 V in and minus 2.0 V out.',
    'Virtual Ground and Input Impedance', s.svg())

s = S(580, 'Flowchart to choose Rf and Rin for an inverting amplifier')
s.head('Choosing Rf and Rin: Design Flow', A2)
bx, bw = 50, 320
steps = [(62, ['1. Set the gain magnitude', 'from input and output range'], ['Example 2: 1.5 V peak in,', 'plus and minus 12 V supply']),
         (142, ['2. Pick Rin', 'often 4.7 kΩ to 10 kΩ'], ['Rin = 4.7 kΩ']),
         (222, ['3. Calculate Rf = gain × Rin', 'round to an E96 value'], ['First try Rf = 47 kΩ,', 'gain minus 10'])]
for y, ls, note in steps:
    s.box(bx, y, bw, 58, ls, L, A, size=17)
    for k, n in enumerate(note): s.t(420, y + 25 + k * 24, n, 18, A2, 'bold' if k == 0 else 'normal', 'start')
s.ar(210, 120, 210, 140); s.ar(210, 200, 210, 220); s.ar(210, 280, 210, 298)
s.dia(210, 342, 320, 88, ['4. Peak output', 'inside swing?'], '#ffffff', A, 17)
s.t(420, 330, '15 V peak exceeds 10.5 V: No', 18, '#b91c1c', 'bold', 'start')
s.t(420, 356, 'Rf = 22 kΩ gives 7.02 V peak: Yes', 18, A2, 'bold', 'start')
s.pl([(50, 342), (25, 342), (25, 251), (48, 251)], '#b91c1c', 2.5); s.t(30, 380, 'No', 17, '#b91c1c', 'bold', 'start')
s.ar(210, 386, 210, 410); s.t(222, 404, 'Yes', 17, A2, 'bold', 'start')
s.box(bx, 410, bw, 58, ['5. Check bandwidth', 'GBW ÷ (1 + Rf/Rin), keep margin'], L, A, size=17)
s.t(420, 435, 'Example 1: 1 MHz ÷ 11', 18, A2, 'bold', 'start'); s.t(420, 459, '= 90.9 kHz', 18, A2, 'normal', 'start')
s.ar(210, 468, 210, 488)
s.box(bx, 488, bw, 58, ['6. Add compensation', 'Rin parallel Rf on + input'], L, A, size=17)
s.t(420, 513, 'For bipolar op amps', 18, A2, 'bold', 'start'); s.t(420, 537, 'Final gain minus 4.68', 18, A2, 'normal', 'start')
fig(slug, 'inverting-amplifier-gain-rf-rin-selection-flowchart',
    'flowchart to choose Rf and Rin for the right inverting amplifier gain',
    'Diagram by Instrumentation Blog showing the six steps to choose Rf and Rin, with the output swing check from Solved Example 2 that lowers the gain to minus 4.68.',
    'How to Choose Rf and Rin for the Right Inverting Amplifier Gain', s.svg())

s = S(500, 'Bandwidth of an inverting amplifier for different gains with a 1 MHz GBW op amp')
s.head('Inverting Gain vs Bandwidth (GBW = 1 MHz)', A2)
data = [('Minus 1', 2, 500), ('Minus 2', 3, 333), ('Minus 5', 6, 167), ('Minus 10', 11, 90.9), ('Minus 100', 101, 9.9)]
s.t(40, 80, 'Gain', 18, '#4b5563', 'bold', 'start'); s.t(160, 80, 'Noise gain', 18, '#4b5563', 'bold', 'start'); s.t(300, 80, 'Bandwidth', 18, '#4b5563', 'bold', 'start')
for i, (g, ng, bw) in enumerate(data):
    y = 100 + i * 56
    s.t(40, y + 28, g, 19, '#1a2b4a', 'bold', 'start'); s.t(200, y + 28, str(ng), 19, '#1a2b4a', 'normal', 'middle')
    wpx = max(6, bw / 500 * 330)
    s.raw(f'<rect x="300" y="{y + 8}" width="{wpx:.1f}" height="30" rx="6" fill="{A if i % 2 == 0 else A2}"/>')
    lab = (f'{bw:g} kHz')
    s.t(300 + wpx + 10, y + 30, lab, 19, '#1a2b4a', 'bold', 'start')
s.raw(f'<rect x="40" y="390" width="720" height="90" rx="12" fill="{L}" stroke="{A}" stroke-width="2"/>')
s.t(400, 425, 'Bandwidth = GBW ÷ noise gain = GBW ÷ (1 + Rf/Rin)', 20, A2, 'bold')
s.t(400, 457, 'A unity gain inverter has half the bandwidth of a follower', 18, '#1a2b4a')
fig(slug, 'inverting-amplifier-gain-bandwidth-chart',
    'inverting amplifier gain vs bandwidth chart with noise gain for a 1 MHz op amp',
    'Diagram by Instrumentation Blog charting closed loop bandwidth for gains of minus 1 to minus 100 using a 1 MHz GBW op amp, divided by noise gain 1 + Rf/Rin.',
    'Inverting Amplifier Gain and Bandwidth', s.svg())

# ================= 3. LM35 temperature sensor =================
slug = 'lm35-temperature-sensor'
A, A2, L = '#dc2626', '#7f1d1d', '#fef2f2'
s = S(520, 'LM35 temperature sensor pinout and wiring to Arduino Uno')
s.head('LM35 Pinout and Arduino Wiring', A2)
s.raw(f'<path d="M110 230 L110 140 Q110 90 170 90 Q230 90 230 140 L230 230 Z" fill="#374151" stroke="#111827" stroke-width="2.5"/>')
s.t(170, 170, 'LM35', 22, '#ffffff', 'bold'); s.t(170, 196, 'flat face', 17, '#e5e7eb')
cols3 = [('#dc2626', '1  +Vs'), ('#16a34a', '2  Vout'), ('#111827', '3  GND')]
for i, (c, lab) in enumerate(cols3):
    x = 140 + i * 30
    s.ln(x, 230, x, 300, '#9ca3af', 5)
s.t(225, 280, 'Flat face forward: 1 +Vs, 2 Vout, 3 GND', 17, '#1a2b4a', 'bold', 'start')
for i in range(3): s.t(140 + i * 30, 224, str(i + 1), 17, '#fde68a', 'bold')
ys = [420, 380, 300]
for i, (c, lab) in enumerate(cols3):
    x = 140 + i * 30; y = [450, 400, 360][i]
    s.pl([(x, 300), (x, y), (560, y)], c, 3.5, False)
s.raw(f'<rect x="560" y="300" width="200" height="190" rx="12" fill="#0f766e" stroke="#134e4a" stroke-width="2.5"/>')
s.t(660, 330, 'Arduino Uno', 20, '#ffffff', 'bold')
for y, lab in [(360, 'GND'), (400, 'A0'), (450, '5V')]:
    s.raw(f'<rect x="560" y="{y-10}" width="24" height="20" fill="#f3f4f6" stroke="#111827"/>')
    s.t(600, y + 6, lab, 18, '#ffffff', 'bold', 'start')
s.t(400, 392, 'Vout: 10 mV per °C', 17, '#16a34a', 'bold', 'middle')
s.t(400, 442, '+Vs: 4 V to 30 V', 17, '#dc2626', 'bold', 'middle')
s.box(300, 80, 460, 150, ['Wiring notes', 'Fit 0.1 µF from +Vs to GND at the sensor', 'Keep one common ground with the ADC', 'Reversed supply makes it hot in seconds'],
      L, A, size=17)
fig(slug, 'lm35-temperature-sensor-pinout-arduino-wiring-diagram',
    'LM35 temperature sensor pinout and wiring diagram to Arduino 5V, A0 and GND',
    'Diagram by Instrumentation Blog showing the LM35 TO 92 pinout with the flat face forward and its three wires to the Arduino Uno 5V, A0 and GND pins.',
    'LM35 Temperature Sensor Pinout and Connection', s.svg())

s = S(580, 'LM35 troubleshooting flowchart for wrong temperature readings')
s.head('LM35 Wrong Reading? Troubleshooting Flow', A2)
s.box(260, 50, 280, 42, ['Reading looks wrong'], A, A2, '#ffffff', size=18)
qs = [('Reads about 500 °C?', ['Vout shorted to 5 V or open', 'ground: check pin order, GND']),
      ('Reads 0 °C always?', ['Output open or wrong pin:', 'confirm A0 in code and wiring']),
      ('Jumps several degrees?', ['Noise or cable oscillation: add', '0.1 µF bypass and RC damper']),
      ('Reads 2 to 5 °C high?', ['Self heating: move away from', 'the regulator, reduce load']),
      ('Body very hot?', ['Supply reversed:', 'power off and rewire'])]
s.ar(400, 92, 400, 104)
for i, (q, fx) in enumerate(qs):
    y = 104 + i * 92
    s.box(40, y + 6, 290, 52, [q], '#ffffff', A, size=18)
    s.ar(332, y + 32, 396, y + 32, A, 2.5); s.t(364, y + 24, 'Yes', 17, A, 'bold')
    s.box(398, y, 370, 64, fx, L, A2, size=17, bold_first=False)
    if i < 4:
        s.ar(185, y + 58, 185, y + 96); s.t(195, y + 84, 'No', 17, '#4b5563', 'normal', 'start')
s.t(400, 562, 'Still wrong: compare with a reference thermometer at two points', 17, '#4b5563', 'bold')
fig(slug, 'lm35-temperature-sensor-troubleshooting-flowchart',
    'LM35 troubleshooting flowchart for 500 degree, zero, jumping or high readings',
    'Diagram by Instrumentation Blog showing a step by step check of LM35 faults, from a shorted output reading 500 degrees to a reversed supply making the sensor hot.',
    'LM35 Troubleshooting Table', s.svg())

s = S(520, 'LM35 Arduino ADC formula with two solved examples')
s.head('LM35 Arduino Formula: Two Solved Examples', A2)
s.raw(f'<rect x="40" y="60" width="720" height="96" rx="12" fill="{A2}"/>')
s.t(400, 98, 'Vout (mV) = reading × Vref × 1000 ÷ 1024', 22, '#ffffff', 'bold')
s.t(400, 134, 'T (°C) = Vout (mV) ÷ 10', 22, '#ffffff', 'bold')
cards = [('Default 5 V reference', [('Reading', '62'), ('Vout', '302.7 mV'), ('Temperature', '30.27 °C'), ('Fahrenheit', '86.49 °F'), ('Step', '4.88 mV, 0.49 °C')]),
         ('Internal 1.1 V reference', [('Reading', '233'), ('Vout', '250.3 mV'), ('Temperature', '25.03 °C'), ('Range ends', 'near 110 °C'), ('Step', '1.07 mV, 0.11 °C')])]
for i, (h, kv) in enumerate(cards):
    x = 40 + i * 370
    s.raw(f'<rect x="{x}" y="176" width="350" height="290" rx="14" fill="{L if i == 0 else "#ffffff"}" stroke="{A}" stroke-width="2.5"/>')
    s.t(x + 175, 212, h, 20, A2, 'bold')
    for j, (k, v) in enumerate(kv):
        yy = 254 + j * 44
        s.t(x + 24, yy, k, 18, '#4b5563', 'normal', 'start'); s.t(x + 326, yy, v, 19, A if j == 2 else '#1a2b4a', 'bold', 'end')
        if j < 4: s.ln(x + 20, yy + 16, x + 330, yy + 16, '#fecaca', 1.5)
s.t(400, 500, 'Short form for 5 V: T = reading × 500 ÷ 1024', 18, '#1a2b4a', 'bold')
fig(slug, 'lm35-temperature-sensor-arduino-formula-infographic',
    'LM35 Arduino ADC formula solved examples with 5 V and 1.1 V reference',
    'Diagram by Instrumentation Blog showing the LM35 ADC formula with two solved examples: reading 62 gives 30.27 degrees C at 5 V, and 233 gives 25.03 degrees C at 1.1 V.',
    'LM35 Temperature Sensor Arduino Formula', s.svg())

# ================= 4. IDMT relay =================
slug = 'idmt-relay-characteristics-tms-psm'
A, A2, L = '#b45309', '#78350f', '#fffbeb'
s = S(520, 'IDMT relay grading of two relays in series on a radial feeder')
s.head('Grading Two IDMT Relays in Series', A2)
Y = 150
s.ln(70, Y, 700, Y, '#1a2b4a', 4)
s.raw(f'<circle cx="60" cy="{Y}" r="26" fill="#ffffff" stroke="#1a2b4a" stroke-width="2.5"/>')
s.raw(f'<path d="M44 {Y} Q52 {Y-14} 60 {Y} T76 {Y}" fill="none" stroke="#1a2b4a" stroke-width="2.5"/>')
s.t(60, 205, 'Source', 17, '#1a2b4a', 'bold')
s.ln(400, Y - 50, 400, Y + 50, '#1a2b4a', 6); s.t(400, 88, 'Bus B', 17, '#1a2b4a', 'bold')
for cbx, ctx, rx, nm, sett in [(160, 220, 150, 'R2 upstream', 'TMS 0.22'), (460, 520, 450, 'R1 downstream', 'TMS 0.1')]:
    s.raw(f'<rect x="{cbx-16}" y="{Y-16}" width="32" height="32" fill="#ffffff" stroke="#1a2b4a" stroke-width="2.5"/>')
    s.t(cbx, Y - 26, 'CB', 17, '#1a2b4a', 'bold')
    s.raw(f'<circle cx="{ctx}" cy="{Y}" r="13" fill="none" stroke="{A}" stroke-width="3"/>'); s.t(ctx, Y - 26, 'CT', 17, A, 'bold')
    s.box(rx, 230, 170, 70, [nm, sett], L, A, size=17)
    s.ln(ctx, Y + 13, ctx, 230, A, 2, '5 4')
    s.ar(cbx + 6, 230, cbx, Y + 18, '#4b5563', 2, '5 4')
s.t(250, 325, 'trip', 17, '#4b5563', 'normal', 'middle')
s.pl([(690, 110), (672, 140), (700, 145), (680, 182)], '#dc2626', 4, True)
s.t(712, 205, 'Fault', 18, '#dc2626', 'bold')
s.t(560, 325, 'same fault seen by both', 17, '#4b5563')
ax0, ax1, yA = 150, 710, 470
s.ln(ax0, yA, ax1, yA, '#1a2b4a', 2)
for v in [0, 0.2, 0.4, 0.6, 0.8]:
    x = ax0 + v / 0.8 * (ax1 - ax0); s.ln(x, yA, x, yA + 8, '#1a2b4a', 2); s.t(x, yA + 30, f'{v:g} s', 17, '#4b5563')
for i, (nm, tv, c) in enumerate([('R1', 0.30, A), ('R2', 0.65, A2)]):
    y = 370 + i * 44; w = tv / 0.8 * (ax1 - ax0)
    s.t(140, y + 24, nm, 18, '#1a2b4a', 'bold', 'end')
    s.raw(f'<rect x="{ax0}" y="{y+4}" width="{w:.1f}" height="28" rx="5" fill="{c}"/>')
    s.t(ax0 + w + 10, y + 25, f'{tv:.2f} s', 18, c, 'bold', 'start')
x30, x65 = ax0 + 0.30 / 0.8 * 560, ax0 + 0.65 / 0.8 * 560
s.ln(x30, 360, x30, 452, '#9ca3af', 1.5, '4 4')
s.t((x30 + x65) / 2 + 30, 362, 'grading margin 0.35 s', 17, A2, 'bold', 'start')
fig(slug, 'idmt-relay-grading-relays-in-series-diagram',
    'IDMT relay grading diagram with upstream and downstream relays and 0.35 s margin',
    'Diagram by Instrumentation Blog showing two IDMT relays in series: the downstream relay trips at 0.30 s and the upstream relay at 0.65 s, a 0.35 s grading margin.',
    'Grading Relays in Series', s.svg())

s = S(500, 'IDMT relay trip time calculation steps with PSM and TMS')
s.head('IDMT Trip Time: Step by Step Calculation', A2)
st6 = [(['1. Pickup current', 'CT 400/1, plug 100 %', '= 400 A']), (['2. PSM', '4000 A ÷ 400 A', '= 10']),
       (['3. Curve constants', 'standard inverse', 'k 0.14, α 0.02']), (['4. PSM to the α', '10 to the power 0.02', '= 1.0471']),
       (['5. Base time', '0.14 ÷ 0.0471', '= 2.97 s']), (['6. Trip time', 'TMS × base time', '0.1 × 2.97 = 0.30 s'])]
for i, ls in enumerate(st6):
    r, c = divmod(i, 3)
    if r == 1: c = 2 - c
    x = 40 + c * 250; y = 70 + r * 190
    s.box(x, y, 220, 120, ls, L if i != 5 else A, A, '#1a2b4a' if i != 5 else '#ffffff', size=18)
    if i in (0, 1): s.ar(x + 222, y + 60, x + 248, y + 60, A2, 3)
    if i == 2: s.ar(x + 110, y + 122, x + 110, y + 188, A2, 3)
    if i in (3, 4): s.ar(x - 2, y + 60, x - 28, y + 60, A2, 3)
s.raw(f'<rect x="40" y="405" width="720" height="76" rx="12" fill="#ffffff" stroke="{A}" stroke-width="2"/>')
s.t(400, 436, 't = TMS × k ÷ (PSM to the α minus 1)', 20, A2, 'bold')
s.t(400, 466, 'Same fault: very inverse 0.15 s, extremely inverse 0.081 s', 18, '#1a2b4a')
fig(slug, 'idmt-relay-trip-time-calculation-flowchart',
    'IDMT relay trip time calculation flowchart from CT ratio and PSM to TMS',
    'Diagram by Instrumentation Blog showing the six steps of the worked example: 400 A pickup, PSM 10, standard inverse constants and a 0.30 s trip at TMS 0.1.',
    'IDMT Relay Trip Time Formula', s.svg())

s = S(560, 'IEC IDMT relay curves on a log log graph at TMS 0.1')
s.head('4 IEC Curves at TMS 0.1 (log scales)', A2)
gx0, gx1, gy0, gy1 = 110, 560, 70, 470
def X(p): return gx0 + (math.log10(p) - math.log10(2)) / (math.log10(20) - math.log10(2)) * (gx1 - gx0)
def Yt(t): return gy1 - (math.log10(t) - (-2)) / (math.log10(20) + 2) * (gy1 - gy0)
s.raw(f'<rect x="{gx0}" y="{gy0}" width="{gx1-gx0}" height="{gy1-gy0}" fill="#ffffff" stroke="#1a2b4a" stroke-width="2"/>')
for p in [2, 5, 10, 20]:
    s.ln(X(p), gy0, X(p), gy1, '#e5e7eb', 1.5); s.t(X(p), gy1 + 26, str(p), 17, '#4b5563')
for t in [0.01, 0.1, 1, 10]:
    s.ln(gx0, Yt(t), gx1, Yt(t), '#e5e7eb', 1.5); s.t(gx0 - 8, Yt(t) + 6, f'{t:g}', 17, '#4b5563', 'normal', 'end')
s.t((gx0 + gx1) / 2, gy1 + 54, 'PSM (fault current ÷ pickup)', 18, '#1a2b4a', 'bold')
s.raw(f'<text x="34" y="{(gy0+gy1)/2}" font-size="18" fill="#1a2b4a" font-weight="bold" text-anchor="middle" transform="rotate(270 34 {(gy0+gy1)/2})">Trip time, s</text>')
curves = [('Standard inverse', 0.14, 0.02, '#b45309', '0.30 s'), ('Very inverse', 13.5, 1, '#2563eb', '0.15 s'),
          ('Extremely inverse', 80, 2, '#dc2626', '0.081 s'), ('Long time inverse', 120, 1, '#16a34a', '1.33 s')]
for nm, k, a, c, lab in curves:
    pts = [(X(p), Yt(0.1 * k / (p ** a - 1))) for p in [2 + i * 0.25 for i in range(73)]]
    s.pl([(round(x, 1), round(y, 1)) for x, y in pts], c, 3, False)
    t10 = 0.1 * k / (10 ** a - 1)
    s.raw(f'<circle cx="{X(10):.1f}" cy="{Yt(t10):.1f}" r="6" fill="{c}" stroke="#ffffff" stroke-width="2"/>')
for i, (nm, k, a, c, lab) in enumerate(curves):
    y = 95 + i * 78
    s.raw(f'<rect x="585" y="{y}" width="195" height="64" rx="10" fill="#ffffff" stroke="{c}" stroke-width="2.5"/>')
    s.t(682, y + 26, nm, 17, c, 'bold'); s.t(682, y + 52, f'PSM 10: {lab}', 17, '#1a2b4a')
s.t(682, 430, 'Dots mark PSM 10', 17, '#4b5563', 'bold')
fig(slug, 'idmt-relay-iec-curves-comparison-chart',
    'IDMT relay IEC curves chart of trip time vs PSM for four inverse curves',
    'Diagram by Instrumentation Blog plotting the four IEC IDMT curves at TMS 0.1 on log scales, with the PSM 10 trip times of 0.30, 0.15, 0.081 and 1.33 s.',
    '4 Standard IEC Curves', s.svg())

# ================= 5. Lighting design calculation =================
slug = 'lighting-design-calculation'
A, A2, L = '#7c3aed', '#4c1d95', '#f5f3ff'
s = S(520, 'Room cross section for lighting design calculation with mounting height and working plane')
s.head('Room Section: Mounting Height and Working Plane', A2)
fl, ce = 450, 120; ppm = (fl - ce) / 3.0; wp = fl - 0.8 * ppm
s.raw(f'<rect x="90" y="{ce}" width="420" height="{fl-ce}" fill="#fafafa" stroke="#1a2b4a" stroke-width="3"/>')
s.raw(f'<clipPath id="rm"><rect x="90" y="{ce}" width="420" height="{wp-ce}"/></clipPath>')
for i in range(4):
    x = 135 + i * 95
    s.raw(f'<polygon points="{x+6},{ce+6} {x+54},{ce+6} {x+110},{wp} {x-50},{wp}" fill="#fde68a" opacity="0.45" clip-path="url(#rm)"/>')
    s.raw(f'<rect x="{x}" y="{ce}" width="60" height="10" fill="{A}"/>')
s.ln(90, wp, 510, wp, A2, 2.5, '9 6'); s.t(330, wp + 30, 'Working plane (desk height)', 18, A2, 'bold')
s.raw(f'<rect x="110" y="{wp}" width="60" height="{fl-wp}" fill="none" stroke="#9ca3af" stroke-width="2"/>')
dim(s, 60, ce, fl); s.t(48, (ce + fl) / 2 + 6, '3 m', 18, '#1a2b4a', 'bold', 'end')
dim(s, 490, ce + 10, wp); s.t(482, (ce + wp) / 2 + 6, 'Hm = 2.2 m', 18, A2, 'bold', 'end')
dim(s, 490, wp, fl); s.t(482, (wp + fl) / 2 + 6, '0.8 m', 18, '#1a2b4a', 'bold', 'end')
s.t(300, 485, 'Room 20 m long × 10 m wide', 18, '#1a2b4a', 'bold')
s.box(545, 110, 230, 110, ['Room Index', 'RI = (L × W) ÷', '(Hm × (L + W))'], L, A, size=18)
s.box(545, 240, 230, 90, ['200 ÷ (2.2 × 30)', '= 200 ÷ 66 = 3.03'], '#ffffff', A, size=18, bold_first=False)
s.box(545, 350, 230, 90, ['UF from table', 'RI 3.0 gives 0.65'], L, A, size=18)
s.ar(660, 220, 660, 238, A2); s.ar(660, 330, 660, 348, A2)
fig(slug, 'lighting-design-calculation-room-index-section-diagram',
    'lighting design calculation room section with 2.2 m mounting height and working plane',
    'Diagram by Instrumentation Blog showing the 3 m office section from the worked example, with a 0.8 m working plane, 2.2 m mounting height and room index of 3.03.',
    'Lighting Design Calculation: The Lumen Method Explained', s.svg())

s = S(600, 'Lumen method lighting design calculation step by step flowchart')
s.head('Lumen Method in 7 Steps', A2)
st7 = [('Required lux level E', 'open plan office', 'E = 500 lux'), ('Room area A', 'length × width', 'A = 20 × 10 = 200 m²'),
       ('Flux per fixture F', 'fixture data sheet', 'F = 3600 lm (40 W LED)'), ('Room index RI', 'from L, W and Hm', 'RI = 200 ÷ 66 = 3.03'),
       ('Utilisation factor UF', 'photometric table', 'UF = 0.65'), ('Maintenance factor MF', 'clean office', 'MF = 0.8'),
       ('N = (E × A) ÷ (F × UF × MF)', 'round up', 'N = 53.4, so 54')]
for i, (h, sub, v) in enumerate(st7):
    y = 60 + i * 70
    s.raw(f'<circle cx="62" cy="{y+27}" r="20" fill="{A}"/>'); s.t(62, y + 34, str(i + 1), 19, '#ffffff', 'bold')
    s.raw(f'<rect x="96" y="{y}" width="330" height="54" rx="10" fill="{L}" stroke="{A}" stroke-width="2"/>')
    s.t(112, y + 23, h, 18, A2, 'bold', 'start'); s.t(112, y + 45, sub, 17, '#4b5563', 'normal', 'start')
    s.ar(428, y + 27, 470, y + 27, A2, 2.5)
    s.raw(f'<rect x="472" y="{y+4}" width="300" height="46" rx="23" fill="{"#ffffff" if i < 6 else A}" stroke="{A}" stroke-width="2"/>')
    s.t(622, y + 34, v, 18, A2 if i < 6 else '#ffffff', 'bold')
    if i < 6: s.ar(62, y + 48, 62, y + 68, A2, 2)
s.t(400, 575, 'Arrange 54 fixtures as 6 rows × 9 columns for a symmetric layout', 18, '#1a2b4a', 'bold')
fig(slug, 'lighting-design-calculation-lumen-method-steps-flowchart',
    'lighting design calculation flowchart of the lumen method steps with worked values',
    'Diagram by Instrumentation Blog showing the seven lumen method steps, from 500 lux and 200 square metres to room index 3.03 and 54 fixtures.',
    'The Lighting Design Calculation Formula', s.svg())

s = S(540, 'Worked lighting design calculation example with fixture layout')
s.head('Worked Example: 54 Fixtures for a 500 Lux Office', A2)
s.raw(f'<rect x="30" y="64" width="300" height="440" rx="14" fill="{A2}"/>')
s.t(180, 102, 'N = (E × A) ÷', 21, '#ffffff', 'bold'); s.t(180, 130, '(F × UF × MF)', 21, '#ffffff', 'bold')
for j, ln_ in enumerate(['E = 500 lux', 'A = 200 m²', 'F = 3600 lm', 'UF = 0.65, MF = 0.8', '100000 ÷ 1872', 'N = 53.4']):
    s.t(180, 180 + j * 38, ln_, 19, '#ede9fe')
s.raw(f'<rect x="60" y="420" width="240" height="56" rx="10" fill="#ffffff"/>'); s.t(180, 456, 'Round up: 54', 22, A2, 'bold')
rx0, ry0, rw, rh_ = 380, 110, 380, 190
s.raw(f'<rect x="{rx0}" y="{ry0}" width="{rw}" height="{rh_}" fill="{L}" stroke="{A}" stroke-width="2.5"/>')
for i in range(9):
    for j in range(6):
        cx = rx0 + (i + 0.5) * rw / 9; cy = ry0 + (j + 0.5) * rh_ / 6
        s.raw(f'<rect x="{cx-12:.1f}" y="{cy-7:.1f}" width="24" height="14" rx="3" fill="{A}"/>')
s.t(rx0 + rw / 2, ry0 - 14, '20 m, 9 columns', 18, '#1a2b4a', 'bold')
s.raw(f'<text x="{rx0+rw+20}" y="{ry0+rh_/2}" font-size="18" fill="#1a2b4a" font-weight="bold" text-anchor="middle" transform="rotate(90 {rx0+rw+20} {ry0+rh_/2})">10 m, 6 rows</text>')
s.box(380, 330, 380, 80, ['Always round up', 'rounding down misses 500 lux'], '#ffffff', A, size=18)
s.box(380, 424, 380, 80, ['Uniformity check', 'minimum at least 60 % of average'], '#ffffff', A, size=18)
fig(slug, 'lighting-design-calculation-worked-example-infographic',
    'worked example of 54 LED panels in a 20 by 10 m office',
    'Diagram by Instrumentation Blog showing the worked lumen method example: 500 lux over 200 square metres with 3600 lumen panels needs 53.4, rounded up to 54 in a 6 by 9 grid.',
    'Worked Lighting Design Calculation Example', s.svg())

if __name__ == '__main__': main()
