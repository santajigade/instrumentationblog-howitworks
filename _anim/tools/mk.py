# python3 _anim/tools/mk.py <slug> <out.webp> [width=800] [quality=65]
import sys, glob, os
from PIL import Image
slug, out = sys.argv[1], sys.argv[2]; w = int(sys.argv[3]) if len(sys.argv) > 3 else 800; q = int(sys.argv[4]) if len(sys.argv) > 4 else 65
fr = [Image.open(f).convert('RGB') for f in sorted(glob.glob(f'/tmp/anim/frames/{slug}/f*.png'))]
fr = [im.resize((w, round(im.height * w / im.width)), Image.LANCZOS) for im in fr]
fr[0].save(out, save_all=True, append_images=fr[1:], duration=80, loop=0, quality=q, method=6)
print(out, len(fr), os.path.getsize(out) // 1024, 'KB')
