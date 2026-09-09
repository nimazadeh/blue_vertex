# -*- coding: utf-8 -*-
"""Master QA — phase 2: real horizontal scroll across all pages × widths."""
import os, json
from playwright.sync_api import sync_playwright

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = 'http://127.0.0.1:8801/'
PAGES = sorted([os.path.join(r, f).replace(ROOT + '/', '')
                for r, _, fs in os.walk(ROOT) for f in fs if f.endswith('.html')])
WIDTHS = [360, 390, 414, 768, 1024, 1280, 1440, 1680]

JS = """(() => {
  const vw = window.innerWidth;
  window.scrollTo(400, 0);
  const sw = document.documentElement.scrollWidth;
  const sx = window.scrollX;
  const off = [];
  if (sx > 0 || sw > vw + 1) {
    document.querySelectorAll('body *').forEach(el => {
      const r = el.getBoundingClientRect();
      if (r.width < 2) return;
      let a = el, abs = false;
      while (a && a !== document.body) {
        const cs = getComputedStyle(a);
        if (cs.position === 'fixed' || cs.position === 'absolute') { abs = true; break; }
        a = a.parentElement;
      }
      if (abs) return;
      if (r.right > vw + 1 || r.left < -1) {
        off.push(el.tagName + '.' + (el.className || '').toString().split(' ').slice(0, 2).join('.') +
          ' w=' + Math.round(r.width) + ' right=' + Math.round(r.right) +
          (el.textContent ? ' :: ' + el.textContent.trim().slice(0, 22) : ''));
      }
    });
  }
  window.scrollTo(0, 0);
  return {sw, sx, off: off.slice(0, 5)};
})()"""

with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={'width': 1440, 'height': 900})
    bad = []
    for page in PAGES:
        for w in WIDTHS:
            pg.set_viewport_size({'width': w, 'height': 900})
            try:
                pg.goto(BASE + page, wait_until='networkidle', timeout=20000)
            except Exception:
                bad.append((page, w, ['LOAD FAIL']))
                continue
            pg.wait_for_timeout(220)
            r = pg.evaluate(JS)
            if r['sx'] > 0 or r['sw'] > w + 1:
                bad.append((page, w, f"sw={r['sw']} scrollX={r['sx']}", r['off']))
    if bad:
        for row in bad:
            print(row[0], '@', row[1], '|', row[2])
            for o in row[3]:
                print('    ', o)
    else:
        print(f'NO H-SCROLL: {len(PAGES)} pages × {len(WIDTHS)} widths clean')
    b.close()
