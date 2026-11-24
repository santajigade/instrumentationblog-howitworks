"""Locked featured image template for instrumentationblog.in (1200x675 WebP).
Same font, title size, positions and logo strip on every image; accent colour and illustration change per article."""
import html, io, sys
from pathlib import Path
from playwright.sync_api import sync_playwright
from PIL import Image

F = Path(__file__).parent / 'node_modules/@fontsource/poppins/files'
ICONS = {
    'opamp': '<path d="M60 40v120l110-60z"/><path d="M20 70h40M20 130h40M170 100h40"/><path d="M78 70h14M85 63v14M78 130h14"/>',
    'binary': '<path d="M10 140h30V60h30v80h30V60h30v80h30V60h30v80h20"/>',
    'diode': '<path d="M10 100h60M130 100h60"/><path d="M70 50v100l60-50z"/><path d="M130 50v100"/>',
    'power': '<rect x="30" y="40" width="140" height="120" rx="12"/><path d="M110 60l-30 45h30l-15 35"/><path d="M50 175v15M150 175v15"/>',
    'hysteresis': '<path d="M20 170h170M20 170V20"/><path d="M40 150C70 150 80 60 170 50"/><path d="M40 150C130 140 140 50 170 50"/>',
    'valve': '<path d="M20 70l80 40-80 40zM180 70l-80 40 80 40z"/><path d="M100 110V45M60 45h80"/><path d="M60 45c0-25 80-25 80 0"/>',
    'switch': '<circle cx="100" cy="100" r="70"/><path d="M100 100l40-40"/><path d="M55 140h90"/><circle cx="100" cy="100" r="8"/>',
    'ph': '<path d="M80 20h40M88 20v60l-50 85a10 10 0 0 0 9 15h106a10 10 0 0 0 9-15l-50-85V20"/><path d="M58 140h84"/>',
    'rtd': '<path d="M115 125V35a15 15 0 0 0-30 0v90a30 30 0 1 0 30 0z"/><path d="M100 60v75"/><path d="M140 50h40M140 80h30M140 110h40"/>',
    # added 24 Nov 2026
    'recorder': '<rect x="30" y="25" width="140" height="150" rx="10"/><path d="M50 60h100M50 150h100" opacity=".6"/><path d="M50 120l20-25 15 15 20-40 15 30 15-15 15 10"/><path d="M150 85l15-10"/><circle cx="150" cy="85" r="5"/>',
    'conveyor': '<circle cx="45" cy="120" r="25"/><circle cx="155" cy="120" r="25"/><path d="M45 95h110M45 145h110"/><path d="M100 95V55"/><circle cx="100" cy="45" r="12"/><path d="M112 45l30-20"/>',
    'dust': '<path d="M40 170h120l-15-110H55z"/><path d="M70 60V30h60v30"/><circle cx="85" cy="110" r="4"/><circle cx="110" cy="95" r="4"/><circle cx="120" cy="130" r="4"/><circle cx="95" cy="140" r="4"/><circle cx="75" cy="135" r="3"/>',
    # added 23 Nov 2026
    'ai': '<rect x="55" y="55" width="90" height="90" rx="12"/><path d="M80 55V25M100 55V25M120 55V25M80 145v30M100 145v30M120 145v30M55 80H25M55 100H25M55 120H25M145 80h30M145 100h30M145 120h30"/><path d="M78 125l12-50 10 30 10-30 12 50"/>',
    'orifice': '<path d="M10 60h180M10 140h180"/><path d="M95 60v30M95 140v-30M105 60v30M105 140v-30"/><path d="M60 40v20M140 40v20"/><path d="M60 40c0-15 80-15 80 0"/><path d="M20 100h55M125 100h55" opacity=".6"/>',
    'gauge': '<circle cx="100" cy="95" r="70"/><path d="M100 95l40-35"/><circle cx="100" cy="95" r="9"/><path d="M50 95h14M136 95h14M100 45v14M65 60l10 10"/><path d="M90 165h20v25h-20z"/>',
    'tank': '<path d="M45 30h110v150H45z"/><path d="M45 110h110" /><path d="M55 120h20M85 135h20M115 125h20" opacity=".6"/><path d="M100 30V10M85 10h30"/><path d="M100 30l-15 25M100 30l15 25" opacity=".6"/>',
    # added 21 Nov 2026
    'scada': '<rect x="20" y="30" width="160" height="110" rx="10"/><path d="M40 115l30-35 25 20 30-45 35 30"/><path d="M80 170h40M100 140v30"/>',
    'dcs': '<rect x="45" y="20" width="110" height="160" rx="8"/><path d="M45 60h110M45 100h110M45 140h110"/><circle cx="70" cy="40" r="6"/><circle cx="70" cy="80" r="6"/><circle cx="70" cy="120" r="6"/><circle cx="70" cy="160" r="6"/><path d="M95 40h40M95 80h40M95 120h40M95 160h40"/>',
    'shield': '<path d="M100 20l65 25v50c0 45-30 75-65 88-35-13-65-43-65-88V45z"/><rect x="75" y="95" width="50" height="40" rx="6"/><path d="M85 95V80a15 15 0 0 1 30 0v15"/>',
    'topology': '<circle cx="100" cy="100" r="18"/><circle cx="40" cy="40" r="14"/><circle cx="160" cy="40" r="14"/><circle cx="40" cy="160" r="14"/><circle cx="160" cy="160" r="14"/><path d="M87 87L52 52M113 87l35-35M87 113l-35 35M113 113l35 35"/><path d="M54 40h92M54 160h92" opacity=".6"/>',
    'turbine': '<circle cx="100" cy="100" r="75"/><circle cx="100" cy="100" r="16"/><path d="M100 84V30M100 116v54M84 100H30M116 100h54M89 89L52 52M111 111l37 37M89 111l-37 37M111 89l37-37"/>',
    'tacho': '<path d="M30 140a70 70 0 0 1 140 0"/><path d="M100 140l45-50"/><circle cx="100" cy="140" r="9"/><path d="M42 105l12 7M100 70v14M158 105l-12 7"/><path d="M50 170h100"/>',
    'threephase': '<path d="M10 100c20-60 40-60 60 0s40 60 60 0 40-60 60 0"/><path d="M10 60c20 60 40 60 60 0" opacity=".6"/><path d="M70 140c20-60 40-60 60 0s40 60 60 0" opacity=".6"/>',
    'pcb': '<rect x="65" y="65" width="70" height="70" rx="6"/><path d="M80 65V30M100 65V20M120 65V30M80 135v35M100 135v45M120 135v35M65 85H30M65 115H20M135 85h35M135 115h45"/><circle cx="30" cy="85" r="6"/><circle cx="170" cy="115" r="6"/>',
    'mcc': '<rect x="40" y="20" width="120" height="165" rx="8"/><path d="M40 75h120M40 130h120"/><path d="M60 45h30M60 100h30M60 155h30"/><circle cx="135" cy="47" r="7"/><circle cx="135" cy="102" r="7"/><circle cx="135" cy="157" r="7"/>',
    'ladder': '<path d="M25 20v160M175 20v160"/><path d="M25 70h35M70 55v30M85 55v30M85 70h45"/><circle cx="145" cy="70" r="15"/><path d="M160 70h15"/><path d="M25 135h35M70 120v30M85 120v30M85 135h90"/>',
}


