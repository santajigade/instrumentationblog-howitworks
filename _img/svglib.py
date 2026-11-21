import html
FONT = 'Arial, Helvetica, sans-serif'
def esc(s): return html.escape(s, quote=True)
class S:
    def __init__(self, h, title, w=800):
        self.w, self.h = w, h
        self.o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%" font-family="{FONT}">',
                  f'<title>{esc(title)}</title>', f'<rect width="{w}" height="{h}" fill="#ffffff"/>',
                  '<defs><marker id="ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#1a2b4a"/></marker></defs>']
    def t(self, x, y, s, size=18, fill='#1a2b4a', weight='normal', anchor='middle'):
        self.o.append(f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}" font-weight="{weight}" text-anchor="{anchor}">{esc(s)}</text>')
    def head(self, s, color='#1a2b4a'): self.t(self.w/2, 34, s, 24, color, 'bold')
    def box(self, x, y, w, h, lines, fill='#eef6ff', stroke='#1a2b4a', tc='#1a2b4a', size=18, bold_first=True, r=10):
        self.o.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}" stroke="{stroke}" stroke-width="2"/>')
        n = len(lines); lh = size + 6; y0 = y + h/2 - (n-1)*lh/2 + size*0.35
        for i, ln in enumerate(lines): self.t(x + w/2, y0 + i*lh, ln, size, tc, 'bold' if (bold_first and i == 0) else 'normal')
    def dia(self, cx, cy, w, h, lines, fill='#fff7e6', stroke='#1a2b4a', size=18):
        self.o.append(f'<polygon points="{cx},{cy-h/2} {cx+w/2},{cy} {cx},{cy+h/2} {cx-w/2},{cy}" fill="{fill}" stroke="{stroke}" stroke-width="2"/>')
        n = len(lines); lh = size + 4; y0 = cy - (n-1)*lh/2 + size*0.35
        for i, ln in enumerate(lines): self.t(cx, y0 + i*lh, ln, size, '#1a2b4a', 'bold')
    def ar(self, x1, y1, x2, y2, color='#1a2b4a', w=2.5, dash=None):
        d = f' stroke-dasharray="{dash}"' if dash else ''
        self.o.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{w}" marker-end="url(#ah)"{d}/>')
    def pl(self, pts, color='#1a2b4a', w=2.5, arrow=True, dash=None, fill='none'):
        d = f' stroke-dasharray="{dash}"' if dash else ''
        m = ' marker-end="url(#ah)"' if arrow else ''
        self.o.append(f'<polyline points="{" ".join(f"{a},{b}" for a,b in pts)}" fill="{fill}" stroke="{color}" stroke-width="{w}"{m}{d}/>')
    def ln(self, x1, y1, x2, y2, color='#1a2b4a', w=2.5, dash=None):
        d = f' stroke-dasharray="{dash}"' if dash else ''
        self.o.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{w}"{d}/>')
    def raw(self, s): self.o.append(s)
    def svg(self): return '\n'.join(self.o + ['</svg>'])
