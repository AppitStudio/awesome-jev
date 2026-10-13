# PaperRadar

[All projects](../README.md) · [Web apps](README.md#web-apps)

Local web app to browse conference papers (ICML, ICLR, CVPR, NeurIPS and more), filter by research tags and export to Zotero; new tagging runs use TypeSafe Jev.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/eyad-al-shami/PaperRadar) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [github.com/eyad-al-shami/PaperRadar#readme](https://github.com/eyad-al-shami/PaperRadar#readme) |
| Pricing and access | Free MIT source; browsing bundled data needs no key; new tagging is billed to your TypeSafe key. |
| Jev evidence | [`research_tagger/classifier.py`](https://github.com/eyad-al-shami/PaperRadar/blob/972ab2ff7ba09d2a29f2fc2987ea8531fef295d3/research_tagger/classifier.py) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |
| Maintainer | [eyad-al-shami](https://github.com/eyad-al-shami). Independently curated. |
| Format | Local web app (Python) |
| Platform and availability | Web (local, `uv run research-tagger-web`) |
| Jev's role | Jev applies your chosen research tags to scraped papers (with a cost estimate first); 25k saved tagging results ship with the app. |
| Requirements | Python with uv; TypeSafe key for new tagging. |
| License | [MIT](https://github.com/eyad-al-shami/PaperRadar/blob/972ab2ff7ba09d2a29f2fc2987ea8531fef295d3/LICENSE) |

## When to use

- Shortlist relevant papers across conferences by topic tags.
- Mismatch: Open-source alternatives to Jev for tagging are planned, not available.

## How it works

Scrapers collect papers; selected tags are applied by Jev; the UI filters by intersecting tags and exports to Zotero. (Summarized from the upstream [README](https://github.com/eyad-al-shami/PaperRadar/blob/972ab2ff7ba09d2a29f2fc2987ea8531fef295d3/README.md); not reproduced here.)

## Get started

From the upstream README (not run on the review host): `uv sync` then `uv run research-tagger-web` and open `http://127.0.0.1:8000`.

## Limits and data handling

Paper titles/abstracts go to TypeSafe when tagging. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-13** (Europe/Sofia) at [commit 972ab2ff7ba0](https://github.com/eyad-al-shami/PaperRadar/tree/972ab2ff7ba09d2a29f2fc2987ea8531fef295d3). Inspected the upstream README, LICENSE (where present), and the Jev integration evidence linked above; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
