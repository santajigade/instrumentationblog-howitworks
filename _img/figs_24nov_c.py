import sys; sys.path.insert(0, '/home/claude/instrumentationblog-howitworks/_img'); from figs_24nov_common import *

GRN, RED, AMB = '#16a34a', '#dc2626', '#d97706'

def spring_v(s, cx, y1, y2, c='#4b5563'):
    n = 6; h = (y2 - y1) / n; pts = [(cx, y1)]
    for i in range(n): pts.append((cx + (12 if i % 2 == 0 else -12), y1 + h * (i + 0.5)))
    pts.append((cx, y2)); s.pl(pts, c, 3, False)

# ================= 1. Fail safe valve =================
slug = 'fail-safe-valve-position-fail-open-fail-closed-fail-locked'
A, A2, L = '#dc2626', '#991b1b', '#fef2f2'
s = S(580, 'Fail safe valve actuator diagram showing spring return fail open, fail closed and lock up relay fail locked')
s.head('How the Actuator Sets the Fail Safe Position', A2)
panels = [('FO, Fail Open', 'ATC actuator', GRN, 'fo'), ('FC, Fail Closed', 'ATO actuator', RED, 'fc'), ('FL, Fail Locked', 'Piston and lock up relay', AMB, 'fl')]
texts = {'fo': ['Air lost: spring pushes', 'stem up off the seat', 'Valve goes OPEN'],
         'fc': ['Air lost: spring pushes', 'stem down onto seat', 'Valve goes CLOSED'],
         'fl': ['Air lost: relay traps air', 'on both piston sides', 'Valve STAYS PUT']}
for i, (ttl, sub, c, k) in enumerate(panels):
    x0 = 20 + i * 260; cx = x0 + 120
    s.raw(f'<rect x="{x0}" y="56" width="240" height="508" rx="14" fill="#ffffff" stroke="{c}" stroke-width="2.5"/>')
    s.t(cx, 88, ttl, 21, c, 'bold'); s.t(cx, 114, sub, 17, '#4b5563')
    # actuator housing
    fill_up = '#fde68a' if k == 'fl' else '#ffffff'
    s.raw(f'<rect x="{cx-80}" y="130" width="160" height="80" rx="16" fill="{fill_up}" stroke="#1a2b4a" stroke-width="2.5"/>')
    s.ln(cx - 78, 170, cx + 78, 170, A if k != 'fl' else '#1a2b4a', 5)
    if k == 'fc':
        spring_v(s, cx, 134, 168)
        s.ar(cx + 40, 140, cx + 40, 166, '#4b5563', 2.5)
    elif k == 'fo':
        spring_v(s, cx, 172, 208)
        s.ar(cx + 40, 204, cx + 40, 176, '#4b5563', 2.5)
    # air port with cross
    if k in ('fo', 'fc'):
        py = 150 if k == 'fo' else 192
        s.ln(cx + 80, py, cx + 108, py, '#2563eb', 3)
        s.ln(cx + 94, py - 8, cx + 108, py + 8, RED, 3); s.ln(cx + 94, py + 8, cx + 108, py - 8, RED, 3)
        s.t(cx - 50, 154 if k == 'fc' else 196, 'air', 17, '#2563eb', 'bold')
    else:
        s.raw(f'<rect x="{cx+35}" y="222" width="80" height="60" rx="8" fill="#fff7e6" stroke="{AMB}" stroke-width="2"/>')
        s.t(cx + 75, 247, 'Lock up', 17, '#1a2b4a', 'bold'); s.t(cx + 75, 270, 'relay', 17, '#1a2b4a', 'bold')
        s.pl([(cx + 100, 222), (cx + 100, 150), (cx + 80, 150)], '#2563eb', 3, False)
        s.pl([(cx + 88, 222), (cx + 88, 192), (cx + 80, 192)], '#2563eb', 3, False)
        s.t(cx - 40, 156, 'trapped', 17, '#92400e', 'bold'); s.t(cx - 40, 198, 'trapped', 17, '#92400e', 'bold')
    # bonnet and stem
    s.raw(f'<rect x="{cx-22}" y="262" width="44" height="36" rx="4" fill="#e5e7eb" stroke="#1a2b4a" stroke-width="2"/>')
    pb = {'fo': 334, 'fc': 368, 'fl': 352}[k]
    # body
    s.raw(f'<rect x="{cx-95}" y="298" width="190" height="112" rx="22" fill="{L}" stroke="#1a2b4a" stroke-width="2.5"/>')
    s.ln(cx, 210, cx, pb - 22, '#1a2b4a', 5)
    s.ln(cx - 70, 370, cx - 20, 370, '#1a2b4a', 7); s.ln(cx + 20, 370, cx + 70, 370, '#1a2b4a', 7)
    s.raw(f'<path d="M{cx-26} {pb-22} L{cx+26} {pb-22} L{cx+16} {pb} L{cx-16} {pb} Z" fill="{c}" stroke="#1a2b4a" stroke-width="2"/>')
    if k != 'fc':
        s.ar(cx - 8, 395, cx - 8, 376, c, 2.5) if False else None
        s.pl([(cx - 85, 392), (cx - 30, 392)], c, 3, True); s.pl([(cx + 30, 392), (cx + 85, 392)], c, 3, True)
    else:
        s.t(cx, 398, 'no flow', 17, RED, 'bold')
    for j, ln_ in enumerate(texts[k]): s.t(cx, 446 + j * 26, ln_, 17, '#1a2b4a', 'bold' if j == 2 else 'normal')
    ex = {'fo': 'Example: cooling water', 'fc': 'Example: fuel gas', 'fl': 'Not for SIS duty'}[k]
    s.raw(f'<rect x="{x0+15}" y="516" width="210" height="36" rx="8" fill="{c}"/>')
    s.t(cx, 540, ex, 17, '#ffffff', 'bold')
