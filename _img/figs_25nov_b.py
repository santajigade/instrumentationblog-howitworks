import sys; sys.path.insert(0, '/home/claude/instrumentationblog-howitworks/_img'); from figs_24nov_common import *
GREY = '#4b5563'

# ================= 1. DCS =================
slug = 'distributed-control-system-dcs'
A, A2, L = '#0369a1', '#0c4a6e', '#f0f9ff'
s = S(600, 'Distributed control system block diagram with levels 0 to 4')
s.head('Distributed Control System Block Diagram', A2)
lv = [('Level 4', 'Plant management and scheduling', 70, '#0c4a6e'), ('Level 3', 'Production control and coordination', 140, '#075985'),
      ('Level 2', 'Supervisory computers, operator stations', 210, '#0369a1')]
for n, t, y, c in lv:
    s.raw(f'<rect x="150" y="{y}" width="500" height="52" rx="10" fill="{c}"/>')
    s.t(225, y + 33, n, 18, '#ffffff', 'bold'); s.t(460, y + 33, t, 17, '#ffffff')
    if y < 210: s.ln(400, y + 52, 400, y + 70, A2, 3)
s.ln(400, 262, 400, 292, A2, 3)
s.ln(60, 300, 740, 300, '#f59e0b', 6); s.t(400, 290, '', 17)
s.t(70, 288, 'High speed communication bus', 17, '#b45309', 'bold', 'start')
for i, x in enumerate((90, 330, 570)):
    s.ln(x + 70, 300, x + 70, 340, A2, 3)
    s.box(x, 340, 140, 70, [f'Controller {i+1}', 'I/O rack'], L, A, size=17)
    for j, dx in enumerate((20, 70, 120)):
        s.ln(x + dx, 410, x + dx, 450, A2, 2)
        lab = ['TT', 'PT', 'CV'][j]
        if lab == 'CV':
            s.raw(f'<polygon points="{x+dx-12},{462} {x+dx+12},{484} {x+dx+12},{462} {x+dx-12},{484}" fill="#ffffff" stroke="{A2}" stroke-width="2"/>')
        else:
            s.raw(f'<circle cx="{x+dx}" cy="473" r="22" fill="#ffffff" stroke="{A2}" stroke-width="2"/>'); s.t(x + dx, 479, lab, 17, A2, 'bold')
s.raw(f'<rect x="20" y="510" width="760" height="76" rx="10" fill="{L}" stroke="{A}" stroke-width="2"/>')
s.t(400, 540, 'Level 1: controllers and I/O racks.  Level 0: sensors, transducers, actuators', 17, A2, 'bold')
s.t(400, 568, 'If one controller fails, the other stations keep their part of the plant running', 17, '#1a2b4a')
fig(slug, 'distributed-control-system-levels-block-diagram',
    'distributed control system block diagram with field devices, controllers, bus and operator levels',
    'Diagram by Instrumentation Blog showing DCS levels 0 to 4: field devices, controllers with I/O racks on a high speed bus, operator stations, production control and plant management.',
    'Distributed Control System (DCS) Block Diagram', s.svg())

s = S(610, 'Flowchart of a measurement travelling through the DCS levels and back to a valve')
s.head('How a Signal Moves Through the DCS', A2)
up = [('Level 0', 'Sensor measures', 'temperature or flow'), ('Level 1', 'I/O rack reads it,', 'controller runs the loop'), ('Level 2', 'Operator station', 'shows value, alarms')]
dn = [('Level 2', 'Operator changes', 'setpoint if needed'), ('Level 1', 'Controller sends', 'new output'), ('Level 0', 'Actuator moves', 'the valve')]
for i, (lv_, a, b) in enumerate(up):
    y = 450 - i * 140
    s.box(40, y, 300, 96, [lv_, a, b], L if i % 2 == 0 else '#ffffff', A, size=17)
    if i < 2: s.ar(190, y, 190, y - 44, A2, 3)
for i, (lv_, a, b) in enumerate(dn):
    y = 170 + i * 140
    s.box(460, y, 300, 96, [lv_, a, b], L if i % 2 == 0 else '#ffffff', A2, size=17)
    if i < 2: s.ar(610, y + 96, 610, y + 140, A2, 3)
s.ar(340, 218, 458, 218, A2, 3)
s.pl([(610, 546), (610, 566), (190, 566), (190, 550)], A2, 2.5, True, '6 5')
s.t(400, 92, 'Levels 3 and 4 watch production and set schedules,', 17, GREY)
s.t(400, 118, 'they do not drive field devices directly', 17, GREY)
s.t(400, 592, 'process responds, loop repeats', 17, GREY)
fig(slug, 'distributed-control-system-signal-flowchart',
    'flowchart of a signal moving from sensor to controller, operator station and back to a valve',
    'Diagram by Instrumentation Blog tracing a DCS loop: the sensor reading rises through the I/O rack and controller to the operator station, then the output returns to the actuator.',
    'Layers of a Distributed Control System (DCS)', s.svg())

