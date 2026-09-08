# -*- coding: utf-8 -*-
"""Light-theme sweep: every built page × 2 widths — attr, console errors, H-scroll."""
import os, sys
from playwright.sync_api import sync_playwright

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = 'http://127.0.0.1:8801'

PAGES = sorted([os.path.join(r, f).replace(ROOT + '/', '')
                for r, _, fs in os.walk(ROOT)
                for f in fs if f.endswith('.html')])
WIDTHS = [1280, 390]

fails = []
with sync_playwright() as p:
    b = p.chromium.launch()
    for w in WIDTHS:
        ctx = b.new_context(viewport={'width': w, 'height': 900})
        pg = ctx.new_page()
        errs = []
        pg.on('pageerror', lambda e: errs.append('PAGE:' + str(e)))
        pg.on('console', lambda m: errs.append('CON:' + m.text) if m.type == 'error' else None)
        for page in PAGES:
            pg.goto(BASE + '/' + page, wait_until='networkidle')
            pg.evaluate("localStorage.setItem('bv-theme','light')")
            pg.reload(wait_until='networkidle')
            att = pg.evaluate("document.documentElement.getAttribute('data-theme')")
            if att != 'light':
                fails.append('%s w=%s attr=%s' % (page, w, att))
            hs = pg.evaluate("document.documentElement.scrollWidth - document.documentElement.clientWidth")
            if hs > 0:
                fails.append('%s w=%s HSCROLL=%s' % (page, w, hs))
            if errs:
                fails.append('%s w=%s ERR %s' % (page, w, ' '.join(errs[:2])))
                errs.clear()
        ctx.close()
    b.close()

print('LIGHT SWEEP: %d pages x %d widths' % (len(PAGES), len(WIDTHS)))
if fails:
    for f in fails[:30]:
        print('FAIL:', f)
    print('FAIL COUNT:', len(fails))
    sys.exit(1)
print('CLEAN')
