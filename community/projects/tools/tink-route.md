# tink-route

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Confidence-aware Agent Skills router: keep a cold skill library offline, ask TypeSafe Jev whether a specialist skill is needed, then optionally install only the winning skill via [Tink](https://github.com/jon-devlapaz/tink).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/jon-devlapaz/tink-route) |
| Maintainer | [jon-devlapaz](https://github.com/jon-devlapaz). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Python CLI **`tink-route` 0.3.1** (MIT); stdlib HTTP client (no runtime dependency declared). |
| Requirements | Python ≥ 3.11; live routing needs `TYPESAFE_API_KEY`. Skill install/prune paths need a working [Tink](https://github.com/jon-devlapaz/tink) skill library under `~/.tink/skills/`. |
| License | [MIT](https://github.com/jon-devlapaz/tink-route/blob/13b4f7d996bc2110f5065846d1877a8a8f91ab24/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source and offline pytest inspected. Live TypeSafe calls and Tink installs were not run. Upstream latency/accuracy tables were not reproduced. |

## When to use

Use it when progressive disclosure of many Agent Skills bloats every turn’s system prompt and you want a two-stage Jev gate (specialist needed? → which skill?) before mutating `.agents/skills/`. Prefer [Skill Dash](skill-dash.md) or [SkillRanker](skillranker.md) when you want to *judge* skills rather than install them on demand.

## How it works

[`client.py`](https://github.com/jon-devlapaz/tink-route/blob/13b4f7d996bc2110f5065846d1877a8a8f91ab24/src/tink_route/client.py) POSTs to TypeSafe System One (default model `jev-1.13.0`). Stage 1 is a Noul (`specialist_needed`); below the threshold the CLI exits without loading skills. Stage 2 is a Choice over library candidates. Optional `--install` calls `tink skill add`; ephemeral installs can be pruned later. Exit codes separate routed / unrouted / operational failure for scripting.

## Get started

```sh
git clone https://github.com/jon-devlapaz/tink-route.git
cd tink-route
git checkout 13b4f7d996bc2110f5065846d1877a8a8f91ab24
python3 -m pip install -e .
python3 -m pytest -q
```

Live routing:

```sh
export TYPESAFE_API_KEY=...
tink-route "Fix off-by-one bug in binary search"   # often no_skill_needed
# charges: sends the task string (and candidate skill metadata) to TypeSafe
```

## Examples and demos

- README JSON/`--json` contract and exit-code branching examples.
- [`tests/test_tink_route.py`](https://github.com/jon-devlapaz/tink-route/blob/13b4f7d996bc2110f5065846d1877a8a8f91ab24/tests/test_tink_route.py) offline unit coverage.
- [`tests/ab_eval.py`](https://github.com/jon-devlapaz/tink-route/blob/13b4f7d996bc2110f5065846d1877a8a8f91ab24/tests/ab_eval.py) / `results/` — author-reported A/B numbers; not re-run here.

## Limits and data handling

Task text and skill candidate descriptions leave the host on live calls. Thresholds and install mutations are local policy. A/B prompt-overhead and accuracy figures in the README are upstream measurements, not catalog checks.

## Review and maintenance

Reviewed on **2026-09-22** at [commit 13b4f7d](https://github.com/jon-devlapaz/tink-route/tree/13b4f7d996bc2110f5065846d1877a8a8f91ab24) / tag **v0.3.1**. AI-assisted source review of README, `src/tink_route/`, and tests. On the review host: **`pytest -q` → 10 passed**. No live TypeSafe or Tink install runs.

Related: [Skill Dash](skill-dash.md), [SkillRanker](skillranker.md), [pi-jev-router](pi-jev-router.md).
