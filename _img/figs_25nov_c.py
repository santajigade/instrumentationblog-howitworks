import sys; sys.path.insert(0, '/home/claude/instrumentationblog-howitworks/_img'); from figs_24nov_common import *
GREY = '#4b5563'

# ================= 1. Zero and span =================
slug = 'zero-and-span-adjustments'
A, A2, L = '#0891b2', '#164e63', '#ecfeff'
def axes(s, X0, Y0, W, H, xl, yl, xt, yt):
    s.ln(X0, Y0, X0 + W, Y0, '#1a2b4a', 2.5); s.ln(X0, Y0, X0, Y0 - H, '#1a2b4a', 2.5)
    for v, lab in xt: s.ln(X0 + v * W, Y0, X0 + v * W, Y0 + 6, '#1a2b4a', 2); s.t(X0 + v * W, Y0 + 26, lab, 17, '#1a2b4a')
    for v, lab in yt: s.ln(X0 - 6, Y0 - v * H, X0, Y0 - v * H, '#1a2b4a', 2); s.t(X0 - 10, Y0 - v * H + 6, lab, 17, '#1a2b4a', 'normal', 'end')
    s.t(X0 + W / 2, Y0 + 54, xl, 18, '#1a2b4a', 'bold')
s = S(560, 'Transmitter calibration line y equals 0.16x plus 4 with live zero')
s.head('y = 0.16x + 4 for a 0 to 100 PSI, 4 to 20 mA Transmitter', A2)
X0, Y0, W, H = 110, 440, 400, 360
ymA = lambda m: (m) / 20
axes(s, X0, Y0, W, H, 'Input pressure, PSI', '', [(0, '0'), (0.25, '25'), (0.5, '50'), (0.75, '75'), (1, '100')], [(0, '0'), (0.2, '4'), (0.6, '12'), (1, '20')])
s.t(60, 70, 'mA', 18, '#1a2b4a', 'bold')
for v in (0.2, 0.6, 1.0): s.ln(X0, Y0 - v * H, X0 + W, Y0 - v * H, '#e5e7eb', 1.5)
s.ln(X0, Y0 - 0.2 * H, X0 + W, Y0 - H, A, 4)
s.ln(X0 + 0.5 * W, Y0, X0 + 0.5 * W, Y0 - 0.6 * H, A2, 2, '6 5'); s.ln(X0, Y0 - 0.6 * H, X0 + 0.5 * W, Y0 - 0.6 * H, A2, 2, '6 5')
s.raw(f'<circle cx="{X0+0.5*W}" cy="{Y0-0.6*H}" r="7" fill="{A2}"/><circle cx="{X0}" cy="{Y0-0.2*H}" r="7" fill="#dc2626"/>')
s.t(X0 + 16, Y0 - 0.2 * H + 28, 'Live zero:', 17, '#dc2626', 'bold', 'start'); s.t(X0 + 16, Y0 - 0.2 * H + 50, '0 PSI gives 4 mA', 17, '#dc2626', 'bold', 'start')
s.raw(f'<rect x="545" y="90" width="235" height="300" rx="14" fill="{L}" stroke="{A}" stroke-width="2"/>')
for i, (t_, b) in enumerate([('m = 16 ÷ 100', 0), ('= 0.16 mA per PSI', 0), ('b = 4 mA', 1), ('At 50 PSI:', 1), ('0.16 × 50 + 4', 0), ('= 12 mA', 1), ('Span = 20 − 4', 0), ('= 16 mA', 1)]):
    s.t(662, 124 + i * 34, t_, 18, A2 if b else '#1a2b4a', 'bold' if b else 'normal')
s.t(400, 540, 'Zero sets b, the intercept. Span sets m, the slope.', 18, A2, 'bold')
fig(slug, 'zero-and-span-calibration-line-chart',
    'zero and span calibration line y = 0.16x + 4 for a pressure transmitter',
    'Diagram by Instrumentation Blog plotting the article equation y = 0.16x + 4: 0 PSI gives the 4 mA live zero, 50 PSI gives 12 mA and 100 PSI gives 20 mA.',
    'Linear Slope Intercept Equation for Instrument Calibration', s.svg())

