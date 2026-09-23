# JevTree (Chuf-H)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Jev-native probability tree/graph runtime for finite multi-step decisions: batched TypeSafe Jev action distributions, path mass, merge, and Pareto selection. Distinct from [reachjalil/jev-tree](jev-tree.md) (recursive taxonomy Choice over the 255-option cap).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Chuf-H/jev-tree) |
| Maintainer | [Chuf-H](https://github.com/Chuf-H). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Python package **`jev-tree` 0.1.0** (`jevtree`; CLI `jev-tree`; depends on `typesafe-sdk`). |
| Requirements | Python ≥ 3.10; `TYPESAFE_API_KEY` for live trees; `--provider heuristic` offline smoke needs no key. |
| License | [Apache-2.0](https://github.com/Chuf-H/jev-tree/blob/c129b4d0eed274dcb1500d69b8eef0ed6ef621f8/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Source inspected (README, LICENSE, pyproject). Live Game24/MiniGrid benches and TypeSafe runs were **not** reproduced on the review host. Upstream tables are author-reported. |

## When to use

Use it when local Jev action probs must compose into verifiable multi-step path mass (adapter owns legality, transitions, terminal checks). Prefer [jev-tree](jev-tree.md) (reachjalil) only for hierarchical Choice taxonomies under the flat Choice size limit.

## How it works

Your adapter defines states/actions/transitions/verification. JevTree expands candidates, asks Jev for `P(action|state)`, composes joint path mass, merges equivalent states, tracks unresolved mass, and picks from a Pareto frontier of local probability vs downstream success/risk—not one-step greed alone.

## Get started

```sh
git clone https://github.com/Chuf-H/jev-tree.git
cd jev-tree
git checkout c129b4d0eed274dcb1500d69b8eef0ed6ef621f8
python -m venv .venv && . .venv/bin/activate
python -m pip install -e ".[dev]"
pytest
jev-tree game24 1 2 3 4 --provider heuristic --output /tmp/jev-tree-smoke.json
```

## Examples and demos

- Offline Game24 smoke; `examples/custom_workflow.py`.
- Optional Docker/`demo_server`; author Game24/MiniGrid evidence in README (not reproduced here).

## Limits and data handling

Live search sends state/action descriptions to TypeSafe. Suited to structured enumerable action spaces with a verifier—not open-ended chat. This listing did not call live Jev or claim Opus comparison generality.

## Review and maintenance

Reviewed on **2026-09-23** at [commit c129b4d](https://github.com/Chuf-H/jev-tree/tree/c129b4d0eed274dcb1500d69b8eef0ed6ef621f8) (**0.1.0**, Apache-2.0). AI-assisted source review of README, LICENSE, pyproject. No live TypeSafe spend.

Related: [jev-tree](jev-tree.md), [systemone-harness](systemone-harness.md), [DecideKit](decidekit.md).