fig(slug, 'fail-safe-valve-actuator-spring-and-lock-up-relay-diagram',
    'fail safe valve actuator diagram with spring return fail open, fail closed and fail locked',
    'Diagram by Instrumentation Blog showing how the actuator spring drives a fail open ATC or fail closed ATO valve, and how a lock up relay traps air for fail locked.',
    'How the Actuator Achieves Each Fail Safe Position', s.svg())

s = S(590, 'Flowchart to select fail open, fail closed or fail locked valve position')
s.head('Choosing the Fail Safe Position', A2)
s.box(190, 56, 420, 50, ['Study the hazard in the PHA or HAZOP'], L, A, size=18)
s.ar(400, 106, 400, 122)
s.dia(400, 170, 260, 96, ['Full open on', 'failure hazardous?'], '#ffffff', A, size=17)
s.ar(270, 170, 232, 170); s.t(251, 158, 'No', 17, GRN, 'bold')
s.box(30, 140, 200, 62, ['FO, fail open', 'ATC, cooling water'], '#f0fdf4', GRN, size=17)
s.ar(400, 218, 400, 244); s.t(420, 237, 'Yes', 17, RED, 'bold', 'start')
s.dia(400, 292, 260, 96, ['Full close on', 'failure hazardous?'], '#ffffff', A, size=17)
s.ar(530, 292, 568, 292); s.t(549, 280, 'No', 17, GRN, 'bold')
s.box(570, 262, 200, 62, ['FC, fail closed', 'ATO, fuel gas'], L, RED, size=17)
s.ar(400, 340, 400, 366); s.t(420, 359, 'Yes', 17, RED, 'bold', 'start')
s.dia(400, 414, 260, 96, ['SIS final', 'element?'], '#ffffff', A, size=17)
s.ar(270, 414, 232, 414); s.t(251, 402, 'No', 17, GRN, 'bold')
s.box(20, 384, 210, 62, ['FL, fail locked', 'lock up relay'], '#fff7e6', AMB, size=17)
s.ar(530, 414, 568, 414); s.t(549, 402, 'Yes', 17, RED, 'bold')
s.box(570, 378, 210, 74, ['FL not allowed', 'define FO or FC', 'per IEC 61511'], '#ffffff', A2, size=17)
s.raw(f'<rect x="40" y="490" width="720" height="80" rx="12" fill="{L}" stroke="{A}" stroke-width="2"/>')
s.t(400, 522, 'The process hazard decides the position, not instrument convenience.', 17, A2, 'bold')
s.t(400, 550, 'Record FO, FC or FL on the P&ID; changing it later needs a management of change.', 17, '#1a2b4a')
fig(slug, 'fail-safe-valve-position-selection-flowchart',
    'flowchart to choose fail open, fail closed or fail locked control valve position',
    'Diagram by Instrumentation Blog showing how the hazard of full open or full close on failure, and SIS duty, decide between FO, FC and FL valve positions.',
    'Fail-Safe Valve Position Selector Tool', s.svg())

s = S(540, 'Fail safe valve comparison of fail open, fail closed and fail locked positions')
s.head('FO vs FC vs FL at a Glance', A2)
cards = [('FO', 'Fail Open', GRN, '#f0fdf4', ['Goes fully open', 'ATC, air to close', 'Spring opens valve'], ['Cooling water', 'Steam heating lines', 'Critical feed valves'], 'SIS: allowed'),
         ('FC', 'Fail Closed', RED, '#fef2f2', ['Goes fully closed', 'ATO, air to open', 'Spring closes valve'], ['Fuel gas to burner', 'Chemical injection', 'HP letdown valve'], 'SIS: allowed'),
         ('FL', 'Fail Locked', AMB, '#fffbeb', ['Stays at last position', 'No spring action', 'Lock up relay holds'], ['Pipeline isolation', 'Ratio control', 'Step sensitive duty'], 'SIS: never')]
for i, (code, nm, c, bg, acts, uses, sis) in enumerate(cards):
    x = 20 + i * 260
    s.raw(f'<rect x="{x}" y="60" width="240" height="440" rx="14" fill="{bg}" stroke="{c}" stroke-width="2.5"/>')
    s.raw(f'<rect x="{x}" y="60" width="240" height="70" rx="14" fill="{c}"/>')
    s.t(x + 120, 92, code, 26, '#ffffff', 'bold'); s.t(x + 120, 120, nm, 18, '#ffffff', 'bold')
    s.t(x + 20, 162, 'On loss of air', 17, c, 'bold', 'start')
    for j, a in enumerate(acts): s.t(x + 20, 190 + j * 26, a, 17, '#1a2b4a', 'normal', 'start')
    s.t(x + 20, 290, 'Typical services', 17, c, 'bold', 'start')
    for j, u in enumerate(uses): s.t(x + 20, 318 + j * 26, u, 17, '#1a2b4a', 'normal', 'start')
    s.raw(f'<rect x="{x+20}" y="420" width="200" height="50" rx="10" fill="#ffffff" stroke="{c}" stroke-width="2"/>')
    s.t(x + 120, 452, sis, 18, c, 'bold')
s.t(400, 528, 'Fail locked is a process continuity choice, not a safety choice.', 17, '#4b5563')
fig(slug, 'fail-safe-valve-fo-fc-fl-comparison-infographic',
    'fail open vs fail closed vs fail locked valve comparison with actuator action and services',
    'Diagram by Instrumentation Blog comparing FO, FC and FL valves: action on air loss, ATC or ATO actuator, typical services and whether each is allowed for SIS duty.',
    'The Three Fail Safe Valve Positions Explained', s.svg())

