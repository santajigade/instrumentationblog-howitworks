import sys; sys.path.insert(0, '/home/claude/instrumentationblog-howitworks/_img'); from figs_24nov_common import *
GREY = '#4b5563'

# ================= 1. Types of controllers =================
slug = 'types-of-controllers-in-instrumentation'
A, A2, L = '#4f46e5', '#312e81', '#eef2ff'
s = S(520, 'Feedback plus feedforward control block diagram')
s.head('Feedback and Feedforward Working Together', A2)
s.box(30, 230, 120, 64, ['Setpoint', 'SP'], L, A, size=18)
s.raw(f'<circle cx="205" cy="262" r="22" fill="#ffffff" stroke="{A2}" stroke-width="2.5"/>')
s.t(205, 269, 'Σ', 20, A2, 'bold'); s.t(176, 250, '+', 18, A2, 'bold'); s.t(214, 300, '−', 20, A2, 'bold')
s.ar(150, 262, 181, 262)
s.box(255, 222, 170, 80, ['Feedback', 'controller'], A, A2, '#ffffff', size=18)
s.ar(227, 262, 253, 262)
s.raw(f'<circle cx="470" cy="262" r="22" fill="#ffffff" stroke="{A2}" stroke-width="2.5"/>')
s.t(470, 269, 'Σ', 20, A2, 'bold')
s.ar(425, 262, 446, 262)
s.box(520, 222, 150, 80, ['Valve and', 'process'], L, A, size=18)
s.ar(492, 262, 518, 262)
s.ar(670, 262, 760, 262); s.t(722, 250, 'PV', 18, A2, 'bold')
s.pl([(715, 262), (715, 400), (205, 400), (205, 286)], A2, 2.5)
s.box(390, 372, 170, 56, ['Transmitter'], '#ffffff', A2, size=18)
s.t(400, 462, 'Feedback corrects only after the PV has moved', 17, GREY)
s.box(300, 70, 210, 60, ['Disturbance', 'measured'], '#fef3c7', '#b45309', size=18)
s.pl([(510, 100), (595, 100), (595, 220)], '#b45309', 2.5)
s.t(660, 120, 'upsets', 17, '#b45309', 'bold'); s.t(660, 142, 'process', 17, '#b45309', 'bold')
s.ar(470, 130, 470, 150, '#b45309')
s.box(395, 150, 150, 54, ['Feedforward'], '#fef3c7', '#b45309', size=18)
s.ar(470, 204, 470, 238, '#b45309')
s.t(400, 492, 'Feedforward acts on the measured disturbance before it reaches the PV', 17, GREY)
fig(slug, 'types-of-controllers-in-instrumentation-feedforward-feedback-diagram',
    'block diagram of feedback and feedforward controllers acting on one control valve',
    'Diagram by Instrumentation Blog showing a feedback controller correcting the measured PV while a feedforward controller acts early on a measured disturbance.',
    '10. Feedforward Controller', s.svg())

s = S(590, 'Flowchart for choosing a controller type by process need')
s.head('Which Controller Action Fits the Loop?', A2)
s.dia(400, 110, 400, 96, ['Small swings around', 'setpoint acceptable?'], '#ffffff', A, size=18)
s.ar(600, 110, 640, 110); s.t(620, 98, 'Yes', 17, A2, 'bold')
s.box(642, 78, 140, 64, ['On off', 'control'], A2, A2, '#ffffff', size=18)
s.ar(400, 158, 400, 182); s.t(420, 174, 'No', 17, A2, 'bold', 'start')
s.dia(400, 232, 400, 96, ['Small offset OK,', 'fast response needed?'], '#ffffff', A, size=18)
s.ar(600, 232, 640, 232); s.t(620, 220, 'Yes', 17, A2, 'bold')
s.box(642, 200, 140, 64, ['P', 'control'], A, A2, '#ffffff', size=18)
s.ar(400, 280, 400, 304); s.t(420, 296, 'No', 17, A2, 'bold', 'start')
s.dia(400, 354, 400, 96, ['Slow process, overshoot', 'must be reduced?'], '#ffffff', A, size=18)
s.ar(600, 354, 640, 354); s.t(620, 342, 'Yes', 17, A2, 'bold')
s.box(642, 322, 140, 64, ['PID', 'control'], A, A2, '#ffffff', size=18)
s.ar(400, 402, 400, 426); s.t(420, 418, 'No', 17, A2, 'bold', 'start')
s.box(260, 426, 280, 64, ['PI control', 'flow, level, pressure'], L, A, size=18)
s.box(14, 190, 172, 210, ['Remember', 'P: keeps offset', 'I: ends offset', 'D: acts on rate', 'D: noise prone'], '#ffffff', A2, size=17)
s.t(400, 530, 'Motion and position loops that need speed and less overshoot often use PD', 17, GREY)
s.t(400, 560, 'Most PLC and DCS loops are configured as PI by default', 17, GREY)
fig(slug, 'types-of-controllers-in-instrumentation-selection-flowchart',
    'flowchart to choose on off, P, PI, PD or PID controller for a process loop',
    'Diagram by Instrumentation Blog showing how to pick a controller action: on off for tolerant loops, P for small offset, PID for slow loops and PI for most loops.',
    'Types of Controllers in Instrumentation: Introduction', s.svg())

