/* ==========================================================================
   BLUE VERTEX — ADMIN CONSOLE — admin.js
   Layer 4 interactions: tables (sort/filter/search/pager/select/bulk),
   drawers, modals (typed confirm), palette (Ctrl+K), global search (Ctrl+/),
   tabs, date-range pills, flags rollout, tickets, notifications, audit.
   Data comes exclusively from window.ADMIN (admin-data.js).
   ========================================================================== */
(function () {
  'use strict';
  var doc = document;
  var $ = function (s, c) { return (c || doc).querySelector(s); };
  var $$ = function (s, c) { return Array.prototype.slice.call((c || doc).querySelectorAll(s)); };
  var A = window.ADMIN || {};
  var fmt = function (v) { return (window.BV && BV.faNum) ? BV.faNum(v) : String(v); };
  var money = function (v) { return fmt(v) + ' تومان'; };
  var esc = function (s) { return String(s == null ? '' : s).replace(/[&<>"']/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]; }); };
  var ic = function (n) { return (window.BV && BV.iconSvg) ? BV.iconSvg(n) : ''; };
  var toast = function (t, m, s) { if (window.BV) BV.toast(t, m, s); };

  function byId(list, id) { for (var i = 0; i < list.length; i++) if (list[i].id === id) return list[i]; return null; }
  function pushAudit(action, target) {
    A.audit.unshift({
      id: 'AUD-' + fmt(2950 + A.audit.length),
      actor: 'مریم کریمی', action: action, target: target,
      at: 'همین حالا', ip: '5.122.30.77', ua: 'مرورگر · پنل ادمین',
      before: '—', after: 'ثبت از طریق پنل ادمین', result: 'success'
    });
    var t = $('[data-ad-audit-count]');
    if (t) t.textContent = fmt(A.audit.length);
  }

  /* ====================================================== STATUS BADGES */
  var ST = {
    active: { c: 'badge badge-green', l: 'فعال' },
    suspended: { c: 'badge', l: 'تعلیق‌شده' },
    churned: { c: 'badge', l: 'لغوشده' },
    past_due: { c: 'badge badge-amber', l: 'پرداخت معوق' },
    trial: { c: 'badge badge-cyan', l: 'آزمایشی' },
    trialing: { c: 'badge badge-cyan', l: 'آزمایشی' },
    canceled: { c: 'badge', l: 'لغوشده' },
    paid: { c: 'badge badge-green', l: 'پرداخت‌شده' },
    pending: { c: 'badge badge-amber', l: 'در انتظار' },
    failed: { c: 'badge', l: 'ناموفق' },
    refunded: { c: 'badge badge-cyan', l: 'مسترد' },
    none: { c: 'badge', l: '—' },
    success: { c: 'badge badge-green', l: 'موفق' },
    open: { c: 'badge badge-cyan', l: 'باز' },
    urgent: { c: 'badge badge-amber', l: 'فوری' },
    resolved: { c: 'badge badge-green', l: 'حل‌شده' },
    wait_customer: { c: 'badge', l: 'در انتظار مشتری' },
    wait_support: { c: 'badge badge-amber', l: 'در انتظار پشتیبانی' },
    monitoring: { c: 'badge badge-cyan', l: 'مانیتورینگ' },
    blocked: { c: 'badge', l: 'مسدود' },
    terminated: { c: 'badge', l: 'پایان‌یافته' },
    flagged: { c: 'badge badge-amber', l: 'نشان‌دار' },
    done: { c: 'badge badge-green', l: 'انجام‌شده' },
    draft: { c: 'badge', l: 'پیش‌نویس' },
    review: { c: 'badge badge-amber', l: 'در بازبینی' },
    published: { c: 'badge badge-green', l: 'منتشرشده' },
    archived: { c: 'badge', l: 'بایگانی' },
    scheduled: { c: 'badge badge-cyan', l: 'زمان‌بندی‌شده' },
    info: { c: 'badge badge-cyan', l: 'اطلاع‌رسانی' },
    warning: { c: 'badge badge-amber', l: 'هشدار' },
    update: { c: 'badge badge-blue', l: 'به‌روزرسانی' },
    critical: { c: 'badge', l: 'بحرانی' },
    enabled: { c: 'badge badge-green', l: 'فعال' },
    disabled: { c: 'badge', l: 'غیرفعال' }
  };
  function stb(s) { var st = ST[s] || { c: 'badge', l: s }; return '<span class="' + st.c + '">' + st.l + '</span>'; }
  var PRIO = {
    critical: '<span class="risk risk-critical">' + ic('siren') + 'بحرانی</span>',
    high: '<span class="risk risk-high">' + ic('alert-triangle') + 'زیاد</span>',
    medium: '<span class="risk risk-medium">' + ic('alert-circle') + 'متوسط</span>',
    low: '<span class="risk risk-low">' + ic('info') + 'کم</span>'
  };
  function risk(r) { return '<span class="risk risk-' + esc(r) + '">' + ic(r === 'critical' ? 'siren' : r === 'high' ? 'alert-triangle' : r === 'medium' ? 'alert-circle' : r === 'low' || r === 'none' ? 'shield-check' : 'info') + esc({ low: 'کم', medium: 'متوسط', high: 'زیاد', critical: 'بحرانی', none: '—' }[r] || r) + '</span>'; }

  /* =================================================== TABLE ENGINE */
  var state = {};       /* key → {page, sort, dir, filters, search, sel:Set, size} */
  function T(key) {
    if (!state[key]) state[key] = { page: 0, sort: null, dir: 1, filters: {}, search: '', sel: {}, size: 8 };
    return state[key];
  }
  function ROWS(entity) {
    if (entity === 'users') return A.users;
    if (entity === 'orgs') return A.orgs;
    if (entity === 'subs') return A.subs;
    if (entity === 'invoices') return A.invoices;
    if (entity === 'payments') return A.payments;
    if (entity === 'tickets') return A.tickets;
    if (entity === 'flags') return A.flags;
    if (entity === 'security') return A.security;
    if (entity === 'audit') return A.audit;
    if (entity === 'incidents') return A.incidents;
    if (entity === 'blog') return A.content.blog;
    if (entity === 'docs') return A.content.docs;
    if (entity === 'changelog') return A.content.changelog;
    if (entity === 'annc') return A.content.annc;
    if (entity === 'notif') return A.notifications;
    return [];
  }
  var CELL = {
    users: function (u) {
      return '<td class="cell-main">' + ic('user-round') + ' ' + esc(u.name) + '<span class="cell-sub">' + esc(u.email) + '</span></td>' +
        '<td>' + (byId(A.orgs, u.org) || {}).name + '</td>' +
        '<td><span class="badge badge-blue">' + esc(u.plan) + '</span></td>' +
        '<td>' + stb(u.status) + '</td>' +
        '<td class="num">' + esc(u.last) + '</td>' +
        '<td class="cell-sub">' + esc(u.joined) + '</td>' +
        '<td><span class="row-act">' +
        '<button data-action="view" title="مشاهده"><i data-icon="eye"></i></button>' +
        '<button data-action="notify" title="ارسال اعلان"><i data-icon="bell"></i></button>' +
        '<button data-action="danger" data-op="suspend" title="تعلیق"><i data-icon="user-x" style="color:var(--red)"></i></button></span></td>';
    },
    orgs: function (o) {
      return '<td class="cell-main">' + ic('building-2') + ' ' + esc(o.name) + '<span class="cell-sub">' + esc(o.id) + '</span></td>' +
        '<td>' + esc(o.owner) + '</td>' +
        '<td class="num">' + fmt(o.members) + '</td>' +
        '<td><span class="badge badge-blue">' + esc(o.plan) + '</span></td>' +
        '<td class="num">' + fmt(o.req30) + '</td>' +
        '<td class="num">' + money(o.mrr) + '</td>' +
        '<td>' + stb(o.status) + '</td>' +
        '<td>' + risk(o.risk) + '</td>';
    },
    subs: function (s) {
      return '<td class="cell-main">' + esc(s.orgName) + '<span class="cell-sub">' + esc(s.id) + '</span></td>' +
        '<td><span class="badge badge-blue">' + esc(s.plan) + '</span></td>' +
        '<td class="num">' + money(s.price) + '</td>' +
        '<td>' + stb(s.status) + '</td>' +
        '<td class="cell-sub">' + esc(s.renew) + '</td>' +
        '<td><div class="progress thin" style="width:86px"><i style="width:' + s.usage + '%"></i></div><span class="cell-sub num">' + fmt(s.usage) + '٪</span></td>' +
        '<td>' + stb(s.pay) + '</td>';
    },
    invoices: function (v) {
      return '<td class="cell-main ltr" style="direction:ltr">' + esc(v.id) + '</td>' +
        '<td>' + esc(v.orgName) + '</td>' +
        '<td class="num">' + money(v.amount) + '</td>' +
        '<td>' + stb(v.status) + '</td>' +
        '<td class="cell-sub">' + esc(v.issue) + '</td>' +
        '<td class="cell-sub">' + esc(v.due) + '</td>' +
        '<td><span class="row-act"><button data-action="view" title="مشاهده"><i data-icon="eye"></i></button><button data-action="export" title="دانلود"><i data-icon="download"></i></button></span></td>';
    },
    payments: function (p) {
      return '<td class="cell-main ltr" style="direction:ltr">' + esc(p.id) + '</td>' +
        '<td>' + esc(p.orgName) + '</td>' +
        '<td class="num">' + money(p.amount) + '</td>' +
        '<td>' + stb(p.status) + '</td>' +
        '<td>' + esc(p.method) + '</td>' +
        '<td class="cell-sub">' + esc(p.at) + '</td>' +
        '<td>' + (p.fail ? '<span class="cell-sub" title="' + esc(p.fail) + '">' + esc(p.fail.slice(0, 34)) + '…</span>' : '—') + '</td>';
    },
    tickets: function (t) {
      return '<td class="cell-main ltr" style="direction:ltr">' + esc(t.id) + '</td>' +
        '<td>' + esc(t.subject) + '</td>' +
        '<td class="cell-sub">' + esc(t.user) + '</td>' +
        '<td>' + esc(t.orgName) + '</td>' +
        '<td>' + (PRIO[t.priority] || '—') + '</td>' +
        '<td>' + stb(t.status) + '</td>' +
        '<td class="cell-sub">' + esc(t.owner) + '</td>' +
        '<td class="cell-sub">' + esc(t.last) + '</td>';
    },
    flags: function (f) {
      return '<td class="cell-main">' + esc(f.name) + '<span class="cell-sub ltr" style="direction:ltr">' + esc(f.key) + '</span></td>' +
        '<td><span class="fswitch' + (f.on ? ' on' : '') + '" data-flag-toggle="' + esc(f.id) + '" role="switch" aria-checked="' + f.on + '" tabindex="0" aria-label="وضعیت ' + esc(f.name) + '"></span></td>' +
        '<td>' + (f.env === 'production' ? '<span class="badge badge-amber">تولید</span>' : '<span class="badge badge-cyan">آزمایش</span>') + '</td>' +
        '<td class="num">' + fmt(f.rollout) + '٪</td>' +
        '<td class="cell-sub">' + esc(f.created) + '</td>' +
        '<td class="cell-sub">' + esc(f.changed) + '</td>' +
        '<td>' + esc(f.owner) + '</td>';
    },
    security: function (e) {
      return '<td class="cell-main">' + esc(e.type) + '<span class="cell-sub">' + esc(e.id) + '</span></td>' +
        '<td>' + esc(e.user) + '</td>' +
        '<td class="ltr" style="direction:ltr">' + esc(e.ip) + '</td>' +
        '<td class="cell-sub">' + esc(e.device) + '</td>' +
        '<td class="cell-sub">' + esc(e.at) + '</td>' +
        '<td>' + (PRIO[e.severity] || '—') + '</td>' +
        '<td>' + stb(e.status) + '</td>';
    },
    audit: function (a) {
      return '<td class="cell-main">' + esc(a.action) + '<span class="cell-sub ltr" style="direction:ltr">' + esc(a.id) + '</span></td>' +
        '<td>' + esc(a.actor) + '</td>' +
        '<td class="cell-sub">' + esc(a.target) + '</td>' +
        '<td class="cell-sub">' + esc(a.at) + '</td>' +
        '<td class="ltr" style="direction:ltr">' + esc(a.ip) + '</td>' +
        '<td>' + stb(a.result) + '</td>';
    },
    incident: function (n) {
      return '<td class="cell-main">' + esc(n.title) + '</td>' +
        '<td>' + (PRIO[n.severity] || '—') + '</td>' +
        '<td>' + esc(n.service) + '</td>' +
        '<td class="cell-sub">' + esc(n.started) + '</td>' +
        '<td class="cell-sub">' + esc(n.duration) + '</td>' +
        '<td>' + stb(n.status) + '</td>' +
        '<td class="cell-sub">' + esc(n.team) + '</td>';
    },
    blog: function (b) {
      return '<td class="cell-main">' + esc(b.title) + '</td><td>' + esc(b.author) + '</td><td>' + stb(b.status) + '</td><td class="num">' + esc(b.views) + '</td><td class="cell-sub">' + esc(b.at) + '</td>' +
        '<td><span class="row-act"><button data-action="edit" title="ویرایش"><i data-icon="pencil"></i></button><button data-action="publish" title="انتشار"><i data-icon="send"></i></button></span></td>';
    },
    docs: function (d) {
      return '<td class="cell-main">' + esc(d.title) + '</td><td>' + esc(d.cat) + '</td><td>' + esc(d.author) + '</td><td>' + stb(d.status) + '</td><td class="cell-sub">' + esc(d.updated) + '</td><td class="num">' + esc(d.views) + '</td>' +
        '<td><span class="row-act"><button data-action="edit" title="ویرایش"><i data-icon="pencil"></i></button><button data-action="archive" title="بایگانی"><i data-icon="archive"></i></button></span></td>';
    },
    changelog: function (c) {
      return '<td class="cell-main ltr" style="direction:ltr"><span class="badge badge-blue">' + esc(c.version) + '</span></td><td>' + esc(c.title) + '</td><td>' + stb(c.status) + '</td><td class="cell-sub">' + esc(c.at) + '</td><td>' + esc(c.author) + '</td>' +
        '<td><span class="row-act"><button data-action="edit" title="ویرایش"><i data-icon="pencil"></i></button></span></td>';
    },
    annc: function (a) {
      return '<td class="cell-main">' + esc(a.title) + '</td><td>' + stb(a.type) + '</td><td>' + stb(a.status) + '</td><td class="cell-sub">' + esc(a.at) + '</td><td>' + esc(a.author) + '</td>' +
        '<td><span class="row-act"><button data-action="edit" title="ویرایش"><i data-icon="pencil"></i></button><button data-action="publish" title="انتشار"><i data-icon="send"></i></button></span></td>';
    },
    notif: function (n) {
      return '<div class="notif-item' + (n.unread ? ' unread' : '') + '" data-notif="' + esc(n.id) + '">' +
        '<span class="n-ic" style="background:' + nIcBg(n.type) + ';color:' + nIcC(n.type) + '">' + ic(nIc(n.type)) + '</span>' +
        '<div class="n-body"><b>' + esc(n.title) + '</b><p>' + esc(n.text) + '</p><div class="n-at">' + esc(n.at) + '</div></div>' +
        (n.unread ? '<span class="n-dot"></span>' : '') + '</div>';
    }
  };
  CELL.incidents = CELL.incident;

  var FILTERS = { users: ['status', 'plan', 'org'], subs: ['status', 'pay'], tickets: ['priority', 'status'], notif: ['type'] };
  function filtered(entity) {
    var st = T(entity), rows = ROWS(entity).slice();
    Object.keys(st.filters).forEach(function (f) {
      var v = st.filters[f];
      if (v) rows = rows.filter(function (r) { return String(r[f]) === v; });
    });
    if (st.search) {
      var q = st.search.toLowerCase();
      rows = rows.filter(function (r) {
        return JSON.stringify(r).toLowerCase().indexOf(q) !== -1;
      });
    }
    if (st.sort) {
      rows.sort(function (a, b) {
        var x = a[st.sort], y = b[st.sort];
        if (typeof x === 'string') return x.localeCompare(y, 'fa') * st.dir;
        return ((x || 0) - (y || 0)) * st.dir;
      });
    }
    return rows;
  }
  function renderTable(entity) {
    var tbl = $('[data-ad-table="' + entity + '"]');
    if (!tbl) return;
    var st = T(entity), body = tbl.tBodies[0];
    var rows = filtered(entity);
    var pages = Math.max(1, Math.ceil(rows.length / st.size));
    if (st.page >= pages) st.page = pages - 1;
    var start = st.page * st.size, slice = rows.slice(start, start + st.size);
    if (!slice.length) {
      body.innerHTML = '<tr><td colspan="' + tbl.tHead.rows[0].cells.length + '" style="text-align:center;padding:34px 12px">' +
        ic('search-x') + '<div class="t-caption" style="margin-top:10px;color:var(--text-4)">' +
        (rows.length ? '—' : 'هیچ ردیفی مطابق فیلترهای انتخاب‌شده پیدا نشد.') + '</div></td></tr>';
    } else {
      body.innerHTML = slice.map(function (r) {
        var sel = st.sel[r.id] ? ' selected' : '';
        var cb = tbl.querySelector('thead input.ck-all') ? '<td><input type="checkbox" class="ck" data-uid="' + esc(r.id) + '"' + (st.sel[r.id] ? ' checked' : '') + ' aria-label="انتخاب ردیف"></td>' : '';
        return '<tr data-id="' + esc(r.id) + '" data-entity="' + entity + '"' + (sel ? ' class="selected"' : '') + '>' + cb + CELL[entity](r) + '</tr>';
      }).join('');
    }
    /* row action icons are injected above; iconize them now */
    if (window.BV) BV.mountIcons(body);
    /* sort arrows */
    $$('th.sortable', tbl).forEach(function (th) {
      var d = th.querySelector('.dir');
      th.dataset.dir = '';
      if (th.dataset.sort === st.sort) { th.dataset.dir = st.dir === 1 ? 'asc' : 'desc'; if (d) d.textContent = st.dir === 1 ? '▲' : '▼'; }
      else if (d) d.textContent = '';
    });
    /* pager */
    var pg = $('[data-ad-pager="' + entity + '"]');
    if (pg) {
      var msg = $('[data-ad-pmsg="' + entity + '"]', pg);
      if (msg) msg.textContent = 'نمایش ' + fmt(start + 1) + '–' + fmt(Math.min(start + st.size, rows.length)) + ' از ' + fmt(rows.length) + ' ردیف';
      pg.innerHTML = pg.innerHTML.replace(/<button.*?pnav.*?<\/button>/, '');
      var nav = $('[data-ad-pnav="' + entity + '"]');
      if (!nav && pg) {
        nav = doc.createElement('span'); nav.setAttribute('data-ad-pnav', entity);
        pg.appendChild(nav);
      }
      if (nav) {
        var h = '';
        for (var i = 0; i < pages; i++) h += '<button class="page-btn' + (i === st.page ? ' cur' : '') + '" data-page="' + i + '">' + fmt(i + 1) + '</button>';
        nav.innerHTML = h;
      }
    }
    /* bulk bar */
    updateBulk(entity);
  }
  function updateBulk(entity) {
    var bar = $('[data-ad-bulk="' + entity + '"]');
    if (!bar) return;
    var st = T(entity), n = Object.keys(st.sel).length;
    bar.classList.toggle('show', n > 0);
    var c = $('[data-ad-bcount]', bar);
    if (c) c.textContent = fmt(n);
  }
  function bindTable(entity) {
    var tbl = $('[data-ad-table="' + entity + '"]');
    if (!tbl) return;
    var st = T(entity);
    $$('th.sortable', tbl).forEach(function (th) {
      th.addEventListener('click', function () {
        var k = th.dataset.sort;
        if (st.sort === k) st.dir *= -1; else { st.sort = k; st.dir = 1; }
        renderTable(entity);
      });
    });
    tbl.addEventListener('click', function (e) {
      var row = e.target.closest('tr[data-id]');
      var act = e.target.closest('[data-action]');
      if (act && row) { onAction(entity, act.dataset.action, row.dataset.id, act); return; }
      var btn = e.target.closest('[data-flag-toggle]');
      if (btn) { toggleFlag(btn.dataset.flagToggle); return; }
      if (e.target.classList && e.target.classList.contains('ck')) {
        var id = e.target.dataset.uid;
        if (e.target.checked) st.sel[id] = 1; else delete st.sel[id];
        updateBulk(entity);
        return;
      }
      if (row && row.dataset.entity === entity && !row.querySelector('.ck')) openDrawerFor(entity, row.dataset.id);
    });
    var all = $('thead input.ck-all', tbl);
    if (all) all.addEventListener('change', function () {
      filtered(entity).slice(st.page * st.size, st.page * st.size + st.size).forEach(function (r) {
        if (all.checked) st.sel[r.id] = 1; else delete st.sel[r.id];
      });
      renderTable(entity);
    });
    /* flag switches are spans (role="switch", tabindex=0): keyboard support */
    tbl.addEventListener('keydown', function (e) {
      if (e.key !== 'Enter' && e.key !== ' ') return;
      var sw = e.target.closest('[data-flag-toggle]');
      if (!sw) return;
      e.preventDefault();
      toggleFlag(sw.dataset.flagToggle);
    });
    ['search', 'filter'].forEach(function (kind) {
      $$('[data-ad-' + kind + '="' + entity + '"]').forEach(function (el) {
        el.addEventListener(kind === 'search' ? 'input' : 'change', function () {
          if (kind === 'search') st.search = el.value;
          else st.filters[el.dataset.field] = el.value;
          st.page = 0;
          renderTable(entity);
        });
      });
    });
    $$('[data-ad-pager="' + entity + '"]').forEach(function (pg) {
      pg.addEventListener('click', function (e) {
        var b = e.target.closest('[data-page]');
        if (b) { st.page = parseInt(b.dataset.page, 10); renderTable(entity); }
      });
    });
    $$('[data-ad-size="' + entity + '"]').forEach(function (el) {
      el.addEventListener('change', function () { st.size = parseInt(el.value, 10) || 8; st.page = 0; renderTable(entity); });
    });
    renderTable(entity);
  }
  function onAction(entity, act, id, el) {
    var row = byId(ROWS(entity), id);
    if (!row) return;
    if (act === 'view') { openDrawerFor(entity, id); return; }
    if (act === 'export') { fakeExport('فاکتور ' + row.id); return; }
    if (act === 'edit' || act === 'publish' || act === 'archive' || act === 'notify') {
      var msgs = {
        edit: ['ویرایش ' + (row.name || row.title || row.id), 'ویرایشگر محتوا در نسخه‌ی اتصال، به این سرویس متصل می‌شود.'],
        publish: ['انتشار «' + (row.title || row.name || row.id) + '»', 'هیچ‌گاه صفحه‌ی خالی نمی‌سازیم؛ انتشار شبیه‌سازی و در گزارش ثبت شد.'],
        archive: ['بایگانی «' + row.title + '»', 'سند به بایگانی منتقل شد.'],
        notify: ['اعلان برای ' + row.name, 'یک اعلان آزمایشی برای کاربر ارسال شد.']
      };
      var m = msgs[act];
      confirmAd({ title: m[0], text: m[1], ok: 'ادامه' }, function () { toast('success', 'انجام شد', m[1]); pushAudit(act === 'notify' ? 'ارسال اعلان' : 'ویرایش محتوا', row.name || row.id); });
      return;
    }
    if (act === 'danger' && el.dataset.op === 'suspend') {
      confirmAd({ title: 'تعلیق کاربر ' + row.name, text: 'کاربر از ورود به پنل و همه‌ی نشست‌ها قطع می‌شود. سازمان او به استفاده از کلیدها ادامه می‌دهد.', danger: true, typed: null }, function () {
        row.status = 'suspended';
        toast('success', 'کاربر تعلیق شد', row.name + ' به‌صورت منطقی غیرفعال شد.');
        pushAudit('تعلیق کاربر', row.name + ' (' + row.id + ')');
        renderTable(entity);
      });
    }
  }

  /* ===================================================== DRAWER */
  var DETAILS = {
    user: function (u) {
      var o = byId(A.orgs, u.org) || {};
      return '<div class="ad-sec"><h3>' + ic('user-round') + 'اطلاعات پایه</h3><div class="ad-meta">' +
        '<div class="kv"><span>ایمیل</span><b class="ltr" style="direction:ltr">' + esc(u.email) + '</b></div>' +
        '<div class="kv"><span>شناسه</span><b class="ltr" style="direction:ltr">' + esc(u.id) + '</b></div>' +
        '<div class="kv"><span>سازمان</span><b>' + esc(o.name || '—') + '</b></div>' +
        '<div class="kv"><span>پلن</span><b>' + esc(u.plan) + '</b></div>' +
        '<div class="kv"><span>تاریخ ثبت‌نام</span><b>' + esc(u.joined) + '</b></div>' +
        '<div class="kv"><span>آخرین فعالیت</span><b>' + esc(u.last) + '</b></div>' +
        '<div class="kv"><span>وضعیت</span><b>' + stb(u.status) + '</b></div>' +
        '<div class="kv"><span>احراز دومرحله‌ای</span><b>' + (u.twofa ? 'فعال' : 'غیرفعال') + '</b></div></div></div>' +
        '<div class="ad-sec"><h3>' + ic('activity') + 'فعالیت و مصرف</h3>' +
        '<div class="ad-kv"><span>درخواست‌های ۳۰ روز اخیر</span><b class="num">' + fmt(u.req30) + '</b></div>' +
        '<div class="ad-kv"><span>خطاهای ۳۰ روز اخیر</span><b class="num">' + fmt(u.err30) + '</b></div>' +
        '<div class="ad-kv"><span>نرخ خطا</span><b>' + fmt(Math.round(u.err30 / Math.max(u.req30, 1) * 1000) / 10) + '٪</b></div>' +
        '<div class="ad-kv"><span>MRR</span><b class="num">' + money(u.mrr) + '</b></div></div>' +
        '<div class="ad-sec"><h3>' + ic('shield') + 'امنیت و نشست‌ها</h3>' +
        '<div class="ad-kv"><span>نشست‌های فعال</span><b class="num">' + fmt(u.sessions) + '</b></div>' +
        '<div class="ad-kv"><span>آخرین ورود</span><b>' + esc(u.last) + '</b></div>' +
        '<div class="ad-kv"><span>IP آخرین ورود</span><b class="ltr" style="direction:ltr">' + (u.twofa ? '5.122.30.77' : '185.12.44.9') + '</b></div></div>';
    },
    org: function (o) {
      return '<div class="ad-sec"><h3>' + ic('building-2') + 'سازمان</h3><div class="ad-meta">' +
        '<div class="kv"><span>شناسه</span><b class="ltr" style="direction:ltr">' + esc(o.id) + '</b></div>' +
        '<div class="kv"><span>مالک</span><b>' + esc(o.owner) + '</b></div>' +
        '<div class="kv"><span>تاریخ ایجاد</span><b>' + esc(o.created) + '</b></div>' +
        '<div class="kv"><span>وضعیت</span><b>' + stb(o.status) + '</b></div></div></div>' +
        '<div class="ad-sec"><h3>' + ic('activity') + 'سلامت سازمان</h3>' +
        '<div class="ad-kv"><span>اعضا</span><b class="num">' + fmt(o.members) + '</b></div>' +
        '<div class="ad-kv"><span>درخواست ۳۰ روز</span><b class="num">' + fmt(o.req30) + '</b></div>' +
        '<div class="ad-kv"><span>خطا</span><b class="num">' + fmt(o.err30) + '</b></div>' +
        '<div class="ad-kv"><span>MRR</span><b class="num">' + money(o.mrr) + '</b></div>' +
        '<div class="ad-kv"><span>ریسک</span><b>' + risk(o.risk) + '</b></div>' +
        '<div class="ad-kv"><span>سهمیه‌ی مصرف</span><b class="num">' + fmt(Math.min(99, Math.round(o.req30 / (o.plan === 'سازمانی' ? 10000000 : 5000000) * 100))) + '٪</b></div></div>';
    },
    sub: function (s) {
      var invs = A.invoices.filter(function (v) { return v.orgName === s.orgName; }).slice(0, 3);
      return '<div class="ad-sec"><h3>' + ic('credit-card') + 'اشتراک</h3><div class="ad-meta">' +
        '<div class="kv"><span>مشتری</span><b>' + esc(s.orgName) + '</b></div>' +
        '<div class="kv"><span>شناسه</span><b class="ltr" style="direction:ltr">' + esc(s.id) + '</b></div>' +
        '<div class="kv"><span>پلن</span><b>' + esc(s.plan) + '</b></div>' +
        '<div class="kv"><span>مبلغ</span><b class="num">' + money(s.price) + '</b></div>' +
        '<div class="kv"><span>شروع</span><b>' + esc(s.since) + '</b></div>' +
        '<div class="kv"><span>تمدید</span><b>' + esc(s.renew) + '</b></div>' +
        '<div class="kv"><span>وضعیت</span><b>' + stb(s.status) + '</b></div>' +
        '<div class="kv"><span>پرداخت</span><b>' + stb(s.pay) + '</b></div></div></div>' +
        '<div class="ad-sec"><h3>' + ic('chart-column') + 'مصرف</h3>' +
        '<div class="ad-kv"><span>استفاده از سهمیه</span><b class="num">' + fmt(s.usage) + '٪</b></div>' +
        '<div class="progress" style="margin-top:6px"><i style="width:' + s.usage + '%"></i></div></div>' +
        '<div class="ad-sec"><h3>' + ic('receipt') + 'فاکتورهای اخیر</h3>' + (invs.length ? invs.map(function (v) {
          return '<div class="ad-kv"><span class="ltr" style="direction:ltr">' + esc(v.id) + '</span><b>' + stb(v.status) + ' · ' + money(v.amount) + '</b></div>';
        }).join('') : '<div class="t-caption">فاکتوری ثبت نشده است.</div>') + '</div>';
    },
    ticket: function (t) {
      var th = '<div class="thread">' + t.notes.map(function (m) {
        return '<div class="msg ' + m.role + '"><div class="m-head"><b>' + esc(m.who) + '</b><span>' + esc(m.t) + '</span></div>' + esc(m.text) + '</div>';
      }).join('') + '</div>';
      return '<div class="ad-sec"><h3>' + ic('life-buoy') + 'مکالمه</h3>' + th +
        '<div class="thread" style="margin-top:12px"><div class="msg note">' +
        '<textarea id="adNoteInput" class="input" rows="2" placeholder="یادداشت داخلی — فقط برای تیم پشتیبانی…" aria-label="یادداشت داخلی"></textarea>' +
        '<div style="display:flex;gap:8px;margin-top:8px"><button class="btn btn-secondary btn-sm" id="adNoteSend"><i data-icon="send"></i> ثبت یادداشت</button>' +
        (t.status !== 'resolved' ? '<button class="btn btn-primary btn-sm" id="adNoteResolve"><i data-icon="check"></i> حل تیکت</button>' : '') + '</div></div></div></div>' +
        '<div class="ad-sec"><h3>' + ic('users-round') + 'مشتری</h3><div class="ad-meta">' +
        '<div class="kv"><span>کاربر</span><b>' + esc(t.user) + '</b></div>' +
        '<div class="kv"><span>سازمان</span><b>' + esc(t.orgName) + '</b></div>' +
        '<div class="kv"><span>اولویت</span><b>' + (PRIO[t.priority] || '—') + '</b></div>' +
        '<div class="kv"><span>مسئول</span><b>' + esc(t.owner) + '</b></div></div></div>';
    },
    flag: function (f) {
      var opts = [0, 10, 25, 50, 75, 100];
      return '<div class="ad-sec"><h3>' + ic('flag') + 'جزئیات</h3><div class="ad-meta">' +
        '<div class="kv"><span>نام</span><b>' + esc(f.name) + '</b></div>' +
        '<div class="kv"><span>کلید</span><b class="ltr" style="direction:ltr">' + esc(f.key) + '</b></div>' +
        '<div class="kv"><span>محیط</span><b>' + (f.env === 'production' ? 'تولید' : 'آزمایش') + '</b></div>' +
        '<div class="kv"><span>ساخته‌شده</span><b>' + esc(f.created) + '</b></div>' +
        '<div class="kv"><span>آخرین تغییر</span><b>' + esc(f.changed) + '</b></div>' +
        '<div class="kv"><span>مالک</span><b>' + esc(f.owner) + '</b></div></div>' +
        '<p class="t-caption" style="margin-top:10px">' + esc(f.desc) + '</p></div>' +
        '<div class="ad-sec"><h3>' + ic('sliders-horizontal') + 'توزیع تدریجی (Rollout)</h3><div class="rollout">' +
        '<div class="r-scale" data-rscale="' + esc(f.id) + '">' + opts.map(function (p) {
          return '<button data-rp="' + p + '"' + (p === f.rollout ? ' class="active"' : '') + '>' + (p === 0 ? '۰٪' : fmt(p) + '٪') + '</button>';
        }).join('') + '</div>' +
        '<div class="r-track"><i style="width:' + f.rollout + '%"></i></div>' +
        '<div class="r-note">' + ic('alert-triangle') + '<span>افزایش توزیع روی «تولید» نیاز به تأیید دارد و در سابقه‌ی ممیزی ثبت می‌شود.</span></div></div></div>';
    },
    audit: function (a) {
      return '<div class="ad-sec"><h3>' + ic('scroll-text') + 'رویداد</h3><div class="ad-meta">' +
        '<div class="kv"><span>شناسه</span><b class="ltr" style="direction:ltr">' + esc(a.id) + '</b></div>' +
        '<div class="kv"><span>فرد</span><b>' + esc(a.actor) + '</b></div>' +
        '<div class="kv"><span>اقدام</span><b>' + esc(a.action) + '</b></div>' +
        '<div class="kv"><span>هدف</span><b>' + esc(a.target) + '</b></div>' +
        '<div class="kv"><span>زمان</span><b>' + esc(a.at) + '</b></div>' +
        '<div class="kv"><span>نتیجه</span><b>' + stb(a.result) + '</b></div>' +
        '<div class="kv"><span>IP</span><b class="ltr" style="direction:ltr">' + esc(a.ip) + '</b></div>' +
        '<div class="kv"><span>User Agent</span><b class="ltr" style="direction:ltr">' + esc(a.ua) + '</b></div></div></div>' +
        '<div class="ad-sec"><h3>' + ic('git-compare') + 'تغییرات</h3>' +
        '<div class="ad-kv"><span>قبل</span><b>' + esc(a.before) + '</b></div>' +
        '<div class="ad-kv"><span>بعد</span><b>' + esc(a.after) + '</b></div></div>';
    },
    incident: function (n) {
      return '<div class="ad-sec"><h3>' + ic('siren') + 'شرح</h3>' +
        '<p class="t-sm" style="line-height:2">' + esc(n.desc) + '</p>' +
        '<div class="ad-meta" style="margin-top:12px">' +
        '<div class="kv"><span>سرویس</span><b>' + esc(n.service) + '</b></div>' +
        '<div class="kv"><span>شدت</span><b>' + (PRIO[n.severity] || '—') + '</b></div>' +
        '<div class="kv"><span>شروع</span><b>' + esc(n.started) + '</b></div>' +
        '<div class="kv"><span>مدت</span><b>' + esc(n.duration) + '</b></div>' +
        '<div class="kv"><span>تیم مسئول</span><b>' + esc(n.team) + '</b></div>' +
        '<div class="kv"><span>وضعیت</span><b>' + stb(n.status) + '</b></div></div></div>';
    },
    invoice: function (v) {
      return '<div class="ad-sec"><h3>' + ic('receipt') + 'فاکتور</h3><div class="ad-meta">' +
        '<div class="kv"><span>شماره</span><b class="ltr" style="direction:ltr">' + esc(v.id) + '</b></div>' +
        '<div class="kv"><span>مشتری</span><b>' + esc(v.orgName) + '</b></div>' +
        '<div class="kv"><span>مبلغ</span><b class="num">' + money(v.amount) + '</b></div>' +
        '<div class="kv"><span>وضعیت</span><b>' + stb(v.status) + '</b></div>' +
        '<div class="kv"><span>صدور</span><b>' + esc(v.issue) + '</b></div>' +
        '<div class="kv"><span>سررسید</span><b>' + esc(v.due) + '</b></div></div></div>';
    },
    payment: function (p) {
      return '<div class="ad-sec"><h3>' + ic('credit-card') + 'تراکنش</h3><div class="ad-meta">' +
        '<div class="kv"><span>شناسه</span><b class="ltr" style="direction:ltr">' + esc(p.id) + '</b></div>' +
        '<div class="kv"><span>سازمان</span><b>' + esc(p.orgName) + '</b></div>' +
        '<div class="kv"><span>مبلغ</span><b class="num">' + money(p.amount) + '</b></div>' +
        '<div class="kv"><span>وضعیت</span><b>' + stb(p.status) + '</b></div>' +
        '<div class="kv"><span>روش</span><b>' + esc(p.method) + '</b></div>' +
        '<div class="kv"><span>زمان</span><b>' + esc(p.at) + '</b></div></div>' +
        (p.fail ? '<div class="rollout r-note" style="margin-top:12px">' + ic('alert-circle') + '<span>' + esc(p.fail) + '</span></div>' : '') + '</div>';
    }
  };
  var DRAWER_FOOT = {
    user: function (u) {
      return '<button class="btn btn-secondary btn-sm" data-dact="notify"><i data-icon="bell"></i> ارسال اعلان</button>' +
        '<button class="btn btn-ghost btn-sm" data-dact="role"><i data-icon="shield"></i> تغییر نقش</button>' +
        '<button class="btn btn-ghost btn-sm" data-dact="sessions"><i data-icon="log-out"></i> خروج از نشست‌ها</button>' +
        (u.status !== 'suspended' ? '<button class="btn btn-danger btn-sm" data-dact="suspend"><i data-icon="user-x"></i> تعلیق</button>' : '<button class="btn btn-primary btn-sm" data-dact="activate"><i data-icon="user-check"></i> فعال‌سازی</button>');
    },
    sub: function (s) {
      return '<button class="btn btn-ghost btn-sm" data-dact="cancel"><i data-icon="trash-2"></i> لغو اشتراک</button>';
    },
    ticket: function (t) { return ''; }
  };
  function drawerOpen(id) { var d = doc.getElementById('adDrawer'); if (d) d.classList.add('open'); var bd = doc.getElementById('adDrBack'); if (bd) bd.classList.add('open'); doc.body.style.overflow = 'hidden'; }
  function drawerClose() { var d = doc.getElementById('adDrawer'); if (d) d.classList.remove('open'); var bd = doc.getElementById('adDrBack'); if (bd) bd.classList.remove('open'); if (!$('.drawer.open')) doc.body.style.overflow = ''; }
  /* table entity names are plural; detail templates are keyed 1:1 */
  var DETAIL_KEY = { users: 'user', orgs: 'org', subs: 'sub', tickets: 'ticket', flags: 'flag',
                     incidents: 'incident', invoices: 'invoice', payments: 'payment', audit: 'audit' };
  function openDrawerFor(entity, id) {
    var row = byId(ROWS(entity), id);
    if (!row) return;
    var d = doc.getElementById('adDrawer'), body = doc.getElementById('adDrawerBody'), foot = doc.getElementById('adDrawerFoot');
    if (!d || !body) return;
    var dk = DETAIL_KEY[entity] || entity;
    var headBadge = entity === 'flags' ? stb(row.on ? 'enabled' : 'disabled')
      : entity === 'incidents' ? (PRIO[row.severity] || stb(row.status))
      : (row.status ? stb(row.status) : stb('active'));
    body.innerHTML = '<div class="ad-sec" style="display:flex;align-items:center;gap:12px;margin-bottom:16px"><span class="ava ava' + (entity.length % 5 + 1) + '">' + esc((row.name || row.orgName || row.title || '—').charAt(0)) + '</span><div><h2 class="t-h4" style="margin:0">' + esc(row.name || row.orgName || row.title || row.id) + '</h2><div class="cell-sub">' + esc(row.id) + '</div></div>' +
      '<span style="margin-inline-start:auto">' + headBadge + '</span></div>' + (DETAILS[dk] ? DETAILS[dk](row) : '');
    body.scrollTop = 0;
    if (foot && DRAWER_FOOT[dk]) { foot.style.display = ''; foot.innerHTML = DRAWER_FOOT[dk](row); }
    else if (foot) foot.style.display = 'none';
    if (window.BV) { BV.mountIcons(body); if (foot) BV.mountIcons(foot); }
    drawerOpen();
    bindDrawerWidgets(entity, row);
  }
  function bindDrawerWidgets(entity, row) {
    /* flag rollout scale inside drawer */
    var body = doc.getElementById('adDrawerBody');
    var rscale = body ? body.querySelector('[data-rscale]') : null;
    if (rscale && entity === 'flags') {
      rscale.addEventListener('click', function (e) {
        var b = e.target.closest('[data-rp]');
        if (!b) return;
        var p = parseInt(b.dataset.rp, 10);
        if (p === row.rollout) return;
        var apply = function () {
          row.rollout = p; row.changed = 'همین حالا'; row.on = p > 0;
          toast('success', 'توزیع به‌روزرسانی شد', row.name + ' → ' + fmt(p) + '٪');
          pushAudit('تغییر توزیع Feature Flag', row.key + ' → ' + fmt(p) + '٪');
          renderFlagTable();
          openDrawerFor('flags', row.id);
        };
        if (row.env === 'production') {
          confirmAd({ title: (p > row.rollout ? 'افزایش' : 'کاهش') + ' توزیع «' + row.name + '» در تولید',
            text: 'توزیع از ' + fmt(row.rollout) + '٪ به ' + fmt(p) + '٪ می‌رسد و روی ترافیک واقعی اعمال می‌شود.', danger: true, ok: 'اعمال توزیع' }, apply);
        } else apply();
      });
    }
    var inp = doc.getElementById('adNoteInput'), send = doc.getElementById('adNoteSend'), res = doc.getElementById('adNoteResolve');
    if (send && inp) send.addEventListener('click', function () {
      var v = inp.value.trim();
      if (!v) { toast('error', 'یادداشت خالی است', 'متن یادداشت داخلی را بنویسید.'); return; }
      row.notes.push({ who: 'مریم کریمی', role: 'note', t: 'همین حالا', text: v });
      row.last = 'همین حالا';
      toast('success', 'یادداشت ثبت شد', 'یادداشت داخلی برای تیم پشتیبانی ذخیره شد.');
      pushAudit('یادداشت داخلی تیکت', row.id);
      openDrawerFor('tickets', row.id);
    });
    if (res) res.addEventListener('click', function () {
      confirmAd({ title: 'حل تیکت ' + row.id, text: 'تیکت بسته می‌شود و به کاربر اطلاع داده می‌شود. این اقدام در سابقه‌ی ممیزی ثبت می‌شود.', ok: 'حل تیکت' }, function () {
        row.status = 'resolved'; row.last = 'همین حالا'; row.notes.push({ who: 'مریم کریمی', role: 'agent', t: 'همین حالا', text: 'درخواست برطرف و تیکت بسته شد.' });
        toast('success', 'تیکت حل شد', 'کاربر از طریق ایمیل مطلع شد.');
        pushAudit('حل تیکت', row.id);
        openDrawerFor('tickets', row.id);
        var t = $('[data-ad-table="tickets"]'); if (t) renderTable('tickets');
      });
    });
    var foot = doc.getElementById('adDrawerFoot');
    if (foot) $$('[data-dact]', foot).forEach(function (b) {
      b.addEventListener('click', function () {
        var act = b.dataset.dact;
        if (act === 'suspend' || act === 'cancel') {
          confirmAd({ title: act === 'suspend' ? 'تعلیق کاربر ' + row.name : 'لغو اشتراک ' + row.orgName, text: act === 'suspend' ? 'کاربر از ورود قطع می‌شود اما داده‌هایش حفظ می‌شود.' : 'اشتراک از دوره‌ی بعد تمدید نمی‌شود و دسترسی API حفظ می‌شود.', danger: true }, function () {
            if (act === 'suspend') { row.status = 'suspended'; pushAudit('تعلیق کاربر', row.name); }
            else { row.status = 'canceled'; row.pay = 'none'; pushAudit('لغو اشتراک', row.orgName); }
            toast('success', 'انجام شد', 'تغییر با موفقیت اعمال و در سابقه ثبت شد.');
            drawerClose(); renderTable('subs'); renderTable('users');
          });
        } else if (act === 'activate') {
          row.status = 'active'; pushAudit('فعال‌سازی کاربر', row.name);
          toast('success', 'کاربر فعال شد', row.name + ' به پنل دسترسی دارد.');
          drawerClose(); renderTable('users');
        } else if (act === 'notify') {
          toast('success', 'اعلان ارسال شد', 'یک اعلان آزمایشی برای ' + row.name + ' ارسال شد.');
          pushAudit('ارسال اعلان', row.name);
        } else if (act === 'role') {
          toast('info', 'تغییر نقش', 'نقش کاربر به «اپراتور» تغییر کرد (شبیه‌سازی).');
          pushAudit('تغییر نقش', row.name);
        } else if (act === 'sessions') {
          row.sessions = 0; toast('success', 'همه‌ی نشست‌ها قطع شدند', row.name + ' باید دوباره وارد شود.');
          pushAudit('خروج از نشست‌ها', row.name);
          drawerClose();
        }
      });
    });
  }

  /* ==================================================== CONFIRM MODAL */
  function confirmAd(opt, onYes) {
    var bd = doc.getElementById('adConfirm');
    if (!bd) { onYes(); return; }
    var mt = $('[data-adc-title]', bd), mb = $('[data-adc-body]', bd), ok = $('[data-adc-ok]', bd), cancel = $('[data-adc-cancel]', bd);
    if (!mt || !mb || !ok || !cancel) return;
    mt.textContent = opt.title;
    mb.innerHTML = '<p>' + esc(opt.text) + '</p>' + (opt.typed ? '<div class="field" style="margin-top:12px"><label class="field-label">برای ادامه، عبارت «' + esc(opt.typed) + '» را تایپ کنید</label><input class="input" id="adcTypedInput" placeholder="' + esc(opt.typed) + '" autocomplete="off"></div>' : '');
    ok.textContent = opt.ok || 'تأیید';
    ok.className = 'btn ' + (opt.danger ? 'btn-danger' : 'btn-primary');
    bd.classList.add('open'); doc.body.style.overflow = 'hidden';
    var done = function () { bd.classList.remove('open'); doc.body.style.overflow = ''; ok.onclick = cancel.onclick = null; };
    var proceed = function () {
      if (opt.typed) {
        var v = ($('#adcTypedInput') || {}).value || '';
        if (v.trim() !== opt.typed) { toast('error', 'عبارت اشتباه است', 'برای ادامه باید دقیقاً «' + opt.typed + '» را تایپ کنید.'); return; }
      }
      done(); onYes();
    };
    ok.onclick = proceed;
    cancel.onclick = done;
    bd.addEventListener('click', function (e) { if (e.target === bd) done(); });
    var ti = $('#adcTypedInput');
    if (ti) {
      setTimeout(function () { ti.focus(); }, 60);
      ti.addEventListener('keydown', function (e) { if (e.key === 'Enter') { e.preventDefault(); proceed(); } });
    } else { try { ok.focus(); } catch (e) {} }
  }

  /* ==================================================== FLAGS */
  function toggleFlag(id) {
    var f = byId(A.flags, id);
    if (!f) return;
    var next = !f.on;
    if (next && f.env === 'production') {
      confirmAd({ title: 'فعال‌سازی ' + f.name + ' در تولید', text: 'این تغییر بلافاصله روی ترافیک واقعی اعمال می‌شود و در سابقه‌ی ممیزی ثبت خواهد شد.', danger: true, ok: 'فعال کن' }, function () {
        f.on = true; pushAudit('فعال‌سازی Feature Flag', f.key);
        toast('success', 'Feature Flag فعال شد', f.name + ' روی ' + (f.env === 'production' ? 'تولید' : 'آزمایش') + ' فعال است.');
        renderFlagTable();
      });
    } else if (!next && f.rollout > 0) {
      confirmAd({ title: 'غیرفعال‌سازی ' + f.name, text: 'ویژگی برای همه‌ی کاربران غیرفعال می‌شود. توزیع فعلی ' + fmt(f.rollout) + '٪ است.', danger: true }, function () {
        f.on = false; f.rollout = 0; pushAudit('غیرفعال‌سازی Feature Flag', f.key);
        toast('success', 'Feature Flag غیرفعال شد', 'توزیع به ۰٪ بازگشت.');
        renderFlagTable();
      });
    } else {
      f.on = next; toast('success', 'وضعیت تغییر کرد', f.name + ' ' + (next ? 'فعال' : 'غیرفعال') + ' شد.');
      renderFlagTable();
    }
  }
  function renderFlagTable() { var t = $('[data-ad-table="flags"]'); if (t) renderTable('flags'); }

  /* ================================================ NOTIFICATIONS */
  var N_IC = { system: 'server', security: 'shield-alert', billing: 'credit-card', operations: 'activity', support: 'life-buoy', product: 'sparkles', incident: 'siren' };
  var N_BG = { system: 'rgba(56,189,248,.1)', security: 'rgba(248,113,113,.12)', billing: 'rgba(52,211,153,.1)', operations: 'rgba(245,158,11,.12)', support: 'rgba(167,139,250,.12)', product: 'rgba(251,191,36,.1)', incident: 'rgba(248,113,113,.12)' };
  function nIc(t) { return N_IC[t] || 'bell'; }
  function nIcBg(t) { return N_BG[t] || 'rgba(255,255,255,.06)'; }
  function nIcC(t) { return { security: 'var(--red)', billing: 'var(--green)', operations: 'var(--amber)', support: 'var(--violet)', product: 'var(--amber)', system: 'var(--electric)', incident: 'var(--red)' }[t] || 'var(--text-2)'; }
  function renderNotifs() {
    var list = $('[data-ad-notif-list]');
    if (!list) return;
    var flt = T('notif').filters.type || '';
    var rows = A.notifications.filter(function (n) { return !flt || n.type === flt; });
    list.innerHTML = rows.length ? rows.map(function (n) { return CELL.notif(n); }).join('') : '<div class="empty-state" style="padding:30px">' + ic('bell-off') + '<h2 class="t-h4">اعلانی با این فیلتر وجود ندارد</h2><p>فیلتر دیگری را امتحان کنید.</p></div>';
    if (window.BV) BV.mountIcons(list);
    var unread = A.notifications.filter(function (n) { return n.unread; }).length;
    $$('[data-ad-unread]').forEach(function (el) { el.textContent = fmt(unread); });
  }

  /* ====================================================== EXPORT */
  function fakeExport(what) {
    var b = doc.activeElement;
    if (b && b.classList) b.classList.add('btn-loading');
    setTimeout(function () {
      if (b && b.classList) b.classList.remove('btn-loading');
      toast('success', 'خروجی آماده شد', what + ' در قالب CSV آماده‌ی دانلود است (نسخه‌ی نمایشی).');
    }, 900);
  }

  /* ================================================ CHARTS RANGE PILLS */
  var CHART_SETS = {
    mrr: { monthly: { labels: A.charts.mrr.labels, values: A.charts.mrr.values } }
  };
  function bindRangePills() {
    $$('[data-ranges]').forEach(function (wrap) {
      var key = wrap.dataset.ranges;
      $$('button', wrap).forEach(function (b) {
        b.addEventListener('click', function () {
          $$('button', wrap).forEach(function (x) { x.classList.remove('active'); });
          b.classList.add('active');
          var range = b.dataset.range, label = b.dataset.rangeLabel || range;
          var lbl = $('[data-range-label="' + key + '"]');
          if (lbl) lbl.textContent = label;
          switchRange(key, range);
        });
      });
    });
  }
  function switchRange(key, range) {
    var global = window['ADMIN_CHARTS_' + key.toUpperCase()];
    var sets = global || A.charts[key + '_ranges'] || CHART_SETS[key];
    var set = sets && sets[range];
    if (!set) return;
    if (window.BVCharts && BVCharts.destroyAll) {
      try { BVCharts.destroyAll(); } catch (e) {}
    }
    $$('canvas[data-chart][data-chart-holder="' + key + '"]').forEach(function (cv) {
      cv.setAttribute('data-labels', JSON.stringify(set.labels));
      cv.setAttribute('data-values', JSON.stringify(set.values || set.data));
    });
    if (window.BVCharts) { try { BVCharts.mount(); } catch (e) {} }
    var lbl = $('[data-range-label="' + key + '"]');
    if (lbl) lbl.textContent = { monthly: 'ماهانه', weekly: 'هفتگی', daily: 'روزانه' }[range] || range;
  }

  /* =============================================== PALETTE + SEARCH */
  function setupPalette() {
    var bd = doc.getElementById('adPalette');
    if (!bd) return;
    var input = doc.getElementById('adPaletteInput'), list = doc.getElementById('adPaletteList');
    var NAV = [
      { g: 'عملیات' }, { l: 'نمای کلی', h: 'index.html', ic: 'layout-dashboard', s: 'سلامت، درآمد و مصرف پلتفرم' },
      { l: 'فعالیت سیستم', h: 'activity.html', ic: 'activity', s: 'تایم‌لاین رویدادها و Incidentها' },
      { g: 'مشتریان' }, { l: 'کاربران', h: 'users.html', ic: 'users-round', s: 'مدیریت کاربران' },
      { l: 'سازمان‌ها', h: 'organizations.html', ic: 'building-2', s: 'مدیریت سازمان‌ها' },
      { l: 'اشتراک‌ها', h: 'subscriptions.html', ic: 'credit-card', s: 'اشتراک‌ها و تمدید' },
      { g: 'مالی' }, { l: 'درآمد', h: 'revenue.html', ic: 'wallet', s: 'MRR، فاکتورها و پرداخت‌ها' },
      { g: 'پلتفرم' }, { l: 'مصرف API', h: 'api.html', ic: 'server', s: 'عملکرد Endpointها و خطاها' },
      { l: 'Feature Flags', h: 'flags.html', ic: 'flag', s: 'توزیع تدریجی ویژگی‌ها' },
      { l: 'محتوای سایت', h: 'content.html', ic: 'file-text', s: 'بلاگ، مستندات و اعلان‌ها' },
      { l: 'تنظیمات سیستم', h: 'settings.html', ic: 'settings', s: 'نقش‌ها، امنیت و منطقه‌ی خطر' },
      { g: 'پشتیبانی' }, { l: 'تیکت‌ها', h: 'support.html', ic: 'life-buoy', s: 'مرکز پشتیبانی' },
      { l: 'اعلان‌ها', h: 'notifications.html', ic: 'bell', s: 'مرکز اعلان‌ها' },
      { g: 'امنیت' }, { l: 'مرکز امنیت', h: 'security.html', ic: 'shield-check', s: 'رویدادهای امنیتی' },
      { l: 'Audit Logs', h: 'security.html#audit', ic: 'scroll-text', s: 'سابقه‌ی کامل اقدامات' }
    ];
    var open = false, act = 0;
    function render(q) {
      q = (q || '').trim().toLowerCase();
      var html = '', n = 0;
      NAV.forEach(function (it) {
        if (it.g) { html += '<div class="palette-group-title">' + it.g + '</div>'; return; }
        if (q && it.l.toLowerCase().indexOf(q) === -1 && it.s.toLowerCase().indexOf(q) === -1) return;
        html += '<a href="' + it.h + '" class="palette-item"><span class="p-icon">' + ic(it.ic) + '</span><span style="flex:1;min-width:0"><b style="display:block;color:inherit">' + it.l + '</b><div class="p-sub">' + it.s + '</div></span></a>';
        n++;
      });
      if (q) {
        var hits = [];
        A.users.forEach(function (u) { if (u.name.toLowerCase().indexOf(q) !== -1 || u.email.toLowerCase().indexOf(q) !== -1) hits.push({ l: u.name, s: u.email, h: 'users.html' }); });
        A.orgs.forEach(function (o) { if (o.name.toLowerCase().indexOf(q) !== -1) hits.push({ l: o.name, s: 'سازمان · ' + o.id, h: 'organizations.html' }); });
        A.subs.forEach(function (s) { if (s.id.toLowerCase().indexOf(q) !== -1) hits.push({ l: s.id, s: 'اشتراک · ' + s.orgName, h: 'subscriptions.html' }); });
        A.tickets.forEach(function (t) { if (t.id.toLowerCase().indexOf(q) !== -1) hits.push({ l: t.id, s: 'تیکت · ' + t.subject.slice(0, 40), h: 'support.html' }); });
        hits.slice(0, 6).forEach(function (h) {
          html += '<a href="' + h.h + '" class="palette-item"><span class="p-icon" style="color:var(--amber)">' + ic('search') + '</span><span style="flex:1;min-width:0"><b style="display:block;color:inherit">' + h.l + '</b><div class="p-sub">' + h.s + '</div></span></a>';
          n++;
        });
      }
      if (!n) html = '<div class="palette-empty">' + ic('search-x') + '<div style="margin-top:10px">نتیجه‌ای برای «' + esc(q) + '» پیدا نشد.</div></div>';
      list.innerHTML = html;
      act = 0;
      $$('.palette-item', list).forEach(function (el, i) { el.classList.toggle('active', i === 0); });
    }
    function setAct(i) {
      var items = $$('.palette-item', list);
      if (!items.length) return;
      act = Math.max(0, Math.min(i, items.length - 1));
      items.forEach(function (el, x) { el.classList.toggle('active', x === act); });
      if (items[act] && items[act].scrollIntoView) { try { items[act].scrollIntoView({ block: 'nearest' }); } catch (e) {} }
    }
    function openP() { bd.classList.add('open'); doc.body.style.overflow = 'hidden'; render(''); setTimeout(function () { input.focus(); }, 50); }
    function closeP() { bd.classList.remove('open'); doc.body.style.overflow = ''; }
    $$('[data-ad-palette-open]').forEach(function (b) { b.addEventListener('click', openP); });
    bd.addEventListener('click', function (e) { if (e.target === bd) closeP(); });
    input.addEventListener('input', function () { render(input.value); });
    input.addEventListener('keydown', function (e) {
      if (e.key === 'ArrowDown') { e.preventDefault(); setAct(act + 1); }
      else if (e.key === 'ArrowUp') { e.preventDefault(); setAct(act - 1); }
      else if (e.key === 'Enter') {
        var items = $$('.palette-item', list);
        if (items[act]) window.location.href = items[act].getAttribute('href');
      }
      else if (e.key === 'Escape') closeP();
    });
    doc.addEventListener('keydown', function (e) {
      if ((e.ctrlKey || e.metaKey) && (e.key === 'k' || e.key === 'K')) { e.preventDefault(); e.stopPropagation(); bd.classList.contains('open') ? closeP() : openP(); }
    }, true);
    window.__adClosePalette = closeP;
  }
  function setupSearch() {
    var ov = doc.getElementById('adSearch');
    if (!ov) return;
    var input = doc.getElementById('adSearchInput'), res = doc.getElementById('adSearchResults'), rec = doc.getElementById('adSearchRecents'), empty = doc.getElementById('adSearchEmpty');
    var REC_KEY = 'bv-ad-recents';
    function recents() { try { return JSON.parse(localStorage.getItem(REC_KEY) || '[]'); } catch (e) { return []; } }
    function saveRecent(q) {
      var r = recents().filter(function (x) { return x !== q; }); r.unshift(q);
      try { localStorage.setItem(REC_KEY, JSON.stringify(r.slice(0, 4))); } catch (e) {}
    }
    function renderRecents() {
      var r = recents();
      rec.innerHTML = r.length ? '<div class="menu-title" style="padding:0">جستجوهای اخیر</div>' + r.slice(0, 3).map(function (q) { return '<a class="palette-item" data-q="' + esc(q) + '"><span class="p-icon">' + ic('history') + '</span><b style="color:inherit">' + esc(q) + '</b></a>'; }).join('') : '';
      if (window.BV) BV.mountIcons(rec);
      $$('[data-q]', rec).forEach(function (el) { el.addEventListener('click', function () { input.value = el.dataset.q; run(el.dataset.q); }); });
    }
    function run(q) {
      q = (q || '').trim().toLowerCase();
      var groups = [];
      function add(title, icon, items, hrefBase) {
        if (!items.length) return;
        groups.push('<div class="palette-group-title">' + title + '</div>' + items.slice(0, 4).map(function (it) {
          return '<a href="' + hrefBase + '" class="palette-item"><span class="p-icon">' + ic(icon) + '</span><span style="flex:1;min-width:0"><b style="display:block;color:inherit">' + it.t + '</b><div class="p-sub">' + it.s + '</div></span></a>';
        }).join(''));
      }
      add('کاربران', 'users-round', A.users.filter(function (u) { return u.name.toLowerCase().indexOf(q) !== -1 || u.email.toLowerCase().indexOf(q) !== -1; }).map(function (u) { return { t: u.name, s: u.email }; }), 'users.html');
      add('سازمان‌ها', 'building-2', A.orgs.filter(function (o) { return o.name.toLowerCase().indexOf(q) !== -1; }).map(function (o) { return { t: o.name, s: o.id + ' · ' + o.plan }; }), 'organizations.html');
      add('اشتراک‌ها', 'credit-card', A.subs.filter(function (s) { return s.id.toLowerCase().indexOf(q) !== -1 || s.orgName.toLowerCase().indexOf(q) !== -1; }).map(function (s) { return { t: s.orgName, s: s.id + ' · ' + s.plan }; }), 'subscriptions.html');
      add('فاکتورها', 'receipt', A.invoices.filter(function (v) { return v.id.toLowerCase().indexOf(q) !== -1 || v.orgName.toLowerCase().indexOf(q) !== -1; }).map(function (v) { return { t: v.id, s: v.orgName + ' · ' + money(v.amount) }; }), 'revenue.html');
      add('تیکت‌ها', 'life-buoy', A.tickets.filter(function (t) { return t.id.toLowerCase().indexOf(q) !== -1 || t.subject.toLowerCase().indexOf(q) !== -1; }).map(function (t) { return { t: t.id, s: t.subject }; }), 'support.html');
      add('سوابق ممیزی', 'scroll-text', A.audit.filter(function (a) { return a.action.toLowerCase().indexOf(q) !== -1 || a.target.toLowerCase().indexOf(q) !== -1; }).map(function (a) { return { t: a.action, s: a.target + ' · ' + a.id }; }), 'security.html#audit');
      var showEmpty = !groups.length;
      empty.style.display = showEmpty ? '' : 'none';
      res.innerHTML = groups.join('');
      res.style.display = showEmpty ? 'none' : '';
      rec.style.display = q ? 'none' : '';
      if (q) saveRecent(q);
      if (window.BV) BV.mountIcons(res);
    }
    function open() { ov.classList.add('open'); doc.body.style.overflow = 'hidden'; renderRecents(); res.innerHTML = ''; res.style.display = ''; empty.style.display = 'none'; setTimeout(function () { input.focus(); }, 50); }
    function close() { ov.classList.remove('open'); doc.body.style.overflow = ''; }
    $$('[data-ad-search-open]').forEach(function (b) { b.addEventListener('click', open); });
    ov.addEventListener('click', function (e) { if (e.target === ov) close(); });
    input.addEventListener('input', function () { run(input.value); });
    input.addEventListener('keydown', function (e) { if (e.key === 'Escape') close(); });
    doc.addEventListener('keydown', function (e) {
      if ((e.ctrlKey || e.metaKey) && e.key === '/') { e.preventDefault(); e.stopPropagation(); ov.classList.contains('open') ? close() : open(); }
    }, true);
    window.__adCloseSearch = close;
  }

  /* =================================================== PAGE TABS */
  function setupTabs() {
    $$('.a-tabs[data-atabs]').forEach(function (wrap) {
      wrap.addEventListener('click', function (e) {
        var b = e.target.closest('button[data-atab]');
        if (!b) return;
        var grp = wrap.dataset.atabs;
        $$('button[data-atab]', wrap).forEach(function (x) { x.classList.toggle('active', x === b); });
        $$('[data-apanel]').forEach(function (p) { p.classList.toggle('active', p.dataset.apanel === grp && p.dataset.atab === b.dataset.atab); });
      });
    });
    /* deep links: security.html#audit, settings.html#settings-profile */
    if (window.location.hash) {
      var h = window.location.hash.slice(1);
      var els = $$('[data-atab="' + h + '"]');
      if (els.length) {
        els.forEach(function (b) { b.click(); });
      } else {
        var panel = doc.getElementById(h);
        if (panel && panel.dataset.atab) {
          $$('.a-tabs button[data-atab]').forEach(function (b) {
            b.classList.toggle('active', b.dataset.atab === panel.dataset.atab);
          });
          $$('[data-apanel]').forEach(function (p) {
            p.classList.toggle('active', p === panel);
          });
        }
      }
    }
  }

  /* ==================================================== SETTINGS/ROLES */
  function setupSettings() {
    $$('[data-dg]').forEach(function (b) {
      b.addEventListener('click', function () {
        confirmAd({ title: b.dataset.dgTitle, text: b.dataset.dgText, danger: true, typed: b.dataset.dgTyped || null, ok: b.dataset.dgOk || 'تأیید' }, function () {
          toast('success', b.dataset.dgOk || 'انجام شد', 'عملیات حساس با موفقیت شبیه‌سازی و در Audit ثبت شد.');
          pushAudit(b.dataset.dgTitle, 'تنظیمات سیستم');
        });
      });
    });
    /* setting selects: changing a value gives the same feedback as toggles */
    $$('.set-card select').forEach(function (sel) {
      sel.addEventListener('change', function () {
        var row = sel.closest('.set-row');
        var label = row ? row.querySelector('span').textContent.trim() : 'تنظیم';
        toast('info', 'تنظیم ذخیره شد', '«' + label + '» به «' + sel.value + '» تغییر کرد.');
        pushAudit('تغییر تنظیم', label);
      });
    });
    $$('[data-role-toggle]').forEach(function (el) {
      /* buttons = actions (need confirm); span switches = toggle on click,
         keyboard included (role="switch" with tabindex) */
      if (el.tagName === 'BUTTON') {
        el.addEventListener('click', function () {
          confirmAd({ title: 'تکثیر نقش «پشتیبانی»', text: 'نقش تکراری با همان مجوزها ساخته می‌شود (شبیه‌سازی).', ok: 'تکثیر نقش' }, function () {
            toast('success', 'نقش تکثیر شد', 'نقش «پشتیبانی (کپی)» با ۸ مجوز ساخته شد.');
            pushAudit('تکثیر نقش', 'پشتیبانی');
          });
        });
        return;
      }
      var toggle = function () {
        var on = el.classList.toggle('on');
        el.setAttribute('aria-checked', on ? 'true' : 'false');
        var row = el.closest('.set-row');
        var label = row ? row.querySelector('span').textContent.trim() : 'تنظیم';
        toast('info', 'تنظیم به‌روزرسانی شد', '«' + label + '» ' + (on ? 'فعال' : 'غیرفعال') + ' شد.');
        pushAudit('تغییر تنظیم', label);
      };
      el.addEventListener('click', toggle);
      el.addEventListener('keydown', function (e) {
        if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); toggle(); }
      });
    });
  }

  /* =============================================== INIT */
  function init() {
    $$('[data-ad-table]').forEach(function (t) { bindTable(t.dataset.adTable); });
    var nb = doc.getElementById('adDrawerClose');
    if (nb) nb.addEventListener('click', drawerClose);
    var bd = doc.getElementById('adDrBack');
    if (bd) bd.addEventListener('click', drawerClose);
    var bx = doc.getElementById('adConfirmClose');
    if (bx) bx.addEventListener('click', function () { doc.getElementById('adConfirm').classList.remove('open'); doc.body.style.overflow = ''; });
    setupPalette(); setupSearch(); setupTabs(); bindRangePills(); setupSettings();
    var nl = doc.getElementById('adNotifList');
    if (nl && A.notifications) {
      renderNotifs();
      nl.addEventListener('click', function (e) {
        var it = e.target.closest('[data-notif]');
        if (!it) return;
        var n = byId(A.notifications, it.dataset.notif);
        if (n) { n.unread = false; renderNotifs(); toast('info', 'اعلان خوانده شد', n.title); }
      });
      $$('[data-ad-notif-all]').forEach(function (b) {
        b.addEventListener('click', function () {
          A.notifications.forEach(function (n) { n.unread = false; });
          renderNotifs();
          toast('success', 'همه خوانده شد', 'همه‌ی اعلان‌ها به‌عنوان خوانده علامت خوردند.');
        });
      });
      $$('[data-ad-notif-filter]').forEach(function (b) {
        b.addEventListener('click', function () {
          $$('[data-ad-notif-filter]').forEach(function (x) { x.classList.toggle('active', x === b); });
          var v = b.getAttribute('data-ad-notif-filter');
          T('notif').filters.type = v === 'all' ? '' : v;
          renderNotifs();
        });
      });
    }
    var tcount = $('[data-ad-ticket-urgent]');
    if (tcount) tcount.textContent = fmt(A.tickets.filter(function (t) { return t.status === 'urgent'; }).length);
    var tcount2 = $('[data-ad-ticket-open]');
    if (tcount2) tcount2.textContent = fmt(A.tickets.filter(function (t) { return t.status === 'open' || t.status === 'urgent' || t.status === 'wait_support'; }).length);
    $$('[data-ad-export]').forEach(function (b) { b.addEventListener('click', function () { fakeExport(b.dataset.adExport); }); });
    $$('[data-ad-count="users"]').forEach(function (el) {
      var v = el.dataset.countKey;
      el.textContent = fmt(v === 'active' ? A.users.filter(function (u) { return u.status === 'active'; }).length : v === 'suspended' ? A.users.filter(function (u) { return u.status === 'suspended'; }).length : A.users.length);
    });
    var envSel = $$('[data-env-opt]');
    envSel.forEach(function (b) {
      b.addEventListener('click', function () {
        var env = b.dataset.envOpt;
        $$('.env-chip').forEach(function (c) {
          c.classList.remove('env-staging', 'env-dev');
          if (env !== 'production') c.classList.add('env-' + env);
          var name = $('[data-env-name]', c);
          if (name) name.textContent = env === 'production' ? 'Production' : env === 'staging' ? 'Staging' : 'Development';
        });
        toast('info', 'محیط نمایش عوض شد', 'نشانگر محیط به ' + (env === 'production' ? 'تولید' : env === 'staging' ? 'آزمایش' : 'توسعه') + ' تغییر کرد.');
        pushAudit('تغییر محیط', 'نشانگر محیط ' + env);
      });
    });
    var closeSide = $('[data-side-open-close]');
    if (closeSide) closeSide.addEventListener('click', function () {
      var s = doc.getElementById('dashSide');
      if (s) s.classList.remove('open');
      var sb = doc.getElementById('sideBackdrop');
      if (sb) sb.classList.remove('show');
    });
    /* bulk actions (users) */
    doc.addEventListener('click', function (e) {
      var b = e.target.closest('[data-bulk-action]');
      if (!b) return;
      var entity = 'users';
      var ids = Object.keys(T(entity).sel);
      if (!ids.length) { toast('error', 'ردیفی انتخاب نشده', 'ابتدا یک یا چند کاربر را انتخاب کنید.'); return; }
      var rows = A.users.filter(function (u) { return ids.indexOf(u.id) !== -1; });
      var act = b.dataset.bulkAction;
      if (act === 'export') { fakeExport('خروجی کاربران (' + fmt(rows.length) + ' ردیف)'); return; }
      if (act === 'notify') {
        toast('success', 'اعلان گروهی ارسال شد', 'برای ' + fmt(rows.length) + ' کاربر ارسال شد.');
        pushAudit('ارسال اعلان گروهی', fmt(rows.length) + ' کاربر');
        return;
      }
      if (act === 'plan') {
        confirmAd({ title: 'تغییر پلن ' + fmt(rows.length) + ' کاربر', text: 'پلن کاربران انتخاب‌شده به «رشد» تغییر می‌کند (شبیه‌سازی).', ok: 'تغییر پلن' }, function () {
          toast('success', 'پلن تغییر کرد', fmt(rows.length) + ' کاربر به پلن رشد منتقل شدند.');
          pushAudit('تغییر پلن گروهی', fmt(rows.length) + ' کاربر');
          T(entity).sel = {}; updateBulk(entity); renderTable(entity);
        });
        return;
      }
      var verb = act === 'suspend' ? 'تعلیق' : 'فعال‌سازی';
      confirmAd({ title: verb + ' ' + fmt(rows.length) + ' کاربر', text: act === 'suspend' ? 'کاربران از ورود به پنل قطع می‌شوند؛ داده‌هایشان حفظ می‌شود.' : 'کاربران دوباره به پنل دسترسی پیدا می‌کنند.', danger: act === 'suspend', ok: verb }, function () {
        rows.forEach(function (u) { u.status = act === 'suspend' ? 'suspended' : 'active'; });
        toast('success', verb + ' انجام شد', fmt(rows.length) + ' کاربر به‌روزرسانی شدند.');
        pushAudit(verb + ' گروهی کاربران', fmt(rows.length) + ' کاربر');
        T(entity).sel = {}; updateBulk(entity); renderTable(entity);
      });
    });
  }
  if (doc.readyState === 'loading') doc.addEventListener('DOMContentLoaded', init); else init();
})();
