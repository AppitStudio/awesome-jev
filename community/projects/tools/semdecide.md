# SemDecide

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

CLI that turns TypeSafe Jev typed judgments into Unix-friendly predicates, routes, scores, and JSONL filters for pipelines and CI—stable exit codes without hand-rolled prompt parsing.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/sharziki/semdecide) |
| Maintainer | [sharziki / Sharvil Saxena](https://github.com/sharziki). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Python CLI package **semdecide 0.2.1** (`is` / `choose` / `score` / `filter`; GitHub release wheel; not yet on PyPI). |
| Requirements | Python ≥ 3.10; live calls need `TYPESAFE_API_KEY` (or `~/.config/typesafe/credentials.env`). |
| License | [MIT](https://github.com/sharziki/semdecide/blob/33cf5c03c50e02e59df3f3ea81f0650f6b791545/LICENSE). |

## When to use

Use it when shell or CI steps need semantic yes/no, multi-option routing, ordered rubrics, or JSONL filtering with predictable process exits. Prefer [jegrep](jegrep.md) / [jev-semgrep](jev-semgrep.md) for searching or filtering *source lines* by meaning, and [typesafe-cli](typesafe-cli.md) for a general shell `jev` asker. Do not treat probabilities as audited security or compliance determinations.

## How it works

[`src/reflex_guard/providers/typesafe.py`](https://github.com/sharziki/semdecide/blob/33cf5c03c50e02e59df3f3ea81f0650f6b791545/src/reflex_guard/providers/typesafe.py) posts to `https://api.typesafe.ai/v1/systemone`, validates answer shapes, and maps them into CLI verdicts. Application policy owns thresholds, uncertainty margins, retries, and exit codes—Jev does not invent options or silently force borderline results.

## Get started

```sh
# release wheel (see upstream README), or from source:
git clone https://github.com/sharziki/semdecide.git
cd semdecide
git checkout 33cf5c03c50e02e59df3f3ea81f0650f6b791545
python3 -m venv .venv && .venv/bin/pip install -e .
export TYPESAFE_API_KEY=…   # live inference
printf '%s' 'Login from a new country, followed by payout changes.' \
  | semdecide is 'This describes a plausible account takeover'
```

Live commands send piped text to TypeSafe and can incur charges. This listing did not run live inference.

## Examples and demos

- README `is` / `choose` / `score` / `filter` examples with `--json` schemas.
- Offline tests under `tests/` (`test_v02.py`, `test_reflex.py`).
- Architecture notes in `docs/`.

## Limits and data handling

Piped content leaves the host for TypeSafe. Keep credentials in the environment or a mode-`600` credentials file—not CLI argv. Upstream latency/cost claims were not reproduced here. Pin a model when calibrating thresholds (`jev` aliases can move).

## Review and maintenance

Reviewed on **2026-09-20** at [commit 33cf5c03](https://github.com/sharziki/semdecide/tree/33cf5c03c50e02e59df3f3ea81f0650f6b791545): **0.2.1**, MIT. AI-assisted source review of README, `providers/typesafe.py`, `pyproject.toml`, license, and tests inventory. Offline pytest and live TypeSafe calls were not executed on the review host.

Related: [typesafe-cli](typesafe-cli.md), [jegrep](jegrep.md), [jev-semgrep](jev-semgrep.md).
