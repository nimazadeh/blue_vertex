# -*- coding: utf-8 -*-
"""Blue Vertex — Layer 4: Admin Console (persian-first SaaS operations).
Builds admin/*.html pages on the same design system; data lives in
assets/js/admin-data.js and interactions in assets/js/admin.js."""

import json

from chrome import head, scripts

IC = lambda n: '<i data-icon="%s"></i>' % n

NAV = [
    ('عملیات', [
        ('نمای کلی', 'index.html', 'layout-dashboard', ''),
        ('فعالیت سیستم', 'activity.html', 'activity', ''),
        ('Incidentها', 'activity.html#incidents', 'siren', ''),
    ]),
    ('مشتریان', [
        ('کاربران', 'users.html', 'users-round', ''),
        ('سازمان‌ها', 'organizations.html', 'building-2', ''),
        ('اشتراک‌ها', 'subscriptions.html', 'credit-card', ''),
    ]),
    ('مالی', [
        ('درآمد', 'revenue.html', 'wallet', ''),
    ]),
    ('پلتفرم', [
        ('مصرف API', 'api.html', 'server', ''),
        ('Feature Flags', 'flags.html', 'flag', ''),
        ('محتوا', 'content.html', 'file-text', ''),
        ('تنظیمات سیستم', 'settings.html', 'settings', ''),
    ]),
    ('پشتیبانی', [
        ('تیکت‌ها', 'support.html', 'life-buoy', '۱'),
        ('اعلان‌ها', 'notifications.html', 'bell', ''),
    ]),
    ('امنیت', [
        ('مرکز امنیت و Audit', 'security.html', 'shield-check', ''),
    ]),
]

def _sidebar(active):
    nav = ''
    for group, items in NAV:
        nav += '<div class="side-section-title">%s</div>' % group
        for label, href, icon, badge in items:
            act = ' active' if active == href else ''
            cur = ' aria-current="page"' if active == href else ''
            b = '<span class="side-badge blue">%s</span>' % badge if badge else ''
            nav += '<a class="side-link%s" href="%s"%s>%s<span>%s</span>%s</a>' % (act, href, cur, IC(icon), label, b)
    return f'''<aside class="dash-side" id="dashSide">
  <div class="side-brand">
    <a class="brand" href="index.html"><span class="brand-mark">{IC('shield')}</span><span class="brand-name">بلو ورتکس<small>ADMIN CONSOLE</small></span></a>
    <button class="topbar-btn" style="margin-inline-start:auto" data-side-open-close aria-label="بستن منو"><i data-icon="x"></i></button>
  </div>
  <nav class="side-nav" aria-label="منوی مدیریت">''' + nav + '''</nav>
  <div class="side-foot" style="margin-top:auto">
    <div class="side-upgrade">
      <b><i data-icon="activity"></i> وضعیت سرویس</b>
      <p>همه سرویس‌ها پایدارند — آپ‌تایم ۳۰ روز: <b class="fa-num">۹۹٫۹۸٪</b></p>
      <div class="progress green"><i style="width:99.98%"></i></div>
      <div class="flex gap-8 mt-8">
        <a class="btn btn-ghost btn-sm btn-block" href="../status/index.html">صفحه وضعیت</a>
        <button class="btn btn-secondary btn-sm btn-block" data-ad-palette-open>⌘K فرمان</button>
      </div>
    </div>
  </div>
</aside>
<div class="side-backdrop" id="sideBackdrop"></div>'''

def _topbar(crumb, extra=''):
    return f'''<header class="dash-topbar">
  <button class="topbar-btn side-toggle" data-side-open aria-label="باز کردن منو"><i data-icon="panel-right"></i></button>
  <div class="topbar-breadcrumb">
    <span>پلتفرم بلو ورتکس</span><span class="sep"><i data-icon="chevron-left"></i></span><b>{crumb}</b>
  </div>
  <div style="flex:1"></div>
  <button class="topbar-btn theme-toggle" data-theme-toggle aria-label="تغییر حالت نمایش" title="حالت روشن"><i data-icon="sun"></i></button>
  <div class="dropdown" data-dd>
    <button class="env-chip" data-dd-toggle aria-haspopup="true" aria-label="محیط نمایش — تغییر محیط">
      <span class="env-dot"></span>محیط: <b data-env-name>Production</b>
      <i data-icon="chevron-down" style="width:12px;height:12px"></i>
    </button>
    <div class="dropdown-menu" style="min-width:210px">
      <div class="menu-title">محیط نمایش</div>
      <button class="menu-item" data-env-opt="production"><span class="env-dot" style="background:#FBBF24;box-shadow:0 0 8px #FBBF24"></span>Production<span class="badge badge-amber" style="margin-inline-start:auto">فعال</span></button>
      <button class="menu-item" data-env-opt="staging"><span class="env-dot" style="background:#A78BFA;box-shadow:0 0 8px #A78BFA"></span>Staging</button>
      <button class="menu-item" data-env-opt="dev"><span class="env-dot" style="background:#38BDF8;box-shadow:0 0 8px #38BDF8"></span>Development</button>
    </div>
  </div>
  <button class="topbar-search" data-ad-search-open aria-label="جستجوی سراسری">
    {IC('search')}<span>جستجوی کاربر، سازمان، تراکنش…</span><span class="kbd">Ctrl /</span>
  </button>
  <div class="dropdown" data-dd>
    <button class="topbar-btn" data-dd-toggle aria-label="اعلان‌ها"><i data-icon="bell"></i><span class="notif-dot"></span></button>
    <div class="dropdown-menu" style="width:330px">
      <div class="menu-title">اعلان‌ها <span class="badge badge-blue" data-ad-unread>۳</span></div>
      <a class="menu-item ma-top" href="notifications.html"><span style="flex:1;min-width:0"><b style="color:var(--text-1);font-size:var(--fs-caption)">۳ اعلان جدید</b><span style="display:block;font-size:.66rem;color:var(--text-4)">مشاهده همه اعلان‌ها</span></span><i data-icon="arrow-left"></i></a>
      <div class="menu-sep"></div>
      <a class="menu-item" href="revenue.html"><i data-icon="credit-card" style="color:var(--red)"></i>پرداخت ناموفق سازمان رایانش</a>
      <a class="menu-item" href="security.html"><i data-icon="shield-alert" style="color:var(--amber)"></i>۳ تلاش ورود ناموفق مسدود شد</a>
      <a class="menu-item" href="activity.html"><i data-icon="activity" style="color:var(--amber)"></i>کندی صف گزارش‌گیری</a>
    </div>
  </div>
  <div class="dropdown" data-dd>
    <button class="topbar-user" data-dd-toggle aria-label="پروفایل ادمین">
      <span class="avatar avatar-sm" style="background:linear-gradient(135deg,#A78BFA,#6D28D9)">م</span>
      <span class="u-info"><span class="u-name">مریم کریمی</span><span class="u-mail">admin@bluevertex.ir</span></span>
      <i data-icon="chevron-down" class="chev"></i>
    </button>
    <div class="dropdown-menu">
      <div class="menu-title">admin@bluevertex.ir</div>
      <span class="role-chip" data-role="super" style="margin:0 10px 8px">Super Admin</span>
      <a class="menu-item" href="settings.html#settings-profile"><i data-icon="user-round"></i>پروفایل و نشست‌ها</a>
      <a class="menu-item" href="settings.html"><i data-icon="settings"></i>تنظیمات سیستم</a>
      <div class="menu-sep"></div>
      <a class="menu-item" href="../index.html"><i data-icon="external-link"></i>مشاهده سایت</a>
      <a class="menu-item" href="../dashboard/index.html"><i data-icon="layout-dashboard"></i>کنسول توسعه‌دهنده</a>
      <a class="menu-item" href="../auth/login.html"><i data-icon="log-out"></i>خروج</a>
    </div>
  </div>
</header>'''

CHROME_END = '''<div class="palette-backdrop" id="adPalette" role="dialog" aria-modal="true" aria-label="فرمان‌های ادمین">
  <div class="palette">
    <div class="palette-input-wrap">
      <span data-icon="command" style="display:flex"></span>
      <input id="adPaletteInput" class="palette-input" placeholder="فرمان یا جستجوی سریع…" aria-label="فرمان سریع">
      <button class="topbar-btn" data-ad-palette-close style="display:none" aria-label="بستن"><i data-icon="x"></i></button>
      <span class="kbd">ESC</span>
    </div>
    <div class="palette-list" id="adPaletteList"></div>
    <div class="palette-foot"><span><span class="kbd">↑</span><span class="kbd">↓</span> حرکت</span><span><span class="kbd">↵</span> انتخاب</span><span style="margin-inline-start:auto;font-weight:700;color:var(--text-4)">Admin Console</span></div>
  </div>
</div>
<div class="search-view" id="adSearch" role="dialog" aria-modal="true" aria-label="جستجوی سراسری ادمین">
  <div class="search-panel">
    <div class="search-header"><span style="display:flex;color:var(--text-3)" data-icon="search"></span>
      <input id="adSearchInput" placeholder="جستجوی کاربر، سازمان، اشتراک، فاکتور، تیکت، Audit…" aria-label="جستجوی سراسری"><span class="kbd">ESC</span></div>
    <div class="search-recents" id="adSearchRecents" style="padding:12px 18px"></div>
    <div class="search-results" id="adSearchResults" style="padding:6px 18px 16px"></div>
    <div id="adSearchEmpty" style="display:none"><div class="search-empty"><span style="display:inline-flex" data-icon="search-x"></span><p>نتیجه‌ای پیدا نشد. عبارت دیگری را امتحان کنید.</p></div></div>
    <div class="search-foot"><span>جستجو در داده‌های نمایشی ادمین</span></div>
  </div>
</div>
<div class="modal-backdrop" id="adConfirm" role="dialog" aria-modal="true" aria-label="تأیید عملیات">
  <div class="modal modal-sm">
    <div class="modal-head"><div><h2 data-adc-title>تأیید عملیات</h2></div>
      <button class="modal-close" id="adConfirmClose" aria-label="بستن"><i data-icon="x"></i></button></div>
    <div class="modal-body" data-adc-body></div>
    <div class="modal-foot"><button class="btn btn-ghost" data-adc-cancel>انصراف</button><button class="btn btn-primary" data-adc-ok>تأیید</button></div>
  </div>
</div>
<div class="drawer-backdrop" id="adDrBack"></div>
<aside class="drawer ad-drawer" id="adDrawer" role="dialog" aria-modal="true" aria-label="جزئیات">
  <div class="drawer-head">
    <div class="flex gap-8"><h2 class="t-h4">جزئیات</h2></div>
    <button class="modal-close" id="adDrawerClose" aria-label="بستن"><i data-icon="x"></i></button>
  </div>
  <div class="drawer-body" id="adDrawerBody"></div>
  <div class="drawer-foot" id="adDrawerFoot" style="display:none"></div>
</aside>'''

