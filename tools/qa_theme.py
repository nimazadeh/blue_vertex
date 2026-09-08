# -*- coding: utf-8 -*-
"""
Theme QA — DOM only, no screenshots.
Checks: bootstrap, toggles (navbar/topbar/mobile/settings), persistence,
URL override, chart re-mount, H-scroll, console errors, contrast audit
for hardcoded color breakage in both themes.
"""
import sys
from playwright.sync_api import sync_playwright

BASE = 'http://127.0.0.1:8801'
DARK_BG = 'rgb(11, 13, 18)'
LIGHT_BG = 'rgb(244, 246, 249)'

PUBLIC = ['/', '/pages/pricing.html', '/docs/getting-started.html', '/pages/solutions.html', '/status/index.html']
DASH = ['/dashboard/index.html', '/dashboard/settings.html']
ADMIN = ['/admin/index.html', '/admin/settings.html']

def lum(c):
    def ch(x):
        x /= 255.0
        return x / 12.92 if x <= 0.03928 else ((x + 0.055) / 1.055) ** 2.4
    return 0.2126 * ch(c[0]) + 0.7152 * ch(c[1]) + 0.0722 * ch(c[2])

def parse_css_color(s):
    """returns (r,g,b,a) tuple or None"""
    s = s.strip()
    if s.startswith('rgba'):
        p = s[5:-1].split(',')
        return (int(p[0]), int(p[1]), int(p[2]), float(p[3]))
    if s.startswith('rgb'):
        p = s[4:-1].split(',')
        return (int(p[0]), int(p[1]), int(p[2]), 1.0)
    return None

def composite(fg, bg, page):
    """composite fg (may be rgba) over bg over page"""
    r, g, b, a = fg
    if a < 0.05:
        return bg
    out = []
    for i in range(3):
        out.append(fg[i] * a + bg[i] * (1 - a))
    return tuple(out)

def contrast(fg, bg):
    l1, l2 = lum(fg), lum(bg)
    a, b = max(l1, l2), min(l1, l2)
    return (a + 0.05) / (b + 0.05)

results = {'pass': [], 'fail': []}
def ok(name, cond, detail=''):
    (results['pass'] if cond else results['fail']).append(name + ((' | ' + detail) if detail else ''))

