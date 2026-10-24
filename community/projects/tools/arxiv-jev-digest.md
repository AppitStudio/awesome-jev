# arXiv Jev Digest (daily arXiv screening with Jev, summaries by email)

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

GitHub Actions job that has Jev judge each new arXiv paper in your field against your research interests, filters and ranks by relevance and verified author institutions, then has DeepSeek write structured summaries and emails the top picks.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Monkeypox966/arxiv-jev-digest) |
| Maintainer | [Monkeypox966](https://github.com/Monkeypox966). Independently curated. |
| Format | Python job on GitHub Actions |
| Requirements | A GitHub repository with Actions; TypeSafe (or OpenRouter), DeepSeek and SMTP credentials. |
| License | [MIT](https://github.com/Monkeypox966/arxiv-jev-digest/blob/32944ba67d5418f3caf745c7016725d7391683fe/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/arxiv_digest/clients.py`](https://github.com/Monkeypox966/arxiv-jev-digest/blob/32944ba67d5418f3caf745c7016725d7391683fe/src/arxiv_digest/clients.py) at the pinned commit. |

## When to use

- Get a short daily list of relevant papers instead of reading the full feed.
- Tune interests, thresholds and institution weights in config.
- Mismatch: summaries are based on abstracts only; docs are in Chinese.

## How it works

`config.toml` sets `https://api.typesafe.ai/v1/systemone` with `jev-1.14.0` (or `typesafe/jev-1.14` via OpenRouter); `clients.py` sends one yes/no question per interest, and code combines the probabilities. Integration evidence: [`src/arxiv_digest/clients.py`](https://github.com/Monkeypox966/arxiv-jev-digest/blob/32944ba67d5418f3caf745c7016725d7391683fe/src/arxiv_digest/clients.py).

## Get started

From the upstream README (not run on the review host):

```sh
cp .env.example .env   # TYPESAFE_API_KEY, DEEPSEEK_API_KEY, SMTP_*
# or set them as GitHub Secrets and enable the daily workflow
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README (Chinese): [github.com/Monkeypox966/arxiv-jev-digest#readme](https://github.com/Monkeypox966/arxiv-jev-digest#readme)

## Limits and data handling

Paper titles and abstracts go to TypeSafe and DeepSeek. Default config tracks humanoid robotics in cs.RO.

## Review and maintenance

Reviewed **2026-10-24** (Europe/Sofia) at [commit 32944ba67d54](https://github.com/Monkeypox966/arxiv-jev-digest/tree/32944ba67d5418f3caf745c7016725d7391683fe). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
