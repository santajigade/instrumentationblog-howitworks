import json, sys
sys.path.insert(0, '/home/claude/imgpilot')
from svglib import S
OUT = '/home/claude/instrumentationblog-howitworks/_img/changes'
CH = {}
def fig(slug, name, alt, caption, after, svg):
    CH.setdefault(slug, []).append(dict(name=name, alt=alt, caption=caption, after_h2=after, svg=svg))

# ============ 1. Basic parts of a control valve ============
A, A2, L = '#0e7490', '#155e75', '#ecfeff'
s = S(560, 'Parts of a control valve cross section with actuator, bonnet, trim, body and positioner')
s.head('Parts of a Control Valve', A2)
# actuator dome
s.raw(f'<path d="M230 70 Q330 40 430 70 L430 120 L230 120 Z" fill="{L}" stroke="#1a2b4a" stroke-width="2.5"/>')
s.ln(240, 108, 420, 108, A, 4)  # diaphragm
s.raw('<polyline points="330,120 315,130 345,140 315,150 345,160 330,170" fill="none" stroke="#4b5563" stroke-width="3"/>')
# yoke
s.ln(270, 120, 290, 230, '#1a2b4a', 3); s.ln(390, 120, 370, 230, '#1a2b4a', 3)
# bonnet + packing
s.raw(f'<rect x="285" y="230" width="90" height="60" rx="6" fill="#e5e7eb" stroke="#1a2b4a" stroke-width="2.5"/>')
s.raw('<rect x="318" y="238" width="24" height="40" fill="#fde68a" stroke="#1a2b4a" stroke-width="1.5"/>')
# body
s.raw(f'<path d="M190 330 L250 330 Q260 290 330 290 Q400 290 410 330 L470 330 L470 440 L410 440 Q400 480 330 480 Q260 480 250 440 L190 440 Z" fill="{L}" stroke="#1a2b4a" stroke-width="2.5"/>')
# seat and plug
s.ln(285, 410, 310, 410, '#1a2b4a', 6); s.ln(350, 410, 375, 410, '#1a2b4a', 6)
s.ln(330, 120, 330, 382, A2, 6)
s.raw(f'<path d="M305 380 L355 380 L345 405 L315 405 Z" fill="{A}" stroke="#1a2b4a" stroke-width="2"/>')
# flow arrows
s.ar(120, 385, 185, 385, A, 4); s.ar(475, 385, 540, 385, A, 4); s.t(150, 365, 'Flow in', 18, A2, 'bold'); s.t(515, 365, 'Flow out', 18, A2, 'bold')
# positioner
s.box(560, 150, 170, 70, ['Positioner', 'stem feedback'], '#fff7e6', size=18)
s.ln(560, 200, 375, 200, '#4b5563', 2, '6 5')
s.ar(645, 110, 645, 148, '#1a2b4a'); s.t(690, 100, '4 to 20 mA', 18, '#1a2b4a', 'bold')
s.pl([(645, 220), (645, 260), (520, 260), (520, 95), (432, 95)], A, 2.5); s.t(585, 285, 'Air to actuator', 18, A2)
# labels left
for y, lab, x2 in [(80, 'Diaphragm actuator', 235), (150, 'Spring', 315), (200, 'Yoke', 283), (258, 'Bonnet and packing', 285), (345, 'Stem', 326), (432, 'Plug and seat', 300), (470, 'Valve body', 260)]:
    s.t(30, y + 6, lab, 18, '#1a2b4a', 'bold', 'start'); s.ln(30 + len(lab)*9.6 + 8, y, x2, y, '#9ca3af', 1.5)
s.t(400, 530, 'Body and trim touch the process fluid; actuator and positioner move the stem', 18, '#4b5563')
fig('basic-parts-of-a-control-valve', 'parts-of-a-control-valve-cross-section-diagram',
    'parts of a control valve cross section showing actuator, bonnet, plug, seat and body',
    'Diagram by Instrumentation Blog showing the main parts of a globe control valve: diaphragm actuator, spring, yoke, stem, bonnet with packing, plug, seat, body and positioner.',
    'Basic Parts of Control Valves', s.svg())

