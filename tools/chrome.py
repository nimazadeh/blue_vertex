# -*- coding: utf-8 -*-
"""Blue Vertex — shared chrome (head / navbar / footer / sidebars / palette).
Generates identical, correctly-linked chrome for every page."""

FONT_BOOT = '<script>/* fonts under file:// — browsers block woff2 via CORS from origin null, so\n  inline the variable font as a data URI (last @font-face wins for all weights) */\n(function(){try{\n  if(location.protocol===\'file:\'){\n    var base=document.querySelector(\'link[rel="stylesheet"][href$="base.css"]\');\n    var l=document.createElement(\'link\');l.rel=\'stylesheet\';\n    l.href=(base?base.getAttribute(\'href\'):\'assets/css/base.css\').replace(/base\\.css$/,\'fonts-embed.css\');\n    document.head.appendChild(l);\n  }\n}catch(e){}})();</script>'

THEME_BOOT = "<script>/* theme bootstrap - runs before CSS paint to avoid flash */\n(function(){try{var q=(location.search.match(/[?&]theme=(light|dark)/i)||[])[1];var t=q||localStorage.getItem('bv-theme');if(t==='light'||t==='dark')document.documentElement.setAttribute('data-theme',t);}catch(e){}})();</script>"

TITLE_SUFFIX = ' — بلو ورتکس | پلتفرم توسعه‌دهنده فارسی'

def head(title, desc, prefix, extra_css='', extra_meta='', canonical=None, og_type='website'):
    css = f'{prefix}assets/css/'
    canon = canonical or (prefix + 'index.html')
    __THEME_BOOT = THEME_BOOT
    __FONT_BOOT = FONT_BOOT
    __html = f'''<!DOCTYPE html>'
<html lang="fa" dir="rtl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}{TITLE_SUFFIX}</title>
<meta name="description" content="{desc}">
<meta name="keywords" content="پلتفرم توسعه‌دهنده، API فارسی، داشبورد توسعه‌دهنده، مستندات API، SDK، Blue Vertex">
<meta name="robots" content="index, follow">
<link rel="canonical" href="{canon}">
<meta property="og:type" content="{og_type}">
<meta property="og:title" content="{title} — بلو ورتکس">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canon}">
<meta property="og:site_name" content="بلو ورتکس">
<meta property="og:image" content="https://bluevertex.ir/assets/og/og-cover.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:locale" content="fa_IR">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="https://bluevertex.ir/assets/og/og-cover.jpg">
<meta name="theme-color" content="#050505">
{__THEME_BOOT}
{extra_meta}
<link rel="icon" type="image/svg+xml" href="{css}../icons/favicon.svg">
<link rel="stylesheet" href="{css}base.css">
<link rel="stylesheet" href="{css}site.css">
<link rel="stylesheet" href="{css}docs.css">
<link rel="stylesheet" href="{css}dashboard.css">
{extra_css}
{__FONT_BOOT}
</head>
'''
    return __html

def announce(prefix=''):
    p = prefix
    return f'''<div class="announce">
  <span class="badge badge-blue">جدید</span>
  <span>نسخه ۲٫۴٫۰ منتشر شد؛ SDK پایتون با پشتیبانی کامل از تایپ منتشر شد.</span>
  <a href="{p}changelog/index.html">مشاهده تغییرات <span data-icon="chevron-left"></span></a>
</div>'''

NAV_LINKS = [
    ('خانه', 'index.html', 'active_home'),
    ('محصولات', None, 'mega_products'),
    ('مستندات', None, 'mega_docs'),
    ('تغییرات', 'changelog/index.html', 'active_changelog'),
    ('وبلاگ', 'pages/blog.html', 'active_blog'),
]

MEGA_PRODUCTS = [
    ('امکانات', 'pages/features.html', 'sparkles', 'هر آنچه برای ساخت محصول API نیاز دارید'),
    ('راهکارها', 'pages/solutions.html', 'layers', 'راهکار برای استارتاپ و سازمان'),
    ('قیمت‌گذاری', 'pages/pricing.html', 'credit-card', 'پلن شفاف و منعطف به تومان'),
    ('مشتریان', 'pages/customers.html', 'users', 'داستان شرکت‌هایی که با ما ساختند'),
    ('درباره ما', 'pages/about.html', 'building-2', 'تیم و فلسفه بلو استودیو'),
    ('تماس با ما', 'pages/contact.html', 'mail', 'گفتگو با تیم فروش'),
]

