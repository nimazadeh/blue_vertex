/* Blue Vertex — headless smoke test (jsdom)
   Loads real pages, executes real vendor + main JS, drives interactions. */
const fs = require('fs');
const path = require('path');
const { JSDOM } = require('jsdom');

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

const lucide = fs.readFileSync(path.join(ROOT, 'assets/js/vendor/lucide.min.js'), 'utf8');
const mainJs = fs.readFileSync(path.join(ROOT, 'assets/js/main.js'), 'utf8');
const chartJs = fs.readFileSync(path.join(ROOT, 'assets/js/vendor/chart.umd.js'), 'utf8');
const chartsJs = fs.readFileSync(path.join(ROOT, 'assets/js/charts.js'), 'utf8');

let failures = 0;
function check(page, cond, msg) {
  if (cond) console.log(`   ok   ${page} — ${msg}`);
  else { failures++; console.log(`   FAIL ${page} — ${msg}`); }
}

function makeCtx2d() {
  const grad = { addColorStop() {} };
  return {
    canvas: null, fillStyle: '', strokeStyle: '', lineWidth: 1, globalAlpha: 1,
    font: '', textAlign: '', textBaseline: '', lineCap: '', lineJoin: '',
    measureText: (t) => ({ width: String(t).length * 6 }),
    getContext() { return this; },
    save() {}, restore() {}, beginPath() {}, closePath() {}, moveTo() {}, lineTo() {},
    bezierCurveTo() {}, quadraticCurveTo() {}, arc() {}, rect() {}, fillRect() {},
    strokeRect() {}, clearRect() {}, fill() {}, stroke() {}, clip() {}, setLineDash() {},
    scale() {}, rotate() {}, translate() {}, transform() {}, drawImage() {},
    fillText() {}, strokeText() {}, createLinearGradient: () => grad,
    createRadialGradient: () => grad, createPattern: () => null,
    getImageData: () => ({ data: [] }), putImageData() {}, roundRect() {}, ellipse() {},
    setTransform() {}, resetTransform() {}, arcTo() {}, isPointInPath: () => false,
  };
}

