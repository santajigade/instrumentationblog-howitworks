C = dict(
title="Absolute Pressure: Formula, Gauge vs Absolute & Example",
meta="Absolute pressure is measured from a perfect vacuum, so it is never negative. Gauge vs absolute diagram, altitude table, worked example and common mistakes.",
svg_h2="Absolute, Gauge and Vacuum on One Scale",
svg='''<svg viewBox="0 0 680 290" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Pressure scale showing perfect vacuum at zero absolute, atmospheric pressure line, gauge pressure above atmosphere and vacuum below it">
<path d="M120 260 H600" stroke="#1e293b" stroke-width="3"/><text x="130" y="280" font-size="13" fill="#1e293b">Perfect vacuum = 0 bar a</text>
<path d="M120 160 H600" stroke="#1e73be" stroke-width="2" stroke-dasharray="6 4"/><text x="430" y="152" font-size="13" fill="#1e73be">Atmosphere ≈ 1.013 bar a (sea level)</text>
<circle cx="250" cy="60" r="6" fill="#d9622b"/><text x="262" y="56" font-size="13" fill="#1e293b">Point A: 6.013 bar a</text>
<path d="M230 60 V258" stroke="#d9622b" stroke-width="3"/><text x="150" y="118" font-size="12" fill="#d9622b">absolute</text>
<path d="M275 62 V158" stroke="#1f9d55" stroke-width="3"/><text x="285" y="112" font-size="12" fill="#1f9d55">gauge = 5 bar g</text>
<circle cx="470" cy="210" r="6" fill="#6b3fb0"/><text x="482" y="214" font-size="13" fill="#1e293b">Point B: 0.2 bar a</text>
<path d="M450 212 V258" stroke="#d9622b" stroke-width="3"/><path d="M495 162 V208" stroke="#6b3fb0" stroke-width="3"/><text x="505" y="190" font-size="12" fill="#6b3fb0">vacuum = 0.813 bar</text>
</svg>''',
svg_cap="Absolute pressure always starts from perfect vacuum. Gauge pressure starts from the local atmosphere, so it can be negative when there is vacuum.",
table=("Standard Atmospheric Pressure by Altitude", ["Altitude", "Typical atmospheric pressure"], [
    ["Sea level", "1.013 bar a (101.3 kPa)"],
    ["500 m", "0.955 bar a"],
    ["1,000 m", "0.899 bar a"],
    ["1,500 m", "0.846 bar a"],
    ["2,000 m", "0.795 bar a"]]),
table_note="<p>Values follow the standard atmosphere. Real local pressure also moves a few percent with weather.</p>",
example=("Worked Example: Gauge to Absolute at a Hill Site",
    "A plant at 1,000 m altitude reads 4.00 bar g on a gas line. Local atmospheric pressure is about 0.899 bar a.",
    ["p<sub>abs</sub> = p<sub>gauge</sub> + p<sub>atm</sub>.",
     "p<sub>abs</sub> = 4.00 + 0.899 = 4.899 bar a.",
     "Using 1.013 bar by mistake gives 5.013 bar a, which is 2.3 % too high."],
    "Use 4.90 bar a for gas density and flow calculations. The 2.3 % pressure error would become a 2.3 % error in gas density and in standard flow."),
tips=("Field Tips", [
    "Use absolute transmitters for vacuum service, gas flow compensation and distillation columns, where small atmospheric changes matter.",
    "Label units clearly as bar a or bar g on drawings, data sheets and the DCS to avoid mix ups.",
    "An absolute transmitter left open to air should read local barometric pressure, which is a quick zero check.",
    "Convert units quickly with the <a href=\"https://www.instrumentationblog.in/unit-converters/\">pressure unit converters</a>."]),
mistakes=("Common Mistakes", [
    "Adding 1.013 bar at a high altitude site instead of the local atmospheric pressure.",
    "Feeding gauge pressure into the gas law or a flow computer that expects absolute pressure.",
    "Writing bar without a or g, which leaves the reader guessing.",
    "Zeroing an absolute transmitter to read 0 at atmosphere, which turns it into a poor gauge transmitter."]),
faq=[
    ("Can absolute pressure be negative?", "No. Zero absolute is a perfect vacuum, the lowest pressure possible, so absolute pressure is always zero or positive."),
    ("What is the difference between psia and psig?", "psia is measured from perfect vacuum and psig from local atmosphere. At sea level psia is about psig plus 14.7.")],
)