MEGA_DOCS = [
    ('شروع سریع', 'docs/getting-started.html', 'rocket', 'اولین درخواست در ۵ دقیقه'),
    ('احراز هویت', 'docs/authentication.html', 'shield-check', 'کلید API و مدیریت نشست'),
    ('مرجع کامل API', 'docs/api-reference.html', 'braces', 'پایان‌پوینت‌های /v1'),
    ('SDK رسمی', 'docs/sdks.html', 'package', 'جاوااسکریپت، پایتون، PHP، گو'),
    ('نمونه‌ها', 'docs/examples.html', 'code-2', 'کد آماده برای کپی'),
    ('خطاها و کدها', 'docs/errors.html', 'alert-triangle', 'رفع خطای رایج'),
]

def navbar(active, prefix):
    p = prefix
    ann = announce(p) if 'changelog' not in active else ''
    login = f'{p}auth/login.html'
    register = f'{p}auth/register.html'
    links = ''
    for label, href, key in NAV_LINKS:
        if href is None:
            act_cls = ' class="nav-link active"' if active == key.replace('mega_', 'active_') else ' class="nav-link"'
            if key == 'mega_products':
                items = ''.join(
                    f'<a class="mega-item" href="{p}{h}"><span class="icon-tile icon-tile-sm"><i data-icon="{ic}"></i></span><span><b class="mega-title">{t}</b><p>{d}</p></span></a>'
                    for t, h, ic, d in MEGA_PRODUCTS)
                links += f'''<div class="nav-item dropdown" data-dd><a{act_cls} href="#" data-dd-toggle>محصولات <span data-icon="chevron-down"></span></a>
  <div class="dropdown-menu nav-mega">{items}</div></div>'''
            else:
                items = ''.join(
                    f'<a class="mega-item" href="{p}{h}"><span class="icon-tile icon-tile-sm"><i data-icon="{ic}"></i></span><span><b class="mega-title">{t}</b><p>{d}</p></span></a>'
                    for t, h, ic, d in MEGA_DOCS)
                links += f'''<div class="nav-item dropdown" data-dd><a{act_cls} href="#" data-dd-toggle>مستندات <span data-icon="chevron-down"></span></a>
  <div class="dropdown-menu nav-mega">{items}</div></div>'''
        else:
            cls = ' class="nav-link active"' if active == key else ' class="nav-link"'
            links += f'<a{cls} href="{p}{href}">{label}</a>'
    return f'''{ann}
<header class="navbar">
  <div class="container-wide nav-inner">
    <a class="brand" href="{p}index.html" aria-label="بلو ورتکس">
      <span class="brand-mark"><i data-icon="zap"></i></span>
      <span class="brand-name">بلو ورتکس<small>BLUE VERTEX</small></span>
    </a>
    <nav class="nav-links" aria-label="ناوبری اصلی">{links}</nav>
    <div class="nav-cta">
      <button class="btn-icon theme-toggle" data-theme-toggle aria-label="تغییر حالت نمایش" title="حالت روشن"><i data-icon="sun"></i></button>
      <a class="btn btn-ghost nav-keep" href="{login}">ورود</a>
      <a class="btn btn-primary nav-keep" href="{register}">شروع کنید</a>
      <button class="nav-burger" data-mobile-open="mobileMenu" aria-label="باز کردن منو"><i data-icon="menu"></i></button>
    </div>
  </div>
</header>
<div class="mobile-menu" id="mobileMenu" role="dialog" aria-modal="true" aria-label="منوی موبایل">
  <div class="mobile-panel">
    <div class="flex-between">
      <a class="brand" href="{p}index.html"><span class="brand-mark"><i data-icon="zap"></i></span><span class="brand-name">بلو ورتکس<small>BLUE VERTEX</small></span></a>
      <button class="modal-close" data-mobile-close aria-label="بستن"><i data-icon="x"></i></button>
    </div>
    <div class="mobile-theme-row" style="display:flex;align-items:center;justify-content:space-between;padding:4px 22px 10px">
      <span class="t-caption" style="color:var(--text-3)">حالت نمایش</span>
      <button class="btn btn-outline btn-sm theme-toggle" data-theme-toggle aria-label="تغییر حالت نمایش"><i data-icon="sun"></i></button>
    </div>
    <nav class="mobile-links" aria-label="منوی موبایل">
      <a class="mobile-link" href="{p}index.html">خانه</a>
      <a class="mobile-link" href="{p}pages/features.html">امکانات</a>
      <a class="mobile-link" href="{p}pages/solutions.html">راهکارها</a>
      <a class="mobile-link" href="{p}pages/pricing.html">قیمت‌گذاری</a>
      <a class="mobile-link" href="{p}docs/index.html">مستندات</a>
      <a class="mobile-link" href="{p}changelog/index.html">تغییرات</a>
      <a class="mobile-link" href="{p}pages/blog.html">وبلاگ</a>
      <a class="mobile-link" href="{p}status/index.html">وضعیت سرویس</a>
      <a class="mobile-link" href="{p}auth/login.html">ورود به حساب</a>
    </nav>
    <div class="mobile-cta">
      <a class="btn btn-primary btn-block" href="{register}">شروع کنید — رایگان</a>
      <a class="btn btn-secondary btn-block" href="{p}auth/login.html">ورود</a>
    </div>
  </div>
</div>'''