# ================= 2. Mass flow controller =================
slug = 'mass-flow-controller-working-principle'
A, A2, L = '#059669', '#065f46', '#ecfdf5'
s = S(540, 'Thermal mass flow controller diagram with bypass sensor tube, RTDs, heater, PID and proportional valve')
s.head('Inside a Thermal Mass Flow Controller', A2)
# main channel
s.raw(f'<rect x="40" y="360" width="720" height="44" fill="{L}" stroke="#1a2b4a" stroke-width="2.5"/>')
s.ar(10, 382, 60, 382, A, 4); s.t(70, 440, 'Gas inlet', 17, A2, 'bold')
s.ar(740, 382, 792, 382, A, 4); s.t(720, 440, 'Gas outlet', 17, A2, 'bold')
# filter
s.raw('<rect x="90" y="362" width="26" height="40" fill="#e5e7eb" stroke="#1a2b4a" stroke-width="1.5"/>')
for yy in range(366, 400, 8): s.ln(92, yy, 114, yy + 6, '#6b7280', 1.5)
s.t(103, 345, 'Filter', 17, '#1a2b4a', 'bold')
# laminar flow element
s.raw('<rect x="230" y="364" width="160" height="36" fill="#d1fae5" stroke="#1a2b4a" stroke-width="1.5"/>')
for xx in range(236, 390, 12): s.ln(xx, 366, xx, 398, A, 1.5)
s.t(310, 440, 'Laminar flow element', 17, '#1a2b4a', 'bold')
# bypass tube
s.pl([(200, 360), (200, 230), (420, 230), (420, 360)], '#1a2b4a', 4, False)
s.ar(240, 222, 380, 222, A, 2) if False else None
for xx, lab, col in [(250, 'T up', '#2563eb'), (310, 'Heater', RED), (370, 'T down', '#2563eb')]:
    for k_ in range(5): s.raw(f'<ellipse cx="{xx-10+k_*5}" cy="230" rx="3" ry="11" fill="none" stroke="{col}" stroke-width="2"/>')
    s.t(xx, 264, lab, 17, col, 'bold')
s.ar(215, 300, 215, 250, A, 2.5); s.ar(405, 250, 405, 300, A, 2.5)
s.t(310, 304, 'Bypass tube', 17, '#1a2b4a', 'bold')
s.t(310, 328, 'small share of gas', 17, '#4b5563')
# proportional valve on channel
s.raw('<polygon points="540,362 540,402 600,362 600,402" fill="#ffffff" stroke="#1a2b4a" stroke-width="2.5"/>')
s.ln(570, 382, 570, 300, '#1a2b4a', 3)
s.box(510, 250, 120, 50, ['Valve coil'], '#fff7e6', size=17)
s.t(570, 440, 'Proportional valve', 17, '#1a2b4a', 'bold')
# PID box
s.box(470, 80, 290, 76, ['PID controller', 'compares flow with setpoint'], '#ffffff', A, size=17)
s.ar(615, 50, 615, 78, '#1a2b4a'); s.t(690, 64, 'Setpoint', 17, '#1a2b4a', 'bold')
s.pl([(370, 216), (370, 120), (468, 120)], '#4b5563', 2, True, '6 5'); s.t(270, 125, 'ΔT signal', 17, '#4b5563', 'bold')
s.pl([(700, 158), (700, 275), (632, 275)], '#4b5563', 2, True, '6 5'); s.t(712, 230, 'drive', 17, '#4b5563', 'bold', 'start')
s.t(400, 486, 'ΔT = T down minus T up, and ΔT is proportional to ṁ × Cp', 18, A2, 'bold')
s.t(400, 516, 'At zero flow both RTDs read the same temperature, so ΔT = 0', 17, '#4b5563')
fig(slug, 'mass-flow-controller-thermal-sensor-and-valve-diagram',
    'thermal mass flow controller diagram with bypass tube, RTD sensors, heater, PID and valve',
    'Diagram by Instrumentation Blog showing a thermal MFC: inlet filter, laminar flow element, heated bypass tube with two RTDs, PID controller and proportional valve.',
    'Thermal MFC: The Most Common Type', s.svg())

s = S(560, 'Mass flow controller closed loop control flowchart')
s.head('Mass Flow Controller Control Loop', A2)
s.box(250, 58, 300, 54, ['Setpoint entered', 'in sccm or slm'], L, A, size=17)
s.ar(400, 112, 400, 132)
s.box(230, 132, 340, 54, ['Sensor measures', 'actual mass flow'], L, A, size=17)
s.ar(400, 186, 400, 206)
s.dia(400, 256, 290, 98, ['Flow equal to', 'setpoint?'], '#ffffff', A, size=17)
s.ar(545, 256, 590, 256); s.t(566, 246, 'Yes', 17, GRN, 'bold')
s.box(590, 226, 180, 60, ['Hold valve', 'position'], '#ffffff', A, size=17)
s.ar(400, 305, 400, 330); s.t(418, 324, 'No', 17, RED, 'bold', 'start')
s.box(200, 330, 400, 60, ['High: valve closes slightly', 'Low: valve opens slightly'], '#fff7e6', A, size=17, bold_first=False)
s.pl([(200, 360), (120, 360), (120, 159), (228, 159)], A, 2.5)
s.pl([(680, 286), (680, 420), (120, 420), (120, 362)], A, 2.5, False, '6 5')
s.t(400, 412, 'loop repeats continuously', 17, '#4b5563')
s.raw(f'<rect x="40" y="446" width="720" height="96" rx="12" fill="{L}" stroke="{A}" stroke-width="2"/>')
s.t(400, 476, 'Example: upstream pressure rises, a needle valve passes more gas,', 17, '#1a2b4a')
s.t(400, 502, 'but the MFC sees the higher flow and closes its valve slightly.', 17, '#1a2b4a')
s.t(400, 528, 'Settling to 98% of setpoint takes about 1 to 3 s.', 17, A2, 'bold')
fig(slug, 'mass-flow-controller-closed-loop-control-flowchart',
    'how does mass flow controller work flowchart with setpoint, sensor, PID and valve',
    'Diagram by Instrumentation Blog showing the MFC closed loop: the sensor measures mass flow, the PID compares it with the setpoint and the valve corrects the error.',
    'How a Mass Flow Controller Works', s.svg())

