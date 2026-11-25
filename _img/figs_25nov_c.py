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

# ================= 5. Gray code =================
slug = 'gray-code-binary-conversion'
A, A2, L = '#4338ca', '#1e1b4b', '#eef2ff'
import math
s = S(580, 'Four bit Gray code absolute encoder disc with 16 positions')
s.head('4 Bit Gray Code Encoder Disc', A2)
cx, cy = 270, 310
radii = [(60, 100), (100, 140), (140, 180), (180, 220)]  # bit3 inner .. bit0 outer
for k in range(16):
    g = k ^ (k >> 1)
    a0 = math.radians(90 - k * 22.5); a1 = math.radians(90 - (k + 1) * 22.5)
    for b, (r0, r1) in zip((3, 2, 1, 0), radii):
        on = (g >> b) & 1
        p = [(cx + r1 * math.cos(a0), cy - r1 * math.sin(a0)), (cx + r1 * math.cos(a1), cy - r1 * math.sin(a1)),
             (cx + r0 * math.cos(a1), cy - r0 * math.sin(a1)), (cx + r0 * math.cos(a0), cy - r0 * math.sin(a0))]
        d = f'M{p[0][0]:.1f} {p[0][1]:.1f} A{r1} {r1} 0 0 1 {p[1][0]:.1f} {p[1][1]:.1f} L{p[2][0]:.1f} {p[2][1]:.1f} A{r0} {r0} 0 0 0 {p[3][0]:.1f} {p[3][1]:.1f} Z'
        s.raw(f'<path d="{d}" fill="{A2 if on else "#ffffff"}" stroke="#c7d2fe" stroke-width="1"/>')
    am = math.radians(90 - (k + 0.5) * 22.5)
    s.t(cx + 240 * math.cos(am), cy - 240 * math.sin(am) + 6, str(k), 17, A, 'bold')
s.raw(f'<circle cx="{cx}" cy="{cy}" r="56" fill="#f1f5f9" stroke="#94a3b8" stroke-width="2"/>'); s.t(cx, cy + 6, 'shaft', 17, GREY)
s.raw(f'<rect x="{cx-8}" y="{cy-228}" width="16" height="172" rx="4" fill="none" stroke="#dc2626" stroke-width="3"/>')
s.raw(f'<rect x="560" y="120" width="220" height="250" rx="14" fill="{L}" stroke="{A}" stroke-width="2"/>')
s.t(670, 156, 'Tracks', 19, A2, 'bold')
for i, t_ in enumerate(['inner: bit 3, MSB', 'bit 2', 'bit 1', 'outer: bit 0, LSB']): s.t(670, 194 + i * 34, t_, 17, '#1a2b4a')
s.t(670, 340, 'dark = 1, light = 0', 17, GREY)
s.raw(f'<rect x="560" y="390" width="220" height="150" rx="14" fill="#ffffff" stroke="#dc2626" stroke-width="2"/>')
s.t(670, 424, 'Red window = sensors', 17, '#dc2626', 'bold'); s.t(670, 458, 'Neighbouring sectors', 17, '#1a2b4a'); s.t(670, 484, 'differ in one track', 17, '#1a2b4a'); s.t(670, 512, 'even 15 back to 0', 17, '#1a2b4a')
fig(slug, 'gray-code-absolute-encoder-disc-diagram',
    'Gray code absolute encoder disc with four tracks and 16 positions',
    'Diagram by Instrumentation Blog drawing a 4 bit Gray code encoder disc: four concentric tracks give 16 positions, and every neighbouring sector differs in only one track.',
    'Gray Code in Absolute Encoders', s.svg())

s = S(600, 'Flowchart of Gray to binary decoding with XOR')
s.head('Gray to Binary Decoding Loop', A2)
s.box(240, 56, 320, 56, ['Start with Gray 1011'], L, A, size=18)
s.ar(400, 112, 400, 132)
s.box(240, 132, 320, 64, ['Copy MSB', 'B3 = G3 = 1'], A, A2, '#ffffff', size=18)
s.ar(400, 196, 400, 216)
s.box(240, 216, 320, 64, ['Next bit: B = previous B', 'XOR next Gray bit'], '#ffffff', A, size=17)
s.ar(400, 280, 400, 300)
s.dia(400, 350, 300, 100, ['LSB done?'], '#ffffff', A2, size=18)
s.pl([(250, 350), (180, 350), (180, 248), (238, 248)], A, 2.5); s.t(170, 340, 'No', 17, A, 'bold', 'end')
s.ar(400, 400, 400, 430); s.t(420, 422, 'Yes', 17, A2, 'bold', 'start')
s.box(240, 430, 320, 64, ['Binary 1101', 'decimal 13'], A2, A2, '#ffffff', size=19)
s.raw(f'<rect x="590" y="132" width="190" height="230" rx="12" fill="{L}" stroke="{A}" stroke-width="2"/>')
for i, t_ in enumerate(['B3 = 1', 'B2 = 1 XOR 0 = 1', 'B1 = 1 XOR 1 = 0', 'B0 = 0 XOR 1 = 1']):
    s.t(685, 176 + i * 50, t_, 17, A2 if i == 0 else '#1a2b4a', 'bold' if i == 0 else 'normal')
