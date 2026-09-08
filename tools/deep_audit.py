# -*- coding: utf-8 -*-
"""Deep static audit for admin pages: ids, icons, dead buttons, a11y, HTML structure."""
from playwright.sync_api import sync_playwright

BASE = 'http://127.0.0.1:8801/admin/'
PAGES = ['index.html', 'users.html', 'organizations.html', 'subscriptions.html', 'revenue.html',
         'api.html', 'activity.html', 'support.html', 'notifications.html', 'content.html',
         'flags.html', 'security.html', 'settings.html']

JS = """(() => {
  const out = {dupIds: [], deadBtns: [], badLinks: [], noAlt: [], noLabel: [], badIcon: [],
               knownIcons: [], tableIssues: [], dataDupes: [], kpiVsData: []};
  // duplicate ids
  const seen = {};
  document.querySelectorAll('[id]').forEach(el => {
    if (seen[el.id]) out.dupIds.push(el.id);
    seen[el.id] = 1;
  });
  // icon validity against loaded lucide
  const icons = window.lucide && window.lucide.icons ? Object.keys(window.lucide.icons) : [];
  out.knownIcons = icons.length;
  document.querySelectorAll('[data-icon]').forEach(el => {
    const n = el.getAttribute('data-icon');
    if (!n) return;
    const key = n.split('-').map(p => p.charAt(0).toUpperCase() + p.slice(1)).join('');
    if (!icons.length || !icons.includes(key)) out.badIcon.push(el.getAttribute('data-icon'));
  });
  // buttons that look handler-less (no data-* contract at all)
  document.querySelectorAll('button').forEach(b => {
    const attrs = [...b.attributes].map(a => a.name).filter(n => n.startsWith('data-'));
    const hasAria = b.getAttribute('aria-label');
    const txt = b.textContent.trim();
    if (!attrs.length && !hasAria && !txt) out.deadBtns.push(b.outerHTML.slice(0, 80));
  });
  // icon-only buttons without aria-label
  document.querySelectorAll('button').forEach(b => {
    const svg = b.querySelector('svg') || b.querySelector('[data-icon]');
    const aria = b.getAttribute('aria-label');
    const hasText = b.textContent.trim().length > 0;
    const title = b.getAttribute('title');
    if (svg && !hasText && !aria && !title) {
      out.noLabel.push((b.className||'').toString().slice(0,30) + ' :: ' + b.outerHTML.slice(0,60));
    }
  });
  // bad links
  document.querySelectorAll('a').forEach(a => {
    const h = a.getAttribute('href');
    if (h === null || h === '' || h === '#' || h === 'javascript:void(0)') {
      out.badLinks.push((a.className||'').toString().slice(0,26) + ' :: ' + a.textContent.trim().slice(0,24));
    }
  });
  // img alt
  document.querySelectorAll('img').forEach(im => {
    if (!im.hasAttribute('alt')) out.noAlt.push(im.getAttribute('src') || '');
  });
  // inputs / selects / textareas without label or aria
  document.querySelectorAll('input, select, textarea').forEach(f => {
    if (f.type === 'hidden' || f.type === 'checkbox') return;
    const id = f.id;
    if (id && document.querySelector('label[for="' + id + '"]')) return;
    if (f.getAttribute('aria-label') || f.getAttribute('placeholder') && f.tagName !== 'SELECT') return;
    if (f.closest('.search-input') || f.closest('.palette-input-wrap')) return;
    out.noLabel.push(f.tagName + '#' + (f.id||'') + ' :: ' + (f.className||'').toString().slice(0,24));
  });
  // data duplicate ids in ADMIN arrays
  const A = window.ADMIN || {};
  ['users','orgs','subs','tickets','notifications','flags','incidents'].forEach(k => {
    if (!A[k]) return;
    const s = {}; const d = [];
    A[k].forEach(r => { if (s[r.id]) d.push(k + ':' + r.id); s[r.id] = 1; });
    if (d.length) out.dataDupes.push(d.slice(0,4).join(','));
  });
  // KPI vs data counts
  if (A.users) {
    const active = A.users.filter(u => u.status === 'active').length;
    out.kpiVsData.push('users total=' + A.users.length + ' active=' + active);
  }
  if (A.subs) {
    const mrr = A.subs.filter(s => s.status === 'active' && s.pay && s.pay !== 'none').length;
    out.kpiVsData.push('subs=' + A.subs.length + ' active=' + mrr);
  }
  return out;
})()"""

with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={'width': 1440, 'height': 900})
    total = {}
    for page in PAGES:
        pg.goto(BASE + page); pg.wait_for_load_state('networkidle'); pg.wait_for_timeout(300)
        r = pg.evaluate(JS)
        flags = {k: v for k, v in r.items() if v and k not in ('knownIcons', 'kpiVsData')}
        ok = not flags
        print(f"{page:20s} {'OK ' if ok else 'ISSUES'}  icons={r['knownIcons']}   {r['kpiVsData']}")
        for k, v in flags.items():
            print(f"    {k}: {v[:6] if isinstance(v, list) else v}")
        for k, v in r.items():
            if v and k not in ('knownIcons','kpiVsData'):
                total[k] = total.get(k, 0) + len(v)
    print('TOTAL:', total)
    b.close()
