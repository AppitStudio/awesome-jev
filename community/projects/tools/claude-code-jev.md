# claude-code-jev

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Experimental Claude Code **PreToolUse** permission gate that classifies each tool call as `allow` / `block` / `ask` with TypeSafe Jev via OpenRouter’s typed decisions API, plus reproducible latency/cost fixtures.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/RahulBalakavi/claude-code-jev) |
| Maintainer | [RahulBalakavi](https://github.com/RahulBalakavi). Independently curated; this page is not an upstream submission or endorsement. |
| Format | Python package `jev-auto-mode` **0.1.0** (PyPI-style layout under `src/`); CLI `jev-auto-mode`; hook module and `bin/claude-openrouter` launcher. |
| Requirements | Python ≥ 3.11; live gate needs `OPENROUTER_API_KEY` and Claude Code hook wiring. Default model `typesafe/jev-1.13`. |
| License | [MIT](https://github.com/RahulBalakavi/claude-code-jev/blob/629c3d852faf32fb0f88c724f029bb8e00efc109/LICENSE). OpenRouter/TypeSafe usage billed separately. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Offline `pytest`: **11 passed**. Live OpenRouter/Claude Code sessions not run. Upstream latency/cost tables were not re-measured. |

## When to use

Use it when you want Claude Code’s hot-path permission reflex on a System One classifier instead of a chat model, with logged decisions and a fixture benchmark. Prefer [toolgate](toolgate.md) / [jev-guard](jev-guard.md) for broader multi-harness firewalls, or [The Jev-enator](the-jev-enator.md) for danger/failure Stop hooks. Distinct focus: OpenRouter Decisions + Claude Code PreToolUse + published fixture methodology.

## How it works

[`providers.py`](https://github.com/RahulBalakavi/claude-code-jev/blob/629c3d852faf32fb0f88c724f029bb8e00efc109/src/jev_auto_mode/providers.py) `OpenRouterJevClassifier` posts to `https://openrouter.ai/api/alpha/decisions`. [`hook.py`](https://github.com/RahulBalakavi/claude-code-jev/blob/629c3d852faf32fb0f88c724f029bb8e00efc109/src/jev_auto_mode/hook.py) runs as a PreToolUse hook; [`policy.py`](https://github.com/RahulBalakavi/claude-code-jev/blob/629c3d852faf32fb0f88c724f029bb8e00efc109/src/jev_auto_mode/policy.py) escalates low-confidence answers. The CLI can replay fixtures for benchmarks without claiming Claude Code’s stock classifier was measured live.

## Get started

```sh
git clone https://github.com/RahulBalakavi/claude-code-jev.git
cd claude-code-jev
git checkout 629c3d852faf32fb0f88c724f029bb8e00efc109
uv sync
uv run pytest
# live (bills OpenRouter): configure OPENROUTER_API_KEY and Claude Code PreToolUse per upstream README
```

## Examples and demos

- `fixtures/actions.jsonl` and `results/` document the 18-case / multi-pass methodology.
- This listing: `uv run pytest` → **11 passed**. No live provider call.

## Limits and data handling

Live gates send tool-call context to OpenRouter (TypeSafe Jev). Policy is advisory relative to Claude Code’s own sandbox—confirm hook install carefully. Accuracy/cost claims are upstream measurements on fixtures; treat the ~4 s “LLM-judge” comparison as a published reference, not a controlled Claude Code A/B on this host.

## Review and maintenance

Reviewed on **2026-09-21** at [commit 629c3d8](https://github.com/RahulBalakavi/claude-code-jev/tree/629c3d852faf32fb0f88c724f029bb8e00efc109): **0.1.0**, MIT. AI-assisted source review of README, LICENSE, `providers.py`, `hook.py`, `policy.py`, and offline tests. No live OpenRouter or Claude Code run.

Related: [toolgate](toolgate.md), [jev-guard](jev-guard.md), [The Jev-enator](the-jev-enator.md), [clear-head](clear-head.md).
