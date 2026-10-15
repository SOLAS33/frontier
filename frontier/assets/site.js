(function () {
  "use strict";
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  var reduce = window.matchMedia && matchMedia("(prefers-reduced-motion: reduce)").matches;
  var NS = "http://www.w3.org/2000/svg";
  function el(tag, a, p) { var e = document.createElementNS(NS, tag); for (var k in a) e.setAttribute(k, a[k]); if (p) p.appendChild(e); return e; }
  function fmt(v) { return v >= 1000 ? v.toLocaleString("en-GB", { maximumFractionDigits: 0 }) : v >= 100 ? v.toFixed(0) : v >= 10 ? v.toFixed(1) : v.toFixed(2); }
  function money(v) { return "$" + fmt(v); }
  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); }

  /* ---------- theme, reading level ---------- */
  var root = document.documentElement;
  try { var th = localStorage.getItem("theme"); if (th) root.setAttribute("data-theme", th); } catch (e) {}
  var tb = $("#theme");
  if (tb) tb.onclick = function () {
    var cur = root.getAttribute("data-theme") || (matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light");
    var nx = cur === "dark" ? "light" : "dark"; root.setAttribute("data-theme", nx);
    try { localStorage.setItem("theme", nx); } catch (e) {}
  };
  function setLevel(l) {
    document.body.setAttribute("data-level", l);
    $$("[data-lv]").forEach(function (b) { b.setAttribute("aria-pressed", b.dataset.lv === l); });
    try { localStorage.setItem("level", l); } catch (e) {}
  }
  $$("[data-lv]").forEach(function (b) { b.onclick = function () { setLevel(b.dataset.lv); }; });
  var lv = "g"; try { lv = localStorage.getItem("level") || "g"; } catch (e) {} setLevel(lv);

  /* ---------- progress, active chapter, reveal, counters ---------- */
  var bar = $("#progress");
  function onScroll() { var h = root.scrollHeight - innerHeight; if (bar) bar.style.width = (h > 0 ? scrollY / h * 100 : 0) + "%"; }
  addEventListener("scroll", onScroll, { passive: true }); onScroll();
  var links = $$("nav.bar a.s");
  function count(n) {
    if (n.dataset.done) return; n.dataset.done = 1; if (reduce) return;
    var end = parseFloat(n.dataset.count), pre = n.dataset.pre || "", suf = n.dataset.suf || "", dec = +(n.dataset.dec || 0), t0 = performance.now();
    (function tick(t) {
      var p = Math.min(1, (t - t0) / 1400), v = end * (1 - Math.pow(1 - p, 3));
      n.textContent = pre + v.toLocaleString("en-GB", { minimumFractionDigits: dec, maximumFractionDigits: dec }) + suf;
      if (p < 1) requestAnimationFrame(tick);
    })(t0);
  }
  if ("IntersectionObserver" in window) {
    var co = new IntersectionObserver(function (es) {
      es.forEach(function (e) { if (e.isIntersecting) links.forEach(function (a) { a.classList.toggle("on", a.getAttribute("href") === "#" + e.target.id); }); });
    }, { rootMargin: "-30% 0px -60% 0px" });
    $$(".chapter").forEach(function (c) { co.observe(c); });
    var once = new IntersectionObserver(function (es) {
      es.forEach(function (e) {
        if (!e.isIntersecting) return; e.target.classList.add("go", "in"); once.unobserve(e.target);
        $$("[data-count]", e.target).forEach(count);
      });
    }, { threshold: 0.15 });
    $$(".fig,.rv,.stats").forEach(function (n) { once.observe(n); });
  } else { $$(".fig").forEach(function (n) { n.classList.add("go"); }); }
  $$(".card").forEach(function (c) {
    c.addEventListener("pointermove", function (e) {
      var r = c.getBoundingClientRect(); c.style.setProperty("--mx", (e.clientX - r.left) + "px"); c.style.setProperty("--my", (e.clientY - r.top) + "px");
    });
  });

  /* ---------- scenario maths (mirrors frontier/live/state.py) ---------- */
  function erf(x) { var s = x < 0 ? -1 : 1; x = Math.abs(x); var t = 1 / (1 + 0.3275911 * x);
    return s * (1 - (((((1.061405429 * t - 1.453152027) * t) + 1.421413741) * t - 0.284496736) * t + 0.254829592) * t * Math.exp(-x * x)); }
  function mixCdf(x, price, scen, months, volMult) {
    var tot = 0;
    scen.forEach(function (s) {
      var mu = Math.log(price) + Math.log(1 + s.drift) * months / 12, sd = s.sigma * volMult * Math.sqrt(months / 12);
      tot += s.p * (sd > 0 ? 0.5 * (1 + erf((Math.log(x) - mu) / (sd * Math.SQRT2))) : (x >= Math.exp(mu) ? 1 : 0));
    });
    return tot;
  }
  function mixQ(q, price, scen, months, volMult) {
    var lo = price * 1e-4, hi = price * 1e4;
    for (var i = 0; i < 70; i++) { var m = Math.sqrt(lo * hi); if (mixCdf(m, price, scen, months, volMult) < q) lo = m; else hi = m; }
    return Math.sqrt(lo * hi);
  }

  /* ---------- scenario fan chart (interactive) ---------- */
  var SCEN = window.SCEN || {}, LIVE = null;
  var FAN = { t: Object.keys(SCEN)[0], bear: null, bull: null, vol: 1 };
  function currentScen(t) { return SCEN[t].scen.map(function (s) { return Object.assign({}, s); }); }
  function setProbs(t) {
    var sc = currentScen(t), by = {}; sc.forEach(function (s) { by[s.k] = s; });
    FAN.bear = by.bear.p; FAN.bull = by.bull.p;
    var bearEl = $("#sl-bear"), bullEl = $("#sl-bull"), volEl = $("#sl-vol");
    if (bearEl) { bearEl.value = Math.round(FAN.bear * 100); bullEl.value = Math.round(FAN.bull * 100); volEl.value = Math.round(FAN.vol * 100); }
  }
  function drawFan() {
    var host = $("#fan"); if (!host || !FAN.t) return;
    var d = SCEN[FAN.t], W = 900, H = 440, M = { l: 70, r: 130, t: 18, b: 36 };
    var sc = currentScen(FAN.t), by = {}; sc.forEach(function (s) { by[s.k] = s; });
    var bear = Math.min(FAN.bear, 1 - FAN.bull); FAN.bear = bear;
    by.bear.p = bear; by.bull.p = FAN.bull; by.base.p = Math.max(0, 1 - bear - FAN.bull);
    var months = 36, hist = d.hist.c, hd = d.hist.d, nh = hist.length;
    var Q = { 10: [], 25: [], 50: [], 75: [], 90: [] }, k;
    for (k = 0; k <= months; k++) [10, 25, 50, 75, 90].forEach(function (q) { Q[q].push(k === 0 ? d.price : mixQ(q / 100, d.price, sc, k, FAN.vol)); });
    var lo = Math.min(Math.min.apply(null, hist), Q[10][months] * 0.9), hi = Math.max(Math.max.apply(null, hist), Q[90][months] * 1.05);
    var y0 = Math.log10(lo), y1 = Math.log10(hi), span = nh - 1 + months * 4.345;
    var X = function (w) { return M.l + w / span * (W - M.l - M.r); };
    var Y = function (v) { return M.t + (1 - (Math.log10(Math.max(v, lo * .5)) - y0) / (y1 - y0)) * (H - M.t - M.b); };
    var svg = $("#fansvg"); svg.innerHTML = "";
    for (var e = Math.floor(y0); e <= Math.ceil(y1); e++) [1, 2, 5].forEach(function (m) {
      var v = m * Math.pow(10, e); if (v < lo || v > hi) return;
      el("line", { x1: M.l, x2: W - M.r, y1: Y(v), y2: Y(v), class: "grid" }, svg);
      var t = el("text", { x: M.l - 8, y: Y(v) + 4, "text-anchor": "end" }, svg); t.textContent = money(v);
    });
    var tx = X(nh - 1);
    el("line", { x1: tx, x2: tx, y1: M.t, y2: H - M.b, class: "today" }, svg);
    var tt = el("text", { x: tx + 6, y: M.t + 12, class: "t-amber" }, svg); tt.textContent = "Today";
    var l0 = el("text", { x: M.l, y: H - 10 }, svg); l0.textContent = hd[0].slice(0, 7);
    var l1 = el("text", { x: W - M.r, y: H - 10, "text-anchor": "end" }, svg); l1.textContent = "36 months ahead";
    function band(up, lw, cls) {
      var pts = []; for (var i = 0; i <= months; i++) pts.push(X(nh - 1 + i * 4.345).toFixed(1) + "," + Y(up[i]).toFixed(1));
      for (i = months; i >= 0; i--) pts.push(X(nh - 1 + i * 4.345).toFixed(1) + "," + Y(lw[i]).toFixed(1));
      el("polygon", { points: pts.join(" "), class: cls }, svg);
    }
    band(Q[90], Q[10], "band-wide"); band(Q[75], Q[25], "band-mid");
    [["bear", "sc-bear"], ["base", "sc-base"], ["bull", "sc-bull"]].forEach(function (p) {
      var s = by[p[0]], dd = ""; for (var i = 0; i <= months; i++) dd += (i ? "L" : "M") + X(nh - 1 + i * 4.345).toFixed(1) + " " + Y(d.price * Math.pow(1 + s.drift, i / 12)).toFixed(1);
      el("path", { d: dd, class: p[1] }, svg);
    });
    var hp = ""; hist.forEach(function (v, i) { hp += (i ? "L" : "M") + X(i).toFixed(1) + " " + Y(v).toFixed(1); });
    el("path", { d: hp, class: "hist" }, svg);
    el("circle", { cx: tx, cy: Y(d.price), r: 5, class: "dot" }, svg);
    [[90, "t-teal", "90th"], [50, "t-fg", "middle"], [10, "t-red", "10th"]].forEach(function (r) {
      var t = el("text", { x: W - M.r + 8, y: Y(Q[r[0]][months]) + 4, class: r[1] }, svg); t.textContent = money(Q[r[0]][months]) + " " + r[2];
    });
    var below = mixCdf(d.price, d.price, sc, months, FAN.vol), dbl = 1 - mixCdf(d.price * 2, d.price, sc, months, FAN.vol), half = mixCdf(d.price * .5, d.price, sc, months, FAN.vol);
    $("#fan-read").innerHTML = "<b>" + esc(d.name) + "</b> now " + money(d.price) + ". In three years: middle " + money(Q[50][months]) + ", low end " + money(Q[10][months]) +
      ", high end " + money(Q[90][months]) + ". Chance below today's price " + Math.round(below * 100) + "%, doubling " + Math.round(dbl * 100) + "%, losing half " + Math.round(half * 100) + "%.";
    $("#fan-probs").textContent = "Bear " + Math.round(by.bear.p * 100) + "%, base " + Math.round(by.base.p * 100) + "%, bull " + Math.round(by.bull.p * 100) + "%";
    var tilt = d.tilt_pts; $("#fan-tilt").textContent = LIVE ? "Live news tilt today: " + (tilt >= 0 ? "+" : "") + tilt.toFixed(1) + " points toward " + (tilt >= 0 ? "bull" : "bear") + "." : "";
  }
  function initFan() {
    var tabs = $("#fan-tabs"); if (!tabs || !FAN.t) return;
    Object.keys(SCEN).forEach(function (t) {
      var b = document.createElement("button"); b.dataset.t = t; b.textContent = SCEN[t].name;
      b.onclick = function () { FAN.t = t; FAN.vol = 1; setProbs(t); drawFan(); mark(); }; tabs.appendChild(b);
    });
    function mark() { $$("#fan-tabs button").forEach(function (b) { b.setAttribute("aria-pressed", b.dataset.t === FAN.t); }); }
    $("#sl-bear").oninput = function () { FAN.bear = this.value / 100; if (FAN.bear + FAN.bull > 1) { FAN.bull = 1 - FAN.bear; $("#sl-bull").value = Math.round(FAN.bull * 100); } drawFan(); };
    $("#sl-bull").oninput = function () { FAN.bull = this.value / 100; if (FAN.bear + FAN.bull > 1) { FAN.bear = 1 - FAN.bull; $("#sl-bear").value = Math.round(FAN.bear * 100); } drawFan(); };
    $("#sl-vol").oninput = function () { FAN.vol = this.value / 100; drawFan(); };
    $("#fan-reset").onclick = function () { FAN.vol = 1; setProbs(FAN.t); drawFan(); };
    setProbs(FAN.t); mark(); drawFan();
  }

  /* ---------- share price chart ---------- */
  var P = window.PRICES, ORDER = window.PRICE_ORDER, NAMES = window.PRICE_NAMES, COL = {};
  function initPrices() {
    var svg = $("#chart"); if (!P || !svg) return;
    var W = 900, H = 440, M = { l: 66, r: 20, t: 16, b: 36 };
    ORDER.forEach(function (t, i) { COL[t] = "var(--s" + (i + 1) + ")"; });
    var st = { sel: {}, mode: "growth", range: "2024" };
    (window.PRICE_DEFAULT || ORDER.slice(0, 4)).forEach(function (t) { st.sel[t] = 1; });
    var last = P[ORDER[0]].d[P[ORDER[0]].d.length - 1];
    var le = $("#lastdate"); if (le) le.textContent = new Date(last).toLocaleDateString("en-GB", { day: "numeric", month: "long", year: "numeric" });
    var tick = $("#tickers");
    ORDER.forEach(function (t) {
      var b = document.createElement("button"); b.dataset.t = t;
      b.innerHTML = '<span class="sw" style="background:' + COL[t] + '"></span>' + NAMES[t];
      b.onclick = function () { if (st.sel[t]) { if (Object.keys(st.sel).length > 1) delete st.sel[t]; } else st.sel[t] = 1; draw(); };
      tick.appendChild(b);
    });
    $$("[data-mode]").forEach(function (b) { b.onclick = function () { st.mode = b.dataset.mode; draw(); }; });
    $$("[data-range]").forEach(function (b) { b.onclick = function () { st.range = b.dataset.range; draw(); }; });
    function startFor() {
      if (st.range === "all") return "0000";
      if (st.range === "1y") return new Date(+new Date(last) - 365 * 864e5).toISOString().slice(0, 10);
      return st.range + "-01-01";
    }
    function series(t) {
      var p = P[t], s = startFor(), d = [], c = [];
      for (var i = 0; i < p.d.length; i++) if (p.d[i] >= s) { d.push(p.d[i]); c.push(p.c[i]); }
      if (st.mode === "growth" && c.length) { var b = c[0]; c = c.map(function (v) { return v / b * 100; }); }
      return { d: d, c: c };
    }
    function draw() {
      $$("[data-mode]").forEach(function (b) { b.setAttribute("aria-pressed", b.dataset.mode === st.mode); });
      $$("[data-range]").forEach(function (b) { b.setAttribute("aria-pressed", b.dataset.range === st.range); });
      $$("#tickers button").forEach(function (b) { b.setAttribute("aria-pressed", !!st.sel[b.dataset.t]); });
      svg.innerHTML = "";
      var S = {}, t0 = Infinity, t1 = -Infinity, lo = Infinity, hi = -Infinity;
      Object.keys(st.sel).forEach(function (t) {
        var s = series(t); if (s.d.length < 2) return; S[t] = s;
        t0 = Math.min(t0, +new Date(s.d[0])); t1 = Math.max(t1, +new Date(s.d[s.d.length - 1]));
        s.c.forEach(function (v) { lo = Math.min(lo, v); hi = Math.max(hi, v); });
      });
      if (!isFinite(t0)) return;
      var yv = function (v) { return Math.log10(Math.max(v, 0.01)); };
      var y0 = Math.floor(yv(lo) * 2) / 2, y1 = Math.ceil(yv(hi) * 2) / 2;
      var X = function (t) { return M.l + (t - t0) / (t1 - t0 || 1) * (W - M.l - M.r); };
      var Y = function (v) { return M.t + (1 - (yv(v) - y0) / (y1 - y0 || 1)) * (H - M.t - M.b); };
      for (var e = Math.ceil(y0) - 1; e <= y1; e++) [1, 2, 5].forEach(function (k) {
        var v = k * Math.pow(10, e); if (yv(v) < y0 || yv(v) > y1) return;
        el("line", { x1: M.l, x2: W - M.r, y1: Y(v), y2: Y(v), class: "grid" }, svg);
        var tx = el("text", { x: M.l - 8, y: Y(v) + 4, "text-anchor": "end" }, svg); tx.textContent = (st.mode === "growth" ? "" : "$") + fmt(v);
      });
      var ya = new Date(t0).getFullYear(), yb = new Date(t1).getFullYear(), step = yb - ya > 12 ? 4 : yb - ya > 6 ? 2 : 1;
      for (var y = ya + 1; y <= yb; y += step) {
        var x = X(+new Date(y + "-01-01")); if (x < M.l || x > W - M.r) continue;
        el("line", { x1: x, x2: x, y1: M.t, y2: H - M.b, class: "grid", "stroke-dasharray": "2 5" }, svg);
        var tt = el("text", { x: x, y: H - M.b + 20, "text-anchor": "middle" }, svg); tt.textContent = y;
      }
      Object.keys(S).forEach(function (t) {
        var s = S[t], d = "";
        s.d.forEach(function (dt, i) { d += (i ? "L" : "M") + X(+new Date(dt)).toFixed(1) + " " + Y(s.c[i]).toFixed(1); });
        var p = el("path", { d: d, fill: "none", stroke: COL[t], "stroke-width": 2.3, "stroke-linejoin": "round", pathLength: 1 }, svg);
        if (!reduce) { p.style.strokeDasharray = 1; p.style.animation = "draw 1.4s cubic-bezier(.2,.7,.2,1) both"; }
        el("circle", { cx: X(+new Date(s.d[s.d.length - 1])), cy: Y(s.c[s.c.length - 1]), r: 4, fill: COL[t] }, svg);
      });
      var cross = el("line", { x1: 0, x2: 0, y1: M.t, y2: H - M.b, stroke: "var(--fg)", opacity: 0 }, svg);
      var ov = el("rect", { x: M.l, y: M.t, width: W - M.l - M.r, height: H - M.t - M.b, fill: "transparent" }, svg);
      var tip = $("#tip");
      ov.addEventListener("pointermove", function (ev) {
        var r = svg.getBoundingClientRect(), px = (ev.clientX - r.left) / r.width * W, tm = t0 + (px - M.l) / (W - M.l - M.r) * (t1 - t0);
        cross.setAttribute("x1", px); cross.setAttribute("x2", px); cross.setAttribute("opacity", .5);
        var out = new Date(tm).toLocaleDateString("en-GB", { month: "short", year: "numeric" }) + "   ";
        Object.keys(S).forEach(function (t) {
          var s = S[t], best = -1, bd = Infinity;
          s.d.forEach(function (dt, i) { var dd = Math.abs(+new Date(dt) - tm); if (dd < bd) { bd = dd; best = i; } });
          if (bd < 40 * 864e5) out += t + " " + (st.mode === "growth" ? fmt(s.c[best]) : "$" + fmt(s.c[best])) + "   ";
        });
        tip.textContent = out;
      });
      ov.addEventListener("pointerleave", function () { cross.setAttribute("opacity", 0); });
    }
    draw();
  }

  /* ---------- time machine ---------- */
  function initTime() {
    var sel = $("#tm-asset"); if (!sel || !P) return;
    var assets = window.TM_ASSETS;
    assets.forEach(function (a) { var o = document.createElement("option"); o.value = a[0]; o.textContent = a[1]; sel.appendChild(o); });
    var di = $("#tm-date"), am = $("#tm-amt"), out = $("#tm-out"), svg = $("#tm-svg");
    function setDefault() { var p = P[sel.value]; var pre = window.TM_DEFAULT[sel.value]; di.min = p.d[0]; di.max = p.d[p.d.length - 1]; di.value = pre || p.d[0]; }
    function calc() {
      var p = P[sel.value], amt = Math.max(1, +am.value || 1000), i = p.d.findIndex(function (x) { return x >= di.value; });
      if (i < 0) i = 0;
      var units = amt / p.c[i], vals = p.c.slice(i).map(function (c) { return c * units; });
      var peak = -1, pi = 0, dd = 0, runPeak = vals[0];
      vals.forEach(function (v, k) { if (v > peak) { peak = v; pi = k; } runPeak = Math.max(runPeak, v); dd = Math.min(dd, v / runPeak - 1); });
      var now = vals[vals.length - 1];
      out.innerHTML = "<b>" + money(amt) + "</b> in " + esc(NAMES[sel.value] || sel.options[sel.selectedIndex].textContent) + " on " + p.d[i] +
        " would be worth <b>" + money(now) + "</b> now (" + (now / amt).toFixed(1) + "x). It peaked at " + money(peak) + " in " + p.d[i + pi].slice(0, 7) +
        ". The worst fall from a high along the way was " + Math.round(dd * 100) + "%.";
      svg.innerHTML = "";
      var W = 900, H = 260, M = { l: 70, r: 20, t: 14, b: 28 }, n = vals.length, lo = Math.min.apply(null, vals), hi = Math.max.apply(null, vals);
      var yl = Math.log10(Math.max(lo, 1)), yh = Math.log10(hi);
      var X = function (k) { return M.l + k / (n - 1 || 1) * (W - M.l - M.r); }, Y = function (v) { return M.t + (1 - (Math.log10(Math.max(v, 1)) - yl) / (yh - yl || 1)) * (H - M.t - M.b); };
      for (var e = Math.ceil(yl); e <= yh; e++) { var yy = Y(Math.pow(10, e)); el("line", { x1: M.l, x2: W - M.r, y1: yy, y2: yy, class: "grid" }, svg); var t = el("text", { x: M.l - 8, y: yy + 4, "text-anchor": "end" }, svg); t.textContent = money(Math.pow(10, e)); }
      el("line", { x1: M.l, x2: W - M.r, y1: Y(amt), y2: Y(amt), class: "today" }, svg);
      var d = ""; vals.forEach(function (v, k) { d += (k ? "L" : "M") + X(k).toFixed(1) + " " + Y(v).toFixed(1); });
      var pa = el("path", { d: d, class: "hist" }, svg); pa.style.fill = "none";
      el("circle", { cx: X(pi), cy: Y(peak), r: 5, fill: "var(--amber)" }, svg);
      var a = el("text", { x: M.l, y: H - 6 }, svg); a.textContent = p.d[i].slice(0, 7);
      var b = el("text", { x: W - M.r, y: H - 6, "text-anchor": "end" }, svg); b.textContent = p.d[p.d.length - 1].slice(0, 7);
    }
    sel.onchange = function () { setDefault(); calc(); }; di.onchange = calc; am.oninput = calc;
    setDefault(); calc();
  }

  /* ---------- race map ---------- */
  function initMap() {
    var C = window.COUNTRY, N = window.COUNTRY_NAMES, panel = $("#map-panel"); if (!C || !panel) return;
    function show(cc) {
      var c = C[cc]; if (!c) return;
      $$(".tile").forEach(function (g) { g.classList.toggle("sel", g.dataset.cc === cc); });
      var L = window.MAP_LABELS || { co: "Companies and labs", gov: "Government programme", ctl: "Export controls", note: "Read" };
      panel.innerHTML = "<h3>" + esc(N[cc]) + "</h3><dl><dt>" + esc(L.co) + "</dt><dd>" + esc(c.co) + "</dd><dt>" + esc(L.gov) + "</dt><dd>" + esc(c.gov) +
        "</dd><dt>" + esc(L.ctl) + "</dt><dd>" + esc(c.ctl) + "</dd><dt>" + esc(L.note) + "</dt><dd>" + esc(c.note) + "</dd></dl>";
    }
    $$(".tile").forEach(function (g) {
      g.addEventListener("click", function () { show(g.dataset.cc); });
      g.addEventListener("keydown", function (e) { if (e.key === "Enter" || e.key === " ") { e.preventDefault(); show(g.dataset.cc); } });
    });
    show(window.MAP_DEFAULT || "US");
  }

  /* ---------- live layer ---------- */
  function renderLive(L) {
    LIVE = L;
    document.dispatchEvent(new CustomEvent("frontier:live", { detail: L }));
    var st = $("#live-stamp");
    if (st) st.textContent = "Last updated " + new Date(L.generated).toLocaleString("en-GB", { dateStyle: "long", timeStyle: "short" }) + " (UTC " + L.generated.slice(11, 16) + ")";
    Object.keys(L.tickers).forEach(function (t) {
      if (!SCEN[t]) return;
      var o = L.tickers[t]; SCEN[t].price = o.price; SCEN[t].tilt_pts = o.tilt_pts; SCEN[t].scen = o.scen.map(function (s) { return { k: s.k, label: s.label, p: s.p, drift: s.drift, sigma: s.sigma }; });
    });
    var ev = $("#live-events");
    if (ev) ev.innerHTML = L.events.length ? L.events.slice(0, 12).map(function (e) {
      return "<li><span class=\"tag\">" + esc(e.ticker) + "</span><span class=\"tag " + (e.nudge > 0 ? "ok" : e.nudge < 0 ? "dis" : "") + "\">" + esc(e.type.replace("_", " ")) + "</span> " +
        "<a href=\"" + esc(e.url) + "\" target=\"_blank\" rel=\"noopener\">" + esc(e.title) + "</a> <span class=\"muted\">" + esc(e.date) + ", " + esc(e.source) +
        (e.nudge ? ", odds effect " + (e.nudge > 0 ? "+" : "") + e.nudge.toFixed(1) + " pts at first" : "") + "</span></li>";
    }).join("") : "<li>No classified announcements in the window. SEC filings need the job's contact email set; headlines depend on the news feed answering.</li>";
    var lg = $("#live-log");
    if (lg) lg.innerHTML = L.changelog.length ? L.changelog.slice(0, 10).map(function (c) {
      return "<li><b>" + esc(c.ticker) + "</b> " + esc(c.at.slice(0, 10)) + ": bear " + Math.round(c.from.bear * 100) + "% to " + Math.round(c.to.bear * 100) + "%, bull " +
        Math.round(c.from.bull * 100) + "% to " + Math.round(c.to.bull * 100) + "%. " + c.causes.map(function (x) { return esc(x.title); }).join("; ") + "</li>";
    }).join("") : "<li>No projection changes yet. The odds start at the author's priors and move only when a classified announcement passes the thresholds.</li>";
    var pp = $("#live-papers");
    if (pp) pp.innerHTML = L.papers.slice(0, 8).map(function (p) {
      return "<li><a href=\"" + esc(p.url) + "\" target=\"_blank\" rel=\"noopener\">" + esc(p.title) + "</a> <span class=\"muted\">" + esc(p.date) + ", mentions " + esc(p.term) + "</span></li>";
    }).join("");
    var hl = $("#live-news");
    if (hl) {
      var items = []; Object.keys(L.headlines).forEach(function (t) { L.headlines[t].forEach(function (h) { items.push([t, h]); }); });
      hl.innerHTML = items.length ? items.slice(0, 10).map(function (x) {
        return "<li><span class=\"tag\">" + esc(x[0]) + "</span><a href=\"" + esc(x[1].url) + "\" target=\"_blank\" rel=\"noopener\">" + esc(x[1].title) + "</a> <span class=\"muted\">" + esc(x[1].source) + ", " + esc(x[1].date) + "</span></li>";
      }).join("") : "<li>No headlines were returned on the last run.</li>";
    }
    var rt = $("#live-react");
    if (rt) rt.innerHTML = L.reactions.length ? "<thead><tr><th>Filing type</th><th class=\"n\">Cases</th><th class=\"n\">Median 1 day</th><th class=\"n\">Median 5 days</th><th class=\"n\">Share up</th><th>Reliable?</th></tr></thead><tbody>" +
      L.reactions.map(function (r) { return "<tr><td>" + esc(r.type.replace("_", " ")) + "</td><td class=\"n\">" + r.n + "</td><td class=\"n\">" + (r.median_1d * 100).toFixed(1) + "%</td><td class=\"n\">" +
        (r.median_5d * 100).toFixed(1) + "%</td><td class=\"n\">" + Math.round(r.share_up_5d * 100) + "%</td><td>" + (r.enough ? "enough cases" : "too few cases") + "</td></tr>"; }).join("") + "</tbody>" : "";
    var sc = $("#live-score");
    if (sc) {
      var s = L.scorecard;
      sc.innerHTML = "<b>" + s.logged + "</b> predictions logged, <b>" + s.scored + "</b> scored so far. " + (s.coverage === null ? "None have reached their date yet. The first 3-month checks fall due in January." :
        "Actual prices landed inside the stated 10th to 90th range " + Math.round(s.coverage * 100) + "% of the time (a well-calibrated range lands inside about 80%).") +
        " Log integrity: " + (s.chain_ok ? "intact" : "BROKEN") + ".";
    }
    Object.keys(L.status).forEach(function (k) { /* surfaced in the status line */ });
    var ss = $("#live-status");
    if (ss) { var bad = Object.keys(L.status).filter(function (k) { return L.status[k] !== "ok"; });
      ss.textContent = bad.length ? "Sources with problems on the last run: " + bad.map(function (k) { return k + " (" + L.status[k] + ")"; }).join(", ") : "All sources answered on the last run."; }
    if ($("#fan")) { setProbs(FAN.t); drawFan(); }
    var cards = $$("[data-live-price]");
    cards.forEach(function (c) { var t = c.dataset.livePrice; if (L.tickers[t]) c.textContent = money(L.tickers[t].price); });
  }
  function loadLive() {
    if (!window.fetch) return;
    fetch("live.json", { cache: "no-cache" }).then(function (r) { return r.ok ? r.json() : Promise.reject(); }).then(renderLive).catch(function () {
      var st = $("#live-stamp"); if (st) st.textContent = "Live layer not reachable from this copy of the page; showing the build-time numbers.";
    });
  }

  initPrices(); initFan(); initTime(); initMap(); loadLive();
})();
