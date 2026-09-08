# -*- coding: utf-8 -*-
"""Alignment + responsiveness audit for admin pages (DOM measurements only)."""
from playwright.sync_api import sync_playwright

BASE = 'http://127.0.0.1:8801/admin/'
PAGES = ['index.html', 'users.html', 'organizations.html', 'subscriptions.html', 'revenue.html',
         'api.html', 'activity.html', 'support.html', 'notifications.html', 'content.html',
         'flags.html', 'security.html', 'settings.html']

SELECTORS = [
    '.side-link', '.kpi-top', '.topbar-search', '.env-chip', '.topbar-user',
    '.a-tabs button', '.ad-note', '.health-card .h-name', '.set-card h3', '.ad-sec > h3',
    '.alert-item', '.session-row', '.notif-item', '.thread .msg .m-head', '.tl-item .tl-title',
    '.chart-card-head .link', '.chart-legend span', '.kpi-delta', '.dropdown-menu .menu-item',
    '.ad-table .cell-main', '.ad-table .row-act', '.ad-table .risk', '.side-upgrade b',
    '.dg-item', '.pager', '.panel-act'
]

JS = """(() => {
  function pairLine(el, ir) {
    // the text line the icon visually pairs with:
    // 1. lines on the SAME ROW (vertical overlap) win; among them the closest one
    // 2. otherwise the vertically nearest line
    const tw = document.createTreeWalker(el, NodeFilter.SHOW_TEXT);
    let n, range = document.createRange(), sameRow = null, near = null;
    while ((n = tw.nextNode())) {
      if (!n.textContent.trim()) continue;
      range.selectNodeContents(n);
      const r = range.getBoundingClientRect();
      if (r.width < 2) continue;
      const gapX = Math.max(0, Math.max(ir.left, r.left) - Math.min(ir.right, r.right));
      const overlapY = Math.min(ir.bottom, r.bottom) - Math.max(ir.top, r.top);
      if (overlapY > 2) {
        if (!sameRow || gapX < sameRow.g) sameRow = {g: gapX, c: (r.top + r.bottom) / 2};
      } else {
        const dy = Math.min(Math.abs(ir.top - r.bottom), Math.abs(ir.bottom - r.top));
        if (!near || dy < near.d) near = {d: dy, c: (r.top + r.bottom) / 2};
      }
    }
    return sameRow ? sameRow.c : (near ? near.c : null);
  }
  const out = [];
  const sels = %s;
  sels.forEach(function (sel) {
    document.querySelectorAll(sel).forEach(function (el) {
      const svg = el.querySelector('svg');
      if (!svg) return;
      const sr = svg.getBoundingClientRect();
      if (sr.width < 2) return;
      const tc = pairLine(el, sr);
      if (tc == null) return;
      out.push({sel: sel, d: Math.round((sr.top + sr.bottom) / 2 - tc), w: Math.round(sr.width),
                h: Math.round(sr.height),
                cls: (el.className || '').toString().slice(0, 30)});
    });
  });
  return out;
})()"""

with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={'width': 1440, 'height': 900})
    all_issues = {}
    for page in PAGES:
        pg.goto(BASE + page); pg.wait_for_load_state('networkidle'); pg.wait_for_timeout(350)
        rows = pg.evaluate(JS % ('[' + ','.join('"%s"' % s for s in SELECTORS) + ']'))
        for r in rows:
            # flag: big icons (>20) or vertical delta > 3
            if abs(r['d']) > 3 or r['w'] > 20:
                key = (r['sel'], r['cls'][:22])
                all_issues.setdefault(key, []).append((page, r['d'], r['w'], r['h']))
    print('=== MISALIGNED / UNSIZED ICONS (grouped) ===')
    for (sel, cls), rows in sorted(all_issues.items()):
        pages = sorted(set(x[0] for x in rows))
        ds = [x[1] for x in rows]; ws = [x[2] for x in rows]
        print(f"{sel:38s} | {cls:24s} | pages={len(pages):2d} | dY min/max={min(ds)}/{max(ds)} | w min/max={min(ws)}/{max(ws)}")
    b.close()