s = S(560, 'Comparison chart of on off P PI PD and PID controller actions')
s.head('Controller Actions Compared', A2)
cols = ['Removes offset', 'Speed', 'Overshoot', 'Typical use']
rows = [('On off', ['No, cycles', 'Full on, off', 'Swings', 'Thermostat, pump']),
        ('P', ['No', 'Fast', 'Some', 'Flow, speed']),
        ('PI', ['Yes', 'Medium', 'Some', 'Flow, level, pressure']),
        ('PD', ['No', 'Fastest', 'Reduced', 'Motion, robots']),
        ('PID', ['Yes', 'Fast', 'Reduced', 'Temperature, furnace'])]
xs = [20, 130, 290, 420, 560]; ws = [110, 160, 130, 140, 220]
for j, c in enumerate(['Type'] + cols):
    s.raw(f'<rect x="{xs[j]}" y="62" width="{ws[j]}" height="52" fill="{A2}"/>')
    s.t(xs[j] + ws[j] / 2, 95, c, 17, '#ffffff', 'bold')
for i, (n, v) in enumerate(rows):
    y = 114 + i * 72
    s.raw(f'<rect x="20" y="{y}" width="760" height="72" fill="{L if i % 2 == 0 else "#ffffff"}" stroke="#c7d2fe"/>')
    s.t(75, y + 44, n, 20, A, 'bold')
    for j, val in enumerate(v):
        col = '#15803d' if val in ('Yes', 'Reduced') else ('#b91c1c' if val.startswith('No') or val == 'Swings' else '#1a2b4a')
        s.t(xs[j + 1] + ws[j + 1] / 2, y + 44, val, 17, col, 'bold' if col != '#1a2b4a' else 'normal')
s.t(400, 500, 'P reacts to present error, I to past error, D to the rate of change', 17, GREY)
s.t(400, 530, 'Derivative action is sensitive to measurement noise', 17, GREY)
fig(slug, 'types-of-controllers-in-instrumentation-comparison-infographic',
    'types of controllers in instrumentation compared: on off, P, PI, PD and PID',
    'Diagram by Instrumentation Blog comparing on off, P, PI, PD and PID controllers by offset removal, speed, overshoot and typical applications from the article.',
    '5. Proportional + Integral + Derivative (PID) Controller', s.svg())


# ================= 2. Maximum power transfer theorem =================
slug = 'maximum-power-transfer-theorem'
A, A2, L = '#0f766e', '#134e4a', '#f0fdfa'
def res_h(s, x, y, w, lab, c):
    s.raw(f'<rect x="{x}" y="{y-12}" width="{w}" height="24" fill="#ffffff" stroke="{c}" stroke-width="2.5"/>'); s.t(x + w/2, y - 20, lab, 18, c, 'bold')
def res_v(s, x, y, h, lab, c):
    s.raw(f'<rect x="{x-12}" y="{y}" width="24" height="{h}" fill="#ffffff" stroke="{c}" stroke-width="2.5"/>'); s.t(x + 20, y + h/2 + 6, lab, 18, c, 'bold', 'start')
def src(s, x, y, lab, c):
    s.raw(f'<circle cx="{x}" cy="{y}" r="26" fill="#ffffff" stroke="{c}" stroke-width="2.5"/>'); s.t(x, y - 4, '+', 18, c, 'bold'); s.t(x, y + 18, '−', 18, c, 'bold'); s.t(x - 36, y + 6, lab, 18, c, 'bold', 'end')
s = S(560, 'Maximum power transfer worked example reduced to a Thevenin equivalent')
s.head('Worked Example: Find RL for Maximum Power', A2)
# original circuit
c = '#1a2b4a'; top, bot = 110, 290
src(s, 90, 200, '24 V', c)
s.ln(90, 174, 90, top, c); s.ln(90, top, 130, top, c); res_h(s, 130, top, 70, '6 Ω', c); s.ln(200, top, 250, top, c)
s.ln(250, top, 250, 160, c); res_v(s, 250, 160, 80, '12 Ω', c); s.ln(250, 240, 250, bot, c)
s.ln(250, top, 290, top, c); res_h(s, 290, top, 60, '2 Ω', c); s.ln(350, top, 370, top, c)
s.ln(90, 226, 90, bot, c); s.ln(90, bot, 370, bot, c)
s.raw(f'<circle cx="370" cy="{top}" r="6" fill="#ffffff" stroke="{c}" stroke-width="2.5"/><circle cx="370" cy="{bot}" r="6" fill="#ffffff" stroke="{c}" stroke-width="2.5"/>')
s.t(230, 330, 'Original network, load removed', 17, GREY)
s.ar(405, 200, 455, 200, A, 3)
# thevenin
src(s, 540, 200, '16 V', A)
s.ln(540, 174, 540, top, A); s.ln(540, top, 570, top, A); res_h(s, 570, top, 70, 'Rth 6 Ω', A); s.ln(640, top, 720, top, A)
s.ln(720, top, 720, 160, A); res_v(s, 720, 160, 80, '', '#b45309'); s.t(700, 205, 'RL', 18, '#b45309', 'bold', 'end'); s.t(700, 227, '6 Ω', 18, '#b45309', 'bold', 'end')
s.ln(720, 240, 720, bot, A); s.ln(540, 226, 540, bot, A); s.ln(540, bot, 720, bot, A)
s.t(610, 330, 'Thevenin form, matched load', 17, GREY)
s.raw(f'<rect x="40" y="360" width="720" height="180" rx="14" fill="{L}" stroke="{A}" stroke-width="2"/>')
for i, ln_ in enumerate(['Vth = 24 × 12 ÷ (6 + 12) = 16 V', 'Rth = (6 × 12 ÷ 18) + 2 = 4 + 2 = 6 Ω',
                         'Pmax = 16² ÷ (4 × 6) = 256 ÷ 24 = 10.67 W', 'Load voltage 8 V, load current 1.33 A']):
    s.t(400, 398 + i * 40, ln_, 19 if i < 3 else 18, A2 if i < 3 else '#1a2b4a', 'bold' if i == 2 else 'normal')
