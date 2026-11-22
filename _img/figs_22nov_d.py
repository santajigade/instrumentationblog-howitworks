import json, sys, os
sys.path.insert(0, '/home/claude/instrumentationblog-howitworks/_img')
from svglib import S
OUT = '/home/claude/instrumentationblog-howitworks/_img/changes'
CH = {}
def fig(slug, name, alt, caption, after, svg):
    CH.setdefault(slug, []).append(dict(name=name, alt=alt, caption=caption, after_h2=after, svg=svg))

def num(s, x, y, n, c, r=17):
    s.raw(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{c}"/>'); s.t(x, y + 6, str(n), 18, '#ffffff', 'bold')

# ================= 1. Types of thermocouples =================
slug = 'types-of-thermocouples-and-ranges'
A, A2, L = '#c2410c', '#9a3412', '#fff1e6'
s = S(470, 'Thermocouple construction with hot junction, two dissimilar wires and voltmeter')
s.head('How a Thermocouple Makes a Voltage', A2)
# process heat zone
s.raw(f'<rect x="40" y="110" width="200" height="200" rx="14" fill="{L}" stroke="{A}" stroke-width="2.5" stroke-dasharray="8 5"/>')
s.t(140, 140, 'Process heat', 19, A2, 'bold')
s.raw(f'<circle cx="150" cy="210" r="13" fill="{A}" stroke="#1a2b4a" stroke-width="2"/>')
s.t(140, 270, 'Hot junction', 19, '#1a2b4a', 'bold'); s.t(140, 294, '(measuring end)', 17, '#4b5563')
# wires
s.pl([(160, 202), (300, 170), (560, 170)], '#2563eb', 5, arrow=False)
s.pl([(160, 218), (300, 250), (560, 250)], '#dc2626', 5, arrow=False)
s.t(420, 158, 'Metal A, for example iron', 18, '#2563eb', 'bold')
s.t(420, 285, 'Metal B, for example constantan', 18, '#dc2626', 'bold')
# reference end
s.raw('<rect x="560" y="150" width="30" height="120" rx="4" fill="#e5e7eb" stroke="#1a2b4a" stroke-width="2"/>')
s.t(575, 128, 'Reference end', 18, '#1a2b4a', 'bold')
s.pl([(590, 170), (650, 170), (650, 185)], '#1a2b4a', 2.5, arrow=False)
s.pl([(590, 250), (650, 250), (650, 235)], '#1a2b4a', 2.5, arrow=False)
s.raw(f'<circle cx="650" cy="210" r="27" fill="#ffffff" stroke="#1a2b4a" stroke-width="2.5"/>')
s.t(650, 217, 'mV', 18, '#1a2b4a', 'bold')
s.t(700, 275, 'Instrument', 18, '#1a2b4a', 'bold'); s.t(700, 298, 'reads mV', 17, '#4b5563')
s.box(60, 340, 680, 100, ['Seebeck effect', 'A temperature difference between the two ends of two dissimilar metals', 'generates a small voltage that the instrument converts to temperature.'],
      '#ffffff', A, size=18)
fig(slug, 'types-of-thermocouples-seebeck-junction-diagram',
    'thermocouple hot junction and reference end with two dissimilar metal wires and millivolt meter',
    'Diagram by Instrumentation Blog showing how a thermocouple works: two dissimilar metal wires joined at a hot junction create a small Seebeck voltage read by the instrument.',
    'What Are Thermocouples?', s.svg())

# range chart
s = S(540, 'Types of thermocouples and their temperature ranges bar chart')
s.head('Types of Thermocouples and Their Ranges', A2)
x0, x1, tmin, tmax = 150, 760, -200, 1800
def X(t): return x0 + (t - tmin) * (x1 - x0) / (tmax - tmin)
for t in range(-200, 1801, 400):
    s.ln(X(t), 70, X(t), 470, '#e5e7eb', 1.5)
    s.t(X(t), 495, ('minus 200' if t < 0 else str(t)), 17, '#4b5563')
s.t(455, 525, 'Temperature in °C', 18, '#1a2b4a', 'bold')
rows = [('K', -200, 1260, 'general purpose'), ('J', -40, 750, 'economical'), ('T', -200, 350, 'low temperature'),
        ('E', -200, 900, 'highest output'), ('N', -200, 1300, 'better stability'), ('S', 0, 1480, 'noble metal'),
        ('R', 0, 1600, 'noble metal'), ('B', 0, 1700, 'highest range')]
cols = ['#ea580c', '#ca8a04', '#0891b2', '#7c3aed', '#16a34a', '#64748b', '#475569', '#334155']
for i, (k, lo, hi, note) in enumerate(rows):
    y = 80 + i * 48
    s.t(60, y + 25, 'Type ' + k, 19, '#1a2b4a', 'bold')
    s.raw(f'<rect x="{X(lo):.0f}" y="{y+6}" width="{X(hi)-X(lo):.0f}" height="30" rx="6" fill="{cols[i]}"/>')
    lab = (('minus ' + str(-lo)) if lo < 0 else str(lo)) + ' to ' + str(hi)
    s.t(X(lo) + 10, y + 28, lab, 17, '#ffffff', 'bold', 'start')
    s.t(X(hi) + 8, y + 28, note, 17, '#4b5563', 'normal', 'start') if X(hi) + 8 + len(note) * 8.5 < 795 else None
fig(slug, 'types-of-thermocouples-temperature-range-chart',
    'types of thermocouples and their ranges bar chart from Type K to Type B',
    'Diagram by Instrumentation Blog comparing thermocouple types K, J, T, E, N, S, R and B by temperature range, from minus 200 °C up to 1700 °C for Type B.',
    'Common Types of Thermocouples and Their Ranges', s.svg())

# selection flowchart
s = S(600, 'Thermocouple selection flowchart by process application')
s.head('Choosing a Thermocouple Type', A2)
qs = [('Above 1400 °C?', 'Type S, R or B', 'glass, steel, lab furnaces'),
      ('Sub zero or cryogenic?', 'Type T', 'food, pharma, cryogenic tanks'),
      ('Continuous high temp?', 'Type N', 'low drift, long life'),
      ('Oxidizing, general use?', 'Type K', 'boilers, furnaces')]
y = 70
for i, (q, ans, why) in enumerate(qs):
    s.dia(210, y + 45, 300, 86, [q], L, size=18)
    s.ar(362, y + 45, 440, y + 45, A); s.t(400, y + 35, 'Yes', 17, A2, 'bold')
    s.box(445, y + 10, 320, 70, [ans, why], '#ffffff', A, size=18)
    if i < 3:
        s.ar(210, y + 89, 210, y + 112); s.t(232, y + 106, 'No', 17, '#4b5563', 'bold')
    y += 115
s.ar(210, y - 26, 210, y - 3); s.t(232, y - 9, 'No', 17, '#4b5563', 'bold')
s.box(60, y, 300, 56, ['Type J (to 750 °C)', 'or Type E for high output'], '#fef3c7', '#1a2b4a', size=17)
s.box(445, y - 4, 320, 64, ['Then check', 'sheath, wire size, accuracy'], '#fef3c7', '#1a2b4a', size=17)
s.ar(362, y + 28, 440, y + 28)
fig(slug, 'types-of-thermocouples-selection-flowchart',
    'thermocouple selection flowchart by process temperature, atmosphere and duty',
    'Diagram by Instrumentation Blog showing how to choose between thermocouple types by temperature, cryogenic duty, continuous operation and atmosphere, then sheath, wire size and accuracy.',
    'Thermocouple Selection Based on Process Application', s.svg())

# ================= 2. Mimic panel =================
slug = 'what-is-a-mimic-panel-types-uses'
A, A2, L = '#047857', '#065f46', '#ecfdf5'
s = S(520, 'Mimic panel construction layers: front surface, LEDs, backplate and mounting in control desk')
s.head('How a Mimic Panel Is Built', A2)
# exploded layers (side view, slanted)
layers = [(120, '#dbeafe', 'Acrylic overlay'), (165, '#ffffff', 'Printed or engraved diagram'),
          (240, '#fef9c3', 'Super bright LEDs'), (310, '#d1d5db', 'Backplate')]
for i, (x, c, lab) in enumerate(layers):
    s.raw(f'<polygon points="{x},90 {x+40},70 {x+40},380 {x},400" fill="{c}" stroke="#1a2b4a" stroke-width="2"/>')
# diagram lines on front layer
s.ln(175, 140, 195, 133, A, 3); s.ln(175, 220, 195, 213, '#dc2626', 3)
for yy in (150, 220, 290):
    s.raw(f'<circle cx="262" cy="{yy}" r="9" fill="#facc15" stroke="#1a2b4a" stroke-width="1.5"/>')
# desk cutout
s.raw(f'<rect x="390" y="80" width="40" height="330" fill="#9ca3af" stroke="#1a2b4a" stroke-width="2"/>')
s.raw('<rect x="390" y="150" width="40" height="190" fill="#ffffff" stroke="#1a2b4a" stroke-width="2" stroke-dasharray="5 4"/>')
s.ln(350, 110, 395, 110, '#1a2b4a', 3); s.ln(350, 370, 395, 370, '#1a2b4a', 3)
s.t(410, 440, 'Desk cutout', 18, '#1a2b4a', 'bold')
s.ar(90, 245, 112, 245, A); s.t(60, 230, 'Operator', 18, A2, 'bold'); s.t(60, 254, 'side', 17, A2)
items = [('Front surface', 'polycarbonate or polyester sheet', 'with acrylic overlay'),
         ('Indicator lighting', 'LEDs readable up to', '100 m away'),
         ('Backplate', 'bakelite, composite, CRCA', 'sheet or aluminum'),
         ('Mounting', 'screws into a cutout', 'in the control desk')]
for i, (h, a, b) in enumerate(items):
    y = 80 + i * 95
    num(s, 480, y + 22, i + 1, A)
    s.t(505, y + 28, h, 19, A2, 'bold', 'start')
    s.t(505, y + 54, a, 17, '#1a2b4a', 'normal', 'start'); s.t(505, y + 76, b, 17, '#1a2b4a', 'normal', 'start')
num(s, 160, 430, 1, A); num(s, 262, 430, 2, A); num(s, 330, 430, 3, A); num(s, 372, 72, 4, A)
s.t(400, 505, 'Simple build, so the panel works for decades with almost no maintenance', 17, '#4b5563')
fig(slug, 'mimic-panel-construction-layers-diagram',
    'mimic panel construction layers with polycarbonate front, LEDs, backplate and desk mounting',
    'Diagram by Instrumentation Blog showing the four parts of a mimic panel: printed or engraved front surface, super bright LEDs, rigid backplate and screw mounting in a desk cutout.',
    'How a Mimic Panel Is Built', s.svg())

s = S(580, 'Fire and gas mimic panel operator response flowchart')
s.head('Fire and Gas Mimic Panel in an Emergency', A2)
steps = [['Detector senses', 'fire or gas'], ['Hazard lamp', 'lights at sensor spot'],
         ['Operator reads', 'the plant layout'], ['Check pumps', 'and foam status']]
x = 25
for i, ls in enumerate(steps):
    s.box(x, 75, 178, 90, ls, L if i % 2 == 0 else '#ffffff', A, size=17)
    if i < 3: s.ar(x + 180, 120, x + 196, 120, A)
    x += 195
s.pl([(700, 167), (700, 205), (400, 205), (400, 222)], A, 2.5)
s.dia(400, 280, 330, 110, ['Action needed?'], '#fef3c7', size=19)
s.pl([(235, 280), (150, 280), (150, 360)], A, 2.5); s.t(190, 268, 'Shut down', 17, A2, 'bold')
s.pl([(565, 280), (650, 280), (650, 360)], A, 2.5); s.t(610, 268, 'Extinguish', 17, A2, 'bold')
s.box(30, 365, 240, 90, ['Shutdown push button', 'trips the plant', 'from the panel'], '#ffffff', A, size=17)
s.box(530, 365, 240, 90, ['Manual extinguish', 'control fires the', 'extinguishing system'], '#ffffff', A, size=17)
s.box(240, 480, 320, 76, ['Guarded critical buttons', 'stop accidental operation'], '#fee2e2', '#b91c1c', size=17)
s.ar(270, 455, 290, 478, '#b91c1c'); s.ar(530, 455, 510, 478, '#b91c1c')
fig(slug, 'mimic-panel-fire-and-gas-response-flowchart',
    'fire and gas mimic panel flowchart from hazard lamp to shutdown or manual extinguish',
    'Diagram by Instrumentation Blog showing how a fire and gas mimic panel is used: hazard lamp, layout reading, pump status, then guarded shutdown or manual extinguish buttons.',
    'Mimic Panel Role in Fire and Gas Safety Systems', s.svg())

s = S(500, 'Physical mimic panel vs software mimic screen comparison infographic')
s.head('Physical Panel vs Software Mimic Screen', A2)
s.box(250, 60, 260, 56, ['Physical panel'], A, A, '#ffffff', size=20)
s.box(525, 60, 260, 56, ['Software screen'], '#1a2b4a', '#1a2b4a', '#ffffff', size=20)
rows = [('Needs power or network', ['No, purely', 'electrical lamps'], ['Yes, workstation', 'and network']),
        ('After a plant change', ['New artwork', 'required'], ['Edited in config', 'software']),
        ('Detail and drill down', ['Fixed, high', 'level view only'], ['Zoom into', 'individual loops']),
        ('Visibility in a room', ['Readable from', '100 meters'], ['Limited by screen', 'size and glare'])]
for i, (f, p, q) in enumerate(rows):
    y = 128 + i * 82
    s.box(15, y, 225, 72, [f], '#f3f4f6', '#9ca3af', size=17)
    s.box(250, y, 260, 72, p, L, A, size=17, bold_first=False)
    s.box(525, y, 260, 72, q, '#eef2ff', '#1a2b4a', size=17, bold_first=False)
s.t(400, 482, 'Most new control rooms pair both: the panel is the always on backup', 18, '#1a2b4a', 'bold')
fig(slug, 'mimic-panel-vs-software-screen-comparison-infographic',
    'mimic panel vs software mimic screen comparison of power, updates, detail and visibility',
    'Diagram by Instrumentation Blog comparing a physical mimic panel with a software mimic screen on power dependence, plant changes, drill down detail and visibility across a room.',
    'Physical Panel vs Software Mimic Screen', s.svg())

# ================= 3. RTD =================
slug = 'what-is-rtd-and-how-it-works'
A, A2, L = '#7c3aed', '#5b21b6', '#f5f3ff'
s = S(530, 'RTD 2 wire, 3 wire and 4 wire wiring diagrams')
s.head('RTD Wiring: 2 Wire, 3 Wire and 4 Wire', A2)
def rtd(s, x, y):
    s.raw(f'<polyline points="{x},{y} {x},{y+10} {x+12},{y+18} {x-12},{y+34} {x+12},{y+50} {x-12},{y+66} {x},{y+74} {x},{y+84}" fill="none" stroke="{A}" stroke-width="3"/>')
cols = [(40, '2 Wire', 2, ['Lead resistance adds', 'to the reading', 'Short cables only']),
        (295, '3 Wire', 3, ['One lead measured', 'and subtracted', 'Industrial standard']),
        (550, '4 Wire', 4, ['Two wires carry I,', 'two measure V', 'Lead error removed'])]
for x, title, n, notes in cols:
    s.raw(f'<rect x="{x}" y="60" width="215" height="400" rx="12" fill="{L}" stroke="{A}" stroke-width="2"/>')
    s.t(x + 107, 92, title, 21, A2, 'bold')
    ex = x + 40; rtd(s, ex, 130); s.t(ex, 245, 'Pt100', 17, A2, 'bold')
    s.raw(f'<rect x="{x+125}" y="110" width="55" height="130" rx="6" fill="#ffffff" stroke="#1a2b4a" stroke-width="2"/>')
    s.t(x + 152, 268, 'Transmitter', 17, '#1a2b4a', 'bold')
    tops = {2: [130], 3: [130], 4: [120, 140]}[n]
    bots = {2: [214], 3: [204, 224], 4: [204, 224]}[n]
    bx = ex + 30
    for node, ys in ((130, tops), (214, bots)):
        s.ln(ex, node, bx, node, '#1a2b4a', 2.2)
        s.ln(bx, min(ys + [node]), bx, max(ys + [node]), '#1a2b4a', 2.2)
        for yy in ys:
            s.ln(bx, yy, x + 125, yy, '#1a2b4a', 2.2)
            s.raw(f'<circle cx="{x+125}" cy="{yy}" r="4" fill="#1a2b4a"/>')
        if len(ys) > 1: s.raw(f'<circle cx="{bx}" cy="{node}" r="4.5" fill="{A}"/>')
    s.t(x + 107, 315, f'{n} leads', 19, '#1a2b4a', 'bold')
    for j, l in enumerate(notes): s.t(x + 107, 360 + j * 30, l, 17, '#1a2b4a')
s.t(400, 500, 'Head mount transmitter: short element distance, 4 to 20 mA out', 18, A2, 'bold')
fig(slug, 'rtd-2-3-4-wire-wiring-diagram',
    'RTD 2 wire 3 wire and 4 wire connection diagram to a temperature transmitter',
    'Diagram by Instrumentation Blog comparing RTD 2 wire, 3 wire and 4 wire connections to a transmitter and how each one handles lead wire resistance error.',
    'RTD Wiring Configurations: 2-Wire, 3-Wire and 4-Wire', s.svg())

s = S(560, 'RTD resistance formula infographic with Pt100 and Pt1000 worked example and graph')
s.head('RTD Resistance Formula', A2)
s.raw(f'<rect x="30" y="60" width="350" height="470" rx="14" fill="{L}" stroke="{A}" stroke-width="2.5"/>')
s.t(205, 105, 'R(T) = R₀ × (1 + α × T)', 22, A2, 'bold')
for j, l in enumerate(['R₀ = 100 Ω for Pt100', 'R₀ = 1000 Ω for Pt1000', 'α = 0.00385 Ω/Ω/°C', 'T in °C, 0 to 400 °C']):
    s.t(55, 150 + j * 30, l, 18, '#1a2b4a', 'normal', 'start')
s.t(205, 300, 'Worked example at 200 °C', 19, A2, 'bold')
for j, l in enumerate(['Pt100: 100 × (1 + 0.00385 × 200)', '= 100 × 1.77 = 177.0 Ω', 'Pt1000: 1000 × 1.77', '= 1770.0 Ω']):
    s.t(55, 340 + j * 32, l, 18, '#1a2b4a', 'bold' if j % 2 else 'normal', 'start')
s.t(205, 500, 'Real table at 200 °C: 175.86 Ω', 17, '#4b5563')
# graph
gx0, gy0, gx1, gy1 = 460, 480, 760, 90
s.ln(gx0, gy0, gx1, gy0, '#1a2b4a', 2); s.ln(gx0, gy0, gx0, gy1, '#1a2b4a', 2)
def GX(t): return gx0 + t / 200 * (gx1 - gx0 - 20)
def GY(r): return gy0 - (r - 80) / 110 * (gy0 - gy1 - 20)
for t in (0, 100, 200): s.t(GX(t), gy0 + 26, str(t), 17, '#4b5563')
for r in (100, 140, 180): s.t(gx0 - 10, GY(r) + 6, str(r), 17, '#4b5563', anchor='end'); s.ln(gx0, GY(r), gx1, GY(r), '#e5e7eb', 1)
s.ln(GX(0), GY(100), GX(200), GY(177), A, 4)
for t, r, lab in [(0, 100, '100 Ω'), (100, 138.5, '138.5 Ω'), (200, 177, '177.0 Ω')]:
    s.raw(f'<circle cx="{GX(t):.0f}" cy="{GY(r):.0f}" r="6" fill="{A2}"/>')
    s.t(GX(t) + (12 if t < 200 else -12), GY(r) - 12, lab, 17, A2, 'bold', 'start' if t < 200 else 'end')
s.t(610, gy0 + 52, 'Temperature in °C', 17, '#1a2b4a', 'bold')
s.t(610, 75, 'Pt100 resistance in Ω', 17, '#1a2b4a', 'bold')
fig(slug, 'rtd-resistance-formula-pt100-infographic',
    'RTD resistance formula with Pt100 at 200 °C worked example and resistance graph',
    'Diagram by Instrumentation Blog showing the RTD formula R equals R0 times 1 plus alpha T, with a Pt100 reading 177.0 ohm and a Pt1000 reading 1770.0 ohm at 200 °C.',
    'RTD Resistance Formula', s.svg())

s = S(600, 'RTD field check flowchart using the Pt100 resistance table')
s.head('Checking an RTD With the Resistance Table', A2)
steps = [['1. Disconnect the RTD', 'from the transmitter'], ['2. Measure resistance', 'across the leads'],
         ['3. For 3 wire, subtract', 'the lead resistance'], ['4. Measure bath temp', 'with a reference']]
for i, ls in enumerate(steps):
    x = 30 + (i % 2) * 390; y = 70 + (i // 2) * 105
    s.box(x, y, 350, 80, ls, L, A, size=18)
s.ar(382, 110, 418, 110, A); s.pl([(605, 152), (605, 162), (205, 162), (205, 172)], A, 2.5)
s.ar(382, 215, 418, 215, A)
s.pl([(605, 257), (605, 272), (400, 272), (400, 285)], A, 2.5)
s.dia(400, 345, 420, 110, ['Matches table value?'], '#fef3c7', size=19)
s.pl([(190, 345), (130, 345), (130, 420)], '#16a34a', 2.5); s.t(165, 333, 'Yes', 17, '#15803d', 'bold')
s.pl([(610, 345), (670, 345), (670, 420)], '#b91c1c', 2.5); s.t(640, 333, 'No', 17, '#b91c1c', 'bold')
s.box(25, 425, 250, 90, ['Sensor is healthy', 'reconnect and', 'return to service'], '#dcfce7', '#16a34a', size=17)
s.box(505, 425, 270, 90, ['Large deviation, open', 'circuit or near zero Ω', 'means damaged element'], '#fee2e2', '#b91c1c', size=17)
s.t(400, 555, 'Pt100 table: 100.00 Ω at 0 °C, 138.51 Ω at 100 °C, 175.86 Ω at 200 °C', 17, A2, 'bold')
s.t(400, 584, 'Pt1000 values are ten times larger', 17, '#4b5563')
fig(slug, 'rtd-field-check-resistance-table-flowchart',
    'how to check a Pt100 RTD with a multimeter and resistance table flowchart',
    'Diagram by Instrumentation Blog showing the field check for a platinum RTD: disconnect, measure, subtract lead resistance, compare with the Pt100 table and judge the element.',
    'Platinum RTD Resistance Table for Pt100 and Pt1000', s.svg())

# ================= 4. Wheatstone bridge =================
slug = 'wheatstone-bridge-10-applications'
A, A2, L = '#1d4ed8', '#1e3a8a', '#eff6ff'
s = S(560, 'Wheatstone bridge circuit with R1 R2 R3 Rx, DC excitation and galvanometer')
s.head('Wheatstone Bridge Circuit', A2)
T, Bm, Lf, Rt = (300, 80), (300, 440), (160, 260), (440, 260)
def res(s, p, q, lab, lx, ly, col='#1a2b4a'):
    (x1, y1), (x2, y2) = p, q
    mx, my = (x1 + x2) / 2, (y1 + y2) / 2
    import math
    ang = math.degrees(math.atan2(y2 - y1, x2 - x1))
    s.ln(x1, y1, x2, y2, '#1a2b4a', 2.5)
    s.raw(f'<rect x="{mx-34}" y="{my-13}" width="68" height="26" fill="#ffffff" stroke="{col}" stroke-width="2.5" transform="rotate({ang:.1f} {mx} {my})"/>')
    s.t(lx, ly, lab, 20, col, 'bold')
res(s, T, Lf, 'R1', 190, 160); res(s, Lf, Bm, 'R2', 190, 375)
res(s, T, Rt, 'R3', 415, 160); res(s, Rt, Bm, 'Rx', 415, 375, '#dc2626')
for p in (T, Bm, Lf, Rt): s.raw(f'<circle cx="{p[0]}" cy="{p[1]}" r="6" fill="#1a2b4a"/>')
s.ln(160, 260, 262, 260, '#1a2b4a', 2.5); s.ln(338, 260, 440, 260, '#1a2b4a', 2.5)
s.raw('<circle cx="300" cy="260" r="36" fill="#fef9c3" stroke="#1a2b4a" stroke-width="2.5"/>'); s.t(300, 268, 'G', 22, '#1a2b4a', 'bold')
s.t(160, 296, 'B', 18, '#1a2b4a', 'bold'); s.t(440, 296, 'D', 18, '#1a2b4a', 'bold')
# battery on left loop
s.pl([(300, 80), (70, 80), (70, 240)], '#1a2b4a', 2.5, arrow=False)
s.pl([(70, 280), (70, 440), (300, 440)], '#1a2b4a', 2.5, arrow=False)
s.ln(50, 240, 90, 240, '#1a2b4a', 3); s.ln(60, 280, 80, 280, '#1a2b4a', 5)
s.t(100, 236, '+', 20, '#1a2b4a', 'bold'); s.t(40, 320, 'VIN', 19, A2, 'bold'); s.t(40, 344, 'DC', 17, '#4b5563')
# side panel
s.raw(f'<rect x="510" y="70" width="270" height="420" rx="14" fill="{L}" stroke="{A}" stroke-width="2"/>')
lines = [('Balance condition', True), ('R1 / R2 = R3 / Rx', False), ('Rx = (R2 × R3) / R1', False), ('', False),
         ('Worked example', True), ('R1 = 100 Ω, R2 = 100 Ω', False), ('R3 = 250 Ω', False), ('Rx = (100 × 250) / 100', False), ('Rx = 250 Ω', True)]
for j, (l, b) in enumerate(lines):
    s.t(645, 110 + j * 40, l, 19 if b else 18, A2 if b else '#1a2b4a', 'bold' if b else 'normal')
s.t(400, 520, 'At balance B and D are at equal voltage, so no current flows through G', 18, '#1a2b4a')
fig(slug, 'wheatstone-bridge-circuit-balance-diagram',
    'Wheatstone bridge circuit diagram with R1, R2, R3, unknown Rx, DC supply and galvanometer',
    'Diagram by Instrumentation Blog of a Wheatstone bridge with known arms R1 and R2, adjustable R3, unknown Rx, DC excitation and galvanometer, with the balance formula worked example.',
    'Wheatstone Bridge Circuit Elements Explained', s.svg())

s = S(560, 'Wheatstone bridge measurement sequence flowchart')
s.head('How a Wheatstone Bridge Measures Resistance', A2)
steps = [['1. Known resistors', 'set the ratio'], ['2. DC excitation', 'energizes bridge'],
         ['3. Compare the', 'two midpoints']]
x = 30
for i, ls in enumerate(steps):
    s.box(x, 70, 225, 84, ls, L, A, size=18)
    if i < 2: s.ar(x + 227, 112, x + 253, 112, A)
    x += 255
s.pl([(652, 156), (652, 185), (400, 185), (400, 200)], A, 2.5)
s.dia(400, 260, 380, 110, ['Ratios match?'], '#fef3c7', size=20)
s.pl([(210, 260), (150, 260), (150, 330)], '#16a34a', 2.5); s.t(180, 248, 'Yes', 17, '#15803d', 'bold')
s.pl([(590, 260), (650, 260), (650, 330)], '#b91c1c', 2.5); s.t(620, 248, 'No', 17, '#b91c1c', 'bold')
s.box(25, 335, 255, 110, ['Balanced: 0 mV', 'no current in G', 'Rx = R2 × R3 / R1'], '#dcfce7', '#16a34a', size=18)
s.box(520, 335, 255, 110, ['Unbalanced', 'small mV appears', 'size shows change'], '#fee2e2', '#b91c1c', size=18)
s.box(300, 350, 200, 80, ['Null mode:', 'adjust R3'], '#ffffff', A, size=17)
s.ar(518, 390, 502, 390, A); s.ar(298, 390, 282, 390, A)
s.box(470, 470, 305, 70, ['4. Amplify the mV signal', 'in sensors (deflection mode)'], L, A, size=17)
s.ar(647, 447, 647, 468, '#b91c1c')
s.t(235, 505, 'Outputs: 0.0 mV balanced, 4.2 and 18.6 mV unbalanced', 17, '#4b5563')
fig(slug, 'wheatstone-bridge-measurement-steps-flowchart',
    'how a Wheatstone bridge measures resistance flowchart with balanced and unbalanced modes',
    'Diagram by Instrumentation Blog showing the Wheatstone bridge measuring sequence: known ratio, DC excitation, midpoint comparison, then null balance or a millivolt output that is amplified.',
    'How a Wheatstone Bridge Measures Resistance', s.svg())

s = S(560, '10 applications of Wheatstone bridge infographic')
s.head('10 Applications of a Wheatstone Bridge', A2)
apps = [('Resistance', 'unknown R by balance'), ('Strain', 'gauges, load cells'), ('Temperature', 'RTDs and thermistors'),
        ('Pressure', 'diaphragm strain to mV'), ('Level', 'sensor deformation'), ('Gas detection', 'resistance change'),
        ('Medical', 'ECG and EEG'), ('Automation', 'transmitters, sensors'), ('Robotics', 'force and torque'),
        ('Automotive', 'pressure, load, temp')]
for i, (h, d) in enumerate(apps):
    x = 30 + (i % 2) * 380; y = 62 + (i // 2) * 96
    s.raw(f'<rect x="{x}" y="{y}" width="360" height="84" rx="12" fill="{L if (i//2+i)%2==0 else "#ffffff"}" stroke="{A}" stroke-width="2"/>')
    num(s, x + 36, y + 42, i + 1, A, 20)
    s.t(x + 70, y + 36, h, 20, A2, 'bold', 'start'); s.t(x + 70, y + 64, d, 18, '#1a2b4a', 'normal', 'start')
fig(slug, 'wheatstone-bridge-applications-infographic',
    'applications of Wheatstone bridge in strain, pressure, temperature, gas and medical sensors',
    'Diagram by Instrumentation Blog listing ten Wheatstone bridge applications, from resistance and strain measurement to pressure transmitters, gas sensors, medical, robotics and automotive sensors.',
    '10 Surprising Applications of a Wheatstone Bridge', s.svg())

if __name__ == '__main__':
    import cairosvg
    out = sys.argv[1] if len(sys.argv) > 1 else None
    for slug, figs in CH.items():
        json.dump({'slug': slug, 'figs': figs}, open(os.path.join(OUT, slug + '.json'), 'w'), ensure_ascii=False, indent=1)
        if out:
            for f in figs: cairosvg.svg2png(bytestring=f['svg'].encode(), write_to=os.path.join(out, f['name'] + '.png'), output_width=800)
    print({k: [f['name'] for f in v] for k, v in CH.items()})
