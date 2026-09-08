const { chromium } = require('playwright');
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
  const totals = { imgNoAlt: 0, btnNoName: 0, inputNoLabel: 0, orphanH: 0 };
  const byPage = {};
  for (const page of PAGES) {
    const pg = await (await b.newContext()).newPage();
    try {
      await pg.goto('http://127.0.0.1:8801/' + page, { waitUntil: 'domcontentloaded', timeout: 15000 });
    } catch (e) {
      console.log('RETRY', page);
      await pg.goto('http://127.0.0.1:8801/' + page, { waitUntil: 'domcontentloaded', timeout: 30000 });
    }
    await pg.waitForTimeout(400);
    const r = await pg.evaluate(() => {
      const out = { imgNoAlt: [], btnNoName: [], inputNoLabel: [], orphanH: [] };
      document.querySelectorAll('img').forEach(i => { if (!i.getAttribute('alt')) out.imgNoAlt.push(1); });
      document.querySelectorAll('button, a[role=button]').forEach(b => {
        const name = (b.getAttribute('aria-label') || b.textContent || '').trim();
        if (!name) out.btnNoName.push(1);
      });
      document.querySelectorAll('input, select, textarea').forEach(inp => {
        if (inp.type === 'hidden') return;
        const id = inp.id;
        const labelled = (id && document.querySelector('label[for="' + id + '"]')) || inp.closest('label') || inp.getAttribute('aria-label') || inp.getAttribute('placeholder') || inp.getAttribute('aria-labelledby');
        if (!labelled) out.inputNoLabel.push(inp.name || inp.type);
      });
      const h1 = document.querySelector('h1');
      if (h1) {
        let prev = 1;
        document.querySelectorAll('h1,h2,h3,h4,h5,h6').forEach(h => {
          const lv = +h.tagName[1];
          if (lv > prev + 1) out.orphanH.push(h.tagName);
          prev = lv;
        });
      }
      return out;
    });
    for (const k of Object.keys(totals)) {
      if (r[k].length) { totals[k] += r[k].length; byPage[page + ':' + k] = r[k].length; }
    }
    await pg.context().close();
  }
  await b.close();
  console.log('TOTALS:', JSON.stringify(totals));
  console.log(JSON.stringify(byPage, null, 1));
})();
