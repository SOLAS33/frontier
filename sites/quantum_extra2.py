"""Section builders that stitch the extra content into chapters 3, 4 and 6."""
from __future__ import annotations

from sites import quantum_extra as X


def ch3_extra() -> str:
    jobs = "".join(f'<li><a href="{u}" target="_blank" rel="noopener"><b>{n}</b></a>: {d}</li>' for n, d, u in X.JOBS)
    return f'''
<h3 style="margin-top:40px">The security clock</h3>
<div class="tl">
<div class="ev big"><div class="yr">Aug 2024</div><p>The US standards body NIST publishes the first post-quantum encryption standards (FIPS 203, 204, 205).</p></div>
<div class="ev fut"><div class="yr">About 2030</div><p>Published government roadmaps plan to stop using today's public-key encryption for the most sensitive systems. Check the current NIST and EU dates, which have moved before.</p></div>
<div class="ev fut"><div class="yr">About 2035</div><p>Target for finishing migration in most roadmaps. A machine able to break RSA-2048 is estimated to need around a million noisy qubits.</p></div>
</div>
<div class="callout"><b>Bitcoin and other coins.</b> They sign payments with the kind of cryptography a large quantum computer would break. Coins in addresses whose public key is already visible on the chain are the most exposed. The coin community is working on upgrades, but a change needs wide agreement, which is slow. The Frontier coin site will cover this in detail.</div>
<h3 style="margin-top:36px">Close to home: Ireland</h3>
<div class="cols">
<div class="card rv"><h3>The strategy</h3><p>Ireland published a national quantum strategy, Quantum 2030, in 2023, aimed at building research strength, skills and links with industry.</p></div>
<div class="card rv"><h3>The companies and labs</h3><p>Equal1 in Dublin builds quantum chips on silicon. The Tyndall National Institute in Cork works on photonics and materials. Large US technology firms run research teams here.</p></div>
<div class="card rv"><h3>Why it matters here</h3><p>Ireland hosts a large share of Europe's data centres and holds a lot of other countries' encrypted data. Both make the post-quantum migration a local business issue, and the power question a local energy issue.</p></div>
</div>
<h3 style="margin-top:36px">Jobs, skills and where to start</h3>
<div class="cols">
<div class="card rv"><h3>Who is hiring</h3><p>Hardware physicists and engineers, cryogenic and control-electronics engineers, software and compiler developers, and people who can translate a chemistry or finance problem into a quantum one. Most roles want a degree, but security and cloud roles are open to anyone who learns the basics.</p></div>
<div class="card rv"><h3>Free ways to learn</h3><ul>{jobs}</ul></div>
</div>
<h3 style="margin-top:36px">Society and ethics</h3>
<div class="cols">
<div class="card rv"><h3>Who gets access</h3><p>Machines will be rented from a few firms and governments. Whoever holds the best hardware first gains an edge in chemistry, finance and intelligence work.</p></div>
<div class="card rv"><h3>Energy and climate</h3><p>One machine uses little power, but a fleet of large ones could add real load. Possible gains in fertiliser, batteries and solar materials could outweigh that, if they arrive.</p></div>
<div class="card rv"><h3>Jobs and inequality</h3><p>Few jobs are replaced directly. The larger effect is on which chemistry and materials industries get cheaper, and which countries host them.</p></div>
</div>
{X.defence()}'''