s = S(520, 'Zero error shifts the line while span error changes its slope')
s.head('Zero Shifts the Line, Span Tilts It', A2)
for k, (x0, title, sub) in enumerate([(40, 'Zero adjustment', 'adds or subtracts, changes b'), (430, 'Span adjustment', 'multiplies or divides, changes m')]):
    X0, Y0, W, H = x0 + 50, 400, 280, 260
    s.ln(X0, Y0, X0 + W, Y0, '#1a2b4a', 2.5); s.ln(X0, Y0, X0, Y0 - H, '#1a2b4a', 2.5)
    s.t(X0 + W / 2, Y0 + 28, 'Input 0 to 100 %', 17, '#1a2b4a'); s.t(X0 - 10, Y0 - H + 6, 'Out', 17, '#1a2b4a', 'normal', 'end')
    s.ln(X0, Y0 - 0.2 * H, X0 + W, Y0 - H, '#16a34a', 4)
    if k == 0:
        s.ln(X0, Y0 - 0.34 * H, X0 + W * 0.86, Y0 - H * 1.0, '#dc2626', 3, '8 5'); s.ln(X0, Y0 - 0.06 * H, X0 + W, Y0 - 0.86 * H, '#dc2626', 3, '8 5')
        s.ar(X0 + 140, Y0 - 0.6 * H - 34, X0 + 140, Y0 - 0.6 * H - 6, '#dc2626', 2.5); s.ar(X0 + 140, Y0 - 0.6 * H + 40, X0 + 140, Y0 - 0.6 * H + 10, '#dc2626', 2.5)
    else:
        s.ln(X0, Y0 - 0.2 * H, X0 + W, Y0 - 0.78 * H, '#dc2626', 3, '8 5'); s.ln(X0, Y0 - 0.2 * H, X0 + W * 0.78, Y0 - H, '#dc2626', 3, '8 5')
        s.raw(f'<circle cx="{X0}" cy="{Y0-0.2*H}" r="7" fill="{A2}"/>'); s.t(X0 + 14, Y0 - 0.2 * H + 28, 'pivot at zero', 17, A2, 'bold', 'start')
    s.t(x0 + 180, 80, title, 20, A2, 'bold'); s.t(x0 + 180, 106, sub, 17, GREY)
s.ln(20, 470, 780, 470, '#e5e7eb', 2)
s.ln(60, 495, 100, 495, '#16a34a', 4); s.t(110, 501, 'Ideal line', 17, '#16a34a', 'bold', 'start')
s.ln(300, 495, 340, 495, '#dc2626', 3, '8 5'); s.t(350, 501, 'Instrument before adjustment', 17, '#dc2626', 'bold', 'start')
fig(slug, 'zero-and-span-shift-diagram',
    'zero and span adjustment diagram: zero shifts the line, span changes the slope',
    'Diagram by Instrumentation Blog comparing a zero adjustment, which moves the whole response line up or down, with a span adjustment, which changes the slope about the zero point.',
    'Zero and Span Adjustments', s.svg())

