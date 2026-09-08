/* ==========================================================================
   BLUE VERTEX — ADMIN CONSOLE — admin-data.js
   Single source of truth for ALL mock entities of the Admin Console.
   Any real backend can replace these arrays later (UI stays untouched):
   window.ADMIN.users / orgs / subs / invoices / payments / tickets /
   incidents / flags / security / audit / notifications / content / charts
   ========================================================================== */
(function () {
  'use strict';

  /* ---------------------------------------------------------- people ----- */
  var USERS = [
    { id: 'usr_82K9Q1', name: 'سارا احمدی',   email: 'sara@abrino.ir',     org: 'org_7F31A2', plan: 'رشد',      status: 'active',   joined: '۱۴ مهر ۱۴۰۳', last: 'همین حالا',          mrr: 1490000, req30: 1834000, err30: 214, twofa: true,  sessions: 3 },
    { id: 'usr_4M7X2B', name: 'علی رضایی',    email: 'ali@dadehpardaz.ir', org: 'org_2B8C4D', plan: 'حرفه‌ای',  status: 'active',   joined: '۲ آذر ۱۴۰۳', last: '۱۲ دقیقه پیش',       mrr: 3490000, req30: 4120000, err30: 389, twofa: true,  sessions: 2 },
    { id: 'usr_9T1N5F', name: 'نگار موسوی',   email: 'negar@hooshyar.ir',  org: 'org_9D1E6F', plan: 'رشد',      status: 'active',   joined: '۱۸ بهمن ۱۴۰۳', last: '۴۰ دقیقه پیش',       mrr: 1490000, req30: 987000,  err30: 97,  twofa: false, sessions: 1 },
    { id: 'usr_5G8H3J', name: 'امیر حسینی',   email: 'amir@faraz.io',      org: 'org_4E5F8A', plan: 'پایه',     status: 'trial',    joined: '۵ خرداد ۱۴۰۵', last: '۳ ساعت پیش',         mrr: 0,       req30: 45200,   err30: 31,  twofa: false, sessions: 1 },
    { id: 'usr_2K6L4M', name: 'رضا قاسمی',    email: 'reza@shabakeno.ir',  org: 'org_6A3B7C', plan: 'سازمانی',  status: 'active',   joined: '۲۶ اسفند ۱۴۰۲', last: '۲ ساعت پیش',       mrr: 9900000, req30: 9210000, err30: 1021, twofa: true, sessions: 5 },
    { id: 'usr_8N3P7Q', name: 'الهام شریفی',  email: 'elham@paiesh.ir',    org: 'org_3C8D9E', plan: 'رشد',      status: 'active',   joined: '۹ تیر ۱۴۰۴', last: 'دیروز',             mrr: 1490000, req30: 1240000, err30: 156, twofa: true,  sessions: 2 },
    { id: 'usr_6R2S8T', name: 'حسین نادری',   email: 'hossein@rayanesh.ir',org: 'org_8F1A2B', plan: 'حرفه‌ای',  status: 'suspended',joined: '۳۱ فروردین ۱۴۰۴', last: '۶ روز پیش',        mrr: 3490000, req30: 0,       err30: 0,   twofa: true,  sessions: 0 },
    { id: 'usr_3V5W1X', name: 'فاطمه رحیمی',  email: 'fatemeh@abrino.ir',  org: 'org_7F31A2', plan: 'رشد',      status: 'active',   joined: '۲۲ مرداد ۱۴۰۴', last: '۵ دقیقه پیش',       mrr: 1490000, req30: 1610000, err30: 189, twofa: false, sessions: 2 },
    { id: 'usr_7Y9Z4C', name: 'پارسا کاظمی',  email: 'parsa@datapardaz.ir',org: 'org_2B8C4D', plan: 'پایه',     status: 'active',   joined: '۱۷ مهر ۱۴۰۴', last: '۱ روز پیش',          mrr: 0,       req30: 128000,  err30: 64,  twofa: false, sessions: 1 },
    { id: 'usr_1A2B3D', name: 'مهدی توکلی',   email: 'mehdi@hooshyar.ir',  org: 'org_9D1E6F', plan: 'پایه',     status: 'churned',  joined: '۱۱ آذر ۱۴۰۳', last: '۳۸ روز پیش',        mrr: 0,       req30: 0,       err30: 0,   twofa: false, sessions: 0 },
    { id: 'usr_4C5D6F', name: 'یاسمن عبادی',  email: 'yasaman@faraz.io',   org: 'org_4E5F8A', plan: 'رشد',      status: 'active',   joined: '۳۰ مهر ۱۴۰۴', last: '۲۰ دقیقه پیش',       mrr: 1490000, req30: 763000,  err30: 88,  twofa: true,  sessions: 1 },
    { id: 'usr_8E7F9G', name: 'نوید صادقی',   email: 'navid@shabakeno.ir', org: 'org_6A3B7C', plan: 'حرفه‌ای',  status: 'past_due', joined: '۱۴ اردیبهشت ۱۴۰۳', last: '۱۶ روز پیش',  mrr: 3490000, req30: 640000,  err30: 130, twofa: false, sessions: 1 }
  ];

  /* -------------------------------------------------------- companies --- */
  var ORGS = [
    { id: 'org_7F31A2', name: 'ابرینو',     owner: 'سارا احمدی',  plan: 'رشد',     members: 6,  mrr: 2980000,  req30: 3444000, err30: 403,  status: 'active',   created: '۱۴ مهر ۱۴۰۳', risk: 'low' },
    { id: 'org_2B8C4D', name: 'داده‌پرداز', owner: 'علی رضایی',   plan: 'حرفه‌ای', members: 11, mrr: 6980000,  req30: 4248000, err30: 453,  status: 'active',   created: '۲ آذر ۱۴۰۳',  risk: 'low' },
    { id: 'org_9D1E6F', name: 'هوش‌یار',    owner: 'نگار موسوی',  plan: 'رشد',     members: 4,  mrr: 1490000,  req30: 987000,  err30: 97,   status: 'active',   created: '۱۸ بهمن ۱۴۰۳', risk: 'low' },
    { id: 'org_4E5F8A', name: 'فراز',       owner: 'امیر حسینی',  plan: 'پایه',    members: 2,  mrr: 0,         req30: 45200,   err30: 31,   status: 'trial',   created: '۵ خرداد ۱۴۰۵', risk: 'medium' },
    { id: 'org_6A3B7C', name: 'شبکه‌نو',    owner: 'رضا قاسمی',   plan: 'سازمانی', members: 23, mrr: 19800000, req30: 9210000, err30: 1021, status: 'active',   created: '۲۶ اسفند ۱۴۰۲', risk: 'medium' },
    { id: 'org_3C8D9E', name: 'پایش',       owner: 'الهام شریفی', plan: 'رشد',     members: 5,  mrr: 1490000,  req30: 1240000, err30: 156,  status: 'active',   created: '۹ تیر ۱۴۰۴',  risk: 'low' },
    { id: 'org_8F1A2B', name: 'رایانش',     owner: 'حسین نادری',  plan: 'حرفه‌ای', members: 3,  mrr: 3490000,  req30: 0,       err30: 0,    status: 'suspended',created: '۳۱ فروردین ۱۴۰۴', risk: 'critical' },
    { id: 'org_5E2F3G', name: 'کدینو',      owner: '—',           plan: 'پایه',    members: 1,  mrr: 0,         req30: 0,       err30: 0,    status: 'churned',  created: '۱۹ آبان ۱۴۰۳', risk: 'none' }
  ];

  /* ------------------------------------------------------ subscriptions -- */
  var SUBS = [
    { id: 'sub_1A2B', user: 'usr_82K9Q1', org: 'org_7F31A2', orgName: 'ابرینو',     plan: 'رشد',     price: 1490000, status: 'active',   since: '۱۴ مهر ۱۴۰۳', renew: '۱۴ مهر ۱۴۰۵', usage: 68,  pay: 'paid' },
    { id: 'sub_2C3D', user: 'usr_4M7X2B', org: 'org_2B8C4D', orgName: 'داده‌پرداز', plan: 'حرفه‌ای', price: 3490000, status: 'active',   since: '۲ آذر ۱۴۰۳',  renew: '۲ آذر ۱۴۰۵',  usage: 84,  pay: 'paid' },
    { id: 'sub_3E4F', user: 'usr_9T1N5F', org: 'org_9D1E6F', orgName: 'هوش‌یار',    plan: 'رشد',     price: 1490000, status: 'active',   since: '۱۸ بهمن ۱۴۰۳', renew: '۱۸ بهمن ۱۴۰۵', usage: 41, pay: 'paid' },
    { id: 'sub_4G5H', user: 'usr_5G8H3J', org: 'org_4E5F8A', orgName: 'فراز',       plan: 'پایه',    price: 0,       status: 'trialing', since: '۵ خرداد ۱۴۰۵',  renew: '۵ شهریور ۱۴۰۵', usage: 12, pay: 'none' },
    { id: 'sub_5J6K', user: 'usr_2K6L4M', org: 'org_6A3B7C', orgName: 'شبکه‌نو',    plan: 'سازمانی', price: 9900000, status: 'active',   since: '۲۶ اسفند ۱۴۰۲', renew: '۲۶ اسفند ۱۴۰۵', usage: 92, pay: 'paid' },
    { id: 'sub_6L7M', user: 'usr_8N3P7Q', org: 'org_3C8D9E', orgName: 'پایش',       plan: 'رشد',     price: 1490000, status: 'active',   since: '۹ تیر ۱۴۰۴',  renew: '۹ تیر ۱۴۰۵',  usage: 57,  pay: 'paid' },
    { id: 'sub_7N8P', user: 'usr_6R2S8T', org: 'org_8F1A2B', orgName: 'رایانش',     plan: 'حرفه‌ای', price: 3490000, status: 'canceled', since: '۳۱ فروردین ۱۴۰۴', renew: '—', usage: 0, pay: 'failed' },
    { id: 'sub_8Q9R', user: 'usr_8E7F9G', org: 'org_6A3B7C', orgName: 'شبکه‌نو',    plan: 'حرفه‌ای', price: 3490000, status: 'past_due', since: '۱۴ اردیبهشت ۱۴۰۳', renew: '۱۴ اردیبهشت ۱۴۰۵', usage: 51, pay: 'failed' },
    { id: 'sub_9S1T', user: 'usr_1A2B3D', org: 'org_9D1E6F', orgName: 'هوش‌یار',    plan: 'پایه',    price: 0,       status: 'canceled', since: '۱۱ آذر ۱۴۰۳', renew: '—', usage: 0, pay: 'none' },
    { id: 'sub_2U3V', user: 'usr_3V5W1X', org: 'org_7F31A2', orgName: 'ابرینو',     plan: 'رشد',     price: 1490000, status: 'active',   since: '۲۲ مرداد ۱۴۰۴', renew: '۲۲ مرداد ۱۴۰۵', usage: 73, pay: 'pending' }
  ];

  var INVOICES = [
    { id: 'INV-۱۴۰۵-۰۸۱', org: 'org_6A3B7C', orgName: 'شبکه‌نو', amount: 9900000, status: 'paid',    issue: '۱ شهریور ۱۴۰۵', due: '۸ شهریور ۱۴۰۵' },
    { id: 'INV-۱۴۰۵-۰۸۰', org: 'org_2B8C4D', orgName: 'داده‌پرداز', amount: 3490000, status: 'paid',    issue: '۱ شهریور ۱۴۰۵', due: '۸ شهریور ۱۴۰۵' },
    { id: 'INV-۱۴۰۵-۰۷۹', org: 'org_7F31A2', orgName: 'ابرینو', amount: 2980000, status: 'paid',     issue: '۱ شهریور ۱۴۰۵', due: '۸ شهریور ۱۴۰۵' },
    { id: 'INV-۱۴۰۵-۰۷۸', org: 'org_8F1A2B', orgName: 'رایانش', amount: 3490000, status: 'failed',   issue: '۱ شهریور ۱۴۰۵', due: '۸ شهریور ۱۴۰۵' },
    { id: 'INV-۱۴۰۵-۰۷۷', org: 'org_3C8D9E', orgName: 'پایش', amount: 1490000, status: 'paid',      issue: '۱ شهریور ۱۴۰۵', due: '۸ شهریور ۱۴۰۵' },
    { id: 'INV-۱۴۰۵-۰۷۶', org: 'org_9D1E6F', orgName: 'هوش‌یار', amount: 1490000, status: 'pending',  issue: '۱ شهریور ۱۴۰۵', due: '۱۵ شهریور ۱۴۰۵' },
    { id: 'INV-۱۴۰۵-۰۶۱', org: 'org_6A3B7C', orgName: 'شبکه‌نو', amount: 9900000, status: 'paid',     issue: '۱ مرداد ۱۴۰۵',  due: '۸ مرداد ۱۴۰۵' },
    { id: 'INV-۱۴۰۵-۰۶۰', org: 'org_2B8C4D', orgName: 'داده‌پرداز', amount: 3490000, status: 'refunded',issue: '۱ مرداد ۱۴۰۵', due: '۸ مرداد ۱۴۰۵' }
  ];

  var PAYMENTS = [
    { id: 'tx_92KLM8', org: 'org_6A3B7C', orgName: 'شبکه‌نو',   amount: 9900000, status: 'success', method: 'زرین‌پال',  at: '۱ شهریور ۱۴۰۵ · ۰۹:۱۲', fail: null },
    { id: 'tx_18QWR4', org: 'org_2B8C4D', orgName: 'داده‌پرداز', amount: 3490000, status: 'success', method: 'کارت',      at: '۱ شهریور ۱۴۰۵ · ۰۹:۰۴', fail: null },
    { id: 'tx_67ZPT9', org: 'org_7F31A2', orgName: 'ابرینو',   amount: 2980000, status: 'success', method: 'کارت',      at: '۱ شهریور ۱۴۰۵ · ۰۸:۵۸', fail: null },
    { id: 'tx_41HNM7', org: 'org_8F1A2B', orgName: 'رایانش',   amount: 3490000, status: 'failed',  method: 'کارت',      at: '۱ شهریور ۱۴۰۵ · ۰۸:۴۱', fail: 'کد امنیتی نامعتبر (CVV2) — ۳ تلاش ناموفق' },
    { id: 'tx_05CTB2', org: 'org_3C8D9E', orgName: 'پایش',     amount: 1490000, status: 'success', method: 'زرین‌پال',  at: '۱ شهریور ۱۴۰۵ · ۰۸:۳۵', fail: null },
    { id: 'tx_73RLG6', org: 'org_9D1E6F', orgName: 'هوش‌یار',  amount: 1490000, status: 'pending', method: 'واریز',     at: '۱ شهریور ۱۴۰۵ · ۰۸:۲۰', fail: null },
    { id: 'tx_29JWD8', org: 'org_6A3B7C', orgName: 'شبکه‌نو',   amount: 9900000, status: 'refunded',method: 'زرین‌پال',  at: '۲۶ مرداد ۱۴۰۵ · ۱۴:۰۲', fail: 'درخواست مشتری — استفاده نشد' },
    { id: 'tx_54PQK1', org: 'org_2B8C4D', orgName: 'داده‌پرداز', amount: 3490000, status: 'failed',  method: 'کارت',      at: '۲۹ تیر ۱۴۰۵ · ۱۱:۴۷', fail: 'موجودی کافی نیست (NSF)' },
    { id: 'tx_88XNM3', org: 'org_6A3B7C', orgName: 'شبکه‌نو',   amount: 9900000, status: 'success', method: 'کارت',      at: '۱ مرداد ۱۴۰۵ · ۰۹:۰۱',  fail: null },
    { id: 'tx_12BVH5', org: 'org_5E2F3G', orgName: 'کدینو',    amount: 0,       status: 'failed',  method: 'کارت',      at: '۱۹ آبان ۱۴۰۳ · ۱۰:۲۲', fail: 'کارت مسدود' }
  ];

  var TICKETS = [
    { id: 'TKT-۱۰۴۲', org: 'org_6A3B7C', orgName: 'شبکه‌نو',   user: 'رضا قاسمی',  subject: 'بروز خطای 429 در حین پردازش دسته‌ای',  priority: 'critical', status: 'urgent',  owner: 'مریم کریمی', last: '۱۸ دقیقه پیش', created: '۳۱ مرداد ۱۴۰۵',
      notes: [ { who: 'رضا قاسمی', role: 'user', t: '۳۱ مرداد · ۱۴:۲۰', text: 'از ساعت ۱۴:۱۰ همه‌ی فراخوانی‌های دسته‌ای به 429 می‌خورند. حد نرخ ما 1000 در دقیقه است اما از ۲۰۰ شروع شده.' },
               { who: 'مریم کریمی', role: 'agent', t: '۳۱ مرداد · ۱۴:۳۵', text: 'سهمیه‌ی سازمان ۹۲٪ مصرف شده و حد نرخ لحظه‌ای برای پلن سازمانی ۷۵۰ در دقیقه است. در حال بررسی لاگ هستم.' },
               { who: 'مریم کریمی', role: 'note', t: '۳۱ مرداد · ۱۴:۴۱', text: 'پیشنهاد: افزایش موقت حد نرخ تا ۱۵۰۰ به مدت ۲۴ ساعت (نیاز به تأیید مدیر مالی).' } ] },
    { id: 'TKT-۱۰۴۱', org: 'org_2B8C4D', orgName: 'داده‌پرداز', user: 'علی رضایی',  subject: 'عدم دریافت Webhook پرداخت', priority: 'high', status: 'wait_customer', owner: 'علی توحیدی', last: '۲ ساعت پیش', created: '۳۰ مرداد ۱۴۰۵',
      notes: [ { who: 'علی رضایی', role: 'user', t: '۳۰ مرداد · ۱۰:۰۵', text: 'پیام‌های Webhook بعد از ساعت ۱۰:۰۰ امروز به دست ما نمی‌رسد.' },
               { who: 'علی توحیدی', role: 'agent', t: '۳۰ مرداد · ۱۰:۳۰', text: 'آدرس endpoint شما IP ثابت ندارد و رتبه‌ی ارسال‌ها ۴۸ است؛ لطفاً IP ثابت را فعال کنید.' } ] },
    { id: 'TKT-۱۰۴۰', org: 'org_8F1A2B', orgName: 'رایانش',   user: 'حسین نادری',  subject: 'درخواست بازگشت وجه دوره‌ی اخیر', priority: 'medium', status: 'open', owner: '—', last: '۶ ساعت پیش', created: '۲۸ مرداد ۱۴۰۵',
      notes: [ { who: 'حسین نادری', role: 'user', t: '۲۸ مرداد · ۱۶:۱۲', text: 'حساب ما به دلیل خطای بانکی تعلیق شده؛ لطفاً مبلغ دوره‌ی مرداد بازگردانده شود.' } ] },
    { id: 'TKT-۱۰۳۹', org: 'org_7F31A2', orgName: 'ابرینو',   user: 'فاطمه رحیمی', subject: 'راهنمای اتصال SDK پایتون', priority: 'low', status: 'resolved', owner: 'سمیه کاظمی', last: 'دیروز', created: '۲۶ مرداد ۱۴۰۵',
      notes: [ { who: 'فاطمه رحیمی', role: 'user', t: '۲۶ مرداد · ۱۲:۰۰', text: 'در نصب SDK خطای SSL می‌گیرم.' },
               { who: 'سمیه کاظمی', role: 'agent', t: '۲۶ مرداد · ۱۲:۴۰', text: 'پروکسی سازمان شما گواهی را رد می‌کند؛ از متغیر محیطی BV_CA_BUNDLE استفاده کنید.' },
               { who: 'سمیه کاظمی', role: 'agent', t: '۲۶ مرداد · ۱۲:۴۱', text: 'بسته شد — کاربر تأیید کرد.' } ] },
    { id: 'TKT-۱۰۳۸', org: 'org_3C8D9E', orgName: 'پایش',     user: 'الهام شریفی', subject: 'افزایش سهمیه‌ی توکن مدل هوش مصنوعی', priority: 'medium', status: 'open', owner: 'علی توحیدی', last: '۲ روز پیش', created: '۲۵ مرداد ۱۴۰۵',
      notes: [ { who: 'الهام شریفی', role: 'user', t: '۲۵ مرداد · ۰۹:۱۵', text: 'سهمیه‌ی مدل ما برای ۳ روز دیگر کافی است. امکان خرید افزونه هست؟' } ] },
    { id: 'TKT-۱۰۳۷', org: 'org_9D1E6F', orgName: 'هوش‌یار',  user: 'نگار موسوی',  subject: 'گزارش خطای 500 متناوب در /v1/summaries', priority: 'high', status: 'wait_support', owner: 'مریم کریمی', last: '۳ روز پیش', created: '۲۴ مرداد ۱۴۰۵',
      notes: [ { who: 'نگار موسوی', role: 'user', t: '۲۴ مرداد · ۱۳:۳۰', text: 'حدود ۲٪ درخواست‌ها 500 می‌گیرند.' },
               { who: 'مریم کریمی', role: 'note', t: '۲۴ مرداد · ۱۴:۱۰', text: 'مربوط به نمونه‌برداری دمای بالای GPU در مدل خلاصه‌سازی است. issue داخلی ثبت شد.' } ] },
    { id: 'TKT-۱۰۳۶', org: 'org_5E2F3G', orgName: 'کدینو',   user: '—',           subject: 'درخواست حذف حساب', priority: 'low', status: 'resolved', owner: 'سمیه کاظمی', last: '۱۲ روز پیش', created: '۱۹ مرداد ۱۴۰۵',
      notes: [ { who: 'صاحب حساب', role: 'user', t: '۱۹ مرداد · ۱۱:۰۰', text: 'لطفاً حساب و داده‌های ما حذف شود.' },
               { who: 'سمیه کاظمی', role: 'agent', t: '۱۹ مرداد · ۱۱:۲۵', text: 'حذف انجام شد. رسید: AUD-۲۹۴۱' } ] }
  ];

  var INCIDENTS = [
    { id: 'inc_7A', title: 'کندی مقطعی پردازش صف گزارش‌گیری', severity: 'medium', service: 'Queue', started: 'امروز · ۱۰:۴۰', duration: '۱ ساعت و ۲۰ دقیقه', status: 'active', team: 'زیرساخت', desc: 'تأخیر صف پردازش گزارش‌های سنگین بالای ۹۰ ثانیه رفت؛ کاربران متأثر: ۳ سازمان. سرویس اصلی API سالم است.' },
    { id: 'inc_6B', title: 'خطای 5xx متناوب در هوش مصنوعی', severity: 'high', service: 'AI Gateway', started: 'دیروز · ۲۳:۱۰', duration: '۴۵ دقیقه', status: 'monitoring', team: 'هوش مصنوعی', desc: 'نمونه‌برداری دمای GPU باعث ۲٪ خطای 5xx شد؛ به حالت مانیتورینگ رفت و در حال جمع‌بندی گزارش است.' },
    { id: 'inc_5C', title: 'پرداخت‌های ناموفق درگاه کارت', severity: 'critical', service: 'Billing', started: '۳۱ مرداد · ۰۸:۴۰', duration: '۲ ساعت', status: 'resolved', team: 'مالی', desc: 'پاسخی از سرویس صادرکننده‌ی توکن کارت نرسید؛ با تغییر مسیر به درگاه دوم، همه‌ی پرداخت‌ها بازیابی شدند.' },
    { id: 'inc_4D', title: 'تأخیر ارسال Webhook', severity: 'low', service: 'Webhooks', started: '۲۹ مرداد · ۰۲:۱۵', duration: '۳۵ دقیقه', status: 'resolved', team: 'زیرساخت', desc: 'صف تلاش مجدد مسدود شده بود؛ پس از پاک‌سازی صف، ۱۰۰٪ پیام‌ها ارسال شدند.' }
  ];

  var FLAGS = [
    { id: 'ff_new_checkout', name: 'درگاه پرداخت جدید',      key: 'new_checkout',   env: 'production', on: true,  rollout: 100, created: '۲۱ تیر ۱۴۰۵', changed: '۲ روز پیش',  owner: 'مریم کریمی', desc: 'درگاه پرداخت بازطراحی‌شده با پشتیبانی از رمز پویا.' },
    { id: 'ff_ai_summaries', name: 'خلاصه‌ساز هوشمند',        key: 'ai_summaries',   env: 'production', on: true,  rollout: 25,  created: '۱۲ مرداد ۱۴۰۵', changed: '۱ روز پیش', owner: 'مریم کریمی', desc: 'خلاصه‌سازی خودکار لاگ‌ها برای پلن‌های حرفه‌ای و بالاتر.' },
    { id: 'ff_rate_v2',      name: 'موتور محدودیت نرخ نسخه ۲', key: 'rate_limit_v2', env: 'staging',   on: true,  rollout: 100, created: '۵ مرداد ۱۴۰۵', changed: '۳ روز پیش', owner: 'علی توحیدی', desc: 'حد نرخ سازگار با شیدی و بودجه‌ی لحظه‌ای.' },
    { id: 'ff_smart_retry',  name: 'تلاش مجدد هوشمند',        key: 'smart_retry',    env: 'production', on: true,  rollout: 50,  created: '۲۸ خرداد ۱۴۰۵', changed: '۵ روز پیش', owner: 'مریم کریمی', desc: 'تلاش مجدد با عقب‌نشینی نمایی برای خطاهای گذرا.' },
    { id: 'ff_dark_admin',   name: 'حالت تیره‌ی پنل ادمین',    key: 'dark_admin',     env: 'staging',   on: false, rollout: 0,   created: '۱۵ تیر ۱۴۰۵', changed: '۱ هفته پیش', owner: 'علی توحیدی', desc: 'تم تیره برای اپراتورهای شیفت شب.' },
    { id: 'ff_beta_sdk',     name: 'SDK نسخه بتا (Go)',        key: 'beta_sdk_go',    env: 'production', on: true,  rollout: 10,  created: '۳ تیر ۱۴۰۵', changed: '۴ روز پیش', owner: 'سمیه کاظمی', desc: 'پیش‌نمایش عمومی SDK گو با خروجی تایپ‌محور.' },
    { id: 'ff_webhook_fan',  name: 'شاخه‌بندی Webhook',       key: 'webhook_fanout', env: 'staging',   on: false, rollout: 0,   created: '۲۹ خرداد ۱۴۰۵', changed: '۲ هفته پیش', owner: 'علی توحیدی', desc: 'ارسال هر رویداد به چند endpoint به‌صورت موازی.' },
    { id: 'ff_kyc_verify',   name: 'احراز هویت سازمانی',      key: 'kyc_verify',     env: 'production', on: false, rollout: 0,   created: '۱ خرداد ۱۴۰۵', changed: '۳ هفته پیش', owner: 'مریم کریمی', desc: 'احراز هویت برای سازمان‌های حقوقی — با تأیید نوعی.' }
  ];

  var SECURITY = [
    { id: 'sec_01', type: 'ورود ناموفق',     user: '—',           ip: '185.12.44.9',  device: 'Windows · Chrome',  at: 'امروز · ۰۳:۱۲', severity: 'high',     status: 'blocked' },
    { id: 'sec_02', type: 'نشست مشکوک',      user: 'حسین نادری',  ip: '91.98.23.14',  device: 'Android · ‎App',     at: 'دیروز · ۲۲:۰۴', severity: 'critical', status: 'terminated' },
    { id: 'sec_03', type: 'تغییر نقش ادمین', user: 'مریم کریمی',  ip: '5.122.30.77',  device: 'macOS · Firefox',    at: 'دیروز · ۱۴:۲۲', severity: 'medium',   status: 'done' },
    { id: 'sec_04', type: 'کلید API جدید',   user: 'سارا احمدی',  ip: '5.122.30.77',  device: 'macOS · Firefox',    at: '۲ روز پیش · ۱۱:۰۵', severity: 'low', status: 'done' },
    { id: 'sec_05', type: 'تلاش دسترسی ادمین', user: '—',          ip: '45.155.204.11',device: 'Linux · curl',       at: '۲ روز پیش · ۰۴:۳۹', severity: 'critical', status: 'blocked' },
    { id: 'sec_06', type: 'محدودیت نرخ فعال', user: 'شبکه‌نو',     ip: '—',            device: '—',                 at: '۳ روز پیش · ۱۶:۵۰', severity: 'medium',   status: 'done' },
    { id: 'sec_07', type: 'ورود موفق از IP جدید', user: 'نگار موسوی', ip: '78.157.42.19', device: 'Windows · Edge',  at: '۴ روز پیش · ۰۹:۳۰', severity: 'low', status: 'flagged' },
    { id: 'sec_08', type: 'گواهی نامعتبر',   user: '—',           ip: '103.19.66.2',  device: '—',                  at: '۵ روز پیش · ۰۱:۱۵', severity: 'low', status: 'blocked' }
  ];

  var AUDIT = [
    { id: 'AUD-۲۹۴۴', actor: 'مریم کریمی', action: 'تعلیق کاربر', target: 'حسین نادری (usr_6R2S8T)', at: 'امروز · ۱۱:۰۲', ip: '5.122.30.77', ua: 'Firefox 141 · macOS', before: 'وضعیت: فعال', after: 'وضعیت: تعلیق', result: 'success' },
    { id: 'AUD-۲۹۴۳', actor: 'مریم کریمی', action: 'تغییر حد نرخ', target: 'سازمان شبکه‌نو', at: 'امروز · ۰۹:۴۰', ip: '5.122.30.77', ua: 'Firefox 141 · macOS', before: 'حد نرخ: ۷۵۰/دقیقه', after: 'حد نرخ: ۱۵۰۰/دقیقه (۲۴ ساعت)', result: 'success' },
    { id: 'AUD-۲۹۴۲', actor: 'علی توحیدی', action: 'فعال‌سازی Feature Flag', target: 'smart_retry → ۵۰٪', at: 'دیروز · ۱۷:۲۵', ip: '5.122.30.77', ua: 'Chrome 137 · macOS', before: 'rollout: ۲۵٪', after: 'rollout: ۵۰٪', result: 'success' },
    { id: 'AUD-۲۹۴۱', actor: 'سمیه کاظمی', action: 'حذف حساب سازمان', target: 'کدینو (org_5E2F3G)', at: '۱۹ مرداد · ۱۱:۲۵', ip: '151.244.1.9', ua: 'Chrome 137 · Windows', before: 'وضعیت: فعال', after: 'حذف کامل', result: 'success' },
    { id: 'AUD-۲۹۴۰', actor: 'سیستم',     action: 'استقرار نسخه‌ی جدید', target: 'API Gateway v2.14.1', at: '۱۸ مرداد · ۰۲:۰۰', ip: '10.0.4.2', ua: 'CI/CD', before: 'نسخه: 2.14.0', after: 'نسخه: 2.14.1', result: 'success' },
    { id: 'AUD-۲۹۳۹', actor: 'مریم کریمی', action: 'بازگشت وجه', target: 'شبکه‌نو · tx_29JWD8', at: '۲۶ مرداد · ۱۴:۰۲', ip: '5.122.30.77', ua: 'Firefox 141 · macOS', before: 'پرداخت: موفق', after: 'مسترد: ۹٬۹۰۰٬۰۰۰ تومان', result: 'success' },
    { id: 'AUD-۲۹۳۸', actor: 'علی توحیدی', action: 'تغییر پیکربندی', target: 'حداکثر بدنه‌ی درخواست → ۱۲MB', at: '۲۵ مرداد · ۱۳:۱۰', ip: '151.244.1.9', ua: 'Chrome 137 · Windows', before: '۱۰MB', after: '۱۲MB', result: 'success' },
    { id: 'AUD-۲۹۳۷', actor: 'سیستم',     action: 'رویداد امنیتی', target: 'تلاش دسترسی ادمین (مسدود)', at: '۲ روز پیش · ۰۴:۳۹', ip: '45.155.204.11', ua: 'curl/8.1', before: '—', after: 'IP به لیست مسدود اضافه شد', result: 'blocked' },
    { id: 'AUD-۲۹۳۶', actor: 'مریم کریمی', action: 'ارسال اعلان گروهی', target: '۱۲ کاربر پلن سازمانی', at: '۲ روز پیش · ۱۰:۰۰', ip: '5.122.30.77', ua: 'Firefox 141 · macOS', before: '—', after: 'اعلان: به‌روزرسانی امنیتی', result: 'success' },
    { id: 'AUD-۲۹۳۵', actor: 'سمیه کاظمی', action: 'انتشار سند', target: 'راهنمای Webhook (docs)', at: '۳ روز پیش · ۱۵:۴۲', ip: '151.244.1.9', ua: 'Chrome 137 · Windows', before: 'وضعیت: پیش‌نویس', after: 'وضعیت: منتشرشده', result: 'success' },
    { id: 'AUD-۲۹۳۴', actor: 'مریم کریمی', action: 'لغو اشتراک', target: 'هوش‌یار · sub_9S1T', at: '۱۱ آذر ۱۴۰۳ · ۱۲:۳۰', ip: '5.122.30.77', ua: 'Firefox 141 · macOS', before: 'پلن: پایه (آزمایشی)', after: 'لغو کامل', result: 'success' },
    { id: 'AUD-۲۹۳۳', actor: 'سیستم',     action: 'پشتیبان‌گیری خودکار', target: 'پایگاه‌ی داده‌ی اصلی', at: 'هر شب · ۰۳:۰۰', ip: '10.0.0.7', ua: 'cron', before: '—', after: 'نسخه‌ی پشتیبان ۳۴۱', result: 'success' }
  ];

  var NOTIFICATIONS = [
    { id: 'nt_01', type: 'operations', title: 'پرداخت ناموفق سازمان رایانش', text: 'درگاه کارت در تلاش سوم هم پاسخ نداد. فاکتور INV-۱۴۰۵-۰۷۸ در وضعیت ناموفق است.', at: 'امروز · ۰۸:۴۲', unread: true,  link: 'revenue.html' },
    { id: 'nt_02', type: 'security',    title: '۳ تلاش ورود ناموفق از IP خارجی', text: 'IP 45.155.204.11 در پورتال ادمین مسدود شد.', at: 'امروز · ۰۳:۱۴', unread: true,  link: 'security.html' },
    { id: 'nt_03', type: 'incident',    title: 'کندی صف گزارش‌گیری', text: 'تأخیر صف از ۹۰ ثانیه عبور کرد. تیم زیرساخت در حال بررسی است.', at: 'دیروز · ۱۰:۴۱', unread: true,  link: 'activity.html' },
    { id: 'nt_04', type: 'support',     title: 'تیکت فوری TKT-۱۰۴۲ باز شد', text: 'شبکه‌نو: خطای 429 در پردازش دسته‌ای.', at: 'دیروز · ۱۴:۲۱', unread: false, link: 'support.html' },
    { id: 'nt_05', type: 'billing',     title: 'فاکتور شهریور صادر شد', text: '۸ فاکتور از مجموع ۱۲٬۴۱۰٬۰۰۰ تومان صادر شد.', at: '۱ شهریور · ۰۹:۰۰', unread: false, link: 'revenue.html' },
    { id: 'nt_06', type: 'product',     title: 'قابلیت جدید: خلاصه‌ساز لاگ', text: 'Feature Flag ‏ai_summaries به ۲۵٪ کاربران رسید.', at: '۲ روز پیش', unread: false, link: 'flags.html' },
    { id: 'nt_07', type: 'operations',  title: 'استقرار موفق 2.14.1', text: 'API Gateway با ۰٪ خطا استقرار یافت.', at: '۱۸ مرداد · ۰۲:۰۵', unread: false, link: 'activity.html' },
    { id: 'nt_08', type: 'security',    title: 'گواهی SSL ۳۰ روز دیگر منقضی می‌شود', text: 'گواهی api.bluevertex.ir در ۸ مهر منقضی می‌شود.', at: '۱۵ مرداد · ۰۹:۰۰', unread: false, link: 'settings.html' }
  ];

  /* ----------------------------------------------------------- content --- */
  var CONTENT = {
    blog: [
      { id: 'bl_1', title: 'معرفی موتور محدودیت نرخ نسخه ۲', author: 'سمیه کاظمی', status: 'published', views: '۱۲٬۴۱۰', at: '۲۸ مرداد ۱۴۰۵' },
      { id: 'bl_2', title: 'مدیریت خطاهای 429 در سیستم‌های توزیع‌شده', author: 'علی توحیدی', status: 'published', views: '۸٬۹۴۰', at: '۲۱ مرداد ۱۴۰۵' },
      { id: 'bl_3', title: 'مهاجرت به SDK نسخه ۳ بدون قطعی', author: 'سمیه کاظمی', status: 'draft', views: '—', at: '—' },
      { id: 'bl_4', title: 'الگوهای تلاش مجدد برای APIهای مالی', author: 'مریم کریمی', status: 'review', views: '—', at: '—' }
    ],
    docs: [
      { id: 'dc_1', title: 'شروع سریع با REST API', cat: 'شروع', author: 'سمیه کاظمی', status: 'published', updated: '۲۰ مرداد ۱۴۰۵', views: '۴۸٬۲۰۰' },
      { id: 'dc_2', title: 'احراز هویت و کلیدهای API', cat: 'امنیت', author: 'مریم کریمی', status: 'published', updated: '۱۲ مرداد ۱۴۰۵', views: '۳۶٬۷۴۰' },
      { id: 'dc_3', title: 'مرجع Webhook', cat: 'رویدادها', author: 'علی توحیدی', status: 'published', updated: '۸ مرداد ۱۴۰۵', views: '۱۹٬۳۱۰' },
      { id: 'dc_4', title: 'محدودیت نرخ و سهمیه', cat: 'مفاهیم', author: 'علی توحیدی', status: 'draft', updated: '—', views: '—' },
      { id: 'dc_5', title: 'خطاهای رایج و رفع آن‌ها', cat: 'عیب‌یابی', author: 'سمیه کاظمی', status: 'archived', updated: '۲ خرداد ۱۴۰۵', views: '۲۲٬۰۸۰' }
    ],
    changelog: [
      { id: 'cl_1', version: '2.14.1', title: 'بهبود پایداری Gateway', status: 'published', at: '۱۸ مرداد ۱۴۰۵', author: 'علی توحیدی' },
      { id: 'cl_2', version: '2.14.0', title: 'درگاه پرداخت جدید', status: 'published', at: '۲۱ تیر ۱۴۰۵', author: 'مریم کریمی' },
      { id: 'cl_3', version: '2.15.0-beta', title: 'SDK گو (بتا)', status: 'draft', at: '—', author: 'سمیه کاظمی' },
      { id: 'cl_4', version: '2.13.2', title: 'رفع باگ Webhook در صف‌های فشرده', status: 'published', at: '۱ تیر ۱۴۰۵', author: 'علی توحیدی' }
    ],
    annc: [
      { id: 'an_1', title: 'توقف سرویس نسخه‌های قدیمی API', type: 'warning', status: 'published', at: '۱ شهریور ۱۴۰۵', author: 'مریم کریمی' },
      { id: 'an_2', title: 'به‌روزرسانی امنیتی الزامی', type: 'critical', status: 'scheduled', at: '۱۵ شهریور ۱۴۰۵', author: 'مریم کریمی' },
      { id: 'an_3', title: 'افزایش سقف سهمیه برای پلن رشد', type: 'info', status: 'published', at: '۱۲ مرداد ۱۴۰۵', author: 'علی توحیدی' },
      { id: 'an_4', title: 'گزارش وضعیت آگوست (اگوست)', type: 'update', status: 'draft', at: '—', author: 'سمیه کاظمی' }
    ]
  };

  /* ------------------------------------------------------------ charts --- */
  var CHARTS = {
    mrr: {
      labels: ['مهر', 'آبان', 'آذر', 'دی', 'بهمن', 'اسفند', 'فروردین', 'اردیبهشت', 'خرداد', 'تیر', 'مرداد', 'شهریور'],
      values: [112, 118, 124, 131, 139, 146, 158, 165, 172, 184, 196, 207]   /* میلیون تومان */
    },
    growth: {
      labels: ['مهر', 'آبان', 'آذر', 'دی', 'بهمن', 'اسفند', 'فروردین', 'اردیبهشت', 'خرداد', 'تیر', 'مرداد', 'شهریور'],
      signups: [42, 38, 51, 47, 63, 58, 74, 82, 96, 108, 121, 134],
      active: [310, 322, 340, 351, 372, 386, 402, 415, 431, 446, 458, 462]
    },
    api: {
      labels: ['شنبه', 'یکشنبه', 'دوشنبه', 'سه‌شنبه', 'چهارشنبه', 'پنجشنبه', 'جمعه'],
      values: [41200, 44800, 43100, 47600, 51200, 48900, 43400]
    },
    planRev: { labels: ['سازمانی', 'حرفه‌ای', 'رشد', 'پایه'], values: [52, 31, 14, 3] },
    newVsExisting: { labels: ['مرداد', 'تیر', 'خرداد'], news: [18, 14, 11], existing: [178, 170, 161] },
    errors: { labels: ['401', '429', '404', '422', '5xx'], values: [2840, 1920, 1110, 840, 410] }
  };

  var STATUS_TXT = {
    active: 'فعال', suspended: 'تعلیق‌شده', churned: 'لغوشده', past_due: 'پرداخت معوق', trial: 'آزمایشی'
  };

  window.ADMIN = {
    users: USERS, orgs: ORGS, subs: SUBS, invoices: INVOICES, payments: PAYMENTS,
    tickets: TICKETS, incidents: INCIDENTS, flags: FLAGS, security: SECURITY,
    audit: AUDIT, notifications: NOTIFICATIONS, content: CONTENT, charts: CHARTS,
    statusTxt: STATUS_TXT
  };
})();
