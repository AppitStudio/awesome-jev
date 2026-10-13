# Working Note

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Google Sheet + Python service that coaches financial variance commentary against a team's written standard; TypeSafe Jev grades each material line on active criteria.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/alexxxram25/working-note) |
| Maintainer | [alexxxram25](https://github.com/alexxxram25). Independently curated. |
| Format | Google Sheet add-on menu + Python service |
| Requirements | Google Sheets; Python service hosting; TypeSafe or OpenRouter key. |
| License | [MIT](https://github.com/alexxxram25/working-note/blob/74e7a67b1bcf0a21f4564292ecac6d41768afdf6/LICENSE) |
| Jev evidence | [`backend/coach/config.py`](https://github.com/alexxxram25/working-note/blob/74e7a67b1bcf0a21f4564292ecac6d41768afdf6/backend/coach/config.py) at the pinned commit. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |

## When to use

- Give preparers immediate feedback on flux commentary before review.
- Mismatch: prototype tested only on a fictional company.

## How it works

Arithmetic and duplicate checks run in code; only material lines that pass go to Jev with each criterion's "passes when" text for a yes/no grade. (Summarized from the upstream [README](https://github.com/alexxxram25/working-note/blob/74e7a67b1bcf0a21f4564292ecac6d41768afdf6/README.md); not reproduced here.)

## Get started

From the upstream README (not run on the review host): deploy the backend and attach the Coach menu to the sheet per the README.

## Limits and data handling

Commentary lines go to Jev; entity names, periods and emails are not sent; OpenRouter requests set `data_collection: deny`. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-13** (Europe/Sofia) at [commit 74e7a67b1bcf](https://github.com/alexxxram25/working-note/tree/74e7a67b1bcf0a21f4564292ecac6d41768afdf6). Inspected the upstream README, LICENSE (where present), and the Jev integration evidence linked above; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
