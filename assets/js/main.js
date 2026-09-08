/* ==========================================================================
   BLUE VERTEX — main.js — interaction core
   Blue Studio © 1405 · Vanilla JS · No dependencies except lucide (vendored)
   ========================================================================== */
(function () {
  'use strict';

  var doc = document;
  /* relative prefix from this page back to the site root — derived from the
     script src so it works under any mount path (subfolder deployments too) */
  try {
    var _mainSrc = doc.querySelector('script[src*="assets/js/main.js"]');
    window.BV_BASE = _mainSrc ? _mainSrc.getAttribute('src').replace(/assets\/js\/main\.js.*$/, '') : '';
  } catch (e) { window.BV_BASE = ''; }
  var $ = function (sel, ctx) { return (ctx || doc).querySelector(sel); };
  var $$ = function (sel, ctx) { return Array.prototype.slice.call((ctx || doc).querySelectorAll(sel)); };

  /* ---------------------------------------------------------------
     1. ICONS — data-icon → lucide
  --------------------------------------------------------------- */
  function mountIcons(root) {
    var els = $$('[data-icon]', root || doc);
    /* when called with a single element (setIcon), querySelectorAll does NOT
       include the root itself — prepend it so the icon never stays empty */
    if (root && root.nodeType === 1 && root.matches && root.matches('[data-icon]')) els.unshift(root);
    els.forEach(function (el) {
      if (el.dataset.iconized) return;
      el.dataset.iconized = '1';
      var i = doc.createElement('i');
      i.setAttribute('data-lucide', el.dataset.icon);
      /* every icon gets the `.icon` class so the sizing rules across
         the design system (.link .icon, .menu-item .icon, …) apply */
      i.setAttribute('class', 'icon' + (el.dataset.iconClass ? ' ' + el.dataset.iconClass : ''));
      el.appendChild(i);
    });
    if (window.lucide) {
      try { lucide.createIcons({ icons: lucide.icons }); } catch (e) { /* console clean */ }
    }
  }

  /* ---------------------------------------------------------------
     2. PERSIAN NUMBERS — Intl fa-IR (native Jalali-style grouping)
  --------------------------------------------------------------- */
  var NF = (function () {
    try { return new Intl.NumberFormat('fa-IR'); } catch (e) { return null; }
  })();
  function faNum(n) {
    if (n === null || n === undefined || n === '') return '';
    if (NF) return NF.format(n);
    return String(n).replace(/\d/g, function (d) { return '۰۱۲۳۴۵۶۷۸۹'[d]; });
  }
  function faNumShort(n) { /* compact: ۱٫۲ میلیون */
    if (n >= 1000000) return faNum((n / 1000000).toFixed(1).replace(/\.0$/, '')) + ' میلیون';
    if (n >= 1000) return faNum((n / 1000).toFixed(1).replace(/\.0$/, '')) + ' هزار';
    return faNum(n);
  }
  function faPct(n, digits) { return faNum((n).toFixed(digits === undefined ? 2 : digits)) + '٪'; }
  function faMoney(n) { return faNum(n) + ' تومان'; }

  /* ---------------------------------------------------------------
     3. JALALI CALENDAR — port of the jalaali-js algorithm (MIT, Behrang Noruzi Niya)
  --------------------------------------------------------------- */
  function div(a, b) { return ~~(a / b); }
  function mod(a, b) { return a - ~~(a / b) * b; }
  function jalCal(jy) {
    var breaks = [-61, 9, 38, 199, 426, 686, 756, 818, 1111, 1181, 1210, 1635, 2060, 2097, 2192, 2262, 2324, 2394, 2456, 3178];
    var bl = breaks.length, gy = jy + 621, leapJ = -14, jp = breaks[0], jm, jump, leap, leapG, march, n, i;
    for (i = 1; i < bl; i += 1) {
      jm = breaks[i]; jump = jm - jp;
      if (jy < jm) break;
      leapJ = leapJ + div(jump, 33) * 8 + div(mod(jump, 33), 4);
      jp = jm;
    }
    n = jy - jp;
    leapJ = leapJ + div(n, 33) * 8 + div(mod(n, 33) + 3, 4);
    if (mod(jump, 33) === 4 && jump - n === 4) leapJ += 1;
    leapG = div(gy, 4) - div((div(gy, 100) + 1) * 3, 4) - 150;
    march = 20 + leapJ - leapG;
    if (jump - n < 6) n = n - jump + div(jump + 4, 33) * 33;
    leap = mod(mod(n + 1, 33) - 1, 4);
    if (leap === -1) leap = 4;
    return { leap: leap, gy: gy, march: march };
  }
  function j2d(jy, jm, jd) {
    var r = jalCal(jy);
    return g2d(r.gy, 3, r.march) + (jm - 1) * 31 - div(jm, 7) * (jm - 7) + jd - 1;
  }
  function d2j(jdn) {
    var gy = d2g(jdn).gy, jy = gy - 621, r = jalCal(jy), jdn1f = g2d(gy, 3, r.march), k, jm, jd;
    k = jdn - jdn1f;
    if (k >= 0) {
      if (k <= 185) { jm = 1 + div(k, 31); jd = mod(k, 31) + 1; return { jy: jy, jm: jm, jd: jd }; }
      k -= 186;
    } else {
      jy -= 1; k += 179;
      if (r.leap === 1) k += 1;
    }
    jm = 7 + div(k, 30); jd = mod(k, 30) + 1;
    return { jy: jy, jm: jm, jd: jd };
  }
  function g2d(gy, gm, gd) {
    var d = div((gy + div(gm - 8, 6) + 100100) * 1461, 4) + div(153 * mod(gm + 9, 12) + 2, 5) + gd - 34840408;
    d = d - div(div(gy + 100100 + div(gm - 8, 6), 100) * 3, 4) + 752;
    return d;
  }
  function d2g(jdn) {
    var j, i, gd, gm, gy;
    j = 4 * jdn + 139361631;
    j = j + div(div(4 * jdn + 183187720, 146097) * 3, 4) * 4 - 3908;
    i = div(mod(j, 1461), 4) * 5 + 308;
    gd = div(mod(i, 153), 5) + 1;
    gm = mod(div(i, 153), 12) + 1;
    gy = div(j, 1461) - 100100 + div(8 - gm, 6);
    return { gy: gy, gm: gm, gd: gd };
  }
  function jFromDate(d) { return d2j2(d.getFullYear(), d.getMonth() + 1, d.getDate()); }
  function d2j2(gy, gm, gd) { return d2j(g2d(gy, gm, gd)); }

  var FA_MONTHS = ['فروردین', 'اردیبهشت', 'خرداد', 'تیر', 'مرداد', 'شهریور', 'مهر', 'آبان', 'آذر', 'دی', 'بهمن', 'اسفند'];
  var FA_WDAYS = ['یکشنبه', 'دوشنبه', 'سه‌شنبه', 'چهارشنبه', 'پنجشنبه', 'جمعه', 'شنبه'];

  function faDigits(s) { /* digits only, no grouping — for years, ids */
    return String(s).replace(/\d/g, function (d) { return '۰۱۲۳۴۵۶۷۸۹'[d]; });
  }
  function faDate(d) {
    var j = jFromDate(d);
    return faNum(j.jd) + ' ' + FA_MONTHS[j.jm - 1] + ' ' + faDigits(j.jy);
  }
  function faDateFull(d) {
    var j = jFromDate(d);
    return FA_WDAYS[d.getDay()] + '، ' + faNum(j.jd) + ' ' + FA_MONTHS[j.jm - 1] + ' ' + faDigits(j.jy);
  }
  function faStamp(d) { /* for logs: ۱۴۰۵/۰۵/۲۹ — ۱۲:۰۴ */
    var j = d2j(d);
    function p(x) { return (x < 10 ? '0' : '') + x; }
    return faNum(j.jy + '/' + p(j.jm) + '/' + p(j.jd)) + ' — ' + faNum(p(d.getHours()) + ':' + p(d.getMinutes()));
  }
  function timeAgo(ms) {
    var s = Math.round((Date.now() - ms) / 1000);
    if (s < 60) return 'لحظاتی پیش';
    var m = Math.round(s / 60);
    if (m < 60) return faNum(m) + ' دقیقه پیش';
    var h = Math.round(m / 60);
    if (h < 24) return faNum(h) + ' ساعت پیش';
    var d = Math.round(h / 24);
    if (d < 7) return faNum(d) + ' روز پیش';
    return faDate(new Date(ms));
  }

  /* ---------------------------------------------------------------
     4. TOASTS
  --------------------------------------------------------------- */
  var toastRegion = null;
  function ensureToastRegion() {
    if (!toastRegion) {
      toastRegion = doc.createElement('div');
      toastRegion.className = 'toast-region';
      toastRegion.setAttribute('aria-live', 'polite');
      doc.body.appendChild(toastRegion);
    }
    return toastRegion;
  }
  var ICON_MAP = { success: 'check-circle-2', error: 'x-circle', info: 'info', warning: 'alert-triangle' };
  function toast(type, title, msg) {
    var region = ensureToastRegion();
    var el = doc.createElement('div');
    el.className = 'toast ' + (type || 'info');
    el.setAttribute('role', 'status');
    el.innerHTML =
      '<span class="toast-icon"><i data-lucide="' + (ICON_MAP[type] || ICON_MAP.info) + '"></i></span>' +
      '<div style="flex:1;min-width:0"><div class="toast-title"></div><div class="toast-msg"></div></div>' +
      '<button class="toast-close" aria-label="بستن"><i data-lucide="x"></i></button>';
    el.querySelector('.toast-title').textContent = title || '';
    el.querySelector('.toast-msg').textContent = msg || '';
    mountIcons(el);
    region.appendChild(el);
    var kill = function () {
      el.classList.add('leaving');
      setTimeout(function () { if (el.parentNode) el.parentNode.removeChild(el); }, 260);
    };
    el.querySelector('.toast-close').addEventListener('click', kill);
    setTimeout(kill, 5200);
    if (region.children.length > 4) region.removeChild(region.firstChild);
  }

  /* ---------------------------------------------------------------
     5. MODALS / DRAWERS
  --------------------------------------------------------------- */
  function openModal(id) {
    var m = doc.getElementById(id);
    if (!m) return;
    m.classList.add('open');
    doc.body.style.overflow = 'hidden';
    var f = $('[data-autofocus]', m);
    if (f) setTimeout(function () { f.focus(); }, 120);
  }
  function closeModal(id) {
    var m = doc.getElementById(id);
    if (!m) return;
    m.classList.remove('open');
    if (!$('.modal-backdrop.open')) doc.body.style.overflow = '';
  }
  /* close on «×» / «انصراف» ([data-modal-close]) and on backdrop click */
  doc.addEventListener('click', function (e) {
    var t = e.target && e.target.nodeType === 1 ? e.target : (e.target && e.target.parentElement);
    if (!t) return;
    var closer = t.closest('[data-modal-close]');
    if (closer) { closeModal(closer.getAttribute('data-modal-close')); return; }
    var openBackdrop = t.closest('.modal-backdrop.open');
    if (openBackdrop && !t.closest('.modal')) closeModal(openBackdrop.id);
  });
  function drawerBackdrop(d) {
    /* backdrop sits right before the drawer in the markup */
    var bd = d.previousElementSibling;
    return (bd && bd.classList && bd.classList.contains('drawer-backdrop')) ? bd : null;
  }
  function openDrawer(id) {
    var d = doc.getElementById(id);
    if (!d) return;
    d.classList.add('open');
    var bd = drawerBackdrop(d);
    if (bd) bd.classList.add('open');
    doc.body.style.overflow = 'hidden';
  }
  function closeDrawer(id) {
    var d = doc.getElementById(id);
    if (!d) return;
    d.classList.remove('open');
    var bd = drawerBackdrop(d);
    if (bd) bd.classList.remove('open');
    if (!$('.drawer.open')) doc.body.style.overflow = '';
  }
  function initDrawers(root) {
    /* bind every close trigger + backdrop of every drawer */
    $$('[data-drawer-close]', root || doc).forEach(function (btn) {
      btn.addEventListener('click', function () { closeDrawer(btn.getAttribute('data-drawer-close')); });
    });
    $$('.drawer-backdrop', root || doc).forEach(function (bd) {
      bd.addEventListener('click', function () {
        var d = bd.nextElementSibling;
        if (d && d.classList && d.classList.contains('drawer')) closeDrawer(d.id);
      });
    });
  }

  /* ---------------------------------------------------------------
     6. TABS / CODE TABS / ACCORDION / SEGMENTED
  --------------------------------------------------------------- */
  function initTabs(root) {
    $$('[data-tabs]', root || doc).forEach(function (wrap) {
      var scope = wrap.closest('[data-tabs-scope]') || wrap.parentNode;
      $$('.tab-btn', wrap).forEach(function (btn) {
        btn.addEventListener('click', function () {
          $$('.tab-btn', wrap).forEach(function (b) { b.classList.remove('active'); b.setAttribute('aria-selected', 'false'); });
          btn.classList.add('active');
          btn.setAttribute('aria-selected', 'true');
          var target = btn.getAttribute('data-tab');
          $$('[data-panel]', scope).forEach(function (p) {
            p.classList.toggle('active', p.getAttribute('data-panel') === target);
          });
          doc.dispatchEvent(new CustomEvent('bv:tabs', { detail: { tab: target } }));
        });
      });
    });
    $$('[data-code-tabs]', root || doc).forEach(function (wrap) {
      $$('.code-tab', wrap).forEach(function (btn) {
        btn.addEventListener('click', function () {
          $$('.code-tab', wrap).forEach(function (b) { b.classList.remove('active'); });
          btn.classList.add('active');
          var lang = btn.getAttribute('data-lang');
          $$('[data-lang-panel]', wrap).forEach(function (p) {
            p.classList.toggle('active', p.getAttribute('data-lang-panel') === lang);
          });
          $$('.code-block pre', wrap).forEach(function (pre) {
            pre.className = pre.className.replace(/\s*line-numbers/g, '');
          });
        });
      });
    });
    $$('.accordion', root || doc).forEach(function (acc) {
      var head = $('.acc-head', acc);
      if (!head) return;
      var body = $('.acc-body', acc);
      head.addEventListener('click', function () {
        var isOpen = acc.classList.contains('open');
        $$('.accordion', acc.parentNode).forEach(function (other) {
          other.classList.remove('open');
          var ob = $('.acc-body', other);
          if (ob) ob.style.maxHeight = '0px';
        });
        if (!isOpen) {
          acc.classList.add('open');
          body.style.maxHeight = body.scrollHeight + 'px';
        }
      });
      head.setAttribute('aria-expanded', 'false');
      head.setAttribute('role', 'button');
      head.setAttribute('tabindex', '0');
      var toggle = function () { head.click(); };
      head.addEventListener('keydown', function (e) { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); toggle(); } });
    });
    $$('.segmented[data-seg]', root || doc).forEach(function (seg) {
      $$('button', seg).forEach(function (b) {
        b.addEventListener('click', function () {
          $$('button', seg).forEach(function (x) { x.classList.remove('active'); });
          b.classList.add('active');
          seg.dispatchEvent(new CustomEvent('bv:seg', { bubbles: true, detail: { value: b.getAttribute('data-seg-val') } }));
        });
      });
    });
  }

  /* ---------------------------------------------------------------
     7. DROPDOWNS
  --------------------------------------------------------------- */
  function initDropdowns(root) {
    $$('[data-dd]', root || doc).forEach(function (dd) {
      dd.addEventListener('click', function (e) {
        if (e.target.closest('.dropdown-menu') && !e.target.closest('[data-dd-keep]')) {
          /* allow clicks on menu when marked keep-open */
        }
        if (!e.target.closest('.dropdown-menu') || e.target.closest('[data-dd-toggle]')) {
          var was = dd.classList.contains('open');
          closeAllDropdowns();
          if (!was) dd.classList.add('open');
        }
      });
    });
  }
  function closeAllDropdowns() {
    $$('.dropdown.open, .side-ws.open').forEach(function (d) { d.classList.remove('open'); });
  }
  /* close every open dropdown when clicking anywhere outside it */
  doc.addEventListener('click', function (e) {
    if (!e.target.closest('[data-dd], .side-ws, .dropdown-menu')) closeAllDropdowns();
  });

  /* ---------------------------------------------------------------
     8. COPY
  --------------------------------------------------------------- */
  function copyText(text, btn) {
    function done() {
      var original = btn.innerHTML;
      btn.classList.add('copied');
      /* feedback without innerHTML swap */
      var icon = btn.querySelector('i[data-lucide]') || btn.querySelector('svg');
      btn.setAttribute('aria-label', 'کپی شد');
      setTimeout(function () { btn.classList.remove('copied'); btn.setAttribute('aria-label', 'کپی'); }, 1800);
      toast('success', 'کپی شد', 'محتوای موردنظر در کلیپ‌بورد قرار گرفت.');
    }
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(text).then(done, function () { fallback(); });
    } else { fallback(); }
    function fallback() {
      var ta = doc.createElement('textarea');
      ta.value = text;
      ta.style.cssText = 'position:fixed;opacity:0';
      doc.body.appendChild(ta);
      ta.select();
      try { doc.execCommand('copy'); done(); } catch (e) { /* noop */ }
      doc.body.removeChild(ta);
    }
  }
  function initCopy(root) {
    $$('[data-copy], .code-copy', root || doc).forEach(function (btn) {
      if (btn.dataset.copyInit) return;
      btn.dataset.copyInit = '1';
      btn.addEventListener('click', function (e) {
        e.preventDefault();
        var text = null;
        if (btn.hasAttribute('data-copy-target')) {
          var t = $(btn.getAttribute('data-copy-target'));
          if (t) text = t.textContent;
        } else if (btn.hasAttribute('data-copy')) {
          text = btn.getAttribute('data-copy');
        } else {
          var block = btn.closest('.code-block');
          if (block) {
            var pre = $('pre', block);
            if (pre) text = pre.textContent;
          }
        }
        if (text !== null) copyText(text.trim(), btn);
      });
    });
  }

  /* ---------------------------------------------------------------
     9. COMMAND PALETTE (Ctrl/Cmd + K)
  --------------------------------------------------------------- */
  var PALETTE = [
    { group: 'ناوبری' },
    { label: 'جستجو در مستندات', sub: 'مستندات Blue Vertex', icon: 'book-open', href: 'docs/index.html', kbd: '⌘K' },
    { label: 'رفتن به داشبورد', sub: 'کنترل پنل توسعه‌دهنده', icon: 'layout-dashboard', href: 'dashboard/index.html' },
    { label: 'کلیدهای API', sub: 'مدیریت و ساخت کلید', icon: 'key-round', href: 'dashboard/api-keys.html' },
    { label: 'گزارش درخواست‌ها', sub: 'لاگ‌های زنده', icon: 'scroll-text', href: 'dashboard/logs.html' },
    { label: 'مرجع API', sub: '/v1 endpoints', icon: 'braces', href: 'docs/api-reference.html' },
    { label: 'تغییرات محصول', sub: 'changelog', icon: 'history', href: 'changelog/index.html' },
    { label: 'وضعیت سرویس', sub: 'uptime ۹۹٫۹۸٪', icon: 'activity', href: 'status/index.html' },
    { label: 'قیمت‌گذاری', sub: 'پلن‌ها و تعرفه‌ها', icon: 'credit-card', href: 'pages/pricing.html' }
  ];
  var paletteOpen = false, paletteActive = 0;
  var paletteBackdrop, paletteInput, paletteList, paletteItems = [];

  function iconSvg(name) {
    /* Build an inline SVG string from the lucide icon node tree.
       lucide.icons keyed by PascalCase: ["svg", {attrs}, [[tag,{attrs}],...]] */
    if (!window.lucide || !lucide.icons || !name) return '';
    var key = name.split('-').map(function (p) { return p.charAt(0).toUpperCase() + p.slice(1); }).join('');
    var icon = lucide.icons[key];
    if (!icon) return '';
    function attrsToString(a) {
      var s = '';
      for (var k in a) {
        if (k === 'class') s += ' class="' + a[k] + '"';
        else s += ' ' + k + '="' + a[k] + '"';
      }
      return s;
    }
    function nodes(list) {
      return list.map(function (n) { return '<' + n[0] + attrsToString(n[1]) + '/>'; }).join('');
    }
    return '<svg xmlns="http://www.w3.org/2000/svg"' + attrsToString(icon[1]) + '>' + nodes(icon[2]) + '</svg>';
  }
  function renderPalette(filter) {
    if (!paletteList) return;
    var q = (filter || '').trim().toLowerCase();
    var html = '', count = 0;
    PALETTE.forEach(function (item) {
      if (item.group) {
        html += '<div class="palette-group-title">' + item.group + '</div>';
        count = 0;
        return;
      }
      if (q && item.label.toLowerCase().indexOf(q) === -1 && item.sub.toLowerCase().indexOf(q) === -1) return;
      html += '<a href="' + (window.BV_BASE || '') + item.href + '" class="palette-item" data-pi="' + count + '">' +
        '<span class="p-icon">' + iconSvg(item.icon) + '</span>' +
        '<span style="flex:1;min-width:0"><b style="display:block;color:inherit">' + item.label + '</b><div class="p-sub">' + item.sub + '</div></span>' +
        (item.kbd ? '<span class="kbd">' + item.kbd + '</span>' : '') +
        '<span class="p-arrow">' + iconSvg('corner-down-left') + '</span></a>';
      count += 1;
    });
    if (count === 0) {
      html = '<div class="palette-empty">' + iconSvg('search-x') + '<div style="margin-top:10px">نتیجه‌ای برای «' + filter + '» پیدا نشد.</div></div>';
    }
    paletteList.innerHTML = html;
    paletteItems = $$('.palette-item', paletteList);
    paletteActive = 0;
    setPaletteActive(0);
  }
  function setPaletteActive(i) {
    paletteItems.forEach(function (el, idx) { el.classList.toggle('active', idx === i); });
    if (paletteItems[i] && paletteItems[i].scrollIntoView) {
      try { paletteItems[i].scrollIntoView({ block: 'nearest' }); } catch (e) {}
    }
  }
  function openPalette() {
    paletteOpen = true;
    paletteActive = 0;
    if (!paletteBackdrop) {
      paletteBackdrop = doc.getElementById('paletteBackdrop');
      paletteInput = doc.getElementById('paletteInput');
      paletteList = doc.getElementById('paletteList');
      var close = $('[data-palette-close]', paletteBackdrop);
      if (close) close.addEventListener('click', closePalette);
      if (paletteBackdrop) paletteBackdrop.addEventListener('click', function (e) { if (e.target === paletteBackdrop) closePalette(); });
      if (paletteInput) {
        paletteInput.addEventListener('input', function () { renderPalette(paletteInput.value); });
        paletteInput.addEventListener('keydown', function (e) {
          if (e.key === 'ArrowDown') { e.preventDefault(); paletteActive = Math.min(paletteActive + 1, paletteItems.length - 1); setPaletteActive(paletteActive); }
          else if (e.key === 'ArrowUp') { e.preventDefault(); paletteActive = Math.max(paletteActive - 1, 0); setPaletteActive(paletteActive); }
          else if (e.key === 'Enter') { if (paletteItems[paletteActive]) window.location.href = paletteItems[paletteActive].getAttribute('href'); }
        });
      }
    }
    var p = doc.getElementById('palette');
    if (p && p.style) { p.style.display = ''; }
    paletteBackdrop.classList.add('open');
    renderPalette('');
    doc.body.style.overflow = 'hidden';
    setTimeout(function () { if (paletteInput) paletteInput.focus(); }, 60);
  }
  function closePalette() {
    if (!paletteBackdrop) return;
    paletteBackdrop.classList.remove('open');
    doc.body.style.overflow = '';
    paletteOpen = false;
  }

  /* ---------------------------------------------------------------
     10. DOCS SEARCH
  --------------------------------------------------------------- */
  var searchOpen = false;
  var searchCat = 'all';
  function searchResetChips(cat) {
    $$('#searchFilters .chip').forEach(function (c) { c.classList.toggle('active', c.getAttribute('data-search-cat') === cat); });
  }
  function openSearch() {
    searchOpen = true;
    var v = doc.getElementById('docsSearch');
    if (!v) return;
    v.classList.add('open');
    doc.body.style.overflow = 'hidden';
    searchCat = 'all';
    searchResetChips('all');
    var inp = doc.getElementById('searchInput');
    if (inp) { inp.value = ''; setTimeout(function () { inp.focus(); }, 60); }
    if (typeof renderSearch === 'function' && window.BV_DOCS) renderSearch('', 'all');
  }
  function closeSearch() {
    var v = doc.getElementById('docsSearch');
    if (v) v.classList.remove('open');
    searchOpen = false;
    doc.body.style.overflow = '';
  }
  function renderSearch(q, cat) {
    var list = doc.getElementById('searchResults');
    var empty = doc.getElementById('searchEmpty');
    if (!list) return;
    var data = window.BV_DOCS || [];
    q = (q || '').trim().toLowerCase();
    var recents = [];
    try { recents = JSON.parse(localStorage.getItem('bv-recents') || '[]'); } catch (e) {}
    var recBox = doc.getElementById('searchRecents');
    if (recBox) {
      recBox.innerHTML = '';
      if (!q && recents.length) {
        var t = doc.createElement('span');
        t.className = 'palette-group-title';
        t.style.cssText = 'width:100%;padding:2px 0 4px;font-size:.66rem;color:var(--text-4);font-weight:700';
        t.textContent = 'جستجوهای اخیر';
        recBox.appendChild(t);
        recents.forEach(function (r) {
          var chip = doc.createElement('button');
          chip.className = 'chip';
          chip.textContent = r;
          chip.addEventListener('click', function () {
            var inp = doc.getElementById('searchInput');
            if (inp) { inp.value = r; inp.dispatchEvent(new Event('input')); }
          });
          recBox.appendChild(chip);
        });
      }
    }
    var results = data.filter(function (d) {
      if (cat && cat !== 'all' && d.cat !== cat) return false;
      if (!q) return true;
      return (d.title + ' ' + d.desc).toLowerCase().indexOf(q) !== -1;
    });
    list.innerHTML = '';
    if (!results.length) {
      if (empty) {
        empty.style.display = '';
        empty.style.textAlign = 'center';
      }
      return;
    }
    if (empty) empty.style.display = 'none';
    results.forEach(function (r) {
      var row = doc.createElement('div');
      row.className = 'search-row';
      row.setAttribute('role', 'link');
      row.setAttribute('tabindex', '0');
      row.innerHTML = '<span class="s-icon"><i data-lucide="' + r.icon + '"></i></span>' +
        '<span style="flex:1;min-width:0"><b>' + (q ? r.title.replace(new RegExp('(' + q.replace(/[.*+?^${}()|[\]\\]/g, '\\$&') + ')', 'gi'), '<mark>$1</mark>') : r.title) + '</b>' +
        '<span>' + r.desc + '</span></span><span class="cat">' + r.catLabel + '</span>';
      row.addEventListener('click', function () { saveRecent(r.title); window.location.href = r.url; });
      row.addEventListener('keydown', function (e) { if (e.key === 'Enter') row.click(); });
      list.appendChild(row);
    });
    mountIcons(list);
  }
  function saveRecent(term) {
    try {
      var recents = JSON.parse(localStorage.getItem('bv-recents') || '[]');
      recents = recents.filter(function (r) { return r !== term; });
      recents.unshift(term);
      localStorage.setItem('bv-recents', JSON.stringify(recents.slice(0, 5)));
    } catch (e) {}
  }

  /* ---------------------------------------------------------------
     11. FORMS — validation, loading, success/error states
  --------------------------------------------------------------- */
  function setFieldError(field, msg) {
    var wrap = field.closest('.field');
    if (!wrap) return;
    wrap.classList.add('has-error');
    var errEl = $('.field-error', wrap);
    if (errEl && msg) errEl.innerHTML = iconSvg('alert-circle') + '<span>' + msg + '</span>';
  }
  function clearFieldErrors(form) {
    $$('.field.has-error', form).forEach(function (f) { f.classList.remove('has-error'); });
    $$('.field-error', form).forEach(function (e) { e.textContent = ''; });
  }
  function validateField(field) {
    var val = (field.value || '').trim();
    var msg = '';
    if (field.hasAttribute('required') && !val) msg = 'پر کردن این فیلد الزامی است.';
    else if (field.type === 'email' && val && !/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(val)) msg = 'قالب ایمیل معتبر نیست.';
    else if (field.type === 'tel' && val && !/^0?9\d{9}$|^\+98\d{10}$/.test(val.replace(/[\s-]/g, ''))) msg = 'شماره موبایل معتبر نیست.';
    else if (field.hasAttribute('minlength') && val && val.length < +field.getAttribute('minlength')) msg = 'حداقل طول این فیلد ' + faNum(field.getAttribute('minlength')) + ' کاراکتر است.';
    else if (field.name === 'password2' && val && field.form) {
      var orig = field.form.querySelector('input[name="password"]');
      if (orig && val !== orig.value) msg = 'تکرار رمز عبور یکسان نیست.';
    }
    if (msg) setFieldError(field, msg);
    return !msg;
  }
  function initForms(root) {
    $$('form[data-form]', root || doc).forEach(function (form) {
      if (form.dataset.formInit) return;
      form.dataset.formInit = '1';
      var submit = $('button[type="submit"]', form);
      form.addEventListener('submit', function (e) {
        e.preventDefault();
        clearFieldErrors(form);
        $$('input[type="checkbox"][required]', form).forEach(function (cb) {
          if (!cb.checked) toast('error', 'قبول شرایط الزامی است', 'برای ادامه، ابتدا شرایط را بپذیرید.');
        });
        $$('[required], input[type="email"], input[type="tel"], [minlength]', form).forEach(function (f) {
          var skipped = f.closest('.field-hidden');
          if (!skipped && f.type !== 'checkbox') validateField(f);
        });
        if ($('.field.has-error', form)) {
          var first = $('.field.has-error input, .field.has-error select, .field.has-error textarea', form);
          if (first) first.focus();
          return;
        }
        /* loading */
        if (submit) {
          submit.classList.add('btn-loading');
          submit.setAttribute('aria-busy', 'true');
        }
        setTimeout(function () {
          if (submit) { submit.classList.remove('btn-loading'); submit.removeAttribute('aria-busy'); }
          var okBox = form.parentNode.querySelector('[data-form-success]');
          if (form.hasAttribute('data-success-hide')) form.style.display = 'none';
          if (okBox) {
            okBox.style.display = 'flex';
            okBox.classList.add('show');
            okBox.scrollIntoView({ behavior: 'smooth', block: 'center' });
          }
          var g = form.getAttribute('data-success-toast');
          if (g === 'none') { /* no toast */ } else {
            toast('success', form.getAttribute('data-success-title') || 'با موفقیت انجام شد', form.getAttribute('data-success-msg') || '');
          }
          var redir = form.getAttribute('data-redirect');
          if (redir) setTimeout(function () { window.location.href = redir; }, 900);
          form.dispatchEvent(new CustomEvent('bv:form-success'));
        }, 1100);
      });
      $$('[required], input[type="email"], input[type="tel"]', form).forEach(function (f) {
        f.addEventListener('blur', function () { if (f.value) validateField(f); });
        f.addEventListener('input', function () { var w = f.closest('.field'); if (w) w.classList.remove('has-error'); });
      });
    });
  }

  /* ---------------------------------------------------------------
     12. PASSWORD TOGGLE
  --------------------------------------------------------------- */
  function initPasswordToggles(root) {
    $$('[data-pw-toggle]', root || doc).forEach(function (btn) {
      btn.addEventListener('click', function () {
        var id = btn.getAttribute('data-pw-toggle');
        var input = doc.getElementById(id);
        if (!input) return;
        var showing = input.type === 'text';
        input.type = showing ? 'password' : 'text';
        btn.setAttribute('aria-label', showing ? 'نمایش رمز' : 'پنهان کردن رمز');
        btn.innerHTML = iconSvg(showing ? 'eye' : 'eye-off');
      });
    });
  }

  /* ---------------------------------------------------------------
     13. MOBILE MENUS + SIDEBAR + NAVBAR SCROLL + REVEAL
  --------------------------------------------------------------- */
  function initChrome() {
    $$('[data-mobile-open]').forEach(function (b) {
      b.addEventListener('click', function () {
        var m = doc.getElementById(b.getAttribute('data-mobile-open'));
        if (m) m.classList.add('open');
        doc.body.style.overflow = 'hidden';
      });
    });
    $$('[data-mobile-close]').forEach(function (b) {
      b.addEventListener('click', function () {
        var m = b.closest('.mobile-menu');
        if (m) m.classList.remove('open');
        doc.body.style.overflow = '';
      });
    });
    $$('.mobile-menu').forEach(function (m) {
      m.addEventListener('click', function (e) { if (e.target === m) { m.classList.remove('open'); doc.body.style.overflow = ''; } });
    });
    /* dashboard sidebar mobile */
    var dashSide = doc.getElementById('dashSide');
    var sideBackdrop = doc.getElementById('sideBackdrop');
    $$('[data-side-open]').forEach(function (b) {
      b.addEventListener('click', function () {
        if (dashSide) dashSide.classList.add('open');
        if (sideBackdrop) sideBackdrop.classList.add('show');
      });
    });
    if (sideBackdrop) sideBackdrop.addEventListener('click', function () {
      if (dashSide) dashSide.classList.remove('open');
      sideBackdrop.classList.remove('show');
    });
    /* navbar scroll */
    var nav = $('.navbar');
    if (nav) {
      var onScroll = function () { nav.classList.toggle('scrolled', window.scrollY > 8); };
      window.addEventListener('scroll', onScroll, { passive: true });
      onScroll();
    }
    /* reveal */
    if ('IntersectionObserver' in window) {
      var io = new IntersectionObserver(function (entries) {
        entries.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add('revealed'); io.unobserve(en.target); } });
      }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
      $$('[data-reveal]').forEach(function (el) { io.observe(el); });
    } else {
      $$('[data-reveal]').forEach(function (el) { el.classList.add('revealed'); });
    }
    /* palette triggers */
    $$('[data-palette-open]').forEach(function (b) { b.addEventListener('click', openPalette); });
    $$('[data-search-open]').forEach(function (b) { b.addEventListener('click', openSearch); });
    /* docs search: live filter, category chips, backdrop close */
    var sInp = doc.getElementById('searchInput');
    if (sInp) sInp.addEventListener('input', function () { renderSearch(sInp.value, searchCat); });
    $$('#searchFilters .chip').forEach(function (c) {
      c.addEventListener('click', function () {
        searchCat = c.getAttribute('data-search-cat') || 'all';
        $$('#searchFilters .chip').forEach(function (x) { x.classList.toggle('active', x === c); });
        var inp = doc.getElementById('searchInput');
        renderSearch(inp ? inp.value : '', searchCat);
      });
    });
    var sView = doc.getElementById('docsSearch');
    if (sView) sView.addEventListener('click', function (e) { if (e.target === sView) closeSearch(); });
    /* global keys */
    doc.addEventListener('keydown', function (e) {
      if ((e.ctrlKey || e.metaKey) && (e.key === 'k' || e.key === 'K')) { e.preventDefault(); paletteOpen ? closePalette() : openPalette(); }
      if (e.key === 'Escape') { closePalette(); closeSearch(); closeAllDropdowns(); $$('.modal-backdrop.open').forEach(function (m) { closeModal(m.id); }); $$('.drawer.open').forEach(function (d) { closeDrawer(d.id); }); }
      if ((e.ctrlKey || e.metaKey) && e.key === '/' && !searchOpen) { e.preventDefault(); openSearch(); }
    });
  }

  /* ---------------------------------------------------------------
     14. DATE RANGE (dashboard) — dispatches bv:range
  --------------------------------------------------------------- */
  function initDateRange() {
    var btn = $('[data-daterange]');
    if (!btn) return;
    var dd = btn.closest('[data-dd]');
    var menu = dd ? $('.dropdown-menu', dd) : null;
    $$('[data-range]', menu || doc).forEach(function (item) {
      item.addEventListener('click', function () {
        var r = item.getAttribute('data-range');
        $$('[data-range]', menu || doc).forEach(function (x) { x.classList.remove('active'); });
        item.classList.add('active');
        var label = item.getAttribute('data-range-label') || item.textContent.trim();
        var lab = doc.getElementById('rangeLabel');
        if (lab) lab.textContent = label;
        doc.dispatchEvent(new CustomEvent('bv:range', { detail: { range: r, label: label } }));
        closeAllDropdowns();
      });
    });
  }

  /* ---------------------------------------------------------------
     15. TABLE FILTERS (logs / endpoints / keys)
  --------------------------------------------------------------- */
  function initFilters() {
    $$('[data-table-scope]').forEach(function (scope) {
      var rows = $$('tbody tr[data-row]', scope);
      var state = { text: '', status: '', method: '', env: '' };
      function apply() {
        var shown = 0;
        rows.forEach(function (tr) {
          var ok = true;
          if (state.text) {
            var hay = (tr.getAttribute('data-search') || '').toLowerCase();
            if (hay.indexOf(state.text.toLowerCase()) === -1) ok = false;
          }
          if (ok && state.status && tr.getAttribute('data-status') !== state.status) ok = false;
          if (ok && state.method && tr.getAttribute('data-method') !== state.method) ok = false;
          if (ok && state.env && tr.getAttribute('data-env') !== state.env) ok = false;
          tr.style.display = ok ? '' : 'none';
          if (ok) shown += 1;
        });
        var count = $('[data-filter-count]', scope);
        if (count) count.textContent = 'نمایش ' + faNum(shown) + ' مورد از ' + faNum(rows.length);
        var empty = $('[data-filter-empty]', scope.parentNode || doc);
        if (empty) empty.style.display = shown ? 'none' : 'flex';
      }
      $$('[data-filter]', scope.parentNode || doc).forEach(function (input) {
        if (input.hasAttribute('data-filter-for') && input.getAttribute('data-filter-for') !== scope.id) return;
        var key = input.getAttribute('data-filter');
        if (key === 'text') input.addEventListener('input', function () { state.text = input.value; apply(); });
        else input.addEventListener('change', function () { state[key] = input.value; apply(); });
      });
      /* reset via Enter */
    });
  }

  /* ---------------------------------------------------------------
     16. API EXPLORER (simulation)
  --------------------------------------------------------------- */
  function initExplorer() {
    var form = doc.getElementById('expForm');
    if (!form) return;
    var epSelect = doc.getElementById('expEndpoint');
    var btn = doc.getElementById('expSend');
    var out = doc.getElementById('expResponse');
    var bodyBox = doc.getElementById('expBody');
    function buildBody(ep) {
      var m = { 'GET /v1/users': null, 'POST /v1/users': { name: 'سارا احمدی', email: 'sara@abrino.ir', role: 'developer' }, 'GET /v1/projects': null, 'POST /v1/payments': { amount: 2500000, currency: 'IRT', callback: 'https://shop.ir/cb' }, 'POST /v1/files': { name: 'report.pdf', size: 1048576 } };
      return m[ep] !== undefined ? JSON.stringify(m[ep], null, 2) : null;
    }
    epSelect.addEventListener('change', function () {
      var body = buildBody(epSelect.value);
      bodyBox.value = body || '';
    });
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      btn.classList.add('btn-loading');
      btn.setAttribute('aria-busy', 'true');
      out.classList.remove('show');
      setTimeout(function () {
        btn.classList.remove('btn-loading');
        btn.removeAttribute('aria-busy');
        var ep = epSelect.value;
        var authOn = doc.getElementById('expAuth') && doc.getElementById('expAuth').checked !== false;
        var ok = authOn || ep.indexOf('GET') === 0;
        var status = ok ? 200 : 401;
        var ms = 96 + Math.floor(Math.random() * 305);
        var respBody = ok
          ? (ep.indexOf('GET /v1/users') === 0 ? JSON.stringify({ data: [{ id: 'usr_01', name: 'سارا احمدی', email: 'sara@abrino.ir' }, { id: 'usr_02', name: 'علی رضایی', email: 'ali@dadehparvar.ir' }], meta: { total: 2, page: 1, per_page: 20 } }, null, 2)
            : ep.indexOf('files') !== -1 ? JSON.stringify({ data: { id: 'file_9f2', status: 'completed', url: 'https://cdn.bluevertex.ir/f/9f2' } }, null, 2)
            : JSON.stringify({ data: { id: 'req_' + Math.random().toString(36).slice(2, 9), status: 'created' }, meta: { request_id: 'req_' + Math.random().toString(36).slice(2, 11) } }, null, 2))
          : JSON.stringify({ error: { code: 'unauthorized', message: 'کلید API نامعتبر است.', doc: 'https://docs/errors#unauthorized' } }, null, 2);
        var st = out.querySelector('[data-exp-stat]');
        st.className = 'exp-stat ' + (ok ? 'ok' : 'err');
        st.innerHTML = '<span class="dot"></span> HTTP ' + status + (ok ? ' — موفق' : ' — خطا');
        out.querySelector('[data-exp-time]').textContent = faNum(ms) + ' میلیثانیه';
        out.querySelector('[data-exp-size]').textContent = faNum(respBody.length) + ' بایت';
        var rid = out.querySelector('[data-exp-rid]');
        if (rid) rid.textContent = Math.random().toString(36).slice(2, 10);
        var resEl = doc.getElementById('expBodyResult');
        if (resEl) {
          resEl.textContent = respBody;
          if (window.Prism) { try { window.Prism.highlightElement(resEl); } catch (e) {} }
        }
        out.classList.add('show');
        toast(ok ? 'success' : 'error', ok ? 'درخواست شبیهسازی شد' : 'خطای احراز هویت', ok ? 'پاسخ نمونه با موفقیت دریافت شد.' : 'برای دریافت پاسخ، گزینه «ارسال کلید API» را فعال کنید.');
      }, 1300);
    });
  }

  /* ---------------------------------------------------------------
     17. API KEYS PAGE logic
  --------------------------------------------------------------- */
  function initApiKeys() {
    var createBtn = doc.getElementById('createKeyBtn');
    var scope = doc.getElementById('keysTable');
    var revokeTarget = null;
    var renameTarget = null;
    if (createBtn) createBtn.addEventListener('click', function () {
      var s1 = $('#createKeyStep1'), s2 = $('#createKeyStep2'), f1 = $('#mkFoot1'), f2 = $('#mkFoot2');
      if (s1) s1.style.display = '';
      if (s2) s2.style.display = 'none';
      if (f1) f1.style.display = '';
      if (f2) f2.style.display = 'none';
      $('#createKeyModal') && openModal('createKeyModal');
    });
    /* per-row wiring — reused for rows inserted by the create demo */
    function wireKeyRow(row) {
      var key = row.getAttribute('data-key-full');
      $$('.key-reveal-btn', row).forEach(function (b) {
        b.addEventListener('click', function () {
          var code = $('code', row);
          if (!code) return;
          if (code.getAttribute('data-masked') === '1') {
            code.textContent = key; code.removeAttribute('data-masked');
            b.innerHTML = iconSvg('eye-off');
            toast('info', 'کلید نمایش داده شد', 'مطمئن شوید کسی به صفحه نگاه نمیکند.');
          } else {
            code.textContent = 'bv_live_' + '•'.repeat(28);
            code.setAttribute('data-masked', '1');
            b.innerHTML = iconSvg('eye');
          }
        });
      });
      $$('[data-copy]', row).forEach(function (b) {
        if (b.hasAttribute('data-copy')) return;
        b.setAttribute('data-copy', key);
      });
    }
    function wireRevoke(b) {
      b.addEventListener('click', function () {
        var row = b.closest('[data-key-row]');
        var name = row ? row.getAttribute('data-key-name') : '';
        var t = doc.getElementById('revokeKeyName');
        if (t) t.textContent = name;
        revokeTarget = row || null;
        openModal('revokeKeyModal');
      });
    }
    function wireRename(b) {
      b.addEventListener('click', function () {
        var row = b.closest('[data-key-row]');
        renameTarget = row || null;
        var inp = doc.getElementById('renameKeyInput');
        if (inp && row) inp.value = row.getAttribute('data-key-name');
        openModal('renameKeyModal');
      });
    }
    $$('[data-key-row]').forEach(wireKeyRow);
    $$('[data-revoke-key]').forEach(wireRevoke);
    $$('[data-rename-key]').forEach(wireRename);
    var confirmRevoke = doc.getElementById('confirmRevoke');
    if (confirmRevoke) confirmRevoke.addEventListener('click', function () {
      confirmRevoke.classList.add('btn-loading');
      setTimeout(function () {
        confirmRevoke.classList.remove('btn-loading');
        if (revokeTarget) {
          revokeTarget.style.transition = 'opacity .3s';
          revokeTarget.style.opacity = '0';
          setTimeout(function () { revokeTarget.style.display = 'none'; }, 300);
        }
        closeModal('revokeKeyModal');
        toast('success', 'کلید API باطل شد', 'کلید «' + (revokeTarget ? revokeTarget.getAttribute('data-key-name') : '') + '» دیگر در دسترس نیست.');
        var count = $('[data-key-count]');
        if (count) count.textContent = faNum(Math.max(0, parseInt(count.textContent.replace(/[۰-۹]/g, function (d) { return '۰۱۲۳۴۵۶۷۸۹'.indexOf(d); }), 10) - 1));
      }, 900);
    });
    /* rename */
    var saveRename = doc.getElementById('saveRename');
    if (saveRename) saveRename.addEventListener('click', function () {
      var inp = doc.getElementById('renameKeyInput');
      var v = (inp.value || '').trim();
      if (!v) { setFieldError(inp, 'نام کلید نمیتواند خالی باشد.'); return; }
      saveRename.classList.add('btn-loading');
      setTimeout(function () {
        saveRename.classList.remove('btn-loading');
        if (renameTarget) {
          var nm = renameTarget.querySelector('.key-name');
          var span = doc.createElement('span');
          span.textContent = v;
          if (nm.childNodes.length) nm.insertBefore(span, nm.childNodes[0]);
        }
        closeModal('renameKeyModal');
        toast('success', 'نام کلید تغییر کرد', 'کلید اکنون «' + v + '» نامیده میشود.');
      }, 800);
    });
    /* create key flow */
    var mkForm = doc.getElementById('createKeyForm');
    var pendingKey = null;
    if (mkForm) {
      mkForm.addEventListener('submit', function (e) {
        e.preventDefault();
        var nameInput = doc.getElementById('keyName');
        if (!nameInput.value.trim()) { setFieldError(nameInput, 'نام کلید الزامی است.'); return; }
        var btn = $('button[type="submit"]', mkForm) || $('button[type="submit"][form="createKeyForm"]');
        if (btn) btn.classList.add('btn-loading');
        setTimeout(function () {
          if (btn) btn.classList.remove('btn-loading');
          var gen = 'bv_live_' + Math.random().toString(36).slice(2, 10) + Math.random().toString(36).slice(2, 12);
          $('#createKeyStep2').style.display = '';
          $('#createKeyStep1').style.display = 'none';
          $('#mkFoot1').style.display = 'none';
          $('#mkFoot2').style.display = '';
          $('#newKeyValue').textContent = gen;
          var env = (($('.env-tabs button.active') || {}).textContent || '').trim();
          $('#newKeyEnv').textContent = env || 'production';
          pendingKey = {
            name: nameInput.value.trim(),
            env: env || 'production',
            scopes: $$('#permGrid .perm-opt.checked').map(function (opt) { return (opt.textContent || '').trim(); }).filter(Boolean),
            value: gen
          };
          toast('success', 'کلید API ساخته شد', 'کلید فقط همین یکبار نمایش داده میشود.');
        }, 1100);
      });
    }
    var doneKey = doc.getElementById('doneCreateKey');
    if (doneKey) doneKey.addEventListener('click', function () {
      closeModal('createKeyModal');
      var step1 = $('#createKeyStep1'), step2 = $('#createKeyStep2');
      if (step1) step1.style.display = '';
      if (step2) step2.style.display = 'none';
      var f1 = $('#mkFoot1'), f2 = $('#mkFoot2');
      if (f1) f1.style.display = '';
      if (f2) f2.style.display = 'none';
      insertCreatedKey();
      resetCreateForm();
    });
    function buildKeyRow(p) {
      var row = doc.createElement('div');
      row.className = 'key-row';
      row.setAttribute('data-key-row', '');
      row.setAttribute('data-key-name', p.name);
      row.setAttribute('data-key-full', p.value);
      row.setAttribute('data-status', 'active');
      row.setAttribute('data-env', p.env);
      var sc = p.scopes.slice(0, 2).map(function (s) {
        return '<span class="badge badge-blue">' + s + '</span>';
      }).join(' ');
      var envBadge = p.env === 'production'
        ? '<span class="badge badge-amber">تولید</span>'
        : '<span class="badge badge-cyan">آزمایش</span>';
      row.innerHTML =
        '<div class="key-name-block" style="flex:1;min-width:230px">' +
          '<span class="key-name"></span>' +
          '<span class="key-created">ساخته‌شده: <span class="fa-num">همین حالا</span> · آخرین استفاده: <span class="fa-num">هنوز استفاده نشده</span> · ' + envBadge + '</span>' +
        '</div>' +
        '<div class="key-value">' +
          '<code data-masked="1"></code>' +
          '<span class="kv-actions">' +
            '<button class="kv-btn key-reveal-btn" title="نمایش" aria-label="نمایش کلید"><i data-icon="eye"></i></button>' +
            '<button class="kv-btn" data-copy="' + p.value + '" title="کپی" aria-label="کپی کلید"><i data-icon="copy"></i></button>' +
            '<button class="kv-btn" data-rename-key title="تغییر نام" aria-label="تغییر نام"><i data-icon="pencil"></i></button>' +
            '<button class="kv-btn" data-revoke-key title="باطل کردن" aria-label="باطل کردن" style="color:var(--red)"><i data-icon="trash-2"></i></button>' +
          '</span>' +
        '</div>' +
        '<span style="display:flex;gap:6px;flex-wrap:wrap;max-width:280px">' + sc + '<span class="badge badge-green"><span class="dot"></span> فعال</span></span>';
      var nm = row.querySelector('.key-name');
      nm.innerHTML = '<i data-icon="key-round"></i>';
      nm.appendChild(doc.createTextNode(p.name));
      row.querySelector('code').textContent = p.value.slice(0, 7) + '•••••••••••••••';
      mountIcons(row);
      wireKeyRow(row);
      $$('[data-rename-key]', row).forEach(wireRename);
      $$('[data-revoke-key]', row).forEach(wireRevoke);
      return row;
    }
    function insertCreatedKey() {
      if (!pendingKey) return;
      var container = null;
      Array.prototype.slice.call(scope.children).forEach(function (d) {
        if (d.tagName === 'DIV' && !d.classList.contains('card-head')) container = d;
      });
      var row = buildKeyRow(pendingKey);
      if (container) container.insertBefore(row, container.firstChild);
      else scope.appendChild(row);
      row.style.transition = 'background .4s';
      row.style.background = 'rgba(52,211,153,.08)';
      setTimeout(function () { row.style.background = ''; }, 1600);
      var count = $('[data-key-count]');
      if (count) {
        var n = parseInt(count.textContent.replace(/[۰-۹]/g, function (d) { return '۰۱۲۳۴۵۶۷۸۹'.indexOf(d); }), 10);
        count.textContent = faNum(isNaN(n) ? 1 : n + 1);
      }
      var empty = doc.getElementById('keysEmpty');
      if (empty && empty.style.display !== 'none') empty.style.display = 'none';
      pendingKey = null;
    }
    function resetCreateForm() {
      var form = doc.getElementById('createKeyForm');
      if (!form) return;
      var inp = doc.getElementById('keyName');
      if (inp) inp.value = '';
      var wrap = inp ? inp.closest('.field') : null;
      if (wrap) wrap.classList.remove('has-error');
      $$('.field-error', form).forEach(function (s) { s.innerHTML = ''; });
      $$('.env-tabs button', form).forEach(function (b, i) {
        if (i === 0) { b.classList.add('active'); b.style.color = ''; }
        else { b.classList.remove('active'); b.style.color = 'var(--text-3)'; }
      });
      $$('#permGrid .perm-opt', form).forEach(function (opt) {
        var on = /^(users\.read|payments\.read)$/.test((opt.textContent || '').trim());
        var cb = opt.querySelector('input');
        if (cb) cb.checked = on;
        opt.classList.toggle('checked', on);
      });
      $$('select', form).forEach(function (s) { s.selectedIndex = 0; });
    }
    /* empty state toggle demo (dev only) */
    var demoEmpty = doc.getElementById('demoToggleEmpty');
    if (demoEmpty) {
      demoEmpty.addEventListener('click', function () {
        var keys = doc.getElementById('keysTable');
        var empty = doc.getElementById('keysEmpty');
        if (!keys || !empty) return;
        var hidden = keys.style.display === 'none';
        keys.style.display = hidden ? '' : 'none';
        empty.style.display = hidden ? 'none' : 'flex';
        toast('info', 'حالت خالی', hidden ? 'نمودار دید مجدد فعال شد.' : 'این حالت خالی (Empty State) را نمایش میدهد.');
      });
    }
  }

  /* ---------------------------------------------------------------
     18. PRICING billing toggle
  --------------------------------------------------------------- */
  function initPricing() {
    $$('[data-billing]').forEach(function (group) {
      $$('button', group).forEach(function (b) {
        b.addEventListener('click', function () {
          $$('button', group).forEach(function (x) { x.classList.remove('active'); });
          b.classList.add('active');
          var mode = b.getAttribute('data-billing');
          $$('[data-monthly]').forEach(function (el) {
            var m = el.getAttribute('data-monthly'), a = el.getAttribute('data-annual');
            var v = mode === 'annual' ? a : m;
            el.textContent = faMoney(+v);
          });
          $$('.price-period').forEach(function (p) {
            p.textContent = mode === 'annual' ? 'سالانه' : 'ماهانه';
          });
          $$('[data-yearly-note]').forEach(function (n) {
            n.style.display = mode === 'annual' ? '' : 'none';
          });
          group.dispatchEvent(new CustomEvent('bv:billing', { detail: { mode: mode } }));
        });
      });
    });
  }

  /* ---------------------------------------------------------------
     19. ANCHOR TOC highlight
  --------------------------------------------------------------- */
  function initToc() {
    if (!('IntersectionObserver' in window)) return;
    var links = $$('.toc-link');
    if (!links.length) return;
    var map = {};
    links.forEach(function (l) {
      var id = l.getAttribute('href');
      if (id && id.charAt(0) === '#') map[id.slice(1)] = l;
    });
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) {
          links.forEach(function (l) { l.classList.remove('active'); });
          if (map[en.target.id]) map[en.target.id].classList.add('active');
        }
      });
    }, { rootMargin: '-90px 0px -70% 0px' });
    Object.keys(map).forEach(function (id) {
      var el = doc.getElementById(id);
      if (el) io.observe(el);
    });
  }

  /* ---------------------------------------------------------------
     20. LOG DRAWER (dashboard logs)
  --------------------------------------------------------------- */
  function initLogDrawer() {
    $$('tr[data-row][data-log-id]').forEach(function (row) {
      row.addEventListener('click', function () {
        var data = {
          id: row.getAttribute('data-log-id'),
          time: row.getAttribute('data-log-time'),
          method: row.getAttribute('data-log-method'),
          path: row.getAttribute('data-log-path'),
          status: row.getAttribute('data-log-status'),
          ms: row.getAttribute('data-log-ms'),
          ip: row.getAttribute('data-log-ip'),
          env: row.getAttribute('data-log-env')
        };
        var d = doc.getElementById('logDrawer');
        if (!d) return;
        var set = function (id, txt) { var el = doc.getElementById(id); if (el) el.textContent = txt; };
        set('ldRequestId', data.id); set('ldTime', data.time); set('ldPath', data.path);
        set('ldMethod', data.method); set('ldStatus', data.status); set('ldMs', data.ms);
        set('ldIp', data.ip); set('ldEnv', data.env);
        var st = doc.getElementById('ldStatusBadge');
        if (st) {
          var s = +data.status;
          st.className = 'badge ' + (s < 400 ? 'badge-green' : s < 500 ? 'badge-amber' : 'badge-red');
          st.textContent = 'HTTP ' + data.status;
        }
        openDrawer('logDrawer');
      });
    });
  }

  /* ---------------------------------------------------------------
     21. NOTIFICATIONS
  --------------------------------------------------------------- */
  function initNotifications() {
    $$('[data-notif-read]').forEach(function (b) {
      b.addEventListener('click', function () {
        var item = b.closest('.notif-item');
        if (item) item.classList.remove('unread');
        toast('success', 'خوانده شد', 'اعلان بهعنوان خواندهشده علامت خورد.');
      });
    });
    var markAll = doc.getElementById('markAllRead');
    if (markAll) markAll.addEventListener('click', function () {
      $$('.notif-item.unread').forEach(function (n) { n.classList.remove('unread'); });
      toast('success', 'همه اعلانها خوانده شد', 'اعلانهای جدید به صفر رسیدند.');
      var badge = $('#notifBadge');
      if (badge) badge.style.display = 'none';
    });
  }

  /* ---------------------------------------------------------------
     22. NEWSLETTER (footer)
  --------------------------------------------------------------- */
  function initNewsletter() {
    $$('[data-newsletter]').forEach(function (btn) {
      btn.addEventListener('click', function () {
        var input = btn.closest('.newsletter') ? btn.closest('.newsletter').querySelector('input') : null;
        if (input && input.value && !/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(input.value)) {
          toast('error', 'ایمیل معتبر نیست', 'لطفاً یک ایمیل صحیح وارد کنید.');
          return;
        }
        btn.classList.add('btn-loading');
        setTimeout(function () {
          btn.classList.remove('btn-loading');
          btn.textContent = 'عضو شدید';
          toast('success', 'عضویت در خبرنامه', 'از این پس خبرهای بلو ورتکس را دریافت می‌کنید. (دمو)');
        }, 900);
      });
    });
  }

  /* ---------------------------------------------------------------
     THEME (تیره / روشن) — persisted in localStorage("bv-theme")
  --------------------------------------------------------------- */
  function currentTheme() {
    return doc.documentElement.getAttribute('data-theme') === 'light' ? 'light' : 'dark';
  }
  function syncThemeToggle() {
    var light = currentTheme() === 'light';
    $$('[data-theme-toggle]').forEach(function (b) {
      var ic = $('[data-icon]', b);
      if (ic) setIcon(ic, light ? 'moon' : 'sun');
      b.setAttribute('aria-label', light ? 'تغییر به حالت تیره' : 'تغییر به حالت روشن');
      b.title = light ? 'حالت تیره' : 'حالت روشن';
    });
    $$('[data-theme-opt]').forEach(function (b) {
      b.classList.toggle('active', b.getAttribute('data-theme-opt') === currentTheme());
      b.setAttribute('aria-pressed', (b.getAttribute('data-theme-opt') === currentTheme()) ? 'true' : 'false');
    });
  }
  function applyTheme(t) {
    if (t !== 'light' && t !== 'dark') return;
    doc.documentElement.setAttribute('data-theme', t);
    try { localStorage.setItem('bv-theme', t); } catch (e) {}
    var tc = $('meta[name="theme-color"]');
    if (tc) tc.setAttribute('content', t === 'light' ? '#F4F6F9' : '#050505');
    syncThemeToggle();
    doc.dispatchEvent(new CustomEvent('bv:theme', { detail: { theme: t } }));
  }
  function toggleTheme() { applyTheme(currentTheme() === 'light' ? 'dark' : 'light'); }
  function setIcon(el, name) {
    if (!el) return;
    var old = el.querySelector('svg');
    if (old) el.removeChild(old);
    delete el.dataset.iconized;
    el.setAttribute('data-icon', name);
    mountIcons(el);
  }
  function initTheme() {
    $$('[data-theme-toggle]').forEach(function (b) { b.addEventListener('click', toggleTheme); });
    $$('[data-theme-opt]').forEach(function (b) {
      b.addEventListener('click', function () { applyTheme(b.getAttribute('data-theme-opt')); });
    });
    syncThemeToggle();
  }

  /* ---------------------------------------------------------------
     GO
  --------------------------------------------------------------- */
  function init() {
    mountIcons();
    initTheme();
    initTabs();
    initDropdowns();
    initCopy();
    initForms();
    initPasswordToggles();
    initChrome();
    initDateRange();
    initFilters();
    initExplorer();
    initApiKeys();
    initPricing();
    initToc();
    initLogDrawer();
    initDrawers();
    initNotifications();
    initNewsletter();
    if (window.BVCharts) { try { BVCharts.mount(); } catch (e) {} }
  }

  if (doc.readyState === 'loading') doc.addEventListener('DOMContentLoaded', init);
  else init();

  /* expose (for charts + debug) */
  window.BV = {
    faNum: faNum, faNumShort: faNumShort, faPct: faPct, faMoney: faMoney, faDigits: faDigits,
    faDate: faDate, faDateFull: faDateFull, faStamp: faStamp, timeAgo: timeAgo,
    toast: toast, iconSvg: iconSvg, mountIcons: mountIcons,
    openModal: openModal, closeModal: closeModal, openDrawer: openDrawer, closeDrawer: closeDrawer,
    openPalette: openPalette, closePalette: closePalette, openSearch: openSearch, closeSearch: closeSearch,
    renderSearch: renderSearch, renderPalette: renderPalette, copyText: copyText,
    currentTheme: currentTheme, applyTheme: applyTheme, toggleTheme: toggleTheme
  };
})();
