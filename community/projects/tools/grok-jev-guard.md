# grok-jev-guard

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Typed preflight/approval layer for Grok Bot: local policy owns hard boundaries; TypeSafe Jev judges ambiguity; the agent executes only inside the returned envelope (shadow-first).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/0xwhrari/grok-jev-guard) |
| Maintainer | [0xwhrari](https://github.com/0xwhrari). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Python package **grok-jev-guard 0.1.0** (CLI + skill template; `typesafe-sdk`). |
| Requirements | Python **≥ 3.11**; `typesafe-sdk`; TypeSafe API key for live judgments. YAML config (`config.example.yaml`). |
| License | [MIT](https://github.com/0xwhrari/grok-jev-guard/blob/6083fb0584ffc61857fac755447e93d121925b48/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Source inspected (README, LICENSE, `src/grok_jev_guard/jev.py`, policy/tests). Live Grok Bot/Jev runs were **not** executed on the review host. Distinct from [Grok Bot Jev](grok-bot-jev.md). |

## When to use

Use it when Grok Bot tool sequences need an inspectable proceed / scope_down / checkpoint / ask_human / block decision before consequential work. Prefer [Grok Bot Jev](grok-bot-jev.md) for the reference reuse/stop/cap router skill; prefer [opencode-jev-guard](opencode-jev-guard.md) for OpenCode shell gates.

## How it works

Local policy hard-stops secrets/deletion/payments/etc.; [`jev.py`](https://github.com/0xwhrari/grok-jev-guard/blob/6083fb0584ffc61857fac755447e93d121925b48/src/grok_jev_guard/jev.py) sends a scrubbed task state to TypeSafe with Choice/Noul/Score questions (intent, needs_approval, destructive, scope_fits, risk). The returned action is an envelope for the bot—not a model router.

## Get started

```sh
git clone https://github.com/0xwhrari/grok-jev-guard.git
cd grok-jev-guard
git checkout 6083fb0584ffc61857fac755447e93d121925b48
pip install -e .
# configure from config.example.yaml; set TypeSafe key
grok-jev-guard --help
```

Pin for review: [commit 6083fb0](https://github.com/0xwhrari/grok-jev-guard/tree/6083fb0584ffc61857fac755447e93d121925b48). Live judgments send scrubbed state to TypeSafe and may incur charges.

## Examples and demos

- `examples/safe-research.json`, `examples/publish-release.json`.
- Offline tests under `tests/` (policy/redaction/audit; not re-run here).
- Skill template under `skill/grok-jev-guard/`.

## Limits and data handling

Shadow-first by design for adoption. Redaction is best-effort. This listing did not drive a live Grok Bot session.

## Review and maintenance

Reviewed on **2026-09-23** at [commit 6083fb0](https://github.com/0xwhrari/grok-jev-guard/tree/6083fb0584ffc61857fac755447e93d121925b48) (**0.1.0**, MIT). AI-assisted source review. No live TypeSafe spend.

Related: [Grok Bot Jev](grok-bot-jev.md), [opencode-jev-guard](opencode-jev-guard.md), [agent-chaperone](agent-chaperone.md).
