# jev-vs-clef

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Head-to-head stress comparison of TypeSafe Jev (via the Vercel AI Gateway) and Cloudflare Workers AI Clef (27B) / Clef-flash (9B) on synthetic, production-shaped decisions: an identical 159-call battery run in Clef's launch week and again on 2026-10-06, covering edge cases (64-question max, bad-image 422, vision, array state) and a wire gap around `noul` in the swap story, with raw calls and per-call cost published.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/rmax-ai/jev-vs-clef) |
| Maintainer | [rmax-ai](https://github.com/rmax-ai). Independently curated. |
| Format | Python harness (`harness/stress.py`, `harness/vision_demo.py`) with dated results |
| Requirements | Python 3, direnv (optional); Vercel AI Gateway key for Jev and a Cloudflare account/token for Clef. |
| License | The reviewed tree has **no LICENSE file** — listed as Source available; reuse terms are not granted until the maintainer adds a license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Check swap compatibility before moving decisions to Clef.
- Reuse the edge-case battery against another System One–compatible endpoint.
- Mismatch: synthetic tasks; quality numbers are the author's runs.

## How it works

[`harness/jev_client.py`](https://github.com/rmax-ai/jev-vs-clef/blob/58ddaec44e9f806241d5c9749c432bf7828c3ec3/harness/jev_client.py) calls Jev over plain HTTP; the stress harness has a dry-run cost guard and writes reports and `calls.jsonl` under [`results/`](https://github.com/rmax-ai/jev-vs-clef/tree/58ddaec44e9f806241d5c9749c432bf7828c3ec3/results).

## Get started

Configure keys and run the smoke phase (README):

```sh
git clone https://github.com/rmax-ai/jev-vs-clef.git && cd jev-vs-clef
cp .envrc.example .envrc   # add your keys
direnv exec . python3 harness/stress.py --dry-run
direnv exec . python3 harness/stress.py --phases smoke
```

Live runs bill the Vercel AI Gateway (Jev) and Cloudflare (Clef); the vision demo costs about $0.0004.

## Examples and demos

- [Launch run report](https://github.com/rmax-ai/jev-vs-clef/blob/58ddaec44e9f806241d5c9749c432bf7828c3ec3/results/run-20261003-main/report.md).
- [Vision demo](https://github.com/rmax-ai/jev-vs-clef/blob/58ddaec44e9f806241d5c9749c432bf7828c3ec3/VISION-DEMO.md).

## Limits and data handling

Synthetic prompts only. No LICENSE file. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-08** (Europe/Sofia) at [commit 58ddaec44e9f](https://github.com/rmax-ai/jev-vs-clef/tree/58ddaec44e9f806241d5c9749c432bf7828c3ec3). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
