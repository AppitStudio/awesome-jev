# jev-vs-cosine (zero-cost Banking77 benchmark of Jev against cosine similarity and small trained classifiers)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Reproducible benchmark on Banking77 intent routing comparing Jev with embedding cosine similarity, a cross-encoder reranker and a logistic-regression classifier. Jev answered all 1,001 test messages through a free route: with no examples it scored 83.3% against 73.2% for cosine over category descriptions, but a free classifier trained on five labelled examples per category matched it (84.2%). Includes a threshold and cascade triage report.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Madheshvivekanandan/jev-vs-cosine) |
| Maintainer | [Madheshvivekanandan](https://github.com/Madheshvivekanandan). Independently curated. |
| Format | Python benchmark (CLI) |
| Requirements | Python 3; Jev through the free OpenCode route by default, or TypeSafe, Vercel AI Gateway or OpenRouter. |
| License | [MIT](https://github.com/Madheshvivekanandan/jev-vs-cosine/blob/911e91b1093622c605c10067b960c0aff660fc1d/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`app/clients/typesafe_jev_decider.py`](https://github.com/Madheshvivekanandan/jev-vs-cosine/blob/911e91b1093622c605c10067b960c0aff660fc1d/app/clients/typesafe_jev_decider.py) at the pinned commit. |

## When to use

- Decide whether an intent router needs Jev or whether a few labelled examples and embeddings are enough.
- Mismatch: one dataset (Banking77, 77 English banking intents); results may not carry to other domains.

## How it works

`typesafe_jev_decider.py` uses the TypeSafe SDK with an allow-listed host to ask Jev a 77-way choice per message, caching answers so interrupted runs resume; cosine, cross-encoder and trained methods run locally. Integration evidence: [`app/clients/typesafe_jev_decider.py`](https://github.com/Madheshvivekanandan/jev-vs-cosine/blob/911e91b1093622c605c10067b960c0aff660fc1d/app/clients/typesafe_jev_decider.py).

## Get started

From the upstream README (not run on the review host):

```sh
python3 -m venv .venv && .venv/bin/pip install -e ".[dev]"
cp .env.example .env
.venv/bin/python -m app.main download
.venv/bin/python -m app.main run-jev --limit 20 --dry-run
.venv/bin/python -m app.main report
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Results report: [github.com/Madheshvivekanandan/jev-vs-cosine/blob/911e91b1093622c605c10067b960c0aff660fc1d/results/REPORT.md](https://github.com/Madheshvivekanandan/jev-vs-cosine/blob/911e91b1093622c605c10067b960c0aff660fc1d/results/REPORT.md)

## Limits and data handling

Banking77 test messages are sent to the configured Jev route. The free OpenCode route is rate-limited (about 250 requests per IP per day per the README). Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-10-30** (Europe/Sofia) at [commit 911e91b10936](https://github.com/Madheshvivekanandan/jev-vs-cosine/tree/911e91b1093622c605c10067b960c0aff660fc1d). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
