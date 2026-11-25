# Enrich glossary term pages: new title/meta, extra sections (diagram, worked example, tips, mistakes) and extra FAQs.
# Input: _static/glossary/<slug>/index.html (fetched from server) + _gloss/content/<slug>.py (dict C)
# Output: site/glossary/<slug>/index.html (deployed by deploy.yml)
import sys, os, re, json, html as H, runpy
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSS = ('<style id="gl-x">.ibuc .glx-fig{margin:6px 0 4px;text-align:center}.ibuc .glx-fig svg{width:100%;height:auto;max-width:680px}'
       '.ibuc .glx-fig figcaption{font-size:14px;color:var(--m);margin-top:6px}'
       '.ibuc .glx-steps{counter-reset:s;list-style:none;margin:8px 0 0;padding:0}.ibuc .glx-steps li{counter-increment:s;position:relative;padding:10px 12px 10px 46px;margin:0 0 8px;background:var(--l);border:1px solid var(--b);border-radius:10px}'
       '.ibuc .glx-steps li:before{content:counter(s);position:absolute;left:12px;top:10px;width:24px;height:24px;border-radius:50%;background:var(--gc,#1e73be);color:#fff;font-weight:700;font-size:13px;display:flex;align-items:center;justify-content:center}'
       '.ibuc .glx-ans{margin:10px 0 0;padding:12px 14px;border-left:4px solid var(--g);background:#eefaf3;border-radius:8px;font-weight:600}'
       '.ibuc .glx-list{margin:8px 0 0;padding-left:20px}.ibuc .glx-list li{margin:0 0 8px}'
       '.ibuc .glx-tbl{width:100%;border-collapse:collapse;font-size:15px}.ibuc .glx-tbl th,.ibuc .glx-tbl td{border:1px solid var(--b);padding:8px 10px;text-align:left}.ibuc .glx-tbl th{background:var(--l)}'
       '.ibuc .glx-bad li::marker{color:#c0392b}.ibuc .glx-good li::marker{color:var(--g)}</style>')
def sec(h, body): return f'<section class="ibuc-card"><h2>{h}</h2>{body}</section>\n'
def build(slug):
    src = f'{ROOT}/_static/glossary/{slug}/index.html'
    s = open(src, encoding='utf-8').read()
    C = runpy.run_path(f'{ROOT}/_gloss/content/{slug}.py')['C']
    # head: title, description, og/twitter
    t, d = C['title'], C['meta']
    assert len(t) <= 60 and len(d) <= 160, (slug, len(t), len(d))
    for txt in (t, d) + tuple(x for q in C['faq'] for x in q):
        assert '—' not in txt and '–' not in txt, slug
    s = re.sub(r'<title>.*?</title>', f'<title>{H.escape(t, False)}</title>', s, count=1)
    s = re.sub(r'(<meta name="description" content=")[^"]*(")', lambda m: m.group(1) + H.escape(d) + m.group(2), s, count=1)
    s = re.sub(r'(<meta (?:property|name)="(?:og|twitter):title" content=")[^"]*(")', lambda m: m.group(1) + H.escape(t) + m.group(2), s)
    s = re.sub(r'(<meta (?:property|name)="(?:og|twitter):description" content=")[^"]*(")', lambda m: m.group(1) + H.escape(d) + m.group(2), s)
    if 'id="gl-x"' not in s: s = s.replace('</head>', CSS + '</head>', 1)
    # body sections after the Formula card (or the Explained card)
    cards = list(re.finditer(r'<section class="ibuc-card"><h2>(.*?)</h2>.*?</section>', s, flags=re.S))
    anchor = next((m for m in cards if m.group(1).strip().endswith('Formula')), None) or next(m for m in cards if 'Explained' in m.group(1))
    add = ''
    if C.get('svg'):
        add += sec(C['svg_h2'], f'<figure class="glx-fig">{C["svg"]}<figcaption>{C["svg_cap"]}</figcaption></figure>' + C.get('svg_text', ''))
    if C.get('table'):
        hd, rows = C['table'][1], C['table'][2]
        add += sec(C['table'][0], '<div style="overflow-x:auto"><table class="glx-tbl"><thead><tr>' + ''.join(f'<th>{x}</th>' for x in hd) + '</tr></thead><tbody>' +
                   ''.join('<tr>' + ''.join(f'<td>{c}</td>' for c in r) + '</tr>' for r in rows) + '</tbody></table></div>' + C.get('table_note', ''))
    ex = C['example']
    add += sec(ex[0], f'<p>{ex[1]}</p><ol class="glx-steps">' + ''.join(f'<li>{x}</li>' for x in ex[2]) + f'</ol><p class="glx-ans">{ex[3]}</p>')
    add += sec(C['tips'][0], '<ul class="glx-list glx-good">' + ''.join(f'<li>{x}</li>' for x in C['tips'][1]) + '</ul>')
    add += sec(C['mistakes'][0], '<ul class="glx-list glx-bad">' + ''.join(f'<li>{x}</li>' for x in C['mistakes'][1]) + '</ul>')
    if '<!--glx-->' in s: raise SystemExit('already enriched ' + slug)
    s = s[:anchor.end()] + '\n<!--glx-->' + add + s[anchor.end():]
    # FAQ: visible + schema
    faq_html = ''.join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q, a in C['faq'])
    s = re.sub(r'(<section class="ibuc-card"><h2>Frequently Asked Questions</h2>.*?)(</section>)', lambda m: m.group(1) + faq_html + m.group(2), s, count=1, flags=re.S)
    def fix_ld(m):
        dj = json.loads(m.group(1)); g = dj.get('@graph', [dj])
        for x in g:
            if x.get('@type') == 'FAQPage':
                x['mainEntity'] += [{'@type': 'Question', 'name': H.unescape(re.sub('<[^>]+>', '', q)), 'acceptedAnswer': {'@type': 'Answer', 'text': H.unescape(re.sub('<[^>]+>', '', a))}} for q, a in C['faq']]
        return '<script type="application/ld+json">' + json.dumps(dj, ensure_ascii=False) + '</script>'
    s = re.sub(r'<script type="application/ld\+json">(.*?)</script>', fix_ld, s, flags=re.S)
    out = f'{ROOT}/site/glossary/{slug}/index.html'
    os.makedirs(os.path.dirname(out), exist_ok=True); open(out, 'w', encoding='utf-8').write(s)
    vis = H.unescape(re.sub(r'<[^>]+>', ' ', re.sub(r'<(script|style|svg)\b.*?</\1>', ' ', s[s.find('<main'):s.find('</main>')], flags=re.S)))
    for ch in '—–':
        assert ch not in vis, (slug, 'dash in visible text')
    print(slug, 'words', len(vis.split()), 'title', len(t), 'meta', len(d))
if __name__ == '__main__':
    for sl in sys.argv[1:]: build(sl)
