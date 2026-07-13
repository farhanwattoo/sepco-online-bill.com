# sepco-online-bill.com

Static site for SEPCO (Sukkur Electric Power Company) bill guides, with a
browser-side bill estimator built on the FY 2025-26 NEPRA tariff.

## Deploy on Vercel

- Framework Preset: Other
- Root Directory: this folder
- Build Command: leave empty
- Output Directory: leave empty

`vercel.json` enables `cleanUrls` and `trailingSlash`, so every page is served
at its canonical URL (e.g. `/sepco-tariff-rates-2026/`). `404.html` is served
automatically for unknown paths. `.vercelignore` keeps the generator and repo
docs out of the deployment.

## Structure

- `index.html` — homepage (includes the bill estimator)
- `<slug>/index.html` — one folder per article/guide (30 articles + 5 legal pages)
- `styles.css` — single mobile-first stylesheet, no external assets
- `script.js` — slab-based bill estimator (runs entirely client-side)
- `sitemap.xml`, `robots.txt`, `favicon.svg`, `404.html`

## Editing pages

Pages are generated from `_generator/` (plain Python, no dependencies):

- `template.py` — HTML template, nav/footer, schema markup, card metadata
- `content_a.py` — the 20 core bill guides
- `content_b.py` — the 10 newer articles
- `build.py` — page content for home/legal pages + writes all HTML and sitemap.xml

To change content, edit the relevant file and run:

```
python3 _generator/build.py
```

Commit both the generator change and the regenerated HTML.

## Keeping rates current

Tariff figures (slab rates in `script.js` and the tariff/calculator articles)
follow the NEPRA-notified uniform tariff. NEPRA rebases each July and adjusts
quarterly — update `script.js` TARIFF/FIXED_CHARGES plus the tables in
`content_b.py` (`sepco-tariff-rates-2026`) when new determinations land, and
bump the `UPDATED_*` constants in `template.py`.
