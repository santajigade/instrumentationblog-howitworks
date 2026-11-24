import sys; sys.path.insert(0, '/home/claude/instrumentationblog-howitworks/_img'); from figs_24nov_common import *

GREY = '#4b5563'

# ================= 1. Electrical regulations and standards =================
slug = 'electrical-regulations-and-standards'
A, A2, L = '#b45309', '#78350f', '#fff7ed'
s = S(560, 'Major organizations that develop electrical standards and their areas')
s.head('Who Writes Electrical Standards?', A2)
s.raw(f'<circle cx="400" cy="300" r="92" fill="{A}" stroke="{A2}" stroke-width="3"/>')
s.t(400, 290, 'Electrical', 21, '#ffffff', 'bold'); s.t(400, 318, 'installations', 21, '#ffffff', 'bold')
orgs = [(140, 110, 'IEC', ['Global equipment and', 'installation standards']),
        (660, 110, 'IEEE', ['Calculations, grounding,', 'power quality']),
        (140, 300, 'NFPA', ['NFPA 70, the National', 'Electrical Code']),
        (660, 300, 'ISO', ['Quality, environment,', 'safety, energy']),
        (140, 490, 'BIS', ['Indian Standards,', 'aligned with IEC']),
        (660, 490, 'UL', ['Product safety and', 'certification'])]
for x, y, n, ls in orgs:
    s.ln(400 + (x - 400) * 0.36, 300 + (y - 300) * 0.48, x + (120 if x < 400 else -120), y, '#d6a77a', 2.5)
    s.raw(f'<rect x="{x-125}" y="{y-58}" width="250" height="116" rx="14" fill="{L}" stroke="{A}" stroke-width="2.5"/>')
    s.t(x, y - 22, n, 24, A2, 'bold')
    s.t(x, y + 10, ls[0], 17, '#1a2b4a'); s.t(x, y + 34, ls[1], 17, '#1a2b4a')
fig(slug, 'electrical-regulations-and-standards-organizations-diagram',
    'electrical regulations and standards organizations IEC, IEEE, NFPA, ISO, BIS and UL',
    'Diagram by Instrumentation Blog showing the six main bodies behind electrical standards: IEC, IEEE, NFPA, ISO, BIS and UL, with the area each one covers.',
    'Major Organizations That Develop Electrical Standards', s.svg())

s = S(540, 'Flowchart showing when an electrical standard becomes mandatory through a regulation')
s.head('When Does a Standard Become Mandatory?', A2)
s.box(200, 62, 400, 56, ['Standards body publishes', 'IEC, IEEE, NFPA, ISO or BIS'], L, A, size=18)
s.ar(400, 118, 400, 140)
s.box(200, 140, 400, 56, ['Accepted engineering practice', 'for design, testing, installation'], L, A, size=18)
s.ar(400, 196, 400, 216)
s.dia(400, 270, 340, 104, ['Referenced by', 'a regulation?'], '#ffffff', A)
s.ar(230, 270, 175, 270); s.t(205, 258, 'No', 18, A2, 'bold')
s.box(20, 236, 155, 70, ['Voluntary', 'good practice'], '#ffffff', A, size=18)
s.ar(570, 270, 625, 270); s.t(597, 258, 'Yes', 18, A2, 'bold')
s.box(625, 236, 155, 70, ['Mandatory', 'by law'], A, A2, '#ffffff', size=19)
s.ar(702, 306, 702, 350)
s.box(500, 350, 280, 70, ['Inspections and approvals', 'check compliance'], L, A, size=18)
s.ar(640, 420, 640, 445)
s.box(500, 445, 280, 60, ['Violations: penalties'], '#fef2f2', '#dc2626', size=18)
s.box(20, 350, 440, 155, ['Regulation vs standard', 'Regulation: legal duty, government', 'Standard: technical method, expert body', 'Many national rules are based', 'on IEC standards'], '#ffffff', A2, size=18)
fig(slug, 'electrical-regulations-and-standards-compliance-flowchart',
    'flowchart showing when an electrical standard becomes mandatory through a regulation',
    'Diagram by Instrumentation Blog showing how a published standard stays voluntary practice until a regulation references it, then becomes mandatory and is checked by inspections.',
    'Electrical Regulations and Electrical Standards', s.svg())

