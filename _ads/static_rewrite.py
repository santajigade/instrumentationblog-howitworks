# Rewrite old ad slot by position in downloaded static pages; print changed files.
import sys, os, glob
sys.path.insert(0, os.path.dirname(__file__)); from slots import OLD, order
import re
root = sys.argv[1]; changed = []
for f in glob.glob(root + '/**/*.html', recursive=True):
    s = open(f, encoding='utf-8', errors='surrogateescape').read()
    k = s.count(OLD)
    if not k: continue
    seq = iter(order(k))
    s = re.sub(re.escape(OLD), lambda m: f'data-ad-slot="{next(seq)}"', s)
    open(f, 'w', encoding='utf-8', errors='surrogateescape').write(s); changed.append(f)
open('changed.txt', 'w').write('\n'.join(changed))
print('CHANGED', len(changed))
