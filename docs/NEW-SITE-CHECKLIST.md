# Adding the next Frontier site

Worked example: Coin, the second site.

1. **Config.** Set `status = "live"` for the site in `config.toml` (the entry already exists).
2. **Module.** Copy `sites/quantum.py` to `sites/<slug>.py`. Replace the references, companies, scenarios, copy and
   chapter content. Keep the six-chapter shape: how it works, the short version, what changes, the companies and the
   money, the gap, three years out. Keep the disclosures footer unchanged.
3. **Live layer.** Give the module a `SCEN` dictionary (ticker to scenarios). Add the SEC CIK numbers and headline
   aliases to `frontier/live/sources.py` and `classify.py`. Run `python -m frontier.live.run --site <slug>`.
4. **Photographs.** `python tools/find_images.py "<query>" ...`, pick public-domain files, download with `--download`,
   run `tools/optimise_images.py`, look at `sheet.jpg`, and caption only what the picture shows.
5. **Voice.** `python tools/voice_lint.py dist/<slug>/index.html` must report 0 problems.
6. **Facts.** Every number has a source in `REFS`. Targets are labelled targets. Read the page.
7. **Build and look.** `python build.py <slug>`, serve `dist/`, look at the page at 1920 and at phone width.
8. **Disclosures.** Confirm the conflicts statement is still true for this topic. Add anything topic-specific
   (for crypto: the EU markets-in-crypto rules; for health: no medical advice).
9. **Deploy.** `wrangler deploy`, or push and let the workflow do it once the token is set.
10. **Solas33.** Add the product to `solas33web/products.json` (screenshot at 1600x1000 as three webp sizes and an
    icon), the home carousel, and the Atelier migration under Alchemy. Add the docs to the Atelier through
    `watch-portfolio/tools/publish_to_atelier.py`.