def admin_page(crumb, active, title, subtitle, content, actions='', charts=False, extra_scripts='', page_title=None):
    pt = page_title or (title + ' | پنل مدیریت بلو ورتکس')
    pd = 'پنل مدیریت بلو ورتکس — ' + title
    html = head(pt, pd, '../', extra_css='<link rel="stylesheet" href="../assets/css/admin.css">')
    return html + f'''<body class="noise admin">
<div class="dash-shell">
''' + _sidebar(active) + _topbar(crumb) + f'''
  <main class="dash-main">
    <div class="dash-content">
      <div class="dash-head">
        <div><h1 style="margin:0">{title}</h1><p class="greet-sub" style="margin:0;margin-top:4px">{subtitle}</p></div>
        <div class="dash-actions">{actions}</div>
      </div>
      {content}
    </div>
  </main>
</div>
''' + CHROME_END + f'''<div class="toast-region" id="toastRegion"></div>
{scripts('../', charts=charts)}
<script src="../assets/js/admin-data.js"></script>
<script src="../assets/js/admin.js"></script>
{extra_scripts}
</body></html>'''

# ---------------------------------------------------------------- helpers --
def kpi(label, value, sub='', delta=None, icon='activity', accent=False):
    d = ''
    if delta:
        cls = 'up' if delta[0] == 'up' else ('down' if delta[0] == 'down' else 'mid')
        arrow = {'up': 'arrow-up-right', 'down': 'arrow-down-left', 'mid': 'minus'}[delta[0]]
        d = '<span class="kpi-delta %s">%s %s</span>' % (cls, IC(arrow), delta[1])
    return '''<div class="kpi-card%s">
      <div class="kpi-top">%s<span>%s</span></div>
      <div class="kpi-num">%s</div>
      <div class="kpi-sub">%s</div>%s</div>''' % (' accent' if accent else '', IC(icon), label, value, sub, d)

def chart_card(title, sub, canvas, legend='', height=0, extra=''):
    h = ' style="height:%spx"' % height if height else ''
    return f'''<div class="chart-card">
  <div class="chart-card-head"><div><h2>{title}</h2><p>{sub}</p></div>{extra}</div>
  <div class="chart-holder"{h}>{canvas}</div>
  {legend}
</div>'''

def table_card(title, sub, entity, cols, toolbar='', selectable=False, wrap_id=None):
    th = ''
    if selectable:
        th += '<th scope="col" style="width:30px"><input type="checkbox" class="ck ck-all" aria-label="انتخاب همه"></th>'
    th += ''.join(f'<th scope="col"{" class=\"sortable\" data-sort=\"" + c["sort"] + "\"" if c.get("sort") else ""}>{c["label"]}<span class="dir"></span></th>' for c in cols)
    tbody = ''
    return f'''<div class="chart-card" style="padding:0;overflow:hidden">
  <div class="chart-card-head" style="padding:18px 22px 0;margin-bottom:10px">
    <div><h2>{title}</h2><p>{sub}</p></div>
    <div class="flex gap-8">{toolbar}</div>
  </div>
  <div class="table-wrap ad-table-wrap" style="border:none;border-radius:0">
    <table class="ad-table" data-ad-table="{entity}" aria-label="{title}">
      <thead><tr>{th}</tr></thead>
      <tbody>{tbody}</tbody>
    </table>
  </div>
  <div class="pager" style="padding:12px 20px 16px" data-ad-pager="{entity}">
    <span class="p-msg" data-ad-pmsg="{entity}"></span>
  </div>
</div>'''

def search_in(entity, ph):
    return f'''<div class="search-input" style="position:relative;min-width:230px"><span style="position:absolute;inset-inline-start:11px;top:50%;transform:translateY(-50%);display:flex;color:var(--text-4)" data-icon="search"></span><input class="input" data-ad-search="{entity}" placeholder="{ph}" style="padding-inline-start:34px;min-width:230px" aria-label="جستجو"></div>'''

def filt(entity, field, options, label):
    opts = ''.join(f'<option value="{v}">{l}</option>' for v, l in options)
    return f'<select class="select" data-ad-filter="{entity}" data-field="{field}" aria-label="{label}"><option value="">{label}: همه</option>{opts}</select>'

def export_btn(entity, label):
    return '<button class="btn btn-secondary btn-sm" data-ad-export="%s"><i data-icon="download"></i> %s</button>' % (label, label)

def tabs(grp, items):
    btns = ''.join('<button data-atab="%s" class="%s">%s%s</button>' % (k, 'active' if i == 0 else '', l, (c and '<span class="t-count">%s</span>' % c or '')) for i, (k, l, c) in enumerate(items))
    return '<div class="a-tabs" data-atabs="%s" role="tablist">%s</div>' % (grp, btns), grp

def panel(grp, key, html):
    return '<div class="a-panel%s" data-apanel="%s" data-atab="%s">%s</div>' % (' active' if key == 'admin' else '', grp, key, html)

def note(html, icon='info'):
    return '<div class="ad-note">%s<span>%s</span></div>' % (IC(icon), html)

def js(*codes):
    return '<script>%s</script>' % ';'.join(codes)

def J(o):
    return json.dumps(o, ensure_ascii=False)

def canvas(type_, labels, values, colors, unit='', name='', fill=False, stacked=False, holder_key=None):
    attrs = 'data-chart data-chart-type="%s" data-labels=\'%s\' data-values=\'%s\' data-colors=\'%s\'' % (
        type_, J(labels), J(values), J(colors))
    if unit: attrs += ' data-unit="%s"' % unit
    if name: attrs += ' data-name="%s"' % name
    if fill: attrs += ' data-fill="1"'
    if stacked: attrs += ' data-stacked="1"'
    if holder_key: attrs += ' data-chart-holder="%s"' % holder_key
    return '<canvas %s></canvas>' % attrs

def legend(items):
    return '<div class="chart-legend">%s</div>' % ''.join('<span><i style="background:%s"></i> %s</span>' % (c, l) for c, l in items)

def fa(n):
    return f'{n:,}'.translate(str.maketrans('0123456789', '۰۱۲۳۴۵۶۷۸۹')).replace(',', '٬')

def dist_card(vals, labels, display, colors, center_main, center_sub, seg_aria, foot_left, foot_right, cy, cx=70, r=54):
    """Donut + legend rows with mini bars + segmented bar + footer — the same
    component as the dashboard 'توزیع وضعیت' / analytics 'خطاها بر اساس کد' card."""
    total = sum(vals)
    pcts = [round(v * 1000 / total) / 10 for v in vals]
    pcts[-1] = round(100 - sum(pcts[:-1]), 1)
    circles = ''
    off = 0.0
    for p, c in zip(pcts, colors):
        circles += ('<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{c}" stroke-width="16" '
                    'pathLength="100" stroke-dasharray="{p} 100" stroke-dashoffset="{o}"/>').format(
            cx=cx, cy=cy, r=r, c=c, p=p, o=-off)
        off += p
    def pct(p): return ('%g' % p)
    pfa = lambda s: s.translate(str.maketrans('0123456789', '۰۱۲۳۴۵۶۷۸۹')).replace('.', '٫')
    seg = ''.join('<i style="width:%s%%;background:%s"></i>' % (pct(p), c) for p, c in zip(pcts, colors))
    legend_rows = ''
    for val, label, p, c in zip(display, labels, pcts, colors):
        legend_rows += f'''<div class="st-row">
              <div class="st-row-head">
                <span class="st-dot" style="background:{c}"></span>
                <span class="t-caption">{label}</span>
                <b class="t-sm fa-num">{val}</b>
                <span class="fa-num">{pfa(pct(p))}٪</span>
              </div>
              <div class="st-track"><i style="width:{pct(p)}%;background:{c}"></i></div>
            </div>'''
    return f'''<div class="status-dist">
          <div class="status-donut">
            <svg viewBox="0 0 140 140" role="img" aria-label="{seg_aria}">
              <circle cx="{cx}" cy="{cy}" r="{r}" fill="none" style="stroke:var(--track)" stroke-width="16"/>
              <g transform="rotate(-90 {cx} {cy})">{circles}</g>
              <text x="{cx}" y="{cy - 4}" text-anchor="middle" class="status-donut-main">{center_main}</text>
              <text x="{cx}" y="{cy + 16}" text-anchor="middle" class="status-donut-sub">{center_sub}</text>
            </svg>
          </div>
          <div class="status-legend">{legend_rows}</div>
        </div>
        <div class="status-seg" role="img" aria-label="{seg_aria}">{seg}</div>
        <div class="flex-between status-foot">
          <span class="t-caption">{foot_left}</span>
          <b class="t-sm fa-num">{foot_right}</b>
        </div>'''

def risk_chip(r):
    return ''

