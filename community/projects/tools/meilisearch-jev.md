# meilisearch-jev

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

Community CLI companion for Meilisearch that runs a search, asks TypeSafe Jev a yes/no question about at most 20 top hits, and returns accepted `hits` separately from a `review` queue (routes: yes / no / review / failure, default threshold 0.8). README in French, English, and Spanish.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/gbesse/meilisearch-jev) |
| Maintainer | [gbesse](https://github.com/gbesse). Independently curated. |
| Format | Python CLI (`meilisearch_jev.py`) |
| Requirements | Python 3; a Meilisearch instance; `MEILI_API_KEY` and `JEV_API_KEY`. The offline example needs neither. |
| License | [MIT](https://github.com/gbesse/meilisearch-jev/blob/06b5230db7d1dec005e27526dd3a3c7dbbe1fd61/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |

## When to use

- Add a semantic yes/no gate with a human review queue on top of Meilisearch results.
- Mismatch: a companion CLI, not an in-engine Meilisearch plugin.

## How it works

Searches Meilisearch, scores each hit with Jev, routes by threshold; caps calls, timeouts, and response sizes, with an LRU cache keyed by SHA-256 (no raw text stored). (Summarized from the upstream [README](https://github.com/gbesse/meilisearch-jev/blob/06b5230db7d1dec005e27526dd3a3c7dbbe1fd61/README.md); not reproduced here.)

## Get started

From the upstream README (not run on the review host): `python3 -m examples.route_matrix` for the offline demo, or `python meilisearch_jev.py --url ... --index ... --query ... --question ... --field content`.

## Limits and data handling

Hit content is sent to TypeSafe Jev. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-10** (Europe/Sofia) at [commit 06b5230db7d1](https://github.com/gbesse/meilisearch-jev/tree/06b5230db7d1dec005e27526dd3a3c7dbbe1fd61). Inspected the upstream README and LICENSE status at the pinned commit; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