s = S(580, 'Flowchart of the zero and span calibration loop for an analog transmitter')
s.head('Zero and Span Calibration Loop', A2)
s.box(250, 56, 300, 56, ['Apply 0 % input, the LRV'], L, A, size=18)
s.ar(400, 112, 400, 132)
s.box(250, 132, 300, 56, ['Adjust zero for 4 mA'], A, A2, '#ffffff', size=18)
s.ar(400, 188, 400, 208)
s.box(250, 208, 300, 56, ['Apply 100 % input, the URV'], L, A, size=18)
s.ar(400, 264, 400, 284)
s.box(250, 284, 300, 56, ['Adjust span for 20 mA'], A, A2, '#ffffff', size=18)
s.ar(400, 340, 400, 362)
s.dia(400, 414, 340, 104, ['Zero still at 4 mA', 'after span change?'], '#ffffff', A2, size=18)
s.ar(570, 414, 610, 414); s.t(590, 400, 'Yes', 17, A2, 'bold')
s.box(610, 380, 170, 68, ['Calibration', 'complete'], '#16a34a', '#14532d', '#ffffff', size=18)
s.pl([(230, 414), (150, 414), (150, 84), (248, 84)], '#dc2626', 2.5); s.t(140, 400, 'No', 17, '#dc2626', 'bold', 'end')
s.t(140, 250, 'repeat', 17, '#dc2626', 'bold', 'end')
s.t(400, 510, 'In most analog instruments zero and span interact,', 17, GREY)
s.t(400, 536, 'so the technician goes back and forth until both are right', 17, GREY)
fig(slug, 'zero-and-span-calibration-flowchart',
    'zero and span calibration flowchart: set 4 mA at LRV, 20 mA at URV, repeat',
    'Diagram by Instrumentation Blog showing the back and forth calibration loop: set zero at 0 percent, span at 100 percent, then recheck zero because the two adjustments interact.',
    'Zero and Span Calibration', s.svg())

# ================= 2. DCS function block programming =================
slug = 'dcs-function-block-programming-explained'
A, A2, L = '#2563eb', '#1e3a8a', '#eff6ff'
def fblock(s, x, y, name, tag, ins, outs, c=A):
    s.raw(f'<rect x="{x}" y="{y}" width="150" height="150" rx="6" fill="#ffffff" stroke="{c}" stroke-width="3"/>')
    s.raw(f'<rect x="{x}" y="{y}" width="150" height="34" rx="6" fill="{c}"/>')
    s.t(x + 75, y + 24, name, 19, '#ffffff', 'bold'); s.t(x + 75, y + 140, tag, 17, GREY)
    for i, n in enumerate(ins): s.t(x + 8, y + 62 + i * 26, n, 17, '#1a2b4a', 'normal', 'start')
    for i, n in enumerate(outs): s.t(x + 142, y + 62 + i * 26, n, 17, '#1a2b4a', 'normal', 'end')
s = S(540, 'DCS function block loop AI to PID to AO with back calculation')
s.head('AI to PID to AO: One Flow Loop in Function Blocks', A2)
s.raw(f'<circle cx="70" cy="190" r="34" fill="#ffffff" stroke="#334155" stroke-width="2.5"/>'); s.t(70, 197, 'FT', 19, '#334155', 'bold')
s.t(70, 250, 'transmitter', 17, GREY)
s.ar(104, 190, 128, 190, '#334155', 2.5); 
fblock(s, 130, 120, 'AI', 'FI 101', ['IN'], ['OUT'])
s.ar(280, 172, 318, 172, A2, 3)
fblock(s, 320, 120, 'PID', 'FIC 101', ['PV', 'SP', 'BKCAL'], ['OUT'])
s.ar(470, 172, 508, 172, A2, 3)
fblock(s, 510, 120, 'AO', 'FV 101', ['CAS IN'], ['OUT'])
s.pl([(585, 270), (585, 310), (395, 310), (395, 272)], '#dc2626', 2.5, True, '7 5')
s.t(490, 336, 'Back calculation stops integral windup', 17, '#dc2626', 'bold')
s.ar(660, 172, 690, 172, '#334155', 2.5)
s.raw(f'<polygon points="700,160 740,184 740,160 700,184" fill="#ffffff" stroke="#334155" stroke-width="2.5"/>')
s.ln(720, 172, 720, 140, '#334155', 2.5); s.raw('<path d="M702 140 A18 16 0 0 1 738 140 Z" fill="#ffffff" stroke="#334155" stroke-width="2.5"/>')
s.t(720, 220, 'valve', 17, GREY)
s.raw(f'<rect x="30" y="362" width="740" height="160" rx="14" fill="{L}" stroke="{A}" stroke-width="2"/>')
s.t(400, 394, 'AI scales the raw signal to engineering units and checks alarms', 17, '#1a2b4a')
s.t(400, 428, 'PID compares flow with setpoint every scan and calculates output', 17, '#1a2b4a')
s.t(400, 462, 'AO converts the output to 4 to 20 mA for the valve', 17, '#1a2b4a')
s.t(400, 498, 'Execution order: AI runs first in the same scan', 17, A2, 'bold')
fig(slug, 'dcs-function-block-programming-ai-pid-ao-loop-diagram',
    'DCS function block programming loop with AI, PID and AO blocks and back calculation',
    'Diagram by Instrumentation Blog showing a flow loop built from AI, PID and AO function blocks, with the back calculation link from AO to PID that prevents integral windup.',
    'How a Signal Flows Through a Simple Control Loop', s.svg())