def footer(prefix):
    p = prefix
    return f'''<footer class="footer">
  <div class="container-wide">
    <div class="footer-grid">
      <div>
        <a class="brand" href="{p}index.html">
          <span class="brand-mark"><i data-icon="zap"></i></span>
          <span class="brand-name">بلو ورتکس<small>BLUE VERTEX</small></span>
        </a>
        <p class="footer-desc">پلتفرم توسعه‌دهنده فارسی برای ساخت، مستندسازی و نظارت بر APIهای محصول شما؛ از استارتاپ تا سازمان.</p>
        <div class="newsletter">
          <input class="input" type="email" placeholder="ایمیل شما" aria-label="ایمیل برای خبرنامه">
          <button class="btn btn-primary btn-sm" data-newsletter type="button">عضویت</button>
        </div>
        <div class="footer-status mt-16"><span class="status-ind st-green"><span class="pulse"></span> همه سرویس‌ها فعال</span></div>
      </div>
      <div class="footer-col">
        <h2 class="footer-title">محصول</h2>
        <a href="{p}pages/features.html">امکانات</a>
        <a href="{p}pages/solutions.html">راهکارها</a>
        <a href="{p}pages/pricing.html">قیمت‌گذاری</a>
        <a href="{p}pages/customers.html">مشتریان</a>
        <a href="{p}changelog/index.html">تغییرات</a>
      </div>
      <div class="footer-col">
        <h2 class="footer-title">مستندات</h2>
        <a href="{p}docs/index.html">خانه مستندات</a>
        <a href="{p}docs/getting-started.html">شروع سریع</a>
        <a href="{p}docs/authentication.html">احراز هویت</a>
        <a href="{p}docs/api-reference.html">مرجع API</a>
        <a href="{p}docs/sdks.html">SDKها</a>
        <a href="{p}docs/faq.html">سوالات متداول</a>
      </div>
      <div class="footer-col">
        <h2 class="footer-title">توسعه‌دهندگان</h2>
        <a href="{p}dashboard/index.html">داشبورد</a>
        <a href="{p}dashboard/api-keys.html">کلیدهای API</a>
        <a href="{p}dashboard/logs.html">گزارش درخواست‌ها</a>
        <a href="{p}status/index.html">وضعیت سرویس</a>
        <a href="{p}docs/errors.html">خطاها</a>
      </div>
      <div class="footer-col">
        <h2 class="footer-title">شرکت</h2>
        <a href="{p}pages/about.html">درباره ما</a>
        <a href="{p}pages/blog.html">وبلاگ</a>
        <a href="{p}pages/contact.html">تماس با ما</a>
        <a href="{p}auth/register.html">ایجاد حساب</a>
        <a href="{p}auth/login.html">ورود</a>
      </div>
    </div>
    <div class="footer-bottom">
      <span>© ۱۴۰۵ بلو استودیو — Blue Studio. تمامی حقوق محفوظ است.</span>
      <span class="ltr" style="font-size:.72rem;color:var(--text-4)">Blue Vertex v2.4.1</span>
      <div class="footer-social">
        <a href="#" aria-label="گیت‌هاب"><i data-icon="github"></i></a>
        <a href="#" aria-label="لینکدین"><i data-icon="linkedin"></i></a>
        <a href="#" aria-label="تلگرام"><i data-icon="send"></i></a>
        <a href="#" aria-label="ایمیل"><i data-icon="mail"></i></a>
      </div>
    </div>
  </div>
</footer>'''