# ================================================================ PAGES ====
def build_index(prefix=''):
    content = ''
    content += '''<div class="kpi-grid">'''
    content += kpi('کاربران فعال', '۴۶۲', 'از ۵۷۱ کاربر ثبت‌نامی', ('up', '۲٫۱٪'), 'users-round')
    content += kpi('سازمان‌های فعال', '۷', 'از ۸ سازمان', ('up', '+۱'), 'building-2')
    content += kpi('درآمد ماهانه', '۲۰۷<small>میلیون تومان</small>', 'شهریور ۱۴۰۵', ('up', '۵٫۶٪'), 'wallet', True)
    content += kpi('درآمد تکرارشونده', '۱۹۸<small>میلیون تومان</small>', '۹۶٪ از کل درآمد', ('up', '۴٫۲٪'), 'repeat')
    content += kpi('درخواست‌های API', '۳۲٫۴<small>میلیون</small>', '۳۰ روز اخیر', ('up', '۱۲٪'), 'server')
    content += kpi('نرخ موفقیت API', '۹۹٫۸۲٪', 'میانگین ۳۰ روز', ('mid', 'پایدار'), 'check-circle-2')
    content += kpi('خطاهای ۲۴ ساعت اخیر', '۴٬۸۱۰', '۲٪ بیشتر از میانگین', ('down', '۱۲٪'), 'alert-triangle')
    content += kpi('وضعیت سرویس', 'پایدار', 'آپ‌تایم ۳۰ روز: ۹۹٫۹۸٪', ('up', 'همه سرویس‌ها'), 'activity')
    content += '</div>'

    content += '''<div class="dash-grid-2e">
      <div class="chart-card">
        <div class="chart-card-head"><div><h2>روند درآمد تکرارشونده (MRR)</h2><p>۱۲ ماه اخیر — میلیون تومان</p></div>
          <a class="link" style="font-size:var(--fs-caption)" href="revenue.html">گزارش کامل <i data-icon="arrow-left"></i></a></div>
        <div class="chart-holder" style="height:240px">''' + canvas('line', ['مهر', 'آبان', 'آذر', 'دی', 'بهمن', 'اسفند', 'فروردین', 'اردیبهشت', 'خرداد', 'تیر', 'مرداد', 'شهریور'], [112, 118, 124, 131, 139, 146, 158, 165, 172, 184, 196, 207], ['rgb(56,189,248)'], 'میلیون تومان', 'MRR', fill=True) + '''</div>
      </div>
      <div class="chart-card">
        <div class="chart-card-head"><div><h2>رشد کاربران</h2><p>ثبت‌نام جدید و کاربر فعال</p></div></div>
        <div class="chart-holder" style="height:240px">''' + canvas('bar', ['مهر', 'آبان', 'آذر', 'دی', 'بهمن', 'اسفند', 'فروردین', 'اردیبهشت', 'خرداد', 'تیر', 'مرداد', 'شهریور'], [[42, 38, 51, 47, 63, 58, 74, 82, 96, 108, 121, 134], [310, 322, 340, 351, 372, 386, 402, 415, 431, 446, 458, 462]], ['rgb(59,130,246)', 'rgb(56,189,248)'], 'کاربر', 'ثبت‌نام') + legend([('#3B82F6', 'ثبت‌نام جدید'), ('#38BDF8', 'کاربر فعال')]) + '''</div>
      </div>
    </div>'''

    content += '''<div class="dash-grid-2">
      <div class="chart-card">
        <div class="chart-card-head"><div><h2>سلامت سرویس‌ها</h2><p>۷ روز اخیر — ۸ سرویس حیاتی</p></div>
          <a class="link" style="font-size:var(--fs-caption)" href="../status/index.html">صفحه وضعیت <i data-icon="arrow-left"></i></a></div>
        <div class="health-grid">'''
    health = [('API Gateway', 'ok', '۹۹٫۹۸٪ · ۱۲ میلیون درخواست', 'server'), ('پایگاه داده', 'ok', '۹۹٫۹۹٪ · تأخیر ۸ms', 'database'), ('احراز هویت', 'ok', '۹۹٫۹۹٪', 'key-round'), ('داشبورد', 'ok', '۹۹٫۹۷٪', 'layout-dashboard'), ('Webhook', 'deg', '۹۹٫۹۱٪ · تأخیر صف', 'webhook'), ('مستندات', 'ok', '۱۰۰٪', 'book-open'), ('ذخیره‌سازی', 'ok', '۹۹٫۹۸٪ · ۴۶GB', 'hard-drive'), ('صف پردازش', 'deg', '۹۹٫۸۵٪ · Incident فعال', 'list-ordered')]
    hm = {'ok': ('عملکرد عادی', 'ok'), 'deg': ('اختلال جزئی', 'deg'), 'maj': ('اختلال عمده', 'maj')}
    for name, st, meta, icon in health:
        txt, cls = hm[st]
        content += f'''<div class="health-card">
          <div class="h-name">{IC(icon)}<span>{name}</span></div>
          <div class="h-nums"><span class="h-status {cls}"><i></i>{txt}</span></div>
          <div class="h-nums"><span>{meta}</span></div>
        </div>'''
    content += '''</div></div>
      <div>
        <div class="chart-card" style="margin-bottom:14px">
          <div class="chart-card-head"><div><h2>نیاز به توجه</h2><p>اولویت‌های عملیاتی امروز</p></div></div>
          <div class="alert-item crit"><span class="a-ic">''' + IC('credit-card') + '''</span><div><b>پرداخت ناموفق سازمان رایانش</b><p>فاکتور ۳٬۴۹۰٬۰۰۰ تومانی در وضعیت ناموفق — ۳ تلاش انجام شد.</p></div><span class="a-when">۰۸:۴۱</span></div>
          <div class="alert-item warn"><span class="a-ic">''' + IC('shield-alert') + '''</span><div><b>۳ تلاش ورود ناموفق از IP خارجی</b><p>آدرس 45.155.204.11 مسدود شد؛ نشست مشکوک کاربر حسین نادری قطع شد.</p></div><span class="a-when">۰۳:۱۲</span></div>
          <div class="alert-item warn"><span class="a-ic">''' + IC('activity') + '''</span><div><b>کندی صف گزارش‌گیری</b><p>تأخیر پردازش از ۹۰ ثانیه عبور کرد — تیم زیرساخت فعال است.</p></div><span class="a-when">۱۰:۴۰</span></div>
          <div class="alert-item info"><span class="a-ic">''' + IC('life-buoy') + '''</span><div><b>تیکت فوری TKT-۱۰۴۲</b><p>شبکه‌نو: خطای 429 در پردازش دسته‌ای — در انتظار پاسخ.</p></div><span class="a-when">۱۴:۲۱</span></div>
          <div style="display:flex;gap:8px;margin-top:12px">
            <a class="btn btn-secondary btn-sm" href="revenue.html#payments">بررسی پرداخت‌ها</a>
            <a class="btn btn-secondary btn-sm" href="support.html">مرکز پشتیبانی</a>
          </div>
        </div>
        <div class="chart-card">
          <div class="chart-card-head"><div><h2>آخرین رویدادهای سیستم</h2><p>۵ رویداد اخیر از سابقه‌ی ممیزی</p></div>
            <a class="link" style="font-size:var(--fs-caption)" href="activity.html">همه <i data-icon="arrow-left"></i></a></div>
          <div class="timeline">
            <div class="tl-item tl-warn"><div class="tl-title">تعلیق کاربر <b class="ltr" style="direction:ltr">usr_6R2S8T</b></div><div class="tl-meta"><span>مریم کریمی</span><span>همین حالا</span></div></div>
            <div class="tl-item tl-sec"><div class="tl-title">تغییر حد نرخ سازمان شبکه‌نو</div><div class="tl-meta"><span>مریم کریمی</span><span>امروز · ۰۹:۴۰</span></div></div>
            <div class="tl-item tl-ok"><div class="tl-title">استقرار API Gateway v2.14.1</div><div class="tl-meta"><span>سیستم · CI/CD</span><span>۱۸ مرداد · ۰۲:۰۰</span></div></div>
            <div class="tl-item tl-fail"><div class="tl-title">رویداد امنیتی: تلاش دسترسی ادمین</div><div class="tl-meta"><span>مسدود شد</span><span>۲ روز پیش · ۰۴:۳۹</span></div></div>
            <div class="tl-item tl-ok"><div class="tl-title">انتشار سند «راهنمای Webhook»</div><div class="tl-meta"><span>سمیه کاظمی</span><span>۳ روز پیش</span></div></div>
          </div>
        </div>
      </div>
    </div>'''
    return admin_page('نمای کلی', 'index.html', 'نمای کلی سیستم', 'سلامت، درآمد، مصرف و رویدادهای پلتفرم در یک نگاه — <span class="fa-num">۳۱ مرداد ۱۴۰۵</span>', content, charts=True)

