C = dict(
title="Level Bridle: Meaning, Diagram, Uses & Common Mistakes",
meta="A level bridle is an external standpipe that holds level instruments and can be isolated. See a diagram, density example, field tips and common mistakes.",
svg_h2="Level Bridle Arrangement",
svg='''<svg viewBox="0 0 680 320" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Vessel with an external level bridle connected at top and bottom, with isolation valves, a gauge glass and a guided wave radar">
<rect x="60" y="30" width="200" height="260" rx="30" fill="#eaf2fe" stroke="#1e293b" stroke-width="3"/>
<rect x="63" y="150" width="194" height="137" rx="0" fill="#1e73be" opacity=".35"/>
<rect x="420" y="40" width="40" height="250" fill="#fff" stroke="#1e293b" stroke-width="3"/>
<rect x="423" y="150" width="34" height="137" fill="#1e73be" opacity=".35"/>
<path d="M260 70 H420 M260 250 H420" stroke="#1e293b" stroke-width="3"/>
<g fill="#d9622b"><path d="M318 62 L338 70 L318 78 Z M358 62 L338 70 L358 78 Z"/><path d="M318 242 L338 250 L318 258 Z M358 242 L338 250 L358 258 Z"/></g>
<rect x="470" y="60" width="16" height="210" fill="#fff" stroke="#5b6576" stroke-width="2"/><rect x="472" y="150" width="12" height="118" fill="#1e73be" opacity=".5"/>
<path d="M460 80 H470 M460 250 H470" stroke="#5b6576" stroke-width="2"/>
<rect x="425" y="14" width="30" height="22" rx="4" fill="#0b3d6b"/><path d="M440 36 V280" stroke="#0b3d6b" stroke-width="2" stroke-dasharray="5 4"/>
<g font-size="13" fill="#1e293b"><text x="120" y="22">Vessel</text><text x="290" y="56">isolation valves</text>
<text x="500" y="160">gauge glass</text><text x="470" y="28">GWR on top</text><text x="470" y="300">drain at bottom</text></g>
<path d="M440 290 V310" stroke="#1e293b" stroke-width="3"/>
</svg>''',
svg_cap="The bridle connects to the vessel above and below the measuring range. Valves let every instrument be isolated and serviced while the vessel keeps running.",
table=("Typical Bridle Details", ["Item", "Common practice"], [
    ["Pipe size", "2 to 4 inch; 3 or 4 inch is common for guided wave radar and displacers"],
    ["Connections", "Top and bottom process nozzles, plus vent and drain"],
    ["Instruments", "Gauge glass or magnetic gauge, guided wave radar, displacer, level switches"],
    ["Isolation", "Valves on both process nozzles and on each instrument branch"],
    ["Heat loss control", "Insulation or tracing to match vessel temperature"]]),
example=("Worked Example: Reading Error from a Cooler Bridle",
    "A vessel holds a hydrocarbon with density 700 kg/m³ at process temperature. The uninsulated bridle cools the liquid to 740 kg/m³. The bridle shows 1.50 m of liquid.",
    ["Both legs are at the same pressure at the bottom nozzle, so ρ<sub>vessel</sub> × h<sub>vessel</sub> = ρ<sub>bridle</sub> × h<sub>bridle</sub> (ignoring vapour density).",
     "h<sub>vessel</sub> = 740 × 1.50 ÷ 700 = 1.586 m.",
     "Error = 1.586 − 1.50 = 0.086 m."],
    "The bridle reads about 86 mm lower than the true vessel level. Insulation or tracing removes most of this error."),
tips=("Field Tips", [
    "Size the process nozzles generously and keep the connecting lines short and sloped so gas and liquid can move freely.",
    "Fit a vent and a drain so the bridle can be flushed and the instruments checked against each other.",
    "For guided wave radar, choose a bridle size the probe supplier approves and keep internal welds smooth.",
    "Compare the gauge glass with the transmitter during each shift round. A growing difference often means a blocked nozzle."]),
mistakes=("Common Mistakes", [
    "Leaving the bridle uninsulated on a hot or cold vessel, which changes density and gives a steady level error.",
    "Placing the bottom nozzle where sludge collects, so it slowly blocks and the bridle level freezes.",
    "Closing a process valve for maintenance and forgetting to reopen it, which leaves a frozen reading on the DCS.",
    "Mounting instruments so they cannot be isolated individually, which forces a full bridle shutdown for one repair."]),
faq=[
    ("What is the difference between a bridle and a stilling well?", "A bridle is outside the vessel and can be isolated with valves. A stilling well is a perforated pipe inside the tank and cannot be isolated."),
    ("Why do bridles need a vent and drain?", "The vent and drain let you flush deposits, prove the instruments and safely empty the bridle before maintenance.")],
)
