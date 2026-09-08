/* Single-purpose: mobile overflow sweep of all 40 pages at 390px.
   Reports document overflow (px) and the deepest unclipped offender per page. */
const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');

const ROOT = path.resolve(__dirname, '..');
const PAGES = [
  'index.html', 'pages/features.html', 'pages/solutions.html', 'pages/pricing.html',
  'pages/customers.html', 'pages/about.html', 'pages/contact.html', 'pages/blog.html',
  'blog/article.html', 'auth/login.html', 'auth/register.html', 'auth/forgot-password.html',
  'docs/index.html', 'docs/getting-started.html', 'docs/authentication.html',
  'docs/api-reference.html', 'docs/sdks.html', 'docs/examples.html', 'docs/errors.html',
  'docs/limits.html', 'docs/faq.html', 'docs/projects.html', 'docs/webhooks.html',
  'docs/api/users.html', 'docs/api/projects.html', 'docs/api/payments.html', 'docs/api/files.html',
  'dashboard/index.html', 'dashboard/api-keys.html', 'dashboard/usage.html',
  'dashboard/analytics.html', 'dashboard/logs.html', 'dashboard/endpoints.html',
  'dashboard/sdk.html', 'dashboard/team.html', 'dashboard/billing.html',
  'dashboard/notifications.html', 'dashboard/settings.html',
  'changelog/index.html', 'status/index.html'
];

(async () => {
  const b = await chromium.launch();
  let bad = 0;
  for (const page of PAGES) {
    const ctx = await b.newContext({ viewport: { width: 390, height: 844 }, isMobile: true, hasTouch: true });
    const pg = await ctx.newPage();
    await pg.goto('http://127.0.0.1:8801/' + page, { waitUntil: 'load' });
    await pg.waitForTimeout(650);
    const res = await pg.evaluate(() => {
      const se = document.scrollingElement;
      se.scrollLeft = 0;
      const sl = se.scrollLeft;
      const ov = se.scrollWidth - se.clientWidth;
      const out = [];
      document.querySelectorAll('body *').forEach(el => {
        if (['SCRIPT', 'STYLE', 'LINK', 'NOSCRIPT'].includes(el.tagName)) return;
        const st = getComputedStyle(el);
        if (st.position === 'fixed' || st.position === 'absolute' || st.display === 'none') return;
        const r = el.getBoundingClientRect();
        if (r.width <= 0 || r.height <= 0) return;
        const lx = r.left + sl, rx = r.right + sl;
        if (lx < -2 || rx > 392) {
          let clipped = false, a = el.parentElement;
          while (a && a !== document.body) {
            const o = getComputedStyle(a).overflowX;
            if (o === 'hidden' || o === 'clip' || o === 'scroll' || o === 'auto') { clipped = true; break; }
            a = a.parentElement;
          }
          if (!clipped) out.push(el.tagName + '.' + (el.className || '').toString().split(' ').slice(0, 2).join('.') + ' lx=' + Math.round(lx) + ' w=' + Math.round(r.width));
        }
      });
      return { ov, out: out.slice(0, 4) };
    });
    if (res.ov > 2) {
      bad++;
      console.log(`✗ ${page} overflow=${res.ov}px  ${res.out.join(' ; ')}`);
    } else {
      console.log(`✓ ${page} (${res.ov}px)`);
    }
    await ctx.close();
  }
  await b.close();
  console.log(bad ? `\n${bad} pages with overflow` : '\nNO MOBILE OVERFLOW');
  process.exit(bad ? 1 : 0);
})();
