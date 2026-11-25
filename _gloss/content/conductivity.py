C = dict(
title="Conductivity: Formula, Units, Water Ranges & Example",
meta="Conductivity shows how well a solution carries current, in µS/cm or mS/cm. Typical water ranges table, cell constant example, field tips and mistakes.",
svg_h2="How a Conductivity Cell Measures",
svg='''<svg viewBox="0 0 680 270" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Two electrode conductivity cell in a solution with an AC source and meter, showing ions moving between electrodes">
<rect x="160" y="80" width="360" height="160" rx="14" fill="#eaf2fe" stroke="#1e293b" stroke-width="2"/>
<rect x="250" y="60" width="18" height="150" fill="#5b6576"/><rect x="410" y="60" width="18" height="150" fill="#5b6576"/>
<path d="M259 60 V30 H419 V60" stroke="#1e293b" stroke-width="2" fill="none"/>
<circle cx="339" cy="30" r="18" fill="#fff" stroke="#d9622b" stroke-width="2"/><text x="339" y="35" text-anchor="middle" font-size="13" fill="#d9622b">AC</text>
<g font-size="15" font-weight="700"><text x="300" y="130" fill="#1e73be">+</text><text x="350" y="160" fill="#d9622b">−</text><text x="320" y="190" fill="#1e73be">+</text><text x="370" y="120" fill="#d9622b">−</text><text x="290" y="175" fill="#d9622b">−</text><text x="380" y="190" fill="#1e73be">+</text></g>
<path d="M280 225 H400" stroke="#1f9d55" stroke-width="2" marker-end="url(#a)"/><defs><marker id="a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 Z" fill="#1f9d55"/></marker></defs>
<g font-size="13" fill="#1e293b"><text x="530" y="120">ions carry</text><text x="530" y="138">the current</text><text x="40" y="120">electrode area A</text><text x="40" y="138">spacing L</text><text x="40" y="156">K = L ÷ A</text></g>
</svg>''',
svg_cap="More dissolved ions carry more current between the electrodes. The meter measures conductance and multiplies by the cell constant K to give conductivity.",
table=("Typical Conductivity Ranges at 25 °C", ["Water or solution", "Typical conductivity", "Suggested cell constant"], [
    ["Ultrapure water", "0.055 µS/cm", "0.01 /cm"],
    ["Boiler feed or condensate", "0.1 to 10 µS/cm", "0.01 to 0.1 /cm"],
    ["Drinking water", "50 to 800 µS/cm", "0.1 to 1 /cm"],
    ["Cooling tower water", "1 to 5 mS/cm", "1 /cm or inductive"],
    ["Sea water", "about 53 mS/cm", "10 /cm or inductive"],
    ["Caustic or acid CIP solutions", "50 to 500 mS/cm", "inductive (toroidal)"]]),
example=("Worked Example: Temperature Compensation",
    "A cooling water sample reads an uncompensated 2,200 µS/cm at 40 °C. Use the common linear coefficient of 2 % per °C, referred to 25 °C.",
    ["Temperature difference = 40 − 25 = 15 °C.",
     "Correction factor = 1 + 0.02 × 15 = 1.30.",
     "Conductivity at 25 °C = 2,200 ÷ 1.30 = 1,692 µS/cm."],
    "The compensated value is about 1,690 µS/cm. Without compensation the reading would be 30 % high and could trigger an unnecessary blowdown."),
tips=("Field Tips", [
    "Match the cell constant to the range: low K for pure water, higher K or an inductive sensor for dirty and high conductivity liquids.",
    "Mount the sensor where the pipe stays full and air bubbles cannot collect on the electrodes.",
    "Calibrate with a standard solution close to the normal process value, and record the temperature at the same time.",
    "Clean contacting electrodes regularly. Scale and oil films lower the reading slowly over weeks."]),
mistakes=("Common Mistakes", [
    "Reporting uncompensated values and comparing them with limits quoted at 25 °C.",
    "Using a contacting cell in caustic or slurry service, where it fouls or polarises quickly.",
    "Treating conductivity as TDS without a proper conversion factor, which depends on the dissolved salts.",
    "Installing the sensor at the top of a horizontal pipe where air pockets cause a noisy, low reading."]),
faq=[
    ("What is a typical temperature coefficient for conductivity?", "Many natural waters change by about 2 % per °C, so meters often use 2 %/°C referred to 25 °C. Pure water and acids need special compensation curves."),
    ("When should I use an inductive conductivity sensor?", "Use it for high conductivity, dirty, coating or corrosive liquids. It has no exposed electrodes, so it does not polarise or foul as quickly.")],
)
