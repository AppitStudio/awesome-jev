# jev-ticket-triage

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Reproducible support-ticket triage eval: TypeSafe Jev vs Together.ai LLMs on accuracy/cost/latency/confidence (WIP).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/beese54/jev-ticket-triage) |
| Maintainer | [beese54](https://github.com/beese54). Independently curated. |
| Format | Python evaluation / benchmark harness. |
| Requirements | uv; TYPESAFE_API_KEY and/or TOGETHER_API_KEY for live runs; datasets keep their own licenses. |
| License | [MIT](https://github.com/beese54/jev-ticket-triage/blob/b7c887632ee1d9970fe52b119c65ca9cbe51c66e/LICENSE). TypeSafe usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live TypeSafe/provider paths not run on the review host. |

## When to use

Use to **measure** whether System One triage beats LLM baselines on cost/latency/confidence. WIP—not a drop-in production triage bot.

## How it works

Runs Choice/Score/Noul triage questions with `jev-latest` against Together LLM baselines on public ticket datasets; records smoke and planned metrics.

## Get started

```sh
git clone https://github.com/beese54/jev-ticket-triage.git
cd jev-ticket-triage
git checkout b7c887632ee1d9970fe52b119c65ca9cbe51c66e
# uv sync; cp .env.example .env; uv run python scripts/p0_smoke.py
```

## Examples and demos

- Upstream README quickstart and examples at the pinned commit.
- Separate interactive demos only where the upstream README links them; none were executed on the review host.

## Limits and data handling

Live Jev/TypeSafe (or other provider) calls send the judged text/state to that provider and may incur charges. Offline/demo paths stay local when documented upstream. Catalog checks did not run live integrations.

## Review and maintenance

Reviewed **2026-09-26** (Europe/Sofia) at [commit b7c8876](https://github.com/beese54/jev-ticket-triage/tree/b7c887632ee1d9970fe52b119c65ca9cbe51c66e). AI-assisted README and license inspection; install/live paths not executed.