def palette(p):
    return f'''<div class="palette-backdrop" id="paletteBackdrop" role="dialog" aria-modal="true" aria-label="فرمان سریع">
  <div class="palette">
    <div class="palette-input-wrap">
      <span data-icon="search" style="display:flex"></span>
      <input id="paletteInput" class="palette-input" placeholder="جستجو در بلو ورتکس…" aria-label="جستجو">
      <button class="topbar-btn" data-palette-close style="display:none" aria-label="بستن"><i data-icon="x"></i></button>
      <span class="kbd">ESC</span>
    </div>
    <div class="palette-list" id="paletteList"></div>
    <div class="palette-foot">
      <span><span class="kbd">↑</span><span class="kbd">↓</span> حرکت</span>
      <span><span class="kbd">↵</span> انتخاب</span>
      <span style="margin-inline-start:auto;font-weight:700;color:var(--text-4)">Blue Vertex</span>
    </div>
  </div>
</div>'''

SEARCH_OVERLAY = '''<div class="search-view" id="docsSearch" role="dialog" aria-modal="true" aria-label="جستجو در مستندات">
  <div class="search-panel">
    <div class="search-header">
      <span style="display:flex;color:var(--text-3)" data-icon="search"></span>
      <input id="searchInput" placeholder="جستجو در مستندات، API و راهنماها…" aria-label="جستجو در مستندات">
      <span class="kbd">ESC</span>
    </div>
    <div class="search-filters" id="searchFilters">
      <button class="chip active" data-search-cat="all">همه</button>
      <button class="chip" data-search-cat="guide">راهنما</button>
      <button class="chip" data-search-cat="api">API</button>
      <button class="chip" data-search-cat="sdk">SDK</button>
      <button class="chip" data-search-cat="faq">سوالات</button>
    </div>
    <div class="search-recents" id="searchRecents"></div>
    <div class="search-results" id="searchResults"></div>
    <div id="searchEmpty" style="display:none">
      <div class="search-empty">
        <span style="display:inline-flex" data-icon="search-x"></span>
        <p>نتیجه‌ای پیدا نشد. عبارت دیگری را امتحان کنید.</p>
      </div>
    </div>
    <div class="search-foot">
      <span>برای جستجوی سریع، ⟨Ctrl⟩ + ⟨K⟩ را بزنید</span>
    </div>
  </div>
</div>'''

