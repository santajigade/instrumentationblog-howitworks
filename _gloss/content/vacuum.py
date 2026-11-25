C = dict(
title="Vacuum: Definition, Ranges, Units Table & Example",
meta="Vacuum is any pressure below atmosphere, best stated as absolute pressure. Vacuum ranges and gauge table, worked example, field tips and common mistakes.",
svg_h2="Vacuum Ranges and Gauges",
svg='''<svg viewBox="0 0 680 260" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Logarithmic bar showing rough, medium, high and ultra high vacuum ranges with suitable gauge types">
<g font-size="12" fill="#5b6576" text-anchor="middle"><text x="620" y="40">1000 mbar</text><text x="500" y="40">1 mbar</text><text x="340" y="40">0.001 mbar</text><text x="130" y="40">0.0000001 mbar</text></g>
<rect x="500" y="55" width="140" height="44" fill="#c9dcf8"/><rect x="340" y="55" width="160" height="44" fill="#c3e8d2"/><rect x="190" y="55" width="150" height="44" fill="#f5ddb0"/><rect x="40" y="55" width="150" height="44" fill="#ddd0f3"/>
<g font-size="13" font-weight="700" fill="#1e293b" text-anchor="middle"><text x="570" y="82">Rough</text><text x="420" y="82">Medium</text><text x="265" y="82">High</text><text x="115" y="82">Ultra high</text></g>
<g font-size="12" fill="#1e293b" text-anchor="middle"><text x="570" y="125">diaphragm and</text><text x="570" y="141">piezo sensors</text><text x="420" y="125">Pirani and</text><text x="420" y="141">capacitance gauges</text><text x="265" y="125">cold cathode</text><text x="265" y="141">ionisation gauges</text><text x="115" y="125">hot cathode</text><text x="115" y="141">ionisation gauges</text></g>
<path d="M40 175 H640" stroke="#1e293b" stroke-width="2" marker-end="url(#v)"/><defs><marker id="v" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 Z" fill="#1e293b"/></marker></defs>
<text x="340" y="200" text-anchor="middle" font-size="13" fill="#1e293b">absolute pressure rises toward atmosphere</text>
<text x="340" y="235" text-anchor="middle" font-size="12" fill="#5b6576">Most process plant vacuum (distillation, drying, ejectors) is in the rough range.</text>
</svg>''',
svg_cap="No single gauge covers every range. Process plants mostly work in rough vacuum, where diaphragm absolute transmitters are the normal choice.",
table=("Vacuum Units Compared", ["Absolute pressure", "mbar a", "Torr (mm Hg)", "Gauge reading"], [
    ["Atmosphere (sea level)", "1013", "760", "0 mbar g"],
    ["Typical vacuum column top", "100", "75", "−913 mbar g"],
    ["Steam condenser", "about 70 to 100", "53 to 75", "about −940 mbar g"],
    ["Deep rough vacuum", "1", "0.75", "−1012 mbar g"],
    ["Perfect vacuum", "0", "0", "−1013 mbar g"]]),
example=("Worked Example: Boiling Point Under Vacuum",
    "A water evaporator runs at 120 mbar a. Saturated water at 120 mbar a boils at about 49 °C.",
    ["At 1013 mbar a water boils at 100 °C.",
     "At 120 mbar a the boiling point falls to about 49 °C, from steam tables.",
     "If the vacuum is lost and pressure rises to 200 mbar a, the boiling point rises to about 60 °C."],
    "Holding 120 mbar a lets the plant boil water at about 49 °C, which saves steam and protects heat sensitive products. A small vacuum loss quickly raises the boiling point."),
tips=("Field Tips", [
    "Specify vacuum in absolute units such as mbar a. Gauge readings near full vacuum change with weather and altitude.",
    "Use absolute pressure transmitters for vacuum control loops; the process sees absolute pressure, not gauge.",
    "Check the transmitter and its process seal for full vacuum rating. Some diaphragm seals and fill fluids fail under deep vacuum.",
    "Look for air leaks at flanges and gland packing when vacuum drifts up; a small leak can overload an ejector or pump."]),
mistakes=("Common Mistakes", [
    "Writing \"95 % vacuum\" without saying what it means. Give the absolute pressure instead.",
    "Using a gauge transmitter for deep vacuum, where its reading carries the full atmospheric error.",
    "Selecting a remote seal with a fill fluid that boils under vacuum and gives false readings.",
    "Forgetting that vacuum vessels need vacuum rated vessels and lines, not only pressure rated ones."]),
faq=[
    ("What units are best for vacuum?", "Absolute units such as mbar a, Pa or Torr are clearest. A vacuum of 900 mbar can mean very different absolute pressures at different altitudes."),
    ("What is a Pirani gauge used for?", "A Pirani gauge measures medium vacuum, roughly 1000 to 0.001 mbar, by sensing how gas cools a heated wire.")],
)