s.t(400, 540, 'Each step needs the binary bit just found, so decoding runs MSB first', 17, GREY)
s.t(400, 568, 'Encoding needs no chain: G = B XOR (B shifted right by 1)', 17, GREY)
fig(slug, 'gray-code-to-binary-decoding-flowchart',
    'flowchart of Gray code to binary decoding with XOR, 1011 to 1101',
    'Diagram by Instrumentation Blog showing the decoding loop from the article: copy the MSB, XOR each result with the next Gray bit, so Gray 1011 becomes binary 1101, decimal 13.',
    'Gray to Binary Decoding Method', s.svg())

s = S(560, 'Binary versus Gray code change from 7 to 8')
s.head('Step From 7 to 8: Binary vs Gray Code', A2)
def bits(x, y, v, flip, c):
    for i, ch in enumerate(v):
        f = flip[i] == '1'
        s.raw(f'<rect x="{x + i * 62}" y="{y}" width="54" height="64" rx="8" fill="{c if f else "#ffffff"}" stroke="{A2}" stroke-width="2"/>')
        s.t(x + i * 62 + 27, y + 43, ch, 26, '#ffffff' if f else A2, 'bold')
s.t(200, 90, 'Binary', 22, '#dc2626', 'bold'); s.t(600, 90, 'Gray code', 22, '#16a34a', 'bold')
s.t(60, 150, '7', 22, A2, 'bold'); bits(80, 112, '0111', '0000', '#dc2626')
s.t(60, 240, '8', 22, A2, 'bold'); bits(80, 202, '1000', '1111', '#dc2626')
s.t(200, 300, '4 bits change at once', 18, '#dc2626', 'bold')
s.t(460, 150, '7', 22, A2, 'bold'); bits(480, 112, '0100', '0000', '#16a34a')
s.t(460, 240, '8', 22, A2, 'bold'); bits(480, 202, '1100', '1000', '#16a34a')
s.t(600, 300, 'only 1 bit changes', 18, '#16a34a', 'bold')
s.ln(400, 80, 400, 310, '#e5e7eb', 2)
s.raw(f'<rect x="30" y="340" width="740" height="190" rx="14" fill="{L}" stroke="{A}" stroke-width="2"/>')
s.t(400, 376, 'Binary to Gray: Gray = Binary XOR (Binary shifted right by 1)', 18, A2, 'bold')
s.t(400, 414, '13: 1101 XOR 0110 = 1011', 20, A, 'bold')
s.t(400, 454, 'A sample taken mid change in binary can read 1111 or 0000;', 17, '#1a2b4a')
s.t(400, 482, 'in Gray code it reads either the old or the new value', 17, '#1a2b4a')
s.t(400, 512, 'n bit converter: n − 1 XOR gates, no clock', 17, GREY)
fig(slug, 'gray-code-vs-binary-transition-infographic',
    'Gray code vs binary transition from 7 to 8, one bit change instead of four',
    'Diagram by Instrumentation Blog comparing the 7 to 8 step: binary 0111 to 1000 flips four bits, Gray 0100 to 1100 flips one, plus the XOR conversion of 13 to 1011.',
    'Why Does Binary Counting Cause Errors?', s.svg())

# ================= 6. Transformer efficiency =================
slug = 'transformer-efficiency-calculation'
A, A2, L = '#059669', '#064e3b', '#ecfdf5'
def xfmr(s, x, y, c):
    s.raw(f'<rect x="{x}" y="{y}" width="110" height="130" rx="6" fill="none" stroke="#64748b" stroke-width="10"/>')
    for k in range(4):
        s.raw(f'<path d="M{x-8} {y+20+k*24} q14 12 0 24" fill="none" stroke="{c}" stroke-width="4"/>')
        s.raw(f'<path d="M{x+118} {y+20+k*24} q-14 12 0 24" fill="none" stroke="{c}" stroke-width="4"/>')
def meter(s, x, y, lab, c):
    s.raw(f'<circle cx="{x}" cy="{y}" r="22" fill="#ffffff" stroke="{c}" stroke-width="2.5"/>'); s.t(x, y + 6, lab, 18, c, 'bold')