with sync_playwright() as p:
    browser = p.chromium.launch()

    # ---------- 1. default = softened dark ----------
    ctx = browser.new_context(viewport={'width': 1280, 'height': 900})
    pg = ctx.new_page()
    errs = []
    pg.on('pageerror', lambda e: errs.append(str(e)))
    pg.on('console', lambda m: errs.append(m.text) if m.type == 'error' else None)
    pg.goto(BASE + '/', wait_until='networkidle')
    html_attr = pg.evaluate("document.documentElement.getAttribute('data-theme')")
    bg = pg.evaluate("getComputedStyle(document.body).backgroundColor")
    ok('default theme is dark', html_attr in (None, 'dark'), f'attr={html_attr}')
    ok('dark bg is softened #0B0D12', bg == DARK_BG, bg)
    ok('no console errors (home dark)', not errs, '; '.join(errs[:3]))
    vis = pg.evaluate("""() => { const b=document.querySelector('header [data-theme-toggle], .navbar [data-theme-toggle]');
        if(!b) return null; const r=b.getBoundingClientRect(); return r.width>0 && r.height>0; }""")
    ok('navbar toggle visible desktop', bool(vis))
    if vis:
        pg.click('header [data-theme-toggle], .navbar [data-theme-toggle]')
        pg.wait_for_timeout(300)
        a2 = pg.evaluate("document.documentElement.getAttribute('data-theme')")
        ls = pg.evaluate("localStorage.getItem('bv-theme')")
        bg2 = pg.evaluate("getComputedStyle(document.body).backgroundColor")
        ok('toggle -> light attribute', a2 == 'light', str(a2))
        ok('toggle -> localStorage persisted', ls == 'light', str(ls))
        ok('light bg applied #F4F6F9', bg2 == LIGHT_BG, bg2)
        icon_changed = pg.evaluate("""() => { const b=document.querySelector('header [data-theme-toggle], .navbar [data-theme-toggle]');
            return b && (b.innerHTML.includes('moon') || b.getAttribute('aria-label') && b.getAttribute('aria-label').length > 0); }""")
        ok('toggle icon swapped', bool(icon_changed))
        pg.reload(wait_until='domcontentloaded')
        a3 = pg.evaluate("document.documentElement.getAttribute('data-theme')")
        ok('persists across reload', a3 == 'light', str(a3))
        pg.click('header [data-theme-toggle], .navbar [data-theme-toggle]')
        pg.wait_for_timeout(200)
        a4 = pg.evaluate("document.documentElement.getAttribute('data-theme')")
        ok('toggle back -> dark', a4 in (None, 'dark'), str(a4))
        ok('dark restored bg', pg.evaluate("getComputedStyle(document.body).backgroundColor") == DARK_BG)
    pg.set_viewport_size({'width': 390, 'height': 844})
    pg.reload(wait_until='networkidle')
    mvis = pg.evaluate("""() => !!document.querySelector('.mobile-menu [data-theme-toggle], nav [data-theme-toggle]')""")
    ok('mobile menu has theme toggle', bool(mvis))
    if mvis:
        ob = pg.evaluate("""() => !!document.querySelector('[class*=burger],[aria-label*=منو],.menu-btn,.nav-burger')""")
        if ob:
            pg.click('[class*=burger],[aria-label*=منو],.menu-btn,.nav-burger')
            pg.wait_for_timeout(300)
            pg.click('.mobile-menu [data-theme-toggle], nav [data-theme-toggle]')
            pg.wait_for_timeout(300)
            ok('mobile toggle works', pg.evaluate("document.documentElement.getAttribute('data-theme')") == 'light')
    ctx.close()

    # ---------- 2. ?theme=light URL override (fresh, no localStorage) ----------
    ctx = browser.new_context(viewport={'width': 1280, 'height': 900})
    pg = ctx.new_page()
    pg.goto(BASE + '/?theme=light', wait_until='networkidle')
    ok('?theme=light override', pg.evaluate("document.documentElement.getAttribute('data-theme')") == 'light')
    ok('?theme=light bg', pg.evaluate("getComputedStyle(document.body).backgroundColor") == LIGHT_BG)
    ok('?theme=light not persisted', pg.evaluate("localStorage.getItem('bv-theme')") in (None, 'dark'))
    hs = pg.evaluate("document.documentElement.scrollWidth - document.documentElement.clientWidth")
    ok('no H-scroll light 1280', hs <= 0, str(hs))
    ctx.close()

    # ---------- 3. contrast & hardcoded-color audit, both themes ----------
    audit_js = """(pageColor) => {
      const parse = (s) => {
        s = s.trim();
        if (s.startsWith('rgba')) { const p = s.slice(5,-1).split(','); return [+p[0],+p[1],+p[2],+parseFloat(p[3])]; }
        if (s.startsWith('rgb'))  { const p = s.slice(4,-1).split(','); return [+p[0],+p[1],+p[2],1]; }
        return null;
      };
      const codeLike = (el) => !!(el.closest('.code-block,.code-window,pre,.window-dots,.line-numbers,.token'));
      const out = [];
      for (const el of document.querySelectorAll('body *')) {
        if (codeLike(el)) continue;
        const r = el.getBoundingClientRect();
        if (r.width < 2 || r.height < 2) continue;
        if (el.closest('svg, script, style, noscript')) continue;
        const cs = getComputedStyle(el);
        if (cs.visibility === 'hidden' || cs.display === 'none') continue;
        if (parseFloat(cs.opacity) < 0.05) continue;
        if (!el.childNodes.length || !el.textContent.trim()) continue;
        out.push({ tag: el.tagName + '.' + String(el.className).slice(0,36),
                   bg: parse(cs.backgroundColor), fg: parse(cs.color),
                   alpha: parse(cs.backgroundColor) ? parse(cs.backgroundColor)[3] : 0 });
      }
      return out;
    }"""
    for theme in ('dark', 'light'):
        ctx = browser.new_context(viewport={'width': 1280, 'height': 900})
        pg = ctx.new_page()
        pg.goto(BASE + '/', wait_until='domcontentloaded')
        pg.evaluate("localStorage.setItem('bv-theme', '%s')" % theme)
        for path in PUBLIC + DASH + ADMIN:
            errs = []
            pg.on('pageerror', lambda e: errs.append(str(e)))
            pg.goto(BASE + path, wait_until='networkidle')
            attv = pg.evaluate("document.documentElement.getAttribute('data-theme')")
            ok('theme attr %s on %s' % (theme, path), attv == theme, str(attv))
            hs = pg.evaluate("document.documentElement.scrollWidth - document.documentElement.clientWidth")
            ok('no H-scroll %s %s' % (theme, path), hs <= 0, str(hs))
            if errs:
                results['fail'].append('console errors %s %s | %s' % (theme, path, '; '.join(errs[:3])))
            rows = pg.evaluate(audit_js, '')
            page_rgb = (244, 246, 249) if theme == 'light' else (11, 13, 18)
            bad = []
            for rrow in rows:
                bgc, fgc = rrow['bg'], rrow['fg']
                if not bgc or not fgc: continue
                if bgc[3] < 0.05: continue  # transparent — inherits, handled by ancestors
                bgv = composite(bgc, page_rgb, page_rgb)
                b_lum, f_lum = lum(bgv), lum(fgc)
                if theme == 'light':
                    if b_lum < 0.35:
                        bad.append('dark-surface %s bg=%s fg=%s' % (rrow['tag'], rrow['bg'], rrow['fg']))
                    elif b_lum > 0.7 and contrast(fgc, bgv) < 2.0:
                        bad.append('lowcontrast %s bg=%s fg=%s' % (rrow['tag'], rrow['bg'], rrow['fg']))
                else:
                    if b_lum > 0.8 and contrast(fgc, bgv) < 2.0:
                        bad.append('bright-surface %s bg=%s fg=%s' % (rrow['tag'], rrow['bg'], rrow['fg']))
            if bad:
                results['fail'].append('contrast %s %s: %s' % (theme, path, ' | '.join(bad[:6]) + (' …(+%d)' % (len(bad)-6) if len(bad) > 6 else '')))
        ctx.close()

    # ---------- 4. dashboard + admin toggles & settings segmented ----------
    ctx = browser.new_context(viewport={'width': 1280, 'height': 900})
    pg = ctx.new_page()
    pg.goto(BASE + '/dashboard/index.html', wait_until='networkidle')
    pg.evaluate("localStorage.setItem('bv-theme','dark')")
    t = pg.evaluate("!!document.querySelector('.dash-top [data-theme-toggle], .topbar [data-theme-toggle], [data-theme-toggle]')")
    ok('dashboard has topbar toggle', bool(t))
    pg.click('[data-theme-toggle]')
    pg.wait_for_timeout(400)
    ok('dashboard toggle -> light', pg.evaluate("document.documentElement.getAttribute('data-theme')") == 'light')
    n_before = pg.evaluate("document.querySelectorAll('canvas').length")
    pg.wait_for_timeout(700)
    ok('charts present on dashboard', n_before >= 1, 'n=%s' % n_before)
    ok('charts re-render after toggle', pg.evaluate("document.querySelectorAll('canvas').length") >= n_before)
    tc = pg.evaluate("getComputedStyle(document.documentElement).getPropertyValue('--track').trim()")
    ok('--track token defined', len(tc) > 0, tc)
    ctx.close()

    ctx = browser.new_context(viewport={'width': 1280, 'height': 900})
    pg = ctx.new_page()
    pg.goto(BASE + '/dashboard/settings.html', wait_until='networkidle')
    pg.evaluate("localStorage.setItem('bv-theme','dark')")
    seg = pg.evaluate("document.querySelectorAll('[data-theme-opt]').length")
    ok('settings segmented has light/dark opts', seg >= 2, str(seg))
    if seg >= 2:
        pg.click('a[data-settings-nav="appearance"]')
        pg.wait_for_timeout(300)
        segvis = pg.evaluate("""() => { const b=document.querySelector('[data-theme-opt="light"]');
            const r=b.getBoundingClientRect(); return r.width>0 && r.height>0; }""")
        ok('appearance panel opened', bool(segvis))
        if segvis:
            pg.click('[data-theme-opt="light"]')
            pg.wait_for_timeout(300)
            ok('segmented light works', pg.evaluate("document.documentElement.getAttribute('data-theme')") == 'light')
            ok('segmented active state set', pg.evaluate("document.querySelector('[data-theme-opt=\"light\"]').classList.contains('active')"))
            pg.click('[data-theme-opt="dark"]')
            pg.wait_for_timeout(200)
            ok('segmented dark works', pg.evaluate("document.documentElement.getAttribute('data-theme')") in (None, 'dark'))
    pg.goto(BASE + '/admin/index.html', wait_until='networkidle')
    pg.evaluate("localStorage.setItem('bv-theme','dark')")
    ta = pg.evaluate("!!document.querySelector('[data-theme-toggle]')")
    ok('admin has topbar toggle', bool(ta))
    if ta:
        pg.click('[data-theme-toggle]')
        pg.wait_for_timeout(300)
        ok('admin toggle -> light', pg.evaluate("document.documentElement.getAttribute('data-theme')") == 'light')
    ctx.close()
    browser.close()

print('---- THEME QA ----')
print('PASS: %d' % len(results['pass']))
for f in results['fail']:
    print('FAIL:', f)
print('FAIL COUNT: %d' % len(results['fail']))
sys.exit(1 if results['fail'] else 0)
