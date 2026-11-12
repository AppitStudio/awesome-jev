# Apartment Hunter (ranks NYC rentals from StreetEasy and Zillow by your weights, with Jev judgments and photo checks)

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

Local Python tool that reads StreetEasy and Zillow listings through your own Chrome, adds computed data such as subway walk and floor, checks photos with a vision model and Jev, and ranks rentals into tiers on a map by the limits and priority sliders you set.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/itsmartinwho/apartment-hunter) |
| Maintainer | [itsmartinwho](https://github.com/itsmartinwho). Independently curated. |
| Format | Local Python web UI run with `uv` (MIT) |
| Requirements | Python with `uv`, Chrome with remote debugging allowed, `TYPESAFE_API_KEY` and an OpenRouter key (`TEXT_MODEL_API_KEY`) for the text helper and vision model. |
| License | [MIT](https://github.com/itsmartinwho/apartment-hunter/blob/1d095c63494cd0b3a8b16bac9857b9ab577aec11/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`apartment_hunter/jev.py`](https://github.com/itsmartinwho/apartment-hunter/blob/1d095c63494cd0b3a8b16bac9857b9ab577aec11/apartment_hunter/jev.py) at the pinned commit. |

## When to use

- Rank a New York apartment search by your own priorities instead of the sites' sort order.
- Mismatch: other cities or unattended scraping; it targets NYC sources through your own browser.

## How it works

`apartment_hunter/jev.py` sends each listing's state, observations and photos to `https://api.typesafe.ai/v1/systemone`, validates the returned scores, and also uses Jev to interpret a free-text search description into limits and weights; ranking and tiers are computed in code. Integration evidence: [`apartment_hunter/jev.py`](https://github.com/itsmartinwho/apartment-hunter/blob/1d095c63494cd0b3a8b16bac9857b9ab577aec11/apartment_hunter/jev.py).

## Get started

Install with `uv`, add both keys to `.env`, check the setup, then start the local page and click Search.

```sh
uv sync
uv run hunt --check
uv run hunt
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README with screenshot: [github.com/itsmartinwho/apartment-hunter/blob/1d095c63494cd0b3a8b16bac9857b9ab577aec11/README.md](https://github.com/itsmartinwho/apartment-hunter/blob/1d095c63494cd0b3a8b16bac9857b9ab577aec11/README.md)

## Limits and data handling

Listing text and photos go to TypeSafe and OpenRouter on your keys. It drives your Chrome via remote debugging in background tabs; check StreetEasy's and Zillow's terms before use.

## Review and maintenance

Reviewed **2026-11-13** (Europe/Sofia) at [commit 1d095c63494c](https://github.com/itsmartinwho/apartment-hunter/tree/1d095c63494cd0b3a8b16bac9857b9ab577aec11). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