s = S(560, 'Open circuit and short circuit tests that give transformer iron loss and copper loss')
s.head('Where the Two Loss Numbers Come From', A2)
for k, (x0, title, sup, sec, res, note) in enumerate([(20, 'Open circuit test', 'Rated voltage', 'Secondary open', 'Wattmeter = iron loss', 'constant at every load'),
                                                   (410, 'Short circuit test', '5 to 10 % voltage', 'Secondary shorted', 'Wattmeter = copper loss', 'at rated current')]):
    s.raw(f'<rect x="{x0}" y="60" width="370" height="420" rx="16" fill="{L if k == 0 else "#ffffff"}" stroke="{A}" stroke-width="2"/>')
    s.t(x0 + 185, 96, title, 21, A2, 'bold')
    xx = x0 + 180
    xfmr(s, xx, 170, '#b45309')
    s.ln(x0 + 40, 190, xx - 8, 190, '#1a2b4a', 2.5); s.ln(x0 + 40, 290, xx - 8, 290, '#1a2b4a', 2.5)
    s.raw(f'<circle cx="{x0+40}" cy="240" r="22" fill="#ffffff" stroke="#1a2b4a" stroke-width="2.5"/>'); s.t(x0 + 40, 246, '~', 22, '#1a2b4a', 'bold')
    s.ln(x0 + 40, 190, x0 + 40, 218, '#1a2b4a', 2.5); s.ln(x0 + 40, 262, x0 + 40, 290, '#1a2b4a', 2.5)
    meter(s, x0 + 110, 190, 'W', A)
    if k == 0:
        s.ln(xx + 118, 190, xx + 160, 190, '#1a2b4a', 2.5); s.ln(xx + 118, 290, xx + 160, 290, '#1a2b4a', 2.5)
        s.raw(f'<circle cx="{xx+160}" cy="190" r="5" fill="#ffffff" stroke="#1a2b4a" stroke-width="2"/><circle cx="{xx+160}" cy="290" r="5" fill="#ffffff" stroke="#1a2b4a" stroke-width="2"/>')
    else:
        s.pl([(xx + 118, 190), (xx + 160, 190), (xx + 160, 290), (xx + 118, 290)], '#dc2626', 3, False)
    s.t(x0 + 185, 350, sup + ' on primary', 18, '#1a2b4a'); s.t(x0 + 185, 380, sec, 18, '#1a2b4a')
    s.t(x0 + 185, 424, res, 19, A2, 'bold'); s.t(x0 + 185, 452, note, 17, GREY)
s.t(400, 520, 'Example certificate: iron loss 1.2 kW, full load copper loss 2.0 kW', 18, A2, 'bold')
fig(slug, 'transformer-efficiency-oc-sc-test-diagram',
    'open circuit and short circuit test diagram for transformer iron loss and copper loss',
    'Diagram by Instrumentation Blog comparing the open circuit test, which reads iron loss at rated voltage, with the short circuit test, which reads copper loss at rated current.',
    'Transformer Efficiency: Core Loss vs Copper Loss Explained', s.svg())

s = S(600, 'Flowchart for calculating transformer efficiency at any load')
s.head('Transformer Efficiency in 5 Steps', A2)
st = [(['1  Read test certificate', 'P_iron 1.2 kW, P_cu_FL 2.0 kW']), (['2  Set load fraction x', 'x = 0.5 for half load']),
      (['3  P_out = x × kVA × pf', '0.5 × 100 × 0.8 = 40 kW']), (['4  P_cu = x² × P_cu_FL', '0.25 × 2000 = 500 W']),
      (['5  η = P_out ÷ (P_out + losses)', '40,000 ÷ 41,700 = 95.92 %'])]
for i, b in enumerate(st):
    y = 58 + i * 88
    s.box(150, y, 400, 70, b, L if i % 2 == 0 else '#ffffff', A, size=18)
    if i < 4: s.ar(350, y + 70, 350, y + 88, A2)
s.box(590, 190, 190, 210, ['Best load', 'x_max = √(1.2 ÷ 2.0)', '= 0.7746', 'η_max', '96.27 %'], A, A2, '#ffffff', size=17)
s.ar(552, 300, 588, 300, A2, 2)
s.t(400, 520, 'Full load gives 96.15 %, half load 95.92 %', 18, A2, 'bold')
s.t(400, 552, 'Peak efficiency comes where copper loss equals iron loss', 17, GREY)
fig(slug, 'transformer-efficiency-calculation-steps-flowchart',
    'transformer efficiency calculation flowchart with the 100 kVA half load example',
    'Diagram by Instrumentation Blog walking the article formula through five steps for the 100 kVA unit at half load, giving 95.92 percent, with the 77.5 percent maximum efficiency point.',
    'The 3 Transformer Efficiency Formulas You Need', s.svg())