s = S(580, 'Mass flow controller gas conversion factor chart for common gases relative to nitrogen')
s.head('Gas Conversion Factors (Reference N2 = 1.000)', A2)
gases = [('Silane SiH4', 0.600), ('CO2', 0.740), ('Methane CH4', 0.747), ('Oxygen O2', 0.993), ('Nitrogen N2', 1.000),
         ('Hydrogen H2', 1.010), ('Argon Ar', 1.390), ('Helium He', 1.454)]
x0, sc = 190, 300
s.ln(x0 + sc, 62, x0 + sc, 384, '#6b7280', 2, '6 4'); s.t(x0 + sc, 402, 'GCF 1.0', 17, '#4b5563', 'bold')
for i, (g, v) in enumerate(gases):
    y = 66 + i * 39
    c = '#2563eb' if v < 0.99 else (A if v <= 1.011 else '#ea580c')
    s.t(x0 - 12, y + 22, g, 17, '#1a2b4a', 'bold', 'end')
    s.raw(f'<rect x="{x0}" y="{y+4}" width="{v*sc:.0f}" height="28" rx="5" fill="{c}"/>')
    s.t(x0 + v * sc + 10, y + 24, f'{v:.3f}', 17, '#1a2b4a', 'bold', 'start')
s.raw(f'<rect x="30" y="418" width="350" height="146" rx="12" fill="#eff6ff" stroke="#2563eb" stroke-width="2"/>')
s.t(205, 446, 'GCF below 1: under reads', 17, '#1d4ed8', 'bold')
s.t(205, 476, 'CO2, display 100 sccm', 17, '#1a2b4a')
s.t(205, 504, '100 ÷ 0.74 = 135.1 sccm', 18, '#1a2b4a', 'bold')
s.t(205, 534, 'actual is higher', 17, '#4b5563')
s.raw(f'<rect x="420" y="418" width="350" height="146" rx="12" fill="#fff7ed" stroke="#ea580c" stroke-width="2"/>')
s.t(595, 446, 'GCF above 1: over reads', 17, '#c2410c', 'bold')
s.t(595, 476, 'Helium, display 100 sccm', 17, '#1a2b4a')
s.t(595, 504, '100 ÷ 1.454 = 68.8 sccm', 18, '#1a2b4a', 'bold')
s.t(595, 534, 'actual is lower', 17, '#4b5563')
fig(slug, 'mass-flow-controller-gas-conversion-factor-chart',
    'mass flow controller gas conversion factor chart for CO2, argon, helium, methane and silane',
    'Diagram by Instrumentation Blog charting MFC gas conversion factors against nitrogen, with actual flow equal to MFC reading divided by GCF for CO2 and helium.',
    'Gas Conversion Factor (GCF) and Why It Matters', s.svg())

# ================= 3. PID controller types =================
slug = 'pid-controller-types-explained'
A, A2, L = '#4f46e5', '#3730a3', '#eef2ff'
s = S(600, 'PID controller block diagram of parallel, ideal and series forms')
s.head('PID Controller Forms as Block Diagrams', A2)
def sigma(s, x, y):
    s.raw(f'<circle cx="{x}" cy="{y}" r="22" fill="#ffffff" stroke="#1a2b4a" stroke-width="2.5"/>'); s.t(x, y + 8, 'Σ', 22, '#1a2b4a', 'bold')
def three(s, yc, first):
    s.t(165, yc + 6, 'e', 20, '#1a2b4a', 'bold'); s.ln(178, yc, 200, yc)
    s.ln(200, yc - 50, 200, yc + 50)
    for j, lab in enumerate([first, '(1/τi) ∫e dt', 'τd de/dt']):
        yy = yc - 50 + j * 50
        s.ar(200, yy, 228, yy); s.box(230, yy - 20, 180, 40, [lab], '#ffffff', A, size=17)
        s.pl([(410, yy), (445, yy), (452, yc - 12 + j * 12)], '#1a2b4a', 2.5, j != 1)
    s.ar(410, yc, 456, yc)
rows = [('Parallel', 'independent', 125), ('Ideal (ISA)', 'non interacting', 300), ('Series', 'interacting', 475)]
for nm, sub, yc in rows:
    s.raw(f'<rect x="15" y="{yc-75}" width="770" height="150" rx="14" fill="{L}" stroke="{A}" stroke-width="1.5"/>')
    s.t(80, yc - 4, nm, 19, A2, 'bold'); s.t(80, yc + 22, sub, 17, '#4b5563')
