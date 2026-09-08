/* Blue Vertex — Playwright audit: every page in a real browser. */
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
  const browser = await chromium.launch();
  const results = [];
  const fsPath = 'http://127.0.0.1:8801/';

  for (const page of PAGES) {
    const ctx = await browser.newContext({ viewport: { width: 1440, height: 900 } });
    const pg = await ctx.newPage();
    const errors = [];
    pg.on('console', (m) => { if (m.type() === 'error') errors.push('console: ' + m.text()); });
    pg.on('pageerror', (e) => errors.push('pageerror: ' + e.message));
    pg.on('requestfailed', (r) => errors.push('reqfail: ' + r.url()));
    await pg.goto(fsPath + page, { waitUntil: 'load' });
    await pg.waitForTimeout(600);

    const info = await pg.evaluate(() => {
      const out = {};
      out.overflow = document.documentElement.scrollWidth - document.documentElement.clientWidth;
      out.h1 = Array.from(document.querySelectorAll('h1')).map(h => h.textContent.trim().replace(/\s+/g, ' ').slice(0, 60));
      out.fonts = document.fonts ? Array.from(document.fonts).filter(f => f.status === 'loaded').map(f => f.family).filter((v, i, a) => a.indexOf(v) === i) : [];
      out.canvases = Array.from(document.querySelectorAll('canvas')).map(c => ({ id: c.id, w: c.width, h: c.height }));
      out.brokenImgs = Array.from(document.querySelectorAll('img')).filter(i => !i.complete || i.naturalWidth === 0).length;
      out.ariaMissing = document.querySelectorAll('a[href]:not([aria-label]):not([title])').length;
      out.hiddenHeadings = Array.from(document.querySelectorAll('h1, h2')).filter(h => h.offsetParent === null && !h.closest('[hidden]')).length;
      return out;
    });

    // screenshots of key pages
    if (['index.html', 'pages/pricing.html', 'docs/api-reference.html', 'dashboard/index.html',
         'dashboard/logs.html', 'dashboard/settings.html', 'auth/login.html', 'status/index.html',
         'changelog/index.html', 'docs/getting-started.html', 'dashboard/analytics.html',
         'pages/blog.html', 'docs/api/users.html', 'dashboard/api-keys.html'].includes(page)) {
      const shot = path.join(ROOT, 'tools', 'shots', page.replace(/\//g, '__') + '.png');
      fs.mkdirSync(path.dirname(shot), { recursive: true });
      await pg.screenshot({ path: shot, fullPage: false });
    }
    results.push({ page, errors, ...info });
    await ctx.close();
  }
  await browser.close();

  let bad = 0;
  for (const r of results) {
    const errs = r.errors.filter(e => !/favicon\.ico/.test(e) && !/net::ERR_ABORTED/.test(e));
    if (errs.length) { bad++; console.log(`✗ ${r.page}\n    ${errs.join('\n    ')}`); }
  }
  console.log(`\nconsole/page errors: ${bad} pages`);
  const over = results.filter(r => r.overflow > 2);
  console.log(`horizontal overflow > 2px: ${over.length ? over.map(o => o.page) : 'none'}`);
  const noh1 = results.filter(r => r.h1.length === 0);
  console.log(`pages missing h1: ${noh1.length ? noh1.map(n => n.page) : 'none'}`);
  const nofont = results.filter(r => !r.fonts.includes('Vazirmatn'));
  console.log(`pages missing Vazirmatn: ${nofont.length ? nofont.map(n => n.page) : 'none'}`);
  const broken = results.filter(r => r.brokenImgs > 0);
  console.log(`pages with broken imgs: ${broken.length ? broken.map(b => b.page) : 'none'}`);
  process.exit(bad ? 1 : 0);
})();
