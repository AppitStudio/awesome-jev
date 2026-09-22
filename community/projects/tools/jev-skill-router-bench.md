# jev-skill-router-bench

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Independent, reproducible measurement of a Jev (TypeSafe System One) skill router on one 84-skill Hermes roster: 81 author-labelled turns, router scorecard artifacts, and an inconclusive agent-level appendix—not a vendor benchmark replica.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/OrMizL/jev-skill-router-bench) |
| Maintainer | [OrMizL](https://github.com/OrMizL). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Python tooling + committed JSONL/report artifacts under `p1/` and `p2/`. |
| Requirements | Python 3 for aggregation scripts; raw private mined turn text is withheld (placeholders in public files). Re-running live router calls needs whatever credentials the measured router stack uses (not exercised here). |
| License | [MIT](https://github.com/OrMizL/jev-skill-router-bench/blob/3266a69152d80078548c348583872ef2643c0c84/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation with TypeSafe AI or plugin authors. Listing is not an endorsement. Did not re-run live router or agent arms; treat published rates as author-reported for this hand-labelled set. |

## When to use

Use it when you need an inspectable scorecard and methodology critique for a Jev skill-routing setup on Hermes-like rosters. Prefer [jev-skill-gate](jev-skill-gate.md) / [jev-skill-scout](jev-skill-scout.md) for operational gating/auditing, and [jev-agent-failure-benchmark](jev-agent-failure-benchmark.md) for different failure-attribution benches.

## How it works

Committed `p1/` labels and router scores support deterministic aggregation scripts; README/CLAIM state the descriptive rates (e.g. top-1 on skill-labelled turns, abstentions vs mis-suggestions) and explicitly withhold private mined turn text. Agent-level `p2/` appendix is disclosed as noisy/inconclusive.

## Get started

```sh
git clone https://github.com/OrMizL/jev-skill-router-bench.git
cd jev-skill-router-bench
git checkout 3266a69152d80078548c348583872ef2643c0c84
# Read README.md / CLAIM.md / p1/REPORT.md; run aggregation helpers under p1/ as documented upstream.
ls p1/*.jsonl p1/REPORT.md
```

## Examples and demos

- `p1/REPORT.md`, `labels.jsonl`, `router-scores.jsonl` — published router-level artifacts.
- `p2/` — agent-level pilot appendix (author-reported variance).

## Limits and data handling

Hand-selected labels; not a random sample; no independent adjudication. Private user turns withheld. Stochastic router draws; single-pass disclosure. Do not treat figures as production accuracy or as a direct comparison to vendor-published numbers. This listing did not replay live router calls.

## Review and maintenance

Reviewed on **2026-09-22** at [commit 3266a69](https://github.com/OrMizL/jev-skill-router-bench/tree/3266a69152d80078548c348583872ef2643c0c84) (MIT). AI-assisted review of README, CLAIM.md, LICENSE, and `p1/` artifact layout. No live TypeSafe/Hermes replay.

Related: [jev-skill-gate](jev-skill-gate.md), [jev-skill-scout](jev-skill-scout.md), [Hermes Jev Skills](hermes-jev-skills.md), [jev-agent-failure-benchmark](jev-agent-failure-benchmark.md).
