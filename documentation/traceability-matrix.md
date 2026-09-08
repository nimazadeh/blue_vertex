# ماتریس ردیابی نیازمندی‌ها (Traceability Matrix)

> هر نیازمندی محصول → صفحه/فایل پیاده‌ساز → ابزار آزمون → وضعیت.
> وضعیت‌ها: ✅ تأییدشده · 🔶 تأیید خودکار + بازبینی انسانی

---

## ۱. فهرست صفحات الزامی (Inventory)

| # | نیازمندی | مسیر صفحه | فایل مولد | تست | وضعیت |
|---|---|---|---|---|---|
| 1 | صفحه اصلی | `index.html` | `tools/marketing_home.py` | qa/smoke/audit | ✅ |
| 2 | امکانات | `pages/features.html` | `tools/marketing_pages.py` | qa/smoke/mobile | ✅ |
| 3 | راهکارها | `pages/solutions.html` | `tools/marketing_pages.py` | qa/smoke/mobile | ✅ |
| 4 | قیمت‌گذاری | `pages/pricing.html` | `tools/marketing_pages.py` | qa/smoke/mobile | ✅ |
| 5 | مشتریان | `pages/customers.html` | `tools/marketing_pages.py` | qa/smoke | ✅ |
| 6 | درباره ما | `pages/about.html` | `tools/marketing_pages.py` | qa/smoke | ✅ |
| 7 | تماس با ما | `pages/contact.html` | `tools/blog_contact.py` | qa/smoke/form | ✅ |
| 8 | وبلاگ (فهرست) | `pages/blog.html` | `tools/blog_contact.py` | qa/smoke/filter | ✅ |
| 9 | مقاله وبلاگ | `blog/article.html` | `tools/blog_contact.py` | qa/smoke | ✅ |
| 10 | خانه مستندات | `docs/index.html` | `tools/docs_content.py` | qa/smoke | ✅ |
| 11 | شروع سریع | `docs/getting-started.html` | `tools/docs_content.py` | qa/smoke | ✅ |
| 12 | احراز هویت | `docs/authentication.html` | `tools/docs_content.py` | qa/smoke | ✅ |
| 13 | مرجع API | `docs/api-reference.html` | `tools/docs_content.py` | qa/smoke | ✅ |
| 14 | SDKها | `docs/sdks.html` | `tools/docs_content2.py` | qa/smoke/code-tabs | ✅ |
| 15 | نمونه‌ها | `docs/examples.html` | `tools/docs_content2.py` | qa/smoke | ✅ |
| 16 | خطاها | `docs/errors.html` | `tools/docs_content2.py` | qa/smoke | ✅ |
| 17 | محدودیت‌ها | `docs/limits.html` | `tools/docs_content2.py` | qa/smoke | ✅ |
| 18 | سوالات متداول | `docs/faq.html` | `tools/docs_content2.py` | qa/smoke/accordion | ✅ |
| 19 | مفاهیم پروژه | `docs/projects.html` | `tools/docs_content2.py` | qa/smoke | ✅ |
| 20 | Webhookها | `docs/webhooks.html` | `tools/docs_content2.py` | qa/smoke | ✅ |
| 21 | API: کاربران | `docs/api/users.html` | `tools/docs_content2.py` | qa/smoke/prism | ✅ |
| 22 | API: پروژه‌ها | `docs/api/projects.html` | `tools/docs_content2.py` | qa/smoke/prism | ✅ |
| 23 | API: پرداخت‌ها | `docs/api/payments.html` | `tools/docs_content2.py` | qa/smoke/prism | ✅ |
| 24 | API: فایل‌ها | `docs/api/files.html` | `tools/docs_content2.py` | qa/smoke/prism | ✅ |
| 25 | تغییرات (Changelog) | `changelog/index.html` | `tools/misc.py` | qa/smoke/filter | ✅ |
| 26 | وضعیت سرویس | `status/index.html` | `tools/misc.py` | qa/smoke/filter | ✅ |
| 27 | ورود | `auth/login.html` | `tools/auth.py` | qa/smoke/form | ✅ |
| 28 | ثبت‌نام | `auth/register.html` | `tools/auth.py` | qa/smoke/form | ✅ |
| 29 | بازیابی رمز | `auth/forgot-password.html` | `tools/auth.py` | qa/smoke/form | ✅ |
| 30 | داشبورد: نمای کلی | `dashboard/index.html` | `tools/dash.py` | qa/smoke/charts | ✅ |
| 31 | داشبورد: کلیدهای API | `dashboard/api-keys.html` | `tools/dash2.py` | qa/smoke/modal | ✅ |
| 32 | داشبورد: مصرف | `dashboard/usage.html` | `tools/dash2.py` | qa/smoke/charts | ✅ |
| 33 | داشبورد: تحلیل‌ها | `dashboard/analytics.html` | `tools/dash2.py` | qa/smoke/charts | ✅ |
| 34 | داشبورد: گزارش درخواست‌ها | `dashboard/logs.html` | `tools/dash2.py` | qa/smoke/filter/drawer | ✅ |
| 35 | داشبورد: Endpointها | `dashboard/endpoints.html` | `tools/dash2.py` | qa/smoke/table | ✅ |
| 36 | داشبورد: SDK | `dashboard/sdk.html` | `tools/dash3.py` | qa/smoke/toast | ✅ |
| 37 | داشبورد: تیم | `dashboard/team.html` | `tools/dash3.py` | qa/smoke/modal | ✅ |
| 38 | داشبورد: صورتحساب | `dashboard/billing.html` | `tools/dash3.py` | qa/smoke/modal | ✅ |
| 39 | داشبورد: اعلان‌ها | `dashboard/notifications.html` | `tools/dash3.py` | qa/smoke/tabs | ✅ |
| 40 | داشبورد: تنظیمات | `dashboard/settings.html` | `tools/dash3.py` | qa/smoke/deep-link | ✅ |

