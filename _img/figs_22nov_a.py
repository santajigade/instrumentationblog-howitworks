import json, sys, os
sys.path.insert(0, '/home/claude/instrumentationblog-howitworks/_img')
from svglib import S
OUT = '/home/claude/instrumentationblog-howitworks/_img/changes'
CH = {}
def fig(slug, name, alt, caption, after, svg):
    CH.setdefault(slug, []).append(dict(name=name, alt=alt, caption=caption, after_h2=after, svg=svg))
G = '#4b5563'

# ============ 1. 100 essential engineering formulas ============
A, A2, L = '#b45309', '#92400e', '#fff7ed'
slug = '100-essential-engineering-formulas'
s = S(550, 'Hydrostatic pressure and DP level measurement on an open water tank')
s.head('Hydrostatic Pressure and DP Level', A2)
# tank
s.raw(f'<rect x="70" y="80" width="230" height="330" fill="#ffffff" stroke="#1a2b4a" stroke-width="3"/>')
s.raw(f'<rect x="72" y="160" width="226" height="248" fill="#dbeafe"/>')
s.ln(72, 160, 298, 160, '#1d4ed8', 2.5)
s.t(185, 140, 'Open top tank', 18, G)
# height arrow
s.ar(330, 285, 330, 163, A2, 2.5); s.ar(330, 285, 330, 405, A2, 2.5)
s.t(352, 292, 'h', 22, A2, 'bold', 'start')
# HP tapping
s.ln(300, 395, 400, 395, '#1a2b4a', 4)
s.box(400, 360, 150, 70, ['DP transmitter', 'HP side'], L, A, size=17)
s.t(475, 455, 'LP side open', 17, G); s.t(475, 478, 'to atmosphere', 17, G)
s.t(185, 300, 'Water', 20, '#1d4ed8', 'bold'); s.t(185, 325, 'ρ = 1000 kg/m³', 18, '#1d4ed8')
# formula card
s.raw(f'<rect x="575" y="80" width="200" height="350" rx="12" fill="{L}" stroke="{A}" stroke-width="2.5"/>')
s.t(675, 115, 'P = ρ × g × h', 20, A2, 'bold')
s.t(675, 150, 'h = P / (ρ × g)', 18, '#1a2b4a')
s.t(675, 195, 'Example', 18, A2, 'bold')
s.t(675, 222, 'h = 5 m water', 17, '#1a2b4a')
s.t(675, 249, '1000 × 9.81 × 5', 17, '#1a2b4a')
s.t(675, 276, '= 49 kPa gauge', 17, '#1a2b4a')
s.t(675, 303, '+ 101.3 kPa atm', 17, '#1a2b4a')
s.t(675, 330, '≈ 150 kPa abs', 17, A2, 'bold')
s.t(675, 375, 'Rule of thumb', 18, A2, 'bold')
s.t(675, 402, '10 m water ≈ 1 bar', 17, '#1a2b4a')
s.t(400, 530, 'Absolute pressure = gauge pressure + atmospheric pressure', 18, G)
fig(slug, 'engineering-formulas-hydrostatic-pressure-level-diagram',
    'engineering formulas for hydrostatic pressure and DP transmitter tank level measurement',
    'Diagram by Instrumentation Blog showing P = ρgh on an open water tank with a DP transmitter, worked for a 5 m water column of about 150 kPa absolute.',
    'Pressure & Level : Engineering Formulas', s.svg())

s = S(560, 'Reynolds number flowchart to classify laminar, transitional and turbulent pipe flow')
s.head('Reynolds Number: Which Flow Regime?', A2)
s.box(250, 60, 300, 70, ['Collect data', 'ρ, velocity v, pipe D, viscosity μ'], L, A, size=17)
s.ar(400, 130, 400, 160)
s.box(250, 162, 300, 62, ['Calculate', 'Re = ρ × v × D / μ'], L, A, size=18)
s.ar(400, 224, 400, 250)
s.dia(400, 300, 230, 100, ['Re < 2000?'], '#fffbeb', size=18)
s.ar(515, 300, 575, 300); s.t(545, 290, 'Yes', 17, A2, 'bold')
s.box(578, 260, 195, 80, ['Laminar', 'Hagen Poiseuille', 'law is valid'], '#ecfdf5', '#047857', size=17)
s.ar(400, 350, 400, 380); s.t(420, 372, 'No', 17, A2, 'bold', 'start')
s.dia(400, 430, 230, 100, ['Re > 4000?'], '#fffbeb', size=18)
s.ar(515, 430, 575, 430); s.t(545, 420, 'Yes', 17, A2, 'bold')
s.box(578, 395, 195, 70, ['Turbulent', 'typical in pipes'], '#fef2f2', '#b91c1c', size=17)
s.ar(285, 430, 225, 430); s.t(255, 420, 'No', 17, A2, 'bold')
s.box(30, 395, 195, 70, ['Transitional', '2000 to 4000'], '#eef6ff', '#1d4ed8', size=17)
s.t(400, 530, 'Then use Darcy Weisbach for friction head loss in the pipe', 18, G)
fig(slug, 'engineering-formulas-reynolds-number-flowchart',
    'Reynolds number flowchart for laminar, transitional and turbulent flow in pipes',
    'Diagram by Instrumentation Blog showing how to calculate the Reynolds number and classify pipe flow as laminar below 2000, transitional, or turbulent above 4000.',
    'Flow: Engineering Formulas', s.svg())