three(s, 125, 'Kp × e'); sigma(s, 480, 125); s.ar(502, 125, 560, 125); s.t(578, 132, 'm', 20, '#1a2b4a', 'bold')
s.t(690, 120, 'Kp acts on', 17, A2, 'bold'); s.t(690, 144, 'P term only', 17, A2, 'bold')
three(s, 300, 'e'); sigma(s, 480, 300); s.ar(502, 300, 528, 300); s.box(530, 280, 60, 40, ['Kp'], A, A, '#ffffff', size=18)
s.ar(590, 300, 612, 300); s.t(624, 307, 'm', 20, '#1a2b4a', 'bold')
s.t(705, 295, 'Kp scales', 17, A2, 'bold'); s.t(705, 319, 'P, I and D', 17, A2, 'bold')
yc = 475
s.t(165, yc + 6, 'e', 20, '#1a2b4a', 'bold'); s.ar(178, yc, 208, yc)
s.box(210, yc - 22, 60, 44, ['Kp'], A, A, '#ffffff', size=18); s.ar(270, yc, 298, yc)
s.box(300, yc - 32, 140, 64, ['PI unit', 'uses τi'], '#ffffff', A, size=17); s.ar(440, yc, 468, yc)
s.box(470, yc - 32, 140, 64, ['PD unit', 'uses τd'], '#ffffff', A, size=17); s.ar(610, yc, 632, yc)
s.t(645, yc + 7, 'm', 20, '#1a2b4a', 'bold')
s.t(722, yc - 4, 'τi and τd', 17, A2, 'bold'); s.t(722, yc + 20, 'change P too', 17, A2, 'bold')
s.t(400, 580, 'e = error, m = output. With τd = 0 all three forms give the same PI action.', 17, '#4b5563')
fig(slug, 'pid-controller-parallel-ideal-series-block-diagram',
    'types of PID controller block diagram parallel, ideal ISA and series interacting forms',
    'Diagram by Instrumentation Blog showing where Kp, τi and τd act in the parallel, ideal ISA and series interacting PID controller equation forms.',
    'Types of PID Equations Compared Side by Side', s.svg())

s = S(600, 'Flowchart to convert series PID settings to ideal form with a sample calculation')
s.head('Convert Series PID Settings to Ideal Form', A2)
s.box(210, 58, 380, 62, ['Read legacy series settings', 'sample: Kp 2, τi 4 min, τd 1 min'], L, A, size=17)
s.ar(400, 120, 400, 138)
s.dia(400, 180, 220, 84, ['τd = 0?'], '#ffffff', A, size=19)
s.ar(510, 180, 560, 180); s.t(534, 170, 'Yes', 17, GRN, 'bold')
s.box(560, 146, 220, 68, ['PI loop: copy', 'values, no retune'], '#f0fdf4', GRN, size=17)
s.ar(400, 222, 400, 244); s.t(416, 238, 'No', 17, RED, 'bold', 'start')
steps = [('Kp ideal = Kp × (1 + τd/τi)', '2 × (1 + 1/4) = 2.5'),
         ('τi ideal = τi + τd', '4 + 1 = 5 min'),
         ('τd ideal = (τi × τd) ÷ (τi + τd)', '(4 × 1) ÷ 5 = 0.8 min')]
for j, (f_, ex) in enumerate(steps):
    y = 246 + j * 88
    s.box(90, y, 360, 62, [f_], '#ffffff', A, size=17)
    s.ar(452, y + 31, 488, y + 31, A, 2.5)
    s.box(490, y, 250, 62, [ex], L, A, size=18)
    if j < 2: s.ar(270, y + 62, 270, y + 86)
s.ar(270, 484, 270, 504)
s.box(90, 506, 650, 60, ['Enter Kp 2.5, τi 5 min, τd 0.8 min in the ideal controller'], A, A, '#ffffff', size=18)
fig(slug, 'pid-controller-series-to-ideal-conversion-flowchart',
    'flowchart to convert series PID tuning to ideal ISA form with sample values',
    'Diagram by Instrumentation Blog showing how to convert series PID tuning to ideal form using the standard relations, with a sample of Kp 2, τi 4 min and τd 1 min.',
    'Series PID Controller', s.svg())

s = S(560, 'PID controller types tuning interaction matrix')
s.head('What One Setting Change Affects', A2)
cols = ['Change Kp', 'Change τi', 'Change τd']
rws = [('Parallel', ['P only', 'I only', 'D only']), ('Ideal (ISA)', ['P, I and D', 'I only', 'D only']), ('Series', ['P, I and D', 'I and P', 'D and P'])]
for j, c_ in enumerate(cols):
    s.raw(f'<rect x="{200+j*195}" y="64" width="185" height="52" rx="10" fill="{A}"/>'); s.t(292 + j * 195, 97, c_, 19, '#ffffff', 'bold')
for i, (nm, cells) in enumerate(rws):
    y = 128 + i * 92
    s.raw(f'<rect x="20" y="{y}" width="170" height="80" rx="10" fill="{L}" stroke="{A}" stroke-width="2"/>'); s.t(105, y + 47, nm, 19, A2, 'bold')
    for j, cv in enumerate(cells):
        hot = (cv != ['P only', 'I only', 'D only'][j])
        fillc = '#fde68a' if hot else '#ffffff'
        s.raw(f'<rect x="{200+j*195}" y="{y}" width="185" height="80" rx="10" fill="{fillc}" stroke="{A}" stroke-width="2"/>')
        s.t(292 + j * 195, y + 47, cv, 19, '#1a2b4a', 'bold')