s = S(560, 'Key electrical standards every engineer should know with their purpose')
s.head('10 Standards Every Engineer Should Know', A2)
rows = [('IEC 60364', 'LV installations'), ('IEC 60204', 'Equipment of machines'),
        ('IEC 61439', 'Switchgear assemblies'), ('IEC 60529', 'Enclosure IP ratings'),
        ('IEEE 80', 'Substation grounding'), ('IEEE 1584', 'Arc flash calculations'),
        ('IEEE 519', 'Harmonic distortion'), ('NFPA 70', 'US wiring code'),
        ('IS 3043', 'Earthing, India'), ('IS 732', 'Building wiring, India')]
for i, (k, v) in enumerate(rows):
    col, row = i % 2, i // 2
    x = 25 + col * 385; y = 62 + row * 92
    s.raw(f'<rect x="{x}" y="{y}" width="365" height="78" rx="12" fill="{L if (row + col) % 2 == 0 else "#ffffff"}" stroke="{A}" stroke-width="2"/>')
    s.raw(f'<rect x="{x}" y="{y}" width="130" height="78" rx="12" fill="{A}"/>')
    s.t(x + 65, y + 46, k, 19, '#ffffff', 'bold')
    s.t(x + 140, y + 46, v, 18, '#1a2b4a', 'normal', 'start')
s.t(400, 540, 'IEC and IEEE are global, NFPA 70 is the US code, IS standards come from BIS', 17, GREY)
fig(slug, 'electrical-regulations-and-standards-key-codes-infographic',
    'key electrical standards IEC 60364, IEEE 1584, NFPA 70 and IS 3043 with purpose',
    'Diagram by Instrumentation Blog listing ten standards engineers meet most often, from IEC 60364 and IEEE 80 to NFPA 70, IS 3043 and IS 732, with the purpose of each.',
    'Most Important Electrical Standards Every Engineer Should Know', s.svg())

# ================= 2. Industrial automation sensors =================
slug = 'industrial-automation-sensors'
A, A2, L = '#0d9488', '#115e59', '#f0fdfa'
s = S(500, 'Block diagram of industrial automation sensors sending signals to PLC DCS and SCADA')
s.head('Where Sensors Sit in an Automation System', A2)
s.box(25, 90, 170, 300, ['Process', 'or machine', '', 'position', 'presence', 'pressure', 'temperature', 'level, flow', 'speed'], L, A, size=18)
s.ar(197, 240, 245, 240, A, 3); s.t(221, 225, '', 17)
s.box(250, 160, 160, 160, ['Sensor', 'detects the', 'physical', 'change'], '#ffffff', A, size=18)
s.ar(412, 240, 462, 240, A, 3)
s.t(437, 210, 'signal', 17, A2, 'bold')
s.box(465, 150, 150, 180, ['Controller', 'PLC', 'DCS', 'SCADA'], A, A2, '#ffffff', size=19)
s.ar(617, 240, 650, 240, A, 3)
s.box(652, 160, 125, 160, ['Output', 'motor,', 'valve,', 'alarm'], L, A, size=18)
s.pl([(714, 322), (714, 430), (110, 430), (110, 394)], A2, 2.5, True, '7 5')
s.t(412, 460, 'The output acts on the process and the sensor sees the change', 18, '#1a2b4a')
s.t(412, 76, 'Sensors are the eyes and ears of automation', 18, GREY)
fig(slug, 'industrial-automation-sensors-control-system-block-diagram',
    'block diagram of industrial sensors sending signals to PLC, DCS and SCADA control',
    'Diagram by Instrumentation Blog showing how a sensor turns a physical change into an electrical signal for a PLC, DCS or SCADA system that drives the output.',
    'What Are Industrial Automation Sensors?', s.svg())

