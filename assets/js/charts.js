/* ==========================================================================
   BLUE VERTEX — charts.js — Chart.js integration (Persian-first, RTL)
   Requires: chart.umd.js (vendored) · main.js (BV helpers)
   Any element with [data-chart] becomes a chart:
     data-chart-type : line | bar | doughnut | polarArea | area
     data-labels     : JSON array of labels
     data-values     : JSON array (or array of arrays for multi-dataset)
     data-colors     : JSON array of hex colors
     data-name       : dataset label
     data-fill       : "1" to fill area under line
     data-rangeable  : "1" → reacts to bv:range event (overview demo data)
     data-unit       : unit string for tooltips (e.g. "درخواست")
     data-stacked    : "1"
   ========================================================================== */
(function () {
  'use strict';
  var charts = [];
  var FONT = { family: "'Vazirmatn', system-ui, sans-serif" };

  /* theme-aware colors: read the design tokens that the CSS switch re-maps */
  function cssVar(name, fb) {
    try {
      var v = getComputedStyle(document.documentElement).getPropertyValue(name);
      return (v && v.trim()) ? v.trim() : fb;
    } catch (e) { return fb; }
  }
  function themeColors() {
    return {
      elev: cssVar('--bg-elev', '#161616'),
      text1: cssVar('--text-1', '#FFFFFF'),
      text2: cssVar('--text-2', '#A1A1AA'),
      text3: cssVar('--text-3', '#71717A'),
      border: cssVar('--border', 'rgba(255,255,255,.08)'),
      borderStrong: cssVar('--border-strong', 'rgba(255,255,255,.14)'),
      grid: cssVar('--grid-line', 'rgba(255,255,255,.05)')
    };
  }

  var RANGE_SETS = {
    '24h': { labels: ['۰:۰۰', '۳:۰۰', '۶:۰۰', '۹:۰۰', '۱۲:۰۰', '۱۵:۰۰', '۱۸:۰۰', '۲۱:۰۰', '۲۳:۵۹'], values: [320, 410, 380, 540, 620, 705, 660, 590, 510] },
    '7d': { labels: ['شنبه', 'یکشنبه', 'دوشنبه', 'سه‌شنبه', 'چهارشنبه', 'پنجشنبه', 'جمعه'], values: [1240, 1480, 1320, 1690, 1845, 1610, 1420] },
    '30d': { labels: ['هفته ۱', 'هفته ۲', 'هفته ۳', 'هفته ۴'], values: [8200, 9400, 11300, 12850] },
    '90d': { labels: ['مرداد', 'شهریور', 'مهر'], values: [24800, 33600, 41700] }
  };

  function fa(v, unit) {
    var s = (window.BV && BV.faNum) ? BV.faNum(v) : String(v);
    return unit ? s + ' ' + unit : s;
  }

  function baseTools() {
    var TC = themeColors();
    return {
      responsive: true,
      maintainAspectRatio: false,
      animation: { duration: 700, easing: 'easeOutQuart' },
      interaction: { mode: 'index', intersect: false },
      plugins: {
        legend: { display: false },
        tooltip: {
          rtl: true, textDirection: 'rtl', backgroundColor: TC.elev,
          titleColor: TC.text1, bodyColor: TC.text2, borderColor: TC.borderStrong,
          borderWidth: 1, padding: 12, cornerRadius: 10, displayColors: true,
          boxPadding: 6, titleFont: Object.assign({ size: 12, weight: '700' }, FONT),
          bodyFont: Object.assign({ size: 12 }, FONT),
          callbacks: {
            label: function (ctx) {
              var unit = ctx.dataset.unit || '';
              return ' ' + ctx.dataset.label + ': ' + fa(ctx.parsed.y !== undefined ? ctx.parsed.y : ctx.parsed, unit);
            }
          }
        }
      },
      scales: {
        x: { grid: { display: false }, border: { color: TC.border }, ticks: Object.assign({ color: TC.text3, font: Object.assign({ size: 11 }, FONT), maxTicksLimit: 8 }, {}) },
        y: { beginAtZero: true, grid: { color: TC.grid }, border: { display: false }, ticks: Object.assign({ color: TC.text3, font: Object.assign({ size: 11 }, FONT), maxTicksLimit: 6 }, { callback: function (v) { return fa(v); } }) }
      }
    };
  }

  function gradientFill(ctx, area, hex) {
    var g = ctx.createLinearGradient(0, area.top, 0, area.bottom);
    g.addColorStop(0, hex.replace(')', ',.32)').replace('rgb', 'rgba'));
    g.addColorStop(1, hex.replace(')', ',0)').replace('rgb', 'rgba'));
    return g;
  }

  function build(el) {
    var type = el.getAttribute('data-chart-type') || 'line';
    var labels = JSON.parse(el.getAttribute('data-labels') || '[]');
    var values = JSON.parse(el.getAttribute('data-values') || '[]');
    var colors = JSON.parse(el.getAttribute('data-colors') || '[]');
    var name = el.getAttribute('data-name') || 'سری داده';
    var unit = el.getAttribute('data-unit') || '';
    var fill = el.getAttribute('data-fill') === '1';
    var stacked = el.getAttribute('data-stacked') === '1';
    var useRtl = el.getAttribute('data-no-rtl') !== '1';

    var multi = values.length && typeof values[0] === 'object' && values[0] !== null;
    var ds = [];
    if (multi) {
      var setNames = JSON.parse(el.getAttribute('data-ds-names') || '[]');
      values.forEach(function (v, i) {
        ds.push({
          label: setNames[i] || name + ' ' + faNum(i + 1),
          data: v, unit: unit,
          borderColor: colors[i % colors.length], backgroundColor: colors[i % colors.length],
          fill: fill, tension: 0.42, borderWidth: 2.2,
          pointRadius: 0, pointHoverRadius: 4.5, pointHoverBackgroundColor: colors[i % colors.length],
          borderRadius: 6, borderSkipped: false, maxBarThickness: 34
        });
      });
    } else {
      (values.length ? values : [0]).forEach(function (v, i) { });
      var c0 = colors[0] || '#3B82F6';
      ds.push({
        label: name, data: values, unit: unit,
        borderColor: c0,
        backgroundColor: fill ? 'transparent' : c0,
        fill: fill, tension: 0.42, borderWidth: 2.4,
        pointRadius: 0, pointHoverRadius: 5, pointHoverBackgroundColor: c0,
        showLine: type !== 'bar',
        borderRadius: 7, borderSkipped: false, maxBarThickness: 34
      });
    }

    var TC = themeColors();
    var opts = baseTools();
    if (type === 'doughnut' || type === 'polarArea') {
      opts = {
        responsive: true, maintainAspectRatio: false,
        cutout: '70%', borderWidth: 0,
        animation: { duration: 700, easing: 'easeOutQuart' },
        plugins: {
          legend: { display: false },
          tooltip: {
            rtl: true, textDirection: 'rtl', backgroundColor: TC.elev,
            titleColor: TC.text1, bodyColor: TC.text2, borderColor: TC.borderStrong,
            borderWidth: 1, padding: 12, cornerRadius: 10,
            bodyFont: Object.assign({ size: 12 }, FONT), titleFont: Object.assign({ size: 12, weight: '700' }, FONT),
            callbacks: { label: function (ctx) { return ' ' + ctx.label + ': ' + fa(ctx.parsed, unit); } }
          }
        }
      };
    }
    if (stacked) {
      opts.scales = opts.scales || {};
      opts.scales.x = opts.scales.x || {};
      opts.scales.y = opts.scales.y || {};
      opts.scales.x.stacked = true;
      opts.scales.y.stacked = true;
    }
    if (useRtl) {
      opts.scales = opts.scales || {};
      opts.scales.x = opts.scales.x || {};
      opts.scales.y = opts.scales.y || {};
      opts.scales.x.rtl = true;
      opts.scales.x.textDirection = 'rtl';
    }

    /* register gradient before first render */
    var chart = new Chart(el, {
      type: type === 'area' ? 'line' : type,
      data: { labels: labels, datasets: ds },
      options: opts,
      plugins: [{
        beforeDatasetsDraw: function (ch) {
          if (!ch.chartArea || ch.isGradientSet) return;
          ch.isGradientSet = true;
          ch.data.datasets.forEach(function (d, i) {
            if (ch.config.type === 'line' && d.fill === true && !multi) {
              d.backgroundColor = gradientFill(ch.ctx, ch.chartArea, colors[0] || 'rgb(59,130,246)');
            }
          });
        }
      }]
    });
    charts.push({ el: el, chart: chart });
    return chart;
  }

  function destroyAll() {
    charts.forEach(function (c) { try { c.chart.destroy(); } catch (e) {} });
    charts = [];
  }

  function mount() {
    if (!window.Chart) return;
    destroyAll();
    $$('[data-chart]').forEach(build);
    /* re-render on resize of sidebar toggles is handled by Chart.js responsive */
  }

  function setRange(rangeKey) {
    var set = RANGE_SETS[rangeKey];
    if (!set) return;
    charts.forEach(function (c) {
      if (c.el.getAttribute('data-rangeable') !== '1') return;
      var ch = c.chart;
      ch.data.labels = set.labels;
      ch.data.datasets.forEach(function (d) { d.data = set.values; });
      ch.update();
    });
  }

  function $$(sel, ctx) { return Array.prototype.slice.call((ctx || document).querySelectorAll(sel)); }
  function faNum(n) { return (window.BV && BV.faNum) ? BV.faNum(n) : String(n); }

  document.addEventListener('bv:range', function (e) { setRange(e.detail.range); });
  document.addEventListener('bv:theme', function () { try { mount(); } catch (e) {} });
  document.addEventListener('DOMContentLoaded', mount);

  window.BVCharts = { mount: mount, setRange: setRange, destroyAll: destroyAll };
})();