s = S(560, 'All day efficiency timeline for a 100 kVA transformer')
s.head('All Day Efficiency: 24 Hours of the 100 kVA Unit', A2)
X0, W = 60, 680
segs = [('Full load, 6 h', 6, '80 kW out', '19.2 kWh loss', A2), ('Half load, 10 h', 10, '40 kW out', '17.0 kWh loss', A), ('No load, 8 h', 8, '0 kW out', '9.6 kWh loss', '#94a3b8')]
x = X0
for n, h, o, l_, c in segs:
    w = W * h / 24
    s.raw(f'<rect x="{x:.1f}" y="90" width="{w:.1f}" height="70" fill="{c}" stroke="#ffffff" stroke-width="2"/>')
    s.t(x + w / 2, 132, n, 18, '#ffffff', 'bold')
    s.t(x + w / 2, 192, o, 18, A2, 'bold'); s.t(x + w / 2, 220, l_, 17, '#dc2626')
    x += w
s.t(X0, 80, '0 h', 17, GREY, 'normal', 'start'); s.t(X0 + W, 80, '24 h', 17, GREY, 'normal', 'end')
cards = [('880 kWh', 'output', '480 + 400 + 0'), ('45.8 kWh', 'losses', '19.2 + 17.0 + 9.6'), ('95.05 %', 'all day efficiency', '880 ÷ 925.8')]
for i, (big, lab, sub) in enumerate(cards):
    x = 30 + i * 252
    s.raw(f'<rect x="{x}" y="260" width="236" height="160" rx="14" fill="{A2 if i == 2 else L}" stroke="{A}" stroke-width="2"/>')
    c = '#ffffff' if i == 2 else A2
    s.t(x + 118, 316, big, 30, c, 'bold'); s.t(x + 118, 352, lab, 18, c, 'bold'); s.t(x + 118, 388, sub, 17, '#ffffff' if i == 2 else GREY)
s.t(400, 470, 'Iron loss runs all 24 hours, even with no load connected,', 18, '#1a2b4a')
s.t(400, 500, 'so all day efficiency is lower than the full load 96.15 %', 18, '#1a2b4a')
fig(slug, 'transformer-efficiency-all-day-infographic',
    'transformer efficiency all day example: 880 kWh output, 45.8 kWh loss, 95.05 percent',
    'Diagram by Instrumentation Blog laying out the 24 hour load cycle from the article: 6 h full, 10 h half and 8 h no load give 880 kWh out, 45.8 kWh lost and 95.05 percent.',
    'All-Day Efficiency Calculation for the Same 100 kVA Transformer', s.svg())

# ================= 7. Functional safety assessment =================
slug = 'what-is-functional-safety-assessment'
A, A2, L = '#c2410c', '#7c2d12', '#fff7ed'
s = S(560, 'Five functional safety assessment stages along the IEC 61511 safety lifecycle')
s.head('5 FSA Stages Along the Safety Lifecycle', A2)
ph = [('Hazard and', 'risk analysis'), ('Design,', 'FAT'), ('Install,', 'commission'), ('Operate,', 'maintain'), ('Modify,', 'MoC')]
for i, (a, b) in enumerate(ph):
    x = 20 + i * 154
    s.raw(f'<polygon points="{x},150 {x+136},150 {x+150},190 {x+136},230 {x},230 {x+14},190" fill="{L if i % 2 == 0 else "#ffffff"}" stroke="{A}" stroke-width="2.5"/>')
    s.t(x + 75, 184, a, 17, '#1a2b4a', 'bold'); s.t(x + 75, 208, b, 17, '#1a2b4a')
stg = [('FSA 1', 'SIL targets', 'and SRS right?'), ('FSA 2', 'design meets', 'the SRS?'), ('FSA 3', 'pre startup', 'safety review'), ('FSA 4', 'periodic, since', 'Edition 2'), ('FSA 5', 'every change,', 'all software')]
for i, st_ in enumerate(stg):
    xc = 20 + i * 154 + 75
    x = xc
    s.ln(x, 232, x, 270, A2, 2.5)
    s.raw(f'<circle cx="{x}" cy="290" r="22" fill="{A}"/>'); s.t(x, 297, str(i + 1), 19, '#ffffff', 'bold')
    for j, l_ in enumerate(st_[1:]):
        s.t(xc, 344 + j * 24, l_, 17, '#1a2b4a', 'normal')
s.t(400, 100, 'Each stage is an independent review, not led by the design or O&M team', 17, GREY)
s.raw(f'<rect x="20" y="430" width="760" height="100" rx="14" fill="{L}" stroke="{A}" stroke-width="2"/>')
s.t(400, 468, 'Goal: catch systematic errors early and confirm the SIL', 18, A2, 'bold')
s.t(400, 500, 'targets in the Safety Requirements Specification are met', 18, A2, 'bold')
fig(slug, 'functional-safety-assessment-five-stages-diagram',
    'functional safety assessment five stages on the IEC 61511 safety lifecycle',
    'Diagram by Instrumentation Blog placing the five FSA stages on the safety lifecycle: after risk analysis, at FAT, before startup, during operation and at every modification.',
    'When Should You Conduct FSA?', s.svg())