s = S(540, 'Why a distributed control system matters as loop count grows')
s.head('Why a DCS Matters: A Dozen Loops vs 10,000', A2)
s.raw(f'<rect x="30" y="70" width="350" height="230" rx="16" fill="#ffffff" stroke="{A}" stroke-width="2.5"/>')
s.t(205, 112, 'Small wastewater plant', 20, A2, 'bold')
for k in range(12):
    s.raw(f'<circle cx="{95 + (k % 6) * 44}" cy="{160 + (k // 6) * 46}" r="14" fill="{A}"/>')
s.t(205, 272, 'About a dozen loops, staff can manage', 17, '#1a2b4a')
s.raw(f'<rect x="420" y="70" width="350" height="230" rx="16" fill="{L}" stroke="{A2}" stroke-width="2.5"/>')
s.t(595, 112, 'Large refinery', 20, A2, 'bold')
for k in range(150):
    s.raw(f'<circle cx="{445 + (k % 25) * 12.5:.1f}" cy="{140 + (k // 25) * 18}" r="4.5" fill="{A2}"/>')
s.t(595, 272, 'Nearly 10,000 interconnected loops', 17, '#1a2b4a')
adv = ['Control spread over many CPUs', 'One failure does not stop the plant', 'Interlocks changed quickly',
       'Less troubleshooting, easier upkeep', 'Data shown in many formats', 'Shorter engineering time']