def ch4_extra(idx_svg: str) -> str:
    hype = "".join(f'<tr><td class="n">{lvl}</td><td><b>{name}</b><br><span class="muted">{desc}</span></td><td>{ex}</td>'
                   f'<td><span class="tag {cls}">{ "strong" if cls == "ok" else "caution" if cls == "dis" else "target only"}</span></td></tr>'
                   for lvl, name, desc, ex, cls in X.HYPE)
    shovels = "".join(f"<tr><td>{a}</td><td>{b}</td><td>{c}</td><td>{d}</td></tr>" for a, b, c, d in X.SHOVELS)
    return f'''
<h3 style="margin-top:44px">Live updates</h3>
<p>The page checks a live layer for new filings, headlines and papers, and shows how they move the odds used in chapter 6. <span id="live-stamp">Loading the live layer...</span></p>
<div class="cols">
<div class="card"><h3>Announcements that moved the odds</h3><ul class="feed" id="live-events"><li>Loading...</li></ul></div>
<div class="card"><h3>Projection change log</h3><ul class="feed" id="live-log"><li>Loading...</li></ul></div>
<div class="card"><h3>Headlines (links to the publisher)</h3><ul class="feed" id="live-news"><li>Loading...</li></ul></div>
<div class="card"><h3>Latest quantum-computing papers that mention these firms</h3><ul class="feed" id="live-papers"><li>Loading...</li></ul></div>
</div>
<p class="cap" id="live-status"></p>
<div class="scroll"><table id="live-react"></table></div>
<p class="cap">The table shows how these four stocks actually moved after past filings of each type, against the Nasdaq-100 proxy QQQ. It is what the live layer uses to size its nudges, and it is reported with case counts because small samples mislead.</p>

<h3 style="margin-top:44px">Hype or proof?</h3>
<p>Every claim sits on a rung of evidence. The higher the rung, the more weight it deserves.</p>
<div class="scroll"><table><thead><tr><th class="n">Rung</th><th>Evidence</th><th>Examples on this page</th><th>Weight</th></tr></thead><tbody>{hype}</tbody></table></div>

<h3 style="margin-top:44px">The race, country by country</h3>
<p>Select a country. Colour shows role: leaders in teal, major players in violet, emerging in amber. This is a summary from public sources and is approximate.</p>
<div class="map-wrap"><figure class="fig" style="margin:0">{X.tile_map()}</figure><div class="card" id="map-panel"></div></div>
<div class="callout t"><b>Why politics moves these shares.</b> Governments fund their own champions, restrict exports of key parts and sometimes bar foreign buyers. The United States and China each treat quantum computing as a strategic race. A new restriction can cut a company off from customers or suppliers overnight, and a new funding programme can lift a whole group. The live feed tags these as policy events.</div>

<h3 style="margin-top:44px">Who sells the picks and shovels</h3>
<div class="scroll"><table><thead><tr><th>Part of the chain</th><th>Examples</th><th>Where</th><th>Why it matters</th></tr></thead><tbody>{shovels}</tbody></table></div>
<p class="cap">Examples only, not recommendations.</p>

<h3 style="margin-top:44px">The Frontier Index</h3>
<p>An equal-weight basket of the four pure-plays and a basket of the four large groups, both set to 100 at the start. It shows how differently the two routes to the theme have behaved.</p>
<figure class="fig">{idx_svg}<figcaption>Weekly rebalanced equal-weight baskets. Pure-plays: IonQ, Rigetti, D-Wave, Quantum Computing Inc. Large groups: IBM, Alphabet, Microsoft, Honeywell. Computed from weekly closes.</figcaption></figure>

<h3 style="margin-top:44px">Time machine</h3>
<p>Pick an asset and a date. See what a sum of money would be worth now, how high it went, and how far it fell on the way.</p>
<div class="ctrl"><label>Asset <select id="tm-asset"></select></label><label>From <input type="date" id="tm-date"></label><label>Amount (US$) <input type="number" id="tm-amt" value="1000" min="1" step="100"></label></div>
<figure class="fig"><svg id="tm-svg" viewBox="0 0 900 260" role="img" aria-label="Value of the investment over time"></svg><div id="tm-out" class="tmout"></div></figure>
<p class="cap">Past prices only. Apple, Bitcoin and Nvidia are here because they show what a boom and the wait before it look like.</p>'''


def ch6_interactive(sims, companies, fmt_p) -> str:
    rows = "".join(f'<tr><td>{c["name"]} ({c["t"]})</td><td class="n">{fmt_p(sims[c["t"]]["end_p10"])}</td><td class="n">{fmt_p(sims[c["t"]]["end_p50"])}</td>'
                   f'<td class="n">{fmt_p(sims[c["t"]]["end_p90"])}</td><td class="n">{sims[c["t"]]["prob_below_start"]:.0%}</td></tr>' for c in companies)
    return f'''
<div class="callout r"><b>Read this first.</b> These are scenarios built from stated assumptions, not forecasts, recommendations or targets. Past price behaviour is not a guide to the future. You can lose all of the money you put into shares like these. Solas33 holds no position and takes no payment from any company named.</div>
<figure class="fig" id="fan">
<div class="ctrl" id="fan-tabs" role="group" aria-label="Company"></div>
<svg id="fansvg" viewBox="0 0 900 440" role="img" aria-label="Recent price and three-year scenario range for the chosen company"></svg>
<div class="sliders">
<label>Chance of the bear story <output></output><input type="range" id="sl-bear" min="0" max="90" step="1"></label>
<label>Chance of the bull story <input type="range" id="sl-bull" min="0" max="90" step="1"></label>
<label>Volatility (100 = last two years, scaled) <input type="range" id="sl-vol" min="40" max="160" step="5"></label>
<button type="button" id="fan-reset" class="plain">Back to the author's odds</button>
</div>
<p id="fan-probs" class="cap"></p><p id="fan-read"></p><p id="fan-tilt" class="cap"></p>
<figcaption>Drag the sliders to set your own odds. Dashed lines are the typical path in each story; shaded bands are where the middle 50% and 80% of outcomes fall. The live layer may have tilted the author's odds by a few points because of dated announcements, never by more than {12} points.</figcaption>
</figure>
<div class="scroll"><table><thead><tr><th>Stock</th><th class="n">Low end (10th)</th><th class="n">Middle</th><th class="n">High end (90th)</th><th class="n">Below today</th></tr></thead><tbody>{rows}</tbody></table></div>
<p class="cap">Three years from the build date, using the author's starting odds.</p>
<h3 style="margin-top:36px">How this site has done against itself</h3>
<div class="card"><p id="live-score">Loading the scorecard...</p>
<p class="cap">Every week the site records its 3, 6 and 12-month ranges in a hash-chained log before the outcome is known, then scores them. A range of 10th to 90th should hold the actual price about 80% of the time.</p></div>'''
