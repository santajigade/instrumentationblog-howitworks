import json, sys, os, re
sys.path.insert(0, '/home/claude/instrumentationblog-howitworks/_img')
from svglib import S
OUT = '/home/claude/instrumentationblog-howitworks/_img/changes'
CH = {}
WARN = []
_box = S.box
def _chk_box(self, x, y, w, h, lines, fill='#eef6ff', stroke='#1a2b4a', tc='#1a2b4a', size=18, bold_first=True, r=10):
    for ln in lines:
        if len(ln) * 0.55 * size > w - 12: WARN.append(f'box overflow: {ln!r} w={w}')
    n = len(lines)
    if n * (size + 6) > h + 4: WARN.append(f'box too short: {lines} h={h}')
    _box(self, x, y, w, h, lines, fill, stroke, tc, size, bold_first, r)
S.box = _chk_box
def fig(slug, name, alt, caption, after, svg):
    CH.setdefault(slug, []).append(dict(name=name, alt=alt, caption=caption, after_h2=after, svg=svg))
def num(s, x, y, n, c, r=16):
    s.raw(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{c}"/>'); s.t(x, y + 6, str(n), 17, '#ffffff', 'bold')
def valve_v(s, x, y, c='#1a2b4a'):
    s.raw(f'<polygon points="{x-9},{y-11} {x+9},{y-11} {x},{y} " fill="#ffffff" stroke="{c}" stroke-width="2"/>')
    s.raw(f'<polygon points="{x-9},{y+11} {x+9},{y+11} {x},{y} " fill="#ffffff" stroke="{c}" stroke-width="2"/>')

# ================= 1. 2 wire and 4 wire transmitters =================
slug = '2-wire-and-4-wire-transmitters'
A, A2, L = '#2563eb', '#1e3a8a', '#eff6ff'
RED, BLK = '#dc2626', '#1a2b4a'
s = S(520, '2 wire and 4 wire transmitter wiring diagram with power supply and PLC analog input')
s.head('2 Wire vs 4 Wire Transmitter Wiring', A2)
s.raw(f'<rect x="15" y="60" width="380" height="370" rx="14" fill="{L}" stroke="{A}" stroke-width="2"/>')
s.raw(f'<rect x="405" y="60" width="380" height="370" rx="14" fill="#ffffff" stroke="{A}" stroke-width="2"/>')
s.t(205, 90, '2 wire: loop powered', 20, A2, 'bold')
s.t(595, 90, '4 wire: separate power', 20, A2, 'bold')
# 2 wire loop
s.box(35, 120, 130, 70, ['DC supply', 'loop power'], '#ffffff', BLK, size=17)
s.box(235, 120, 140, 70, ['Transmitter', 'field device'], '#ffffff', A, size=17)
s.box(130, 320, 160, 70, ['PLC analog', 'input'], '#ffffff', BLK, size=17)
s.ar(165, 140, 233, 140, RED, 3)
s.t(199, 128, '+', 20, RED, 'bold')
s.pl([(305, 190), (305, 355), (292, 355)], A, 3)
s.pl([(130, 355), (100, 355), (100, 192)], A, 3)
s.t(370, 270, '4 to 20 mA', 17, A2, 'bold', 'end')
s.t(370, 292, 'loop current', 17, A2, 'normal', 'end')
s.t(205, 412, 'Same 2 wires: power and signal', 17, BLK, 'bold')
# 4 wire
s.box(420, 120, 150, 80, ['Power supply', 'AC or DC'], '#ffffff', RED, size=17)
s.box(630, 120, 140, 80, ['Transmitter', 'field device'], '#ffffff', A, size=17)
s.ln(570, 140, 630, 140, RED, 3); s.ln(570, 180, 630, 180, BLK, 3)
s.t(600, 218, '2 power', 17, RED, 'bold'); s.t(600, 238, 'wires', 17, RED, 'bold')
s.box(610, 320, 160, 70, ['PLC analog', 'input'], '#ffffff', BLK, size=17)
s.ln(665, 200, 665, 320, A, 3); s.ln(715, 200, 715, 320, A, 3)
s.t(655, 270, '2 signal', 17, A2, 'bold', 'end'); s.t(655, 292, 'wires', 17, A2, 'bold', 'end')
s.t(595, 412, 'Power pair and signal pair kept apart', 17, BLK, 'bold')
s.t(400, 470, 'In the 2 wire loop the DC supply, transmitter and PLC input are in series,', 17, '#4b5563')
s.t(400, 496, 'while the 4 wire type has its own AC or DC power connection.', 17, '#4b5563')
fig(slug, '2-wire-and-4-wire-transmitter-wiring-diagram',
    '2 wire and 4 wire transmitter wiring diagram with DC supply and PLC analog input',
    'Diagram by Instrumentation Blog comparing a loop powered 2 wire transmitter in series with a DC supply and PLC input against a 4 wire transmitter with separate power and signal pairs.',
    'Transmitter Analog Output Loops', s.svg())

s = S(540, 'Flowchart to choose a 2 wire or 4 wire transmitter')
s.head('Choosing 2 Wire or 4 Wire Wiring', A2)
s.box(90, 55, 340, 56, ['Select transmitter wiring'], L, A, size=18)
s.ar(260, 111, 260, 146)
s.dia(260, 200, 340, 104, ['Needs high power', 'or voltage output?'], '#fef3c7', size=17)
s.ar(430, 200, 498, 200, A); s.t(462, 190, 'Yes', 17, A2, 'bold')
s.box(500, 165, 280, 70, ['4 wire transmitter', 'two power, two signal wires'], '#ffffff', A, size=17)
s.ar(260, 252, 260, 290); s.t(282, 278, 'No', 17, '#4b5563', 'bold')
s.dia(260, 345, 340, 104, ['Designed to be', 'loop powered?'], '#fef3c7', size=17)
s.ar(430, 345, 498, 345, A); s.t(462, 335, 'No', 17, A2, 'bold')
s.box(500, 310, 280, 70, ['4 wire transmitter', 'separate AC or DC supply'], '#ffffff', A, size=17)
s.ar(260, 397, 260, 428); s.t(285, 418, 'Yes', 17, '#4b5563', 'bold')
s.box(90, 430, 340, 84, ['2 wire transmitter', 'DC supply, transmitter and', 'PLC input in series'], '#dcfce7', '#15803d', size=17)
s.ar(430, 472, 498, 472, '#15803d')
s.box(500, 430, 280, 84, ['Why it is popular', 'fewer cables, low power,', 'simple installation'], '#ffffff', '#15803d', size=17)
fig(slug, '2-wire-and-4-wire-transmitter-selection-flowchart',
    'flowchart for choosing a loop powered 2 wire transmitter or a 4 wire transmitter',
    'Diagram by Instrumentation Blog showing when to use a 4 wire transmitter for high power or voltage output, and when a loop powered 2 wire transmitter can be used.',
    'Two-Wire Loop-Powered Transmitters', s.svg())

s = S(520, 'Why current signals are preferred over voltage signals on long transmitter cables')
s.head('Why Current Signals Beat Voltage on Long Cables', A2)
s.raw('<rect x="20" y="60" width="760" height="190" rx="14" fill="#fef2f2" stroke="#dc2626" stroke-width="2"/>')
s.t(40, 90, 'Voltage signal', 20, '#b91c1c', 'bold', 'start')
s.box(45, 110, 150, 70, ['Transmitter', 'sends voltage'], '#ffffff', BLK, size=17)
s.box(600, 110, 160, 70, ['PLC input', 'reads less'], '#ffffff', BLK, size=17)
zig = [(195, 145), (300, 145)]
x = 300
for i in range(8):
    zig.append((x + 12, 130 if i % 2 == 0 else 160)); x += 24
zig += [(x + 6, 145), (600, 145)]
s.pl(zig, '#b91c1c', 3, arrow=False)
s.t(400, 196, 'Long cable resistance', 17, '#b91c1c', 'bold')
s.t(400, 232, 'Voltage drop along the cable gives an inaccurate reading', 17, BLK)
s.raw(f'<rect x="20" y="265" width="760" height="235" rx="14" fill="{L}" stroke="{A}" stroke-width="2"/>')
s.t(40, 295, 'Current signal, series loop', 20, A2, 'bold', 'start')
s.raw(f'<rect x="150" y="320" width="500" height="120" fill="none" stroke="{A}" stroke-width="3"/>')
s.box(65, 345, 150, 70, ['Transmitter', 'sends mA'], '#ffffff', BLK, size=17)
s.box(585, 345, 160, 70, ['PLC input', 'reads mA'], '#ffffff', BLK, size=17)
for cx, cy in ((330, 320), (470, 320), (400, 440)):
    s.raw(f'<circle cx="{cx}" cy="{cy}" r="27" fill="#ffffff" stroke="{A2}" stroke-width="2.5"/>')
    s.t(cx, cy + 6, 'mA', 17, A2, 'bold')
s.t(400, 385, 'All meters read the same', 17, A2, 'bold')
s.t(400, 488, 'Current is the same at every point, so cable length does not change it', 17, BLK)
fig(slug, '2-wire-and-4-wire-current-vs-voltage-signal-infographic',
    'voltage signal drop on a long cable compared with a current loop that stays the same',
    'Diagram by Instrumentation Blog showing why transmitters use current signals: a voltage signal drops along cable resistance, while current in a series loop is the same at every point.',
    'Advantages of 4 Wire Transmitters', s.svg())

# ================= 2. Alarms in DCS =================
slug = '7-types-of-alarms-in-dcs'
A, A2, L = '#b91c1c', '#7f1d1d', '#fef2f2'
s = S(560, 'Sources of DCS system alarms in the controller cabinet and network')
s.head('Where DCS System Alarms Come From', A2)
s.raw('<rect x="25" y="65" width="385" height="300" rx="12" fill="#f3f4f6" stroke="#1a2b4a" stroke-width="2"/>')
s.t(217, 92, 'DCS controller cabinet', 18, '#1a2b4a', 'bold')
s.box(45, 110, 160, 56, ['Primary PSU'], '#ffffff', '#1a2b4a', size=17)
s.box(230, 110, 160, 56, ['Redundant PSU'], '#ffffff', '#1a2b4a', size=17)
s.box(45, 185, 345, 56, ['Controller (CPU)'], L, A, size=18)
s.box(45, 260, 345, 50, ['I/O modules, fuses, wiring'], '#ffffff', '#1a2b4a', size=17)
s.box(45, 322, 345, 34, ['Cooling fans, door, temperature'], '#ffffff', '#1a2b4a', size=17, r=6)
s.ln(217, 365, 217, 395, '#1a2b4a', 3)
s.ln(70, 395, 365, 395, '#1a2b4a', 3)
for xx in (85, 217, 349): s.ln(xx, 395, xx, 420, '#1a2b4a', 3)
s.box(25, 420, 120, 64, ['Operator', 'station'], '#ffffff', '#1a2b4a', size=17)
s.box(157, 420, 120, 64, ['Historian'], '#ffffff', '#1a2b4a', size=17)
s.box(289, 420, 120, 64, ['NTP or GPS', 'clock'], '#ffffff', '#1a2b4a', size=17)
s.t(217, 515, 'System network', 17, '#4b5563', 'bold')
num(s, 45, 213, 1, A); num(s, 45, 120, 2, A); num(s, 45, 285, 3, A); num(s, 25, 420, 4, A)
num(s, 157, 420, 5, A); num(s, 289, 420, 6, A); num(s, 45, 339, 7, A)
items = [('Controller or CPU fault', 'watchdog, memory, CPU load'), ('Power supply failure', 'primary or redundant, low DC'),
         ('I/O module failure', 'module, fuse or wiring fault'), ('Station offline', 'HMI server, operator station'),
         ('Historian failure', 'process data not archived'), ('Time sync fault', 'lost NTP or GPS time'),
         ('Cabinet cooling', 'high temp, fan fail, door open')]
for i, (h, d) in enumerate(items):
    y = 70 + i * 66
    num(s, 445, y + 20, i + 1, A)
    s.t(472, y + 26, h, 18, A2, 'bold', 'start'); s.t(472, y + 50, d, 17, '#1a2b4a', 'normal', 'start')
fig(slug, 'alarms-in-dcs-system-alarm-sources-diagram',
    'DCS system alarm sources: controller, power supplies, I/O modules, servers, historian and clock',
    'Diagram by Instrumentation Blog showing the seven system alarm sources inside a DCS, from controller and power supply faults to historian, time sync and cabinet cooling alarms.',
    '8) System Alarms', s.svg())

s = S(560, 'Operator response flowchart for a process alarm in a DCS')
s.head('How an Operator Responds to a DCS Alarm', A2)
steps = [['Process value crosses', 'its set alarm limit'], ['DCS raises the alarm', 'on the operator screen'],
         ['Operator checks', 'the process'], ['Corrective action', 'adjust valve or setpoint']]
y = 60
for i, ls in enumerate(steps):
    s.box(60, y, 330, 60, ls, L if i % 2 == 0 else '#ffffff', A, size=17)
    s.ar(225, y + 60, 225, y + 82 if i < 3 else y + 90, A)
    y += 84
s.dia(225, 456, 300, 104, ['Back in', 'normal range?'], '#fef3c7', size=18)
s.pl([(75, 456), (35, 456), (35, 342), (58, 342)], A, 2.5)
s.t(52, 482, 'No', 17, A2, 'bold')
s.ar(375, 456, 448, 456, '#15803d'); s.t(410, 446, 'Yes', 17, '#15803d', 'bold')
s.box(450, 420, 320, 72, ['Alarm clears', 'plant back to normal'], '#dcfce7', '#15803d', size=17)
s.box(440, 70, 335, 200, ['Example: reactor', 'Reactor temperature', 'exceeds its safe limit', 'DCS triggers a high', 'temperature alarm', 'Operator reduces heat', 'input or stops the feed'], '#ffffff', A, size=17)
s.t(400, 540, 'Good alarms warn early, before a trip or shutdown occurs', 17, '#4b5563')
fig(slug, 'alarms-in-dcs-operator-response-flowchart',
    'alarms in DCS operator response flowchart from alarm limit to corrective action',
    'Diagram by Instrumentation Blog showing how a DCS alarm works: the process value crosses a limit, the alarm appears, the operator checks the process and acts until it clears.',
    'What Are Alarms in a DCS?', s.svg())

s = S(570, 'Eight types of alarms in DCS with what each protects and an example')
s.head('8 Types of Alarms in a DCS', A2)
types = [('Process', 'value out of normal range', 'e.g. low boiler drum level'),
         ('Equipment', 'machine stress or failure', 'e.g. pump vibration'),
         ('Safety', 'risk to people and plant', 'e.g. toxic gas detected'),
         ('Quality', 'product off specification', 'e.g. pH deviation'),
         ('Maintenance', 'service or calibration due', 'e.g. filter replacement'),
         ('Communication', 'lost data link', 'e.g. remote I/O link failure'),
         ('Security', 'unauthorized access', 'e.g. USB insertion detected'),
         ('System', 'DCS hardware fault', 'e.g. power supply failure')]
cols = ['#b91c1c', '#c2410c', '#dc2626', '#7c3aed', '#0369a1', '#0f766e', '#4338ca', '#374151']
for i, (h, p, e) in enumerate(types):
    x = 25 + (i % 2) * 385; y = 60 + (i // 2) * 126
    s.raw(f'<rect x="{x}" y="{y}" width="365" height="112" rx="12" fill="{L if (i//2 + i) % 2 == 0 else "#ffffff"}" stroke="{cols[i]}" stroke-width="2.5"/>')
    num(s, x + 32, y + 34, i + 1, cols[i], 18)
    s.t(x + 62, y + 41, h + ' alarm', 20, cols[i], 'bold', 'start')
    s.t(x + 22, y + 72, p, 17, '#1a2b4a', 'normal', 'start')
    s.t(x + 22, y + 97, e, 17, '#4b5563', 'normal', 'start')
fig(slug, 'alarms-in-dcs-eight-types-infographic',
    'eight types of alarms in DCS: process, equipment, safety, quality, maintenance and more',
    'Diagram by Instrumentation Blog listing eight DCS alarm types, what each one protects and a typical example, from process and equipment alarms to security and system alarms.',
    'Types of Alarms in DCS – Introduction', s.svg())

# ================= 3. Arithmetic Logic Unit =================
slug = 'arithmetic-logic-unit-alu-architecture'
A, A2, L = '#6d28d9', '#4c1d95', '#f5f3ff'
s = S(545, 'Arithmetic logic unit block diagram with arithmetic unit, logic unit, multiplexer and flags')
s.head('Inside an Arithmetic Logic Unit', A2)
s.raw(f'<rect x="245" y="58" width="380" height="345" rx="14" fill="none" stroke="{A}" stroke-width="2" stroke-dasharray="8 5"/>')
s.t(258, 84, 'ALU core: combinational, no clock', 17, A2, 'bold', 'start')
s.box(25, 110, 150, 60, ['Input A', 'n bit operand'], '#ffffff', '#1a2b4a', size=17)
s.box(25, 320, 150, 60, ['Input B', 'n bit operand'], '#ffffff', '#1a2b4a', size=17)
s.box(270, 100, 220, 100, ['Arithmetic unit', 'full adders:', 'ADD, SUB, INC, DEC'], L, A, size=17)
s.box(270, 290, 220, 100, ['Logic unit', 'AND, OR, XOR, NOT', 'one gate per bit'], L, A, size=17)
s.ar(175, 140, 268, 140)
s.ln(212, 140, 212, 320); s.ar(212, 320, 268, 320)
s.ar(175, 350, 268, 350)
s.ln(236, 350, 236, 172); s.ar(236, 172, 268, 172)
s.raw(f'<polygon points="550,120 610,160 610,330 550,370" fill="#ede9fe" stroke="{A2}" stroke-width="2.5"/>')
s.t(580, 252, 'MUX', 18, A2, 'bold')
s.ar(490, 150, 548, 150); s.ar(490, 340, 548, 340)
s.box(445, 440, 230, 60, ['Select code', '3 to 6 bits'], '#fef3c7', '#1a2b4a', size=17)
s.ar(580, 440, 580, 355)
s.box(655, 200, 130, 70, ['Result', 'n bit'], '#ffffff', A, size=17)
s.ar(610, 235, 653, 235)
s.box(655, 310, 130, 70, ['Flags', 'C, Z, S, V'], '#ffffff', A, size=17)
s.pl([(610, 300), (633, 300), (633, 345), (653, 345)])
s.t(220, 525, 'Both halves compute in parallel and the multiplexer passes one result', 17, '#4b5563', 'normal', 'middle') if False else s.t(400, 530, 'Both halves compute in parallel and the multiplexer passes one result', 17, '#4b5563')
fig(slug, 'arithmetic-logic-unit-block-diagram',
    'arithmetic logic unit block diagram with adder, logic gates, multiplexer, select code and flags',
    'Diagram by Instrumentation Blog showing an ALU: inputs A and B feed the arithmetic and logic units in parallel, and the select code makes the multiplexer pass one result with flags.',
    'Inside the ALU: The Two Functional Halves', s.svg())

s = S(590, 'Flowchart of an instruction through the ALU and a jump if zero branch')
s.head('From Select Code to Branch Decision', A2)
steps = [['Control unit sends', 'the select code'], ['Both units compute', 'in parallel'],
         ['MUX passes the', 'selected result'], ['Flags C, Z, S, V set', 'in status register']]
y = 60
for i, ls in enumerate(steps):
    s.box(40, y, 330, 56, ls, L if i % 2 == 0 else '#ffffff', A, size=17)
    s.ar(205, y + 56, 205, y + 78 if i < 3 else y + 93, A)
    y += 80
s.dia(205, 450, 320, 110, ['Jump if zero:', 'Z flag set?'], '#fef3c7', size=18)
s.ar(365, 450, 448, 450, '#15803d'); s.t(405, 440, 'Yes', 17, '#15803d', 'bold')
s.box(450, 418, 320, 64, ['Branch is taken', 'jump to the new address'], '#dcfce7', '#15803d', size=17)
s.pl([(205, 505), (205, 545), (448, 545)], A, 2.5); s.t(225, 532, 'No', 17, A2, 'bold', 'start')
s.box(450, 515, 320, 60, ['Continue with the', 'next instruction'], '#ffffff', A, size=17)
s.box(420, 60, 360, 200, ['How SUB reuses the adder', '1. Invert operand B', '2. Set carry in to 1', '3. Add in the same', 'full adder chain', 'Result: A minus B in', 'two’s complement'], '#ffffff', A, size=17)
fig(slug, 'arithmetic-logic-unit-flag-branch-flowchart',
    'ALU instruction flowchart from select code to status flags and jump if zero branch',
    'Diagram by Instrumentation Blog showing how an ALU result and its flags drive a jump if zero branch, and how subtraction reuses the adder by inverting B with carry in 1.',
    "Status Flags: The ALU's Report Card", s.svg())

s = S(500, '4 bit ripple carry addition example 1011 plus 0110 equals 10001 with flags')
s.head('Worked Example: 1011 + 0110 in a 4 Bit Adder', A2)
s.t(400, 78, 'A = 1011 (11), B = 0110 (6), carry ripples right to left', 18, '#1a2b4a', 'bold')
stg = [('FA3', '1 + 0 + 1', 'S3 = 0'), ('FA2', '0 + 1 + 1', 'S2 = 0'), ('FA1', '1 + 1 + 0', 'S1 = 0'), ('FA0', '1 + 0 + 0', 'S0 = 1')]
carr = ['1', '1', '0']
for i, (n, ex, sm) in enumerate(stg):
    x = 110 + i * 170
    s.box(x, 110, 130, 90, [n, ex], L, A, size=18)
    s.t(x + 65, 232, sm, 18, A2, 'bold')
    if i < 3:
        s.ar(x + 170, 168, x + 132, 168, '#ea580c', 3)
        s.t(x + 150, 157, carr[i], 18, '#ea580c', 'bold')
s.ar(788, 168, 742, 168, '#ea580c', 3); s.t(768, 157, '0', 18, '#ea580c', 'bold'); s.t(765, 196, 'Cin', 17, '#ea580c', 'bold')
s.ar(110, 168, 70, 168, '#ea580c', 3); s.t(90, 157, '1', 18, '#ea580c', 'bold'); s.t(45, 196, 'Cout', 17, '#ea580c', 'bold')
s.box(80, 260, 640, 76, ['Result 0001 with carry out 1, so 1011 + 0110 = 10001', 'In decimal: 11 + 6 = 17'], '#ffffff', A, size=18)
flags = [('C = 1', 'carry out of MSB'), ('Z = 0', 'result not zero'), ('S = 0', 'MSB of result is 0'), ('V = 0', 'no signed overflow')]
for i, (f, d) in enumerate(flags):
    x = 20 + i * 192
    s.raw(f'<rect x="{x}" y="365" width="180" height="104" rx="12" fill="{L if i % 2 == 0 else "#ffffff"}" stroke="{A}" stroke-width="2"/>')
    s.t(x + 90, 403, f, 22, A2, 'bold'); s.t(x + 90, 440, d, 17, '#1a2b4a')
fig(slug, 'arithmetic-logic-unit-4-bit-ripple-carry-infographic',
    'arithmetic logic unit 4 bit ripple carry adder example 1011 plus 0110 with carry and flags',
    'Diagram by Instrumentation Blog working through 1011 plus 0110 in four chained full adders, giving 10001 or 17, with carry flag set and zero, sign and overflow flags clear.',
    'How the Adder Actually Adds', s.svg())

# ================= 4. CEMS =================
slug = 'cems-continuous-emissions-monitoring-system'
A, A2, L = '#a16207', '#713f12', '#fefce8'
s = S(560, 'Extractive CEMS components from stack probe to analyzers and DAHS')
s.head('Extractive CEMS: Components and Sample Path', A2)
s.raw('<rect x="40" y="75" width="80" height="460" fill="#e5e7eb" stroke="#1a2b4a" stroke-width="2"/>')
s.t(80, 68, 'Stack', 18, '#1a2b4a', 'bold')
s.ar(65, 520, 65, 470, '#6b7280', 3); s.ar(65, 320, 65, 270, '#6b7280', 3)
s.t(95, 300, 'flue', 17, '#4b5563', 'normal', 'middle') if False else None
s.ln(85, 150, 140, 150, '#1a2b4a', 4)
s.box(140, 110, 160, 80, ['Sample probe', 'heated, filter'], L, A, size=17)
s.pl([(300, 150), (440, 150)], '#dc2626', 4, arrow=False, dash='10 5')
s.t(370, 132, 'Heated line', 17, '#dc2626', 'bold'); s.t(370, 178, '180 °C', 17, '#dc2626', 'bold')
s.box(440, 110, 170, 80, ['Conditioning', 'chiller to 4 °C'], L, A, size=17)
s.ar(610, 150, 648, 150)
s.box(650, 115, 135, 70, ['Condensate', 'drain'], '#ffffff', '#1a2b4a', size=17)
s.box(140, 230, 160, 64, ['Calibration gas', 'zero and span'], '#ffffff', A, size=17)
s.ar(220, 230, 220, 193, A)
s.ar(525, 190, 525, 298)
s.box(400, 300, 270, 120, ['Gas analyzers', 'NDIR: SO2, CO, CO2', 'Chemiluminescence: NOx', 'Paramagnetic: O2'], '#ffffff', A, size=17)
s.ln(85, 395, 140, 395, '#1a2b4a', 4)
s.box(140, 360, 170, 70, ['Stack flow', 'monitor'], L, A, size=17)
s.ar(525, 420, 525, 458)
s.box(400, 460, 270, 70, ['DAHS', 'validate, average, report'], '#fef3c7', A2, size=17)
s.pl([(310, 395), (350, 395), (350, 495), (398, 495)])
s.ar(670, 495, 688, 495)
s.box(690, 460, 100, 70, ['Report', 'regulator'], '#ffffff', '#1a2b4a', size=17)
fig(slug, 'cems-extractive-system-components-diagram',
    'CEMS components diagram with heated probe, heated line, chiller, gas analyzers, flow monitor and DAHS',
    'Diagram by Instrumentation Blog showing an extractive CEMS: heated probe and 180 °C line, 4 °C chiller, gas analyzers, stack flow monitor and DAHS reporting to the regulator.',
    'CEMS Components: What Each Part Does', s.svg())

s = S(590, 'CEMS zero and span calibration check flowchart with data substitution')
s.head('CEMS Zero and Span Check Logic', A2)
s.box(60, 60, 300, 60, ['Zero check', 'inject nitrogen or zero air'], L, A, size=17)
s.ar(210, 120, 210, 138)
s.dia(210, 190, 300, 100, ['Within 2.5%', 'of full scale?'], '#fef3c7', size=17)
s.ar(210, 240, 210, 268); s.t(230, 260, 'Yes', 17, A2, 'bold', 'start')
s.box(60, 270, 300, 60, ['Span check', 'gas at 50 to 80% of span'], L, A, size=17)
s.ar(210, 330, 210, 348)
s.dia(210, 400, 300, 100, ['Within 5% of', 'certified value?'], '#fef3c7', size=17)
s.ar(210, 450, 210, 488); s.t(230, 475, 'Yes', 17, A2, 'bold', 'start')
s.box(60, 490, 300, 70, ['DAHS applies the', 'correction factor (CCF)'], '#dcfce7', '#15803d', size=17)
s.pl([(360, 190), (615, 190), (615, 228)], '#b91c1c'); s.t(400, 180, 'No', 17, '#b91c1c', 'bold')
s.pl([(360, 400), (615, 400), (615, 372)], '#b91c1c'); s.t(400, 390, 'No', 17, '#b91c1c', 'bold')
s.box(450, 230, 330, 140, ['Check failed', 'DAHS flags the period and', 'substitutes 90th percentile', 'of last 720 operating hours', 'then recalibrate'], '#fee2e2', '#b91c1c', size=17)
s.box(450, 460, 330, 100, ['Quarterly linearity', 'gases at 20, 50 and 80%', 'each within 5%'], '#ffffff', A, size=17)
fig(slug, 'cems-zero-span-calibration-flowchart',
    'CEMS calibration flowchart for zero check, span check, correction factor and data substitution',
    'Diagram by Instrumentation Blog showing CEMS calibration: zero within 2.5% of full scale, span within 5% of certified value, else the DAHS flags data and substitutes.',
    'CEMS Calibration: Zero, Span and Linearity Checks', s.svg())

s = S(530, 'Extractive CEMS vs in situ CEMS comparison infographic')
s.head('Extractive CEMS vs In Situ CEMS', A2)
s.box(240, 60, 265, 60, ['Extractive'], A, A, '#ffffff', size=20)
s.box(520, 60, 265, 60, ['In situ'], '#0369a1', '#0369a1', '#ffffff', size=20)
rows = [('Measured at', 'analyzer shelter', 'on the stack'), ('Basis', 'dry, convert to wet', 'wet, directly'),
        ('Sample line', 'heated line, conditioner', 'none'), ('Best for', 'SO2, NOx, CO, multi gas', 'sticky HF and HCl'),
        ('Maintenance', 'easy, in shelter', 'hard without shutdown'), ('Weak point', 'more failure points', 'harsh stack conditions')]
for i, (k, a, b) in enumerate(rows):
    y = 135 + i * 58
    fl = L if i % 2 == 0 else '#ffffff'
    s.raw(f'<rect x="15" y="{y}" width="770" height="50" rx="8" fill="{fl}" stroke="#e5e7eb" stroke-width="1.5"/>')
    s.t(30, y + 32, k, 18, A2, 'bold', 'start')
    s.t(372, y + 32, a, 17, '#1a2b4a'); s.t(652, y + 32, b, 17, '#1a2b4a')
s.t(400, 500, 'Opacity (particulate) is always monitored in situ across the stack', 17, '#4b5563', 'bold')
fig(slug, 'cems-extractive-vs-in-situ-infographic',
    'extractive vs in situ CEMS comparison of basis, sample line, best use and maintenance',
    'Diagram by Instrumentation Blog comparing extractive and in situ CEMS by where gas is measured, dry or wet basis, sample line, best pollutants, maintenance and weak points.',
    'Extractive CEMS vs In Situ CEMS', s.svg())

# ================= 5. Condensate pot =================
slug = 'condensate-pot-in-steam-applications'
A, A2, L = '#0e7490', '#164e63', '#ecfeff'
W = '#7dd3fc'
s = S(585, 'Condensate pots on HP and LP impulse lines of a DP transmitter in steam service')
s.head('Condensate Pot Installation on a DP Transmitter', A2)
s.raw('<rect x="40" y="105" width="720" height="40" fill="#fde68a" stroke="#1a2b4a" stroke-width="2"/>')
s.ar(70, 125, 200, 125, '#92400e', 3); s.t(110, 96, 'Steam line', 18, '#1a2b4a', 'bold')
s.raw('<rect x="396" y="92" width="8" height="66" fill="#1a2b4a"/>'); s.t(400, 84, 'Orifice', 17, '#1a2b4a', 'bold')
for px, lab, side in ((250, 'HP pot', 'l'), (550, 'LP pot', 'r')):
    s.ln(px, 145, px, 200, '#1a2b4a', 4)
    s.raw(f'<rect x="{px-40}" y="200" width="80" height="90" rx="8" fill="#ffffff" stroke="#1a2b4a" stroke-width="2.5"/>')
    s.raw(f'<rect x="{px-38}" y="245" width="76" height="43" rx="6" fill="{W}"/>')
    s.t(px, 232, 'steam', 17, '#92400e'); s.t(px, 274, 'water', 17, A2, 'bold')
    s.t(px - 110 if side == 'l' else px + 110, 250, lab, 18, A2, 'bold')
    s.ln(px, 290, px, 510, A, 4)
    valve_v(s, px, 490, '#1a2b4a')
s.ln(205, 245, 595, 245, '#dc2626', 2, '8 5')
s.t(400, 237, 'Same height', 17, '#dc2626', 'bold')
s.box(330, 405, 140, 74, ['DP', 'transmitter'], L, A, size=17)
s.ln(250, 442, 330, 442, A, 4); s.ln(470, 442, 550, 442, A, 4)
s.t(290, 432, 'HP', 17, A2, 'bold'); s.t(510, 432, 'LP', 17, A2, 'bold')
s.t(250, 535, 'Drain', 17, '#1a2b4a', 'bold'); s.t(550, 535, 'Drain', 17, '#1a2b4a', 'bold')
s.t(400, 335, 'Condensate fills both legs', 17, A2, 'bold')
s.t(400, 570, 'Fill both pots with clean condensate to the same level before start up', 17, '#4b5563')
fig(slug, 'condensate-pot-dp-transmitter-installation-diagram',
    'condensate pot installation diagram on HP and LP impulse lines of a steam DP transmitter',
    'Diagram by Instrumentation Blog showing two condensate pots at the same height on the HP and LP impulse lines of a steam DP transmitter, with condensate filled legs and drains.',
    'Installation Guidelines', s.svg())

s = S(545, 'Working principle of a condensate pot flowchart')
s.head('How a Condensate Pot Works', A2)
steps = [['Steam enters', 'impulse line'], ['Heat loss', 'condenses it'], ['Condensate', 'fills the pot'], ['Column reaches', 'transmitter']]
x = 25
for i, ls in enumerate(steps):
    s.box(x, 65, 170, 80, ls, L if i % 2 == 0 else '#ffffff', A, size=17)
    if i < 3: s.ar(x + 170, 105, x + 193, 105, A)
    x += 195
s.pl([(695, 145), (695, 195), (400, 195), (400, 228)], A, 2.5)
s.dia(400, 288, 340, 110, ['Both legs filled', 'equally?'], '#fef3c7', size=17)
s.ar(400, 343, 400, 388, '#15803d'); s.t(420, 372, 'Yes', 17, '#15803d', 'bold', 'start')
s.box(230, 390, 340, 72, ['Transmitter senses', 'only the true process DP'], '#dcfce7', '#15803d', size=17)
s.ar(570, 288, 603, 288, '#b91c1c'); s.t(586, 278, 'No', 17, '#b91c1c', 'bold')
s.box(605, 230, 180, 116, ['Fix it', 'fill both pots to', 'the same level,', 'check heights'], '#fee2e2', '#b91c1c', size=17)
s.box(20, 230, 200, 116, ['Without a pot', 'live steam above', '200 °C reaches', 'the diaphragm'], '#ffffff', '#1a2b4a', size=17)
s.t(400, 505, 'Equal condensate columns cancel out, so only the process DP is measured', 17, '#4b5563')
fig(slug, 'condensate-pot-working-principle-flowchart',
    'condensate pot working principle flowchart from steam condensing to equal liquid columns',
    'Diagram by Instrumentation Blog showing how a condensate pot works: steam condenses, the pot fills, the column reaches the transmitter and equal legs give the true process DP.',
    'Working Principle of Condensate Pot', s.svg())

s = S(520, 'Condensate pot temperature protection and material selection infographic')
s.head('Condensate Pot: Heat Protection and Materials', A2)
base = 440
for x, t, lab1, lab2, c in ((80, 200, 'Live steam', 'above 200 °C', '#dc2626'), (230, 85, 'Transmitter', 'about 85 °C', '#2563eb')):
    hgt = t * 1.4
    s.raw(f'<rect x="{x}" y="{base-hgt}" width="90" height="{hgt}" rx="8" fill="{c}"/>')
    s.t(x + 45, base - hgt - 12, lab2, 18, c, 'bold')
    s.t(x + 45, base + 28, lab1, 18, '#1a2b4a', 'bold')
s.ln(60, base, 340, base, '#1a2b4a', 2)
s.t(200, 500, 'The pot keeps live steam off the sensor', 17, '#4b5563')
s.t(590, 85, 'Material selection', 20, A2, 'bold')
mats = [('SS316 or SS304', 'common, corrosion resistant'), ('Carbon steel', 'high pressure service'), ('Alloy steel or Monel', 'special or corrosive service')]
for i, (h, d) in enumerate(mats):
    y = 105 + i * 120
    s.box(395, y, 385, 100, [h, d], L if i % 2 == 0 else '#ffffff', A, size=18)
s.t(590, 490, 'Choose by medium, pressure and temperature', 17, '#4b5563')
fig(slug, 'condensate-pot-temperature-and-materials-infographic',
    'steam above 200 °C vs transmitter limit about 85 °C and condensate pot materials',
    'Diagram by Instrumentation Blog comparing live steam above 200 °C with a transmitter limit of about 85 °C, and listing stainless, carbon and alloy steel or Monel pot materials.',
    'Advantages of Using Condensate Pots', s.svg())

# ================= 6. ControlLogix 5590 =================
slug = 'controllogix-5590-plc'
A, A2, L = '#15803d', '#14532d', '#f0fdf4'
s = S(560, 'ControlLogix 5590 system architecture with chassis, EtherNet/IP ring, OPC UA and MQTT')
s.head('ControlLogix 5590 System Architecture', A2)
s.raw('<rect x="40" y="75" width="330" height="305" rx="10" fill="#f3f4f6" stroke="#1a2b4a" stroke-width="2"/>')
s.t(205, 100, '1756 chassis', 18, '#1a2b4a', 'bold')
s.raw(f'<rect x="58" y="115" width="62" height="250" rx="6" fill="{A}" stroke="#1a2b4a" stroke-width="2"/>')
s.t(89, 245, '5590', 17, '#ffffff', 'bold')
s.raw('<rect x="130" y="115" width="62" height="250" rx="6" fill="#ffffff" stroke="#1a2b4a" stroke-width="2" stroke-dasharray="6 4"/>')
s.t(161, 245, 'L9SP', 17, '#1a2b4a', 'bold')
for xx in (202, 257, 312):
    s.raw(f'<rect x="{xx}" y="115" width="48" height="250" rx="6" fill="#dbeafe" stroke="#1a2b4a" stroke-width="2"/>')
    s.t(xx + 24, 245, 'I/O', 17, '#1a2b4a', 'bold')
leg = [(A, '5590 controller, single slot'), ('#ffffff', 'Safety partner for SIL 3 / PLe'), ('#dbeafe', 'Existing 1756 I/O modules')]
for i, (c, tx) in enumerate(leg):
    y = 410 + i * 40
    s.raw(f'<rect x="45" y="{y}" width="26" height="26" rx="4" fill="{c}" stroke="#1a2b4a" stroke-width="2"/>')
    s.t(82, y + 19, tx, 17, '#1a2b4a', 'normal', 'start')
s.box(440, 75, 345, 84, ['OPC UA server', 'SCADA, MES, historian', 'up to 100,000 nodes'], L, A, size=17)
s.box(440, 185, 345, 66, ['MQTT and REST', 'cloud and IoT brokers'], '#ffffff', A, size=17)
s.ar(370, 117, 438, 117, A); s.ar(370, 218, 438, 218, A)
s.raw(f'<ellipse cx="600" cy="420" rx="130" ry="78" fill="none" stroke="#0369a1" stroke-width="3.5"/>')
s.t(600, 412, 'DLR ring', 17, '#0369a1', 'bold'); s.t(600, 436, '1 Gb ports', 17, '#0369a1', 'bold')
s.pl([(370, 340), (390, 340), (390, 420), (408, 420)], '#0369a1')
for cx, cy, lab in ((470, 420, 'Remote I/O'), (600, 342, 'Drives'), (730, 420, 'Instruments'), (600, 498, 'Controllers')):
    s.box(cx - 60, cy - 20, 120, 40, [lab], '#ffffff', '#0369a1', size=17, r=8)
fig(slug, 'controllogix-5590-system-architecture-diagram',
    'ControlLogix 5590 system architecture with 1756 chassis, DLR ring, OPC UA and MQTT links',
    'Diagram by Instrumentation Blog showing a ControlLogix 5590 in a 1756 chassis with safety partner and I/O, dual gigabit DLR ring devices, OPC UA server and MQTT or REST links.',
    'ControlLogix 5590 Connectivity and IIoT Integration', s.svg())

s = S(600, 'Flowchart to choose one of the four ControlLogix 5590 operating modes')
s.head('Choosing a ControlLogix 5590 Operating Mode', A2)
s.box(230, 55, 340, 50, ['Configure the 5590 project'], L, A, size=18)
s.ar(400, 105, 400, 118)
s.dia(400, 170, 320, 100, ['Safety task', 'needed?'], '#fef3c7', size=18)
s.pl([(240, 170), (200, 170), (200, 248)]); s.t(215, 160, 'No', 17, '#4b5563', 'bold')
s.pl([(560, 170), (600, 170), (600, 248)]); s.t(585, 160, 'Yes', 17, A2, 'bold')
s.dia(200, 300, 290, 100, ['High', 'availability?'], '#fef3c7', size=18)
s.dia(600, 300, 290, 100, ['Redundancy', 'also needed?'], '#fef3c7', size=18)
for cx in (200, 600):
    s.ln(cx, 350, cx, 400)
    s.ln(cx - 95, 400, cx + 105, 400)
    s.ar(cx - 95, 400, cx - 95, 468); s.ar(cx + 105, 400, cx + 105, 468)
    s.t(cx - 85, 440, 'No', 17, '#4b5563', 'bold', 'start'); s.t(cx + 115, 440, 'Yes', 17, A2, 'bold', 'start')
outs = [('Standard', 'no safety task,', 'full performance'), ('Redundancy', 'two 5590s plus', 'RM3 module'),
        ('Safety mode', 'SIL 2 / PLd;', 'SIL 3 with L9SP'), ('Logix SIS', 'safety plus', 'redundancy, SIL 3')]
for i, ls in enumerate(outs):
    s.box(15 + i * 195 if i < 2 else 15 + i * 195, 470, 185, 92, list(ls), L if i % 2 == 0 else '#ffffff', A, size=17)
s.t(400, 588, 'Mode is set in Studio 5000 v38 or higher, then downloaded', 17, '#4b5563')
fig(slug, 'controllogix-5590-operating-mode-selection-flowchart',
    'ControlLogix 5590 operating mode flowchart: standard, redundancy, safety and Logix SIS',
    'Diagram by Instrumentation Blog showing how to pick one of the four ControlLogix 5590 modes from safety and availability needs: Standard, Redundancy, Safety or Logix SIS.',
    'Four ControlLogix 5590 Operating Modes', s.svg())

s = S(545, 'ControlLogix 5590 vs 5580 key numbers infographic')
s.head('ControlLogix 5590 vs 5580 at a Glance', A2)
cards = [('Maximum user memory', '40 MB', '80 MB'), ('EtherNet/IP nodes', '300+', '600+'), ('Motion axes', '256', '512'),
         ('Scan time', 'baseline', '2x faster'), ('OPC UA nodes', 'limited', '100,000'), ('SIL 2 safety controller', 'GuardLogix', 'built in')]
for i, (h, a, b) in enumerate(cards):
    x = 25 + (i % 2) * 385; y = 60 + (i // 2) * 152
    s.raw(f'<rect x="{x}" y="{y}" width="365" height="138" rx="14" fill="{L if (i//2 + i) % 2 == 0 else "#ffffff"}" stroke="{A}" stroke-width="2"/>')
    s.t(x + 182, y + 32, h, 19, A2, 'bold')
    s.t(x + 85, y + 66, '5580 (L8)', 17, '#6b7280'); s.t(x + 85, y + 102, a, 22, '#6b7280', 'bold')
    s.ar(x + 160, y + 92, x + 205, y + 92, A, 3)
    s.t(x + 280, y + 66, '5590 (L9)', 17, A2); s.t(x + 280, y + 102, b, 22, A, 'bold')
s.t(400, 530, 'Same 1756 chassis and I/O, USB C port and 8 GB MicroSD card included', 17, '#4b5563')
fig(slug, 'controllogix-5590-vs-5580-key-numbers-infographic',
    'ControlLogix 5590 vs 5580 memory, nodes, motion axes, scan time and safety comparison',
    'Diagram by Instrumentation Blog comparing ControlLogix 5590 with 5580: 80 MB vs 40 MB memory, 600+ vs 300+ nodes, 512 vs 256 axes, 2x faster scan and built in safety.',
    'ControlLogix 5590 vs 5580: What Changed in the L9 Generation', s.svg())

def lint():
    bad = []
    for slug, figs in CH.items():
        pg = json.load(open(f'/home/claude/instrumentationblog-howitworks/_img/pages/{slug}.json'))
        h2 = [h['text'] for h in pg['h2s']]
        if len({f['after_h2'] for f in figs}) != 3: bad.append(f'{slug}: H2 not distinct')
        for f in figs:
            if f['after_h2'] not in h2: bad.append(f"{slug}: H2 missing {f['after_h2']}")
            na = len(f['alt'].split());  nc = len(f['caption'].split())
            if not 6 <= na <= 16: bad.append(f"{f['name']}: alt words {na}")
            if not 12 <= nc <= 35: bad.append(f"{f['name']}: caption words {nc}")
            if len(f['name']) > 70: bad.append(f"{f['name']}: name long")
            for fld in ('alt', 'caption'):
                if re.search('[-–—]', f[fld]): bad.append(f"{f['name']}: dash in {fld}")
            for m in re.finditer(r'<(text|title)[^>]*>([^<]*)<', f['svg']):
                if re.search('[-–—]', m.group(2)): bad.append(f"{f['name']}: dash in svg text {m.group(2)!r}")
            for m in re.finditer(r'<text x="([\d.]+)" y="[\d.]+" font-size="([\d.]+)"[^>]*text-anchor="(\w+)">([^<]*)<', f['svg']):
                x, sz, an, tx = float(m.group(1)), float(m.group(2)), m.group(3), m.group(4)
                import html as H; wdt = len(H.unescape(tx)) * 0.55 * sz
                l = x - wdt / 2 if an == 'middle' else (x if an == 'start' else x - wdt)
                if l < 2 or l + wdt > 798: bad.append(f"{f['name']}: off canvas {tx!r}")
                if sz < 17: bad.append(f"{f['name']}: small text")
        fk = pg['focus'].lower().replace(' ', '-')
        if not any(pg['focus'].lower() in f['alt'].lower() for f in figs): bad.append(f'{slug}: no focus kw in alt')
        for f in figs:
            if not f['name'].startswith(fk): bad.append(f"{f['name']}: not starting with {fk}")
    return bad

if __name__ == '__main__':
    import cairosvg
    out = sys.argv[1] if len(sys.argv) > 1 else None
    for slug, figs in CH.items():
        json.dump({'slug': slug, 'figs': figs}, open(os.path.join(OUT, slug + '.json'), 'w'), ensure_ascii=False, indent=1)
        if out:
            for f in figs: cairosvg.svg2png(bytestring=f['svg'].encode(), write_to=os.path.join(out, f['name'] + '.png'), output_width=800)
    print('WARN', WARN); print('LINT', lint())
    print({k: [f['name'] for f in v] for k, v in CH.items()})