s = S(600, 'Flowchart to choose an industrial automation sensor by what you need to measure')
s.head('Which Sensor Do You Need?', A2)
s.box(270, 56, 260, 46, ['What must be sensed?'], L, A, size=19)
s.ar(400, 102, 400, 118)
s.dia(400, 160, 290, 84, ['Is an object', 'present?'], '#ffffff', A, size=18)
s.ar(255, 160, 205, 160); s.t(232, 148, 'Yes', 17, A2, 'bold')
s.dia(120, 160, 170, 84, ['Short', 'range?'], '#ffffff', A, size=18)
s.pl([(35, 160), (14, 160), (14, 372), (28, 372)], A2, 2, True); s.t(22, 150, 'No', 17, A2, 'bold', 'start')
s.box(30, 330, 180, 84, ['Photoelectric', 'longer range,', 'metal or not'], A2, A2, '#ffffff', size=17)
s.ar(120, 202, 120, 236); s.t(140, 224, 'Yes', 17, A2, 'bold', 'start')
s.box(30, 236, 180, 84, ['Proximity', 'inductive or', 'capacitive'], A, A2, '#ffffff', size=17)
s.ar(400, 202, 400, 236); s.t(420, 224, 'No', 17, A2, 'bold', 'start')
s.dia(400, 290, 290, 104, ['Is a shaft', 'rotating?'], '#ffffff', A, size=18)
s.ar(545, 290, 590, 290); s.t(567, 278, 'Yes', 17, A2, 'bold')
s.box(592, 255, 185, 70, ['Encoder', 'position, speed'], A, A2, '#ffffff', size=18)
s.ar(400, 342, 400, 372); s.t(420, 362, 'No', 17, A2, 'bold', 'start')
s.box(250, 372, 300, 46, ['Process variable', ], L, A, size=19)
for i, (n, ty) in enumerate([('Pressure', 'gauge or DP'), ('Temperature', 'RTD, thermocouple'), ('Level', 'float, ultrasonic'), ('Flow', 'magnetic, turbine')]):
    x = 20 + i * 192
    s.ar(400, 418, x + 90, 470, A2, 2)
    s.box(x, 470, 180, 70, [n, ty], '#ffffff', A, size=17)
s.t(400, 575, 'Every sensor converts the change into an electrical signal for the controller', 17, GREY)
fig(slug, 'industrial-automation-sensors-selection-flowchart',
    'flowchart to choose proximity, photoelectric, encoder, pressure, temperature, level or flow sensor',
    'Diagram by Instrumentation Blog showing how to pick an industrial sensor by what must be sensed: object presence, shaft rotation or a process variable.',
    'Why Are Sensors Important in Industrial Automation?', s.svg())

s = S(560, 'Seven industrial automation sensors with common types and typical applications')
s.head('7 Industrial Automation Sensors at a Glance', A2)
cards = [('Proximity', 'Inductive, capacitive', 'Conveyor object detection'),
         ('Photoelectric', 'Through beam, diffuse', 'Packaging, label detection'),
         ('Pressure', 'Gauge, absolute, DP', 'Hydraulics, pump protection'),
         ('Temperature', 'RTD, thermocouple', 'Boilers, heat exchangers'),
         ('Level', 'Float, ultrasonic', 'Tanks, vessels, silos'),
         ('Flow', 'Magnetic, turbine', 'Water and chemical lines'),
         ('Encoder', 'Incremental, absolute', 'Robots, CNC, servo motors')]
