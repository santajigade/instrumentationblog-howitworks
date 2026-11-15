# Converts the PNG snapshots from snap.js to WebP (1560 x 878) and removes the PNGs.
import pathlib
from PIL import Image

SITE = pathlib.Path(__file__).resolve().parent.parent / "site" / "how-it-works"
for png in sorted(SITE.glob("*/*-working-diagram.png")):
    im = Image.open(png).convert("RGB")
    if im.size != (1560, 878):
        im = im.resize((1560, 878), Image.LANCZOS)
    out = png.with_suffix(".webp")
    im.save(out, "WEBP", quality=82, method=6)
    png.unlink()
    print(out.name, out.stat().st_size // 1024, "KB")
