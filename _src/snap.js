// Renders each How It Works animation to site/how-it-works/<slug>/<slug>-working-diagram.png
// Run after build.py:  node _src/snap.js && python3 _src/webp.py
const { chromium } = require('playwright');
const fs = require('fs'), path = require('path');
const SITE = path.resolve(__dirname, '..', 'site', 'how-it-works');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1100, height: 900 }, deviceScaleFactor: 2 });
  await p.route(/^https?:\/\//, r => r.abort());
  const errs = [];
  p.on('pageerror', e => errs.push(e.message));
  for (const slug of fs.readdirSync(SITE)) {
    const f = path.join(SITE, slug, 'index.html');
    if (!fs.existsSync(f)) continue;
    await p.goto('file://' + f);
    await p.evaluate(() => document.getElementById('hw-cv').scrollIntoView({ block: 'center' }));
    await p.waitForTimeout(2200);
    await p.click('#hw-pp');
    await p.waitForTimeout(100);
    const box = await (await p.$('#hw-cv')).boundingBox();
    if (box.width < 700) throw new Error(slug + ' canvas width ' + box.width);
    const url = await p.evaluate(() => window.__hwExport());
    fs.writeFileSync(path.join(SITE, slug, slug + '-working-diagram.png'), Buffer.from(url.split(',')[1], 'base64'));
    console.log('snap', slug);
  }
  await b.close();
  if (errs.length) { console.error(errs); process.exit(1); }
})();
