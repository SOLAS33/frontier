(function () {
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  var reduce = window.matchMedia && matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* theme toggle, remembered if storage allows */
  var btn = $("#theme");
  try { var saved = localStorage.getItem("theme"); if (saved) document.documentElement.setAttribute("data-theme", saved); } catch (e) {}
  if (btn) btn.onclick = function () {
    var cur = document.documentElement.getAttribute("data-theme") ||
      (matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light");
    var next = cur === "dark" ? "light" : "dark";
    document.documentElement.setAttribute("data-theme", next);
    try { localStorage.setItem("theme", next); } catch (e) {}
  };

  /* scroll progress and active chapter */
  var bar = $("#progress");
  function onScroll() {
    var h = document.documentElement.scrollHeight - innerHeight;
    if (bar) bar.style.width = (h > 0 ? scrollY / h * 100 : 0) + "%";
  }
  addEventListener("scroll", onScroll, { passive: true }); onScroll();
  var links = $$("nav.bar a.s");
  if ("IntersectionObserver" in window) {
    var chapObs = new IntersectionObserver(function (es) {
      es.forEach(function (e) {
        if (e.isIntersecting) links.forEach(function (a) { a.classList.toggle("on", a.getAttribute("href") === "#" + e.target.id); });
      });
    }, { rootMargin: "-30% 0px -60% 0px" });
    $$(".chapter").forEach(function (c) { chapObs.observe(c); });

    /* animate figures once when they come into view, count numbers up */
    var once = new IntersectionObserver(function (es) {
      es.forEach(function (e) {
        if (!e.isIntersecting) return;
        e.target.classList.add("go", "in"); once.unobserve(e.target);
        $$("[data-count]", e.target).forEach(count);
        if (e.target.hasAttribute("data-count")) count(e.target);
      });
    }, { threshold: 0.18 });
    $$(".fig,.rv,.stats").forEach(function (n) { once.observe(n); });
  } else { $$(".fig").forEach(function (n) { n.classList.add("go"); }); }
  function count(el) {
    if (el.dataset.done) return; el.dataset.done = 1;
    var end = parseFloat(el.dataset.count), pre = el.dataset.pre || "", suf = el.dataset.suf || "", dec = +(el.dataset.dec || 0);
    if (reduce) return;
    var t0 = performance.now(), dur = 1400;
    (function tick(t) {
      var p = Math.min(1, (t - t0) / dur), v = end * (1 - Math.pow(1 - p, 3));
      el.textContent = pre + v.toLocaleString("en-GB", { minimumFractionDigits: dec, maximumFractionDigits: dec }) + suf;
      if (p < 1) requestAnimationFrame(tick);
    })(t0);
  }

  /* pointer glow on cards */
  $$(".card").forEach(function (c) {
    c.addEventListener("pointermove", function (e) {
      var r = c.getBoundingClientRect();
      c.style.setProperty("--mx", (e.clientX - r.left) + "px"); c.style.setProperty("--my", (e.clientY - r.top) + "px");
    });
  });

  /* interactive share price chart */
  var P = window.PRICES, svg = $("#chart");
  if (!P || !svg) return;
  var NS = "http://www.w3.org/2000/svg", W = 900, H = 440, M = { l: 66, r: 20, t: 16, b: 36 };
  var ORDER = window.PRICE_ORDER, NAMES = window.PRICE_NAMES, COL = {};
  ORDER.forEach(function (t, i) { COL[t] = "var(--s" + (i + 1) + ")"; });
  var st = { sel: { IONQ: 1, RGTI: 1, QBTS: 1, QUBT: 1 }, mode: "growth", range: "2024" };
  var last = P.IONQ.d[P.IONQ.d.length - 1];
  var lastEl = $("#lastdate"); if (lastEl) lastEl.textContent = new Date(last).toLocaleDateString("en-GB", { day: "numeric", month: "long", year: "numeric" });
  function el(tag, a, p) { var e = document.createElementNS(NS, tag); for (var k in a) e.setAttribute(k, a[k]); if (p) p.appendChild(e); return e; }
  function fmt(v) { return v >= 1000 ? v.toLocaleString("en-GB", { maximumFractionDigits: 0 }) : v >= 100 ? v.toFixed(0) : v >= 10 ? v.toFixed(1) : v.toFixed(2); }
  var tick = $("#tickers");
  ORDER.slice(0, 9).forEach(function (t) {
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
    for (var e = Math.ceil(y0); e <= y1; e++) [1, 2, 5].forEach(function (k) {
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
      var p = el("path", { d: d, fill: "none", stroke: COL[t], "stroke-width": 2.3, "stroke-linejoin": "round", pathLength: 1, class: "draw" }, svg);
      p.style.strokeDasharray = 1; if (!reduce) { p.style.animation = "draw 1.4s cubic-bezier(.2,.7,.2,1) both"; }
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
})();