fig(slug, 'maximum-power-transfer-theorem-worked-example-circuit-diagram',
    'maximum power transfer theorem worked example circuit with Thevenin equivalent and 6 ohm load',
    'Diagram by Instrumentation Blog reducing the 24 V, 6, 12 and 2 ohm network to a 16 V, 6 ohm Thevenin source that gives 10.67 W into a 6 ohm load.',
    'Worked Example With a Thevenin Equivalent', s.svg())

s = S(560, 'Flowchart for choosing the load for maximum power in DC and AC circuits')
s.head('Which Load Gives Maximum Power?', A2)
s.box(240, 56, 320, 56, ['Reduce the network to', 'Vth and Rth or Zth'], L, A, size=18)
s.ar(400, 112, 400, 132)
s.dia(400, 180, 300, 92, ['Is the source', 'AC with reactance?'], '#ffffff', A, size=18)
s.ar(250, 180, 190, 180); s.t(220, 168, 'No', 17, A2, 'bold')
s.box(20, 140, 170, 80, ['DC: set', 'RL = Rth'], A, A2, '#ffffff', size=19)
s.ar(400, 226, 400, 254); s.t(420, 246, 'Yes', 17, A2, 'bold', 'start')
s.dia(400, 304, 300, 96, ['Can the load', 'reactance be set?'], '#ffffff', A, size=18)
s.ar(250, 304, 190, 304); s.t(220, 292, 'Yes', 17, A2, 'bold')
s.box(20, 264, 170, 80, ['ZL = Rth − jXth', 'conjugate'], A, A2, '#ffffff', size=18)
s.ar(550, 304, 600, 304); s.t(575, 292, 'No', 17, A2, 'bold')
s.box(600, 264, 180, 80, ['Resistor only', 'RL = |Zth|'], A2, A2, '#ffffff', size=18)
s.box(40, 390, 330, 140, ['Example, Zth = 3 + j4 Ω', 'Vth = 10 V rms', 'ZL = 3 − j4 Ω', 'Pmax = 10² ÷ 12 = 8.33 W'], '#ffffff', A, size=18)
s.box(430, 390, 330, 140, ['Same source, resistor only', 'RL = |Zth| = 5 Ω', 'I = 10 ÷ 8.94 = 1.118 A', 'P = 1.118² × 5 = 6.25 W'], '#ffffff', A2, size=18)
s.ar(105, 344, 160, 388, A, 2); s.ar(690, 344, 620, 388, A2, 2)
fig(slug, 'maximum-power-transfer-theorem-load-matching-flowchart',
    'flowchart for resistive, conjugate and magnitude load matching for maximum power',
    'Diagram by Instrumentation Blog showing when to use RL equal to Rth, the conjugate load or a resistor equal to the source impedance magnitude, with the article example.',
    'AC Version and Conjugate Matching', s.svg())

import math
s = S(600, 'Load power and efficiency versus load to source resistance ratio')
s.head('Power Peaks at RL = Rth, Efficiency Keeps Rising', A2)
X0, X1, Y0, Y1 = 110, 740, 450, 90
def px(k): return X0 + (math.log10(k) + 1) / 3 * (X1 - X0)
def py(v): return Y0 - v * (Y0 - Y1)
for v in [0, 0.25, 0.5, 0.75, 1.0]:
    s.ln(X0, py(v), X1, py(v), '#e5e7eb', 1.5); s.t(X0 - 12, py(v) + 6, f'{int(v*100)} %', 17, GREY, 'normal', 'end')
for k, lab in [(0.1, '0.1'), (0.5, '0.5'), (1, '1'), (2, '2'), (4, '4'), (10, '10'), (100, '100')]:
    s.ln(px(k), Y0, px(k), Y0 + 6, '#1a2b4a', 2); s.t(px(k), Y0 + 28, lab, 17, '#1a2b4a')
