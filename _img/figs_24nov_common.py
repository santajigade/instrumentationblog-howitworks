import json, sys, os, re
sys.path.insert(0, '/home/claude/instrumentationblog-howitworks/_img')
from svglib import S
OUT = '/home/claude/instrumentationblog-howitworks/_img/changes'
CH = {}
WARN = []
_box = S.box
def _chk_box(self, x, y, w, h, lines, fill='#eef6ff', stroke='#1a2b4a', tc='#1a2b4a', size=18, bold_first=True, r=10):
    for ln in lines:
        if len(ln) * 0.55 * size > w - 12: WARN.append(f'box overflow: {ln!r} w={w}')
    n = len(lines)
    if n * (size + 6) > h + 4: WARN.append(f'box too short: {lines} h={h}')
    _box(self, x, y, w, h, lines, fill, stroke, tc, size, bold_first, r)
S.box = _chk_box
def fig(slug, name, alt, caption, after, svg):
    CH.setdefault(slug, []).append(dict(name=name, alt=alt, caption=caption, after_h2=after, svg=svg))
def num(s, x, y, n, c, r=16):
    s.raw(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{c}"/>'); s.t(x, y + 6, str(n), 17, '#ffffff', 'bold')
def valve_v(s, x, y, c='#1a2b4a'):
    s.raw(f'<polygon points="{x-9},{y-11} {x+9},{y-11} {x},{y} " fill="#ffffff" stroke="{c}" stroke-width="2"/>')
    s.raw(f'<polygon points="{x-9},{y+11} {x+9},{y+11} {x},{y} " fill="#ffffff" stroke="{c}" stroke-width="2"/>')


def lint():
    bad = []
    for slug, figs in CH.items():
        pg = json.load(open(f'/home/claude/instrumentationblog-howitworks/_img/pages/{slug}.json'))
        h2 = [h['text'] for h in pg['h2s']]
        if len({f['after_h2'] for f in figs}) != 3: bad.append(f'{slug}: H2 not distinct')
        for f in figs:
            if f['after_h2'] not in h2: bad.append(f"{slug}: H2 missing {f['after_h2']}")
            na = len(f['alt'].split());  nc = len(f['caption'].split())
            if not 6 <= na <= 16: bad.append(f"{f['name']}: alt words {na}")
            if not 12 <= nc <= 35: bad.append(f"{f['name']}: caption words {nc}")
            if len(f['name']) > 70: bad.append(f"{f['name']}: name long")
            for fld in ('alt', 'caption'):
                if re.search('[-–—]', f[fld]): bad.append(f"{f['name']}: dash in {fld}")
            for m in re.finditer(r'<(text|title)[^>]*>([^<]*)<', f['svg']):
                if re.search('[-–—]', m.group(2)): bad.append(f"{f['name']}: dash in svg text {m.group(2)!r}")
            for m in re.finditer(r'<text x="([\d.]+)" y="[\d.]+" font-size="([\d.]+)"[^>]*text-anchor="(\w+)">([^<]*)<', f['svg']):
                x, sz, an, tx = float(m.group(1)), float(m.group(2)), m.group(3), m.group(4)
                import html as H; wdt = len(H.unescape(tx)) * 0.55 * sz
                l = x - wdt / 2 if an == 'middle' else (x if an == 'start' else x - wdt)
                if l < 2 or l + wdt > 798: bad.append(f"{f['name']}: off canvas {tx!r}")
                if sz < 17: bad.append(f"{f['name']}: small text")
        fk = pg['focus'].lower().replace(' ', '-')
        if not any(pg['focus'].lower() in f['alt'].lower() for f in figs): bad.append(f'{slug}: no focus kw in alt')
        for f in figs:
            if not f['name'].startswith(fk): bad.append(f"{f['name']}: not starting with {fk}")
    return bad

def main():
    import cairosvg
    out = sys.argv[1] if len(sys.argv) > 1 else None
    for slug, figs in CH.items():
        json.dump({'slug': slug, 'figs': figs}, open(os.path.join(OUT, slug + '.json'), 'w'), ensure_ascii=False, indent=1)
        if out:
            for f in figs: cairosvg.svg2png(bytestring=f['svg'].encode(), write_to=os.path.join(out, f['name'] + '.png'), output_width=800)
    print('WARN', WARN); print('LINT', lint())
    print({k: [f['name'] for f in v] for k, v in CH.items()})