def build_users(prefix=''):
    org_opts = [('', '—')] + [(o['id'], o['name']) for o in [
        {'id': 'org_7F31A2', 'name': 'ابرینو'}, {'id': 'org_2B8C4D', 'name': 'داده‌پرداز'},
        {'id': 'org_9D1E6F', 'name': 'هوش‌یار'}, {'id': 'org_4E5F8A', 'name': 'فراز'},
        {'id': 'org_6A3B7C', 'name': 'شبکه‌نو'}, {'id': 'org_3C8D9E', 'name': 'پایش'},
        {'id': 'org_8F1A2B', 'name': 'رایانش'}, {'id': 'org_5E2F3G', 'name': 'کدینو'}]]
    toolbar = search_in('users', 'جستجوی نام یا ایمیل…') + \
        filt('users', 'status', [('active', 'فعال'), ('suspended', 'تعلیق‌شده'), ('churned', 'لغوشده'), ('past_due', 'پرداخت معوق'), ('trial', 'آزمایشی')], 'وضعیت') + \
        filt('users', 'plan', [('پایه', 'پایه'), ('رشد', 'رشد'), ('حرفه‌ای', 'حرفه‌ای'), ('سازمانی', 'سازمانی')], 'پلن') + \
        filt('users', 'org', org_opts, 'سازمان') + export_btn('users', 'خروجی')
    cols = [{'label': 'کاربر'}, {'label': 'سازمان'}, {'label': 'پلن'}, {'label': 'وضعیت', 'sort': 'status'},
            {'label': 'آخرین فعالیت', 'sort': 'last'}, {'label': 'ثبت‌نام', 'sort': 'joined'}, {'label': ''}]
    content = '<div class="kpi-grid">' + \
        kpi('کل کاربران', '۵۷۱', 'همه‌ی زمان‌ها', ('up', '۱۲٪'), 'users-round', True) + \
        kpi('کاربران فعال', '۴۶۲', '۳۰ روز اخیر', ('up', '۲٫۱٪'), 'user-check') + \
        kpi('تعلیق‌شده', '۱', 'نیاز به بررسی', ('mid', '—'), 'user-x') + \
        kpi('ثبت‌نام این ماه', '۱۳۴', 'شهریور ۱۴۰۵', ('up', '۱۰٫۷٪'), 'user-plus') + \
        kpi('نرخ تبدیل', '۲۳٫۴٪', 'ثبت‌نام → پرداخت', ('down', '۰٫۸٪'), 'percent') + '</div>'
    content += note('با انتخاب چند کاربر، نوار عملیات گروهی ظاهر می‌شود: تعلیق، فعال‌سازی، ارسال اعلان و خروجی. همه‌ی اقدامات در <a class="link" href="security.html#audit">Audit Logs</a> ثبت می‌شوند.')
    content += table_card('مدیریت کاربران', 'کاربران پلتفرم به‌همراه سازمان و وضعیت اشتراک', 'users', cols, toolbar, selectable=True)
    content += '''<div class="bulk-bar" data-ad-bulk="users">
      <b><span data-ad-bcount>۰</span> کاربر انتخاب شد</b><span class="sep"></span>
      <button class="btn btn-ghost btn-sm" data-bulk-action="suspend"><i data-icon="user-x"></i> تعلیق</button>
      <button class="btn btn-ghost btn-sm" data-bulk-action="activate"><i data-icon="user-check"></i> فعال‌سازی</button>
      <button class="btn btn-ghost btn-sm" data-bulk-action="notify"><i data-icon="bell"></i> اعلان</button>
      <button class="btn btn-ghost btn-sm" data-bulk-action="plan"><i data-icon="repeat"></i> تغییر پلن</button>
      <button class="btn btn-secondary btn-sm" data-bulk-action="export"><i data-icon="download"></i> خروجی</button>
    </div>'''
    return admin_page('کاربران', 'users.html', 'مدیریت کاربران', 'دیده‌بانی، تعلیق و پشتیبانی از کاربران پلتفرم', content)

def build_organizations(prefix=''):
    toolbar = search_in('orgs', 'جستجوی سازمان…') + export_btn('orgs', 'خروجی')
    cols = [{'label': 'سازمان'}, {'label': 'مالک'}, {'label': 'اعضا', 'sort': 'members'}, {'label': 'پلن'},
            {'label': 'درخواست ۳۰ روز', 'sort': 'req30'}, {'label': 'MRR', 'sort': 'mrr'}, {'label': 'وضعیت', 'sort': 'status'}, {'label': 'ریسک', 'sort': 'risk'}]
    content = '<div class="kpi-grid">' + \
        kpi('سازمان‌ها', '۸', '۷ فعال · ۱ تعلیق‌شده', ('up', '+۱'), 'building-2', True) + \
        kpi('مجموع اعضا', '۵۵', 'میانگین ۷ عضو', ('up', '۴٪'), 'users-round') + \
        kpi('مجموع MRR', '۴۰٬۸۰۰<small>هزار تومان</small>', 'از ۷ سازمان فعال', ('up', '۴٫۲٪'), 'wallet') + \
        kpi('سازمان‌های پرریسک', '۲', 'رایانش · شبکه‌نو', ('mid', 'نیاز به بررسی'), 'shield-alert') + '</div>'
    content += note('مصرف سازمان‌ها از داده‌ی مشترک پلتفرم خوانده می‌شود؛ کلیک روی هر ردیف، نمای سلامت سازمان، اعضا و سابقه را باز می‌کند.', 'building-2')
    content += table_card('مدیریت سازمان‌ها', 'سازمان‌های مشتری پلتفرم با سلامت، مصرف و درآمد', 'orgs', cols, toolbar)
    return admin_page('سازمان‌ها', 'organizations.html', 'مدیریت سازمان‌ها', 'سلامت، مصرف و ریسک سازمان‌های مشتری', content)

def build_subscriptions(prefix=''):
    toolbar = search_in('subs', 'جستجوی شماره یا سازمان…') + \
        filt('subs', 'status', [('active', 'فعال'), ('trialing', 'آزمایشی'), ('past_due', 'پرداخت معوق'), ('canceled', 'لغوشده')], 'وضعیت') + \
        filt('subs', 'pay', [('paid', 'پرداخت‌شده'), ('pending', 'در انتظار'), ('failed', 'ناموفق'), ('none', 'بدون پرداخت')], 'پرداخت') + export_btn('subs', 'خروجی')
    cols = [{'label': 'مشتری'}, {'label': 'پلن'}, {'label': 'مبلغ', 'sort': 'price'}, {'label': 'وضعیت', 'sort': 'status'},
            {'label': 'تمدید'}, {'label': 'مصرف'}, {'label': 'پرداخت'}]
    content = '<div class="kpi-grid">' + \
        kpi('اشتراک‌های فعال', '۶', 'درآمد: ۲۲٬۳۴۰٬۰۰۰ تومان', ('up', '۴٪'), 'credit-card', True) + \
        kpi('آزمایشی', '۱', 'فراز — ۵ روز باقی', ('mid', '—'), 'timer') + \
        kpi('پرداخت معوق', '۱', 'شبکه‌نو · ۳٬۴۹۰٬۰۰۰ تومان', ('down', 'نیاز به پیگیری'), 'alert-triangle') + \
        kpi('لغوشده (۳۰ روز)', '۱', 'نرخ چرخش: ۱٫۸٪', ('up', 'بهبود'), 'archive') + '</div>'
    content += table_card('مدیریت اشتراک‌ها', 'اشتراک سازمان‌ها با وضعیت تمدید و پرداخت', 'subs', cols, toolbar)
    return admin_page('اشتراک‌ها', 'subscriptions.html', 'مدیریت اشتراک‌ها', 'چرخه‌ی حیات اشتراک‌ها، تمدید و پرداخت', content)

# ============================================================== REVENUE ====
def _range_pills(key, items, active):
    btns = ''.join('<button data-range="%s" class="%s">%s</button>' % (k, 'active' if k == active else '', l) for k, l in items)
    return '<div class="pill-row" data-ranges="%s" role="group" aria-label="بازه زمانی">%s</div>' % (key, btns)

def build_revenue(prefix=''):
    c1 = canvas('line', ['مهر', 'آبان', 'آذر', 'دی', 'بهمن', 'اسفند', 'فروردین', 'اردیبهشت', 'خرداد', 'تیر', 'مرداد', 'شهریور'],
                [112, 118, 124, 131, 139, 146, 158, 165, 172, 184, 196, 207], ['rgb(56,189,248)'],
                'میلیون تومان', 'MRR', fill=True, holder_key='mrr')
    c1b = canvas('bar', ['هفته ۱', 'هفته ۲', 'هفته ۳', 'هفته ۴', 'هفته ۵', 'هفته ۶', 'هفته ۷', 'هفته ۸'],
                 [44, 46, 45, 48, 47, 50, 49, 52], ['rgb(56,189,248)'], 'میلیون تومان', 'MRR')
    c1c = canvas('line', ['۱', '۲', '۳', '۴', '۵', '۶', '۷', '۸', '۹', '۱۰', '۱۱', '۱۲', '۱۳', '۱۴'],
                 [6.2, 6.4, 6.3, 6.8, 6.6, 7.1, 6.9, 7.4, 7.2, 7.6, 7.4, 7.9, 7.7, 8.1], ['rgb(56,189,248)'],
                 'میلیون تومان', 'MRR', fill=True)
    js_range = """<script>
(function(){
  var MRR_RANGES = {
    monthly: { labels: ['مهر','آبان','آذر','دی','بهمن','اسفند','فروردین','اردیبهشت','خرداد','تیر','مرداد','شهریور'], values: [112,118,124,131,139,146,158,165,172,184,196,207] },
    weekly:  { labels: ['هفته ۱','هفته ۲','هفته ۳','هفته ۴','هفته ۵','هفته ۶','هفته ۷','هفته ۸'], values: [44,46,45,48,47,50,49,52] },
    daily:   { labels: ['۱','۲','۳','۴','۵','۶','۷','۸','۹','۱۰','۱۱','۱۲','۱۳','۱۴'], values: [6.2,6.4,6.3,6.8,6.6,7.1,6.9,7.4,7.2,7.6,7.4,7.9,7.7,8.1] }
  };
  window.ADMIN_CHARTS_MRR = MRR_RANGES;
})();
</script>"""
    rev_chart = chart_card('رشد درآمد تکرارشونده', 'میلیون تومان — با کنترل بازه زمانی', c1,
                           legend([('#38BDF8', 'MRR')]),
                           extra='<div class="flex gap-8" style="flex-wrap:wrap">' + _range_pills('mrr', [('monthly', 'ماهانه'), ('weekly', 'هفتگی'), ('daily', 'روزانه')], 'monthly') + '</div>')
    content = '<div class="kpi-grid">' + \
        kpi('درآمد ماهانه (MRR)', '۲۰۷<small>میلیون تومان</small>', 'شهریور ۱۴۰۵', ('up', '۵٫۶٪'), 'wallet', True) + \
        kpi('درآمد سالانه (ARR)', '۲٬۴۸۴<small>میلیون تومان</small>', 'پیش‌بینی پایان سال', ('up', '۲۳٪'), 'trending-up') + \
        kpi('LTV', '۴۸<small>میلیون تومان</small>', 'میانگین هر مشتری', ('up', '۳٪'), 'gem') + \
        kpi('ARPU', '۳۲۸<small>هزار تومان</small>', 'هر کاربر فعال', ('up', '۱٫۲٪'), 'users-round') + \
        kpi('نرخ چرخش', '۱٫۸٪', 'ماهانه', ('up', '۰٫۳٪ بهبود'), 'repeat') + \
        kpi('درآمد خالص', '۲۰۱<small>میلیون تومان</small>', 'پس از استرداد', ('up', '۵٫۱٪'), 'coins') + \
        kpi('استردادها', '۹٬۹۰۰<small>هزار تومان</small>', '۱ فاکتور', ('mid', '—'), 'rotate-ccw') + \
        kpi('پرداخت‌های ناموفق', '۶٬۹۸۰<small>هزار تومان</small>', '۲ تراکنش · پیگیری', ('down', 'خطر'), 'alert-circle') + '</div>'
    content += rev_chart
    content += '''<div class="dash-grid-2e">
      <div class="chart-card">
        <div class="chart-card-head"><div><h2>درآمد به تفکیک پلن</h2><p>سهم هر پلن از درآمد ماهانه</p></div></div>
        ''' + dist_card(
            [107640000, 64170000, 28980000, 6200000],
            ['سازمانی', 'حرفه‌ای', 'رشد', 'پایه'],
            ['۱۰۷٫۶ م.ت', '۶۴٫۲ م.ت', '۲۹٫۰ م.ت', '۶٫۲ م.ت'],
            ['rgb(56,189,248)', 'rgb(59,130,246)', 'rgb(167,139,250)', 'rgb(113,113,122)'],
            '۲۰۷', 'میلیون تومان',
            'نمودار توزیع درآمد به تفکیک پلن: ۵۲٪ سازمانی، ۳۱٪ حرفه‌ای، ۱۴٪ رشد، ۳٪ پایه',
            'توزیع درآمد — شهریور ۱۴۰۵', '۲۰۷ میلیون تومان', 70) + '''
      </div>
      <div class="chart-card">
        <div class="chart-card-head"><div><h2>درآمد جدید در برابر موجود</h2><p>میلیون تومان — ۳ ماه اخیر</p></div></div>
        <div class="chart-holder" style="height:230px">''' + canvas('bar', ['مرداد', 'تیر', 'خرداد'], [[18, 14, 11], [178, 170, 161]], ['rgb(52,211,153)', 'rgb(56,189,248)'], 'میلیون تومان', 'جدید', stacked=True) + legend([('#34D399', 'درآمد جدید'), ('#38BDF8', 'درآمد موجود')]) + '''</div>
      </div>
    </div>'''
    inv_toolbar = search_in('invoices', 'جستجوی شماره فاکتور…') + export_btn('invoices', 'خروجی فاکتورها')
    inv_cols = [{'label': 'شماره'}, {'label': 'مشتری'}, {'label': 'مبلغ', 'sort': 'amount'}, {'label': 'وضعیت', 'sort': 'status'}, {'label': 'صدور'}, {'label': 'سررسید'}, {'label': ''}]
    content += '<div id="invoices">' + table_card('فاکتورها', 'فاکتورهای صادرشده‌ی شهریور ۱۴۰۵', 'invoices', inv_cols, inv_toolbar) + '</div>'
    pay_toolbar = search_in('payments', 'جستجوی شناسه تراکنش…') + filt('payments', 'status', [('success', 'موفق'), ('failed', 'ناموفق'), ('pending', 'در انتظار'), ('refunded', 'مسترد')], 'وضعیت') + export_btn('payments', 'خروجی تراکنش‌ها')
    pay_cols = [{'label': 'شناسه'}, {'label': 'سازمان'}, {'label': 'مبلغ', 'sort': 'amount'}, {'label': 'وضعیت', 'sort': 'status'}, {'label': 'روش'}, {'label': 'زمان'}, {'label': 'نتیجه / دلیل'}]
    content += '<div id="payments">' + table_card('پرداخت‌ها', 'تراکنش‌های درگاه با وضعیت و دلیل شکست', 'payments', pay_cols, pay_toolbar) + '</div>'
    return admin_page('درآمد', 'revenue.html', 'درآمد و مالی', 'MRR، فاکتورها، پرداخت‌ها و پیگیری پرداخت‌های ناموفق — واحد پول: تومان', content, charts=True, extra_scripts=js_range)