s = S(580, 'Flowchart of a functional safety assessment for a modification')
s.head('FSA Stage 5: Handling a Plant Change', A2)
s.box(250, 56, 300, 56, ['Change proposed'], L, A, size=18)
s.ar(400, 112, 400, 132)
s.box(250, 132, 300, 56, ['Safety impact analysis'], A, A2, '#ffffff', size=18)
s.ar(400, 188, 400, 208)
s.dia(400, 260, 340, 100, ['Software change,', 'even a minor one?'], '#ffffff', A, size=18)
s.ar(570, 260, 610, 260); s.t(590, 246, 'Yes', 17, A2, 'bold')
s.box(610, 222, 170, 76, ['Independent', 'assessment'], A2, A2, '#ffffff', size=18)
s.ar(400, 310, 400, 336); s.t(385, 328, 'No', 17, GREY, 'bold', 'end')
s.dia(400, 388, 340, 100, ['Could it affect', 'the SIL targets?'], '#ffffff', A, size=18)
s.ar(570, 388, 610, 388); s.t(590, 374, 'Yes', 17, A2, 'bold')
s.box(610, 350, 170, 76, ['Reassess against', 'the SRS'], A2, A2, '#ffffff', size=17)
s.ar(400, 438, 400, 464); s.t(420, 456, 'No', 17, GREY, 'bold', 'start')
s.box(250, 464, 300, 60, ['Implement and record'], '#f0fdf4', '#16a34a', size=18)
s.pl([(695, 426), (695, 494), (552, 494)], A2, 2.5, True)
s.pl([(695, 298), (695, 322), (404, 322)], A2, 2.5, True)
s.t(400, 560, 'All software changes go through FSA 5, a point often overlooked', 17, GREY)
fig(slug, 'functional-safety-assessment-modification-flowchart',
    'functional safety assessment flowchart for a plant modification under management of change',
    'Diagram by Instrumentation Blog showing FSA stage 5: every change gets a safety impact analysis, all software changes are independently assessed and SIL impacts are rechecked.',
    'What is Functional Safety Assessment (FSA)?', s.svg())

s = S(560, 'Why functional safety assessment is critical, with the FAT example')
s.head('Why FSA Matters', A2)
rs = [('Accident prevention', 'flaws caught before incidents'), ('Regulatory compliance', 'IEC 61511 requires FSAs'),
      ('Cost savings', 'cheaper to fix at FAT'), ('Reputation and trust', 'regulators, staff, public'), ('Operational reliability', 'SIS stays valid over time')]
for i, (a, b) in enumerate(rs):
    y = 66 + i * 70
    s.raw(f'<rect x="20" y="{y}" width="400" height="58" rx="10" fill="{L if i % 2 == 0 else "#ffffff"}" stroke="{A}" stroke-width="2"/>')
    num(s, 48, y + 29, i + 1, A, 16)
    s.t(76, y + 25, a, 18, A2, 'bold', 'start'); s.t(76, y + 48, b, 17, GREY, 'normal', 'start')
s.raw(f'<rect x="440" y="66" width="340" height="338" rx="14" fill="{A2}"/>')
s.t(610, 104, 'Example from the article', 19, '#ffffff', 'bold')
for i, l_ in enumerate(['New reactor at a', 'petrochemical plant', 'FSA 2 at FAT found a', 'logic solver error:', 'no shutdown under some', 'abnormal conditions', 'Fixed before startup']):
    s.t(610, 148 + i * 34, l_, 18, '#ffffff' if i < 6 else '#fed7aa', 'bold' if i == 6 else 'normal')
s.raw(f'<rect x="20" y="430" width="760" height="100" rx="14" fill="#ffffff" stroke="{A}" stroke-width="2"/>')
s.t(400, 468, 'Many accidents start from systematic failures:', 18, A2, 'bold')
s.t(400, 500, 'weak hazard analysis, poor specifications, software mistakes', 18, '#1a2b4a')
fig(slug, 'functional-safety-assessment-benefits-infographic',
    'functional safety assessment benefits and an FAT example where a logic solver error was caught',
    'Diagram by Instrumentation Blog listing five reasons FSA matters and the article example where FSA stage 2 at FAT caught a logic solver error before reactor startup.',
    'Why is FSA Critical?', s.svg())

