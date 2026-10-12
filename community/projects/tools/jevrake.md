# jevrake

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

Selector-free scraping CLI and Python library: describe fields, jevrake collects every typed value on the page, and Jev picks the value that matches each description, returning confidence and the source text.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/RKasai127/jevrake) |
| Maintainer | [RKasai127](https://github.com/RKasai127). Independently curated. |
| Format | Python CLI + library (PyPI `jevrake`) |
| Requirements | Python 3.12+; `TYPESAFE_API_KEY`. |
| License | [MIT](https://github.com/RKasai127/jevrake/blob/68c6a73bae5ed32ccb071bafc2d1c4b071e4df14/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |

## When to use

- Extract product/listing fields without writing CSS/XPath selectors.
- Pydantic-model extraction from list pages (each item output separately).
- Mismatch: Values below 0.9 confidence become `null`; robots.txt is not checked, so follow each site's rules.

## How it works

Code gathers candidate values by type (`str`, `int`, `float`, `decimal`); Jev chooses among them per field, so output values always come from the page. Jev integration: [`src/jevrake/_internal/jev.py`](https://github.com/RKasai127/jevrake/blob/68c6a73bae5ed32ccb071bafc2d1c4b071e4df14/src/jevrake/_internal/jev.py). (Summarized from the upstream README and source at the pinned commit; not reproduced here.)

## Get started

From the upstream README (not run on the review host):

```sh
pipx install jevrake
export TYPESAFE_API_KEY=your-api-key
jevrake https://books.toscrape.com/ --fields '{"title": "Book title"}'
```

## Limits and data handling

Page candidates are sent to TypeSafe. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-12** (Europe/Sofia) at [commit 68c6a73bae5e](https://github.com/RKasai127/jevrake/tree/68c6a73bae5ed32ccb071bafc2d1c4b071e4df14). Inspected the upstream README, LICENSE, and the Jev integration file linked above; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
