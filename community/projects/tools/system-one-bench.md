# System One Bench (independent benchmark for decision models, including Jev)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Independent benchmark that sends byte-identical System One requests to decision models (Jev 1.13 and 1.14, OpenAI, Perplexity, Liquid AI and Cloudflare decision models, Laya variants and others) and reports accuracy, calibration, latency and cost on frozen text and image suites, with a public leaderboard.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/alilibx/system-one-bench) |
| Maintainer | [alilibx](https://github.com/alilibx). Independently curated. |
| Format | Benchmark scripts, frozen data and leaderboard site (Python; code Apache-2.0, results CC BY 4.0) |
| Requirements | Python, the pinned data from `data.lock.json`, and keys for the services you re-run (OpenRouter for Jev). |
| License | [Apache-2.0](https://github.com/alilibx/system-one-bench/blob/40d9b094b51f177b483136ff8441614661ab48a3/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`run_decisions.py`](https://github.com/alilibx/system-one-bench/blob/40d9b094b51f177b483136ff8441614661ab48a3/run_decisions.py) at the pinned commit. |

## When to use

- Compare decision models on the same frozen cases before picking one.
- Check calibration and latency, not only accuracy.
- Mismatch: benchmark results are the maintainer's own; your data may differ.

## How it works

`build_suites.py` turns every case into one `POST /v1/systemone` body plus gold labels; `run_decisions.py` replays the suites against a model such as `typesafe/jev-1.14` and `score.py` computes the published results. Integration evidence: [`run_decisions.py`](https://github.com/alilibx/system-one-bench/blob/40d9b094b51f177b483136ff8441614661ab48a3/run_decisions.py).

## Get started

Clone the repo, set up the venv from the README, and re-score or re-run the suites.

```sh
git clone https://github.com/alilibx/system-one-bench && cd system-one-bench
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Leaderboard: [systemonebench.dev/](https://systemonebench.dev/)

## Limits and data handling

Re-running sends benchmark cases (public datasets) to the providers you choose.

## Review and maintenance

Reviewed **2026-11-12** (Europe/Sofia) at [commit 40d9b094b51f](https://github.com/alilibx/system-one-bench/tree/40d9b094b51f177b483136ff8441614661ab48a3). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