s.raw('<rect x="200" y="410" width="26" height="22" rx="4" fill="#fde68a" stroke="#4f46e5" stroke-width="1.5"/>')
s.t(236, 428, 'one setting moves more than its own action', 17, '#1a2b4a', 'normal', 'start')
s.raw(f'<rect x="20" y="452" width="760" height="92" rx="12" fill="{L}" stroke="{A}" stroke-width="2"/>')
s.t(400, 482, 'Transmitter span changed? The loop gain changes.', 17, A2, 'bold')
s.t(400, 508, 'Parallel form: retune P, I and D in the right proportion.', 17, '#1a2b4a')
s.t(400, 532, 'Ideal or series form: adjust Kp alone to restore the loop.', 17, '#1a2b4a')
fig(slug, 'pid-controller-tuning-interaction-infographic',
    'PID controller types tuning interaction chart showing what Kp, τi and τd change',
    'Diagram by Instrumentation Blog comparing parallel, ideal and series PID forms by which actions change when Kp, τi or τd is adjusted during tuning.',
    '2. Ideal PID Controller', s.svg())

# ================= 4. Reynolds number =================
slug = 'what-is-reynolds-number'
A, A2, L = '#0284c7', '#075985', '#f0f9ff'
s = S(540, 'Reynolds number diagram of laminar parabolic and turbulent flat velocity profiles in a pipe')
s.head('Reynolds Number and Velocity Profile in a Pipe', A2)
for (yt, yb, nm, rng, prof, col) in [(80, 210, 'Laminar', 'Re < 2300', 'lam', GRN), (300, 430, 'Turbulent', 'Re > 4000', 'turb', '#ea580c')]:
    s.ln(170, yt, 640, yt, '#1a2b4a', 4); s.ln(170, yb, 640, yb, '#1a2b4a', 4)
    s.raw(f'<rect x="170" y="{yt+2}" width="470" height="{yb-yt-4}" fill="{L}"/>')
    s.box(20, yt + 25, 135, 80, [nm, rng], '#ffffff', col, size=17)
    R = (yb - yt) / 2; yc = (yt + yb) / 2
    s.ln(300, yt + 2, 300, yb - 2, '#9ca3af', 2)
    for k_ in range(-5, 6):
        r = k_ / 5.6; y = yc + r * R
        ln_ = 190 * (1 - r * r) if prof == 'lam' else 170 * (1 - abs(r) ** 7)
        if ln_ > 8: s.ar(300, y, 300 + ln_, y, col, 2.2)
    if prof == 'lam':
        pts = ' '.join(f'{300+190*(1-(k_/20)**2):.1f},{yc+k_/20*R:.1f}' for k_ in range(-20, 21))
        s.raw(f'<polyline points="{pts}" fill="none" stroke="{col}" stroke-width="2" stroke-dasharray="5 4"/>')
    else:
        for ex, ey in [(540, yt + 35), (590, yc + 5), (530, yb - 30), (615, yt + 55)]:
            s.raw(f'<path d="M{ex-14} {ey} a14 12 0 1 1 14 12" fill="none" stroke="{col}" stroke-width="2.2"/>')
    s.t(720, yc - 4, 'Parabolic' if prof == 'lam' else 'Flat profile', 17, col, 'bold')
    s.t(720, yc + 20, 'profile' if prof == 'lam' else 'with eddies', 17, col, 'bold')
s.raw('<line x1="190" y1="304" x2="190" y2="426" stroke="#1a2b4a" stroke-width="2" marker-end="url(#ah)" marker-start="url(#ah)"/>')
s.t(212, 372, 'D', 20, '#1a2b4a', 'bold')
s.t(470, 248, 'Fastest at the centreline, zero at the wall', 17, '#4b5563')
s.t(400, 476, 'Re = ρ × v × D ÷ μ (inertial forces ÷ viscous forces)', 19, A2, 'bold')
s.t(400, 508, 'Between 2300 and 4000 flow is transitional: avoid it for metering.', 17, '#4b5563')
fig(slug, 'reynolds-number-laminar-turbulent-velocity-profile-diagram',
    'reynolds number laminar vs turbulent flow velocity profile diagram in a pipe',
    'Diagram by Instrumentation Blog showing the parabolic laminar velocity profile below Re 2300 and the flat turbulent profile with eddies above Re 4000.',
    'Reynolds Number Flow Regimes: Laminar, Transitional and Turbulent', s.svg())

s = S(600, 'Flowchart to calculate Reynolds number and choose a flow meter')
s.head('From Reynolds Number to Flow Meter Choice', A2)
s.box(200, 56, 400, 62, ['Collect ρ, v, D and μ', 'use actual bore, not nominal size'], L, A, size=17)
s.ar(400, 118, 400, 136)
s.box(250, 136, 300, 48, ['Re = ρ × v × D ÷ μ'], '#ffffff', A, size=19)
s.ar(400, 184, 400, 200)
s.dia(400, 246, 240, 90, ['Re < 2300?'], '#ffffff', A, size=18)
s.ar(280, 246, 236, 246); s.t(258, 236, 'Yes', 17, GRN, 'bold')
s.box(16, 206, 220, 80, ['Laminar', 'Coriolis, PD or', 'magnetic meter'], '#f0fdf4', GRN, size=17)
s.ar(400, 291, 400, 314); s.t(416, 307, 'No', 17, RED, 'bold', 'start')
s.dia(400, 360, 240, 90, ['Re ≤ 4000?'], '#ffffff', A, size=18)
s.ar(520, 360, 564, 360); s.t(542, 350, 'Yes', 17, RED, 'bold')
s.box(564, 320, 220, 80, ['Transitional', 'meters unreliable,', 'avoid this range'], '#fef2f2', RED, size=17)
s.ar(400, 405, 400, 428); s.t(416, 421, 'No', 17, GRN, 'bold', 'start')
s.box(200, 428, 400, 48, ['Turbulent: check meter minimum Re'], L, A, size=17)
for j, (m_, r_) in enumerate([('Orifice', '5,000 to 10,000+'), ('Vortex', '10,000 to 20,000'), ('Turbine', '5,000 to 10,000')]):
    x = 30 + j * 255
    s.box(x, 500, 230, 70, [m_, r_], '#ffffff', A, size=17)