s.ln(X0, Y0, X1, Y0, '#1a2b4a', 2); s.ln(X0, Y0, X0, Y1, '#1a2b4a', 2)
s.t((X0 + X1) / 2, Y0 + 58, 'Load ratio k = RL ÷ Rth (log scale)', 18, '#1a2b4a', 'bold')
ks = [10 ** (-1 + 3 * i / 120) for i in range(121)]
s.pl([(px(k), py(4 * k / (1 + k) ** 2)) for k in ks], A, 3.5, False)
s.pl([(px(k), py(k / (1 + k))) for k in ks], '#b45309', 3.5, False, '9 6')
for k, e, p in [(0.5, .333, .889), (1, .5, 1.0), (2, .667, .889), (4, .8, .64), (10, .909, .331), (100, .99, .039)]:
    s.raw(f'<circle cx="{px(k):.1f}" cy="{py(p):.1f}" r="6" fill="{A}"/><circle cx="{px(k):.1f}" cy="{py(e):.1f}" r="6" fill="#b45309"/>')
s.ln(px(1), Y1, px(1), Y0, A2, 2, '4 4')
s.t(px(1) + 12, Y1 - 12, 'Pmax and 50 % efficiency', 17, A2, 'bold', 'start')
s.ln(170, 546, 210, 546, A, 3.5); s.t(220, 552, 'Load power ÷ Pmax', 17, A, 'bold', 'start')
s.ln(470, 546, 510, 546, '#b45309', 3.5, '9 6'); s.t(520, 552, 'Efficiency', 17, '#b45309', 'bold', 'start')
s.t(400, 586, 'Power fraction = 4k ÷ (1 + k)², efficiency = k ÷ (1 + k)', 18, '#1a2b4a', 'bold')
fig(slug, 'maximum-power-transfer-theorem-power-efficiency-chart',
    'maximum power transfer theorem chart of load power and efficiency against RL over Rth',
    'Diagram by Instrumentation Blog plotting load power and efficiency against RL over Rth, using the article table points from 0.5 to 100 with the peak at RL equal to Rth.',
    'Why Efficiency Is Only 50 Percent', s.svg())

# ================= 3. MEMS accelerometer =================
slug = 'mems-accelerometer-working-principle'
A, A2, L = '#7c3aed', '#4c1d95', '#f5f3ff'
s = S(540, 'MEMS accelerometer differential capacitive sensing structure')
s.head('MEMS Accelerometer: Differential Capacitive Cell', A2)
s.raw(f'<rect x="60" y="70" width="680" height="330" rx="10" fill="#f3f4f6" stroke="#374151" stroke-width="3"/>')
s.t(110, 96, 'Frame', 17, '#374151', 'bold')
# anchors and vertical flexure springs
for ya, y0, y1 in ((74, 104, 150), (376, 320, 366)):
    s.raw(f'<rect x="395" y="{ya}" width="50" height="30" fill="#6b7280"/>' if ya == 74 else f'<rect x="395" y="{ya-10}" width="50" height="30" fill="#6b7280"/>')
    pts = []; n = 6
    for i in range(n + 1):
        xx = 420 + (410 - 420) * ((i / n) if ya == 74 else (1 - i / n))
        pts.append((xx + (0 if i in (0, n) else (-12 if i % 2 else 12)), y0 + (y1 - y0) * i / n))
    s.pl(pts, '#374151', 2.5, False)
s.t(470, 128, 'Flexure spring', 17, '#374151', 'bold', 'start')
s.t(470, 98, 'Anchor', 17, '#374151', 'normal', 'start')
# proof mass shifted right by x
mx = 312
s.raw(f'<rect x="{mx}" y="150" width="196" height="170" rx="6" fill="{A}" stroke="{A2}" stroke-width="2.5"/>')
s.t(mx + 98, 230, 'Proof mass', 19, '#ffffff', 'bold'); s.t(mx + 98, 256, 'm', 19, '#ffffff', 'bold')
# fixed electrodes top and bottom acting as plates: left and right inner plates
s.raw(f'<rect x="300" y="150" width="8" height="180" fill="#b45309"/>')
s.raw(f'<rect x="530" y="150" width="8" height="180" fill="#b45309"/>')
s.t(280, 360, 'Fixed', 17, '#b45309', 'bold', 'middle'); s.t(560, 360, 'Fixed', 17, '#b45309', 'bold', 'middle')
s.t(292, 180, 'C1', 18, A2, 'bold', 'end'); s.t(548, 180, 'C2', 18, A2, 'bold', 'start')
s.ar(250, 300, 180, 300, '#dc2626', 3); s.t(215, 330, 'mass lags', 17, '#dc2626', 'bold')
s.ar(690, 440, 760, 440, '#16a34a', 3); s.t(680, 446, 'chip accelerates', 17, '#16a34a', 'bold', 'end')
s.raw(f'<rect x="60" y="460" width="680" height="64" rx="10" fill="{L}" stroke="{A}" stroke-width="2"/>')
s.t(400, 488, 'C1 rises, C2 falls: C1 − C2 is proportional to displacement x', 18, A2, 'bold')
s.t(400, 512, 'x = m × a ÷ k, about 0.98 nm at 1g for a 1 microgram mass', 17, '#1a2b4a')
fig(slug, 'mems-accelerometer-differential-capacitive-sensing-diagram',
    'MEMS accelerometer proof mass on flexure springs between fixed electrodes forming C1 and C2',
    'Diagram by Instrumentation Blog showing the silicon proof mass on flexure springs between fixed electrodes, so acceleration raises C1 and lowers C2 in proportion to displacement.',
    'MEMS Accelerometer Working Principle: Capacitive Sensing', s.svg())