s = S(520, 'Electrical engineering formulas card for instrumentation')
s.head('Electrical Formulas at a Glance', A2)
cards = [('Ohm law', ['V = I × R', '20 mA × 250 Ω = 5 V']),
         ('Power', ['P = V × I = I² × R', 'P = V² / R']),
         ('Energy', ['E = P × t', 'measured in kWh']),
         ('Reactance', ['XL = 2πfL', 'XC = 1 / (2πfC)']),
         ('Frequency', ['f = 1 / T', '50 Hz gives T = 20 ms']),
         ('Three phase', ['P = √3 VL IL cos φ', 'motors and drives'])]
for i, (h, ls) in enumerate(cards):
    x = 30 + (i % 3) * 252; y = 70 + (i // 3) * 200
    s.raw(f'<rect x="{x}" y="{y}" width="236" height="180" rx="14" fill="{L if i % 2 == 0 else "#ffffff"}" stroke="{A}" stroke-width="2.5"/>')
    s.raw(f'<rect x="{x}" y="{y}" width="236" height="46" rx="14" fill="{A}"/><rect x="{x}" y="{y+30}" width="236" height="16" fill="{A}"/>')
    s.t(x + 118, y + 31, h, 20, '#ffffff', 'bold')
    s.t(x + 118, y + 100, ls[0], 20, '#1a2b4a', 'bold')
    s.t(x + 118, y + 140, ls[1], 17, G)
s.t(400, 500, 'Transformer: Vp / Vs = Np / Ns, the basis of CTs and PTs', 18, G)
fig(slug, 'engineering-formulas-electrical-formula-infographic',
    'electrical engineering formulas card with Ohm law, power, reactance and three phase power',
    'Diagram by Instrumentation Blog summarising key electrical formulas for instrumentation: Ohm law, power, energy, reactance, frequency and three phase power.',
    'Electrical: Engineering Formulas', s.svg())

# ============ 2. Astable vs monostable vs bistable ============
A, A2, L = '#7c3aed', '#5b21b6', '#f5f3ff'
slug = 'astable-vs-monostable-vs-bistable-multivibrator'
fs = 'astable-vs-monostable-vs-bistable-multivibrator'
s = S(560, 'Output waveforms of astable, monostable and bistable multivibrators')
s.head('Output Waveforms of the Three Multivibrators', A2)
def axis(y):
    s.ln(200, y, 770, y, '#9ca3af', 1.5)
# astable
s.t(30, 105, 'Astable', 20, A2, 'bold', 'start'); s.t(30, 130, '0 stable states', 17, G, 'normal', 'start')
axis(140)
pts = []; x = 200
for k in range(5):
    pts += [(x, 140), (x, 80), (x + 57, 80), (x + 57, 140), (x + 114, 140)]; x += 114
s.pl(pts, A, 3, arrow=False)
s.t(485, 165, 'free running, no trigger needed', 17, G)
# monostable
s.t(30, 245, 'Monostable', 20, A2, 'bold', 'start'); s.t(30, 270, '1 stable state', 17, G, 'normal', 'start')
for tx in (240, 540):
    s.ln(tx, 200, tx, 228, '#b91c1c', 3); s.raw(f'<polygon points="{tx-6},{222} {tx+6},{222} {tx},{232}" fill="#b91c1c"/>')
s.t(240, 194, 'trigger', 17, '#b91c1c'); s.t(540, 194, 'trigger', 17, '#b91c1c')
axis(300)
s.pl([(200, 300), (240, 300), (240, 245), (380, 245), (380, 300), (540, 300), (540, 245), (680, 245), (680, 300), (770, 300)], A, 3, arrow=False)
s.ar(240, 320, 380, 320, A2, 2); s.ar(380, 320, 240, 320, A2, 2); s.t(310, 342, 'fixed time', 17, A2)
# bistable
s.t(30, 415, 'Bistable', 20, A2, 'bold', 'start'); s.t(30, 440, '2 stable states', 17, G, 'normal', 'start')
for tx, lab in ((280, 'set'), (520, 'reset'), (660, 'set')):
    s.ln(tx, 370, tx, 398, '#b91c1c', 3); s.raw(f'<polygon points="{tx-6},{392} {tx+6},{392} {tx},{402}" fill="#b91c1c"/>')
    s.t(tx, 364, lab, 17, '#b91c1c')
axis(470)
s.pl([(200, 470), (280, 470), (280, 415), (520, 415), (520, 470), (660, 470), (660, 415), (770, 415)], A, 3, arrow=False)
s.t(400, 445, 'holds high', 17, A2); s.t(590, 495, 'holds low', 17, A2)
s.t(400, 540, 'Red arrows are external trigger pulses; purple lines are the output', 18, G)
fig(slug, fs + '-waveform-diagram',
    'astable vs monostable vs bistable multivibrator output waveform comparison with trigger pulses',
    'Diagram by Instrumentation Blog comparing output waveforms: astable square wave, monostable one fixed pulse per trigger, and bistable output held until the next trigger.',
    'Output Waveform Comparison', s.svg())

s = S(560, 'Flowchart to identify an astable, monostable or bistable circuit')
s.head('Which Multivibrator Do You Have?', A2)
s.box(260, 58, 280, 56, ['Look at the output'], L, A, size=19)
s.ar(400, 114, 400, 138)
s.dia(400, 192, 280, 104, ['Toggles with no', 'trigger input?'], '#ffffff', A, 17)
s.ar(540, 192, 590, 192); s.t(565, 182, 'Yes', 17, A2, 'bold')
s.box(592, 152, 180, 80, ['Astable', 'zero stable states'], '#ede9fe', A, size=17)
s.ar(400, 244, 400, 272); s.t(418, 264, 'No', 17, A2, 'bold', 'start')
s.dia(400, 326, 280, 104, ['Returns to rest', 'after fixed time?'], '#ffffff', A, 17)
s.ar(540, 326, 590, 326); s.t(565, 316, 'Yes', 17, A2, 'bold')
s.box(592, 286, 180, 80, ['Monostable', 'one stable state'], '#ede9fe', A, size=17)
s.ar(400, 378, 400, 406); s.t(418, 398, 'No', 17, A2, 'bold', 'start')
s.dia(400, 460, 280, 104, ['Holds state until', 'next trigger?'], '#ffffff', A, 17)
s.ar(540, 460, 590, 460); s.t(565, 450, 'Yes', 17, A2, 'bold')
s.box(592, 420, 180, 80, ['Bistable', 'two stable states'], '#ede9fe', A, size=17)
s.box(30, 170, 190, 300, ['Uses', '', 'Astable:', 'clocks, tones', '', 'Monostable:', 'timing, delays,', 'debounce', '', 'Bistable:', 'latches,', 'flip flops'], '#ffffff', A2, size=17)
s.t(400, 540, 'Count the stable states: 0, 1 or 2', 18, G)
fig(slug, fs + '-identify-flowchart',
    'flowchart to identify astable, monostable and bistable multivibrator circuits by stable states',
    'Diagram by Instrumentation Blog showing a decision flowchart that identifies a multivibrator from its trigger and output behaviour, with typical uses of each type.',
    '4 Steps to Identify Which Circuit You Have', s.svg())

s = S(500, '555 astable frequency formula with worked example')
s.head('555 Astable Frequency Formula', A2)
s.raw(f'<rect x="40" y="65" width="720" height="100" rx="14" fill="{A}"/>')
s.t(400, 112, 'f = 1.44 / ((R1 + 2 × R2) × C)', 28, '#ffffff', 'bold')
s.t(400, 148, 'charge through R1 + R2, discharge through R2', 18, '#ede9fe')
vals = [('R1', '1 kΩ'), ('R2', '10 kΩ'), ('C', '1 µF')]
for i, (k, v) in enumerate(vals):
    x = 40 + i * 245
    s.raw(f'<rect x="{x}" y="190" width="225" height="100" rx="12" fill="{L}" stroke="{A}" stroke-width="2"/>')
    s.t(x + 112, 230, k, 20, A2, 'bold'); s.t(x + 112, 268, v, 24, '#1a2b4a', 'bold')
s.t(60, 335, 'Step 1:  R1 + 2 × R2 = 1 kΩ + 20 kΩ = 21 kΩ', 19, '#1a2b4a', 'normal', 'start')
s.t(60, 370, 'Step 2:  21000 Ω × 0.000001 F = 0.021 s', 19, '#1a2b4a', 'normal', 'start')
s.t(60, 405, 'Step 3:  f = 1.44 / 0.021', 19, '#1a2b4a', 'normal', 'start')
s.raw(f'<rect x="500" y="355" width="260" height="70" rx="12" fill="#ede9fe" stroke="{A}" stroke-width="2.5"/>')
s.t(630, 400, 'f = 68.6 Hz', 26, A2, 'bold')
s.t(400, 470, 'Five or ten percent part tolerance shifts the real frequency', 18, G)
fig(slug, fs + '-frequency-infographic',
    '555 astable frequency formula worked example with R1, R2 and C values',
    'Diagram by Instrumentation Blog working the 555 astable formula f = 1.44 / ((R1 + 2R2) C) with 1 kilohm, 10 kilohm and 1 microfarad to get 68.6 Hz.',
    'Astable Frequency Formula', s.svg())

# ============ 3. Cascode amplifier ============
A, A2, L = '#be123c', '#9f1239', '#fff1f2'
slug = 'cascode-amplifier-working-principle'
s = S(580, 'BJT cascode amplifier circuit with common emitter and common base stages')
s.head('BJT Cascode Amplifier Circuit', A2)
def npn(cx, cy, lab):
    # base line vertical at cx, collector up right, emitter down right
    s.raw(f'<circle cx="{cx+10}" cy="{cy}" r="34" fill="#ffffff" stroke="#1a2b4a" stroke-width="2"/>')
    s.ln(cx, cy - 20, cx, cy + 20, '#1a2b4a', 4)
    s.ln(cx, cy - 8, cx + 30, cy - 30, '#1a2b4a', 2.5)
    s.ar(cx, cy + 8, cx + 28, cy + 30, '#1a2b4a', 2.5)
    s.t(cx + 60, cy + 6, lab, 20, A2, 'bold', 'start')
CX = 300
# Vcc rail
s.ln(240, 70, 420, 70, '#1a2b4a', 3); s.t(330, 62, '+Vcc', 18, '#1a2b4a', 'bold')
# Rc
s.ln(330, 70, 330, 90)
s.raw('<rect x="318" y="90" width="24" height="60" fill="#ffffff" stroke="#1a2b4a" stroke-width="2.5"/>')
s.t(300, 126, 'Rc', 18, '#1a2b4a', 'bold', 'end')
s.ln(330, 150, 330, 214)
# output node
s.raw('<circle cx="330" cy="180" r="5" fill="#1a2b4a"/>'); s.ln(330, 180, 450, 180); s.raw('<circle cx="455" cy="180" r="5" fill="none" stroke="#1a2b4a" stroke-width="2"/>')
s.t(470, 186, 'Vout', 19, A2, 'bold', 'start')
# Q2 at cy=245: collector top at (330,215), emitter bottom (328,275)
npn(CX, 245, 'Q2, CB stage')
s.ln(330, 275, 330, 335)
s.raw('<circle cx="330" cy="305" r="5" fill="#1a2b4a"/>')
# Q2 base bias
s.ln(300, 245, 200, 245); s.t(190, 240, 'Vbias', 18, '#1a2b4a', 'bold', 'end'); s.t(190, 264, 'AC ground', 17, G, 'normal', 'end')
# Q1 at cy=365: collector top (330,335)
npn(CX, 365, 'Q1, CE stage')
s.ln(330, 395, 330, 460); s.ln(300, 460, 360, 460, '#1a2b4a', 3); s.ln(310, 468, 350, 468, '#1a2b4a', 2.5); s.ln(320, 476, 340, 476, '#1a2b4a', 2)
s.ln(300, 365, 200, 365); s.raw('<circle cx="195" cy="365" r="5" fill="none" stroke="#1a2b4a" stroke-width="2"/>')
s.t(180, 371, 'Vin', 19, A2, 'bold', 'end')
# annotation callout for node
s.ln(336, 305, 470, 305, '#9ca3af', 1.5)
s.box(470, 285, 300, 70, ['Q1 collector sees 1/gm2', 'gain of Q1 is about 1'], L, A, size=17)
s.box(470, 395, 300, 70, ['Q1 turns Vin into current', 'Q2 turns it into Vout'], '#ffffff', A, size=17)
s.t(160, 520, 'Av ≈ minus gm × Rc', 19, '#1a2b4a', 'bold'); s.t(410, 520, 'Rout ≈ β × rce2', 19, '#1a2b4a', 'bold'); s.t(640, 520, 'Cin ≈ 2 × Cbc', 19, '#1a2b4a', 'bold')
s.t(400, 555, 'Low swing at Q1 collector removes the Miller multiplication of Cbc', 17, G)
fig(slug, 'cascode-amplifier-bjt-circuit-diagram',
    'cascode amplifier BJT circuit with common emitter Q1 and common base Q2 stages',
    'Diagram by Instrumentation Blog showing a BJT cascode amplifier: common emitter Q1 driving the emitter of common base Q2, with load Rc, bias and output at the Q2 collector.',
    'How the Cascode Amplifier Works', s.svg())

s = S(590, 'Cascode amplifier worked example calculation flowchart')
s.head('Cascode Worked Example, Step by Step', A2)
s.box(150, 56, 500, 56, ['Given: IC = 1 mA, β = 100, Rc = 10 kΩ, Cbc = 2 pF'], '#ffffff', A, size=18)
rows = [('1', 'Transconductance', 'gm = IC / VT = 0.001 / 0.026 = 38.5 mA/V'),
        ('2', 'Voltage gain', 'Av = gm × Rc = 385 V/V  (51.7 dB)'),
        ('3', 'Without cascode', 'Cin = (1 + 385) × 2 pF = 772 pF'),
        ('4', 'With cascode', 'Cin ≈ 2 × 2 pF = 4 pF'),
        ('5', 'Bandwidth gain', '772 pF / 4 pF ≈ 193 times wider')]
y = 135
s.ar(400, 112, 400, y - 2)
for i, (n, h, f) in enumerate(rows):
    s.raw(f'<rect x="60" y="{y}" width="680" height="64" rx="12" fill="{L if i % 2 == 0 else "#ffffff"}" stroke="{A}" stroke-width="2"/>')
    s.raw(f'<circle cx="98" cy="{y+32}" r="20" fill="{A}"/>'); s.t(98, y + 39, n, 19, '#ffffff', 'bold')
    s.t(132, y + 28, h, 18, A2, 'bold', 'start'); s.t(132, y + 52, f, 18, '#1a2b4a', 'normal', 'start')
    if i < 4: s.ar(400, y + 64, 400, y + 86)
    y += 88
s.t(400, 578, 'Gain stays the same as one CE stage; only Cin and bandwidth change', 17, G)
fig(slug, 'cascode-amplifier-worked-example-flowchart',
    'cascode amplifier calculation flowchart for gm, voltage gain, Miller capacitance and bandwidth',
    'Diagram by Instrumentation Blog working the cascode example step by step: gm 38.5 mA/V, gain 385, input capacitance falling from 772 pF to 4 pF.',
    'Cascode Amplifier Key Equations', s.svg())

s = S(560, 'BJT cascode vs MOSFET cascode comparison chart')
s.head('BJT Cascode vs MOSFET Cascode', A2)
s.raw(f'<rect x="30" y="60" width="740" height="50" rx="10" fill="{A}"/>')
s.t(140, 92, 'Parameter', 19, '#ffffff', 'bold'); s.t(395, 92, 'BJT cascode', 19, '#ffffff', 'bold'); s.t(650, 92, 'MOSFET cascode', 19, '#ffffff', 'bold')
rows = [('Input stage', 'Common emitter Q1', 'Common source M1'),
        ('Output stage', 'Common base Q2', 'Common gate M2'),
        ('Output resistance', 'β × rce2', 'gm2 × rds2 × rds1'),
        ('Input capacitance', '≈ 2 × Cbc', '≈ Cgs + 2 × Cgd'),
        ('Headroom', 'two VBE, about 1.4 V', 'two VGS drops'),
        ('Typical use', 'IF and wideband amps', 'RF LNA, CMOS op amps')]
y = 110
for i, (a, b, c) in enumerate(rows):
    s.raw(f'<rect x="30" y="{y}" width="740" height="62" fill="{L if i % 2 == 0 else "#ffffff"}" stroke="#fecdd3" stroke-width="1.5"/>')
    s.t(45, y + 38, a, 18, A2, 'bold', 'start'); s.t(395, y + 38, b, 18, '#1a2b4a'); s.t(650, y + 38, c, 18, '#1a2b4a')
    y += 62
s.ln(260, 110, 260, 482, '#fecdd3', 1.5); s.ln(530, 110, 530, 482, '#fecdd3', 1.5)
s.t(400, 525, 'Both versions remove the Miller effect; MOSFET gives the higher Rout', 18, G)
fig(slug, 'cascode-amplifier-bjt-vs-mosfet-infographic',
    'BJT cascode vs MOSFET cascode comparison of stages, output resistance and input capacitance',
    'Diagram by Instrumentation Blog comparing BJT and MOSFET cascode amplifiers: input and output stages, output resistance, input capacitance, headroom and typical uses.',
    'BJT Cascode vs MOSFET Cascode: Key Differences', s.svg())

# ============ 4. Cold loop and hot loop testing ============
A, A2, L = '#0369a1', '#075985', '#f0f9ff'
slug = 'cold-loop-and-hot-loop-testing'
fs = 'cold-loop-and-hot-loop-testing'
s = S(500, 'Cold loop test setup from field jumper to DCS tag')
s.head('Cold Loop Test Setup: Field to DCS', A2)
blocks = [('Field end', ['Jumper across', 'plus and minus', 'cores']), ('Junction box', ['Field cable', 'terminals']),
          ('Marshalling', ['Multimeter', 'reads near 0 Ω']), ('I/O card', ['Correct channel', 'per I/O list']), ('DCS or PLC', ['Correct tag,', 'range, units'])]
x = 20
for i, (h, ls) in enumerate(blocks):
    s.box(x, 90, 140, 150, [h, ''] + ls, L if i % 2 == 0 else '#ffffff', A, size=17)
    if i < 4: s.ln(x + 140, 150, x + 155, 150, '#1a2b4a', 3); s.ln(x + 140, 180, x + 155, 180, '#1a2b4a', 3)
    x += 155
s.t(400, 290, 'One continuous path: field, JB, marshalling, I/O card, tag', 18, '#1a2b4a', 'bold')
s.raw(f'<rect x="40" y="320" width="340" height="140" rx="12" fill="#ffffff" stroke="{A}" stroke-width="2"/>')
s.t(210, 352, 'Pass looks like', 19, A2, 'bold')
s.t(210, 384, 'Near zero ohms across cores', 17, '#1a2b4a')
s.t(210, 412, 'Shield at panel end only', 17, '#1a2b4a')
s.t(210, 440, '4 mA = 0 %, 20 mA = 100 %', 17, '#1a2b4a')
s.raw(f'<rect x="420" y="320" width="340" height="140" rx="12" fill="#fef2f2" stroke="#b91c1c" stroke-width="2"/>')
s.t(590, 352, 'Fail looks like', 19, '#991b1b', 'bold')
s.t(590, 384, 'Open circuit: broken core', 17, '#1a2b4a')
s.t(590, 412, 'Core to shield short', 17, '#1a2b4a')
s.t(590, 440, 'Wrong terminal or channel', 17, '#1a2b4a')
fig(slug, fs + '-cold-loop-setup-diagram',
    'cold loop testing setup with field jumper, junction box, marshalling, I/O card and DCS tag',
    'Diagram by Instrumentation Blog showing a cold loop test path from a jumper at the field end through the junction box and marshalling panel to the I/O card and DCS tag.',
    'What Is Cold Loop Testing?', s.svg())

s = S(600, 'Cold loop testing procedure flowchart for an analog input loop')
s.head('Cold Loop Procedure: Analog Input Loop', A2)
steps = ['1. Verify tag, location and orientation', '2. Free the cable ends at field or JB', '3. Jumper plus and minus cores at field end',
         '4. Check continuity at marshalling terminal']
y = 56
for i, st in enumerate(steps):
    s.box(40, y, 400, 44, [st], L, A, size=17, bold_first=False)
    s.ar(240, y + 44, 240, y + 58)
    y += 60
s.dia(240, y + 50, 300, 96, ['Near zero ohms?'], '#ffffff', A, 18)
s.ar(390, y + 50, 470, y + 50); s.t(430, y + 40, 'No', 17, '#991b1b', 'bold')
s.box(472, y + 6, 300, 88, ['Find fault', 'open, short or wrong', 'terminal, then repair'], '#fef2f2', '#b91c1c', size=17)
s.pl([(622, y + 6), (622, 198), (442, 198)], '#b91c1c', 2.5, dash='6 5')
s.ar(240, y + 98, 240, y + 118); s.t(256, y + 114, 'Yes', 17, A2, 'bold', 'start')
y2 = y + 120
for st in ['5. Trace to correct I/O card channel', '6. Confirm tag, range and units in DCS', '7. Record PASS, sign off, remove jumper']:
    s.box(40, y2, 400, 44, [st], L, A, size=17, bold_first=False)
    if not st.startswith('7'): s.ar(240, y2 + 44, 240, y2 + 56)
    y2 += 58
fig(slug, fs + '-procedure-flowchart',
    'cold loop testing procedure flowchart for an analog input loop with continuity check',
    'Diagram by Instrumentation Blog showing the seven step cold loop test for an analog input loop, including the continuity check and fault repair path before sign off.',
    'Cold Loop Testing Procedure: Step by Step', s.svg())

s = S(520, 'Commissioning phases with cold loop and hot loop testing')
s.head('Where Cold and Hot Loop Tests Fit', A2)
ph = [('Phase 1', 'Installation', ['No loop testing', 'no field power'], '#f3f4f6', '#4b5563'),
      ('Phase 2', 'Pre commissioning', ['COLD LOOP TEST', 'de energised'], L, A),
      ('Phase 3', 'Commissioning', ['HOT LOOP TEST', 'system powered'], '#fef2f2', '#b91c1c'),
      ('Phase 4', 'Startup', ['All loops signed', 'ready to run'], '#ecfdf5', '#047857')]
x = 20
for i, (p, n, ls, f, c) in enumerate(ph):
    s.raw(f'<rect x="{x}" y="70" width="176" height="180" rx="14" fill="{f}" stroke="{c}" stroke-width="2.5"/>')
    s.t(x + 88, 102, p, 18, c, 'bold'); s.t(x + 88, 134, n, 17, '#1a2b4a', 'bold')
    s.t(x + 88, 186, ls[0], 17, c, 'bold'); s.t(x + 88, 214, ls[1], 17, G)
    if i < 3: s.ar(x + 178, 160, x + 192, 160)
    x += 196
s.raw(f'<rect x="20" y="280" width="760" height="44" rx="8" fill="{A}"/>')
s.t(110, 309, 'Point', 18, '#ffffff', 'bold'); s.t(360, 309, 'Cold loop', 18, '#ffffff', 'bold'); s.t(640, 309, 'Hot loop', 18, '#ffffff', 'bold')
rows = [('Power', 'Off or panel power only', 'Instruments live'), ('Checks', 'Wiring, terminals, tags', 'Full signal and control'),
        ('Signals', 'No live process signal', 'Simulated or real')]
y = 324
for i, (a, b, c) in enumerate(rows):
    s.raw(f'<rect x="20" y="{y}" width="760" height="50" fill="{L if i % 2 == 0 else "#ffffff"}" stroke="#bae6fd" stroke-width="1.5"/>')
    s.t(110, y + 32, a, 18, A2, 'bold'); s.t(360, y + 32, b, 17, '#1a2b4a'); s.t(640, y + 32, c, 17, '#1a2b4a')
    y += 50
s.t(400, 505, 'Rule: cold loop must be signed off before hot loop begins', 18, '#991b1b', 'bold')
fig(slug, fs + '-commissioning-phases-infographic',
    'cold loop and hot loop testing in the commissioning phases with key differences',
    'Diagram by Instrumentation Blog showing the four commissioning phases, with cold loop testing in pre commissioning and hot loop testing in commissioning, plus key differences.',
    'Where Cold and Hot Loop Testing Fit in the Commissioning Sequence', s.svg())

# ============ 5. 3.1 and 3.2 material certificates ============
A, A2, L = '#4d7c0f', '#3f6212', '#f7fee7'
slug = 'difference-between-3-1-and-3-2-material-certificates'
fs = '3-1-and-3-2-material-certificate'
s = S(520, 'Who verifies a 3.1 and a 3.2 material certificate under EN 10204')
s.head('Who Signs a 3.1 and a 3.2 Certificate', A2)
s.box(40, 80, 200, 90, ['Manufacturer', 'production batch'], '#ffffff', A, size=18)
s.ar(240, 125, 290, 125)
s.box(292, 70, 216, 110, ['Tests on batch', 'chemical analysis,', 'mechanical tests'], L, A, size=17)
s.ar(508, 125, 558, 125)
s.box(560, 70, 210, 110, ['Inspection rep', 'independent of', 'production'], '#ffffff', A, size=17)
s.ar(665, 180, 665, 225)
s.box(560, 227, 210, 80, ['3.1 certificate', 'signed'], '#ecfccb', A, size=18)
s.ar(665, 307, 665, 352)
s.box(560, 354, 210, 100, ['3.2 certificate', 'all 3.1 data', 'plus verification'], '#d9f99d', A2, size=17)
s.box(40, 354, 380, 100, ['Independent inspector', 'third party authority or', 'buyer authorised inspector'], '#fefce8', '#a16207', size=17)
s.ar(420, 404, 558, 404, '#a16207', 2.5)
s.t(490, 394, 'verifies', 17, '#a16207', 'bold')
s.box(40, 227, 380, 80, ['Same test data in both:', 'composition, properties, results'], '#ffffff', G, size=17)
s.t(400, 495, '3.2 costs more and cannot be issued after manufacture', 18, G)
fig(slug, fs + '-verification-diagram',
    '3.1 and 3.2 material certificate verification diagram showing manufacturer and independent inspector',
    'Diagram by Instrumentation Blog showing how a 3.1 certificate is signed by the manufacturer inspection representative and a 3.2 adds an independent or buyer inspector.',
    'Difference Between 3.1 and 3.2 Material Certificates', s.svg())

s = S(560, 'Flowchart to choose a 3.1 or 3.2 material certificate')
s.head('3.1 or 3.2: Which to Specify?', A2)
s.box(250, 58, 300, 56, ['New purchase order'], L, A, size=19)
s.ar(400, 114, 400, 136)
s.dia(400, 192, 330, 110, ['Third party or buyer', 'witness required?'], '#ffffff', A, 17)
s.ar(565, 192, 600, 192); s.t(582, 180, 'Yes', 17, A2, 'bold')
s.box(602, 147, 180, 90, ['Specify 3.2', 'critical, high', 'pressure parts'], '#d9f99d', A2, size=17)
s.ar(400, 247, 400, 275); s.t(418, 267, 'No', 17, A2, 'bold', 'start')
s.dia(400, 330, 330, 110, ['Old spec asks', 'for 3.1 B?'], '#ffffff', A, 17)
s.ar(235, 330, 200, 330); s.t(218, 318, 'Yes', 17, A2, 'bold')
s.box(18, 285, 180, 90, ['Accept 3.1', 'current', 'equivalent'], '#ecfccb', A, size=17)
s.ar(400, 385, 400, 413); s.t(418, 405, 'No', 17, A2, 'bold', 'start')
s.box(290, 415, 220, 60, ['Specify 3.1'], '#ecfccb', A, size=19)
s.box(580, 300, 205, 120, ['For a pump with', '3.2, list which', 'parts need it:', 'casing, impeller, shaft'], '#fefce8', '#a16207', size=17, bold_first=False)
s.ar(692, 237, 692, 298, '#a16207', 2)
s.t(400, 530, 'Always check heat number, chemistry and test values match', 18, G)
fig(slug, fs + '-selection-flowchart',
    'flowchart to choose a 3.1 or 3.2 material certificate for a purchase order',
    'Diagram by Instrumentation Blog showing when to specify a 3.1 or 3.2 certificate, how to treat a 3.1 B request, and listing pump parts that need 3.2.',
    'Practical Application of 3.2 Certificates', s.svg())

s = S(540, 'EN 10204 1991 to 2004 certificate type equivalents')
s.head('EN 10204: 1991 Types to 2004 Types', A2)
s.raw(f'<rect x="30" y="60" width="740" height="46" rx="10" fill="{A}"/>')
s.t(110, 90, '1991 type', 18, '#ffffff', 'bold'); s.t(390, 90, 'Validated by', 18, '#ffffff', 'bold'); s.t(675, 90, '2004 type', 18, '#ffffff', 'bold')
rows = [('2.1', 'Manufacturer, no test results', '2.1'), ('2.2', 'Manufacturer, non specific results', '2.2'),
        ('2.3', 'Manufacturer, specific inspection', 'Withdrawn'), ('3.1 A', 'Inspector in official regulations', '3.2'),
        ('3.1 B', 'Independent inspection department', '3.1'), ('3.1 C', 'Inspector appointed by purchaser', '3.2'),
        ('3.2', 'Manufacturer and purchaser jointly', '3.2')]
y = 106
for i, (a, b, c) in enumerate(rows):
    s.raw(f'<rect x="30" y="{y}" width="740" height="52" fill="{L if i % 2 == 0 else "#ffffff"}" stroke="#d9f99d" stroke-width="1.5"/>')
    s.t(110, y + 33, a, 19, A2, 'bold'); s.t(390, y + 33, b, 17, '#1a2b4a')
    col = '#991b1b' if c == 'Withdrawn' else A2
    s.t(675, y + 33, c, 19, col, 'bold')
    y += 52
s.t(400, 500, 'Only 2.1, 2.2, 3.1 and 3.2 remain in EN 10204:2004', 18, G)
fig(slug, fs + '-en-10204-types-infographic',
    'EN 10204 certificate types chart mapping 1991 types to 2004 types',
    'Diagram by Instrumentation Blog mapping EN 10204 1991 certificate types to the 2004 edition, showing 3.1 B became 3.1 and 3.1 A and 3.1 C became 3.2.',
    'What Does 3.1 B Mean on a Material Certificate?', s.svg())

if __name__ == '__main__':
    import cairosvg
    PNG = sys.argv[1] if len(sys.argv) > 1 else None
    for slug, figs in CH.items():
        json.dump({'slug': slug, 'figs': figs}, open(f'{OUT}/{slug}.json', 'w'), indent=1, ensure_ascii=False)
        if PNG:
            for f in figs:
                cairosvg.svg2png(bytestring=f['svg'].encode(), write_to=f'{PNG}/{f["name"]}.png', output_width=800)
    print({k: len(v) for k, v in CH.items()})