# ================= 8. Short circuit current =================
slug = 'short-circuit-current-calculation'
A, A2, L = '#dc2626', '#7f1d1d', '#fef2f2'
B = '#1d4ed8'
s = S(560, 'Single line diagram of the 630 kVA transformer short circuit worked example')
s.head('Worked Example: Fault at the LV Panel', A2)
y = 150
s.raw(f'<rect x="40" y="{y-40}" width="110" height="80" rx="10" fill="#f1f5f9" stroke="#334155" stroke-width="2.5"/>'); s.t(95, y - 4, 'Grid', 18, '#334155', 'bold'); s.t(95, y + 20, 'strong', 17, GREY)
s.ln(150, y, 220, y, '#334155', 3)
s.raw(f'<circle cx="245" cy="{y}" r="26" fill="none" stroke="#334155" stroke-width="3"/><circle cx="280" cy="{y}" r="26" fill="none" stroke="#334155" stroke-width="3"/>')
s.t(262, y + 58, '630 kVA, 415 V', 17, '#1a2b4a', 'bold'); s.t(262, y + 80, '6 % impedance', 17, '#1a2b4a')
s.ln(306, y, 380, y, '#334155', 3)
s.raw(f'<rect x="380" y="{y-14}" width="170" height="28" rx="6" fill="#fde68a" stroke="#b45309" stroke-width="2"/>')
s.t(465, y - 24, '35 mm² Cu, 30 m', 17, '#b45309', 'bold'); s.t(465, y + 40, '0.554 Ω/km', 17, '#b45309')
s.ln(550, y, 620, y, '#334155', 3)
s.ln(620, y - 60, 620, y + 60, '#334155', 8); s.t(620, y - 72, 'LV panel', 17, '#334155', 'bold')
s.raw(f'<polygon points="660,{y-30} 640,{y+2} 656,{y+2} 636,{y+34} 676,{y-6} 660,{y-6} 680,{y-30}" fill="{A}"/>')
s.t(700, y + 6, 'Fault', 18, A, 'bold', 'start')
rows = [('Zt = 0.06 × 415² ÷ 630,000', '0.01640 Ω'), ('Zc = 0.554 × 30 ÷ 1000', '0.01662 Ω'), ('Z total', '0.03302 Ω'),
        ("I''k = 1.05 × 415 ÷ (1.732 × 0.03302)", '7.62 kA'), ('κ at X/R 5 = 1.02 + 0.98 × e^(−0.6)', '1.558'), ('ip = 1.558 × 1.414 × 7,620', '16.8 kA')]
for i, (a, b) in enumerate(rows):
    yy = 270 + i * 44
    s.raw(f'<rect x="40" y="{yy-28}" width="720" height="40" fill="{L if i % 2 == 0 else "#ffffff"}"/>')
    s.t(60, yy, a, 18, '#1a2b4a', 'normal', 'start'); s.t(740, yy, b, 19, A2 if i in (3, 5) else '#1a2b4a', 'bold', 'end')
s.t(400, 540, 'Choose a breaker of 10 kA interrupting and at least 16.8 kA peak withstand', 17, A2, 'bold')
fig(slug, 'short-circuit-current-calculation-worked-example-diagram',
    'short circuit current calculation single line diagram for a 630 kVA transformer LV panel fault',
    'Diagram by Instrumentation Blog showing the article example: a 630 kVA, 6 percent transformer and 30 m of 35 mm2 cable give 7.62 kA symmetrical and 16.8 kA peak at the panel.',
    'Worked Example: 630 kVA Transformer LV Panel', s.svg())

s = S(600, 'Flowchart of the IEC 60909 short circuit current calculation')
s.head('IEC 60909 Short Circuit Calculation Path', A2)
st = [['Add series impedances', 'source + transformer + cable'], ["I''k = c × Vn ÷ (√3 × Zk)", 'c = 1.05 LV, 1.10 HV'],
      ['κ = 1.02 + 0.98 × e^(−3R/X)', 'from the X/R ratio'], ["ip = κ × √2 × I''k", 'peak asymmetrical']]
for i, b in enumerate(st):
    yy = 58 + i * 92
    s.box(200, yy, 400, 70, b, L if i % 2 == 0 else '#ffffff', A, size=18)
    if i < 3: s.ar(400, yy + 70, 400, yy + 92, A2)
s.box(40, 430, 330, 120, ["Use I''k for", 'breaker interrupting rating,', 'fuses, relays, earth', 'conductor, CTs'], '#ffffff', B, size=17)
s.box(430, 430, 330, 120, ['Use ip for', 'breaker momentary rating,', 'busbar bracing,', 'cable supports'], A, A2, '#ffffff', size=17)
s.pl([(400, 404), (400, 414), (205, 414), (205, 428)], A2, 2.5, True); s.pl([(400, 414), (595, 414), (595, 428)], A2, 2.5, True)
s.t(400, 584, 'Add running motor contribution, about 6 × In each, near large motors', 17, GREY)
fig(slug, 'short-circuit-current-calculation-iec-60909-flowchart',
    'IEC 60909 short circuit current calculation flowchart from impedance to I k and peak ip',
    'Diagram by Instrumentation Blog tracing the IEC 60909 steps: sum the impedances, find the symmetrical current, the kappa factor and the peak, then match each value to equipment ratings.',
    'The Calculation Formulas: IEC 60909 Method', s.svg())

