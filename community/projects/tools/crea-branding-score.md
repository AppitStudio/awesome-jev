# crea-branding-score (0-100 branding score for video ads, with Jev checking each frame for the logo)

[All projects](../README.md) · [Customer feedback and marketing](README.md#customer-feedback-and-marketing)

Scores how much a set of video ads shows a brand: speech-to-text finds brand mentions in the voice-over, and Jev answers typed questions on each frame (is the logo visible, compared with your reference logos) through OpenRouter's Decisions API; outputs a per-ad score with a breakdown, group averages and an HTML report.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Bryan21B/crea-branding-score) |
| Maintainer | [Bryan21B](https://github.com/Bryan21B). Independently curated. |
| Format | Python CLI (uv) |
| Requirements | Python with uv; an OpenRouter key for Jev (image input is a preview feature). |
| License | [MIT](https://github.com/Bryan21B/crea-branding-score/blob/92a3ae43a0c0075f34de83199bde2a47d37eedbe/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`cbs/visual_llm.py`](https://github.com/Bryan21B/crea-branding-score/blob/92a3ae43a0c0075f34de83199bde2a47d37eedbe/cbs/visual_llm.py) at the pinned commit. |

## When to use

- Audit branding across a batch of creator or UGC ads.
- Mismatch: Jev does not tell which logo version it sees; image input is a Jev preview feature.

## How it works

`cbs/visual_llm.py` sends frames and reference logos to `~typesafe/jev-latest` via OpenRouter's Decisions API (set by `decisions_model` in `config.yaml`); weights live in the config. Integration evidence: [`cbs/visual_llm.py`](https://github.com/Bryan21B/crea-branding-score/blob/92a3ae43a0c0075f34de83199bde2a47d37eedbe/cbs/visual_llm.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/Bryan21B/crea-branding-score && cd crea-branding-score
uv sync
uv run cbs run --limit 3
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/Bryan21B/crea-branding-score#readme](https://github.com/Bryan21B/crea-branding-score#readme)

## Limits and data handling

Video frames and logos go to OpenRouter and TypeSafe. The README estimates about $0.018 per minute of video.

## Review and maintenance

Reviewed **2026-10-28** (Europe/Sofia) at [commit 92a3ae43a0c0](https://github.com/Bryan21B/crea-branding-score/tree/92a3ae43a0c0075f34de83199bde2a47d37eedbe). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
