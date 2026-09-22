# Codex Jev Preflight

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Fail-open Codex `UserPromptSubmit` hook that asks TypeSafe Jev for advisory `task_type`, `complexity`, `risk`, and `execution_mode` before each task—never blocks on Jev/network/quota errors.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/wellkilo/codex-jev-preflight) |
| Maintainer | [wellkilo](https://github.com/wellkilo). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Python stdlib Codex hook (`jev_user_prompt_hook.py`) plus installer/config helpers and optional browser-workflow helpers. |
| Requirements | Python 3.9+; Codex CLI with hooks; `TYPESAFE_API_KEY` (private env via `configure_jev.py`, default endpoint `https://api.typesafe.ai/v1/systemone`, model `jev-latest`). |
| License | [MIT](https://github.com/wellkilo/codex-jev-preflight/blob/633ddefe6596aa5d7c6b00767c08d07edea61096/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not endorsement. Offline pytest run on the review host; live Codex/TypeSafe not exercised. Distinct from [jev-preflight](jev-preflight.md) (Claude Code Stop risk scores). |

## When to use

Use it when every Codex task should receive a **compact, advisory Jev routing assessment** without risking a blocked prompt. Prefer [codex-jev-router](codex-jev-router.md) for model/effort selection via a Responses proxy, or [jev-preflight](jev-preflight.md) for Claude Code turn-diff risk scoring.

## How it works

[`jev_agent/jev_client.py`](https://github.com/wellkilo/codex-jev-preflight/blob/633ddefe6596aa5d7c6b00767c08d07edea61096/jev_agent/jev_client.py) posts typed questions to TypeSafe System One. [`jev_user_prompt_hook.py`](https://github.com/wellkilo/codex-jev-preflight/blob/633ddefe6596aa5d7c6b00767c08d07edea61096/jev_user_prompt_hook.py) injects a short assessment block into the prompt context, validates enums (unknown → `unknown`), and **fails open** on timeouts, quota exhaustion (persistent breaker), or invalid responses so Codex continues.

## Get started

```sh
git clone https://github.com/wellkilo/codex-jev-preflight.git
cd codex-jev-preflight
git checkout 633ddefe6596aa5d7c6b00767c08d07edea61096
python3 -m pytest -q
python3 configure_jev.py
python3 install_jev_global_hook.py
```

Live hooks send task text to TypeSafe and can incur charges. This listing did not install into a real Codex home or call live APIs.

## Examples and demos

- Offline on the review host: `python3 -m pytest -q` → **27 passed**.
- Docs/demo site: https://wellkilo.github.io/codex-jev-preflight/

## Limits and data handling

Assessment is advisory only and cannot override system/developer instructions or an explicit user request. API keys are written to a private `0600` env file under `$CODEX_HOME`. Not a permission gate.

## Review and maintenance

Reviewed on **2026-09-22** at [commit 633ddef](https://github.com/wellkilo/codex-jev-preflight/tree/633ddefe6596aa5d7c6b00767c08d07edea61096): MIT. AI-assisted source review of README, LICENSE, hook, and `jev_client`. Offline pytest **27 passed**. No live TypeSafe spend.

Related: [codex-jev-router](codex-jev-router.md), [jev-preflight](jev-preflight.md), [mayi](mayi.md).