# ================================================================ API ======
def build_api(prefix=''):
    toolbar = export_btn('orgs', 'خروجی رتبه‌بندی')
    org_cols = [{'label': 'سازمان'}, {'label': 'درخواست', 'sort': 'req30'}, {'label': 'سهم'}, {'label': 'خطا', 'sort': 'err30'}, {'label': 'نرخ خطا'}, {'label': 'رشد'}]
    content = '<div class="kpi-grid">' + \
        kpi('مجموع درخواست‌ها', '۳۲٫۴<small>میلیون</small>', '۳۰ روز اخیر', ('up', '۱۲٪'), 'server', True) + \
        kpi('موفق', '۳۲٬۳۲۱٬۰۰۰', '۹۹٫۸۲٪', ('up', 'پایدار'), 'check-circle-2') + \
        kpi('ناموفق', '۵۷٬۹۰۰', '۰٫۱۸٪', ('down', '۱۶٪'), 'x-circle') + \
        kpi('میانگین تأخیر', '۸۴ms', 'P50', ('up', '−۳ms'), 'timer') + \
        kpi('P95 / P99', '۲۳۰ / ۵۴۰ms', 'صدک‌ها', ('mid', 'پایدار'), 'gauge') + \
        kpi('رویداد محدودیت نرخ', '۴٬۸۱۰', '۴۲۹ در ۳۰ روز', ('down', '۱۲٪'), 'ban') + '</div>'
    content += note('این صفحه نمای عملیاتی کل پلتفرم است؛ برای نمای هر مشتری، به <a class="link" href="organizations.html">سازمان‌ها</a> بروید.', 'server')
    content += '''<div class="chart-card" style="margin-bottom:16px">
      <div class="chart-card-head"><div><h2>ترافیک API — ۷ روز اخیر</h2><p>مجموع درخواست‌های روزانه</p></div></div>
      <div class="chart-holder" style="height:240px">''' + canvas('bar', ['شنبه', 'یکشنبه', 'دوشنبه', 'سه‌شنبه', 'چهارشنبه', 'پنجشنبه', 'جمعه'], [41200, 44800, 43100, 47600, 51200, 48900, 43400], ['rgb(56,189,248)'], 'درخواست', 'درخواست') + '''</div>
    </div>'''
    content += '<div class="dash-grid-2e"><div>' + table_card('مصرف به تفکیک سازمان', 'رتبه‌بندی سازمان‌ها بر اساس درخواست ۳۰ روز', 'orgs', org_cols, toolbar) + '</div>'
    content += '''<div class="chart-card">
      <div class="chart-card-head"><div><h2>مرکز خطاها</h2><p>۳۰ روز اخیر — کدهای خطا</p></div></div>
      ''' + dist_card(
        [2840, 1920, 1110, 840, 410],
        ['401 · احراز هویت', '429 · محدودیت نرخ', '404 · یافت نشد', '422 · داده نامعتبر', '5xx · خطای سرور'],
        [fa(2840), fa(1920), fa(1110), fa(840), fa(410)],
        ['rgb(248,113,113)', 'rgb(251,191,36)', 'rgb(167,139,250)', 'rgb(56,189,248)', 'rgb(34,211,238)'],
        fa(7120), 'خطا',
        'نمودار توزیع خطاها بر اساس کد: ۳۹٫۹٪ احراز هویت، ۲۷٪ محدودیت نرخ، ۱۵٫۶٪ یافت نشد، ۱۱٫۸٪ داده نامعتبر، ۵٫۷٪ خطای سرور',
        'مجموع خطاها — ۳۰ روز اخیر', fa(7120) + ' خطا', 70) + '''
      <div style="margin-top:14px" class="t-caption">سازمان‌های متأثر از خطای 5xx: <b class="fa-num">هوش‌یار</b> و <b class="fa-num">شبکه‌نو</b> — <a class="link" href="activity.html#incidents">Incident باز</a></div>
    </div></div>'''
    content += '''<div class="chart-card" style="margin-top:16px">
      <div class="chart-card-head"><div><h2>عملکرد Endpointها</h2><p>۷ روز اخیر — پرمصرف‌ترین مسیرها</p></div></div>
      <div class="table-wrap ad-table-wrap" style="border:none;border-radius:0">
        <table class="ad-table">
          <thead><tr><th scope="col">Endpoint</th><th scope="col">درخواست</th><th scope="col">نرخ موفقیت</th><th scope="col">نرخ خطا</th><th scope="col">تأخیر میانگین</th><th scope="col">P95</th><th scope="col">P99</th><th scope="col">سازمان‌های متأثر</th></tr></thead>
          <tbody>
            <tr><td class="cell-main ltr" style="direction:ltr">POST /v1/chat/completions</td><td class="num">۸٬۹۴۰٬۰۰۰</td><td class="num">۹۹٫۶۱٪</td><td><span class="badge badge-amber">۰٫۳۹٪</span></td><td class="num">۸۹۴ms</td><td class="num">۲٬۱۰۰ms</td><td class="num">۴٬۲۰۰ms</td><td><b class="fa-num">۳</b></td></tr>
            <tr><td class="cell-main ltr" style="direction:ltr">GET /v1/users</td><td class="num">۴٬۸۲۰٬۰۰۰</td><td class="num">۹۹٫۹۷٪</td><td><span class="badge badge-green">۰٫۰۳٪</span></td><td class="num">۴۱ms</td><td class="num">۱۲۰ms</td><td class="num">۳۱۰ms</td><td><b class="fa-num">۷</b></td></tr>
            <tr><td class="cell-main ltr" style="direction:ltr">POST /v1/payments</td><td class="num">۳٬۱۱۰٬۰۰۰</td><td class="num">۹۹٫۸۸٪</td><td><span class="badge badge-green">۰٫۱۲٪</span></td><td class="num">۱۸۰ms</td><td class="num">۴۶۰ms</td><td class="num">۹۸۰ms</td><td><b class="fa-num">۵</b></td></tr>
            <tr><td class="cell-main ltr" style="direction:ltr">POST /v1/summaries</td><td class="num">۱٬۲۴۰٬۰۰۰</td><td class="num">۹۸٫۱۰٪</td><td><span class="badge badge-amber">۱٫۹۰٪</span></td><td class="num">۱٬۴۵۰ms</td><td class="num">۳٬۹۰۰ms</td><td class="num">۸٬۱۰۰ms</td><td><b class="fa-num">۲</b></td></tr>
            <tr><td class="cell-main ltr" style="direction:ltr">GET /v1/files</td><td class="num">۹۸۰٬۰۰۰</td><td class="num">۹۹٫۹۴٪</td><td><span class="badge badge-green">۰٫۰۶٪</span></td><td class="num">۹۲ms</td><td class="num">۲۴۰ms</td><td class="num">۵۲۰ms</td><td><b class="fa-num">۴</b></td></tr>
          </tbody>
        </table>
      </div>
    </div>'''
    return admin_page('مصرف API', 'api.html', 'مصرف API پلتفرم', 'ترافیک، عملکرد Endpointها، خطاها و محدودیت نرخ در کل پلتفرم', content, charts=True)

