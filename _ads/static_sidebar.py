# Add the sidebar script tag right after the ib-footer.js tag in static pages; print changed files.
import sys, glob, re
TAG = '<script src="/assets/ib-sidebar.js?v=1" defer></script>'
root = sys.argv[1]; changed = []
for f in glob.glob(root + '/**/*.html', recursive=True):
    s = open(f, encoding='utf-8', errors='surrogateescape').read()
    if 'ib-sidebar.js' in s or 'ib-footer.js' not in s: continue
    n = re.sub(r'(<script[^>]*src="/assets/ib-footer\.js"[^>]*></script>)', r'\1' + TAG, s, count=1)
    if n != s:
        open(f, 'w', encoding='utf-8', errors='surrogateescape').write(n); changed.append(f)
open('changed.txt', 'w').write('\n'.join(changed))
print('CHANGED', len(changed))
