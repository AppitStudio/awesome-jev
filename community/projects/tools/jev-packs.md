# jev-packs

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Evidence-gated registry of Jev question packs: curated questions, golden cases, pinned model versions, and reproducible offline benchmark results across TypeSafe Jev and comparison backends.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/dtduc-git/jev-packs) |
| Maintainer | [dtduc-git](https://github.com/dtduc-git). Independently curated; this page is not an upstream submission or endorsement. |
| Format | Pack registry (`packs/`, `index.json`) + scoreboard (`docs/index.html`) + Python scripts; companion runner [jevassert](https://github.com/dtduc-git/jevassert). |
| Requirements | Packs are YAML/JSONL data (no runtime required to read). Recording/replay uses `jevassert`; live recording needs a TypeSafe (or other backend) key. |
| License | [CC0-1.0](https://github.com/dtduc-git/jev-packs/blob/8b650b1e572443fba629071038e27d886857d8b9/LICENSE) for hand-written packs; dataset-derived packs carry upstream attribution in each pack README. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Offline `scripts/validate.py` and `build_scoreboard.py --check` passed. Benchmark accuracy/cost figures are upstream single-run measurements, not re-measured here. No live TypeSafe calls. |

## When to use

Use it when you need shared, measured question packs for triage, RAG, moderation, or citation checks instead of one-off cookbook criteria. Pair with [jevassert](https://github.com/dtduc-git/jevassert) to record/replay and with [jev-table](jev-table.md) when you want CSV/JSONL columns over the same pack shape. Prefer raw SDK scripts for throwaway experiments.

## How it works

Each pack folder holds `pack.yaml` questions and `cases.jsonl` labels. A pack is marked `verified` in `index.json` only when evidence exists. The scoreboard compares backends (including `jev-1.13.0`) on the same cases; CI fails if `docs/index.html` drifts from `results/`. Spec rules require an `unknown` label on Choice/Score questions.

## Get started

```sh
git clone https://github.com/dtduc-git/jev-packs.git
cd jev-packs
git checkout 8b650b1e572443fba629071038e27d886857d8b9
python3 scripts/validate.py
python3 scripts/build_scoreboard.py --check
```

Browse `packs/` and the committed [scoreboard](https://github.com/dtduc-git/jev-packs/blob/8b650b1e572443fba629071038e27d886857d8b9/docs/index.html). Live recording through `jevassert` sends cases to the configured backend and may incur charges.

## Examples and demos

- Nine verified packs (support-triage, moderation, RAG packs, citation-support, entity-merge, and dataset-derived packs).
- `results/` per-backend metrics and `review/FINDINGS.md` methodology write-up.
- Offline validate + scoreboard check (run in this review).

## Limits and data handling

Pack metrics are pinned recordings, not continuous live leaderboards. Dataset-derived packs follow upstream licenses—read each pack README. Live recording transmits case text to the backend. This listing does not re-validate statistical claims in FINDINGS.md.

## Review and maintenance

Reviewed on **2026-09-21** at [commit 8b650b1](https://github.com/dtduc-git/jev-packs/tree/8b650b1e572443fba629071038e27d886857d8b9): CC0-1.0. AI-assisted review of README, `index.json`, pack layout, LICENSE, and scripts. **`python3 scripts/validate.py`**: OK (9 packs, 3 backends). **`build_scoreboard.py --check`**: docs/index.html up to date. No live TypeSafe.

Related: [jev-table](jev-table.md), [jeval](jeval.md), [Jevaluate](jevaluate.md).