s.ar(300, 476, 145, 498); s.ar(400, 476, 400, 498); s.ar(500, 476, 655, 498)
fig(slug, 'reynolds-number-flow-meter-selection-flowchart',
    'flowchart to calculate reynolds number and select a flow meter by flow regime',
    'Diagram by Instrumentation Blog showing how to calculate Re from density, velocity, bore and viscosity, then pick a flow meter by laminar, transitional or turbulent regime.',
    'Reynolds Number and Flow Meter Selection: Which Meter for Which Re?', s.svg())

s = S(580, 'Reynolds number worked examples for water, heavy crude oil and air with a log scale')
s.head('Reynolds Number Worked Examples', A2)
ex = [('Water in DN100', ['ρ 1000, v 2.0 m/s', 'D 0.1023 m, μ 0.001'], '204,600', 'Turbulent', '#ea580c'),
      ('Heavy crude, DN100', ['ρ 900, v 0.5 m/s', 'D 0.1023 m, μ 0.050'], '920', 'Laminar', GRN),
      ('Air in DN200 duct', ['ρ 1.2, v 10 m/s', 'D 0.200 m, μ 0.0000182'], '131,900', 'Turbulent', '#ea580c')]
for i, (h, ins, re_, reg, c) in enumerate(ex):
    x = 20 + i * 260
    s.raw(f'<rect x="{x}" y="60" width="240" height="250" rx="14" fill="{L}" stroke="{A}" stroke-width="2.5"/>')
    s.t(x + 120, 94, h, 19, A2, 'bold')
    for j, l_ in enumerate(ins): s.t(x + 120, 128 + j * 26, l_, 17, '#1a2b4a')
    s.t(x + 120, 210, 'Re = ' + re_, 26, '#1a2b4a', 'bold')
    s.raw(f'<rect x="{x+50}" y="238" width="140" height="44" rx="10" fill="{c}"/>'); s.t(x + 120, 267, reg, 19, '#ffffff', 'bold')
def lx(v):
    import math; return 60 + (math.log10(v) - 2) * 136
y0 = 420
s.raw(f'<rect x="{lx(100):.0f}" y="{y0}" width="{lx(2300)-lx(100):.0f}" height="34" fill="#bbf7d0"/>')
s.raw(f'<rect x="{lx(2300):.0f}" y="{y0}" width="{lx(4000)-lx(2300):.0f}" height="34" fill="#fecaca"/>')
s.raw(f'<rect x="{lx(4000):.0f}" y="{y0}" width="{lx(1e7)-lx(4000):.0f}" height="34" fill="#fed7aa"/>')
s.raw(f'<rect x="{lx(100):.0f}" y="{y0}" width="{lx(1e7)-lx(100):.0f}" height="34" fill="none" stroke="#1a2b4a" stroke-width="2"/>')
for v, lab in [(100, '100'), (1e3, '1,000'), (1e4, '10,000'), (1e5, '100,000'), (1e6, '1 million'), (1e7, '10 million')]:
    s.ln(lx(v), y0 + 34, lx(v), y0 + 44, '#1a2b4a', 2); s.t(lx(v), y0 + 64, lab, 17, '#1a2b4a')
s.t(lx(400), y0 + 23, 'laminar', 17, '#166534', 'bold'); s.t(560, y0 + 23, 'turbulent', 17, '#9a3412', 'bold')
for v, lab, yy, anc in [(920, 'Oil 920', 370, 'middle'), (131900, 'Air', 370, 'end'), (204600, 'Water', 370, 'start')]:
    s.ar(lx(v), yy + 10, lx(v), y0 - 2, '#1a2b4a', 2.5)
    s.t(lx(v) + (0 if anc == 'middle' else (-6 if anc == 'end' else 6)), yy, lab, 17, '#1a2b4a', 'bold', anc)
s.t(400, 534, 'Units: ρ in kg/m³, v in m/s, D in m, μ in Pa.s. Re has no units.', 17, '#4b5563')
s.t(400, 560, 'Transitional band 2300 to 4000 shown in red.', 17, '#4b5563')
fig(slug, 'reynolds-number-worked-examples-infographic',
    'reynolds number worked examples for water 204600, heavy crude oil 920 and air 131900',
    'Diagram by Instrumentation Blog summarising the three worked examples: water in DN100 at Re 204,600, heavy crude at Re 920 and air in a DN200 duct at Re 131,900.',
    'Reynolds Number Worked Examples: Water, Oil and Air', s.svg())

# ================= 5. PSI to bar =================
slug = 'psi-to-bar-conversion'
A, A2, L = '#b45309', '#78350f', '#fffbeb'
s = S(560, 'PSI to bar gauge vs absolute pressure reference diagram')
s.head('Gauge vs Absolute: psig, psia, bar g, bar a', A2)
levels = [(150, '164.7 psia = 150 psig', '11.355 bar a = 10.342 bar g', 'Air receiver at 150 psig'),
          (330, '14.696 psia = 0 psig', '1.01325 bar a = 0 bar g', 'Atmosphere at sea level'),
          (440, '0 psia = minus 14.7 psig', '0 bar a', 'Perfect vacuum')]
