C = dict(
title="Vena Contracta: Definition, Location & Worked Example",
meta="Vena contracta is the narrowest point of the jet after an orifice, about 0.3D to 0.8D downstream. Diagram, worked example, field tips and common mistakes.",
svg_h2="How the Vena Contracta Forms",
svg='''<svg viewBox="0 0 680 300" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Diagram of flow through an orifice plate showing the jet narrowing to the vena contracta and the pressure profile along the pipe">
<rect x="20" y="40" width="640" height="10" fill="#94a3b8"/><rect x="20" y="170" width="640" height="10" fill="#94a3b8"/>
<rect x="196" y="50" width="8" height="42" fill="#1e293b"/><rect x="196" y="128" width="8" height="42" fill="#1e293b"/>
<g fill="none" stroke="#1e73be" stroke-width="2.5">
<path d="M30 70 C150 70 180 95 200 96 C240 98 260 102 300 102 C380 102 460 70 650 66"/>
<path d="M30 110 H650"/>
<path d="M30 150 C150 150 180 125 200 124 C240 122 260 118 300 118 C380 118 460 150 650 154"/></g>
<path d="M300 95 V125" stroke="#d9622b" stroke-width="3"/>
<text x="300" y="30" text-anchor="middle" font-size="15" font-weight="700" fill="#d9622b">Vena contracta</text>
<path d="M300 34 V88" stroke="#d9622b" stroke-width="1.5" stroke-dasharray="4 3"/>
<text x="200" y="30" text-anchor="middle" font-size="14" fill="#1e293b">Orifice plate</text>
<text x="60" y="64" font-size="13" fill="#5b6576">Flow</text>
<g font-size="13" fill="#5b6576"><text x="20" y="206">Pressure profile</text></g>
<path d="M30 230 H180 C200 230 220 284 300 286 C380 286 470 252 650 250" fill="none" stroke="#1f9d55" stroke-width="3"/>
<circle cx="300" cy="286" r="5" fill="#d9622b"/>
<text x="318" y="282" font-size="13" fill="#1e293b">lowest pressure</text>
<text x="560" y="242" font-size="13" fill="#1e293b">recovered</text>
<text x="40" y="248" font-size="13" fill="#1e293b">upstream</text>
</svg>''',
svg_cap="The jet keeps narrowing after the bore, reaches its smallest area at the vena contracta, then expands again. Pressure is lowest at that point and only partly recovers.",
svg_text="<p>The jet area at the vena contracta is about 0.6 to 0.65 times the bore area for a sharp edged orifice. This ratio is called the coefficient of contraction (C<sub>c</sub>), and it is the main reason the orifice discharge coefficient is close to 0.6.</p>",
table=("Vena Contracta at a Glance", ["Item", "Typical value"], [
    ["Coefficient of contraction, C<sub>c</sub> (sharp edged orifice)", "about 0.61"],
    ["Location downstream of the plate", "about 0.3D to 0.8D, closer at high beta ratio"],
    ["Velocity", "highest along the pipe"],
    ["Static pressure", "lowest along the pipe"],
    ["Where cavitation or flashing starts", "at the vena contracta"]]),
table_note="<p>D is the inside pipe diameter. ISO 5167 and ASME MFC-3M give the exact tap locations for each tapping type.</p>",
example=("Worked Example: Jet Velocity at the Vena Contracta",
    "Water flows at 10 m³/h through a 100 mm pipe with a 50 mm sharp edged orifice. Take C<sub>c</sub> = 0.61 and density 1000 kg/m³.",
    ["Bore area = π ÷ 4 × 0.050² = 0.001963 m². Jet area = 0.61 × 0.001963 = 0.001198 m².",
     "Flow = 10 ÷ 3600 = 0.002778 m³/s. Jet velocity = 0.002778 ÷ 0.001198 = 2.32 m/s.",
     "Pipe velocity = 0.002778 ÷ 0.007854 = 0.354 m/s.",
     "Ideal pressure drop to the vena contracta = 0.5 × 1000 × (2.32² − 0.354²) = 2627 Pa."],
    "The pressure at the vena contracta is about 26 mbar below the upstream pressure, and the jet is about 6.5 times faster than the pipe flow."),
tips=("Field Tips", [
    "For liquid service, check that the pressure at the vena contracta stays well above the vapour pressure. If it does not, the orifice or valve will cavitate even when the downstream gauge looks fine.",
    "Control valve sizing uses the liquid pressure recovery factor F<sub>L</sub>, which links the valve pressure drop to the vena contracta pressure. A low F<sub>L</sub> valve cavitates sooner.",
    "Most plants use flange taps on lines 50 mm and above because the tap position does not change with beta ratio, which makes plate changes easier.",
    "Use the <a href=\"https://www.instrumentationblog.in/calculators/flow/orifice-flow-calculator/\">orifice flow calculator</a> to see how DP and flow change when you change the bore."]),
mistakes=("Common Mistakes", [
    "Treating the bore diameter as the jet diameter. The jet is smaller, so velocity is higher than a simple bore calculation suggests.",
    "Using vena contracta taps with a discharge coefficient worked out for flange or corner taps. The coefficient must match the tapping type.",
    "Measuring permanent pressure loss at the vena contracta. The loss is measured about 6D downstream, after the pressure has recovered.",
    "Ignoring cavitation noise and damage on high DP liquid orifices, especially restriction orifices on pump minimum flow lines."]),
faq=[
    ("Where exactly is the vena contracta located?", "It sits a short distance downstream of the plate, roughly 0.3D to 0.8D depending on beta ratio. It moves closer to the plate as the beta ratio increases."),
    ("What is the coefficient of contraction?", "It is the jet area at the vena contracta divided by the bore area. For a sharp edged orifice it is about 0.61.")],
)