# ============================================================ ACTIVITY =====
def build_activity(prefix=''):
    content = '<div class="kpi-grid">' + \
        kpi('استقرارها (۳۰ روز)', '۱۴', 'آخرین: API Gateway 2.14.1', ('up', '—'), 'rocket', True) + \
        kpi('تغییرات پیکربندی', '۹', 'همه ثبت‌شده در Audit', ('mid', '—'), 'settings') + \
        kpi('Incidentهای فعال', '۱', 'کندی صف گزارش‌گیری', ('mid', 'نیاز به بررسی'), 'siren') + \
        kpi('رویدادهای امنیتی', '۸', '۲ مسدود شده در ۷ روز', ('up', '—'), 'shield-alert') + '</div>'
    content += '''<div class="chart-card" style="padding:0;overflow:hidden">
      <div class="chart-card-head" style="padding:18px 22px 0"><div><h2>تایم‌لاین فعالیت سیستم</h2><p>استقرارها، تغییرات پیکربندی، رویدادهای امنیتی و اقدامات مدیریتی — از سابقه‌ی ممیزی</p></div></div>
      <div style="padding:4px 22px 18px" class="timeline">
        <div class="tl-item tl-warn"><div class="tl-title">تعلیق کاربر <b class="ltr" style="direction:ltr">usr_6R2S8T</b></div><div class="tl-meta"><span>اقدام: <b>مریم کریمی</b></span><span>امروز · ۱۱:۰۲</span><span class="risk risk-low">موفق</span></div><div class="tl-desc">سه تلاش ورود از IP ناشناس؛ طبق سیاست امنیتی، حساب تعلیق شد.</div></div>
        <div class="tl-item tl-sec"><div class="tl-title">تغییر حد نرخ سازمان شبکه‌نو <b class="badge badge-amber">۷۵۰ ← ۱۵۰۰ / دقیقه</b></div><div class="tl-meta"><span>اقدام: <b>مریم کریمی</b></span><span>امروز · ۰۹:۴۰</span><span>مدت: ۲۴ ساعت</span></div><div class="tl-desc">در پی تیکت TKT-1042 برای پردازش دسته‌ای موقتاً افزایش یافت.</div></div>
        <div class="tl-item tl-ok"><div class="tl-title">استقرار API Gateway <b class="ltr" style="direction:ltr">v2.14.1</b></div><div class="tl-meta"><span>سیستم · CI/CD</span><span>۱۸ مرداد · ۰۲:۰۰</span></div><div class="tl-desc">۰٪ خطا در ۱۵ دقیقه‌ی اول؛ خطای نمونه‌برداری GPU هموار شد.</div></div>
        <div class="tl-item tl-fail"><div class="tl-title">تلاش دسترسی ادمین <b class="badge">مسدود</b></div><div class="tl-meta"><span>IP: <b class="ltr" style="direction:ltr">45.155.204.11</b></span><span>۲ روز پیش · ۰۴:۳۹</span></div><div class="tl-desc">۵ تلاش ورود با الگوی Brute-force؛ IP به لیست مسدود افزوده شد.</div></div>
        <div class="tl-item tl-ok"><div class="tl-title">انتشار سند «راهنمای Webhook»</div><div class="tl-meta"><span>اقدام: <b>سمیه کاظمی</b></span><span>۳ روز پیش · ۱۵:۴۲</span></div></div>
        <div class="tl-item tl-ok"><div class="tl-title">پشتیبان‌گیری خودکار — نسخه‌ی ۳۴۱</div><div class="tl-meta"><span>سیستم</span><span>هر شب · ۰۳:۰۰</span></div><div class="tl-desc">حجم: ۲۸GB · ماندگاری: ۳۰ روز</div></div>
        <div class="tl-item tl-warn"><div class="tl-title">بازگشت وجه فاکتور <b class="ltr" style="direction:ltr">INV-۱۴۰۵-۰۶۰</b></div><div class="tl-meta"><span>اقدام: <b>مریم کریمی</b></span><span>۲۶ مرداد · ۱۴:۰۲</span></div><div class="tl-desc">درخواست مشتری — دوره استفاده نشده بود.</div></div>
      </div>
    </div>'''
    content += '<div id="incidents">'
    content += note('وضعیت هر Incident با شدت (آیکون + برچسب + رنگ) مشخص است؛ کلیک روی ردیف، جزئیات کامل و تیم مسئول را باز می‌کند.', 'siren')
    inc_cols = [{'label': 'عنوان'}, {'label': 'شدت', 'sort': 'severity'}, {'label': 'سرویس'}, {'label': 'شروع'}, {'label': 'مدت'}, {'label': 'وضعیت', 'sort': 'status'}, {'label': 'تیم مسئول'}]
    content += table_card('Incidentهای سیستم', 'رخدادهای فعال و اخیر با وضعیت پیگیری', 'incidents', inc_cols, '')
    content += '</div>'
    return admin_page('فعالیت سیستم', 'activity.html', 'فعالیت سیستم و Incidentها', 'تایم‌لاین رویدادها و وضعیت رخدادهای زیرساخت', content, extra_scripts='<script>window.__adIncidentAnchor=true;</script>')

# ============================================================ SUPPORT ======
def build_support(prefix=''):
    toolbar = search_in('tickets', 'جستجوی شماره یا موضوع…') + \
        filt('tickets', 'priority', [('critical', 'بحرانی'), ('high', 'زیاد'), ('medium', 'متوسط'), ('low', 'کم')], 'اولویت') + \
        filt('tickets', 'status', [('urgent', 'فوری'), ('open', 'باز'), ('wait_customer', 'در انتظار مشتری'), ('wait_support', 'در انتظار پشتیبانی'), ('resolved', 'حل‌شده')], 'وضعیت') + export_btn('tickets', 'خروجی')
    cols = [{'label': 'شماره'}, {'label': 'موضوع'}, {'label': 'کاربر'}, {'label': 'سازمان'}, {'label': 'اولویت', 'sort': 'priority'}, {'label': 'وضعیت', 'sort': 'status'}, {'label': 'مسئول'}, {'label': 'آخرین فعالیت'}]
    content = '<div class="kpi-grid">' + \
        kpi('تیکت‌های باز', '۴', 'در انتظار تیم پشتیبانی', ('mid', '—'), 'life-buoy', True) + \
        kpi('فوری', '۱', 'TKT-1042 · شبکه‌نو', ('down', 'نیاز به پاسخ'), 'alert-triangle') + \
        kpi('در انتظار مشتری', '۱', 'TKT-1041', ('mid', '—'), 'clock') + \
        kpi('حل‌شده (۷ روز)', '۱۹', 'میانگین پاسخ: ۲۸ دقیقه', ('up', '۴٪'), 'check-circle-2') + '</div>'
    content += note('اولویت‌ها همیشه با آیکون و برچسب نمایش داده می‌شوند (بحرانی / زیاد / متوسط / کم) — نه فقط رنگ. پاسخ داخل کشو با «ثبت یادداشت» و «حل تیکت» شبیه‌سازی می‌شود و در Audit ثبت می‌گردد.', 'life-buoy')
    content += table_card('مرکز پشتیبانی', 'تیکت‌های پشتیبانی مشتریان پلتفرم', 'tickets', cols, toolbar)
    return admin_page('پشتیبانی', 'support.html', 'مرکز پشتیبانی', 'مدیریت تیکت‌ها، اولویت‌بندی و پیگیری پاسخ‌ها', content)

# ======================================================== NOTIFICATIONS ====
def build_notifications(prefix=''):
    content = note('فیلتر نوع، مارک‌گذاری خوانده‌شده و «همه خوانده شد» فعال است. نوع هر اعلان با آیکون متمایز نمایش داده می‌شود.', 'bell')
    chips = ['all', 'incident', 'security', 'billing', 'operations', 'support', 'product']
    labels = {'all': 'همه', 'incident': 'رخداد', 'security': 'امنیت', 'billing': 'مالی', 'operations': 'عملیات', 'support': 'پشتیبانی', 'product': 'محصول'}
    content += '<div class="n-filter">' + ''.join(
        '<button data-ad-notif-filter="%s" class="%s">%s</button>' % (k, 'active' if k == 'all' else '', labels[k]) for k in chips) + '</div>'
    content += '<div id="adNotifList" data-ad-notif-list></div>'
    content += '<div style="margin-top:16px;display:flex;gap:8px"><button class="btn btn-secondary btn-sm" data-ad-notif-all><i data-icon="check-check"></i> علامت‌گذاری همه به‌عنوان خوانده</button>'
    content += '<button class="btn btn-ghost btn-sm" data-ad-export="اعلان‌ها"><i data-icon="download"></i> خروجی</button></div>'
    return admin_page('اعلان‌ها', 'notifications.html', 'مرکز اعلان‌ها', 'اعلان‌های سیستم، امنیت، مالی، عملیات، پشتیبانی و محصول', content)