s = S(500, 'Control valve signal flow from controller to process flow')
s.head('How the Parts Work Together', A2)
steps = [['Controller', '4 to 20 mA', 'command'], ['Positioner', 'compares', 'with stem'], ['Actuator', 'air moves', 'the stem'],
         ['Trim', 'plug sets', 'flow area'], ['Process', 'flow, level', 'or pressure']]
x = 30
for i, ls in enumerate(steps):
    s.box(x, 90, 132, 110, ls, L if i % 2 == 0 else '#fff7e6', size=17)
    if i < 4: s.ar(x + 134, 145, x + 154, 145)
    x += 152
s.pl([(706, 202), (706, 300), (96, 300), (96, 204)], A, 2.5, dash='7 5')
s.box(250, 270, 300, 60, ['Transmitter feedback', 'measured value to controller'], '#ffffff', A, size=17)
s.t(400, 380, 'Closed loop: the controller compares the measured value with the setpoint', 18, '#1a2b4a')
s.t(400, 410, 'and changes the 4 to 20 mA signal until the error is zero.', 18, '#1a2b4a')
s.t(400, 455, 'Accessories such as limit switches and a solenoid valve sit on the actuator.', 18, '#4b5563')
fig('basic-parts-of-a-control-valve', 'parts-of-a-control-valve-signal-flowchart',
    'control valve signal flowchart from controller and positioner to actuator and trim',
    'Diagram by Instrumentation Blog showing how a control valve works in a loop: controller signal, positioner, actuator, trim and process with transmitter feedback.',
    'Actuator Part', s.svg())

s = S(470, 'Four methods of flow control in valves')
s.head('4 Ways a Valve Controls Flow', A2)
cards = [('Plug against orifice', ['Plug moves to or from seat', 'Globe and needle valves', 'Best for throttling']),
         ('Sliding element', ['Gate or plug slides across', 'Gate and plug valves', 'Mostly on and off']),
         ('Rotating element', ['Disc or ball turns 90°', 'Butterfly and ball valves', 'Quarter turn, compact']),
         ('Flexible material', ['Membrane pinches flow', 'Diaphragm and pinch valves', 'Slurry and corrosive fluid'])]
