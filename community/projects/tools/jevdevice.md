# jevdevice

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

MCP harness that turns a plain-language device goal into exactly one gated action on a live Android phone (adb) or the local shell: TypeSafe Jev (default) or an in-process Laya checkpoint picks among candidates discovered at runtime; ordinary code denies, executes, and verifies.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Xopher00/jevdevice) |
| Maintainer | [Xopher00](https://github.com/Xopher00). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Python package **`jevdevice` 0.1.0** (MCP entrypoint `jevdevice-mcp`). |
| Requirements | Python ≥ 3.12; `uv` recommended. Jev engine needs `TYPESAFE_AI_API`. Laya engine needs no TypeSafe key (`JEV_ENGINE=laya`). Android path needs adb / uiautomator2. |
| License | [MIT](https://github.com/Xopher00/jevdevice/blob/b3f846a424621008732b2bde3515470f213341b0/LICENSE). TypeSafe usage billed separately when using the hosted engine. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Offline `uv run pytest`: **192 passed**, **1 failed** (`test_mcp_approval_flow` JSON decode). No live TypeSafe calls and no physical device exercised here. |

## When to use

Use it when an LLM agent should control a real Android device (or local shell) without hard-coded coordinates or resource IDs — candidates come from the live accessibility tree or a frozen CLI set. Prefer [jev-android](jev-android.md) / [Mobile Jev](mobile-jev.md) for other Android stacks; prefer browser listings under this category for web automation.

## How it works

[`jev.py`](https://github.com/Xopher00/jevdevice/blob/b3f846a424621008732b2bde3515470f213341b0/src/jevdevice/jev.py) posts typed Noul/Choice/Score questions to `https://api.typesafe.ai/v1/systemone` (model pinned, default `jev-1.13.0`). The pipeline enumerates device state, asks the judge to pick one real candidate, applies a deny-list plus a safety judgment, then executes and verifies against device truth. `JEV_ENGINE=laya` swaps in a local checkpoint with the same question contract.

## Get started

```sh
git clone https://github.com/Xopher00/jevdevice.git
cd jevdevice
git checkout b3f846a424621008732b2bde3515470f213341b0
uv sync --group dev
uv run pytest
# Live MCP (needs key + device): uv run jevdevice-mcp
```

Live Jev runs send device snapshots / candidate text to TypeSafe and can incur charges.

## Examples and demos

- README pipeline and judge-engine notes.
- Offline tests under `tests/` (mostly mocked; one MCP approval-flow failure observed here).

## Limits and data handling

Accessibility trees, command candidates, and goals leave the host on the hosted Jev engine. Uncertain safety judgments require human approval rather than auto-run. This listing did not validate against a physical phone.

## Review and maintenance

Reviewed on **2026-09-21** at [commit b3f846a](https://github.com/Xopher00/jevdevice/tree/b3f846a424621008732b2bde3515470f213341b0) (0.1.0, MIT). AI-assisted source review of README, LICENSE, `jev.py`, `common.py`. Offline pytest: 192 passed / 1 failed as above. No live provider or device runs.

Related: [jev-android](jev-android.md), [Mobile Jev](mobile-jev.md), [typesafe-computer-use](typesafe-computer-use.md).