s = S(580, 'Flowchart for selecting a MEMS accelerometer')
s.head('Selecting a MEMS Accelerometer in 6 Steps', A2)
steps = [('1  Range', 'Set 2 to 3 times the expected peak'),
         ('2  Noise floor', 'noise density × √bandwidth below signal'),
         ('3  Bandwidth', 'above the highest frequency needed'),
         ('4  Interface', 'SPI or I2C to avoid external ADC noise'),
         ('5  Power', 'low current and standby for IoT'),
         ('6  Shock survival', 'above worst handling shock')]
for i, (a, b) in enumerate(steps):
    y = 62 + i * 82
    s.raw(f'<rect x="130" y="{y}" width="540" height="64" rx="12" fill="{L if i % 2 == 0 else "#ffffff"}" stroke="{A}" stroke-width="2.5"/>')
    s.raw(f'<rect x="130" y="{y}" width="190" height="64" rx="12" fill="{A if i % 2 == 0 else A2}"/>')
    s.t(225, y + 38, a, 18, '#ffffff', 'bold')
    s.t(495, y + 38, b, 17, '#1a2b4a')
    if i < 5: s.ar(400, y + 64, 400, y + 82, A2, 2.5)
fig(slug, 'mems-accelerometer-selection-flowchart',
    'flowchart for MEMS accelerometer selection by range, noise, bandwidth, interface and shock',
    'Diagram by Instrumentation Blog listing the six selection steps from the article: range, noise floor, bandwidth, interface, power and shock survival.',
    'How to Select a MEMS Accelerometer for Your Application', s.svg())

s = S(560, 'MEMS accelerometer key numbers and formulas from the worked example')
s.head('MEMS Accelerometer Numbers That Matter', A2)
cards = [('0.981 nm', 'Displacement at 1g', ['x = m × a ÷ k', 'm = 1 microgram, k = 10 N/m']),
         ('15,900 Hz', 'Resonant frequency', ['f = (1 ÷ 2π) × √(k ÷ m)', 'usable band about 30 %, 5 kHz']),
         ('0.488 mg', 'Resolution per LSB', ['32 g span ÷ 65,536 counts', '16 bit ADC, ±16 g range']),
         ('3.2 mg', 'RMS noise', ['100 ug/√Hz × √1000 Hz', 'noise grows with bandwidth'])]