s = S(600, 'Troubleshooting flowchart for a DCS function block strategy')
s.head('Loop Misbehaving? Check the Blocks First', A2)
qs = [(['PID block left', 'in Manual mode?'], 'Return to Auto or', 'Cascade, bumpless'),
      (['AI reading a', 'frozen value?'], 'Check AI status,', 'range and alarms'),
      (['AO clamped', 'at a limit?'], 'Check output limits', 'and back calculation'),
      (['Block reads stale', 'data each scan?'], 'Fix execution index,', 'source block first')]
s.box(250, 50, 300, 52, ['Watch live values online'], L, A, size=18)
s.ar(400, 102, 400, 116)
for i, (q, a, b) in enumerate(qs):
    cy = 160 + i * 110
    s.dia(400, cy, 300, 88, q, '#ffffff', A, size=17)
    s.ar(550, cy, 590, cy); s.t(570, cy - 12, 'Yes', 17, A2, 'bold')
    s.box(590, cy - 36, 190, 72, [a, b], A, A2, '#ffffff', size=17)
    if i < 3: s.ar(400, cy + 44, 400, cy + 66); s.t(420, cy + 60, 'No', 17, GREY, 'bold', 'start')
s.ar(400, 534, 400, 556); s.t(420, 550, 'No', 17, GREY, 'bold', 'start')
s.box(220, 556, 360, 40, ['Then check field wiring and devices'], '#ffffff', GREY, size=17)
fig(slug, 'dcs-function-block-programming-troubleshooting-flowchart',
    'troubleshooting flowchart for DCS function blocks: manual mode, frozen AI, clamped AO, execution order',
    'Diagram by Instrumentation Blog listing the block level checks from the article: PID left in Manual, frozen AI value, AO clamped at a limit and wrong execution order.',
    'Troubleshooting a DCS Function Block Strategy', s.svg())

s = S(560, 'Anatomy of a DCS function block and the three PID modes')
s.head('Anatomy of a Function Block', A2)
s.raw(f'<rect x="250" y="70" width="300" height="250" rx="10" fill="#ffffff" stroke="{A}" stroke-width="3"/>')
s.raw(f'<rect x="250" y="70" width="300" height="50" rx="10" fill="{A}"/>')
s.t(400, 103, 'PID', 22, '#ffffff', 'bold')
s.t(400, 160, 'FIC 101', 20, A2, 'bold'); s.t(400, 200, 'Kp, Ki, Kd, alarms', 17, '#1a2b4a'); s.t(400, 232, 'limits, bias', 17, '#1a2b4a')
s.t(400, 296, 'runs 3rd in the module', 17, GREY)
parts = [(20, 80, 'Definition name', ['algorithm type', 'AI, PID, AND'], (250, 100)),
         (20, 220, 'Tag name', ['unique instance', 'such as FIC 101'], (250, 160)),
         (580, 80, 'Parameters', ['inputs, outputs,', 'alarms, tuning'], (550, 210)),
         (580, 220, 'Execution index', ['order it runs in', 'each scan'], (550, 296))]
for x, y, t_, ls, (px, py) in parts:
    s.box(x, y, 200, 100, [t_] + ls, L, A, size=17)
    s.ln(x + (200 if x < 250 else 0), y + 50, px, py, A2, 2, '5 4')
