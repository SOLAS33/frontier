/* Frontier motion and frame: hero headline reveal, parallax photo bands, chapter spine, live rail and ticker. */
(function () {
  "use strict";
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  var reduce = window.matchMedia && matchMedia("(prefers-reduced-motion: reduce)").matches;
  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); }

  /* headline: split into words that slide up one after another (words stay readable without script) */
  var h1 = $(".fx-hero h1");
  if (h1 && !h1.dataset.split) {
    h1.dataset.split = 1; var i = 0;
    (function walk(node) {
      Array.prototype.slice.call(node.childNodes).forEach(function (n) {
        if (n.nodeType === 3) {
          var frag = document.createDocumentFragment();
          n.textContent.split(/(\s+)/).forEach(function (t) {
            if (!t) return;
            if (/^\s+$/.test(t)) { frag.appendChild(document.createTextNode(" ")); return; }
            var w = document.createElement("span"); w.className = "w";
            var s = document.createElement("span"); s.textContent = t; s.style.setProperty("--i", i++); w.appendChild(s); frag.appendChild(w);
          });
          node.replaceChild(frag, n);
        } else if (n.nodeType === 1) walk(n);
      });
    })(h1);
  }

  /* parallax: images inside bands and the hero drift slower than the page */
  var movers = $$(".fx-band-img, .fx-hero-img");
  var ticking = false;
  function par() {
    ticking = false;
    var vh = innerHeight;
    movers.forEach(function (m) {
      var r = m.parentNode.getBoundingClientRect();
      if (r.bottom < -100 || r.top > vh + 100) return;
      var p = (r.top + r.height / 2 - vh / 2) / vh;
      m.style.transform = "translate3d(0," + (p * -60).toFixed(1) + "px,0)";
    });
  }
  if (!reduce) {
    addEventListener("scroll", function () { if (!ticking) { ticking = true; requestAnimationFrame(par); } }, { passive: true });
    addEventListener("resize", par); par();
  }

  /* chapter spine */
  var spine = $("#fx-spine");
  if (spine) {
    var chs = $$(".fx-ch");
    spine.innerHTML = chs.map(function (c, k) { return '<a href="#' + c.id + '"><b>' + String(k + 1).padStart(2, "0") + "</b><span>" + esc(c.dataset.title) + "</span></a>"; }).join("");
    var links = $$("a", spine);
    if ("IntersectionObserver" in window) {
      var io = new IntersectionObserver(function (es) {
        es.forEach(function (e) { if (e.isIntersecting) links.forEach(function (a) { a.classList.toggle("on", a.getAttribute("href") === "#" + e.target.id); }); });
      }, { rootMargin: "-35% 0px -55% 0px" });
      chs.forEach(function (c) { io.observe(c); });
    }
  }

  /* live rail and ticker, filled when the live layer arrives */
  document.addEventListener("frontier:live", function (ev) {
    var L = ev.detail, T = L.tickers, keys = Object.keys(T);
    var rail = $("#fx-rail");
    if (rail) {
      var rows = keys.map(function (k) {
        var t = T[k], tilt = t.tilt_pts;
        return '<div class="row"><span>' + k + " <small>$" + t.price.toFixed(2) + '</small></span><span style="color:' + (tilt > 0 ? "var(--green)" : tilt < 0 ? "var(--red)" : "var(--muted)") + '">' +
          (tilt > 0 ? "+" : "") + tilt.toFixed(1) + " pt</span></div>";
      }).join("");
      var e = L.events[0];
      rail.innerHTML = "<h4>Odds tilt today</h4>" + rows + (e ? '<div class="ev"><h4>Latest</h4><a href="' + esc(e.url) + '" target="_blank" rel="noopener">' + esc(e.title) + "</a></div>" : "") +
        '<p style="margin-top:12px;font-size:.72rem">Updated ' + new Date(L.generated).toLocaleString("en-GB", { dateStyle: "medium", timeStyle: "short" }) + "</p>";
    }
    var tk = $("#fx-ticker-track");
    if (tk) {
      var cell = function (k) {
        var t = T[k], wk = t.week_change;
        return "<span>" + k + " $" + t.price.toFixed(2) + (wk != null ? ' <span class="' + (wk >= 0 ? "u" : "d") + '">' + (wk >= 0 ? "+" : "") + (wk * 100).toFixed(1) + "% wk</span>" : "") + "</span>";
      };
      var evs = L.events.slice(0, 4).map(function (x) { return "<span>" + esc(x.ticker) + ": " + esc(x.title.slice(0, 70)) + "</span>"; });
      var line = keys.map(cell).concat(evs).join("");
      tk.innerHTML = line + line;
    }
  });
})();