SEARCH_DATA_JS = '''<script>
window.BV_DOCS = [
  {title:'شروع سریع', url:'{p}docs/getting-started.html', cat:'guide', catLabel:'راهنما', icon:'rocket', desc:'اولین درخواست API در کمتر از ۵ دقیقه'},
  {title:'احراز هویت', url:'{p}docs/authentication.html', cat:'guide', catLabel:'راهنما', icon:'shield-check', desc:'تولید کلید API و ارسال هدر Authorization'},
  {title:'مرجع کامل API', url:'{p}docs/api-reference.html', cat:'api', catLabel:'API', icon:'braces', desc:'پایان‌پوینت‌های /v1 با نمونه درخواست و پاسخ'},
  {title:'پایان‌پوینت کاربران', url:'{p}docs/api/users.html', cat:'api', catLabel:'API', icon:'users', desc:'لیست، ساخت و ویرایش کاربران'},
  {title:'پایان‌پوینت پروژه‌ها', url:'{p}docs/api/projects.html', cat:'api', catLabel:'API', icon:'folder-kanban', desc:'مدیریت پروژه‌ها و اعضای تیم'},
  {title:'پایان‌پوینت پرداخت‌ها', url:'{p}docs/api/payments.html', cat:'api', catLabel:'API', icon:'credit-card', desc:'ایجاد و استعلام پرداخت'},
  {title:'پایان‌پوینت فایل‌ها', url:'{p}docs/api/files.html', cat:'api', catLabel:'API', icon:'file-text', desc:'بارگذاری و مدیریت فایل'},
  {title:'SDK رسمی', url:'{p}docs/sdks.html', cat:'sdk', catLabel:'SDK', icon:'package', desc:'JavaScript ،Python ،PHP و Go'},
  {title:'نمونه‌های کاربردی', url:'{p}docs/examples.html', cat:'guide', catLabel:'راهنما', icon:'code-2', desc:'سناریوهای آماده برای کپی'},
  {title:'کدهای خطا', url:'{p}docs/errors.html', cat:'guide', catLabel:'راهنما', icon:'alert-triangle', desc:'فهرست کامل خطاها و راه‌حل'},
  {title:'محدودیت‌ها و نرخ', url:'{p}docs/limits.html', cat:'guide', catLabel:'راهنما', icon:'gauge', desc:'محدودیت نرخ درخواست و سهمیه هر پلن'},
  {title:'سوالات متداول', url:'{p}docs/faq.html', cat:'faq', catLabel:'سوالات', icon:'help-circle', desc:'پاسخ پرسش‌های رایج توسعه‌دهندگان'},
  {title:'نصب', url:'{p}docs/getting-started.html#install', cat:'guide', catLabel:'راهنما', icon:'download', desc:'نصب SDK با npm و pip'},
  {title:'کلیدهای API', url:'{p}docs/authentication.html#keys', cat:'guide', catLabel:'راهنما', icon:'key-round', desc:'ساخت، چرخش و باطل‌سازی کلید'},
  {title:'Webhookها', url:'{p}docs/webhooks.html', cat:'guide', catLabel:'راهنما', icon:'webhook', desc:'رویدادها، امضا و تحویل مجدد'},
  {title:'خانه مستندات', url:'{p}docs/index.html', cat:'guide', catLabel:'راهنما', icon:'book-open', desc:'نقشه راه مستندات'}
];
</script>'''

def scripts(prefix, prism=False, charts=False, extra=''):
    p = prefix
    out = f'<script src="{p}assets/js/vendor/lucide.min.js"></script>\n'
    if prism:
        out += (f'<script src="{p}assets/js/vendor/prism-core.min.js"></script>\n'
                f'<script src="{p}assets/js/vendor/prism-clike.min.js"></script>\n'
                f'<script src="{p}assets/js/vendor/prism-javascript.min.js"></script>\n'
                f'<script src="{p}assets/js/vendor/prism-json.min.js"></script>\n'
                f'<script src="{p}assets/js/vendor/prism-bash.min.js"></script>\n'
                f'<script src="{p}assets/js/vendor/prism-python.min.js"></script>\n'
                f'<script src="{p}assets/js/vendor/prism-markup.min.js"></script>\n'
                f'<script src="{p}assets/js/vendor/prism-markup-templating.min.js"></script>\n'
                f'<script src="{p}assets/js/vendor/prism-php.min.js"></script>\n'
                f'<script src="{p}assets/js/vendor/prism-go.min.js"></script>\n'
                f'<script src="{p}assets/js/vendor/prism-css.min.js"></script>\n'
                f'<script src="{p}assets/js/vendor/prism-yaml.min.js"></script>\n'
                f'<script src="{p}assets/js/vendor/prism-line-numbers.min.js"></script>\n')
    if charts:
        out += f'<script src="{p}assets/js/vendor/chart.umd.js"></script>\n'
    out += f'<script src="{p}assets/js/main.js"></script>\n'
    if charts:
        out += f'<script src="{p}assets/js/charts.js"></script>\n'
    return out + extra

