# -*- coding: utf-8 -*-
"""Master QA — phase 1: browser console/network errors on every page."""
import os, re, json
from playwright.sync_api import sync_playwright

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = 'http://127.0.0.1:8801/'
PAGES = sorted([os.path.join(r, f).replace(ROOT + '/', '')
                for r, _, fs in os.walk(ROOT) for f in fs if f.endswith('.html')])

with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={'width': 1440, 'height': 900})
    problems = []
    for page in PAGES:
        errs, fails = [], []
        e1 = lambda e, errs=errs: errs.append('PAGEERROR: ' + str(e))
        e2 = lambda m, errs=errs: errs.append('CONSOLE: ' + m.text) if m.type == 'error' else None
        e3 = lambda r, fails=fails: fails.append(r) if r.status >= 400 else None
        pg.on('pageerror', e1); pg.on('console', e2); pg.on('response', e3)
        try:
            pg.goto(BASE + page, wait_until='networkidle', timeout=20000)
        except Exception as ex:
            problems.append((page, ['LOAD FAIL: ' + str(ex)[:120], []]))
            pg.remove_listener('pageerror', e1); pg.remove_listener('console', e2); pg.remove_listener('response', e3)
            continue
        pg.wait_for_timeout(250)
        pg.remove_listener('pageerror', e1); pg.remove_listener('console', e2); pg.remove_listener('response', e3)
        if errs or fails:
            problems.append((page, [errs[:4], fails[:4]]))
    print(json.dumps(problems, ensure_ascii=False, indent=1) if problems else 'ALL PAGES CLEAN')
    b.close()
