C = dict(
title="ADC Resolution: Formula, Bits Table & 4 to 20 mA Example",
meta="ADC resolution is the number of bits an ADC uses, which sets its smallest step. Bits table, 4 to 20 mA worked example, field tips and common mistakes.",
svg_h2="How Resolution Turns a Signal into Steps",
svg='''<svg viewBox="0 0 680 280" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Analog ramp signal compared with a 3 bit staircase showing 8 output codes">
<line x1="60" y1="240" x2="640" y2="240" stroke="#1e293b" stroke-width="2"/><line x1="60" y1="240" x2="60" y2="30" stroke="#1e293b" stroke-width="2"/>
<path d="M60 240 L620 40" stroke="#1e73be" stroke-width="3" fill="none"/>
<path d="M60 240 H130 V215 H200 V190 H270 V165 H340 V140 H410 V115 H480 V90 H550 V65 H620" stroke="#d9622b" stroke-width="3" fill="none"/>
<g font-size="13" fill="#1e293b"><text x="66" y="262">0</text><text x="590" y="262">Full scale</text>
<text x="70" y="28">Output code</text></g>
<g font-size="12" fill="#5b6576"><text x="30" y="244">000</text><text x="30" y="219">001</text><text x="30" y="194">010</text><text x="30" y="169">011</text><text x="30" y="144">100</text><text x="30" y="119">101</text><text x="30" y="94">110</text><text x="30" y="69">111</text></g>
<rect x="430" y="170" width="200" height="56" rx="8" fill="#fff" stroke="#dde3ee"/>
<path d="M444 186 H470" stroke="#1e73be" stroke-width="3"/><text x="478" y="191" font-size="13" fill="#1e293b">analog input</text>
<path d="M444 210 H470" stroke="#d9622b" stroke-width="3"/><text x="478" y="215" font-size="13" fill="#1e293b">3 bit ADC output</text>
</svg>''',
svg_cap="A 3 bit converter has only 8 codes, so a smooth signal becomes a coarse staircase. Each extra bit doubles the number of steps.",
svg_text="<p>The step size is also called one LSB (least significant bit). Any signal change smaller than one LSB is invisible to the converter.</p>",
table=("Resolution by Number of Bits", ["Bits", "Steps (2ⁿ)", "Step on 16 mA span (4 to 20 mA)", "Step on 0 to 10 V"], [
    ["10", "1,024", "15.6 µA", "9.77 mV"],
    ["12", "4,096", "3.91 µA", "2.44 mV"],
    ["14", "16,384", "0.98 µA", "0.61 mV"],
    ["16", "65,536", "0.24 µA", "0.15 mV"],
    ["24", "16,777,216", "0.001 µA", "0.6 µV"]]),
table_note="<p>Many PLC cards do not use the full 2ⁿ range for the live signal. Check the card manual for its count range, for example 0 to 27,648 or 0 to 32,000.</p>",
example=("Worked Example: Temperature Resolution of a 4 to 20 mA Input",
    "A transmitter ranged 0 to 400 °C feeds a 12 bit PLC analog input that uses 4,000 counts for 4 to 20 mA.",
    ["Current per count = 16 mA ÷ 4,000 = 0.004 mA.",
     "Temperature per mA = 400 °C ÷ 16 mA = 25 °C per mA.",
     "Temperature per count = 0.004 × 25 = 0.1 °C."],
    "The PLC can resolve 0.1 °C steps. Accuracy is still set by the transmitter and sensor, which are usually far worse than 0.1 °C."),
tips=("Field Tips", [
    "Pick resolution from the process need. A level that is controlled to ±1 % does not need a 24 bit card.",
    "If a reading jumps by one count, that is resolution. If it wanders by many counts, look for noise, earthing or a loose terminal.",
    "Filtering and averaging in the PLC can smooth noise, but they cannot create detail that the converter never saw.",
    "Use the <a href=\"https://www.instrumentationblog.in/calculators/\">4 to 20 mA calculators</a> to convert counts and mA to engineering units quickly."]),
mistakes=("Common Mistakes", [
    "Calling resolution accuracy. A 16 bit card with 0.1 % accuracy is still only accurate to 0.1 % of span.",
    "Scaling with 2ⁿ when the card uses a smaller count range, which gives a wrong engineering value.",
    "Ignoring that the 0 to 4 mA part of the range is unused on many cards, which wastes about 20 % of the counts.",
    "Choosing more bits to fix a noisy signal instead of fixing shielding and grounding."]),
faq=[
    ("What is one LSB?", "One LSB is the smallest step an ADC can show, equal to the input range divided by 2ⁿ. It is the resolution in signal units."),
    ("Is a 16 bit ADC always better than a 12 bit ADC?", "It has finer steps, but real performance also depends on noise, linearity and drift. A good 12 bit input can beat a noisy 16 bit one.")],
)