for i, (big, lab, ls) in enumerate(cards):
    x = 30 + (i % 2) * 380; y = 64 + (i // 2) * 236
    s.raw(f'<rect x="{x}" y="{y}" width="360" height="216" rx="16" fill="{L if i in (0, 3) else "#ffffff"}" stroke="{A}" stroke-width="2.5"/>')
    s.t(x + 180, y + 62, big, 36, A, 'bold')
    s.t(x + 180, y + 100, lab, 19, A2, 'bold')
    s.ln(x + 40, y + 120, x + 320, y + 120, '#ddd6fe', 2)
    s.t(x + 180, y + 156, ls[0], 18, '#1a2b4a'); s.t(x + 180, y + 188, ls[1], 17, GREY)
fig(slug, 'mems-accelerometer-key-numbers-infographic',
    'MEMS accelerometer displacement, resonant frequency, resolution and noise worked numbers',
    'Diagram by Instrumentation Blog summarising the article numbers: 0.981 nm displacement at 1g, 15,900 Hz resonance, 0.488 mg resolution and 3.2 mg RMS noise.',
    'Key Electrical Parameters for MEMS Accelerometer Selection', s.svg())

# ================= 4. Electrical energy consumption =================
slug = 'electrical-energy-consumption-calculation'
A, A2, L = '#ca8a04', '#713f12', '#fefce8'
s = S(540, 'Three phase motor energy consumption measurement with line voltage and current')
s.head('Example 2: Energy of a Three Phase Motor', A2)
for i, (y, n) in enumerate([(110, 'L1'), (150, 'L2'), (190, 'L3')]):
    s.ln(60, y, 520, y, ['#b45309', '#1a2b4a', '#6b7280'][i], 4); s.t(45, y + 6, n, 18, '#1a2b4a', 'bold', 'end')
s.raw(f'<circle cx="620" cy="150" r="62" fill="{L}" stroke="{A2}" stroke-width="3"/>'); s.t(620, 145, 'Motor', 19, A2, 'bold'); s.t(620, 170, '3 phase', 17, A2)
for y in (110, 150, 190): s.ln(520, y, 562, 150 + (y - 150) * 0.6, '#1a2b4a', 3)
# clamp on L1
s.raw(f'<ellipse cx="300" cy="110" rx="22" ry="32" fill="none" stroke="{A}" stroke-width="5"/>')
s.ln(300, 142, 300, 240, A, 2.5); s.box(230, 240, 140, 58, ['Clamp meter', 'I_L = 20 A'], '#ffffff', A, size=17)
# voltmeter across L1 L2
s.ln(170, 110, 170, 250, '#1a2b4a', 2); s.ln(140, 150, 140, 250, '#1a2b4a', 2)
s.raw(f'<circle cx="140" cy="150" r="4" fill="#1a2b4a"/><circle cx="170" cy="110" r="4" fill="#1a2b4a"/>')
s.box(70, 250, 140, 58, ['Voltmeter', 'V_L = 415 V'], '#ffffff', A2, size=17)
s.box(410, 240, 150, 58, ['Power factor', 'pf = 0.85'], '#ffffff', A2, size=17)
s.raw(f'<rect x="40" y="340" width="720" height="180" rx="14" fill="{L}" stroke="{A}" stroke-width="2"/>')
s.t(400, 378, 'P = 1.732 × V_L × I_L × pf', 21, A2, 'bold')
s.t(400, 416, '= 1.732 × 415 × 20 × 0.85 = 12,220 W = 12.22 kW', 19, '#1a2b4a')
s.t(400, 456, 'E = 12.22 kW × 10 h = 122.2 kWh', 21, A2, 'bold')
s.t(400, 494, 'Use line to line voltage and line current for three phase loads', 17, GREY)
fig(slug, 'electrical-energy-consumption-three-phase-motor-measurement-diagram',
    'electrical energy consumption of a three phase motor from line voltage, line current and pf',
    'Diagram by Instrumentation Blog showing the article example: 415 V line voltage, 20 A line current and 0.85 power factor give 12.22 kW and 122.2 kWh in 10 hours.',
    'Worked Examples: Energy Consumption Calculations', s.svg())

s = S(560, 'Flowchart for choosing the right energy consumption formula')
s.head('Which kWh Formula Should You Use?', A2)
s.dia(400, 112, 340, 96, ['Load wattage known', 'from nameplate?'], '#ffffff', A, size=18)
s.ar(230, 112, 190, 112); s.t(210, 100, 'Yes', 17, A2, 'bold')
s.box(20, 72, 170, 80, ['Formula 1', 'P × t ÷ 1000'], A, A2, '#ffffff', size=18)
s.ar(400, 160, 400, 190); s.t(420, 180, 'No, measure V, I, pf', 17, A2, 'bold', 'start')
s.dia(400, 240, 340, 96, ['Single phase', 'supply?'], '#ffffff', A, size=18)
s.ar(230, 240, 190, 240); s.t(210, 228, 'Yes', 17, A2, 'bold')
s.box(20, 200, 170, 80, ['Formula 2', 'V × I × pf × t'], A, A2, '#ffffff', size=18)
s.ar(570, 240, 596, 240); s.t(583, 226, 'No', 17, A2, 'bold')
s.box(596, 196, 192, 88, ['Formula 3', '1.732 × V_L × I_L', '× pf × t'], A2, A2, '#ffffff', size=17)
for x0, y0 in ((105, 280), (695, 284)):
    s.pl([(x0, y0), (x0, 340), (400, 340), (400, 376)], A2, 2.5, True)
s.pl([(20, 112), (8, 112), (8, 340), (105, 340)], A2, 2.5, False)
s.box(250, 378, 300, 70, ['Daily kWh for every load', 'then add them up'], L, A, size=18)
s.ar(400, 448, 400, 470)
s.box(230, 470, 340, 70, ['Formula 4', 'Daily kWh × 30 × tariff = cost'], A, A2, '#ffffff', size=18)
fig(slug, 'electrical-energy-consumption-formula-selection-flowchart',
    'flowchart to choose the kWh formula for nameplate, single phase and three phase loads',
    'Diagram by Instrumentation Blog showing when to use each of the four energy formulas: nameplate watts, single phase V and I, three phase line values and monthly cost.',
    'The 4 Electrical Energy Consumption Formulas', s.svg())

s = S(560, 'Monthly energy consumption of a mixed load schedule')
s.head('Mixed Load: Where the 721.5 kWh Goes', A2)
rows = [('Split AC, 1500 W, 8 h', 360), ('5 LED tube lights, 500 W, 10 h', 150), ('3 ceiling fans, 225 W, 18 h', 121.5), ('Water pump, 750 W, 4 h', 90)]
X0 = 60; SC = 520 / 360
for i, (n, v) in enumerate(rows):
    y = 80 + i * 92
    s.t(X0, y + 4, n, 18, '#1a2b4a', 'bold', 'start')
    s.raw(f'<rect x="{X0}" y="{y+14}" width="{v*SC:.0f}" height="40" rx="6" fill="{A if i == 0 else "#fde68a"}" stroke="{A2}" stroke-width="1.5"/>')
    s.t(X0 + v * SC + 12, y + 42, f'{v:g} kWh', 18, A2, 'bold', 'start')
s.raw(f'<rect x="60" y="452" width="680" height="88" rx="14" fill="{L}" stroke="{A}" stroke-width="2"/>')
s.t(400, 486, 'Total 24.05 kWh per day, 721.5 kWh per month', 20, A2, 'bold')
s.t(400, 520, 'At Rs 6.00 per kWh: Rs 4,329 per month. The AC is nearly 50 %', 18, '#1a2b4a')
fig(slug, 'electrical-energy-consumption-mixed-load-chart',
    'electrical energy consumption bar chart of AC, lights, fans and pump monthly kWh',
    'Diagram by Instrumentation Blog charting the mixed load table: the split AC uses 360 of 721.5 kWh a month, costing Rs 4,329 in total at Rs 6.00 per kWh.',
    'Mixed Load Schedule: How to Add Up Multiple Appliances', s.svg())

# ================= 5. Split range control =================
slug = 'split-range-control-working-principle'
A, A2, L = '#dc2626', '#7f1d1d', '#fef2f2'
B = '#2563eb'
def bowtie(s, x, y, c):
    s.raw(f'<polygon points="{x-16},{y-11} {x+16},{y+11} {x+16},{y-11} {x-16},{y+11}" fill="#ffffff" stroke="{c}" stroke-width="2.5"/>')
    s.ln(x, y, x, y - 22, c, 2.5); s.raw(f'<path d="M{x-16} {y-22} A16 14 0 0 1 {x+16} {y-22} Z" fill="#ffffff" stroke="{c}" stroke-width="2.5"/>')
s = S(560, 'Split range temperature control with two I/P converters')
s.head('Split Range Temperature Loop', A2)
s.raw(f'<rect x="300" y="250" width="200" height="220" rx="40" fill="#f1f5f9" stroke="#334155" stroke-width="3"/>')
s.t(400, 370, 'Process', 19, '#334155', 'bold')
s.raw(f'<circle cx="470" cy="196" r="26" fill="#ffffff" stroke="#334155" stroke-width="2.5"/>'); s.t(470, 203, 'TT', 18, '#334155', 'bold'); s.ln(470, 222, 470, 250, '#334155', 2.5)
s.raw(f'<circle cx="400" cy="104" r="32" fill="#ffffff" stroke="#334155" stroke-width="2.5"/>'); s.t(400, 111, 'TC', 19, '#334155', 'bold')
s.pl([(470, 170), (470, 104), (434, 104)], '#334155', 2, True, '6 5')
s.pl([(366, 104), (150, 104), (150, 148)], '#334155', 2, True, '6 5')
s.pl([(400, 72), (400, 62), (650, 62), (650, 148)], '#334155', 2, True, '6 5')
s.t(258, 94, '4 to 20 mA', 17, GREY); s.t(540, 54, '4 to 20 mA', 17, GREY)
s.box(80, 148, 140, 62, ['I/P 1', '4 to 12 mA'], '#eff6ff', B, size=17)
s.box(580, 148, 140, 62, ['I/P 2', '12 to 20 mA'], L, A, size=17)
s.ln(20, 340, 300, 340, B, 6); s.ar(40, 340, 80, 340, B, 2.5); s.t(30, 376, 'Cooling water', 17, B, 'bold', 'start')
s.ln(500, 340, 780, 340, A, 6); s.ar(760, 340, 720, 340, A, 2.5); s.t(770, 376, 'Steam', 17, A, 'bold', 'end')
s.ln(150, 210, 150, 296, B, 2, '3 3'); s.ln(650, 210, 650, 296, A, 2, '3 3')
bowtie(s, 150, 340, B); bowtie(s, 650, 340, A)
s.t(150, 410, 'Cooling valve', 17, B, 'bold'); s.t(650, 410, 'Heating valve', 17, A, 'bold')
s.raw(f'<rect x="30" y="486" width="740" height="64" rx="12" fill="#ffffff" stroke="#d1d5db" stroke-width="2"/>')
s.t(400, 512, 'Output 0 to 50 %: cooling valve, fully open at 0 %, shut at 50 %', 17, B, 'bold')
s.t(400, 538, 'Output 50 to 100 %: heating valve opens, fully open at 100 %', 17, A, 'bold')
fig(slug, 'split-range-control-temperature-loop-diagram',
    'split range control temperature loop with TC, two I/P converters, cooling and steam valves',
    'Diagram by Instrumentation Blog showing one temperature controller output split by two I/P converters, 4 to 12 mA to the cooling valve and 12 to 20 mA to the heating valve.',
    'Example: Split Range for Temperature Control Application', s.svg())

s = S(560, 'Flowchart of the split range reactor held at 70 degrees C')
s.head('Reactor at 70 °C: What the Split Range Does', A2)
s.box(270, 56, 260, 56, ['PID reads temperature'], '#ffffff', '#334155', size=18)
s.ar(400, 112, 400, 134)
s.dia(400, 190, 330, 108, ['Temperature vs', '70 °C setpoint?'], '#ffffff', '#334155', size=18)
s.ar(235, 190, 190, 190); s.t(212, 176, 'Low', 17, A2, 'bold')
s.ar(565, 190, 610, 190); s.t(588, 176, 'High', 17, B, 'bold')
s.box(20, 150, 170, 80, ['Output moves', 'toward 4 mA'], L, A, size=18)
s.box(610, 150, 170, 80, ['Output moves', 'toward 20 mA'], '#eff6ff', B, size=18)
s.ar(105, 230, 105, 270, A2); s.ar(695, 230, 695, 270, B)
s.box(20, 270, 170, 90, ['4 to 12 mA', 'steam valve', 'opens'], A, A2, '#ffffff', size=18)
s.box(610, 270, 170, 90, ['12 to 20 mA', 'cooling valve', 'opens'], B, '#1e3a8a', '#ffffff', size=18)
s.ar(400, 244, 400, 290); s.t(420, 272, 'At setpoint', 17, '#334155', 'bold', 'start')
s.box(260, 290, 280, 70, ['About 12 mA', 'both valves closed'], '#f0fdf4', '#16a34a', size=18)
s.pl([(105, 360), (105, 430), (300, 430)], A2, 2.5); s.pl([(695, 360), (695, 430), (500, 430)], '#1e3a8a', 2.5)
s.box(300, 400, 200, 60, ['Back to 70 °C'], '#ffffff', '#334155', size=18)
s.t(400, 510, 'This example puts heating at the low end; the first example', 17, GREY)
s.t(400, 536, 'puts cooling at 0 to 50 %. The controller action decides which.', 17, GREY)
fig(slug, 'split-range-control-reactor-heating-cooling-flowchart',
    'flowchart of split range control opening steam or cooling valve for a 70 C reactor',
    'Diagram by Instrumentation Blog following the 70 degree reactor example: low temperature drives the output toward 4 mA for steam, high temperature toward 20 mA for cooling.',
    'Example: Temperature Control With Heating & Cooling', s.svg())

s = S(560, 'Valve opening versus controller output for three split range types')
s.head('3 Types of Split Range Control', A2)
def panel(x, title, a_rng, b_rng):
    w, h, y0 = 230, 230, 120
    s.raw(f'<rect x="{x}" y="{y0-50}" width="{w+20}" height="{h+150}" rx="14" fill="#ffffff" stroke="#e5e7eb" stroke-width="2"/>')
    s.t(x + 10 + w / 2, y0 - 18, title, 19, A2, 'bold')
    gx, gy = x + 50, y0 + h - 30; gw, gh = w - 70, h - 70
    def X(mA): return gx + (mA - 4) / 16 * gw
    def Y(p): return gy - p / 100 * gh
    s.ln(gx, gy, gx + gw, gy, '#1a2b4a', 2); s.ln(gx, gy, gx, gy - gh - 6, '#1a2b4a', 2)
    for mA in (4, 12, 20): s.t(X(mA), gy + 24, str(mA), 17, '#1a2b4a')
    s.t(gx - 8, Y(100) + 6, '100', 17, GREY, 'normal', 'end'); s.t(gx - 8, gy + 6, '0', 17, GREY, 'normal', 'end')
    s.pl([(X(4), Y(a_rng[2])), (X(a_rng[0]), Y(a_rng[2])), (X(a_rng[1]), Y(a_rng[3])), (X(20), Y(a_rng[3]))], B, 4, False)
    s.pl([(X(4), Y(b_rng[2])), (X(b_rng[0]), Y(b_rng[2])), (X(b_rng[1]), Y(b_rng[3])), (X(20), Y(b_rng[3]))], A, 4, False, '8 5')
    return gy
for x, t, a, b, n1, n2 in [(15, 'Sequential', (4, 12, 0, 100), (12, 20, 0, 100), 'A 4 to 12 mA', 'B 12 to 20 mA'),
                          (275, 'Overlapping', (4, 16, 0, 100), (8, 20, 0, 100), 'A 4 to 16 mA', 'B 8 to 20 mA'),
                          (535, 'Complementary', (4, 20, 0, 100), (4, 20, 100, 0), 'A supply opens', 'B vent closes')]:
    gy = panel(x, t, a, b)
    s.t(x + 125, gy + 60, n1, 17, B, 'bold'); s.t(x + 125, gy + 86, n2, 17, A, 'bold')
s.t(400, 520, 'Valve opening in % against controller output in mA', 18, '#1a2b4a', 'bold')
s.t(400, 548, 'Overlap gives a smooth handover; in complementary one closes as the other opens', 17, GREY)
fig(slug, 'split-range-control-types-valve-opening-chart',
    'split range control types: sequential, overlapping and complementary valve opening curves',
    'Diagram by Instrumentation Blog plotting valve opening against controller output for sequential 4 to 12 and 12 to 20 mA, overlapping 4 to 16 and 8 to 20 mA, and complementary ranges.',
    'Types of Split Range Control', s.svg())

if __name__ == '__main__': main()