s.raw(f'<rect x="388" y="{levels[0][0]}" width="24" height="{levels[2][0]-levels[0][0]}" fill="{L}" stroke="#1a2b4a" stroke-width="2"/>')
for y, lp, rb, nm in levels:
    s.ln(372, y, 428, y, A, 4)
    s.t(362, y - 8, nm, 17, A2, 'bold', 'end')
    s.t(362, y + 18, lp, 17, '#1a2b4a', 'normal', 'end'); s.t(438, y + 6, rb, 17, '#1a2b4a', 'bold', 'start')
s.raw(f'<line x1="40" y1="440" x2="40" y2="154" stroke="#2563eb" stroke-width="3" marker-end="url(#ah)"/>')
s.raw('<text x="28" y="300" font-size="17" fill="#2563eb" font-weight="bold" text-anchor="middle" transform="rotate(-90 28 300)">absolute, from vacuum</text>')
s.raw(f'<line x1="760" y1="330" x2="760" y2="154" stroke="{A}" stroke-width="3" marker-end="url(#ah)"/>')
s.raw(f'<text x="775" y="242" font-size="17" fill="{A}" font-weight="bold" text-anchor="middle" transform="rotate(-90 775 242)">gauge, from air</text>')
s.t(250, 92, 'psi', 20, A2, 'bold'); s.t(550, 92, 'bar', 20, A2, 'bold')
s.raw(f'<rect x="60" y="486" width="680" height="48" rx="10" fill="{L}" stroke="{A}" stroke-width="2"/>')
s.t(400, 516, 'Same factor 0.0689476 for both; psig gives bar g, psia gives bar a', 17, '#1a2b4a', 'bold')
fig(slug, 'psi-to-bar-gauge-vs-absolute-pressure-diagram',
    'psig vs psia vs bar g vs bar a reference diagram from vacuum to atmosphere',
    'Diagram by Instrumentation Blog showing gauge pressure measured from the atmosphere and absolute pressure from vacuum, with 150 psig as 10.342 bar g and 11.355 bar a.',
    'Psig vs Psia vs Bar g vs Bar a', s.svg())

s = S(580, 'Flowchart to convert a pressure transmitter range from psi to bar')
s.head('Converting a Transmitter Range From psi to bar', A2)
steps = [('1  Read the nameplate', 'Range 0 to 500 psig'), ('2  Convert LRV and URV', '500 × 0.0689476 = 34.474'),
         ('3  Round sensibly', 'Match instrument accuracy'), ('4  Update the DCS tag', '0 to 34.474 bar g'),
         ('5  Verify on the bench', '12 mA = 50% = 17.237 bar g')]
for j, (st, ex_) in enumerate(steps):
    y = 62 + j * 98
    s.box(30, y, 330, 64, [st], L if j % 2 == 0 else '#ffffff', A, size=18)
    s.ar(362, y + 32, 398, y + 32, A, 2.5)
    s.box(400, y, 370, 64, [ex_], '#ffffff', '#9ca3af', size=17, bold_first=False)
    if j < 4: s.ar(195, y + 64, 195, y + 96)
s.t(400, 566, 'Change the unit and the range together so the operator never sees a false value.', 17, '#4b5563')
fig(slug, 'psi-to-bar-transmitter-range-conversion-flowchart',
    'flowchart to convert transmitter range from 0 to 500 psig to bar g',
    'Diagram by Instrumentation Blog showing the five steps to convert a gauge or transmitter range, with 0 to 500 psig becoming 0 to 34.474 bar g and 12 mA as 17.237 bar g.',
    'Converting Gauge and Transmitter Ranges', s.svg())

s = S(540, 'PSI to bar conversion formula card with key values')
s.head('PSI to Bar Formula Card', A2)
s.raw(f'<rect x="30" y="62" width="355" height="110" rx="14" fill="{A}"/>')
s.t(207, 100, 'psi to bar', 19, '#ffffff', 'bold'); s.t(207, 146, 'bar = psi × 0.0689476', 22, '#ffffff', 'bold')
s.raw(f'<rect x="415" y="62" width="355" height="110" rx="14" fill="{A2}"/>')
s.t(592, 100, 'bar to psi', 19, '#ffffff', 'bold'); s.t(592, 146, 'psi = bar × 14.5038', 22, '#ffffff', 'bold')
vals = [('100 psi', '6.8948 bar'), ('150 psi', '10.342 bar'), ('16 bar', '232.06 psi'),
        ('14.5 psi', '0.9997 bar'), ('1 kg/cm²', '0.980665 bar'), ('1 psi', '6.894757 kPa')]
for i, (a_, b_) in enumerate(vals):
    x = 30 + (i % 3) * 250; y = 196 + (i // 3) * 132
    s.raw(f'<rect x="{x}" y="{y}" width="230" height="112" rx="12" fill="{L}" stroke="{A}" stroke-width="2"/>')
    s.t(x + 115, y + 40, a_, 20, A2, 'bold'); s.t(x + 115, y + 64, 'equals', 17, '#4b5563'); s.t(x + 115, y + 94, b_, 22, '#1a2b4a', 'bold')
s.raw('<rect x="30" y="466" width="740" height="56" rx="12" fill="#ffffff" stroke="#b45309" stroke-width="2" stroke-dasharray="6 4"/>')
s.t(400, 500, 'Shortcut psi × 0.07 reads about 1.5% high: 100 psi gives 7.0, not 6.89 bar', 17, '#1a2b4a', 'bold')
fig(slug, 'psi-to-bar-conversion-formula-infographic',
    'psi to bar conversion formula card with 100 psi, 150 psi and 16 bar examples',
    'Diagram by Instrumentation Blog showing the psi to bar and bar to psi formulas with key values such as 100 psi equal to 6.8948 bar and 16 bar equal to 232.06 psi.',
    'PSI to Bar Formula and Bar to PSI Formula', s.svg())

if __name__ == '__main__': main()