modes = [('Manual', 'operator sets output'), ('Auto', 'own SP and PV'), ('Cascade', 'SP from upstream block')]
for i, (m, d) in enumerate(modes):
    x = 30 + i * 255
    s.raw(f'<rect x="{x}" y="380" width="230" height="96" rx="12" fill="{A2 if i == 1 else "#ffffff"}" stroke="{A2}" stroke-width="2.5"/>')
    s.t(x + 115, 418, m, 20, '#ffffff' if i == 1 else A2, 'bold'); s.t(x + 115, 450, d, 17, '#ffffff' if i == 1 else '#1a2b4a')
s.t(400, 360, 'PID block modes', 18, A2, 'bold')
s.t(400, 520, 'Switching modes without an output jump is bumpless transfer', 17, GREY)
fig(slug, 'dcs-function-block-programming-anatomy-infographic',
    'DCS function block programming anatomy: definition, tag name, parameters, execution index, modes',
    'Diagram by Instrumentation Blog breaking a PID function block into definition name, tag name, parameters and execution index, plus the Manual, Auto and Cascade modes.',
    'Anatomy of a Function Block', s.svg())

# ================= 3. Multifunction process calibrator =================
slug = 'multifunction-process-calibrator-uses'
A, A2, L = '#d97706', '#78350f', '#fffbeb'
s = S(560, 'Multifunction process calibrator bench setup sourcing pressure and measuring transmitter mA')
s.head('Calibrator Setup: Apply Pressure, Read mA', A2)
# calibrator
s.raw(f'<rect x="300" y="250" width="200" height="270" rx="22" fill="#fde68a" stroke="{A2}" stroke-width="3"/>')
s.raw(f'<rect x="320" y="270" width="160" height="96" rx="6" fill="#1f2937"/>')
s.t(400, 304, 'MEAS 12.04 mA', 17, '#4ade80', 'bold'); s.t(400, 340, 'P 5.000 bar', 17, '#fbbf24', 'bold')
s.t(400, 400, 'Calibrator', 19, A2, 'bold'); s.t(400, 426, 'two channels', 17, A2)
s.raw(f'<circle cx="340" cy="490" r="9" fill="#dc2626"/><circle cx="370" cy="490" r="9" fill="#111827"/><circle cx="430" cy="490" r="9" fill="#dc2626"/><circle cx="460" cy="490" r="9" fill="#111827"/>')
s.t(355, 466, 'mA, 24 V', 17, A2, 'bold'); s.t(445, 466, 'module', 17, A2, 'bold')
# transmitter
s.raw(f'<rect x="80" y="80" width="150" height="110" rx="12" fill="#ffffff" stroke="#334155" stroke-width="3"/>')
s.t(155, 122, 'Pressure', 18, '#334155', 'bold'); s.t(155, 148, 'transmitter', 18, '#334155', 'bold'); s.t(155, 174, '0 to 10 bar', 17, GREY)
s.ln(155, 190, 155, 230, '#334155', 6)
# hand pump and module
s.raw(f'<rect x="560" y="90" width="170" height="90" rx="12" fill="#ffffff" stroke="#334155" stroke-width="3"/>')
s.t(645, 128, 'Hand pump', 18, '#334155', 'bold'); s.t(645, 154, 'applies 5 bar', 17, GREY)
s.raw(f'<rect x="590" y="250" width="110" height="70" rx="10" fill="{A}" stroke="{A2}" stroke-width="2"/>'); s.t(645, 282, 'Pressure', 17, '#ffffff', 'bold')
s.t(645, 306, 'module', 17, '#ffffff', 'bold')
s.pl([(645, 180), (645, 250)], '#334155', 5, False)
s.pl([(645, 215), (155, 215), (155, 230)], '#334155', 5, False)
s.t(400, 206, 'pressure line', 17, GREY)
s.pl([(469, 490), (540, 490), (540, 290), (590, 290)], A2, 2.5, False)
s.pl([(331, 490), (50, 490), (50, 130), (80, 130)], '#dc2626', 2.5, False)
s.pl([(370, 499), (370, 530), (30, 530), (30, 160), (80, 160)], '#111827', 2.5, False)
s.t(150, 330, 'Loop powered', 17, '#dc2626', 'bold'); s.t(150, 354, 'by the 24 V', 17, '#dc2626', 'bold'); s.t(150, 378, 'supply', 17, '#dc2626', 'bold')
fig(slug, 'multifunction-process-calibrator-transmitter-setup-diagram',
    'multifunction process calibrator setup powering a transmitter and reading its mA output',
    'Diagram by Instrumentation Blog showing one calibrator reading the 5 bar input through a pressure module while its 24 V loop supply powers the transmitter and measures 12.04 mA.',
    'Measure, Source and Simulate Functions', s.svg())

