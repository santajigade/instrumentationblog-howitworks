C = dict(
title="Stilling Well: Meaning, Diagram, Sizing Tips & Mistakes",
meta="A stilling well is a perforated pipe inside a tank that calms the surface for level measurement. Diagram, design guide, field tips and common mistakes.",
svg_h2="Stilling Well Inside a Tank",
svg='''<svg viewBox="0 0 680 300" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Tank with turbulent surface and a vertical perforated stilling well with radar on top giving a calm level inside">
<path d="M80 40 V270 H600 V40" stroke="#1e293b" stroke-width="3" fill="none"/>
<path d="M83 140 Q110 125 140 140 T200 140 T260 140 T320 140 T380 140 T440 140 T500 140 T560 140 T597 140 V267 H83 Z" fill="#c9dcf8"/>
<rect x="420" y="30" width="44" height="240" fill="#fff" stroke="#1e293b" stroke-width="3"/>
<rect x="423" y="140" width="38" height="127" fill="#c9dcf8"/><path d="M423 140 H461" stroke="#1e73be" stroke-width="3"/>
<g fill="#1e293b"><circle cx="442" cy="70" r="3"/><circle cx="442" cy="110" r="3"/><circle cx="442" cy="170" r="3"/><circle cx="442" cy="210" r="3"/><circle cx="442" cy="250" r="3"/></g>
<rect x="424" y="8" width="36" height="22" rx="4" fill="#0b3d6b"/><path d="M442 30 V136" stroke="#d9622b" stroke-width="2" stroke-dasharray="5 4"/>
<g font-size="13" fill="#1e293b"><text x="480" y="22">radar for pipes</text><text x="480" y="100">holes keep the level equal</text><text x="480" y="160">calm surface inside</text><text x="150" y="120">turbulent, foamy surface</text></g>
<path d="M200 230 q15 -20 30 0 q15 20 30 0" stroke="#5b6576" stroke-width="2" fill="none"/><text x="180" y="255" font-size="12" fill="#5b6576">mixer or inlet jet</text>
</svg>''',
svg_cap="Holes or slots let the liquid inside the pipe follow the tank level, while the pipe walls shield the surface from waves, foam and agitator flow.",
table=("Stilling Well Design Guide", ["Item", "Good practice"], [
    ["Pipe size", "Usually DN 50 to DN 250; match the size your radar or float supplier approves"],
    ["Openings", "Holes or slots spaced along the full height, plus a vent hole above maximum level"],
    ["Inside finish", "Smooth bore; grind internal welds and avoid steps at flanges"],
    ["Bottom", "Open or slotted near the bottom so sediment can flush out"],
    ["Support", "Fix the pipe to the tank wall so it cannot swing in flow"]]),
example=("Worked Example: Lag in a Stilling Well",
    "A 100 mm stilling well has one 10 mm hole per 250 mm of height. The tank fills at 0.5 m per minute.",
    ["Pipe area = π ÷ 4 × 0.100² = 0.00785 m². Inside volume rise = 0.00785 × 0.5 = 0.0039 m³ per minute.",
     "Hole area = π ÷ 4 × 0.010² = 0.0000785 m². Four holes per metre share the inflow below the level.",
     "Few, small holes make the inside level lag the tank, especially with viscous liquids."],
    "Use enough openings, sized for the liquid viscosity, so the well level keeps up with the fastest fill or empty rate."),
tips=("Field Tips", [
    "For radar in a stilling well, use an antenna designed for pipes and enter the inside diameter in the setup so the signal speed is corrected.",
    "Put the well away from inlet nozzles and mixer blades, or protect it, to stop vibration and fatigue cracks.",
    "Flush the well during tank cleaning. Wax, sludge and crystals can block holes and freeze the reading.",
    "Compare the well reading with a manual dip after commissioning to prove there is no lag or offset."]),
mistakes=("Common Mistakes", [
    "Using a pipe with too few or too small holes, so the inside level lags behind the tank.",
    "Leaving rough welds or a pipe joint inside, which creates false radar echoes.",
    "Forgetting the vent hole above the maximum level, so trapped gas pushes the inside level down.",
    "Using a stilling well for viscous or crystallising liquids that slowly block the openings."]),
faq=[
    ("Do I need a stilling well for radar?", "Not always. Use one when the surface is turbulent, foamy or the tank has internals that cause false echoes. Calm tanks often work well without one."),
    ("What size stilling well is best?", "Follow the instrument supplier. Many radar suppliers recommend DN 80 to DN 150 for good signal strength.")],
)
