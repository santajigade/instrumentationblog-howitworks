# Static pages: sidebar script tag (v3) after ib-footer.js, plus an inline head style that lays out
# content + sidebar columns before ads render (stops ads sizing to the old full width).
import sys, glob, re, os
PRE = open(os.path.join(os.path.dirname(__file__), 'sidebar_pre.css')).read().strip()
STYLE = '<style id="ibsx-pre">' + PRE + '</style>'
TAG = '<script src="/assets/ib-sidebar.js?v=3" defer></script>'
root = sys.argv[1]; changed = []
for f in glob.glob(root + '/**/*.html', recursive=True):
    s = open(f, encoding='utf-8', errors='surrogateescape').read()
    if 'ib-footer.js' not in s: continue
    n = re.sub(r'<script src="/assets/ib-sidebar\.js\?v=\d+" defer></script>', '', s)
    n = re.sub(r'(<script[^>]*src="/assets/ib-footer\.js"[^>]*></script>)', r'\1' + TAG, n, count=1)
    n = re.sub(r'<style id="ibsx-pre">.*?</style>', '', n, flags=re.S)
    n = n.replace('</head>', STYLE + '</head>', 1)
    if n != s:
        open(f, 'w', encoding='utf-8', errors='surrogateescape').write(n); changed.append(f)
open('changed.txt', 'w').write('\n'.join(changed))
print('CHANGED', len(changed))
