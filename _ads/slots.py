# AdSense units (created 24 Nov 2026). Old single unit 5950781970 is replaced by position.
import re
OLD = 'data-ad-slot="5950781970"'
TOP, MID1, MID2, END, MULTI = '7215194230', '6552849252', '7839764783', '5046401284', '3541747929'
QUOTE = '<div class="dcp-quote">'
MULTIPLEX = ('<div class="whc-ad"><div class="whc-ad-label"><div class="line"></div><span>Advertisement</span><div class="line"></div></div>'
             '<ins class="adsbygoogle" style="display:block" data-ad-format="autorelaxed" data-ad-client="ca-pub-3931314195561246" data-ad-slot="' + MULTI + '"></ins>'
             '<script>(adsbygoogle = window.adsbygoogle || []).push({});</script></div>\n')

def order(n):
    """slot ids for n ads in document order"""
    if n <= 0: return []
    if n == 1: return [TOP]
    mids = [MID1 if i % 2 == 0 else MID2 for i in range(n - 2)]
    return [TOP] + mids + [END]

def rewrite(html):
    seq = iter(order(html.count(OLD)))
    html = re.sub(re.escape(OLD), lambda m: f'data-ad-slot="{next(seq)}"', html)
    if MULTI not in html and QUOTE in html:
        html = html.replace(QUOTE, MULTIPLEX + QUOTE, 1)
    return html
