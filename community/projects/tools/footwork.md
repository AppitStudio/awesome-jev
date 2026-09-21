# Footwork

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

Dual-process browser agent: TypeSafe Jev acts as a fast System 1 chooser over a code-built menu, while browser-use's LLM loop remains System 2; a code-owned arbiter picks which system acts and evidence-based verification must pass before a run is marked done.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Tom-R-Main/Footwork) |
| Maintainer | [Tom-R-Main](https://github.com/Tom-R-Main). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Python package **`jevdual` 0.0.1** (PyO3/Rust hot paths + pure-Python twins) on top of pinned `browser-use==0.13.10`. |
| Requirements | Python ≥ 3.11; `uv` recommended. Live System 1 needs `TYPESAFE_API_KEY`; System 2 needs a browser-use LLM key (`META_MODEL_API_KEY` / `OPENAI_API_KEY` per upstream). |
| License | [MIT](https://github.com/Tom-R-Main/Footwork/blob/11efd0681aa30ba553f585365154ca6e3364383e/LICENSE). TypeSafe and LLM provider usage billed separately. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Offline `uv run pytest` in `jevdual/` at the reviewed commit: **269 passed**, **21 skipped**, **1 failed** (`test_upstream_import_is_judge_graded_and_reproducible` — Mind2Web import script non-zero). No live TypeSafe or browser-use agent runs here. Upstream `results/` tables are author-reported, not re-measured. |

## When to use

Use it when you want calibrated Jev judgments (operation/target Choice plus situation Nouls) in front of a deliberate browser-use loop, with a destructive gate and evidence checks before “done”. Prefer [Jev Ultrafast](jev-ultrafast.md) or [jevnav](jevnav.md) for lighter single-stack browser agents; prefer [JevOnly](jevonly.md) when there should be no helper LLM at all.

## How it works

[`policy.py`](https://github.com/Tom-R-Main/Footwork/blob/11efd0681aa30ba553f585365154ca6e3364383e/jevdual/python/jevdual/policy.py) builds one `system_one` request per step (operation/target Choice plus situation Nouls) via `typesafe_sdk`. [`arbiter.py`](https://github.com/Tom-R-Main/Footwork/blob/11efd0681aa30ba553f585365154ca6e3364383e/jevdual/python/jevdual/arbiter.py) decides whether System 1 or System 2 acts. [`verify.py`](https://github.com/Tom-R-Main/Footwork/blob/11efd0681aa30ba553f585365154ca6e3364383e/jevdual/python/jevdual/verify.py) asks Jev whether completion claims match page evidence before marking success. DOM hot paths may run in Rust through PyO3 with equality tests against pure Python.

## Get started

```sh
git clone --recurse-submodules https://github.com/Tom-R-Main/Footwork.git
cd Footwork
git checkout 11efd0681aa30ba553f585365154ca6e3364383e
cd jevdual && uv sync && uv run pytest
```

Live agent loops send page/goal context to TypeSafe and to the System 2 LLM provider and can incur charges.

## Examples and demos

- `jevdual/README.md` and `results/` — author-reported arm comparisons (S1-only / stock / dual); not re-run here.
- Offline pytest suite under `jevdual/tests/` (mostly no network).

## Limits and data handling

Page snapshots, goals, and candidate menus leave the host on live Jev and LLM calls. Upstream notes dual mode is not automatically cheaper than stock browser-use on their splits. This listing did not reproduce the published pass/cost tables.

## Review and maintenance

Reviewed on **2026-09-21** at [commit 11efd06](https://github.com/Tom-R-Main/Footwork/tree/11efd0681aa30ba553f585365154ca6e3364383e) (`jevdual` 0.0.1, MIT). AI-assisted source review of README, LICENSE, `policy.py`, `arbiter.py`, `verify.py`. Offline pytest: 269 passed / 21 skipped / 1 failed as above. No live provider calls.

Related: [Jev Ultrafast](jev-ultrafast.md), [jevnav](jevnav.md), [JevOnly](jevonly.md), [jev-ra](jev-ra.md).