**جمع: ۴۰ صفحه از ۴۰ — بدون هیچ صفحه‌ی جاافتاده.**

---

## ۲. نیازمندی‌های عمودی (Constraint Traceability)

| # | نیازمندی | پیاده‌سازی | آزمون | وضعیت |
|---|---|---|---|---|
| V1 | زبان فارسی تنها زبان UI | همه متن‌ها در فایل‌های مولد فارسی؛ ۰ متن لاتین UI | qa.py (توکن‌های ممنوع) + بازبینی اسکرین‌شات‌ها | ✅ |
| V2 | RTL پیش‌فرض | `<html lang="fa" dir="rtl">` روی همه صفحات | qa.py (بررسی lang/dir) | ✅ |
| V3 | ویژگی‌های منطقی CSS به‌جای left/right | `inset-inline-*`، `margin-inline`، `padding-inline`، `border-inline-end` | grep در CSS + ممیزی RTL | ✅ |
| V4 | جزیره‌های LTR برای محتوای فنی | `direction:ltr; unicode-bidi:isolate` روی کد/URL/متد/کلید/ایمیل/نسخه | بازبینی اسکرین‌شات + بازبینی کد | ✅ |
| V5 | فونت وزیرمتن محلی (woff2، ۴۰۰–۸۰۰، swap) | `assets/fonts/` × ۶ فایل + `@font-face` در base.css | audit.js (فونت لودشده per-page) + آفلاین‌فول (no CDN) | ✅ |
| V6 | کار آفلاین کامل — بدون CDN در runtime | همه کتابخانه‌ها در `assets/js/vendor/` | audit.js (`requestfailed` = ۰) + grep CDN | ✅ |
| V7 | اعداد فارسی در UI / لاتین در شناسه فنی | توابع `faNum/faDigits` در main.js؛ `method` و `code` با LTR | بازبینی اسکرین‌شات (۱۲۴٬۵۸۰، HTTP 200، v2.4.1) | ✅ |
| V8 | تاریخ شمسی | الگوریتم جلالی در main.js + تاریخ‌های نمونه شمسی در همه صفحات | smoke (faDateFull زنده) + بازبینی | ✅ |
| V9 | استاتیک: HTML/CSS/JS فقط | بدون فریم‌ورک، بدون بک‌اند | بازبینی ساختار + build.py | ✅ |
| V10 | کتابخانه فقط وقتی مفید | Chart.js، Lucide، Prism (همه vendored) | — | ✅ |
| V11 | استتیک سازمانی تیره | توکن‌های `#050505`/`#0A0A0A`/`#2563EB`/`#38BDF8` | بازبینی طراحی + اسکرین‌شات | ✅ |
| V12 | قیمت‌گذاری تومانی واقعی | ۹۹۰٬۰۰۰ / ۱٬۹۸۰٬۰۰۰ / ۳٬۹۰۰٬۰۰۰ تومان | بازبینی | ✅ |
| V13 | حالت تیره اصلی و کامل؛ بدون حالت روشن نیمه‌کاره | تنها تم کامل تیره؛ دکمه روشن از تنظیمات حذف شد | بازبینی | ✅ |
| V14 | بدون کپی از Vercel/Stripe/Supabase/Linear | طراحی اختصاصی (نام، ساختار، داده‌ها، چیدمان متفاوت) | بازبینی انسانی | ✅ |
| V15 | بدون TODO/placeholder/دکمه مرده | گیت qa.py (توکن‌های ممنوع) + audit (۰ خطای کنسول) | ✅ |
| V16 | همه حالت‌های UI (خالی/خطا/موفقیت/هشدار/لودینگ واقعی) | بخش ۷ design-system.md | بازبینی هر صفحه | ✅ |
| V17 | تعاملات شبیه‌سازی‌شده بدون بک‌اند | main.js (~۱۱۰۰ خط) + charts.js | smoke.js (۴۰ صفحه) | ✅ |
| V18 | داده‌های نمونه ایرانی معتبر | ابرینو، داده‌پرداز، هوشیار، فراز + اسامی و ایمیل‌های فارسی | بازبینی | ✅ |