import math
s = S(540, 'Symmetrical and asymmetrical fault current waveform with decaying DC offset')
s.head('Asymmetrical Fault Current: AC Plus Decaying DC', A2)
X0, Y0, W, Hs = 70, 270, 690, 75
tau = 5 / (2 * math.pi)
pts_a = []; pts_s = []; pts_d = []
for i in range(401):
    c = 4 * i / 400
    ac = -math.cos(2 * math.pi * c); dc = math.exp(-c / tau)
    pts_s.append((X0 + W * c / 4, Y0 - Hs * ac)); pts_a.append((X0 + W * c / 4, Y0 - Hs * (ac + dc))); pts_d.append((X0 + W * c / 4, Y0 - Hs * dc))
s.ln(X0, Y0, X0 + W, Y0, '#1a2b4a', 2); s.ln(X0, 70, X0, 460, '#1a2b4a', 2)
s.pl(pts_s, B, 2.5, False, '7 5'); s.pl(pts_d, '#16a34a', 2.5, False, '3 4'); s.pl(pts_a, A, 3.5, False)
pk = max(pts_a, key=lambda p: -p[1])
s.raw(f'<circle cx="{pk[0]:.1f}" cy="{pk[1]:.1f}" r="7" fill="{A2}"/>')
s.t(pk[0] + 14, pk[1] + 2, 'ip, first half cycle', 17, A2, 'bold', 'start')
s.t(X0 + W, 445, 'time, 4 cycles', 17, GREY, 'normal', 'end')
s.t(X0 - 8, Y0 + 6, '0', 17, GREY, 'normal', 'end')
s.ln(90, 480, 130, 480, A, 3.5); s.t(138, 486, 'Total fault current', 17, A, 'bold', 'start')
s.ln(340, 480, 380, 480, B, 2.5, '7 5'); s.t(388, 486, "Symmetrical AC, I''k", 17, B, 'bold', 'start')
s.ln(590, 480, 630, 480, '#16a34a', 2.5, '3 4'); s.t(638, 486, 'DC offset', 17, '#16a34a', 'bold', 'start')
s.t(400, 524, 'Drawn for X/R = 5, κ about 1.56: the DC part decays through system resistance', 17, GREY)
fig(slug, 'short-circuit-current-calculation-asymmetrical-waveform-chart',
    'short circuit current calculation waveform: symmetrical AC, decaying DC offset and peak ip',
    'Diagram by Instrumentation Blog drawing a fault current with X/R of 5: the symmetrical AC part, the decaying DC offset and their sum, whose first half cycle peak is ip.',
    'Symmetrical vs Asymmetrical: What Is the Difference', s.svg())

# ================= 9. Negative pressure in pipelines =================
slug = 'negative-pressure-in-pipelines'
A, A2, L = '#0e7490', '#164e63', '#ecfeff'
R_ = '#dc2626'
s = S(560, 'Negative pressure at a pipeline high point with a vacuum breaker valve')
s.head('Where Negative Pressure Forms in a Pipeline', A2)
prof = [(60, 360), (200, 330), (360, 150), (420, 140), (560, 300), (740, 380)]
s.pl(prof, '#475569', 16, False); s.pl(prof, '#bfdbfe', 10, False)
s.raw(f'<circle cx="60" cy="360" r="26" fill="#ffffff" stroke="{A2}" stroke-width="3"/>'); s.t(60, 367, 'P', 19, A2, 'bold'); s.t(60, 410, 'Pump', 17, A2, 'bold')
s.pl([(60, 230), (300, 236), (420, 250), (740, 300)], A, 2.5, False, '8 6')
s.t(40, 212, 'Hydraulic grade line', 17, A, 'bold', 'start')
s.raw(f'<rect x="330" y="126" width="120" height="50" rx="6" fill="none" stroke="{R_}" stroke-width="2.5" stroke-dasharray="5 4"/>')
s.t(482, 172, 'pipe above the grade line:', 17, R_, 'bold', 'start'); s.t(482, 194, 'below atmospheric', 17, R_, 'bold', 'start')
s.ln(395, 140, 395, 96, '#475569', 6)
s.raw(f'<rect x="372" y="70" width="46" height="28" rx="5" fill="#16a34a"/>'); s.ar(450, 62, 405, 80, '#16a34a', 2.5)
s.t(460, 66, 'Vacuum breaker or air valve', 17, '#16a34a', 'bold', 'start'); s.t(460, 90, 'lets air in to break the vacuum', 17, '#16a34a', 'normal', 'start')
s.ar(740, 380, 770, 392, A2, 2.5); s.t(700, 420, 'draining or outflow', 17, A2, 'bold')
cx, cy = 200, 480
s.raw(f'<circle cx="{cx}" cy="{cy}" r="36" fill="#ffffff" stroke="#475569" stroke-width="6"/>')
for k in range(8):
    a = math.radians(k * 45)
    s.ar(cx + 86 * math.cos(a), cy + 70 * math.sin(a), cx + 46 * math.cos(a), cy + 42 * math.sin(a), R_, 2.5)
