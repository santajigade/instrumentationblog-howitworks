C = dict(
title="Specific Gravity: Formula, SG Table & Level Example",
meta="Specific gravity (SG) is liquid density divided by water density. Common SG values table, level transmitter worked example, field tips and mistakes.",
svg_h2="Same Level, Different Pressure",
svg='''<svg viewBox="0 0 680 270" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Three tanks filled to the same height with liquids of different specific gravity giving different bottom pressures">
<g stroke="#1e293b" stroke-width="3" fill="none"><path d="M60 40 V220 H200 V40"/><path d="M270 40 V220 H410 V40"/><path d="M480 40 V220 H620 V40"/></g>
<rect x="63" y="80" width="134" height="137" fill="#f5ddb0"/><rect x="273" y="80" width="134" height="137" fill="#c9dcf8"/><rect x="483" y="80" width="134" height="137" fill="#ddd0f3"/>
<path d="M30 80 H50 M30 217 H50 M40 80 V217" stroke="#5b6576" stroke-width="2"/><text x="10" y="155" font-size="13" fill="#1e293b">2 m</text>
<g font-size="14" text-anchor="middle" fill="#1e293b" font-weight="700"><text x="130" y="30">Diesel, SG 0.85</text><text x="340" y="30">Water, SG 1.00</text><text x="550" y="30">Brine, SG 1.20</text></g>
<g font-size="13" text-anchor="middle" fill="#1e293b"><text x="130" y="245">16.7 kPa</text><text x="340" y="245">19.6 kPa</text><text x="550" y="245">23.5 kPa</text></g>
<text x="340" y="265" text-anchor="middle" font-size="12" fill="#5b6576">pressure at the bottom = SG × 9.81 × height (kPa, with height in m)</text>
</svg>''',
svg_cap="A DP or pressure level transmitter measures pressure, not height. The same 2 m of liquid gives a different signal for each SG.",
table=("Typical Specific Gravity Values (about 15 to 20 °C)", ["Liquid", "Typical SG"], [
    ["Petrol (gasoline)", "0.72 to 0.75"],
    ["Diesel", "0.82 to 0.86"],
    ["Water", "1.00"],
    ["Sea water", "1.02 to 1.03"],
    ["Saturated brine (NaCl)", "about 1.2"],
    ["Sulphuric acid 98 %", "about 1.84"]]),
table_note="<p>Values change with temperature and grade. Always take the SG at operating temperature from the process data sheet.</p>",
example=("Worked Example: Ranging a DP Level Transmitter",
    "A tank holds diesel with SG 0.85. The measuring range is 0 to 3 m above the lower tap, and the tank is vented.",
    ["Pressure per metre = SG × 9.81 kPa = 0.85 × 9.81 = 8.34 kPa per m.",
     "Span = 3 × 8.34 = 25.0 kPa.",
     "Calibrated range = 0 to 25.0 kPa, which is 0 to 250 mbar."],
    "Range the transmitter 0 to 250 mbar. If the same tank were filled with water, 3 m would give 294 mbar and the reading would be 18 % too high."),
tips=("Field Tips", [
    "Use the SG at operating temperature. Many oils lose about 0.07 % of density for every 1 °C rise.",
    "When a tank changes product, update the SG in the transmitter or DCS, otherwise the level reading moves without any real change.",
    "Two pressure transmitters a known distance apart give a live density and SG measurement for blended or changing liquids.",
    "Check your range quickly with the <a href=\"https://www.instrumentationblog.in/calculators/\">level calculators</a>."]),
mistakes=("Common Mistakes", [
    "Using SG at 15 °C for a hot process, which makes the level read wrong at operating temperature.",
    "Forgetting the SG of the seal fluid in capillary or wet leg installations when calculating zero suppression or elevation.",
    "Mixing SG with API gravity or Baumé scales, which are different numbers for the same liquid.",
    "Assuming SG has units. It is a ratio, so it has none."]),
faq=[
    ("How do I convert SG to density?", "Multiply SG by the reference water density, usually 1000 kg/m³ (or 999 kg/m³ at 15 °C). SG 0.85 is about 850 kg/m³."),
    ("Does specific gravity change with temperature?", "Yes. Most liquids expand when heated, so their SG falls. That is why data sheets state SG at a given temperature.")],
)