# ============================================================== CONTENT ====
def build_content(prefix=''):
    btns = []
    panes = []
    def ptabs(grp, key, label, count, tbl):
        btns.append('<button data-atab="%s" class="%s">%s<span class="t-count">%s</span></button>' % (key, 'active' if not btns else '', label, count))
        panes.append('<div class="a-panel%s" data-apanel="%s" data-atab="%s">%s</div>' % (' active' if not panes else '', grp, key, tbl))
    blog = table_card('مدیریت بلاگ', 'مقالات منتشرشده، در بازبینی و پیش‌نویس', 'blog',
                      [{'label': 'عنوان'}, {'label': 'نویسنده'}, {'label': 'وضعیت', 'sort': 'status'}, {'label': 'بازدید', 'sort': 'views'}, {'label': 'تاریخ انتشار'}, {'label': ''}],
                      export_btn('blog', 'خروجی'))
    docs = table_card('مدیریت مستندات', 'مقالات مستندات با دسته‌بندی و وضعیت', 'docs',
                      [{'label': 'مقاله'}, {'label': 'دسته'}, {'label': 'نویسنده'}, {'label': 'وضعیت', 'sort': 'status'}, {'label': 'آخرین به‌روزرسانی'}, {'label': 'بازدید'}, {'label': ''}],
                      export_btn('docs', 'خروجی'))
    cl = table_card('مدیریت تغییرات (Changelog)', 'نسخه‌های منتشرشده و پیش‌نویس', 'changelog',
                    [{'label': 'نسخه'}, {'label': 'عنوان'}, {'label': 'وضعیت', 'sort': 'status'}, {'label': 'تاریخ'}, {'label': 'نویسنده'}, {'label': ''}], '')
    an = table_card('مدیریت اعلان‌ها', 'اطلاع‌رسانی، هشدار، به‌روزرسانی و بحرانی', 'annc',
                    [{'label': 'عنوان'}, {'label': 'نوع'}, {'label': 'وضعیت', 'sort': 'status'}, {'label': 'تاریخ'}, {'label': 'نویسنده'}, {'label': ''}], '')
    ptabs('content', 'blog', 'بلاگ', '۴', blog)
    ptabs('content', 'docs', 'مستندات', '۵', docs)
    ptabs('content', 'changelog', 'Changelog', '۴', cl)
    ptabs('content', 'annc', 'اعلان‌های سایت', '۴', an)
    content = note('هر چهار بخش محتوایی از داده‌ی مشترک تغذیه می‌شوند؛ وضعیت‌ها (پیش‌نویس / در بازبینی / منتشرشده / بایگانی) با بج مشخص‌اند.', 'file-text')
    content += '<div class="a-tabs" data-atabs="content">' + ''.join(btns) + '</div>' + ''.join(panes)
    return admin_page('محتوا', 'content.html', 'مدیریت محتوا', 'بلاگ، مستندات، تغییرات و اعلان‌های سایت در یک پنل', content)

# ================================================================ FLAGS ====
def build_flags(prefix=''):
    toolbar = search_in('flags', 'جستجوی نام یا کلید…') + filt('flags', 'env', [('production', 'تولید'), ('staging', 'آزمایش')], 'محیط') + export_btn('flags', 'خروجی')
    cols = [{'label': 'Feature'}, {'label': 'وضعیت'}, {'label': 'محیط'}, {'label': 'توزیع', 'sort': 'rollout'}, {'label': 'ایجاد'}, {'label': 'آخرین تغییر'}, {'label': 'مالک'}]
    content = '<div class="kpi-grid">' + \
        kpi('Feature Flags', '۸', 'در ۲ محیط', ('mid', '—'), 'flag', True) + \
        kpi('فعال در تولید', '۴', '۲ مورد در حال توزیع', ('up', '—'), 'check-circle-2') + \
        kpi('در حال توزیع', '۳', '۱۰٪ · ۲۵٪ · ۵۰٪', ('mid', '—'), 'sliders-horizontal') + \
        kpi('غیرفعال', '۳', 'نیاز به بازبینی', ('mid', '—'), 'toggle-right') + '</div>'
    content += note('تغییر توزیع (Rollout) روی محیط <b>تولید</b> نیاز به تأیید دارد و در سابقه‌ی ممیزی ثبت می‌شود. سوییچ هر ردیف نیز همین‌قاعده را دنبال می‌کند.', 'shield-check')
    content += table_card('Feature Flags', 'ویژگی‌های پلتفرم با توزیع تدریجی', 'flags', cols, toolbar)
    return admin_page('Feature Flags', 'flags.html', 'Feature Flags', 'کنترل ویژگی‌ها و توزیع تدریجی روی محیط‌های مختلف', content)

# ============================================================== SECURITY ===
def build_security(prefix=''):
    ev = table_card('رویدادهای امنیتی', 'ورودها، نشست‌ها و دسترسی‌های مشکوک — ۷ روز اخیر', 'security',
                    [{'label': 'رویداد'}, {'label': 'کاربر'}, {'label': 'IP'}, {'label': 'دستگاه'}, {'label': 'زمان'}, {'label': 'شدت', 'sort': 'severity'}, {'label': 'وضعیت', 'sort': 'status'}],
                    search_in('security', 'جستجوی رویداد یا IP…') + filt('security', 'severity', [('critical', 'بحرانی'), ('high', 'زیاد'), ('medium', 'متوسط'), ('low', 'کم')], 'شدت'))
    au = table_card('Audit Logs', 'سابقه‌ی کامل اقدامات مدیریتی — چه‌کسی، چه‌کاری، کِی و از کجا', 'audit',
                    [{'label': 'اقدام'}, {'label': 'فرد'}, {'label': 'هدف'}, {'label': 'زمان', 'sort': 'at'}, {'label': 'IP'}, {'label': 'نتیجه'}],
                    search_in('audit', 'جستجوی اقدام یا هدف…') + export_btn('audit', 'خروجی سوابق'))
    content = '<div class="kpi-grid">' + \
        kpi('امتیاز ریسک', '۲۴<small>/۱۰۰</small>', 'کم — وضعیت عادی', ('up', '—'), 'shield', True) + \
        kpi('رویدادهای ۷ روز', '۸', '۲ بحرانی · هر دو مسدود', ('mid', '—'), 'activity') + \
        kpi('ورودهای ناموفق', '۱۴', '۳ از IP خارجی', ('up', '—'), 'key-round') + \
        kpi('نشست‌های مشکوک', '۱', 'پایان‌یافته', ('mid', '—'), 'fingerprint') + \
        kpi('رویداد کلید API', '۶', 'همه مجاز', ('up', '—'), 'shield-alert') + \
        kpi('اقدامات ادمین', '۱۲', 'در ۷ روز', ('up', '—'), 'user-cog') + '</div>'
    content += note('خط‌مشی: داده‌های حساس هرگز به‌صورت کامل نمایش داده نمی‌شوند؛ مقادیر حساس به‌صورت ماسک‌شده‌اند. کلیک روی هر ردیف Audit، جزئیات قبل/بعد و متادیتا را باز می‌کند.', 'lock')
    content += '<div class="a-tabs" data-atabs="sec">' \
        '<button data-atab="events" class="active">رویدادهای امنیتی<span class="t-count">۸</span></button>' \
        '<button data-atab="audit">Audit Logs<span class="t-count" data-ad-audit-count>۱۲</span></button></div>'
    content += '<div class="a-panel active" id="events" data-apanel="sec" data-atab="events">' + ev + '</div>'
    content += '<div class="a-panel" id="audit" data-apanel="sec" data-atab="audit">' + au + '</div>'
    return admin_page('مرکز امنیت', 'security.html', 'مرکز امنیت و Audit Logs', 'رویدادهای امنیتی، نشست‌ها و سابقه‌ی کامل اقدامات مدیریتی', content)

# ============================================================== SETTINGS ===
def _set_card(title, icon, sub, rows):
    r = ''
    for label, ctrl, note_txt in rows:
        if 'aria-label' not in ctrl:
            if '<select' in ctrl:
                ctrl = ctrl.replace('<select', '<select aria-label="%s"' % label, 1)
            elif 'role="switch"' in ctrl:
                ctrl = ctrl.replace('tabindex="0"', 'tabindex="0" aria-label="%s"' % label, 1)
        r += '<div class="set-row"><span>%s</span>%s%s</div>' % (label, (note_txt and '<span class="t-caption">%s</span>' % note_txt) or '', ctrl)
    return '<div class="set-card"><h3>%s%s</h3><p>%s</p>%s</div>' % (IC(icon), title, sub, r)

