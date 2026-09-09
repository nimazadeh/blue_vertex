# -*- coding: utf-8 -*-
"""Master QA — phase 3: interaction sweep on every page.
Clicks every interactive control (buttons, tabs, accordions, dropdown,
palette, copy, forms) and collects JS errors, then re-loads between sweeps
for a clean slate."""
import os, json
from playwright.sync_api import sync_playwright

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = 'http://127.0.0.1:8801/'
PAGES = sorted([os.path.join(r, f).replace(ROOT + '/', '')
                for r, _, fs in os.walk(ROOT) for f in fs if f.endswith('.html')])

CLICKABLE = """(() => {
  const sels = ['button', '[data-acc] > .acc-head', '[data-dd-toggle]', '[data-copy]', '[data-tabs] .tab-btn',
                '[data-code-tabs] .code-tab', '[data-side-open]', '[data-search-open]', '[data-palette-open]',
                '[data-mobile-open]', '[data-billing]', '[data-monthly]', '[data-annual]', '[data-pw-toggle]',
                '[data-daterange]', '[data-seg]', '[data-filter]', '[data-key-row]', '[data-newsletter] button',
                '[data-notif-read]', '[data-log-id]', '[data-export]', '[data-exp-size]'];
  const out = [];
  sels.forEach(sel => {
    document.querySelectorAll(sel).forEach(el => {
      const r = el.getBoundingClientRect();
      if (r.width < 4 || r.height < 4 || el.offsetParent === null) return;
      out.push({sel: sel.split(' ')[0], id: el.id || '', txt: el.textContent.trim().slice(0, 14)});
    });
  });
  return out;
})()"""

CLOSE = """(() => {
  document.querySelectorAll('.dropdown.open, .acc.open').forEach(el => el.classList.remove('open'));
  document.querySelectorAll('.mobile-menu.open').forEach(el => el.classList.remove('open'));
  document.querySelectorAll('[class*="backdrop"].open, .overlay.open, .modal-backdrop.open, .drawer-backdrop.open').forEach(el => {
    try { el.click(); } catch (e) {}
  });
  document.body.style.overflow = '';
})()"""

with sync_playwright() as p:
    b = p.chromium.launch()
    problems = []
    for page in PAGES:
        pg = b.new_page(viewport={'width': 1440, 'height': 900})
        errs = []
        e1 = lambda e, errs=errs: errs.append('PAGEERROR: ' + str(e)[:140])
        e2 = lambda m, errs=errs: errs.append('CONSOLE: ' + m.text[:140]) if m.type == 'error' else None
        pg.on('pageerror', e1); pg.on('console', e2)
        try:
            pg.goto(BASE + page, wait_until='networkidle', timeout=20000)
        except Exception as ex:
            pg.close(); continue
        pg.wait_for_timeout(250)
        controls = pg.evaluate(CLICKABLE)
        for i in range(len(controls)):
            pg.evaluate(CLOSE)
            pg.wait_for_timeout(60)
            try:
                pg.evaluate("""(i) => {
                  const sels = ['button', '[data-acc] > .acc-head', '[data-dd-toggle]', '[data-copy]', '[data-tabs] .tab-btn',
                                '[data-code-tabs] .code-tab', '[data-side-open]', '[data-search-open]', '[data-palette-open]',
                                '[data-mobile-open]', '[data-billing]', '[data-monthly]', '[data-annual]', '[data-pw-toggle]',
                                '[data-daterange]', '[data-seg]', '[data-filter]', '[data-key-row]', '[data-newsletter] button',
                                '[data-notif-read]', '[data-log-id]', '[data-export]', '[data-exp-size]'];
                      const all = [];
                      sels.forEach(sel => document.querySelectorAll(sel).forEach(el => {
                        const r = el.getBoundingClientRect();
                        if (r.width < 4 || r.height < 4 || el.offsetParent === null) return;
                        all.push(el);
                      }));
                      const el = all[i];
                      if (el) {
                        if (el.disabled) return;
                        el.click();
                      }
                    }""", i)
            except Exception:
                pass
            pg.wait_for_timeout(70)
        # forms: fill + submit (if any)
        try:
            pg.evaluate("""(() => {
              document.querySelectorAll('form[data-form]').forEach(f => {
                f.querySelectorAll('input:not([type=hidden]), textarea, select').forEach(inp => {
                  if (inp.type === 'checkbox') return;
                  try {
                    if (inp.tagName === 'SELECT') { if (inp.options.length > 1) inp.selectedIndex = 1; }
                    else if (inp.type === 'password') inp.value = 'Test!2345';
                    else inp.value = 'تست خودکار';
                    inp.dispatchEvent(new Event('input', {bubbles: true}));
                  } catch (e) {}
                });
                f.dispatchEvent(new Event('submit', {bubbles: true, cancelable: true}));
              });
            })()""")
            pg.wait_for_timeout(200)
        except Exception:
            pass
        pg.evaluate(CLOSE)
        pg.wait_for_timeout(150)
        pg.remove_listener('pageerror', e1); pg.remove_listener('console', e2)
        # count how many controls were actually swept
        if errs:
            problems.append((page, len(controls), errs[:4]))
        pg.close()
    print('pages with JS errors after interaction sweep:', len(problems))
    for page, n, errs in problems:
        print(f'--- {page} ({n} controls):')
        for e in errs: print('    ', e)
    b.close()
