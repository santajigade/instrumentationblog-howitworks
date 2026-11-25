C = dict(
title="Discharge Coefficient: Formula, Typical Values & Example",
meta="Discharge coefficient (C) corrects ideal DP flow for real losses: about 0.6 for orifices and 0.98 to 0.99 for venturis. Values table, worked example and tips.",
svg_h2="Why Real Flow Is Lower Than Ideal Flow",
svg='''<svg viewBox="0 0 680 260" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Bar chart comparing typical discharge coefficients of orifice plate, flow nozzle and venturi tube">
<line x1="80" y1="220" x2="640" y2="220" stroke="#1e293b" stroke-width="2"/><line x1="80" y1="220" x2="80" y2="30" stroke="#1e293b" stroke-width="2"/>
<g font-size="12" fill="#5b6576"><text x="40" y="224">0</text><text x="34" y="129">0.5</text><text x="34" y="34">1.0</text></g>
<path d="M80 125 H640 M80 30 H640" stroke="#dde3ee" stroke-dasharray="4 4"/>
<rect x="130" y="106" width="110" height="114" fill="#d9622b"/><text x="185" y="98" text-anchor="middle" font-size="14" font-weight="700" fill="#1e293b">≈ 0.60</text>
<rect x="290" y="42" width="110" height="178" fill="#1e73be"/><text x="345" y="34" text-anchor="middle" font-size="14" font-weight="700" fill="#1e293b">≈ 0.99</text>
<rect x="450" y="34" width="110" height="186" fill="#1f9d55"/><text x="505" y="26" text-anchor="middle" font-size="14" font-weight="700" fill="#1e293b">≈ 0.98 to 0.995</text>
<g font-size="13" fill="#1e293b" text-anchor="middle"><text x="185" y="242">Orifice plate</text><text x="345" y="242">Flow nozzle</text><text x="505" y="242">Venturi tube</text></g>
</svg>''',
svg_cap="A sharp edged orifice loses much more to jet contraction and friction than a smooth nozzle or venturi, so its coefficient is far below 1.",
table=("Typical Discharge Coefficients", ["Flow element", "Typical C", "Standard", "Notes"], [
    ["Orifice plate (flange or corner taps)", "about 0.60", "ISO 5167-2", "Calculated with the Reader Harris Gallagher equation; varies with beta and Reynolds number"],
    ["ISA 1932 nozzle", "about 0.95 to 0.99", "ISO 5167-3", "Depends on beta and Reynolds number"],
    ["Classical venturi tube", "about 0.984 to 0.995", "ISO 5167-4", "Low permanent pressure loss"],
    ["Wedge or cone meter", "about 0.7 to 0.85", "ISO 5167-5 (cone)", "Usually set by flow calibration"]]),
example=("Worked Example: Real Flow Through an Orifice",
    "Water at 1000 kg/m³ flows through a 50 mm bore in a 100 mm pipe (β = 0.5). The DP is 25 kPa and C = 0.605.",
    ["Bore area = π ÷ 4 × 0.050² = 0.001963 m². √(1 − β⁴) = √(1 − 0.0625) = 0.9682.",
     "Ideal flow = 0.001963 ÷ 0.9682 × √(2 × 25,000 ÷ 1000) = 0.002028 × 7.071 = 0.01434 m³/s.",
     "Real flow = C × ideal flow = 0.605 × 0.01434 = 0.008676 m³/s."],
    "Real flow is about 31.2 m³/h, against an ideal 51.6 m³/h. Leaving C out would overstate flow by about 65 %."),
tips=("Field Tips", [
    "C for an orifice changes slightly with Reynolds number, so a flow computer that recalculates it gives better accuracy across the range.",
    "A worn or rounded orifice edge raises the real coefficient, so the meter reads low. Inspect the edge at every shutdown.",
    "Keep the straight pipe lengths given in ISO 5167, because swirl and distorted profiles also shift the effective coefficient.",
    "Run the numbers with the <a href=\"https://www.instrumentationblog.in/calculators/flow/orifice-flow-calculator/\">orifice flow calculator</a> before changing a plate or range."]),
mistakes=("Common Mistakes", [
    "Using C = 0.61 for every orifice calculation instead of the standard equation for the actual beta, taps and Reynolds number.",
    "Applying an orifice coefficient to a venturi or nozzle, or the reverse.",
    "Installing a plate backwards, which turns a sharp edge into a bevelled entry and changes C a lot.",
    "Confusing discharge coefficient with flow coefficient Cv, which is a valve sizing term."]),
faq=[
    ("Why is the orifice discharge coefficient about 0.6?", "Most of the loss comes from the jet narrowing to the vena contracta, whose area is about 0.61 times the bore. Friction adds a small extra loss."),
    ("Is discharge coefficient the same as Cv?", "No. C is a dimensionless ratio for DP flow elements. Cv is a valve capacity figure in US gallons per minute at 1 psi drop.")],
)