# ---------------------------------------------------------------- DOCS SIDEBAR
DOCS_NAV = [
    ('شروع کار', 'rocket', [
        ('معرفی', 'docs/index.html', 'book-open', ''),
        ('شروع سریع', 'docs/getting-started.html', 'zap', ''),
        ('نصب', 'docs/getting-started.html#install', 'download', ''),
    ]),
    ('مفاهیم', 'lightbulb', [
        ('احراز هویت', 'docs/authentication.html', 'shield-check', ''),
        ('پروژه‌ها', 'docs/projects.html', 'folder-kanban', ''),
        ('کلیدهای API', 'docs/authentication.html#keys', 'key-round', ''),
        ('Webhookها', 'docs/webhooks.html', 'webhook', ''),
    ]),
    ('API', 'braces', [
        ('معرفی API', 'docs/api-reference.html', 'book-open', ''),
        ('کاربران', 'docs/api/users.html', 'users', ''),
        ('پروژه‌ها', 'docs/api/projects.html', 'folder-kanban', ''),
        ('پرداخت‌ها', 'docs/api/payments.html', 'credit-card', ''),
        ('فایل‌ها', 'docs/api/files.html', 'file-text', ''),
    ]),
    ('SDK', 'package', [
        ('JavaScript', 'docs/sdks.html#js', 'braces', ''),
        ('Python', 'docs/sdks.html#py', 'braces', ''),
        ('PHP', 'docs/sdks.html#php', 'braces', ''),
        ('Go', 'docs/sdks.html#go', 'braces', ''),
    ]),
    ('راهنما', 'help-circle', [
        ('نمونه‌ها', 'docs/examples.html', 'code-2', ''),
        ('خطاها', 'docs/errors.html', 'alert-triangle', ''),
        ('محدودیت‌ها', 'docs/limits.html', 'gauge', ''),
        ('سوالات متداول', 'docs/faq.html', 'help-circle', ''),
    ]),
]

def docs_sidebar(current, prefix):
    p = prefix
    html = '<div class="docs-side"><div class="docs-side-inner">'
    for group_title, g_icon, items in DOCS_NAV:
        html += f'<div class="docs-group"><div class="docs-group-title"><i data-icon="{g_icon}"></i>{group_title}</div>'
        for label, href, icon, badge in items:
            act = ' active' if current == href else ''
            b = f'<span class="badge badge-blue" style="margin-inline-start:auto">{badge}</span>' if badge else ''
            html += f'<a class="docs-link{act}" href="{p}{href}"><span data-icon="{icon}"></span>{label}{b}</a>'
        html += '</div>'
    html += ('<div class="docs-group"><div class="docs-group-title"><i data-icon="life-buoy"></i>پشتیبانی</div>'
             f'<a class="docs-link" href="{p}status/index.html"><span data-icon="activity"></span>وضعیت سرویس</a>'
             f'<a class="docs-link" href="{p}pages/contact.html"><span data-icon="message-square"></span>تماس با پشتیبانی</a>'
             '</div></div></div>')
    return html

# ---------------------------------------------------------------- API SIDEBAR
API_NAV = [
    ('شروع', [
        ('مرجع API', 'docs/api-reference.html', 'book-open', 'get'),
    ]),
    ('کاربران', [
        ('GET  /v1/users', 'docs/api/users.html', 'users', 'get'),
        ('POST  /v1/users', 'docs/api/users.html#create', 'user-plus', 'post'),
        ('GET  /v1/users/:id', 'docs/api/users.html#show', 'user', 'get'),
        ('DELETE  /v1/users/:id', 'docs/api/users.html#delete', 'user-x', 'delete'),
    ]),
    ('پروژه‌ها', [
        ('GET  /v1/projects', 'docs/api/projects.html', 'folder-kanban', 'get'),
        ('POST  /v1/projects', 'docs/api/projects.html#create', 'folder-plus', 'post'),
    ]),
    ('پرداخت‌ها', [
        ('POST  /v1/payments', 'docs/api/payments.html', 'credit-card', 'post'),
        ('GET  /v1/payments/:id', 'docs/api/payments.html#show', 'receipt', 'get'),
        ('GET  /v1/payments', 'docs/api/payments.html#list', 'list', 'get'),
    ]),
    ('فایل‌ها', [
        ('POST  /v1/files', 'docs/api/files.html', 'upload-cloud', 'post'),
        ('GET  /v1/files/:id', 'docs/api/files.html#show', 'file-text', 'get'),
    ]),
]