for i, (h, ls) in enumerate(cards):
    x = 30 + (i % 2) * 380; y = 70 + (i // 2) * 190
    s.raw(f'<rect x="{x}" y="{y}" width="360" height="170" rx="14" fill="{L if i in (0,3) else "#fff7e6"}" stroke="{A}" stroke-width="2.5"/>')
    s.raw(f'<circle cx="{x+40}" cy="{y+40}" r="22" fill="{A}"/>'); s.t(x + 40, y + 47, str(i + 1), 20, '#ffffff', 'bold')
    s.t(x + 75, y + 47, h, 21, A2, 'bold', 'start')
    for j, l in enumerate(ls): s.t(x + 30, y + 92 + j * 28, l, 18, '#1a2b4a', 'normal', 'start')
s.t(400, 455, 'Control valves mostly use methods 1 and 3 because they throttle smoothly.', 18, '#4b5563')
fig('basic-parts-of-a-control-valve', 'parts-of-a-control-valve-flow-control-methods-infographic',
    'four methods of flow control in valves with globe, gate, butterfly and diaphragm examples',
    'Diagram by Instrumentation Blog comparing the four ways valves control flow: plug against an orifice, sliding, rotating and flexible element designs with valve examples.',
    'Methods of Flow Control in Valves', s.svg())

# ============ 2. Impedance and reactance ============
A, A2, L = '#7c3aed', '#5b21b6', '#f5f3ff'
s = S(400, 'Series RLC circuit used in the worked impedance example')
s.head('Series RLC Circuit in the Worked Example', A2)
s.raw('<circle cx="120" cy="220" r="48" fill="#ffffff" stroke="#1a2b4a" stroke-width="2.5"/>')
s.raw('<path d="M90 220 Q105 190 120 220 T150 220" fill="none" stroke="#1a2b4a" stroke-width="2.5"/>')
s.t(120, 300, '230 V, 50 Hz', 18, '#1a2b4a', 'bold')
s.ln(120, 172, 120, 110); s.ln(120, 110, 230, 110)
s.raw(f'<polyline points="230,110 245,95 265,125 285,95 305,125 325,95 340,110" fill="none" stroke="{A}" stroke-width="3"/>'); s.t(285, 80, 'R = 30 Ω', 18, A2, 'bold')
s.ln(340, 110, 400, 110)
s.raw(f'<path d="M400 110 q15 -30 30 0 q15 -30 30 0 q15 -30 30 0 q15 -30 30 0" fill="none" stroke="{A}" stroke-width="3"/>'); s.t(460, 70, 'L = 0.2 H', 18, A2, 'bold')
s.ln(520, 110, 660, 110); s.ln(660, 110, 660, 190)
s.ln(630, 190, 690, 190, A, 4); s.ln(630, 210, 690, 210, A, 4); s.t(620, 205, 'C = 50 µF', 18, A2, 'bold', 'end')
s.ln(660, 210, 660, 330); s.ln(660, 330, 120, 330); s.ln(120, 330, 120, 268)
s.ar(560, 140, 620, 140, '#1a2b4a'); s.t(590, 162, 'I = 7.66 A', 18, '#1a2b4a', 'bold')
s.t(460, 150, 'XL = 62.83 Ω', 18, '#1a2b4a'); s.t(560, 260, 'XC = 63.66 Ω', 18, '#1a2b4a')
s.t(400, 375, 'XL is almost equal to XC, so the circuit is very close to resonance.', 18, '#4b5563')
fig('impedance-reactance-ac-circuits', 'impedance-and-reactance-series-rlc-circuit-diagram',
    'series RLC circuit with 30 ohm resistor, 0.2 H inductor and 50 uF capacitor on 230 V',
    'Diagram by Instrumentation Blog showing the series RLC circuit from the worked example: 30 ohm, 0.2 H and 50 uF on a 230 V, 50 Hz supply.',
    'Impedance and Reactance in AC Circuits: Key Concepts', s.svg())

s = S(560, 'Flowchart to calculate impedance and reactance step by step')
s.head('How to Calculate Impedance Step by Step', A2)
s.box(250, 60, 300, 50, ['Know R, L, C, f and V'], L, size=18)
s.ar(330, 110, 240, 130); s.ar(470, 110, 560, 130)
s.box(90, 132, 280, 56, ['XL = 2πfL'], '#ffffff', A, size=20)
s.box(430, 132, 280, 56, ['XC = 1 ÷ (2πfC)'], '#ffffff', A, size=20)
s.ar(230, 188, 360, 225); s.ar(570, 188, 440, 225)
s.box(250, 225, 300, 50, ['X = XL minus XC'], L, size=19)
s.ar(400, 275, 400, 300)
s.dia(400, 345, 280, 90, ['Sign of X?'])
s.ar(260, 345, 180, 345); s.box(20, 320, 160, 50, ['X > 0', 'inductive'], '#fff7e6', size=17)
s.ar(540, 345, 620, 345); s.box(620, 320, 160, 50, ['X < 0', 'capacitive'], '#fff7e6', size=17)
s.t(400, 412, 'X = 0 means resonance, Z = R', 18, '#4b5563')
s.ar(400, 420, 400, 440)
s.box(170, 440, 460, 50, ['Z = √(R² + X²) and φ = arctan(X ÷ R)'], L, size=19, bold_first=True)
s.ar(400, 490, 400, 505)
s.box(300, 505, 200, 44, ['I = V ÷ Z'], '#ffffff', A, size=19)
fig('impedance-reactance-ac-circuits', 'impedance-and-reactance-calculation-flowchart',
    'flowchart to calculate inductive reactance, capacitive reactance, impedance and current',
    'Diagram by Instrumentation Blog showing the steps to calculate XL, XC, net reactance, impedance, phase angle and current in a series RLC circuit.',
    'Impedance and Reactance Formulas', s.svg())

s = S(470, 'Worked example results for impedance and reactance')
s.head('Worked Example Results at 50 Hz', A2)
vals = [('XL', '62.83 Ω', '2π × 50 × 0.2'), ('XC', '63.66 Ω', '1 ÷ (2π × 50 × 0.00005)'), ('X', 'minus 0.83 Ω', 'slightly capacitive'),
        ('Z', '30.01 Ω', '√(30² + 0.83²)'), ('φ', 'minus 1.6°', 'power factor near 1'), ('I', '7.66 A', '230 ÷ 30.01')]
for i, (k, v, f) in enumerate(vals):
    x = 30 + (i % 3) * 250; y = 70 + (i // 3) * 175
    s.raw(f'<rect x="{x}" y="{y}" width="230" height="155" rx="14" fill="{L if i % 2 == 0 else "#ffffff"}" stroke="{A}" stroke-width="2.5"/>')
    s.t(x + 115, y + 42, k, 24, A2, 'bold'); s.t(x + 115, y + 88, v, 26, '#1a2b4a', 'bold'); s.t(x + 115, y + 128, f, 17, '#4b5563')
s.t(400, 440, 'R = 30 Ω, L = 0.2 H, C = 50 µF, V = 230 V, f = 50 Hz', 19, '#1a2b4a', 'bold')
fig('impedance-reactance-ac-circuits', 'impedance-and-reactance-worked-example-infographic',
    'impedance and reactance worked example results XL 62.83 ohm XC 63.66 ohm Z 30.01 ohm',
    'Diagram by Instrumentation Blog summarising the worked example: XL 62.83 ohm, XC 63.66 ohm, net reactance, impedance 30.01 ohm, phase angle and 7.66 A current.',
    'Worked Impedance and Reactance Calculation Example', s.svg())

# ============ 3. NPN and PNP ============
A, A2, L = '#ea580c', '#9a3412', '#fff7ed'
def sensor(s, x, kind):
    s.box(x, 110, 120, 170, [kind, 'sensor'], L, A, size=19)
    for i, (c, lab) in enumerate([('#92400e', 'Brown'), ('#111827', 'Black'), ('#2563eb', 'Blue')]):
        y = 150 + i * 50; s.ln(x + 120, y, x + 190, y, c, 4); s.t(x + 160, y - 8, lab, 16, c, 'bold')
s = S(520, 'NPN and PNP proximity sensor wiring with load and PLC input')
s.head('NPN and PNP Proximity Sensor Wiring', A2)
s.ln(20, 75, 780, 75, '#dc2626', 3); s.t(60, 66, '+24 V', 18, '#dc2626', 'bold')
s.ln(20, 460, 780, 460, '#2563eb', 3); s.t(50, 490, '0 V', 18, '#2563eb', 'bold')
sensor(s, 40, 'PNP')
s.pl([(230, 150), (260, 150), (260, 75)], '#92400e', 3, False); s.pl([(230, 250), (260, 250), (260, 460)], '#2563eb', 3, False)
s.pl([(230, 200), (320, 200), (320, 300)], '#111827', 3, False)
s.box(270, 300, 100, 60, ['Load'], '#ffffff', A, size=18); s.ln(320, 360, 320, 460, '#1a2b4a', 3)
s.t(210, 410, 'Output gives +24 V', 18, A2, 'bold')
sensor(s, 430, 'NPN')
s.pl([(620, 150), (650, 150), (650, 75)], '#92400e', 3, False); s.pl([(620, 250), (650, 250), (650, 460)], '#2563eb', 3, False)
s.ln(720, 75, 720, 105, '#1a2b4a', 3)
s.box(670, 105, 100, 60, ['Load'], '#ffffff', A, size=18)
s.pl([(620, 200), (720, 200), (720, 165)], '#111827', 3, False)
s.t(640, 410, 'Output switches to 0 V', 18, A2, 'bold', 'end')
s.ln(400, 90, 400, 445, '#e5e7eb', 2, '6 6')
fig('npn-and-pnp-proximity-sensors', 'npn-and-pnp-proximity-sensors-wiring-diagram',
    'NPN and PNP proximity sensor wiring diagram with brown, black and blue wires and load',
    'Diagram by Instrumentation Blog comparing PNP and NPN 3 wire proximity sensor wiring: brown to plus 24 V, blue to 0 V and the load on the black output wire.',
    'Standard Wire Colors in 3-Wire Proximity Sensors', s.svg())

s = S(540, 'Field test flowchart to identify an NPN or PNP sensor with a multimeter')
s.head('Is It NPN or PNP? Multimeter Field Test', A2)
s.box(230, 60, 340, 50, ['Power sensor with 24 V DC'], L, A, size=18); s.ar(400, 110, 400, 128)
s.box(180, 128, 440, 50, ['Meter on DC volts: black to blue (0 V)'], L, A, size=18); s.ar(400, 178, 400, 196)
s.box(230, 196, 340, 50, ['Bring a metal target near'], L, A, size=18); s.ar(400, 246, 400, 262)
s.dia(400, 312, 300, 96, ['Reading', 'changes?'], '#ffffff', A)
s.ar(250, 312, 175, 312); s.box(15, 285, 160, 54, ['0 V to 24 V'], '#ffffff', A, size=18)
s.ar(95, 340, 95, 380); s.box(25, 380, 140, 54, ['PNP'], A, A, '#ffffff', size=22)
s.ar(550, 312, 625, 312); s.box(625, 285, 160, 54, ['24 V to 0 V'], '#ffffff', A, size=18)
s.ar(705, 340, 705, 380); s.box(635, 380, 140, 54, ['NPN'], A2, A2, '#ffffff', size=22)
s.ar(400, 360, 400, 400); s.box(220, 400, 360, 70, ['No change', 'check supply, target and range'], '#fef2f2', '#dc2626', size=18)
s.t(400, 510, 'Tip: the LED on the sensor should light when the target is detected.', 18, '#4b5563')
fig('npn-and-pnp-proximity-sensors', 'npn-and-pnp-proximity-sensors-field-test-flowchart',
    'flowchart to identify NPN or PNP proximity sensor with a multimeter field test',
    'Diagram by Instrumentation Blog showing the multimeter test to identify a sensor: measure black to blue and watch whether the output rises to 24 V or falls to 0 V.',
    'How to Identify NPN or PNP Sensor in the Field', s.svg())

s = S(480, 'Selection chart to choose NPN or PNP sensor for a PLC input card')
s.head('Which Sensor Does Your PLC Card Need?', A2)
s.box(40, 70, 330, 120, ['PLC input common at 0 V', 'sinking input card'], L, A, size=19)
s.box(430, 70, 330, 120, ['PLC input common at +24 V', 'sourcing input card'], L, A, size=19)
s.ar(205, 190, 205, 230); s.ar(595, 190, 595, 230)
s.box(90, 230, 230, 80, ['Use PNP', 'sourcing sensor'], A, A, '#ffffff', size=21)
s.box(480, 230, 230, 80, ['Use NPN', 'sinking sensor'], A2, A2, '#ffffff', size=21)
s.t(205, 350, 'Common in India and Europe', 18, '#1a2b4a', 'bold'); s.t(595, 350, 'Common in Japan and parts of Asia', 18, '#1a2b4a', 'bold')
s.raw(f'<rect x="40" y="380" width="720" height="70" rx="12" fill="#fef2f2" stroke="#dc2626" stroke-width="2"/>')
s.t(400, 410, 'Wrong pairing means the input LED never lights, even when', 18, '#991b1b', 'bold')
s.t(400, 436, 'the sensor itself switches correctly.', 18, '#991b1b', 'bold')
fig('npn-and-pnp-proximity-sensors', 'npn-and-pnp-proximity-sensors-selection-infographic',
    'how to choose NPN or PNP sensor for sinking or sourcing PLC input card',
    'Diagram by Instrumentation Blog showing how to pick a sensor type: PNP for input cards with common at 0 V and NPN for cards with common at plus 24 V.',
    'How to Choose Between NPN and PNP Sensors', s.svg())

# ============ 4. PLC block diagram ============
A, A2, L = '#2563eb', '#1e3a8a', '#eff6ff'
s = S(500, 'PLC block diagram with input module, CPU, memory, output module and power supply')
s.head('PLC Block Diagram', A2)
s.box(20, 110, 150, 230, ['Field inputs', 'Push buttons', 'Limit switches', 'Sensors', 'Transmitters'], '#fff7e6', size=17)
s.box(200, 140, 130, 170, ['Input', 'module', 'DI and AI'], L, A, size=18)
s.raw(f'<rect x="360" y="100" width="190" height="250" rx="14" fill="{L}" stroke="{A}" stroke-width="3"/>'); s.t(455, 135, 'CPU', 24, A2, 'bold')
s.box(380, 155, 150, 70, ['Processor', 'runs the scan'], '#ffffff', A, size=17)
s.box(380, 245, 150, 80, ['Memory', 'program and data'], '#ffffff', A, size=17)
s.box(580, 140, 130, 170, ['Output', 'module', 'DO and AO'], L, A, size=18)
s.ar(170, 225, 198, 225); s.ar(330, 225, 358, 225); s.ar(550, 225, 578, 225); s.ar(710, 225, 735, 225)
s.t(760, 200, 'Motors', 16, '#1a2b4a', 'bold'); s.t(760, 225, 'Valves', 16, '#1a2b4a', 'bold'); s.t(760, 250, 'Lamps', 16, '#1a2b4a', 'bold')
s.box(330, 395, 250, 60, ['Power supply', '24 V DC to all modules'], '#fef9c3', size=17)
s.pl([(455, 395), (455, 352)], '#ca8a04', 2.5); s.pl([(330, 425), (265, 425), (265, 312)], '#ca8a04', 2.5); s.pl([(580, 425), (645, 425), (645, 312)], '#ca8a04', 2.5)
s.box(600, 60, 180, 60, ['Programming', 'device or HMI'], '#ffffff', A, size=17)
s.pl([(600, 90), (552, 120)], A, 2.5, True, '6 4')
fig('plc-block-diagram', 'plc-block-diagram-modules-diagram',
    'PLC block diagram showing input module, CPU, memory, output module and power supply',
    'Diagram by Instrumentation Blog showing a PLC block diagram: field inputs, input module, CPU with processor and memory, output module, field devices and power supply.',
    'Important Parts of a PLC System', s.svg())

s = S(480, 'PLC scan cycle flowchart read inputs execute program update outputs')
s.head('PLC Scan Cycle: What the CPU Repeats', A2)
pts = [(400, 120, ['1. Read inputs', 'copy input image']), (640, 250, ['2. Execute', 'program logic']),
       (400, 380, ['3. Update outputs', 'write output image']), (160, 250, ['4. Housekeeping', 'comms and diagnostics'])]
for x, y, ls in pts: s.box(x - 115, y - 42, 230, 84, ls, L, A, size=18)
s.ar(515, 120, 640, 205); s.ar(640, 295, 515, 380); s.ar(285, 380, 160, 295); s.ar(160, 205, 285, 120)
s.t(400, 245, 'One scan', 22, A2, 'bold'); s.t(400, 272, 'typically a few ms', 18, '#4b5563')
s.t(400, 460, 'An input that changes mid scan is seen only at the next read.', 18, '#4b5563')
fig('plc-block-diagram', 'plc-block-diagram-scan-cycle-flowchart',
    'PLC scan cycle flowchart read inputs execute program update outputs and housekeeping',
    'Diagram by Instrumentation Blog showing the repeating PLC scan cycle: read inputs, execute the program, update outputs and housekeeping, usually in a few milliseconds.',
    'Working Principle of PLC', s.svg())

s = S(450, 'PLC input and output module signal types with field device examples')
s.head('PLC I/O Modules at a Glance', A2)
rows = [('DI', 'Digital input', '24 V DC on or off', 'Push button, limit switch'), ('AI', 'Analog input', '4 to 20 mA, 0 to 10 V', 'Pressure transmitter, RTD'),
        ('DO', 'Digital output', 'Relay or transistor', 'Motor starter, solenoid'), ('AO', 'Analog output', '4 to 20 mA', 'Valve positioner, VFD speed')]
s.raw(f'<rect x="30" y="60" width="740" height="44" rx="8" fill="{A}"/>')
for x, h in [(90, 'Type'), (240, 'Module'), (440, 'Signal'), (640, 'Example device')]: s.t(x, 89, h, 19, '#ffffff', 'bold')
for i, r in enumerate(rows):
    y = 110 + i * 70
    s.raw(f'<rect x="30" y="{y}" width="740" height="64" rx="8" fill="{L if i % 2 == 0 else "#ffffff"}" stroke="#e5e7eb" stroke-width="1.5"/>')
    s.t(90, y + 40, r[0], 22, A2, 'bold'); s.t(240, y + 40, r[1], 18); s.t(440, y + 40, r[2], 18); s.t(640, y + 40, r[3], 18)
s.t(400, 425, 'Inputs bring field status in; outputs send commands out.', 18, '#4b5563')
fig('plc-block-diagram', 'plc-block-diagram-io-modules-infographic',
    'PLC input and output modules DI AI DO AO with signal types and example devices',
    'Diagram by Instrumentation Blog listing PLC input and output module types with their signals and typical field devices for DI, AI, DO and AO.',
    'Input and Output Module', s.svg())

# ============ 5. Signals AI AO DI DO ============
A, A2, L = '#059669', '#065f46', '#ecfdf5'
s = S(470, 'AI AO DI DO signal loop between field devices and a PLC')
s.head('AI, AO, DI and DO in One Control Loop', A2)
s.raw(f'<rect x="300" y="90" width="200" height="290" rx="16" fill="{L}" stroke="{A}" stroke-width="3"/>'); s.t(400, 125, 'PLC or DCS', 22, A2, 'bold')
for y, lab in [(170, 'AI card'), (230, 'DI card'), (290, 'AO card'), (350, 'DO card')]: s.box(330, y - 22, 140, 40, [lab], '#ffffff', A, size=17)
s.box(20, 120, 210, 66, ['Pressure', 'transmitter'], '#fff7e6', size=17); s.ar(232, 160, 328, 168); s.t(282, 146, '4 to 20 mA', 16, A2, 'bold')
s.box(20, 205, 210, 58, ['Limit switch'], '#fff7e6', size=17); s.ar(232, 232, 328, 230); s.t(282, 222, '24 V DC', 16, A2, 'bold')
s.box(570, 255, 210, 66, ['Control valve', 'positioner'], '#fff7e6', size=17); s.ar(472, 290, 568, 288); s.t(520, 278, '4 to 20 mA', 16, A2, 'bold')
s.box(570, 330, 210, 58, ['Motor starter'], '#fff7e6', size=17); s.ar(472, 350, 568, 358); s.t(520, 345, '24 V DC', 16, A2, 'bold')
s.t(125, 300, 'Inputs: field to PLC', 19, A2, 'bold'); s.t(675, 220, 'Outputs: PLC to field', 19, A2, 'bold')
s.t(400, 440, 'Analog signals carry a range of values; digital signals carry ON or OFF.', 18, '#4b5563')
fig('signals-in-instrumentation-ai-ao-di-do', 'signals-in-instrumentation-ai-ao-di-do-loop-diagram',
    'AI AO DI DO signals diagram with transmitter, limit switch, valve positioner and motor starter',
    'Diagram by Instrumentation Blog showing analog and digital input and output signals between field devices and a PLC: transmitter, limit switch, valve positioner and motor starter.',
    'What are different types of Signals in Instrumentation', s.svg())

s = S(520, 'Troubleshooting flowchart for AI AO DI DO signal problems')
s.head('Signal Problem? Start Here', A2)
s.box(270, 55, 260, 50, ['Which signal fails?'], A, A, '#ffffff', size=20)
cols = [('AI fluctuating', ['Loose terminals', 'Grounding issue', 'EMI from VFD']), ('AO no response', ['Output card scaling', 'Positioner calibration', 'Loop wiring']),
        ('DI not detecting', ['Field switch', 'Cable continuity', 'Then the card']), ('DO not energizing', ['Coil resistance', 'Card rating', 'Fuse and supply'])]
for i, (h, ls) in enumerate(cols):
    x = 15 + i * 197
    s.ar(400, 105, x + 90, 150)
    s.box(x, 150, 180, 56, [h], L, A, size=18)
    for j, l in enumerate(ls):
        s.ar(x + 90, 206 + j * 80, x + 90, 228 + j * 80)
        s.box(x + 5, 228 + j * 80, 170, 52, [l], '#ffffff', A, size=17, bold_first=False)
s.t(400, 505, 'Check the field side first, the card last.', 19, A2, 'bold')
fig('signals-in-instrumentation-ai-ao-di-do', 'signals-in-instrumentation-troubleshooting-flowchart',
    'troubleshooting flowchart for analog and digital input and output signal problems',
    'Diagram by Instrumentation Blog showing what to check when an AI fluctuates, an AO gives no response, a DI does not detect or a DO does not energize.',
    'Troubleshooting Signal Problems', s.svg())

s = S(430, '4 to 20 mA analog input scaling chart for a 0 to 10 bar transmitter')
s.head('Analog Input Scaling: 4 to 20 mA to 0 to 10 bar', A2)
x0, y0, W, H = 110, 340, 600, 250
s.ln(x0, y0, x0 + W, y0, '#1a2b4a', 2.5); s.ln(x0, y0, x0, y0 - H, '#1a2b4a', 2.5)
s.ln(x0, y0, x0 + W, y0 - H, A, 5)
for i, (ma, bar) in enumerate([(4, 0), (8, 2.5), (12, 5), (16, 7.5), (20, 10)]):
    x = x0 + i * W / 4; y = y0 - i * H / 4
    s.raw(f'<circle cx="{x}" cy="{y}" r="7" fill="{A2}"/>'); s.t(x, y0 + 30, f'{ma} mA', 18, '#1a2b4a', 'bold')
    s.t(x0 - 14, y + 6, f'{bar:g} bar', 17, '#1a2b4a', 'normal', 'end'); s.ln(x, y0, x, y, '#e5e7eb', 1.5, '4 4')
s.t(x0 + W / 2, y0 + 62, 'Transmitter current', 18, '#4b5563')
s.box(130, 62, 330, 80, ['Value = (mA minus 4) ÷ 16 × 10', 'Example: 12 mA gives 5 bar'], '#ffffff', A, size=18)
fig('signals-in-instrumentation-ai-ao-di-do', 'signals-in-instrumentation-4-to-20-ma-scaling-infographic',
    '4 to 20 mA analog input scaling chart for a 0 to 10 bar pressure transmitter',
    'Diagram by Instrumentation Blog showing how a PLC scales a 4 to 20 mA analog input to 0 to 10 bar, with 12 mA equal to 5 bar.',
    'Analog Input (AI) Signals in Instrumentation', s.svg())

for slug, figs in CH.items():
    json.dump({'slug': slug, 'figs': figs}, open(f'{OUT}/{slug}.json', 'w'), indent=1)
print({k: len(v) for k, v in CH.items()})