for i, (n, ty, ap) in enumerate(cards):
    if i < 6: x = 25 + (i % 2) * 385; y = 60 + (i // 2) * 120
    else: x = 217; y = 420
    s.raw(f'<rect x="{x}" y="{y}" width="365" height="108" rx="14" fill="{L if i % 3 != 1 else "#ffffff"}" stroke="{A}" stroke-width="2.5"/>')
    num(s, x + 32, y + 34, i + 1, A, 18)
    s.t(x + 62, y + 41, n, 21, A2, 'bold', 'start')
    s.t(x + 22, y + 72, ty, 17, '#1a2b4a', 'normal', 'start')
    s.t(x + 22, y + 96, ap, 17, GREY, 'normal', 'start')
fig(slug, 'industrial-automation-sensors-types-and-applications-infographic',
    'industrial automation sensors types and applications for proximity, pressure, level and encoder',
    'Diagram by Instrumentation Blog summarising the seven industrial automation sensors with their common types and a typical application for each one.',
    '7 Industrial Automation Sensors and Their Applications', s.svg())

# ================= 3. Allen Bradley PLC types =================
slug = 'types-of-allen-bradley-plcs'
A, A2, L = '#be123c', '#881337', '#fff1f2'
s = S(540, 'ControlLogix PLC chassis building blocks with redundancy chassis and network')
s.head('ControlLogix System Building Blocks', A2)
def chassis(x, y, lab):
    s.raw(f'<rect x="{x}" y="{y}" width="330" height="200" rx="8" fill="#f3f4f6" stroke="#1a2b4a" stroke-width="2.5"/>')
    s.ln(x + 10, y + 185, x + 320, y + 185, '#9ca3af', 4)
    mods = [('PS', '#fde68a'), ('CPU', A), ('DI', L), ('AI', L), ('ENET', '#e0f2fe')]
    ws = [70, 60, 55, 55, 70]; xx = x + 10
    for (m, c), w in zip(mods, ws):
        s.raw(f'<rect x="{xx}" y="{y+12}" width="{w-6}" height="166" rx="4" fill="{c}" stroke="#1a2b4a" stroke-width="2"/>')
        s.raw(f'<text x="{xx+(w-6)/2}" y="{y+100}" font-size="18" fill="{"#ffffff" if c == A else "#1a2b4a"}" font-weight="bold" text-anchor="middle" transform="rotate(-90 {xx+(w-6)/2} {y+100})">{m}</text>')
        xx += w
    s.t(x + 165, y + 225, lab, 18, A2, 'bold')
chassis(40, 70, 'Primary chassis')
chassis(430, 70, 'Redundant chassis')
s.ar(370, 160, 428, 160, A, 3); s.ar(428, 190, 372, 190, A, 3)
s.t(400, 140, 'sync', 17, A2, 'bold')
s.ln(40, 420, 760, 420, '#0369a1', 4); s.t(400, 410, 'EtherNet/IP network', 18, '#0369a1', 'bold')
s.ln(335, 270, 335, 420, '#0369a1', 2.5); s.ln(725, 270, 725, 420, '#0369a1', 2.5)
for x, lab in [(60, 'HMI'), (250, 'Drives'), (440, 'Remote I/O'), (630, 'Engineering PC')]:
    s.ln(x + 60, 420, x + 60, 450, '#0369a1', 2.5)
    s.box(x, 450, 140 if lab != 'Engineering PC' else 160, 50, [lab], '#ffffff', '#0369a1', size=17)
s.t(400, 528, 'PS power supply, CPU controller, DI and AI I/O cards, ENET communication', 17, GREY)
fig(slug, 'allen-bradley-plc-controllogix-building-blocks-diagram',
    'Allen Bradley PLC ControlLogix chassis with power supply, controller, I/O and redundancy',
    'Diagram by Instrumentation Blog showing ControlLogix building blocks: chassis, power supply, controller, I/O and communication modules, a redundant chassis and the EtherNet/IP network.',
    'ControlLogix PLC System Building Blocks', s.svg())

s = S(560, 'Flowchart to choose the right Allen Bradley PLC family')
s.head('How to Choose the Right Allen Bradley PLC', A2)
s.box(250, 56, 300, 50, ['Define the application'], L, A, size=19)
s.ar(400, 106, 400, 124)
s.dia(400, 180, 340, 110, ['Large plant, distributed', 'or redundancy needed?'], '#ffffff', A, size=17)
s.ar(570, 180, 610, 180); s.t(590, 168, 'Yes', 17, A2, 'bold')
s.box(612, 140, 170, 80, ['ControlLogix', 'rack, redundant'], A2, A2, '#ffffff', size=17)
s.ar(400, 235, 400, 262); s.t(420, 254, 'No', 17, A2, 'bold', 'start')
s.dia(400, 320, 340, 110, ['New or growing machine', 'or production line?'], '#ffffff', A, size=17)
s.ar(570, 320, 610, 320); s.t(590, 308, 'Yes', 17, A2, 'bold')
s.box(612, 280, 170, 80, ['CompactLogix', 'scalable'], A, A, '#ffffff', size=17)
s.ar(400, 375, 400, 402); s.t(420, 394, 'No', 17, A2, 'bold', 'start')
s.box(220, 402, 360, 70, ['Small standalone machine', 'or existing legacy panel'], L, A, size=18)
s.ar(400, 472, 400, 490)
s.box(290, 490, 220, 56, ['MicroLogix', 'maintain legacy'], '#ffffff', A2, size=17)
s.box(20, 140, 200, 220, ['Also check', 'I/O count', 'networking', 'motion, safety', 'expansion', 'lifecycle'], '#ffffff', A2, size=18)
fig(slug, 'allen-bradley-plc-family-selection-flowchart',
    'flowchart to choose MicroLogix, CompactLogix or ControlLogix Allen Bradley PLC',
    'Diagram by Instrumentation Blog showing how to size an Allen Bradley PLC: ControlLogix for large redundant plants, CompactLogix for growing machines and MicroLogix for legacy panels.',
    'How to choose the right Allen-Bradley PLC', s.svg())

s = S(560, 'Comparison of MicroLogix CompactLogix and ControlLogix PLC families')
s.head('MicroLogix vs CompactLogix vs ControlLogix', A2)
cols = [('MicroLogix', '#fecdd3', '#1a2b4a', ['Brick, fixed I/O', 'RSLogix 500', 'File based', 'No redundancy', 'Legacy phase']),
        ('CompactLogix', A, '#ffffff', ['Modular, expandable', 'Studio 5000', 'Tag based', 'Not typical', 'New projects']),
        ('ControlLogix', A2, '#ffffff', ['Full rack system', 'Studio 5000', 'Tag based', 'Dedicated options', 'Large systems'])]
rowlab = ['Design', 'Software', 'Programming', 'Redundancy', 'Lifecycle']
for j, lab in enumerate(rowlab):
    y = 150 + j * 74
    s.raw(f'<rect x="20" y="{y-30}" width="760" height="64" fill="{L if j % 2 == 0 else "#ffffff"}"/>')
    s.t(30, y + 8, lab, 18, A2, 'bold', 'start')
for i, (n, c, tc, vals) in enumerate(cols):
    x = 165 + i * 205
    s.raw(f'<rect x="{x}" y="62" width="195" height="50" rx="10" fill="{c}" stroke="{A2}" stroke-width="2"/>')
    s.t(x + 97, 94, n, 20, tc, 'bold')
    for j, v in enumerate(vals): s.t(x + 97, 158 + j * 74, v, 18, '#1a2b4a')
s.ar(170, 525, 770, 525, A, 3)
s.t(470, 512, 'Growing I/O count, networking and availability', 17, GREY)
fig(slug, 'allen-bradley-plc-families-comparison-infographic',
    'Allen Bradley PLC types comparison MicroLogix vs CompactLogix vs ControlLogix',
    'Diagram by Instrumentation Blog comparing the three Allen Bradley PLC families on design, software, programming style, redundancy and lifecycle stage.',
    'Key differences between MicroLogix, CompactLogix, and ControlLogix', s.svg())

# ================= 4. Voting architectures =================
slug = 'voting-architectures-safety-systems'
A, A2, L = '#4f46e5', '#312e81', '#eef2ff'
s = S(560, 'Block diagrams of 1oo1 1oo2 2oo2 and 2oo3 voting architectures')
s.head('The Four Voting Architectures', A2)
arch = [('1oo1', 1, 'Single channel trips', 'HFT 0'), ('1oo2', 2, 'Either channel trips', 'HFT 1'),
        ('2oo2', 2, 'Both must agree', 'HFT 0'), ('2oo3', 3, 'Any two of three', 'HFT 1')]
for i, (n, ch, rule, hft) in enumerate(arch):
    x = 20 + (i % 2) * 390; y = 60 + (i // 2) * 245
    s.raw(f'<rect x="{x}" y="{y}" width="370" height="230" rx="14" fill="{L if i in (0, 3) else "#ffffff"}" stroke="{A}" stroke-width="2.5"/>')
    s.t(x + 20, y + 32, n, 22, A2, 'bold', 'start'); s.t(x + 350, y + 32, hft, 18, A, 'bold', 'end')
    cy = y + 125
    ys = [cy] if ch == 1 else ([cy - 30, cy + 30] if ch == 2 else [cy - 50, cy, cy + 50])
    for k, yy in enumerate(ys):
        s.box(x + 20, yy - 19, 100, 38, [f'Sensor {chr(65 + k)}'], '#ffffff', A, size=17)
        s.ar(x + 121, yy, x + 176, cy, A2, 2)
    s.box(x + 178, cy - 32, 90, 64, ['Voter', n], A, A2, '#ffffff', size=17)
    s.ar(x + 270, cy, x + 300, cy, A2, 2.5)
    s.box(x + 300, cy - 25, 58, 50, ['Trip'], '#fef2f2', '#dc2626', size=17)
    s.t(x + 185, y + 212, rule, 18, '#1a2b4a', 'bold')
fig(slug, 'voting-architectures-1oo1-1oo2-2oo2-2oo3-block-diagram',
    'voting architectures block diagram of 1oo1, 1oo2, 2oo2 and 2oo3 sensors and voter',
    'Diagram by Instrumentation Blog showing the four common voting architectures, with redundant sensors feeding a MooN voter and the hardware fault tolerance of each.',
    'The Four Common Voting Architectures', s.svg())

s = S(560, 'Flowchart to select a voting architecture for a safety instrumented function')
s.head('Choosing a Voting Architecture', A2)
s.box(240, 56, 320, 50, ['Required SIL for the SIF'], L, A, size=19)
s.ar(400, 106, 400, 124)
s.dia(400, 182, 360, 112, ['High consequence', 'SIL 2 or SIL 3?'], '#ffffff', A, size=18)
s.ar(220, 182, 175, 182); s.t(197, 170, 'No', 17, A2, 'bold')
s.dia(95, 182, 160, 96, ['Trip', 'averse?'], '#ffffff', A, size=17)
s.ar(95, 230, 95, 262); s.t(110, 252, 'No', 17, A2, 'bold', 'start')
s.box(20, 262, 150, 66, ['1oo1', 'lowest cost'], '#ffffff', A, size=18)
s.pl([(15, 182), (6, 182), (6, 380), (20, 380)], A2, 2, True)
s.box(20, 350, 150, 66, ['2oo2', 'uptime first'], '#ffffff', '#dc2626', size=18)
s.t(24, 342, 'Yes', 17, A2, 'bold', 'start')
s.ar(400, 238, 400, 270); s.t(420, 260, 'Yes', 17, A2, 'bold', 'start')
s.dia(400, 330, 360, 112, ['Spurious trips', 'costly too?'], '#ffffff', A, size=18)
s.ar(580, 330, 620, 330); s.t(600, 318, 'Yes', 17, A2, 'bold')
s.box(622, 295, 160, 70, ['2oo3', 'balanced'], A2, A2, '#ffffff', size=18)
s.ar(400, 386, 400, 418); s.t(420, 408, 'No', 17, A2, 'bold', 'start')
s.box(300, 418, 200, 66, ['1oo2', 'safety first'], A, A, '#ffffff', size=18)
s.t(400, 528, 'Never use 2oo2 to claim a high SIL target', 18, '#dc2626', 'bold')
fig(slug, 'voting-architectures-selection-flowchart',
    'flowchart to choose 1oo1, 1oo2, 2oo2 or 2oo3 voting logic in a safety instrumented system',
    'Diagram by Instrumentation Blog showing how the required SIL and the cost of spurious trips lead to a 1oo1, 1oo2, 2oo2 or 2oo3 voting architecture.',
    'Comparison Table', s.svg())

s = S(520, 'Simplified PFD comparison of voting architectures for a single channel PFD of 0.01')
s.head('Simplified PFD with Single Channel PFD = 0.01', A2)
vals = [('1oo1', 'p', '0.01', ['Baseline', ''], '#ffffff'), ('1oo2', 'p²', '0.0001', ['100 times', 'safer'], L),
        ('2oo2', '2p minus p²', '0.0199', ['About 2 times', 'worse'], '#fef2f2'), ('2oo3', '3p² minus 2p³', '0.000298', ['About 34 times', 'safer'], L)]
for i, (n, f, v, note, c) in enumerate(vals):
    x = 25 + i * 190
    s.raw(f'<rect x="{x}" y="70" width="175" height="290" rx="14" fill="{c}" stroke="{A if i != 2 else "#dc2626"}" stroke-width="2.5"/>')
    s.t(x + 87, 110, n, 26, A2, 'bold')
    s.t(x + 87, 160, f, 17, '#1a2b4a')
    s.t(x + 87, 230, v, 24, '#1a2b4a', 'bold')
    s.t(x + 87, 300, note[0], 17, GREY); s.t(x + 87, 324, note[1], 17, GREY)
s.t(400, 405, 'p = probability that one channel fails dangerously on demand', 18, '#1a2b4a')
s.t(400, 440, 'Simplified: ignores common cause failure and test interval effects', 17, GREY)
s.t(400, 475, 'Lower PFD means a safer architecture', 18, A2, 'bold')
fig(slug, 'voting-architectures-pfd-comparison-infographic',
    'simplified PFD comparison of 1oo1, 1oo2, 2oo2 and 2oo3 voting architectures',
    'Diagram by Instrumentation Blog comparing simplified PFD values for 1oo1, 1oo2, 2oo2 and 2oo3 with a single channel PFD of 0.01, ignoring common cause failure.',
    'Simplified PFD Comparison Calculator', s.svg())

if __name__ == '__main__': main()
