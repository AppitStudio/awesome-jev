# jev-vs-pii (Jev for PII detection benchmark)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Reproducible benchmark of Jev against rules, local PII models and LLMs for finding personal information; on court judgments Jev ties Claude Haiku 4.5 on F2, runs about six times faster and leaves the least personal information unmasked, while larger LLMs stay ahead on short synthetic text.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/AlanViollier/jev-vs-pii) |
| Maintainer | [AlanViollier](https://github.com/AlanViollier). Independently curated. |
| Format | Benchmark and report (Python, uv) |
| Requirements | Python with uv; an OpenRouter key for the paid lanes (about $7.40 for a full rerun). |
| License | [MIT](https://github.com/AlanViollier/jev-vs-pii/blob/109d27931272baf63d34b5d772c8313b8caf30f3/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`jev_vs_pii/clients/decisions.py`](https://github.com/AlanViollier/jev-vs-pii/blob/109d27931272baf63d34b5d772c8313b8caf30f3/jev_vs_pii/clients/decisions.py) at the pinned commit. |

## When to use

- Decide whether a decision model fits an anonymisation scope before building one.
- Reuse the prompt-design lessons (one extra answer option moved F2 from 0.84 to 0.91).
- Mismatch: a comparison of approaches, not a production anonymiser; no method was chosen for GDPR terms.

## How it works

Each lane runs on the same datasets; the Jev lane (`typesafe/jev-1.13` via OpenRouter, see `config.py` and `clients/decisions.py`) answers per-word typed questions, and the report compares F2, leakage, latency and cost. Integration evidence: [`jev_vs_pii/clients/decisions.py`](https://github.com/AlanViollier/jev-vs-pii/blob/109d27931272baf63d34b5d772c8313b8caf30f3/jev_vs_pii/clients/decisions.py).

## Get started

From the upstream README (not run on the review host):

```sh
uv sync --extra dev --extra ner
uv run jev-vs-pii fetch
make bench-free   # rules and local models only, $0
make bench        # full rerun with OpenRouter
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Interactive race page: [alanviollier.github.io/jev-vs-pii/race/](https://alanviollier.github.io/jev-vs-pii/race/)
- Findings in the README: [github.com/AlanViollier/jev-vs-pii#readme](https://github.com/AlanViollier/jev-vs-pii#readme)

## Limits and data handling

Paid lanes send dataset text to third-party APIs through OpenRouter. Results are the author's runs and will age as models change.

## Review and maintenance

Reviewed **2026-10-22** (Europe/Sofia) at [commit 109d27931272](https://github.com/AlanViollier/jev-vs-pii/tree/109d27931272baf63d34b5d772c8313b8caf30f3). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