s = S(600, 'Flowchart of a transmitter calibration with a multifunction process calibrator')
s.head('As Found to As Left With One Calibrator', A2)
st = [['Enter range, LRV and URV'], ['Step 0, 25, 50, 75, 100 %'], ['Read mA, calculate error', '% of span at each point']]
y = 56
for i, b in enumerate(st):
    h = 52 if len(b) == 1 else 66
    s.box(230, y, 340, h, b, L if i % 2 == 0 else '#ffffff', A, size=18)
    s.ar(400, y + h, 400, y + h + 20); y += h + 20
s.dia(400, y + 50, 340, 100, ['Every point within', 'tolerance?'], '#ffffff', A2, size=18)
s.ar(570, y + 50, 610, y + 50); s.t(590, y + 36, 'Yes', 17, '#16a34a', 'bold')
s.box(610, y + 14, 170, 72, ['Pass, store', 'results'], '#16a34a', '#14532d', '#ffffff', size=18)
s.ar(400, y + 100, 400, y + 130); s.t(420, y + 120, 'No', 17, '#dc2626', 'bold', 'start')
s.box(230, y + 130, 340, 66, ['Zero and span adjust', 'or sensor trim'], A, A2, '#ffffff', size=18)
s.pl([(230, y + 163), (150, y + 163), (150, 56 + 52 + 20 + 26), (228, 56 + 52 + 20 + 26)], '#dc2626', 2.5)
s.t(140, y + 60, 'as left', 17, '#dc2626', 'bold', 'end'); s.t(140, y + 84, 'test', 17, '#dc2626', 'bold', 'end')
s.t(400, 560, 'Keep at least 4 to 1 accuracy ratio between calibrator and device', 17, GREY)
fig(slug, 'multifunction-process-calibrator-calibration-flowchart',
    'flowchart of as found and as left transmitter calibration with a process calibrator',
    'Diagram by Instrumentation Blog showing the calibration routine: enter the range, step through five points, check error against tolerance, adjust or trim, then repeat as left.',
    'Accuracy, Traceability and Good Practice', s.svg())

s = S(540, 'Transmitter error worked example from the article')
s.head('Transmitter Error: 0 to 10 bar at 5 bar', A2)
s.raw(f'<rect x="30" y="70" width="740" height="110" rx="14" fill="{L}" stroke="{A}" stroke-width="2"/>')
s.t(400, 108, 'Expected mA = 4 + 16 × (Input − LRV) ÷ (URV − LRV)', 19, A2, 'bold')
s.t(400, 150, 'Error % of span = (Measured − Expected) ÷ 16 × 100', 19, A2, 'bold')
cards = [('12.00 mA', 'Expected', '4 + 16 × (5 ÷ 10)'), ('12.04 mA', 'Measured', 'read by calibrator'), ('0.25 %', 'Error of span', '(12.04 − 12.00) ÷ 16 × 100')]
for i, (big, lab, sub) in enumerate(cards):
    x = 30 + i * 252
    s.raw(f'<rect x="{x}" y="210" width="236" height="170" rx="14" fill="{A if i == 2 else "#ffffff"}" stroke="{A2}" stroke-width="2.5"/>')
    c = '#ffffff' if i == 2 else A2
    s.t(x + 118, 268, big, 32, c, 'bold'); s.t(x + 118, 308, lab, 19, c, 'bold'); s.t(x + 118, 346, sub, 17, '#ffffff' if i == 2 else GREY)