---

## ۳. مسیر ابزار → نتیجه (آخرین اجرا)

| ابزار | دستور | نتیجه |
|---|---|---|
| گیت ساخت | `python3 tools/build.py` | ۴۰ صفحه، بدون خطا |
| کنترل کیفیت | `python3 tools/qa.py` | ۴۰ صفحه بررسی — ۰ خطا، ۰ هشدار |
| تست تعاملات | `node tools/smoke.js` | ALL SMOKE TESTS PASSED |
| ممیزی مرورگر | `node tools/audit.js` | ۰ خطای کنسول/صفحه، ۰ سرریز دسکتاپ، فونت کامل، ۰ تصویر خراب |
| ریسپانسیو موبایل | `node tools/mobile.js` | ۴۰/۴۰ صفحه بدون سرریز افقی در ۳۹۰px |
| دسترس‌پذیری | `node tools/a11y.js` | ۰ تصویر بدون alt، ۰ دکمه بی‌نام، ۰ ورودی بدون برچسب، ۰ پرش سلسله‌مراتب |
| حجم | `du -sh` (بدون tools/node_modules) | ~۲٫۲ مگابایت |

## ۴. موارد خارج از محدوده (صریح)

- هیچ بک‌اند، API واقعی، پرداخت واقعی یا ذخیره‌سازی داده وجود ندارد (دمو).
- هیچ حالت روشن (Light Mode) عرضه نمی‌شود — تصمیم محصول.
- هیچ صفحه‌ی دوزبانه EN/FA وجود ندارد — تصمیم محصول.
