# -*- coding: utf-8 -*-
"""Blue Vertex — build script.
Generates the complete static HTML product into ../ (blue-vertex/ root).
Usage: python3 tools/build.py
"""
import os, sys, io, re, datetime

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
SITE = 'https://bluevertex.ir/'
OUT = []

def _abs_canonical(rel_path, html):
    """turn relative canonical/og:url into absolute (SEO) URLs"""
    def repl(m):
        href = m.group(1)
        if href.startswith(('http', '#', '/')):
            return m.group(0)
        full = os.path.normpath(os.path.join(os.path.dirname(rel_path), href)).replace(os.sep, '/')
        return 'rel="canonical" href="%s%s"' % (SITE, full)
    def repl_og(m):
        href = m.group(1)
        if href.startswith(('http', '#', '/')):
            return m.group(0)
        full = os.path.normpath(os.path.join(os.path.dirname(rel_path), href)).replace(os.sep, '/')
        return 'property="og:url" content="%s%s"' % (SITE, full)
    html = re.sub(r'rel="canonical" href="([^"]+)"', repl, html)
    return re.sub(r'property="og:url" content="([^"]+)"', repl_og, html)

def emit(rel_path, html, out=OUT):
    html = _abs_canonical(rel_path, html)
    full = os.path.join(ROOT, rel_path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with io.open(full, 'w', encoding='utf-8') as f:
        f.write(html)
    OUT.append(rel_path)

def b():
    import marketing_home, marketing_pages, blog_contact, auth, docs_pages, docs_content, docs_content2, dash, dash2, dash3, misc, admin as admin_pages
    emit('index.html', marketing_home.build(''))
    emit('pages/features.html', marketing_pages.build_features('../'))
    emit('pages/solutions.html', marketing_pages.build_solutions('../'))
    emit('pages/pricing.html', marketing_pages.build_pricing('../'))
    emit('pages/customers.html', marketing_pages.build_customers('../'))
    emit('pages/about.html', marketing_pages.build_about('../'))
    emit('pages/contact.html', blog_contact.build_contact('../'))
    emit('pages/blog.html', blog_contact.build_blog('../'))
    emit('blog/article.html', blog_contact.build_article('../'))
    emit('auth/login.html', auth.build_login('../'))
    emit('auth/register.html', auth.build_register('../'))
    emit('auth/forgot-password.html', auth.build_forgot('../'))
    emit('docs/index.html', docs_content.build_docs_index('../'))
    emit('docs/getting-started.html', docs_content.build_getting_started('../'))
    emit('docs/authentication.html', docs_content.build_authentication('../'))
    emit('docs/api-reference.html', docs_content.build_api_reference('../'))
    emit('docs/api/users.html', docs_content2.build_users('../../'))
    emit('docs/api/projects.html', docs_content2.build_projects('../../'))
    emit('docs/api/payments.html', docs_content2.build_payments('../../'))
    emit('docs/api/files.html', docs_content2.build_files('../../'))
    emit('docs/sdks.html', docs_content2.build_sdks('../'))
    emit('docs/examples.html', docs_content2.build_examples('../'))
    emit('docs/errors.html', docs_content2.build_errors('../'))
    emit('docs/limits.html', docs_content2.build_limits('../'))
    emit('docs/faq.html', docs_content2.build_faq('../'))
    emit('docs/projects.html', docs_content2.build_projects_concept('../'))
    emit('docs/webhooks.html', docs_content2.build_webhooks('../'))
    emit('dashboard/index.html', dash.build_index('../'))
    emit('dashboard/api-keys.html', dash2.build_api_keys('../'))
    emit('dashboard/usage.html', dash2.build_usage('../'))
    emit('dashboard/analytics.html', dash2.build_analytics('../'))
    emit('dashboard/logs.html', dash2.build_logs('../'))
    emit('dashboard/endpoints.html', dash2.build_endpoints('../'))
    emit('dashboard/sdk.html', dash3.build_sdk('../'))
    emit('dashboard/team.html', dash3.build_team('../'))
    emit('dashboard/billing.html', dash3.build_billing('../'))
    emit('dashboard/notifications.html', dash3.build_notifications('../'))
    emit('dashboard/settings.html', dash3.build_settings('../'))
    emit('changelog/index.html', misc.build_changelog('../'))
    emit('status/index.html', misc.build_status('../'))
    for rel, html in admin_pages.build_all():
        emit(rel, html)
    emit('index.html', marketing_home.build(''))

def seo_extras():
    """robots.txt, sitemap.xml, 404.html — regenerated on every build."""
    public = [p for p in sorted(OUT) if not p.startswith(('admin/', 'dashboard/', 'auth/'))]
    today = datetime.date.today().isoformat()
    robots = ('User-agent: *\n'
              'Allow: /\n'
              'Disallow: /admin/\n'
              'Disallow: /dashboard/\n'
              'Disallow: /auth/\n'
              'Disallow: /dashboard/*#*\n'
              '\nSitemap: ' + SITE + 'sitemap.xml\n')
    with io.open(os.path.join(ROOT, 'robots.txt'), 'w', encoding='utf-8') as f:
        f.write(robots)
    urls = ''.join('  <url><loc>%s%s</loc><lastmod>%s</lastmod></url>\n' % (SITE, p, today) for p in public)
    sitemap = ('<?xml version="1.0" encoding="UTF-8"?>\n'
               '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
               + urls + '</urlset>\n')
    with io.open(os.path.join(ROOT, 'sitemap.xml'), 'w', encoding='utf-8') as f:
        f.write(sitemap)
    # 404 page (same chrome, noindex)
    from chrome import head
    body = '''<body class="noise">
<button class="fixed-theme-toggle" data-theme-toggle aria-label="تغییر حالت نمایش" title="حالت روشن"><i data-icon="sun"></i></button>
<div class="wrap" style="max-width:620px;margin:0 auto;padding:110px 22px;text-align:center">
  <div style="font-size:2.6rem;font-weight:800;letter-spacing:-.02em;margin-bottom:10px">۴۰۴</div>
  <p style="color:var(--text-3);font-size:var(--fs-sm);margin-bottom:28px;direction:rtl">صفحه‌ای که دنبالش بودید پیدا نشد؛ شاید آدرس تغییر کرده یا حذف شده باشد.</p>
  <div class="flex gap-8" style="justify-content:center">
    <a class="btn btn-primary" href="index.html">بازگشت به خانه</a>
    <a class="btn btn-ghost" href="pages/contact.html">تماس با پشتیبانی</a>
  </div>
</div>
</body></html>'''
    html = head('خطای ۴۰۴ — صفحه پیدا نشد', 'صفحه مورد نظر پیدا نشد.', '').replace('<meta name="robots" content="index, follow">', '<meta name="robots" content="noindex">')
    html = re.sub(r'<link rel="canonical"[^>]*>\n?', '', html)
    from chrome import scripts
    html += body.replace('</body>', scripts('') + '</body>')
    emit('404.html', html)

if __name__ == '__main__':
    b()
    seo_extras()
    print(f'generated {len(OUT)} pages')
    for p in sorted(OUT):
        print('  ', p)
