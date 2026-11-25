C = dict(
title="I/P Converter: Working, Formula & 4 to 20 mA Example",
meta="An I/P converter turns a 4 to 20 mA signal into 0.2 to 1.0 bar air pressure. Working diagram, signal table, worked example, field tips and mistakes.",
svg_h2="How an I/P Converter Works",
svg='''<svg viewBox="0 0 680 280" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="I/P converter block diagram with coil, flapper and nozzle, pneumatic relay and output to the valve actuator">
<rect x="20" y="110" width="110" height="60" rx="8" fill="#eaf2fe" stroke="#1e73be" stroke-width="2"/><text x="75" y="136" text-anchor="middle" font-size="13" fill="#1e293b">Controller</text><text x="75" y="155" text-anchor="middle" font-size="12" fill="#5b6576">4 to 20 mA</text>
<path d="M130 140 H190" stroke="#1e73be" stroke-width="3"/>
<rect x="190" y="90" width="220" height="110" rx="10" fill="#fff" stroke="#1e293b" stroke-width="2"/>
<rect x="210" y="115" width="50" height="60" rx="6" fill="#fde7dc" stroke="#d9622b"/><text x="235" y="150" text-anchor="middle" font-size="12" fill="#1e293b">coil</text>
<path d="M270 120 L340 150" stroke="#1e293b" stroke-width="4"/><text x="290" y="112" font-size="12" fill="#5b6576">flapper</text>
<rect x="344" y="140" width="14" height="30" fill="#5b6576"/><text x="330" y="188" font-size="12" fill="#5b6576">nozzle</text>
<path d="M410 145 H460" stroke="#1f9d55" stroke-width="3"/>
<rect x="460" y="115" width="90" height="60" rx="8" fill="#e8f7ef" stroke="#1f9d55" stroke-width="2"/><text x="505" y="141" text-anchor="middle" font-size="13" fill="#1e293b">Relay</text><text x="505" y="160" text-anchor="middle" font-size="12" fill="#5b6576">boosts air</text>
<path d="M550 145 H600" stroke="#1f9d55" stroke-width="3"/>
<path d="M600 115 H660 V175 H600 Z" fill="#f3edfc" stroke="#6b3fb0" stroke-width="2"/><text x="630" y="150" text-anchor="middle" font-size="12" fill="#1e293b">Actuator</text>
<path d="M505 60 V115" stroke="#5b6576" stroke-width="2"/><text x="505" y="52" text-anchor="middle" font-size="12" fill="#5b6576">supply air 1.4 bar</text>
<text x="575" y="200" text-anchor="middle" font-size="12" fill="#1f9d55">0.2 to 1 bar</text>
<text x="300" y="230" text-anchor="middle" font-size="13" fill="#1e293b">More current pulls the flapper closer to the nozzle, raising back pressure and output.</text>
</svg>''',
svg_cap="The coil and flapper set a small pilot pressure, and the relay amplifies it so the output can fill an actuator quickly.",
table=("Signal Conversion Table", ["Input (mA)", "Output (bar g)", "Output (psi)", "Valve position (air to open)"], [
    ["4", "0.20", "3", "0 %"],
    ["8", "0.40", "6", "25 %"],
    ["12", "0.60", "9", "50 %"],
    ["16", "0.80", "12", "75 %"],
    ["20", "1.00", "15", "100 %"]]),
example=("Worked Example: Checking an I/P in the Field",
    "The DCS sends 14 mA to an I/P ranged 0.2 to 1.0 bar g. The output gauge reads 0.63 bar g.",
    ["Expected output = 0.2 + 0.8 × (14 − 4) ÷ 16 = 0.70 bar g.",
     "Error = 0.63 − 0.70 = −0.07 bar.",
     "As a share of the 0.8 bar span: −0.07 ÷ 0.8 = −8.75 %."],
    "The I/P is reading 8.75 % of span low, well outside a typical ±1 % limit. Check supply pressure, nozzle condition and calibration."),
tips=("Field Tips", [
    "Feed the I/P with clean, dry instrument air through a filter regulator set to the supplier value, commonly about 1.4 bar g for a 0.2 to 1 bar output.",
    "Check zero at 4 mA and span at 20 mA, then confirm 12 mA reads 0.6 bar g to prove linearity.",
    "Mount the I/P away from strong vibration or use a model rated for it, because the flapper is sensitive.",
    "Calculate expected outputs with the <a href=\"https://www.instrumentationblog.in/calculators/\">signal calculators</a> before you start a loop check."]),
mistakes=("Common Mistakes", [
    "Using wet or oily air, which blocks the nozzle and causes slow, drifting output.",
    "Expecting a small I/P to stroke a large actuator quickly. Use a booster relay or a positioner instead.",
    "Mixing up air to open and air to close, which reverses the valve response to the controller.",
    "Forgetting that most smart positioners already contain an I/P, then adding a second converter in the loop."]),
faq=[
    ("What supply pressure does an I/P converter need?", "It needs a regulated supply a little above its maximum output. For a 0.2 to 1.0 bar output, around 1.4 bar g is common; follow the data sheet."),
    ("Is an I/P converter the same as a positioner?", "No. An I/P only converts current to pressure. A positioner also measures valve stem position and corrects it until the valve reaches the demanded position.")],
)