s.t(cx, cy + 6, 'low P', 17, R_, 'bold')
s.t(300, 470, 'Outside pressure pushes inward:', 18, '#1a2b4a', 'bold', 'start')
s.t(300, 496, 'thin wall, plastic or ageing pipes can buckle,', 17, '#1a2b4a', 'normal', 'start')
s.t(300, 520, 'and joints can draw in air or contaminants', 17, '#1a2b4a', 'normal', 'start')
fig(slug, 'negative-pressure-in-pipelines-high-point-diagram',
    'negative pressure in pipelines at a high point above the hydraulic grade line with vacuum breaker',
    'Diagram by Instrumentation Blog showing a pipeline high point above the hydraulic grade line, where pressure falls below atmospheric and an air valve admits air to protect the pipe.',
    'What negative pressure actually means', s.svg())

s = S(600, 'Flowchart for finding the cause of negative pressure and the matching fix')
s.head('Vacuum Found? Match the Cause to the Fix', A2)
cases = [(['At pump suction?'], ['Clean strainer, open valve,', 'check pump not oversized']),
         (['At a high point', 'while draining?'], ['Service or fit air valve', 'at the high point']),
         (['After a pump trip or', 'fast valve closure?'], ['Slow starts and stops,', 'control transients']),
         (['Hot liquid cooling', 'in an isolated line?'], ['Add vacuum relief or', 'a makeup connection']),
         (['At a fan inlet', 'in a duct?'], ['Clear louvers and filters,', 'match fan to intake'])]
for i, (q, f_) in enumerate(cases):
    cy = 110 + i * 100
    s.dia(240, cy, 330, 84, q, '#ffffff', A, size=17)
    s.ar(405, cy, 450, cy); s.t(427, cy - 12, 'Yes', 17, A2, 'bold')
    s.box(450, cy - 36, 330, 72, f_, L if i % 2 == 0 else '#ffffff', A, size=17)
    if i < 4: s.ar(240, cy + 42, 240, cy + 58); s.t(258, cy + 54, 'No', 17, GREY, 'bold', 'start')
s.t(400, 586, 'Buried and subsea lines carry extra outside load, so check them first', 17, GREY)
fig(slug, 'negative-pressure-in-pipelines-cause-fix-flowchart',
    'flowchart matching negative pressure causes in pipelines to fixes like air valves and slow closure',
    'Diagram by Instrumentation Blog matching each vacuum cause in the article, from pump suction and draining to transients, cooling and fan inlets, with the prevention step.',
    'Prevention strategies', s.svg())

s = S(540, 'Core principle of negative pressure: outflow exceeds inflow and the pipe cannot breathe')
s.head('The One Line to Remember', A2)
s.raw(f'<rect x="200" y="90" width="400" height="120" rx="60" fill="{L}" stroke="#475569" stroke-width="6"/>')
s.t(400, 156, 'pressure falls', 20, R_, 'bold')
s.ar(90, 150, 196, 150, A, 4); s.t(120, 130, 'in', 18, A, 'bold')
s.ar(604, 135, 730, 135, R_, 4); s.ar(604, 168, 730, 168, R_, 4); s.t(670, 116, 'out', 18, R_, 'bold')
s.t(400, 250, 'More fluid leaves than enters, and the system cannot breathe', 19, A2, 'bold')
cols = [('Liquid lines', ['Pump suction', 'Column separation', 'Draining', 'Thermal contraction']),
        ('Gas lines', ['Fan suction', 'Gas cooling in', 'a closed system']),
        ('All systems', ['High points', 'Blockages', 'Abrupt size changes'])]
for i, (t_, ls) in enumerate(cols):
    x = 30 + i * 252
    s.raw(f'<rect x="{x}" y="286" width="236" height="220" rx="14" fill="{"#ffffff" if i != 1 else L}" stroke="{A}" stroke-width="2"/>')
    s.raw(f'<rect x="{x}" y="286" width="236" height="48" rx="14" fill="{A if i != 1 else A2}"/>')
    s.t(x + 118, 318, t_, 19, '#ffffff', 'bold')
    for j, l_ in enumerate(ls): s.t(x + 118, 370 + j * 34, l_, 17, '#1a2b4a')
fig(slug, 'negative-pressure-in-pipelines-core-principle-infographic',
    'negative pressure in pipelines causes for liquid, gas and all systems with the core principle',
    'Diagram by Instrumentation Blog showing the article core principle, more fluid leaving than entering, with the causes listed for liquid lines, gas lines and all pipeline systems.',
    'The core principle (the “one line” you should remember)', s.svg())

if __name__ == '__main__': main()
