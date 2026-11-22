import json, sys, math
sys.path.insert(0, '/home/claude/instrumentationblog-howitworks/_img')
from svglib import S
OUT = '/home/claude/instrumentationblog-howitworks/_img/changes'
CH = {}
def fig(slug, name, alt, caption, after, svg):
    CH.setdefault(slug, []).append(dict(name=name, alt=alt, caption=caption, after_h2=after, svg=svg))
def rect(s, x, y, w, h, fill, stroke='#1a2b4a', r=10, sw=2):
    s.raw(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>')
def circ(s, cx, cy, r, fill, stroke='#1a2b4a', sw=2):
    s.raw(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>')

# ============ 1. Photoelectric sensors (orange) ============
SL = 'different-types-of-photoelectric-sensors'
A, A2, L = '#d97706', '#92400e', '#fff7ed'
BEAM = '#dc2626'
s = S(600, 'Three photoelectric sensor types: through beam, retro reflective and diffuse reflective')
s.head('3 Types of Photoelectric Sensor', A2)
rows = [(80, '1. Through beam', 'Object blocks the beam to the separate receiver'),
        (255, '2. Retro reflective', 'Light returns from a reflector; object blocks it'),
        (430, '3. Diffuse reflective', 'The object itself reflects light back')]
for y, h, note in rows:
    rect(s, 20, y, 760, 160, L, A, 14)
    s.t(40, y + 30, h, 20, A2, 'bold', 'start')
    s.t(760, y + 30, note, 17, '#4b5563', 'normal', 'end')
# row 1: emitter, object, receiver
y = 80
rect(s, 50, y + 60, 120, 70, '#ffffff'); s.t(110, y + 102, 'Emitter', 18, '#1a2b4a', 'bold')
rect(s, 630, y + 60, 120, 70, '#ffffff'); s.t(690, y + 102, 'Receiver', 18, '#1a2b4a', 'bold')
s.ln(172, y + 95, 360, y + 95, BEAM, 4)
s.ln(440, y + 95, 628, y + 95, BEAM, 2, '6 6')
rect(s, 362, y + 55, 76, 80, '#9ca3af', r=6); s.t(400, y + 101, 'Object', 17, '#ffffff', 'bold')
s.t(530, y + 80, 'no light', 17, '#4b5563')
# row 2: sensor unit + reflector
y = 255
rect(s, 50, y + 55, 150, 85, '#ffffff'); s.t(125, y + 85, 'Emitter and', 17, '#1a2b4a', 'bold'); s.t(125, y + 108, 'receiver', 17, '#1a2b4a', 'bold')
s.ar(202, y + 75, 655, y + 75, BEAM, 3)
s.ar(655, y + 120, 202, y + 120, BEAM, 3)
s.raw(f'<polygon points="660,{y+55} 700,{y+75} 660,{y+97} 700,{y+118} 660,{y+140}" fill="#fde68a" stroke="#1a2b4a" stroke-width="2"/>')
s.t(745, y + 150, 'Reflector', 17, '#1a2b4a', 'bold', 'end')
s.t(430, y + 102, 'beam goes out and back', 17, '#4b5563')
# row 3: diffuse
y = 430
rect(s, 50, y + 55, 150, 85, '#ffffff'); s.t(125, y + 85, 'Emitter and', 17, '#1a2b4a', 'bold'); s.t(125, y + 108, 'receiver', 17, '#1a2b4a', 'bold')
s.ar(202, y + 75, 525, y + 75, BEAM, 3)
s.ar(525, y + 120, 202, y + 120, BEAM, 3, '7 5')
s.raw(f'<rect x="530" y="{y+55}" width="90" height="85" rx="6" fill="#9ca3af" stroke="#1a2b4a" stroke-width="2"/>')
s.t(575, y + 103, 'Object', 17, '#ffffff', 'bold')
s.t(365, y + 102, 'reflected light', 17, '#4b5563')
fig(SL, 'photoelectric-sensor-types-through-beam-retro-diffuse-diagram',
    'photoelectric sensor types diagram with through beam, retro reflective and diffuse reflective modes',
    'Diagram by Instrumentation Blog comparing the three photoelectric sensor sensing modes: through beam with separate emitter and receiver, retro reflective with a reflector, and diffuse reflective from the object.',
    'Type of Photoelectric Sensors', s.svg())

s = S(520, 'How a photoelectric sensor detects an object, from emitter light to output signal')
s.head('How a Photoelectric Sensor Detects an Object', A2)
steps = [['1. Emitter', 'LED or laser', 'diode makes light'], ['2. Light path', 'object blocks', 'or reflects it'],
         ['3. Receiver', 'photodiode or', 'phototransistor']]
x = 40
for i, ls in enumerate(steps):
    s.box(x, 80, 210, 110, ls, L if i % 2 == 0 else '#ffffff', A, size=18)
    if i < 2: s.ar(x + 212, 135, x + 248, 135)
    x += 250
s.pl([(645, 192), (645, 240)], '#1a2b4a', 2.5)
steps2 = [['4. Amplifier', 'light change to', 'electrical signal'], ['5. Detection circuit', 'checks the light came', 'from its own emitter'], ['6. Output', 'object detected', 'signal sent']]
x = 540
for i, ls in enumerate(steps2):
    s.box(x, 245, 210, 110, ls, '#ffffff' if i % 2 == 0 else L, A, size=17)
    if i < 2: s.ar(x - 2, 300, x - 38, 300)
    x -= 250
s.pl([(145, 357), (145, 395)], '#1a2b4a', 2.5)
s.box(40, 400, 330, 90, ['Digital output', 'ON or OFF to PLC, relay, alarm'], L, A, size=17)
s.box(430, 400, 330, 90, ['Analog output', 'voltage or current to light level'], L, A, size=17)
s.pl([(145, 395), (595, 395), (595, 398)], '#1a2b4a', 2.5)
fig(SL, 'photoelectric-sensor-working-sequence-flowchart',
    'how a photoelectric sensor works from emitter light to receiver and output signal',
    'Diagram by Instrumentation Blog showing the photoelectric sensor working sequence: emitter light, object blocking or reflecting it, receiver, amplifier, detection circuit and digital or analog output.',
    'What are Photoelectric Sensors?', s.svg())

s = S(560, 'Light On and Dark On output modes with sourcing PNP and sinking NPN outputs')
s.head('Photoelectric Sensor Output Modes', A2)
cols = [(30, 260, 'Condition'), (290, 240, 'Light On'), (530, 240, 'Dark On')]
yy = 70
for x, w, h in cols:
    rect(s, x, yy, w, 50, A, A, 0); s.t(x + w / 2, yy + 32, h, 19, '#ffffff', 'bold')
data = [('Through beam or retro:', 'beam reaches receiver', 'Output ON', 'Output OFF'),
        ('Through beam or retro:', 'object breaks beam', 'Output OFF', 'Output ON'),
        ('Diffuse:', 'object reflects light', 'Output ON', 'Output OFF'),
        ('Diffuse:', 'no object, no light', 'Output OFF', 'Output ON')]
for i, (a, b, c, d) in enumerate(data):
    y = 120 + i * 70
    f = L if i % 2 == 0 else '#ffffff'
    for x, w, _ in cols: rect(s, x, y, w, 70, f, '#e5c9a0', 0, 1.5)
    s.t(45, y + 30, a, 17, '#1a2b4a', 'bold', 'start'); s.t(45, y + 54, b, 17, '#1a2b4a', 'normal', 'start')
    for x, v in ((410, c), (650, d)):
        s.t(x, y + 42, v, 18, '#15803d' if 'ON' in v else '#6b7280', 'bold')
rect(s, 30, 420, 360, 115, '#ffffff', A, 12); s.t(210, 455, 'Sourcing (PNP)', 20, A2, 'bold')
s.t(210, 485, 'gives positive voltage', 18); s.t(210, 510, 'to the load when ON', 18)
rect(s, 410, 420, 360, 115, '#ffffff', A, 12); s.t(590, 455, 'Sinking (NPN)', 20, A2, 'bold')
s.t(590, 485, 'connects the load to', 18); s.t(590, 510, 'ground or negative', 18)
fig(SL, 'photoelectric-sensor-light-on-dark-on-output-infographic',
    'photoelectric sensor light on and dark on output table with PNP and NPN outputs',
    'Diagram by Instrumentation Blog showing when a photoelectric sensor output switches in Light On and Dark On modes for through beam, retro and diffuse types, plus PNP and NPN outputs.',
    'Photoelectric Sensor Outputs', s.svg())

# ============ 2. Flip-flop types (purple) ============
SL = 'flip-flop-types-sr-jk-d-t'
A, A2, L = '#7c3aed', '#5b21b6', '#f5f3ff'
def ff(s, x, y, labs=('J', 'CLK', 'K')):
    rect(s, x, y, 120, 150, '#ffffff', A2, 8, 2.5)
    s.t(x + 60, y + 30, 'JK FF', 18, A2, 'bold')
    for i, lb in enumerate(labs):
        yy = y + 50 + i * 40
        s.t(x + 12, yy + 6, lb, 17, '#1a2b4a', 'bold', 'start')
    s.t(x + 108, y + 56, 'Q', 18, '#1a2b4a', 'bold', 'end'); s.t(x + 108, y + 136, "Q'", 18, '#1a2b4a', 'bold', 'end')
    s.ln(x + 120, y + 50, x + 170, y + 50); s.ln(x + 120, y + 130, x + 170, y + 130)
s = S(480, 'Converting a JK flip flop into a D flip flop and a T flip flop')
s.head('Converting a JK Flip Flop to D and T', A2)
rect(s, 20, 60, 370, 400, L, A, 14); rect(s, 410, 60, 370, 400, L, A, 14)
s.t(205, 95, 'JK to D', 21, A2, 'bold'); s.t(595, 95, 'JK to T', 21, A2, 'bold')
# JK to D
fx, fy = 200, 150
ff(s, fx, fy)
s.ln(50, fy + 50, fx, fy + 50); s.t(50, fy + 40, 'D', 19, A2, 'bold', 'start')
circ(s, 90, fy + 50, 5, '#1a2b4a')
s.pl([(90, fy + 50), (90, fy + 130), (120, fy + 130)], '#1a2b4a', 2.5, False)
s.raw(f'<polygon points="120,{fy+115} 120,{fy+145} 148,{fy+130}" fill="#ffffff" stroke="#1a2b4a" stroke-width="2"/>')
circ(s, 153, fy + 130, 5, '#ffffff')
s.ln(158, fy + 130, fx, fy + 130)
s.ln(150, fy + 90, fx, fy + 90); s.t(140, fy + 96, 'Clock', 17, '#1a2b4a', 'normal', 'end')
s.t(205, 370, 'D goes to J, inverted D to K,', 18); s.t(205, 396, 'so J and K are always opposite', 18)
s.t(205, 430, 'Q follows D on each clock edge', 18, A2, 'bold')
# JK to T
fx = 590
ff(s, fx, fy)
s.ln(430, fy + 90, 470, fy + 90); s.t(432, fy + 80, 'T', 19, A2, 'bold', 'start')
circ(s, 470, fy + 90, 5, '#1a2b4a')
s.pl([(470, fy + 90), (470, fy + 50), (fx, fy + 50)], '#1a2b4a', 2.5, False)
s.pl([(470, fy + 90), (470, fy + 130), (fx, fy + 130)], '#1a2b4a', 2.5, False)
s.ln(535, fy + 90, fx, fy + 90); s.t(482, fy + 96, 'Clock', 17, '#1a2b4a', 'normal', 'start')
s.t(595, 370, 'J and K tied together', 18); s.t(595, 396, 'form the single T input', 18)
s.t(595, 430, 'T = 1 toggles, T = 0 holds', 18, A2, 'bold')
fig(SL, 'flip-flop-types-jk-to-d-and-t-conversion-diagram',
    'JK flip flop converted to D and T flip flop wiring diagram',
    'Diagram by Instrumentation Blog showing how a JK flip flop becomes a D flip flop with an inverter on K, and a T flip flop with J and K tied together.',
    'Converting Between Flip-Flop Types', s.svg())

s = S(560, 'Flip flop operating cycle flowchart with JK input decisions')
s.head('How a JK Flip Flop Decides Its Next State', A2)
s.box(40, 70, 220, 80, ['Inputs set up', 'J and K driven'], L, A, size=18)
s.ar(262, 110, 318, 110)
s.dia(420, 110, 200, 110, ['Clock', 'edge?'], '#fff7e6', A2)
s.pl([(520, 110), (570, 110)], '#1a2b4a', 2.5); s.t(545, 100, 'No', 17, '#6b7280', 'bold')
s.box(572, 75, 200, 70, ['Hold Q', 'inputs ignored'], '#ffffff', '#6b7280', size=17)
s.pl([(672, 147), (672, 175), (150, 175), (150, 152)], '#6b7280', 2, dash='6 5')
s.ar(420, 165, 420, 215); s.t(440, 200, 'Yes', 17, '#15803d', 'bold', 'start')
s.box(270, 218, 300, 60, ['Read J and K'], L, A, size=19)
s.ln(420, 278, 420, 305)
s.ln(115, 305, 685, 305)
outs = [('J=0, K=0', 'Hold', 'Q unchanged'), ('J=0, K=1', 'Reset', 'Q = 0'), ('J=1, K=0', 'Set', 'Q = 1'), ('J=1, K=1', 'Toggle', "Q = Q'")]
for i, (c, op, q) in enumerate(outs):
    x = 30 + i * 190
    s.ar(x + 85, 305, x + 85, 330)
    s.box(x, 333, 170, 110, [c, op, q], L if i % 2 == 0 else '#ffffff', A, size=18)
s.box(170, 470, 460, 64, ['Q locks and holds until the next clock edge'], '#fff7e6', A2, size=18)
fig(SL, 'flip-flop-types-jk-next-state-flowchart',
    'JK flip flop flowchart deciding hold, reset, set or toggle on a clock edge',
    'Diagram by Instrumentation Blog showing the flip flop cycle: inputs set up, the clock edge triggers a read of J and K, and Q holds, resets, sets or toggles.',
    'How a Flip-Flop Stores One Bit', s.svg())

s = S(540, 'Characteristic equations of SR, JK, D and T flip flops with a worked JK example')
s.head('Flip Flop Characteristic Equations', A2)
cards = [('SR', "Q(next) = S + R'Q", 'valid only when S and R are not both 1'),
         ('JK', "Q(next) = JQ' + K'Q", 'no invalid state, J = K = 1 toggles'),
         ('D', 'Q(next) = D', 'Q copies D on the clock edge'),
         ('T', 'Q(next) = T XOR Q', 'T = 1 toggles, T = 0 holds')]
for i, (n, eq, note) in enumerate(cards):
    x = 30 + (i % 2) * 380; y = 65 + (i // 2) * 145
    rect(s, x, y, 360, 128, L, A, 14)
    circ(s, x + 42, y + 42, 26, A, A); s.t(x + 42, y + 49, n, 19, '#ffffff', 'bold')
    s.t(x + 82, y + 50, eq, 21, A2, 'bold', 'start')
    s.t(x + 20, y + 100, note, 17, '#1a2b4a', 'normal', 'start')
rect(s, 30, 365, 740, 150, '#ffffff', A2, 14, 2.5)
s.t(400, 400, 'Worked example: JK with Q = 0, J = 1, K = 1', 20, A2, 'bold')
s.t(400, 440, "Q(next) = JQ' + K'Q = (1)(1) + (0)(0) = 1", 21, '#1a2b4a', 'bold')
s.t(400, 485, 'Q goes from 0 to 1, so the output toggled', 18, '#4b5563')
fig(SL, 'flip-flop-types-characteristic-equations-infographic',
    'flip flop types characteristic equations for SR, JK, D and T with a worked example',
    'Diagram by Instrumentation Blog listing the next state equations of SR, JK, D and T flip flops, with the JK worked example where Q goes from 0 to 1.',
    'Flip-Flop Characteristic Equations', s.svg())

# ============ 3. Flow characteristics (green) ============
SL = 'flow-characteristics-of-control-valves'
A, A2, L = '#15803d', '#14532d', '#f0fdf4'
s = S(540, 'Inherent flow characteristic chart: quick opening, linear and equal percentage curves')
s.head('Inherent Flow Characteristics of Control Valves', A2)
ox, oy, W, H = 110, 470, 420, 380
s.ln(ox, oy, ox + W, oy, '#1a2b4a', 2.5); s.ln(ox, oy, ox, oy - H, '#1a2b4a', 2.5)
for k in range(0, 101, 25):
    gx = ox + W * k / 100; gy = oy - H * k / 100
    s.ln(gx, oy, gx, oy - H, '#e5e7eb', 1); s.ln(ox, gy, ox + W, gy, '#e5e7eb', 1)
    s.t(gx, oy + 24, str(k), 17); s.t(ox - 12, gy + 6, str(k), 17, '#1a2b4a', 'normal', 'end')
s.t(ox + W / 2, oy + 52, 'Valve travel, %', 18, '#1a2b4a', 'bold')
s.raw(f'<text x="40" y="{oy - H/2}" font-size="18" font-weight="bold" fill="#1a2b4a" text-anchor="middle" transform="rotate(-90 40 {oy - H/2})">Flow, %</text>')
def curve(f, col):
    pts = [(ox + W * x / 100, oy - H * f(x / 100)) for x in range(0, 101, 2)]
    s.pl(pts, col, 4, False)
curve(lambda x: math.sqrt(x) if x > 0 else 0, '#dc2626')
curve(lambda x: x, '#2563eb')
curve(lambda x: 50 ** (x - 1), A)
lx = 565
for i, (c, n, d) in enumerate([('#dc2626', 'Quick opening', 'big flow at small travel'),
                                 ('#2563eb', 'Linear', '20% travel, 20% flow'),
                                 (A, 'Equal percentage', 'gain rises with travel')]):
    y = 120 + i * 95
    s.ln(lx, y, lx + 40, y, c, 5); s.t(lx + 50, y + 6, n, 18, c, 'bold', 'start')
    s.t(lx + 50, y + 32, d, 17, '#4b5563', 'normal', 'start')
s.t(lx + 100, 420, 'At constant', 17, '#4b5563'); s.t(lx + 100, 444, 'pressure drop', 17, '#4b5563')
fig(SL, 'flow-characteristics-control-valve-inherent-curves-chart',
    'control valve flow characteristics chart of quick opening, linear and equal percentage curves',
    'Diagram by Instrumentation Blog plotting percent flow against percent valve travel for quick opening, linear and equal percentage trims at constant pressure drop.',
    'What Are Flow Characteristics?', s.svg())

s = S(500, 'Inherent versus installed flow characteristic: test lab piping compared with real plant piping')
s.head('Inherent vs Installed Flow Characteristic', A2)
rect(s, 20, 60, 760, 150, L, A, 14)
s.t(40, 90, 'Inherent: manufacturer test lab', 20, A2, 'bold', 'start')
s.raw(f'<rect x="60" y="130" width="250" height="26" fill="#cbd5e1" stroke="#1a2b4a" stroke-width="2"/>')
s.raw(f'<polygon points="310,118 360,143 310,168" fill="{A}" stroke="#1a2b4a" stroke-width="2"/><polygon points="410,118 360,143 410,168" fill="{A}" stroke="#1a2b4a" stroke-width="2"/>')
s.raw(f'<rect x="410" y="130" width="60" height="26" fill="#cbd5e1" stroke="#1a2b4a" stroke-width="2"/>')
s.t(360, 195, 'Valve', 17, A2, 'bold')
s.t(500, 140, 'Very short piping,', 18, '#1a2b4a', 'normal', 'start'); s.t(500, 166, 'constant pressure drop', 18, '#1a2b4a', 'bold', 'start')
rect(s, 20, 230, 760, 250, '#ffffff', A, 14)
s.t(40, 260, 'Installed: real plant', 20, A2, 'bold', 'start')
s.raw(f'<rect x="40" y="300" width="720" height="26" fill="#cbd5e1" stroke="#1a2b4a" stroke-width="2"/>')
items = [(110, 'Pipe length'), (250, 'Elbow, tee'), (400, 'Valve'), (540, 'Exchanger'), (680, 'Flow meter')]
for x, n in items:
    if n == 'Valve':
        s.raw(f'<polygon points="{x-40},288 {x},313 {x-40},338" fill="{A}" stroke="#1a2b4a" stroke-width="2"/><polygon points="{x+40},288 {x},313 {x+40},338" fill="{A}" stroke="#1a2b4a" stroke-width="2"/>')
    elif n != 'Pipe length':
        rect(s, x - 45, 290, 90, 46, '#fde68a', r=6)
    s.t(x, 366, n, 17, A2 if n == 'Valve' else '#1a2b4a', 'bold')
s.ar(40, 280, 120, 280, A, 3); s.t(125, 286, 'flow', 17, A2, 'normal', 'start')
s.t(400, 410, 'Series losses rise with about the square of flow,', 18)
s.t(400, 440, 'so the valve pressure drop changes as the valve opens', 18, '#1a2b4a', 'bold')
fig(SL, 'flow-characteristics-inherent-vs-installed-piping-diagram',
    'inherent vs installed control valve flow characteristic piping diagram',
    'Diagram by Instrumentation Blog comparing the short test lab piping that gives the inherent characteristic with real plant piping where fittings and equipment change the valve pressure drop.',
    'Installed Control Valve Flow Characteristics', s.svg())

s = S(600, 'Flowchart for choosing a control valve flow characteristic by application')
s.head('Choosing a Flow Characteristic', A2)
qs = [('On and off or', 'safety duty?', 'Quick opening'),
      ('Level loop or constant', 'valve pressure drop?', 'Linear'),
      ('Flow or pressure loop', 'with variable load?', 'Equal percentage'),
      ('Temperature loop or', 'energy optimisation?', 'Modified parabolic or hybrid')]
y = 75
for i, (a, b, r) in enumerate(qs):
    s.box(40, y, 360, 82, [a, b], L, A, size=18, bold_first=False)
    s.ar(402, y + 41, 470, y + 41, A, 2.5); s.t(436, y + 31, 'Yes', 17, A, 'bold')
    s.box(472, y + 6, 290, 70, [r], '#ffffff', A2, size=18)
    if i < 3:
        s.ar(220, y + 84, 220, y + 108); s.t(240, y + 102, 'No', 17, '#6b7280', 'bold', 'start')
    y += 110
s.ar(220, y - 26, 220, y + 2); s.t(240, y - 6, 'No', 17, '#6b7280', 'bold', 'start')
s.box(40, y + 4, 722, 64, ['Engineered special case only: hyperbolic'], '#fff7e6', A2, size=18)
fig(SL, 'flow-characteristics-control-valve-selection-flowchart',
    'flowchart to select linear, equal percentage or quick opening control valve characteristic',
    'Diagram by Instrumentation Blog showing how to choose a valve flow characteristic: quick opening for on and off duty, linear for level, equal percentage for flow and pressure.',
    'Practical Selection Guidelines', s.svg())

# ============ 4. Half adder vs full adder (red) ============
SL = 'half-adder-vs-full-adder'
A, A2, L = '#dc2626', '#991b1b', '#fef2f2'
s = S(500, 'Full adder built from two half adders and an OR gate')
s.head('Full Adder From Two Half Adders', A2)
rect(s, 170, 90, 170, 150, L, A, 12); s.t(255, 125, 'Half adder 1', 18, A2, 'bold')
s.t(255, 160, 'S1 = A XOR B', 17); s.t(255, 190, 'C1 = A AND B', 17)
rect(s, 430, 170, 170, 150, L, A, 12); s.t(515, 205, 'Half adder 2', 18, A2, 'bold')
s.t(515, 240, 'S = S1 XOR Cin', 17); s.t(515, 270, 'C2 = S1 AND Cin', 17)
s.raw(f'<path d="M560 380 Q600 380 640 405 Q600 430 560 430 Q575 405 560 380 Z" fill="#ffffff" stroke="#1a2b4a" stroke-width="2.5"/>')
s.t(600, 412, 'OR', 17, A2, 'bold')
# inputs
s.ln(60, 130, 170, 130); s.t(50, 136, 'A', 20, A2, 'bold', 'end')
s.ln(60, 200, 170, 200); s.t(50, 206, 'B', 20, A2, 'bold', 'end')
s.ln(60, 290, 430, 290); s.t(50, 296, 'Cin', 20, A2, 'bold', 'end')
# S1 to HA2
s.pl([(340, 130), (385, 130), (385, 210), (430, 210)], '#1a2b4a', 2.5, False); s.t(362, 120, 'S1', 17, A2, 'bold')
# C1 to OR
s.raw('<path d="M340 210 H365 V280 A10 10 0 0 1 365 300 V420 H566" fill="none" stroke="#1a2b4a" stroke-width="2.5"/>'); s.t(395, 412, 'C1', 17, A2, 'bold')
# C2 to OR
s.pl([(600, 290), (615, 290), (615, 345), (520, 345), (520, 390), (566, 390)], '#1a2b4a', 2.5, False); s.t(500, 372, 'C2', 17, A2, 'bold')
# outputs
s.ar(600, 210, 720, 210, A, 3); s.t(730, 216, 'Sum', 20, A2, 'bold', 'start')
s.ar(640, 405, 720, 405, A, 3); s.t(730, 411, 'Cout', 20, A2, 'bold', 'start')
s.t(400, 475, 'Cout = C1 OR C2, total gates: 2 XOR, 2 AND, 1 OR', 18, '#4b5563')
fig(SL, 'half-adder-vs-full-adder-two-half-adders-circuit-diagram',
    'full adder made from two half adders and one OR gate block diagram',
    'Diagram by Instrumentation Blog showing a full adder built from two half adders: the first adds A and B, the second adds Cin, and an OR gate joins both carries.',
    'Building a Full Adder From Two Half Adders', s.svg())

s = S(560, 'Full adder worked example A equals 1, B equals 0, Cin equals 1 step by step')
s.head('Full Adder Worked Example: A=1, B=0, Cin=1', A2)
steps = [('Step 1', 'First half adder', 'S1 = 1 XOR 0 = 1', 'C1 = 1 AND 0 = 0'),
         ('Step 2', 'Second half adder', 'Sum = S1 XOR Cin = 1 XOR 1 = 0', 'C2 = S1 AND Cin = 1 AND 1 = 1'),
         ('Step 3', 'OR gate', 'Cout = C1 OR C2 = 0 OR 1 = 1', '')]
y = 70
for i, (n, h, l1, l2) in enumerate(steps):
    hh = 110 if l2 else 84
    rect(s, 60, y, 680, hh, L if i % 2 == 0 else '#ffffff', A, 12)
    circ(s, 105, y + hh / 2, 30, A, A); s.t(105, y + hh / 2 + 7, str(i + 1), 22, '#ffffff', 'bold')
    s.t(155, y + 32, h, 19, A2, 'bold', 'start')
    s.t(155, y + 62, l1, 18, '#1a2b4a', 'normal', 'start')
    if l2: s.t(155, y + 90, l2, 18, '#1a2b4a', 'normal', 'start')
    if i < 2: s.ar(400, y + hh + 2, 400, y + hh + 26)
    y += hh + 30
rect(s, 60, y, 680, 92, '#fff7e6', A2, 12, 2.5)
s.t(400, y + 36, 'Result: Sum = 0, Cout = 1', 21, A2, 'bold')
s.t(400, y + 70, 'Check: Cout = AB + BCin + ACin = 0 + 0 + 1 = 1', 18, '#1a2b4a')
fig(SL, 'half-adder-vs-full-adder-worked-example-flowchart',
    'full adder worked example flowchart with A 1, B 0 and carry in 1',
    'Diagram by Instrumentation Blog working through the full adder example A equals 1, B equals 0, Cin equals 1, giving Sum 0 and Cout 1 through two half adders.',
    'Sum and Carry Formulas', s.svg())

s = S(560, 'Half adder vs full adder comparison of inputs, sum, carry, gates and cascading')
s.head('Half Adder vs Full Adder at a Glance', A2)
cols = [(30, 200, 'Point'), (230, 260, 'Half adder'), (490, 280, 'Full adder')]
for x, w, h in cols:
    rect(s, x, 65, w, 50, A2 if h == 'Point' else A, A2, 0); s.t(x + w / 2, 97, h, 19, '#ffffff', 'bold')
data = [('Inputs', '2: A, B', '3: A, B, Cin'), ('Sum', 'A XOR B', 'A XOR B XOR Cin'),
        ('Carry', 'A AND B', 'AB + BCin + ACin'), ('Gates', '1 XOR, 1 AND', '2 XOR, 2 AND, 1 OR'),
        ('Cascading', 'Cannot be chained', 'Ripple carry adder'), ('Used at', 'Least significant bit', 'Every other bit')]
for i, row in enumerate(data):
    y = 115 + i * 66
    for j, (x, w, _) in enumerate(cols):
        rect(s, x, y, w, 66, L if i % 2 == 0 else '#ffffff', '#f3c4c4', 0, 1.5)
        s.t(x + w / 2, y + 40, row[j], 18, A2 if j == 0 else '#1a2b4a', 'bold' if j == 0 else 'normal')
s.t(400, 535, 'Half adder truth table: 4 rows. Full adder truth table: 8 rows.', 18, '#4b5563')
fig(SL, 'half-adder-vs-full-adder-comparison-infographic',
    'half adder vs full adder comparison of inputs, sum, carry and gate count',
    'Diagram by Instrumentation Blog comparing half adder and full adder inputs, sum and carry expressions, gate count, cascading and where each is used in a multi bit adder.',
    '5 Key Differences Between Half Adder and Full Adder', s.svg())

# ============ 5. Hazardous area classification (magenta) ============
SL = 'hazardous-area-classification-zone'
A, A2, L = '#be185d', '#831843', '#fdf2f8'
s = S(560, 'Hazardous area zones around a flammable liquid storage tank: Zone 0, Zone 1 and Zone 2')
s.head('Hazardous Area Zones Around a Tank', A2)
s.raw('<ellipse cx="270" cy="330" rx="240" ry="200" fill="#fef9c3" stroke="#a16207" stroke-width="2.5" stroke-dasharray="9 6"/>')
s.raw('<ellipse cx="270" cy="330" rx="165" ry="140" fill="#fed7aa" stroke="#c2410c" stroke-width="2.5" stroke-dasharray="9 6"/>')
s.raw(f'<rect x="185" y="260" width="170" height="200" rx="8" fill="#fecaca" stroke="#1a2b4a" stroke-width="3"/>')
s.raw('<rect x="262" y="236" width="16" height="24" fill="#9ca3af" stroke="#1a2b4a" stroke-width="2"/>')
s.t(270, 345, 'Zone 0', 20, '#991b1b', 'bold'); s.t(270, 372, 'inside tank', 17, '#1a2b4a')
s.t(270, 228, 'Vent', 17, '#1a2b4a', 'bold')
s.t(147, 336, 'Zone 1', 18, '#9a3412', 'bold')
s.t(270, 168, 'Zone 2', 19, '#854d0e', 'bold')
keys = [('#fecaca', 'Zone 0', 'more than 1,000 h per year', 'Category 1G, Ex ia'),
        ('#fed7aa', 'Zone 1', '10 to 1,000 h per year', 'Category 2G, Ex d, e, ib'),
        ('#fef9c3', 'Zone 2', 'less than 10 h per year', 'Category 3G, Ex n, e, p')]
for i, (c, z, hrs, eq) in enumerate(keys):
    y = 80 + i * 140
    rect(s, 540, y, 240, 120, c, A, 12)
    s.t(660, y + 32, z, 20, A2, 'bold'); s.t(660, y + 64, hrs, 17); s.t(660, y + 94, eq, 17, '#1a2b4a', 'bold')
s.t(400, 548, 'Real zone boundaries come from gas dispersion study, not fixed radii', 17, '#4b5563')
fig(SL, 'hazardous-area-classification-zone-0-1-2-tank-diagram',
    'hazardous area classification diagram of zone 0, zone 1 and zone 2 around a tank',
    'Diagram by Instrumentation Blog showing Zone 0 inside a flammable liquid tank, Zone 1 around the vent and Zone 2 outside, with hours per year and equipment category.',
    'Zone 0, Zone 1 and Zone 2: IEC 60079-10-1 Definitions', s.svg())

s = S(600, 'Flowchart for selecting Ex equipment: zone, gas group, temperature class and protection method')
s.head('Selecting Ex Equipment for a Hazardous Area', A2)
steps = [('1. Find the zone', 'how long the explosive atmosphere is present'),
         ('2. Pick the category', '1G for Zone 0, 2G for Zone 1, 3G for Zone 2'),
         ('3. Pick the gas group', 'IIC covers IIB and IIA; IIA only for IIA gases'),
         ('4. Pick the T class', 'max surface temperature below the gas AIT'),
         ('5. Pick the protection', 'Ex ia, d, e, n, p by zone and device type'),
         ('6. Check the marking', 'nameplate code matches all of the above')]
y = 62
for i, (h, d) in enumerate(steps):
    rect(s, 40, y, 520, 72, L if i % 2 == 0 else '#ffffff', A, 12)
    s.t(60, y + 30, h, 19, A2, 'bold', 'start'); s.t(60, y + 58, d, 17, '#1a2b4a', 'normal', 'start')
    if i < 5: s.ar(300, y + 73, 300, y + 88)
    y += 89
rect(s, 585, 290, 190, 230, '#fff7e6', A2, 12, 2.5)
s.t(680, 322, 'T class example', 18, A2, 'bold')
for j, l in enumerate(['H2S AIT is', 'about 260°C', 'T3 (200°C): safe', 'T2 (300°C): not', 'acceptable']):
    s.t(680, 356 + j * 30, l, 17, '#1a2b4a', 'bold' if j in (2, 3) else 'normal')
s.pl([(562, 383), (583, 383)], A2, 2.5)
fig(SL, 'hazardous-area-classification-ex-equipment-selection-flowchart',
    'flowchart to select Ex equipment by zone, gas group, temperature class and protection',
    'Diagram by Instrumentation Blog showing how to select Ex equipment: find the zone, category, gas group, temperature class below the gas auto ignition temperature, protection method and marking.',
    'Temperature Classes (T-Classes): Preventing Ignition by Hot Surfaces', s.svg())

s = S(560, 'How to read the Ex marking II 2G Ex d IIB T4 Gb')
s.head('Reading an Ex Marking: II 2G Ex d IIB T4 Gb', A2)
parts = [('II', 'Group II', 'surface,', 'not mining'),
         ('2G', 'Category 2', 'gas, Zone 1', 'and Zone 2'),
         ('Ex d', 'Flameproof', 'enclosure', 'protection'),
         ('IIB', 'Gas group', 'IIB and IIA,', 'not IIC'),
         ('T4', 'Max surface', 'temperature', '135°C'),
         ('Gb', 'EPL Gb', 'Zone 1 and', 'Zone 2')]
w = 118
for i, (code, a, b, c) in enumerate(parts):
    x = 30 + i * (w + 6)
    rect(s, x, 75, w, 70, A, A2, 10); s.t(x + w / 2, 120, code, 26, '#ffffff', 'bold')
    s.ln(x + w / 2, 147, x + w / 2, 180, A2, 2.5)
    rect(s, x, 180, w, 150, L, A, 10)
    s.t(x + w / 2, 215, a, 17, A2, 'bold'); s.t(x + w / 2, 255, b, 17); s.t(x + w / 2, 285, c, 17)
rect(s, 30, 360, 740, 170, '#ffffff', A2, 12, 2)
s.t(400, 395, 'Second example: II 1G Ex ia IIC T6 Ga', 20, A2, 'bold')
s.t(400, 432, '1G and Ga: suitable for Zone 0, 1 and 2', 18)
s.t(400, 464, 'Ex ia: intrinsic safety, IIC: covers every gas group', 18)
s.t(400, 496, 'T6: maximum surface temperature 85°C', 18)
fig(SL, 'hazardous-area-classification-ex-marking-code-infographic',
    'how to read Ex equipment marking code II 2G Ex d IIB T4 Gb',
    'Diagram by Instrumentation Blog decoding the Ex marking II 2G Ex d IIB T4 Gb part by part, with a second example of an intrinsically safe Zone 0 marking.',
    'How to Read Ex Equipment Marking Codes', s.svg())

for slug, figs in CH.items():
    json.dump({'slug': slug, 'figs': figs}, open(f'{OUT}/{slug}.json', 'w'), indent=1)
    print(slug, len(figs))
