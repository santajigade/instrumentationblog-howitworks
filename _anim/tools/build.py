# python3 _anim/tools/build.py <slug> "<Footer title>"  -> /tmp/anim/site/<slug>/index.html from _anim/scenes/<slug>.js
import sys, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / '_src'))
import scenes
slug, title = sys.argv[1], sys.argv[2]
js = scenes.COMMON.replace('@@SCENE@@', (ROOT / '_anim/scenes' / f'{slug}.js').read_text())
html = f'''<!doctype html><html><head><meta charset="utf-8"></head><body style="margin:0;background:#fff">
<div style="width:1040px;margin:20px"><canvas id="hw-cv" style="width:100%;display:block"></canvas></div>
<button id="hw-dl" data-title="{title}" style="display:none"></button>
<script>{js}</script></body></html>'''
d = pathlib.Path('/tmp/anim/site') / slug; d.mkdir(parents=True, exist_ok=True)
(d / 'index.html').write_text(html); print('built', d)