s.raw(f'<rect x="30" y="410" width="740" height="100" rx="14" fill="#ffffff" stroke="{A}" stroke-width="2"/>')
s.t(400, 448, 'Test uncertainty ratio 4 to 1:', 18, A2, 'bold')
s.t(400, 482, 'a 0.1 % transmitter needs a calibrator of about 0.025 % or better', 18, '#1a2b4a')
fig(slug, 'multifunction-process-calibrator-error-infographic',
    'multifunction process calibrator transmitter error example, 12.00 mA expected, 0.25 percent error',
    'Diagram by Instrumentation Blog working the article example: a 0 to 10 bar transmitter at 5 bar should give 12.00 mA, reads 12.04 mA, so the error is 0.25 percent of span.',
    'Transmitter Error Formula With a Worked Example', s.svg())

# ================= 4. Offset error =================
slug = 'offset-error-zero-point-error-span-error'
A, A2, L = '#e11d48', '#881337', '#fff1f2'
G = '#16a34a'
s = S(560, 'Offset error versus span error on a pressure sensor output graph')
s.head('Offset Error vs Span Error: Two Cases', A2)
for k, (x0, title, err, pts, lab) in enumerate([(30, 'Case 1: offset only', 'shifted 2 mV, drawn larger', [(0, 12), (10, 112)], '0 psi gives 2 mV, 10 psi gives 102 mV'),
                                             (420, 'Case 2: span only', 'slope 11 mV per psi', [(0, 0), (10, 110)], '0 psi gives 0 mV, 10 psi gives 110 mV')]):
    X0, Y0, W, H = x0 + 70, 420, 270, 300
    px = lambda p: X0 + p / 10 * W
    py = lambda v: Y0 - v / 120 * H
    s.ln(X0, Y0, X0 + W, Y0, '#1a2b4a', 2.5); s.ln(X0, Y0, X0, Y0 - H, '#1a2b4a', 2.5)
    for v in (0, 50, 100):
        s.t(X0 - 10, py(v) + 6, str(v), 17, '#1a2b4a', 'normal', 'end'); s.ln(X0, py(v), X0 + W, py(v), '#f1f5f9', 1.5)
    s.t(X0 - 10, py(120) + 6, 'mV', 17, '#1a2b4a', 'bold', 'end')
    for p in (0, 5, 10): s.t(px(p), Y0 + 26, str(p), 17, '#1a2b4a')
    s.t(X0 + W / 2, Y0 + 52, 'pressure, psi', 17, '#1a2b4a')
    s.ln(px(0), py(0), px(10), py(100), G, 4)
    s.ln(px(pts[0][0]), py(pts[0][1]), px(pts[1][0]), py(pts[1][1]), A, 3.5, '9 6')
    s.raw(f'<circle cx="{px(10)}" cy="{py(pts[1][1])}" r="6" fill="{A}"/><circle cx="{px(10)}" cy="{py(100)}" r="6" fill="{G}"/>')
    if k == 0: s.ln(px(5), py(50), px(5), py(62), A2, 2); s.t(px(5) + 10, py(56) + 30, 'constant gap', 17, A2, 'bold', 'start')
    s.t(x0 + 175, 80, title, 20, A2, 'bold'); s.t(x0 + 175, 106, err, 17, A, 'bold')
s.ln(140, 512, 180, 512, G, 4); s.t(190, 518, 'Ideal: 10 mV per psi', 17, G, 'bold', 'start')
s.ln(430, 512, 470, 512, A, 3.5, '9 6'); s.t(480, 518, 'Sensor output', 17, A, 'bold', 'start')
s.t(400, 548, 'Offset moves the whole line, span changes its slope', 17, GREY)
fig(slug, 'offset-error-vs-span-error-diagram',
    'offset error vs span error graph for a pressure sensor at 0 and 10 psi',
    'Diagram by Instrumentation Blog plotting the two article cases: a 2 mV offset that shifts the whole line, and a span error that raises the slope to 11 mV per psi.',
    'Offset Error and Span Error', s.svg())