def build_settings(prefix=''):
    def sw(on, extra):
        return '<span class="fswitch%s" role="switch" aria-checked="%s" tabindex="0" %s></span>' % (' on' if on else '', 'true' if on else 'false', extra)

    general = '<div class="set-grid">' + \
        _set_card('عمومی', 'settings', 'هویت پلتفرم و محل استقرار.', [
            ('نام پلتفرم', '<span class="badge badge-blue">بلو ورتکس</span>', ''),
            ('آدرس پایه API', '<code class="inline ltr">api.bluevertex.ir</code>', ''),
            ('منطقه زمانی', '<select class="select" style="width:auto;min-width:0"><option>تهران (UTC+3:30)</option></select>', ''),
            ('زبان پیش‌فرض', '<select class="select" style="width:auto;min-width:0"><option>فارسی</option><option>English</option></select>', '')]) + \
        _set_card('امنیت و احراز هویت', 'lock', 'سیاست‌های ورود و نشست‌ها.', [
            ('ورود دومرحله‌ای اجباری (ادمین)', sw(True, 'data-role-toggle'), ''),
            ('انقضای نشست ادمین', '<select class="select" style="width:auto;min-width:0"><option>۱۲ ساعت</option></select>', ''),
            ('قفل پس از تلاش ناموفق', sw(True, 'data-role-toggle'), '۵ تلاش'),
            ('IPهای مجاز پنل', '<code class="inline ltr">5.122.30.77</code>', '')]) + \
        _set_card('اعلان‌ها', 'bell', 'کانال‌های اطلاع‌رسانی تیم.', [
            ('اعلان بحرانی → تیکت', sw(True, 'data-role-toggle'), ''),
            ('ایمیل روزانه‌ی خلاصه', sw(True, 'data-role-toggle'), ''),
            ('اعلان Webhook', sw(False, 'data-role-toggle'), ''),
            ('اسلک تیم عملیات', sw(True, 'data-role-toggle'), '')]) + \
        _set_card('محدودیت نرخ و ذخیره‌سازی', 'gauge', 'حدود پیش‌فرض پلتفرم.', [
            ('حد نرخ پیش‌فرض', '<code class="inline ltr" style="direction:ltr">1000/min</code>', ''),
            ('حداکثر بدنه‌ی درخواست', '<select class="select" style="width:auto;min-width:0"><option>۱۲MB</option></select>', ''),
            ('ماندگاری لاگ‌ها', '<select class="select" style="width:auto;min-width:0"><option>۹۰ روز</option></select>', ''),
            ('ذخیره‌سازی فایل', sw(True, 'data-role-toggle'), '۴۶GB از ۲۰۰GB')]) + '</div>'

    roles_h = [('مجوز', 'Super Admin', 'Admin', 'عملیات', 'مالی', 'پشتیبانی', 'محتوا')]
    mx_rows = [('کاربران', 'yes', 'yes', 'yes', 'no', 'part', 'no'), ('سازمان‌ها', 'yes', 'yes', 'yes', 'no', 'part', 'no'),
               ('مالی و فاکتورها', 'yes', 'part', 'no', 'yes', 'no', 'no'), ('امنیت و Audit', 'yes', 'yes', 'part', 'no', 'no', 'no'),
               ('Feature Flags', 'yes', 'yes', 'part', 'no', 'no', 'no'), ('محتوا', 'yes', 'part', 'no', 'no', 'no', 'yes'),
               ('تنظیمات سیستم', 'yes', 'no', 'no', 'no', 'no', 'no')]
    mx_body = ''
    for row in mx_rows:
        cells = ''
        for i, v in enumerate(row):
            if i == 0:
                cells += '<td>%s</td>' % row[0]
            else:
                icon = {'yes': ('check', 'mx-yes'), 'no': ('minus', 'mx-no'), 'part': ('slash', 'mx-part')}[v]
                cells += '<td class="%s">%s</td>' % (icon[1], IC(icon[0]))
        mx_body += '<tr>%s</tr>' % cells
    mx = '''<div class="set-card" style="grid-column:1/-1">
      <h3>%s ماتریس نقش‌ها</h3><p>مجوز هر نقش روی ماژول‌ها — تغییرات با ذخیره در Audit ثبت می‌شود.</p>
      <div class="matrix-wrap"><table class="matrix">
        <thead><tr><th scope="col">مجوز</th><th scope="col">Super Admin</th><th scope="col">Admin</th><th scope="col">عملیات</th><th scope="col">مالی</th><th scope="col">پشتیبانی</th><th scope="col">محتوا</th></tr></thead>
        <tbody>%s</tbody></table></div>
    </div>''' % (IC('shield-check'), mx_body)
    roles = '<div class="set-grid">' + \
        _set_card('نقش‌ها', 'users-round', 'پنج نقش پیش‌فرض با مجوزهای مشخص.', [
            ('Super Admin', '<span class="role-chip" data-role="super">دسترسی کامل</span>', ''),
            ('Admin', '<span class="role-chip">۲۲ مجوز</span>', ''),
            ('عملیات', '<span class="role-chip">۱۴ مجوز</span>', ''),
            ('مالی', '<span class="role-chip">۹ مجوز</span>', ''),
            ('پشتیبانی', '<span class="role-chip">۸ مجوز</span>', ''),
            ('محتوا', '<span class="role-chip">۷ مجوز</span>', '')]) + \
        _set_card('مدیریت نقش', 'user-cog', 'ایجاد، تکثیر یا غیرفعال‌سازی نقش — پس از تأیید.', [
            ('ایجاد نقش جدید', '<button class="btn btn-secondary btn-sm" data-dg data-dg-title="ایجاد نقش" data-dg-text="نقش جدید با مجوزهای پیش‌فرض «فقط خواندنی» ساخته می‌شود." data-dg-ok="ایجاد نقش">' + IC('plus') + ' نقش جدید</button>', ''),
            ('تکثیر نقش «پشتیبانی»', '<button class="btn btn-secondary btn-sm" data-role-toggle>تکثیر</button>', ''),
            ('غیرفعال‌سازی نقش موقت', sw(False, 'data-role-toggle'), '')]) + mx + '</div>'

    sessions = '''<div class="set-grid">
      <div class="set-card"><h3>%s پروفایل ادمین</h3><p>مریم کریمی — مدیر پلتفرم</p>
        <div class="ad-kv"><span>نام</span><b>مریم کریمی</b></div>
        <div class="ad-kv"><span>ایمیل</span><b class="ltr" style="direction:ltr">admin@bluevertex.ir</b></div>
        <div class="ad-kv"><span>نقش</span><b><span class="role-chip" data-role="super">Super Admin</span></b></div>
        <div class="ad-kv"><span>ورود دومرحله‌ای</span><b>فعال · آخرین ورود: امروز ۰۷:۴۵</b></div>
      </div>
      <div class="set-card"><h3>%s نشست‌های فعال</h3><p>دستگاه‌هایی که به پنل متصل‌اند.</p>
        <div class="session-row"><span class="s-ic">%s</span><div style="flex:1"><b>macOS · Firefox</b><div class="s-meta">تهران، ایران · 5.122.30.77 · همین حالا</div></div><span class="cur-badge">نشست فعلی</span></div>
        <div class="session-row"><span class="s-ic">%s</span><div style="flex:1"><b>iPhone 16 · Safari</b><div class="s-meta">تهران، ایران · 5.122.30.77 · ۲ ساعت پیش</div></div><button class="btn btn-ghost btn-sm" data-dg data-dg-title="خروج از نشست" data-dg-text="این نشست بلافاصله بسته می‌شود." data-dg-ok="قطع نشست">قطع</button></div>
        <div class="session-row"><span class="s-ic">%s</span><div style="flex:1"><b>Windows · Edge</b><div class="s-meta">اصفهان، ایران · 5.122.44.91 · ۳ روز پیش</div></div><button class="btn btn-ghost btn-sm" data-dg data-dg-title="خروج از نشست" data-dg-text="این نشست بلافاصله بسته می‌شود." data-dg-ok="قطع نشست">قطع</button></div>
      </div>
    </div>''' % (IC('user-round'), IC('monitor-smartphone'), IC('laptop'), IC('smartphone'), IC('monitor'))

    dg = '''<div class="set-card" style="border-color:rgba(248,113,113,.35)">
      <h3 style="color:var(--red)">%s منطقه‌ی خطر</h3>
      <p>اقدامات برگشت‌ناپذیر — با تأیید نوعی محافظت می‌شوند.</p>
      <div class="dg-item"><div><b>غیرفعال‌سازی کامل پلتفرم</b><p>همه‌ی APIها از دسترس خارج می‌شوند. تایپ <code class="inline ltr">غیرفعال‌سازی</code> الزامی است.</p></div>
        <button class="btn btn-danger btn-sm" data-dg data-dg-title="غیرفعال‌سازی پلتفرم" data-dg-text="همه سرویس‌ها از دسترس خارج می‌شوند؛ این اقدام روی ترافیک واقعی اعمال می‌شود." data-dg-typed="غیرفعال‌سازی" data-dg-ok="غیرفعال‌سازی کامل">غیرفعال‌سازی پلتفرم</button></div>
      <div class="dg-item"><div><b>حذف سازمان «کدینو»</b><p>داده‌ها، کلیدها و سوابق به‌صورت کامل پاک می‌شوند. تایپ <code class="inline ltr">حذف</code> الزامی است.</p></div>
        <button class="btn btn-danger btn-sm" data-dg data-dg-title="حذف سازمان" data-dg-text="سازمان کدینو و همه‌ی داده‌هایش برای همیشه حذف می‌شود." data-dg-typed="حذف" data-dg-ok="حذف سازمان">حذف سازمان</button></div>
      <div class="dg-item"><div><b>غیرفعال‌سازی موقت API در محیط تولید</b><p>استقرار نسخه‌ی قبلی حفظ می‌شود؛ با تأیید ساده انجام می‌شود.</p></div>
        <button class="btn btn-danger btn-sm" data-dg data-dg-title="غیرفعال‌سازی API" data-dg-text="کلیدهای واقعی تا ۱۰ دقیقه پاسخ 503 دریافت می‌کنند." data-dg-ok="غیرفعال‌سازی">غیرفعال‌سازی API</button></div>
      <div class="dg-item"><div><b>تغییر پیکربندی تولید</b><p>مقادیر حیاتی (حد نرخ، سهمیه‌ها) فقط با تأیید مدیر قابل تغییر است.</p></div>
        <button class="btn btn-danger btn-sm" data-dg data-dg-title="تغییر پیکربندی تولید" data-dg-text="این تغییر در سابقه‌ی ممیزی با جزئیات قبل/بعد ثبت می‌شود." data-dg-ok="تأیید تغییر">تغییر پیکربندی</button></div>
    </div>''' % IC('alert-triangle')

    tab = 'general'
    content = '<div class="a-tabs" data-atabs="set">' \
        '<button data-atab="general" class="active">عمومی و امنیت</button>' \
        '<button data-atab="roles">نقش‌ها و مجوزها</button>' \
        '<button data-atab="profile">پروفایل و نشست‌ها</button>' \
        '<button data-atab="danger">منطقه‌ی خطر<span class="t-count">۴</span></button></div>'
    content += '<div class="a-panel active" id="settings-general" data-apanel="set" data-atab="general">' + general + '</div>'
    content += '<div class="a-panel" id="settings-roles" data-apanel="set" data-atab="roles">' + roles + '</div>'
    content += '<div class="a-panel" id="settings-profile" data-apanel="set" data-atab="profile">' + sessions + '</div>'
    content += '<div class="a-panel" id="settings-danger" data-apanel="set" data-atab="danger">' + dg + '</div>'
    return admin_page('تنظیمات سیستم', 'settings.html', 'تنظیمات سیستم', 'پیکربندی پلتفرم، نقش‌ها، پروفایل و منطقه‌ی خطر', content)

# ================================================================ build ====
def build_all():
    return [
        ('admin/index.html', build_index()),
        ('admin/users.html', build_users()),
        ('admin/organizations.html', build_organizations()),
        ('admin/subscriptions.html', build_subscriptions()),
        ('admin/revenue.html', build_revenue()),
        ('admin/api.html', build_api()),
        ('admin/activity.html', build_activity()),
        ('admin/support.html', build_support()),
        ('admin/notifications.html', build_notifications()),
        ('admin/content.html', build_content()),
        ('admin/flags.html', build_flags()),
        ('admin/security.html', build_security()),
        ('admin/settings.html', build_settings()),
    ]
