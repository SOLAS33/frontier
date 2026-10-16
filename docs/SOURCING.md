# Sourcing rule

Set by the founder on 16 October 2026: no fact goes on a Frontier site from memory.

1. Every number, date, name and claim must be checked against a source fetched at the time of writing. Prefer the company filing, the regulator, the agency or the original paper. A news report is acceptable if the primary source cannot be fetched, and the page says so ("on secondary summaries").
2. Every sourced claim carries a numbered reference (`cite(n)`) that links to the page that supports it. `python build.py <slug> --check-links` must show no `broken` links.
3. Where sources disagree, the text says so and gives the range. Do not pick one quietly.
4. Do not state a negative ("none exist") unless a source says it. Write "we found no ..." and name what was searched.
5. Company targets and promises are labelled as targets or company claims.
6. Photographs are public domain or CC0 only (`tools/find_images.py`), with the Commons licence recorded in `credits.json`.
7. Opinion is allowed in the outlook chapter and the scenarios, and is labelled as ours.
8. Re-check the figures before each refresh of a site. Results, prices and deals change.

Status on 16 October 2026: all fourteen sites were written, rewritten or audited to this rule. The audit record is docs/AUDIT-2026-10-16.md, including what was not re-checked.
