# docseek

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

Goal-driven document crawler where a relevance judge (Jev is one built-in option) scores links, ranks pages, flags pages that hide documents, and picks filter values.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/mohojojo/docseek) |
| Maintainer | [mohojojo](https://github.com/mohojojo). Independently curated. |
| Format | Python package + HTTP server with Playwright |
| Requirements | Python, Playwright Chromium; a judge backend (Jev via TypeSafe key, or another model). |
| License | [Apache-2.0](https://github.com/mohojojo/docseek/blob/e0d3006cd4338224c03423c04aa3924131b634f5/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`docseek/jev.py`](https://github.com/mohojojo/docseek/blob/e0d3006cd4338224c03423c04aa3924131b634f5/docseek/jev.py) at the pinned commit. |

## When to use

- Find every matching document on sites with year filters, tabs, load-more lists or JSON-backed SPAs.
- Mismatch: Jev is one of three judges; the crawl agent model is separate.

## How it works

The judge answers four questions (is this link a wanted document, what kind of page, does the page still hide documents, which filter value). Code crawls, sets filters and escalates hard pages to a browsing agent. Integration evidence: [`docseek/jev.py`](https://github.com/mohojojo/docseek/blob/e0d3006cd4338224c03423c04aa3924131b634f5/docseek/jev.py).

## Get started

From the upstream README (not run on the review host):

```sh
pip install docseek
playwright install chromium
uvicorn docseek.server:app --port 8010
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Jev judge: `docseek/jev.py`, `docseek/jev_crawl.py`.
- Evaluation folder: `eval/`.

## Limits and data handling

Page text and links are sent to the configured judge and agent model.

## Review and maintenance

Reviewed **2026-10-14** (Europe/Sofia) at [commit e0d3006cd433](https://github.com/mohojojo/docseek/tree/e0d3006cd4338224c03423c04aa3924131b634f5). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