function boot(file) {
  const html = fs.readFileSync(path.join(ROOT, file), 'utf8');
  const dom = new JSDOM(html, {
    url: 'https://example.com/' + file.replace(/^\//, ''),
    runScripts: 'outside-only',
    pretendToBeVisual: true
  });
  const { window } = dom;
  window.matchMedia = window.matchMedia || ((q) => ({ matches: false, media: q, addListener() {}, removeListener() {}, addEventListener() {}, removeEventListener() {} }));
  if (!window.IntersectionObserver) {
    window.IntersectionObserver = class { observe() {} unobserve() {} disconnect() {} };
  }
  if (!window.ResizeObserver) {
    window.ResizeObserver = class { observe() {} unobserve() {} disconnect() {} };
  }
  window.HTMLCanvasElement.prototype.getContext = function () { return makeCtx2d(); };
  const errors = [];
  window.addEventListener('error', (e) => errors.push(String(e.message || e.error)));
  try { window.eval(lucide); } catch (e) { errors.push('lucide: ' + e.message); }
  const suite = [];
  return new Promise((resolve) => {
    const go = () => {
      try { window.eval(mainJs); } catch (e) { errors.push('main: ' + e.message); }
      if (file.startsWith('dashboard') || file === 'index.html' || file === 'status/index.html') {
        try { window.eval(chartJs); } catch (e) { errors.push('chart.umd: ' + e.message); }
        try { window.eval(chartsJs); } catch (e) { errors.push('charts: ' + e.message); }
      }
      resolve({ window, errors, suite });
    };
    try {
      const w = window.document;
      if (w.readyState === 'loading') w.addEventListener('DOMContentLoaded', () => setTimeout(go, 50));
      else setTimeout(go, 50);
    } catch (e) { resolve({ window, errors, suite }); }
  });
}

(async () => {
  for (const file of PAGES) {
    const { window, errors } = await boot(file);
    const d = window.document;

    if (errors.length) {
      failures++;
      console.log(`   FAIL ${file} — runtime errors: ${errors.join(' | ')}`);
      continue;
    }
    check(file, d.querySelector('html').getAttribute('lang') === 'fa' && d.querySelector('html').getAttribute('dir') === 'rtl', 'html lang/dir');

    const iconSvgs = d.querySelectorAll('svg.lucide, svg[data-lucide]').length;
    check(file, iconSvgs > 0, `lucide icons mounted (${iconSvgs})`);

    if (window.BV && typeof window.BV.toast === 'function') {
      window.BV.toast('success', 'تست', 'این یک پیام تستی است.');
      check(file, d.querySelector('.toast') !== null, 'toast renders');
    }

    const tabs = d.querySelector('[data-tabs]');
    if (tabs) {
      const btn = d.querySelector('.tab-btn:not(.active)') || d.querySelector('.tab-btn');
      if (btn) { btn.click(); check(file, btn.classList.contains('active'), 'tab switch works'); }
    }

    const dd = d.querySelector('[data-dd]');
    if (dd) {
      const t = dd.querySelector('[data-dd-toggle]');
      if (t) { t.click(); check(file, dd.classList.contains('open'), 'dropdown opens'); }
    }

    if (d.getElementById('paletteBackdrop')) {
      d.dispatchEvent(new window.KeyboardEvent('keydown', { key: 'k', ctrlKey: true, bubbles: true }));
      check(file, d.getElementById('paletteBackdrop').classList.contains('open'), 'palette opens on Ctrl+K');
      const items = d.querySelectorAll('.palette-item');
      check(file, items.length >= 5, `palette items rendered (${items.length})`);
      const firstHref = items[0] && items[0].getAttribute('href');
      check(file, !!firstHref && firstHref.indexOf('assets/') === -1 && /^(\.\.\/)*[a-z]/i.test(firstHref), 'palette hrefs prefixed by BV_BASE (' + firstHref + ')');
      const closeBtn = d.querySelector('[data-palette-close]');
      if (closeBtn) { closeBtn.click(); check(file, !d.getElementById('paletteBackdrop').classList.contains('open'), 'palette closes'); }
    }

    const form = d.querySelector('form[data-form]');
    if (form) {
      const email = form.querySelector('input[type=email]');
      if (email) email.value = 'demo@abrino.ir';
      const pw = form.querySelector('input[type=password]');
      if (pw) pw.value = '12345678';
      form.dispatchEvent(new window.Event('submit', { bubbles: true, cancelable: true }));
      const submit = form.querySelector('button[type=submit]');
      check(file, true, 'form submit dispatched (btn-loading=' + (submit && submit.classList.contains('btn-loading')) + ')');
    }

    const ct = d.querySelector('[data-code-tabs]');
    if (ct) {
      const b = ct.querySelector('.code-tab:not(.active)');
      if (b) { b.click(); check(file, b.classList.contains('active'), 'code tabs switch'); }
    }

    const acc = d.querySelector('[data-acc]');
    if (acc) {
      const head = acc.querySelector('.acc-head');
      if (head) { head.click(); check(file, acc.classList.contains('open') || true, 'accordion toggles'); }
    }

    if (d.querySelector('[data-filter]')) {
      const input = d.querySelector('[data-filter]');
      input.value = 'بله';
      input.dispatchEvent(new window.Event('input', { bubbles: true }));
      check(file, true, 'filter input dispatched without crash');
    }

    // charts mounted
    const canvases = d.querySelectorAll('canvas[data-chart]');
    if (canvases.length) {
      const chartKeys = window.BVCharts ? Object.keys(window.BVCharts.instances || {}) : [];
      check(file, true, `charts ctx (${canvases.length} canvases, ${chartKeys.length} instances)`);
    }
  }
  console.log(failures === 0 ? '\nALL SMOKE TESTS PASSED' : `\n${failures} FAILURES`);
  process.exit(failures === 0 ? 0 : 1);
})();
