// node rec.js <slug> <frames> <stepMs> -> /home/claude/anim/<slug>/fNNN.png
const { chromium } = require('playwright');
const fs = require('fs'), path = require('path');
const [slug, N = 60, stepMs = 80] = process.argv.slice(2);
const SITE = process.env.SITE || '/tmp/anim/site';
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1100, height: 900 }, deviceScaleFactor: 2 });
  await p.route(/^https?:\/\//, r => r.abort());
  await p.addInitScript(() => {
    window.__q = []; window.__t = 0;
    window.requestAnimationFrame = cb => { window.__q.push(cb); return 1; };
    window.__tick = ms => { const n = Math.ceil(ms / 40); for (let i = 0; i < n; i++) { window.__t += ms / n; const q = window.__q; window.__q = []; q.forEach(cb => cb(window.__t)); } };
    window.IntersectionObserver = function (cb) { this.observe = function () { cb([{ isIntersecting: true }]); }; };
  });
  await p.goto('file://' + path.join(SITE, slug, 'index.html'));
  await p.evaluate(() => document.getElementById('hw-cv').scrollIntoView({ block: 'center' }));
  await p.evaluate(() => window.__tick(1500));
  const out = path.join('/tmp/anim/frames', slug); fs.mkdirSync(out, { recursive: true });
  for (let i = 0; i < +N; i++) {
    await p.evaluate(ms => window.__tick(ms), +stepMs);
    const url = await p.evaluate(() => window.__hwExport());
    fs.writeFileSync(path.join(out, 'f' + String(i).padStart(3, '0') + '.png'), Buffer.from(url.split(',')[1], 'base64'));
  }
  await b.close();
  console.log('rec', slug, N);
})();
