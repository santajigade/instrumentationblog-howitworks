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
    # added 21 Nov 2026
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
    ('tachometer-working-principle-types', 'Tachometer Working Principle', 'Types and RPM Calculator', 'Electronic Sensors', ['RPM Formula', 'Hall Sensor', 'PPR'], 'tacho', None),
    ('why-three-phase-voltage-is-440v', 'Why Three Phase Voltage Is 440V', 'Formula, Chart and Calculator', 'Electronics Fundamentals', ['√3 Rule', '415 V', 'Phasor'], 'threephase', None),
    ('pcb-propagation-delay-calculation', 'PCB Propagation Delay', 'Formula, Calculator and Solved Example', 'PCB Design & Signal Integrity', ['Microstrip', 'Stripline', 'Skew'], 'pcb', None),
    ('intelligent-mcc-imcc', 'Intelligent MCC (iMCC)', 'Diagram, Calculator and Table', 'Power Electronics & Protection', ['iMCC', 'Smart Relay', 'Profinet'], 'mcc', None),
    ('instruction-list-plc-programming', 'Instruction List PLC Programming', 'Examples and Calculator', 'PLC', ['IEC 61131 3', 'LD AND ST', 'Ladder to IL'], 'ladder', None),
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