def api_sidebar(current, prefix):
    p = prefix
    html = '<div class="api-side">'
    html += f'<div class="docs-group"><div class="docs-group-title"><i data-icon="braces"></i>مرجع API</div></div>'
    for group, items in API_NAV:
        html += f'<div class="docs-group" style="padding-top:14px"><div class="docs-group-title">{group}</div>'
        for label, href, icon, method in items:
            act = ' active' if current == href else ''
            path = label.split('  ')[-1] if '  ' in label else label
            html += (f'<a class="docs-link-sub{act}" href="{p}{href}">'
                     f'<span class="method method-{method}">{method}</span><span class="api-path">{path.strip()}</span></a>')
        html += '</div>'
    html += (f'<div class="docs-group" style="padding-top:14px"><div class="docs-group-title">عمومی</div>'
             f'<a class="docs-link {"" if current=="docs/api-reference.html" else ""}" href="{p}docs/api-reference.html">نمای کلی</a>'
             f'<a class="docs-link" href="{p}docs/errors.html">کدهای خطا</a>'
             f'<a class="docs-link" href="{p}docs/authentication.html">احراز هویت</a></div>'
             '</div>')
    return html

# ---------------------------------------------------------------- DASH SIDEBAR
DASH_NAV = [
    ('پیشخوان', [
        ('نمای کلی', 'dashboard/index.html', 'layout-dashboard', ''),
        ('کلیدهای API', 'dashboard/api-keys.html', 'key-round', ''),
        ('مصرف', 'dashboard/usage.html', 'gauge', ''),
        ('تحلیل‌ها', 'dashboard/analytics.html', 'bar-chart-3', ''),
        ('گزارش درخواست‌ها', 'dashboard/logs.html', 'scroll-text', 'red'),
    ]),
    ('ساخت و توسعه', [
        ('Endpointها', 'dashboard/endpoints.html', 'braces', ''),
        ('SDKها', 'dashboard/sdk.html', 'package', 'blue'),
    ]),
    ('مدیریت', [
        ('تیم', 'dashboard/team.html', 'users', ''),
        ('صورتحساب', 'dashboard/billing.html', 'credit-card', ''),
        ('اعلان‌ها', 'dashboard/notifications.html', 'bell', 'blue'),
        ('تنظیمات', 'dashboard/settings.html', 'settings', ''),
    ]),
]

def dash_sidebar(active, prefix):
    p = prefix
    html = f'''<aside class="dash-side" id="dashSide">
  <div class="side-brand">
    <a class="brand" href="{p}index.html"><span class="brand-mark"><i data-icon="zap"></i></span><span class="brand-name">بلو ورتکس<small>DEVELOPER CONSOLE</small></span></a>
    <button class="topbar-btn" style="margin-inline-start:auto" data-side-close aria-label="بستن منو" onclick="document.getElementById('dashSide').classList.remove('open');document.getElementById('sideBackdrop').classList.remove('show')"><i data-icon="x"></i></button>
  </div>
  <div class="dropdown side-ws" data-dd>
    <button type="button" style="width:100%;display:flex;align-items:center;gap:10px;text-align:start" data-dd-toggle>
      <span class="ws-avatar">ا</span>
      <span style="flex:1;min-width:0"><span class="ws-name">ابرینو</span><span class="ws-plan" style="display:block">پلن رشد</span></span>
      <span data-icon="chevrons-up-down" style="display:flex"></span>
    </button>
    <div class="ws-menu">
      <div class="menu-title">فضاهای کاری</div>
      <button class="menu-item" type="button"><span class="ws-avatar">ا</span>ابرینو<span class="badge badge-blue" style="margin-inline-start:auto">فعال</span></button>
      <button class="menu-item" type="button"><span class="ws-avatar" style="background:linear-gradient(135deg,#34D399,#065F46)">د</span>داده‌پرداز</button>
      <button class="menu-item" type="button"><span class="ws-avatar" style="background:linear-gradient(135deg,#A78BFA,#4C1D95)">ه</span>هوش‌یار</button>
      <div class="menu-sep"></div>
      <button class="menu-item" type="button"><span data-icon="plus" style="display:flex"></span>ایجاد فضای کاری جدید</button>
    </div>
  </div>
  <nav class="side-nav" aria-label="منوی داشبورد">'''
    for group_title, items in DASH_NAV:
        html += f'<div class="side-section-title">{group_title}</div>'
        for label, href, icon, badge in items:
            act = ' active' if active == href else ''
            b = f'<span class="side-badge {badge}">' + ('۳' if badge == 'blue' else '۱۲') + '</span>' if badge else ''
            html += f'<a class="side-link{act}" href="{p}{href}"><span data-icon="{icon}"></span>{label}{b}</a>'
    html += '''</nav>
  <div class="side-foot">
    <div class="side-upgrade">
      <b><i data-icon="sparkles"></i> ارتقای پلن</b>
      <p>۸۲٪ از سهمیه درخواست ماهانه مصرف شده است.</p>
      <div class="progress amber"><i style="width:82%" id="sideQuota"></i></div>
      <a class="btn btn-primary btn-sm btn-block mt-8" href="billing.html">ارتقا به سازمانی</a>
    </div>
  </div>
</aside>
<div class="side-backdrop" id="sideBackdrop"></div>'''
    return html