s = S(580, 'Flowchart to find and correct offset and span errors during calibration')
s.head('Finding and Fixing Offset and Span Errors', A2)
s.box(250, 56, 300, 56, ['Apply 0 psi reference'], L, A, size=18)
s.ar(400, 112, 400, 130)
s.dia(400, 180, 320, 100, ['Output different', 'from 0 mV?'], '#ffffff', A, size=18)
s.ar(560, 180, 600, 180); s.t(580, 166, 'Yes', 17, A2, 'bold')
s.box(600, 144, 180, 72, ['Offset error:', 'adjust zero trim'], A, A2, '#ffffff', size=17)
s.ar(400, 230, 400, 254); s.t(385, 250, 'No', 17, GREY, 'bold', 'end')
s.pl([(690, 216), (690, 236), (400, 236)], A2, 2, False)
s.box(250, 254, 300, 56, ['Apply 10 psi reference'], L, A, size=18)
s.ar(400, 310, 400, 328)
s.dia(400, 378, 320, 100, ['Output different', 'from 100 mV?'], '#ffffff', A, size=18)
s.ar(560, 378, 600, 378); s.t(580, 364, 'Yes', 17, A2, 'bold')
s.box(600, 342, 180, 72, ['Span error:', 'adjust span trim'], A, A2, '#ffffff', size=17)
s.ar(400, 428, 400, 452); s.t(420, 444, 'No', 17, GREY, 'bold', 'start')
s.box(250, 452, 300, 60, ['Both corrected,', 'readings are true'], '#f0fdf4', G, size=18)
s.pl([(690, 414), (690, 482), (552, 482)], A2, 2, True)
s.t(400, 552, 'Both errors are systematic, so calibration can remove them', 17, GREY)
fig(slug, 'offset-error-calibration-flowchart',
    'flowchart to detect offset error with zero trim and span error with span trim',
    'Diagram by Instrumentation Blog showing the calibration steps: check the 0 psi output for offset and fix with zero trim, then check 10 psi for span error and fix with span trim.',
    'Why Correcting Both Errors is Important', s.svg())

s = S(520, 'Offset error zero point error and span error compared')
s.head('Offset, Zero Point and Span Error at a Glance', A2)
cards = [('Offset error', 'Whole output shifts', ['0 psi: 5 mV', '10 psi: 105 mV', 'same 5 mV everywhere']),
         ('Zero point error', 'Deviation at zero input', ['0 psi: 1 mV', 'should read 0 mV', 'a type of offset error']),
         ('Span error', 'Gain or slope is wrong', ['10 psi: 110 mV', '11 mV per psi', 'should be 10 mV per psi'])]
for i, (t_, d, ls) in enumerate(cards):
    x = 20 + i * 257
    s.raw(f'<rect x="{x}" y="70" width="245" height="360" rx="16" fill="{L if i != 1 else "#ffffff"}" stroke="{A}" stroke-width="2.5"/>')
    s.raw(f'<rect x="{x}" y="70" width="245" height="70" rx="16" fill="{A if i != 1 else A2}"/>')
    s.t(x + 122, 114, t_, 21, '#ffffff', 'bold')
    s.t(x + 122, 186, d, 18, A2, 'bold')
    for j, l_ in enumerate(ls): s.t(x + 122, 250 + j * 50, l_, 18 if j < 2 else 17, '#1a2b4a' if j < 2 else GREY)
s.t(400, 474, 'All three are systematic, predictable and repeatable', 18, A2, 'bold')
s.t(400, 502, 'Offset and span errors are independent of each other', 17, GREY)
fig(slug, 'offset-error-zero-point-span-infographic',
    'offset error, zero point error and span error compared with mV examples',
    'Diagram by Instrumentation Blog comparing the three errors with the article examples: a 5 mV offset, a 1 mV zero point error and a span error of 11 mV per psi.',
    'Offset Error and Zero-Point Error', s.svg())

if __name__ == '__main__': main()