for i, a in enumerate(adv):
    x = 30 + (i % 2) * 380; y = 330 + (i // 2) * 64
    s.raw(f'<rect x="{x}" y="{y}" width="360" height="52" rx="10" fill="{L if i % 3 == 0 else "#ffffff"}" stroke="{A}" stroke-width="2"/>')
    num(s, x + 28, y + 26, i + 1, A, 15)
    s.t(x + 54, y + 33, a, 17, '#1a2b4a', 'normal', 'start')
fig(slug, 'distributed-control-system-advantages-infographic',
    'distributed control system advantages and loop count comparison of a small plant and a refinery',
    'Diagram by Instrumentation Blog comparing a wastewater plant with about a dozen loops to a refinery with nearly 10,000, plus six DCS advantages listed in the article.',
    'What Makes the DCS so Important?', s.svg())

# ================= 2. Star vs delta =================
slug = 'star-vs-delta-connection'
A, A2, L = '#16a34a', '#14532d', '#f0fdf4'
D, D2 = '#9333ea', '#581c87'
import math
def coil(s, x1, y1, x2, y2, c, n=4):
    dx, dy = x2 - x1, y2 - y1; ln_ = math.hypot(dx, dy); ux, uy = dx / ln_, dy / ln_; nx, ny = -uy, ux
    a = 0.25; b = 0.75
    p1 = (x1 + dx * a, y1 + dy * a); p2 = (x1 + dx * b, y1 + dy * b)
    s.ln(x1, y1, *p1, c, 3); s.ln(*p2, x2, y2, c, 3)
    seg = ln_ * (b - a) / n; d = f'M{p1[0]:.1f} {p1[1]:.1f}'
    for i in range(n):
        ex, ey = p1[0] + ux * seg * (i + 1), p1[1] + uy * seg * (i + 1)
        cx, cy = p1[0] + ux * seg * (i + 0.5) + nx * 14, p1[1] + uy * seg * (i + 0.5) + ny * 14
        d += f' Q{cx:.1f} {cy:.1f} {ex:.1f} {ey:.1f}'
    s.raw(f'<path d="{d}" fill="none" stroke="{c}" stroke-width="3"/>')
s = S(520, 'Star and delta connection of three windings with line and neutral conductors')
s.head('Star vs Delta Connection of Three Windings', '#1a2b4a')
cx, cy = 200, 260
pts = [(cx, cy - 130), (cx - 115, cy + 75), (cx + 115, cy + 75)]
for p in pts: coil(s, cx, cy, p[0], p[1], A)
s.raw(f'<circle cx="{cx}" cy="{cy}" r="7" fill="{A2}"/>')
s.ln(cx, cy, cx + 150, cy, A2, 2.5, '6 4'); s.t(cx + 160, cy + 6, 'N', 18, A2, 'bold', 'start')
for (x, y), n in zip(pts, ['L1', 'L2', 'L3']):
    s.raw(f'<circle cx="{x}" cy="{y}" r="5" fill="#1a2b4a"/>'); s.t(x + (0 if n == 'L1' else (-26 if n == 'L2' else 26)), y + (-14 if n == 'L1' else 26), n, 18, '#1a2b4a', 'bold')
s.t(200, 420, 'Star (Wye): 4 wire', 20, A2, 'bold'); s.t(200, 450, 'V_Line = √3 × V_Phase', 18, '#1a2b4a'); s.t(200, 478, 'I_Line = I_Phase', 18, '#1a2b4a')
tp = [(600, 120), (480, 335), (720, 335)]
for i in range(3): coil(s, *tp[i], *tp[(i + 1) % 3], D)
for (x, y), n in zip(tp, ['L1', 'L2', 'L3']):
    s.raw(f'<circle cx="{x}" cy="{y}" r="6" fill="#1a2b4a"/>'); s.t(x + (0 if n == 'L1' else (-30 if n == 'L2' else 30)), y + (-14 if n == 'L1' else 8), n, 18, '#1a2b4a', 'bold')
s.t(600, 420, 'Delta: 3 wire, no neutral', 20, D2, 'bold'); s.t(600, 450, 'V_Line = V_Phase', 18, '#1a2b4a'); s.t(600, 478, 'I_Line = √3 × I_Phase', 18, '#1a2b4a')
s.ln(400, 70, 400, 490, '#e5e7eb', 2)
fig(slug, 'star-vs-delta-connection-winding-diagram',
    'star vs delta connection of three windings with neutral point and closed triangle',
    'Diagram by Instrumentation Blog comparing a star connection, windings joined at a neutral point for a 4 wire system, with a delta loop that has no neutral.',
    'What is Star and Delta Connection?', s.svg())

s = S(560, 'Flowchart for choosing star or delta connection')
s.head('Star or Delta? A Quick Decision Path', '#1a2b4a')
s.dia(400, 112, 360, 96, ['Need a neutral and both', 'phase and line voltage?'], '#ffffff', A, size=18)
s.ar(220, 112, 180, 112); s.t(200, 98, 'Yes', 17, A2, 'bold')
s.box(14, 72, 166, 80, ['Star', '230 V and 400 V'], A, A2, '#ffffff', size=18)
s.ar(400, 160, 400, 190); s.t(420, 180, 'No', 17, '#1a2b4a', 'bold', 'start')
s.dia(400, 240, 360, 96, ['Motor needs lower', 'starting current?'], '#ffffff', '#1a2b4a', size=18)
s.ar(220, 240, 180, 240); s.t(200, 226, 'Yes', 17, A2, 'bold')
s.box(14, 196, 166, 88, ['Start in star,', 'run in delta', '58 % voltage'], L, A, size=17)
s.ar(400, 288, 400, 318); s.t(420, 308, 'No', 17, '#1a2b4a', 'bold', 'start')
s.dia(400, 368, 360, 96, ['Ride through a winding', 'fault or trap harmonics?'], '#ffffff', D, size=18)
s.ar(580, 368, 622, 368); s.t(601, 354, 'Yes', 17, D2, 'bold')
s.box(622, 328, 160, 80, ['Delta', '3 wire'], D, D2, '#ffffff', size=18)
s.ar(400, 416, 400, 446); s.t(420, 436, 'No', 17, '#1a2b4a', 'bold', 'start')
s.box(220, 446, 360, 64, ['Check machine nameplate', 'and supply system'], '#ffffff', '#1a2b4a', size=18)
s.t(400, 540, 'A delta system can still deliver about two thirds capacity on two windings', 17, GREY)
fig(slug, 'star-vs-delta-connection-selection-flowchart',
    'flowchart to choose star or delta connection for distribution, motor starting or resilience',
    'Diagram by Instrumentation Blog guiding the choice: star when a neutral and dual voltage are needed, star then delta for motor starting, delta for resilience and harmonics.',
    'Applications', s.svg())

s = S(540, 'Phasor diagram showing why star line voltage is root 3 times phase voltage')
s.head('Why V_Line = √3 × V_Phase in Star', '#1a2b4a')
ox, oy, R = 230, 300, 150
ang = {'V1': 90, 'V2': -30, 'V3': 210}
for k, a in ang.items():
    x = ox + R * math.cos(math.radians(a)); y = oy - R * math.sin(math.radians(a))
    s.ar(ox, oy, x, y, A, 3.5)
    s.t(x + (0 if k == 'V1' else (30 if k == 'V2' else -30)), y + (-12 if k == 'V1' else 24), k, 18, A2, 'bold')
x1 = ox + R * math.cos(math.radians(90)); y1 = oy - R * math.sin(math.radians(90))
x2 = ox + R * math.cos(math.radians(-30)); y2 = oy - R * math.sin(math.radians(-30))
s.ar(x2, y2, x1, y1, D, 3.5)
s.t((x1 + x2) / 2 + 42, (y1 + y2) / 2 - 6, 'V12', 18, D2, 'bold')
s.raw(f'<path d="M{ox:.1f} {oy-34:.1f} A34 34 0 0 0 {ox-34*math.cos(math.radians(30)):.1f} {oy+17:.1f}" fill="none" stroke="{GREY}" stroke-width="2"/>')
s.t(ox - 44, oy - 22, '120°', 17, GREY, 'bold', 'end')
s.raw(f'<rect x="430" y="80" width="340" height="200" rx="14" fill="{L}" stroke="{A}" stroke-width="2"/>')
s.t(600, 116, 'Worked example, star', 19, A2, 'bold')
s.t(600, 156, 'V_Phase = 230 V', 18, '#1a2b4a')
s.t(600, 192, 'V_Line = √3 × 230', 18, '#1a2b4a')
s.t(600, 230, '= 398.4 V ≈ 400 V', 22, A2, 'bold')
s.t(600, 262, 'two phasors 120° apart', 17, GREY)
s.raw(f'<rect x="430" y="300" width="340" height="190" rx="14" fill="#faf5ff" stroke="{D}" stroke-width="2"/>')
s.t(600, 336, 'Star delta starting', 19, D2, 'bold')
s.t(600, 376, 'Each winding in star sees', 18, '#1a2b4a')
s.t(600, 408, '1 ÷ √3 of delta voltage', 18, '#1a2b4a')
s.t(600, 446, '≈ 58 %', 24, D2, 'bold')
s.t(230, 500, 'V12 is the vector difference of V1 and V2', 17, GREY)
fig(slug, 'star-vs-delta-connection-phasor-infographic',
    'phasor diagram showing star line voltage is root 3 times phase voltage',
    'Diagram by Instrumentation Blog drawing the star phasors 120 degrees apart, the 230 V to 398.4 V worked example and the 58 percent winding voltage in star delta starting.',
    'Formulas', s.svg())

# ================= 3. Fire alarm system =================
slug = 'how-a-fire-alarm-system-works'
A, A2, L = '#ea580c', '#7c2d12', '#fff7ed'
s = S(560, 'Fire alarm system block diagram with input devices, control panel and outputs')
s.head('Fire Alarm System: Detect, Decide, Respond', A2)
ins = ['Smoke detector', 'Heat detector', 'Flame detector', 'Gas detector', 'Manual call point']
for i, n in enumerate(ins):
    y = 74 + i * 80
    s.box(20, y, 200, 60, [n], L, A, size=17)
    s.pl([(220, y + 30), (262, y + 30), (262, 280), (300, 280)], A2, 2, False)
s.ar(262, 280, 298, 280, A2, 2.5)
s.box(300, 190, 200, 180, ['FACP', 'control panel', 'checks signal', 'shows zone', 'sends commands'], A, A2, '#ffffff', size=18)
outs = [('Hooter', 'loud siren'), ('Beacon, strobe', 'visual warning'), ('Sprinklers', 'water on fire'), ('Gas suppression', 'CO2, clean agent'), ('ECR, fire service', 'remote alert')]
for i, (n, d) in enumerate(outs):
    y = 74 + i * 80
    s.box(580, y, 200, 60, [n, d], '#ffffff', A2, size=17)
    s.pl([(500, 280), (540, 280), (540, y + 30), (576, y + 30)], A2, 2, True)
s.t(120, 500, 'Input devices', 19, A, 'bold'); s.t(400, 500, 'Brain', 19, A2, 'bold'); s.t(680, 500, 'Output devices', 19, A2, 'bold')
s.t(400, 536, 'Detect the fire early, warn people, start fire fighting', 17, GREY)
fig(slug, 'fire-alarm-system-block-diagram',
    'fire alarm system block diagram with detectors, control panel FACP and output devices',
    'Diagram by Instrumentation Blog showing smoke, heat, flame and gas detectors and call points feeding the FACP, which drives hooters, beacons, sprinklers, gas suppression and the ECR.',
    'Main Parts of a Fire Alarm System', s.svg())

s = S(600, 'Flowchart of what the fire alarm control panel does after a detector signal')
s.head('What the FACP Does When a Detector Trips', A2)
s.box(250, 56, 300, 56, ['Detector or call point signal'], L, A, size=18)
s.ar(400, 112, 400, 132)
s.dia(400, 186, 320, 104, ['Real fire or', 'false alarm?'], '#ffffff', A, size=18)
s.ar(240, 186, 184, 186); s.t(212, 172, 'False', 17, GREY, 'bold')
s.box(14, 150, 170, 72, ['Not a real fire,', 'filtered out'], '#ffffff', GREY, size=17)
s.ar(400, 238, 400, 262); s.t(420, 256, 'Real', 17, A2, 'bold', 'start')
s.box(250, 262, 300, 56, ['Show zone or room on panel'], L, A, size=18)
s.ar(400, 318, 400, 340)
s.box(250, 340, 300, 56, ['Sound hooters, flash beacons'], A, A2, '#ffffff', size=18)
s.ar(400, 396, 400, 418)
s.box(250, 418, 300, 56, ['Start suppression system'], A, A2, '#ffffff', size=18)
s.ar(400, 474, 400, 496)
s.box(250, 496, 300, 56, ['Notify ECR and fire service'], A2, A2, '#ffffff', size=18)
s.box(590, 300, 190, 160, ['Suppression', 'sprinklers', 'deluge', 'fire water pumps', 'gas system'], '#ffffff', A, size=17)
s.ar(550, 446, 588, 420, A, 2)
fig(slug, 'fire-alarm-system-control-panel-flowchart',
    'flowchart of fire alarm control panel steps from detector signal to alarms and suppression',
    'Diagram by Instrumentation Blog following the FACP sequence: check the signal, show the zone, sound alarms, start suppression and notify the emergency control room.',
    'B) Control Panel – The Brain of the Fire Alarm System', s.svg())

s = S(580, 'Which fire detector suits which fire or location')
s.head('Choosing the Right Fire Detector', A2)
rows = [('Ionization smoke', 'Fast burning, flaming fires', 'senses small smoke particles'),
        ('Photoelectric smoke', 'Slow, smoldering fires', 'fewer false alarms'),
        ('UV flame', 'Explosions, fast fires', 'very fast response'),
        ('IR flame', 'Dusty or smoky areas', 'sees flame flicker'),
        ('Heat detector', 'Kitchens, workshops, dust', 'trips above preset limit'),
        ('Gas detector', 'Flammable or toxic gas', 'alerts before a fire starts')]
s.raw(f'<rect x="20" y="62" width="760" height="48" fill="{A2}"/>')
s.t(130, 93, 'Detector', 18, '#ffffff', 'bold'); s.t(400, 93, 'Best for', 18, '#ffffff', 'bold'); s.t(650, 93, 'Why', 18, '#ffffff', 'bold')
for i, (a, b, c) in enumerate(rows):
    y = 110 + i * 70
    s.raw(f'<rect x="20" y="{y}" width="760" height="70" fill="{L if i % 2 == 0 else "#ffffff"}" stroke="#fed7aa"/>')
    s.t(130, y + 42, a, 18, A, 'bold'); s.t(400, y + 42, b, 17, '#1a2b4a'); s.t(650, y + 42, c, 17, GREY)
s.t(400, 556, 'Combined UV and IR detectors are used to avoid false alarms', 17, A2, 'bold')
fig(slug, 'fire-alarm-system-detector-selection-infographic',
    'fire alarm system detector selection chart for smoke, flame, heat and gas detectors',
    'Diagram by Instrumentation Blog matching each detector to the fires or places it suits, from ionization and photoelectric smoke detectors to UV, IR, heat and gas detectors.',
    'A) Input Devices – How the System Detects Fire', s.svg())

# ================= 4. Nuclear level measurement =================
slug = 'types-of-nuclear-level-measurement'
A, A2, L = '#65a30d', '#365314', '#f7fee7'
Y = '#eab308'
s = S(560, 'Nuclear level measurement with gamma source, vessel and detector outside the vessel')
s.head('How Nuclear Level Measurement Works', A2)
vx, vw, vt, vb = 290, 220, 80, 480
lev = 290
s.raw(f'<rect x="{vx}" y="{lev}" width="{vw}" height="{vb-lev}" fill="#bfdbfe"/>')
s.raw(f'<rect x="{vx}" y="{vt}" width="{vw}" height="{vb-vt}" rx="20" fill="none" stroke="#334155" stroke-width="8"/>')
s.t(400, lev + 100, 'Process', 18, '#1e3a8a', 'bold')
s.ln(vx + 8, lev, vx + vw - 8, lev, '#1e40af', 3)
# source housing
s.raw(f'<rect x="120" y="230" width="110" height="120" rx="10" fill="#475569"/>')
s.raw(f'<circle cx="210" cy="290" r="10" fill="{Y}"/>')
s.t(175, 380, 'Source in', 17, '#334155', 'bold'); s.t(175, 402, 'shielded housing', 17, '#334155', 'bold')
# beams
for yy in range(110, 471, 40):
    absorbed = yy > lev
    s.ln(220, 290, 600, yy, Y if not absorbed else '#fde68a', 2.5 if not absorbed else 1.5, None if not absorbed else '5 5')
# detector
s.raw(f'<rect x="600" y="100" width="40" height="380" rx="8" fill="{A}" stroke="{A2}" stroke-width="2.5"/>')
s.t(660, 260, 'Detector', 18, A2, 'bold', 'start'); s.t(660, 284, 'strip', 18, A2, 'bold', 'start')
s.box(656, 360, 130, 54, ['4 to 20 mA', 'level signal'], '#ffffff', A2, size=17)
s.t(110, 130, 'Above the liquid:', 17, '#a16207', 'bold', 'start'); s.t(110, 154, 'rays pass', 17, '#a16207', 'normal', 'start')
s.t(400, 520, 'Higher level absorbs more gamma, so less reaches the detector', 18, '#1a2b4a', 'bold')
s.t(400, 546, 'Source and detector are both outside the vessel, nothing touches the process', 17, GREY)
fig(slug, 'nuclear-level-measurement-working-principle-diagram',
    'nuclear level measurement with shielded gamma source and detector strip outside the vessel',
    'Diagram by Instrumentation Blog showing gamma rays from a shielded source crossing the vessel: liquid absorbs part of them, so the detector strip sees less radiation as level rises.',
    'How Nuclear Level Measurement Works', s.svg())

s = S(580, 'Flowchart for deciding when to choose nuclear level measurement')
s.head('When to Choose Nuclear Level Measurement', A2)
qs = [['Do process conditions', 'destroy normal sensors?'], ['Is vessel penetration', 'not allowed?'], ['Is maintenance access', 'difficult or unsafe?']]
for i, q in enumerate(qs):
    cy = 110 + i * 130
    s.dia(300, cy, 340, 96, q, '#ffffff', A, size=17)
    s.ln(470, cy, 500, cy, A2, 2.5); s.t(485, cy - 12, 'Yes', 17, A2, 'bold')
    if i < 2: s.ar(300, cy + 48, 300, cy + 82); s.t(320, cy + 72, 'No', 17, GREY, 'bold', 'start')
s.pl([(500, 110), (500, 370)], A2, 2.5, False)
s.ar(300, 418, 300, 450); s.t(320, 440, 'No', 17, GREY, 'bold', 'start')
s.box(150, 450, 300, 70, ['Use radar, ultrasonic,', 'DP or displacer first'], '#ffffff', GREY, size=17)
s.dia(650, 250, 260, 120, ['Licensing and', 'approvals', 'manageable?'], L, A2, size=17)
s.ar(500, 250, 518, 250, A2, 2.5)
s.ar(650, 310, 650, 380); s.t(670, 348, 'Yes', 17, A2, 'bold', 'start')
s.box(540, 380, 220, 80, ['Nuclear level', 'measurement'], A, A2, '#ffffff', size=19)
s.t(400, 556, 'Not the first choice, but often the best final choice', 17, A2, 'bold')
fig(slug, 'nuclear-level-measurement-selection-flowchart',
    'flowchart for when to choose nuclear level measurement over conventional level sensors',
    'Diagram by Instrumentation Blog turning the article checklist into a decision path: harsh conditions, no penetration or unsafe access, plus manageable licensing, point to nuclear level.',
    'When Should You Choose Nuclear Level Measurement?', s.svg())

s = S(560, 'Four types of nuclear level measurement and what each one measures')
s.head('4 Types of Nuclear Level Measurement', A2)
def mini(x, y, kind):
    s.raw(f'<rect x="{x+70}" y="{y}" width="90" height="150" rx="10" fill="none" stroke="#334155" stroke-width="4"/>')
    if kind == 'interface':
        s.raw(f'<rect x="{x+72}" y="{y+50}" width="86" height="45" fill="#fde68a"/><rect x="{x+72}" y="{y+95}" width="86" height="53" fill="#bfdbfe"/>')
    elif kind == 'density':
        s.raw(f'<rect x="{x+72}" y="{y+2}" width="86" height="146" fill="#d6d3d1"/>')
    else:
        s.raw(f'<rect x="{x+72}" y="{y+70}" width="86" height="78" fill="#bfdbfe"/>')
    if kind != 'point': s.raw(f'<rect x="{x+20}" y="{y+60}" width="34" height="34" rx="5" fill="#475569"/><circle cx="{x+48}" cy="{y+77}" r="5" fill="{Y}"/>')
    if kind == 'point':
        s.ln(x + 54, y + 50, x + 176, y + 50, Y, 3); s.raw(f'<rect x="{x+176}" y="{y+36}" width="20" height="28" rx="4" fill="{A}"/>')
        s.raw(f'<rect x="{x+20}" y="{y+33}" width="34" height="34" rx="5" fill="#475569"/><circle cx="{x+48}" cy="{y+50}" r="5" fill="{Y}"/>')
    elif kind == 'continuous':
        for yy in (y + 10, y + 50, y + 100, y + 140): s.ln(x + 54, y + 77, x + 176, yy, Y, 2)
        s.raw(f'<rect x="{x+176}" y="{y}" width="20" height="150" rx="4" fill="{A}"/>')
    elif kind == 'density':
        s.ln(x + 54, y + 77, x + 176, y + 77, Y, 3); s.raw(f'<rect x="{x+176}" y="{y+62}" width="20" height="30" rx="4" fill="{A}"/>')
    else:
        for yy in (y + 40, y + 75, y + 110): s.ln(x + 54, y + 77, x + 176, yy, Y, 2)
        s.raw(f'<rect x="{x+176}" y="{y+30}" width="20" height="90" rx="4" fill="{A}"/>')
cards = [('Point level', 'High or low alarm,', 'safety interlock', 'point'), ('Continuous level', 'Full vessel height', 'as 4 to 20 mA', 'continuous'),
         ('Density', 'Liquids or slurries', 'from attenuation', 'density'), ('Interface', 'Two layer boundary', 'like oil and water', 'interface')]
for i, (t, a, b, k) in enumerate(cards):
    x = 20 + (i % 2) * 390; y = 62 + (i // 2) * 246
    s.raw(f'<rect x="{x}" y="{y}" width="370" height="232" rx="14" fill="{L}" stroke="{A}" stroke-width="2"/>')
    mini(x, y + 20, k)
    s.t(x + 283, y + 70, t, 19, A2, 'bold'); s.t(x + 283, y + 110, a, 17, '#1a2b4a'); s.t(x + 283, y + 136, b, 17, '#1a2b4a')
fig(slug, 'nuclear-level-measurement-types-infographic',
    'nuclear level measurement types: point level, continuous level, density and interface',
    'Diagram by Instrumentation Blog sketching source and detector layouts for point, continuous, density and interface nuclear measurement with what each one reports.',
    'Types of Nuclear Level Measurement', s.svg())

# ================= 5. Bimetallic thermometer =================
slug = 'bimetallic-thermometer-working-principle'
A, A2, L = '#b91c1c', '#7f1d1d', '#fef2f2'
s = S(600, 'Bimetallic thermometer labelled diagram from dial to stem tip')
s.head('Bimetallic Thermometer Diagram, Label by Label', A2)
cx = 300
s.raw(f'<circle cx="{cx}" cy="150" r="88" fill="#f8fafc" stroke="#475569" stroke-width="6"/>')
s.raw(f'<circle cx="{cx}" cy="150" r="74" fill="#ffffff" stroke="#cbd5e1" stroke-width="2"/>')
import math
for k in range(11):
    a = math.radians(225 - k * 27)
    s.ln(cx + 62 * math.cos(a), 150 - 62 * math.sin(a), cx + 72 * math.cos(a), 150 - 72 * math.sin(a), '#475569', 2.5)
s.ln(cx, 150, cx + 48, 118, A, 4); s.raw(f'<circle cx="{cx}" cy="150" r="7" fill="{A2}"/>')
s.raw(f'<rect x="{cx-26}" y="238" width="52" height="34" fill="#94a3b8" stroke="#475569" stroke-width="2"/>')
for yy in range(276, 300, 6): s.ln(cx - 22, yy, cx + 22, yy, '#475569', 2)
s.raw(f'<rect x="{cx-12}" y="300" width="24" height="270" fill="#e2e8f0" stroke="#475569" stroke-width="2.5"/>')
s.ln(cx, 160, cx, 470, '#1a2b4a', 2)
d = f'M{cx} 470'
for i in range(8):
    y0 = 470 + i * 11
    d += f' Q{cx+10} {y0+3} {cx} {y0+5.5} Q{cx-10} {y0+8} {cx} {y0+11}'
s.raw(f'<path d="{d}" fill="none" stroke="{A}" stroke-width="3"/>')
s.raw(f'<rect x="{cx-10}" y="558" width="20" height="10" fill="#1a2b4a"/>')
labs = [(118, 'Pointer', cx + 40, 122), (178, 'Dial, scale and case', cx + 76, 178), (254, 'Connection fitting', cx + 28, 254),
        (360, 'Stem, 6 or 8 mm stainless', cx + 14, 360), (420, 'Central shaft', cx + 2, 420), (505, 'Bimetal helix', cx + 12, 505), (562, 'Fixed end at stem tip', cx + 12, 562)]
for y, t, x0, y0 in labs:
    s.ln(x0, y0, 470, y, '#94a3b8', 1.5); s.raw(f'<circle cx="{x0}" cy="{y0}" r="3.5" fill="{A2}"/>')
    s.t(478, y + 6, t, 18, A2, 'bold', 'start')
s.t(110, 470, 'Heat enters', 17, A, 'bold'); s.t(110, 494, 'at the tip', 17, A, 'bold')
s.ar(150, 520, 282, 520, A, 2)
fig(slug, 'bimetallic-thermometer-labelled-parts-diagram',
    'bimetallic thermometer labelled diagram with pointer, dial, stem, shaft and bimetal helix',
    'Diagram by Instrumentation Blog labelling a dial thermometer from top to tip: pointer, dial and case, connection, stainless stem, central shaft, bimetal helix and fixed end.',
    'Bimetallic Thermometer Diagram Explained Label by Label', s.svg())

s = S(580, 'Flowchart for specifying a bimetallic thermometer')
s.head('Specifying a Bimetallic Thermometer', A2)
s.dia(400, 110, 340, 92, ['Must the reading', 'reach the DCS?'], '#ffffff', A, size=18)
s.ar(570, 110, 610, 110); s.t(590, 96, 'Yes', 17, A2, 'bold')
s.box(612, 74, 170, 72, ['Use a temperature', 'transmitter'], '#ffffff', GREY, size=17)
s.ar(400, 156, 400, 180); s.t(420, 172, 'No, local dial', 17, A2, 'bold', 'start')
s.box(220, 180, 360, 56, ['Pick range with normal value mid scale'], L, A, size=17)
s.ar(400, 236, 400, 256)
s.dia(400, 304, 340, 92, ['Pumps or compressors', 'shaking the pointer?'], '#ffffff', A, size=18)
s.ar(570, 304, 610, 304); s.t(590, 290, 'Yes', 17, A2, 'bold')
s.box(612, 264, 170, 80, ['Silicone fill,', 'case below 250 °C'], A, A2, '#ffffff', size=17)
s.ar(400, 350, 400, 374); s.t(420, 366, 'No', 17, A2, 'bold', 'start')
s.box(220, 374, 360, 56, ['Mount in a thermowell'], L, A, size=18)
s.ar(400, 430, 400, 450)
s.box(220, 450, 360, 64, ['Stem long enough to fully', 'immerse the helix'], A2, A2, '#ffffff', size=17)
s.pl([(697, 344), (697, 402), (582, 402)], A2, 2.5)
s.t(400, 552, 'Check class 1 or 2 to EN 13190 and verify yearly in a dry block', 17, GREY)
fig(slug, 'bimetallic-thermometer-specification-flowchart',
    'flowchart for specifying a bimetallic thermometer range, silicone filling, thermowell and stem',
    'Diagram by Instrumentation Blog walking through the article advice: transmitter for remote signals, mid scale range, silicone fill for vibration, a thermowell and full helix immersion.',
    'Bimetallic Thermometer Standards and Accuracy Classes', s.svg())

s = S(560, 'Deflection of a straight bimetal strip worked example')
s.head('Straight Strip Deflection: Brass on Invar', A2)
s.raw(f'<rect x="60" y="100" width="40" height="120" fill="#475569"/>')
s.raw(f'<rect x="100" y="146" width="300" height="10" fill="#f59e0b"/><rect x="100" y="156" width="300" height="10" fill="#94a3b8"/>')
s.raw(f'<path d="M100 146 Q260 146 395 170 L393 180 Q260 156 100 156 Z" fill="#f59e0b" opacity="0.45"/>')
s.raw(f'<path d="M100 156 Q260 156 393 180 L391 190 Q260 166 100 166 Z" fill="#94a3b8" opacity="0.45"/>')
s.ln(412, 152, 412, 186, A, 2.5); s.t(422, 176, 'δ', 20, A, 'bold', 'start')
s.t(250, 214, 'Brass on top, 19 ppm/K', 17, '#b45309', 'bold'); s.t(250, 238, 'Invar below, 1.2 ppm/K', 17, '#475569', 'bold')
s.t(250, 90, 'Heated: curls toward the low expansion Invar', 17, GREY)
s.raw(f'<rect x="470" y="80" width="310" height="160" rx="14" fill="{L}" stroke="{A}" stroke-width="2"/>')
for i, t_ in enumerate(['ΔT = 100 K', 't = 1 mm total', 'L = 50 mm free length', 'equal layers and modulus']):
    s.t(625, 116 + i * 34, t_, 18 if i < 3 else 17, '#1a2b4a' if i < 3 else GREY)
s.raw(f'<rect x="20" y="270" width="760" height="190" rx="14" fill="#ffffff" stroke="{A2}" stroke-width="2"/>')
s.t(400, 308, '1/R = 3 × (α1 − α2) × ΔT ÷ (2 × t)', 20, A2, 'bold')
s.t(400, 344, '= 3 × 0.0000178 × 100 ÷ 2 = 0.00267 per mm, R = 374.5 mm', 18, '#1a2b4a')
s.t(400, 390, 'δ ≈ L² ÷ (2 × R)', 20, A2, 'bold')
s.t(400, 426, '= 2500 ÷ (2 × 374.5) = 3.34 mm', 20, A, 'bold')
s.t(400, 500, 'Only 3.34 mm for a 100 K rise, so real gauges coil a long strip', 18, '#1a2b4a', 'bold')
s.t(400, 528, 'into a helix that turns the pointer', 18, '#1a2b4a', 'bold')
fig(slug, 'bimetallic-thermometer-strip-deflection-infographic',
    'bimetallic thermometer strip deflection worked example, brass on Invar, 3.34 mm at 100 K',
    'Diagram by Instrumentation Blog working the article example: brass on Invar, 1 mm thick and 50 mm long, curls to R 374.5 mm and deflects 3.34 mm for a 100 K rise.',
    'Deflection of a Straight Bimetal Strip', s.svg())

if __name__ == '__main__': main()