DASH_TOP = f'''<header class="dash-topbar">
  <button class="topbar-btn side-toggle" data-side-open aria-label="باز کردن منو"><i data-icon="panel-right"></i></button>
  <div class="topbar-breadcrumb">
    <span>ابرینو</span><span class="sep"><i data-icon="chevron-left"></i></span><b id="crumbHere">نمای کلی</b>
  </div>
  <div style="flex:1"></div>
  <button class="topbar-btn theme-toggle" data-theme-toggle aria-label="تغییر حالت نمایش" title="حالت روشن"><i data-icon="sun"></i></button>
  <button class="topbar-search" data-palette-open aria-label="جستجوی سریع">
    <i data-icon="search"></i>
    <span>جستجوی سریع…</span>
    <span class="kbd">Ctrl K</span>
  </button>
  <div class="dropdown" data-dd>
    <button class="topbar-btn" data-dd-toggle aria-label="اعلان‌ها"><i data-icon="bell"></i><span class="notif-dot"></span></button>
    <div class="dropdown-menu" style="width:320px">
      <div class="menu-title">اعلان‌ها</div>
      <a class="menu-item" href="notifications.html"><span style="flex:1;min-width:0"><b style="color:var(--text-1);font-size:var(--fs-caption)">۳ اعلان جدید</b><span style="display:block;font-size:.66rem;color:var(--text-4)">مشاهده همه اعلان‌ها</span></span></a>
      <div class="menu-sep"></div>
      <a class="menu-item" href="notifications.html"><i data-icon="shield-alert" style="color:var(--amber)"></i>کلید API جدید ساخته شد</a>
      <a class="menu-item" href="billing.html"><i data-icon="credit-card"></i>صورتحساب مرداد صادر شد</a>
    </div>
  </div>
  <div class="dropdown" data-dd>
    <button class="topbar-user" data-dd-toggle aria-label="پروفایل کاربر">
      <span class="avatar avatar-sm">س</span>
      <span class="u-info"><span class="u-name">سارا احمدی</span><span class="u-mail">sara@abrino.ir</span></span>
      <i data-icon="chevron-down" class="chev"></i>
    </button>
    <div class="dropdown-menu">
      <div class="menu-title">sara@abrino.ir</div>
      <a class="menu-item" href="settings.html"><i data-icon="user"></i>پروفایل</a>
      <a class="menu-item" href="settings.html#panel-security"><i data-icon="shield"></i>امنیت و ورود</a>
      <a class="menu-item" href="settings.html"><i data-icon="palette"></i>ظاهر</a>
      <div class="menu-sep"></div>
      <a class="menu-item" href="../docs/index.html"><i data-icon="book-open"></i>مستندات</a>
      <a class="menu-item" href="../status/index.html"><i data-icon="activity"></i>وضعیت سرویس</a>
      <div class="menu-sep"></div>
      <a class="menu-item danger" href="../index.html"><i data-icon="log-out"></i>خروج از حساب</a>
    </div>
  </div>
</header>'''

TOAST_REGION = '<div class="toast-region" aria-live="polite"></div>'

SCRIPT_DASH_BOOT = '''<script>
(function(){
  var crumb = document.getElementById('crumbHere');
  var href = location.pathname.split('/').pop();
  document.getElementById('sideBackdrop').addEventListener('click', function(){});
})();
</script>'''