def page(title, sub, cat, chips, icon, accent):
    e = html.escape
    chips_html = ''.join(f'<span class="chip">{e(c)}</span>' for c in chips)
    return f'''<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:P;font-weight:500;src:url({F}/poppins-latin-500-normal.woff2)}}
@font-face{{font-family:P;font-weight:700;src:url({F}/poppins-latin-700-normal.woff2)}}
@font-face{{font-family:P;font-weight:800;src:url({F}/poppins-latin-800-normal.woff2)}}
*{{margin:0;box-sizing:border-box}}
body{{width:1200px;height:675px;font-family:P;background:#0b2540;overflow:hidden;position:relative;color:#fff}}
.grid{{position:absolute;inset:0;background-image:linear-gradient(rgba(255,255,255,.045) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.045) 1px,transparent 1px);background-size:40px 40px}}
.bar{{position:absolute;left:0;top:0;bottom:0;width:14px;background:{accent}}}
.logo{{position:absolute;left:64px;top:48px;display:flex;align-items:center;gap:14px}}
.mark{{width:56px;height:56px;background:#ffed00;color:#008dd2;font:800 36px/56px P;text-align:center;letter-spacing:-2px}}
.site{{font:500 22px P;color:#cbd5e1}}
.cat{{position:absolute;left:64px;top:150px;font:700 18px P;letter-spacing:.12em;text-transform:uppercase;color:#0b2540;background:{accent};padding:6px 16px;border-radius:999px}}
.title{{position:absolute;left:64px;top:205px;width:640px;max-height:300px}}
.title h1{{font:800 64px/1.12 P;letter-spacing:-.01em}}
.sub{{margin-top:22px;width:640px;font:500 28px/1.3 P;color:#ffed00}}
.chips{{position:absolute;left:64px;bottom:52px;display:flex;gap:12px}}
.chip{{font:500 18px P;color:#fff;border:2px solid rgba(255,255,255,.35);border-radius:10px;padding:6px 16px}}
.panel{{position:absolute;right:56px;top:96px;width:400px;height:483px;border-radius:28px;background:rgba(255,255,255,.06);border:2px solid rgba(255,255,255,.12);display:flex;align-items:center;justify-content:center}}
.panel:before{{content:"";position:absolute;width:300px;height:300px;border-radius:50%;border:2px dashed {accent};opacity:.45}}
.panel svg{{width:250px;height:250px;fill:none;stroke:{accent};stroke-width:9;stroke-linecap:round;stroke-linejoin:round;position:relative}}
.foot{{position:absolute;right:56px;bottom:40px;width:400px;text-align:center;font:500 16px P;color:#94a3b8}}
</style></head><body><div class="grid"></div><div class="bar"></div>
<div class="logo"><div class="mark">ib</div><div class="site">instrumentationblog.in</div></div>
<div class="cat">{e(cat)}</div>
<div class="title"><h1 id="t">{e(title)}</h1><div class="sub">{e(sub)}</div></div>
<div class="chips">{chips_html}</div>
<div class="panel"><svg viewBox="0 0 200 200">{ICONS[icon]}</svg></div>
<div class="foot">Free guides, calculators and tools</div>
<script>
const t=document.getElementById('t');let s=64;while(t.scrollHeight>220&&s>44){{s-=2;t.style.fontSize=s+'px';}}
</script></body></html>'''


