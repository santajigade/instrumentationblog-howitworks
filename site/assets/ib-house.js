/* Instrumentation Blog house promo: when AdSense leaves one of OUR manual ad boxes unfilled,
   show a small eBook card there instead of an empty gap. Real ads are never touched or re-requested. */
(function () {
  if (window.__ibHouse) return; window.__ibHouse = 1;
  var S = 'https://www.instrumentationblog.in/instrumentation-ebooks/', U = 'https://www.instrumentationblog.in/wp-content/uploads/2026/11/';
  var B = [
    ['field-instruments-calibration-ebook', 'Practical Guide to Field Instruments and Calibration', '$4.99', 'field-instruments-calibration-ebook-cover.webp', /calibrat|transmitter|field|loop|instrument/],
    ['plc-and-control-systems-ebook', 'PLC and Control Systems', '$5.99', 'plc-control-systems-ebook-cover.webp', /plc|ladder|scada|dcs|pid|control-system|automation|hmi|modbus|profibus|opc/],
    ['control-valve-sizing-selection-ebook', 'Control Valve Sizing and Selection', '$5.99', 'control-valve-sizing-selection-ebook-cover.webp', /valve|actuator|positioner|cv-|cavitation/],
    ['functional-safety-sis-sil-ebook', 'Functional Safety in Practice: SIS, SIL and SIF', '$6.99', 'functional-safety-ebook-cover.webp', /sil|sis|safety|sif|61511|61508|interlock|esd/],
    ['hazardous-area-instrumentation-ebook', 'Hazardous Area Instrumentation', '$5.99', 'hazardous-area-instrumentation-ebook-cover.webp', /hazard|atex|explosion|intrinsic|zone|ex-d|flameproof/],
    ['instrumentation-interview-questions-ebook', 'Instrumentation Interview Guide', '$2.99', 'instrumentation-interview-guide-cover.webp', /interview|question|viva|mcq|basics/],
    ['flow-measurement-ebook', 'Flow Measurement Guide', '$6.99', 'flow-measurement-ebook-cover.webp', /flow|orifice|venturi|coriolis|magnetic|vortex|rotameter|meter/],
    ['pressure-measurement-ebook', 'Pressure Measurement Guide', '$6.99', 'pressure-measurement-ebook-cover-v2.webp', /pressure|gauge|vacuum|manometer|diaphragm/],
    ['level-measurement-ebook', 'Level Measurement Guide', '$6.99', 'level-measurement-ebook-cover-v2.webp', /level|radar|ultrasonic|float|displacer|tank|bridle/],
    ['temperature-measurement-ebook', 'Temperature Measurement Guide', '$6.99', 'temperature-measurement-ebook-cover.webp', /temperature|rtd|pt100|thermocouple|thermowell|thermistor|pyrometer/],
    ['instrumentation-engineers-toolkit', "Instrumentation Engineer's Toolkit", '$9.99', 'instrumentation-engineers-toolkit-cover-v2.webp', /tool|template|excel|checklist|datasheet|download/]
  ];
  var path = (location.pathname + ' ' + document.title).toLowerCase();
  if (path.indexOf('/instrumentation-ebooks/') >= 0) return;           // shop pages sell books already
  var order = B.map(function (b, i) { return [b[4].test(path) ? 0 : 1, (i * 7 + path.length) % 11, b]; })
    .sort(function (a, b) { return a[0] - b[0] || a[1] - b[1]; }).map(function (x) { return x[2]; });
  var used = 0;
  var css = '.ibh-house{display:block !important}' +
    '.whc-ad.ibh-house:has(ins[data-ad-status="unfilled"]),.ibuc-ad.ibh-house:has(ins[data-ad-status="unfilled"]),.ibsx-ad.ibh-house:has(ins[data-ad-status="unfilled"]),.ibsb-ad.ibh-house:has(ins[data-ad-status="unfilled"]){display:block !important}' +
    '.ibh-house ins.adsbygoogle{display:none !important}' +
    '.ibh-card{display:flex;gap:16px;align-items:center;max-width:620px;margin:6px auto 0;padding:14px 16px;background:#f6f8fc;border:1px solid #dde3ee;border-radius:14px;text-align:left;font-family:"Segoe UI",Arial,sans-serif;text-decoration:none !important;color:#1f2733 !important;transition:box-shadow .15s,transform .15s}' +
    '.ibh-card:hover{box-shadow:0 8px 22px rgba(11,37,64,.12);transform:translateY(-2px)}' +
    '.ibh-card img{width:72px;height:auto;flex:none;border-radius:4px;box-shadow:0 6px 14px rgba(0,0,0,.25);margin:0 !important}' +
    '.ibh-txt{display:flex;flex-direction:column;gap:4px;min-width:0}.ibh-tag{font-size:12px;font-weight:700;color:#0077c0;text-transform:uppercase;letter-spacing:.05em}' +
    '.ibh-t{font-size:17px;font-weight:800;line-height:1.3;color:#0b2540}.ibh-row{display:flex;flex-wrap:wrap;align-items:center;gap:10px;margin-top:4px}' +
    '.ibh-p{font-weight:800;color:#1f9d55}.ibh-btn{display:inline-block;background:#ffed00;color:#0b2540;font-weight:800;font-size:14px;padding:7px 14px;border-radius:8px}' +
    '.ibsx .ibh-card,.ibsb .ibh-card{flex-direction:column;text-align:center}.ibsx .ibh-card img,.ibsb .ibh-card img{width:110px}.ibsx .ibh-row,.ibsb .ibh-row{justify-content:center}';
  var st = document.createElement('style'); st.id = 'ibh-css'; st.textContent = css; document.head.appendChild(st);
  function box(ins) { return ins.closest('.whc-ad,.ibuc-ad,.ibsx-ad,.ibsb-ad'); }
  function fill(ins) {
    var b = box(ins); if (!b || b.classList.contains('ibh-house')) return;
    var k = order[used++ % order.length];
    b.classList.add('ibh-house');
    var w = b.querySelectorAll('span,div');
    for (var i = 0; i < w.length; i++) { if (!w[i].children.length && /^\s*advertisement\s*$/i.test(w[i].textContent)) w[i].textContent = 'From Instrumentation Blog'; }
    var a = document.createElement('a'); a.className = 'ibh-card'; a.href = S + k[0] + '/';
    a.innerHTML = '<img src="' + U + k[3] + '" alt="' + k[1] + ' eBook cover" width="72" height="102" loading="lazy">' +
      '<span class="ibh-txt"><span class="ibh-tag">eBook</span><span class="ibh-t">' + k[1] + '</span>' +
      '<span class="ibh-row"><span class="ibh-p">' + k[2] + '</span><span class="ibh-btn">Get the eBook &#8594;</span></span></span>';
    ins.parentNode.insertBefore(a, ins.nextSibling);
  }
  function scan() { var l = document.querySelectorAll('ins.adsbygoogle[data-ad-status="unfilled"]'); for (var i = 0; i < l.length; i++) fill(l[i]); }
  new MutationObserver(function (m) { for (var i = 0; i < m.length; i++) { var t = m[i].target; if (t.tagName === 'INS' && t.getAttribute('data-ad-status') === 'unfilled') fill(t); } })
    .observe(document.documentElement, { subtree: true, attributes: true, attributeFilter: ['data-ad-status'] });
  scan(); setTimeout(scan, 4000);
})();