# One accent colour per main category (hub); the pill still shows the subcategory name.
HUB_COLORS = {
    'Process Instrumentation': '#38bdf8',  # sky blue
    'Automation': '#a78bfa',               # violet
    'Electronics': '#f472b6',              # pink
    'Electrical': '#fbbf24',               # amber
    'Interview Q&A': '#34d399',            # green
    'Industry News': '#fb923c',            # orange
}
HUB_OF = {
    'Analog Electronics': 'Electronics', 'Digital Electronics': 'Electronics', 'Electronic Components': 'Electronics',
    'Electronic Sensors': 'Electronics', 'Electronics Fundamentals': 'Electronics', 'PCB Design & Signal Integrity': 'Electronics',
    'Power Electronics & Protection': 'Electronics',
    'Design': 'Process Instrumentation', 'Calibration': 'Process Instrumentation', 'Control Valves': 'Process Instrumentation',
    'Switches': 'Process Instrumentation', 'Analytical': 'Process Instrumentation', 'Temperature': 'Process Instrumentation',
    'Analytical Measurements': 'Process Instrumentation', 'Temperature Measurement': 'Process Instrumentation',
    'Flow Measurement': 'Process Instrumentation', 'Pressure Measurement': 'Process Instrumentation', 'Level Measurement': 'Process Instrumentation',
    'PLC': 'Automation', 'SCADA': 'Automation', 'DCS': 'Automation', 'Communication': 'Automation', 'Cybersecurity': 'Automation',
    'Safety Systems': 'Automation', 'Industrial AI': 'Automation',
}

POSTS = [
    ('spm-analyzer-suspended-particulate-matter', 'SPM Analyzer', 'Working, CPCB Limits & Calculator', 'Analytical Measurements', ['High volume', 'Beta', 'µg/m³'], 'dust', None),
    ('belt-sway-switch-working-principle', 'Belt Sway Switch', 'Working, PLC Wiring & Calculator', 'Switches', ['Alarm 15°', 'Trip 25°', 'Conveyor'], 'conveyor', None),
    ('breather-valve-working-principle', 'Breather Valve Working Principle', 'Set Pressure Calculator', 'Control Valves', ['Pallets', 'API 2000', 'Vacuum'], 'valve', None),
    ('static-and-dynamic-characteristics-of-instruments', 'Static and Dynamic Characteristics', 'Table, Solved Example & Calculator', 'Calibration', ['Accuracy', 'Time constant', 'Step response'], 'gauge', None),
    ('strip-chart-recorder-working-principle', 'Strip Chart Recorder', 'Working, Types & Speed Calculator', 'Design', ['Servo pen', 'Thermal head', 'Zero & span'], 'recorder', None),
]

if __name__ == '__main__':
    out = Path(sys.argv[1] if len(sys.argv) > 1 else 'out'); out.mkdir(exist_ok=True)
    only = sys.argv[2:] or None
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path='/usr/bin/google-chrome')
        pg = b.new_page(viewport={'width': 1200, 'height': 675})
        for slug, title, sub, cat, chips, icon, _ in POSTS:
            acc = HUB_COLORS[HUB_OF[cat]]
            if only and slug not in only:
                continue
            tmp = out / f'{slug}.html'; tmp.write_text(page(title, sub, cat, chips, icon, acc), encoding='utf-8')
            pg.goto(tmp.resolve().as_uri()); pg.wait_for_timeout(250)
            png = pg.screenshot(type='png'); tmp.unlink()
            Image.open(io.BytesIO(png)).convert('RGB').save(out / f'{slug}.webp', 'WEBP', quality=88, method=6)
            print('ok', slug)
        b.close()
