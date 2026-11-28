# Jev Guard by sport-viz (PreToolUse guard for Claude Code, Antigravity and Pi that screens risky tool calls with Jev)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Tool-call guard for Claude Code, Antigravity (`agy`) and the Pi coding agent. Code rules deny catastrophes and protect the guard itself, known harmless calls skip Jev, and everything else gets one Jev call with yes/no hazard questions (data loss, external effects, secrets, security weakening, obfuscation, unrequested actions) plus a severity score. Tunable thresholds turn the probabilities into deny, ask or no opinion; every decision is logged with raw probabilities, and a shadow mode shows what it would do first.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/sport-viz/jev-guard) |
| Maintainer | [sport-viz](https://github.com/sport-viz) (commits by Deryck Henson). Independently curated. |
| Format | Python hook (uv) + Pi extension |
| Requirements | Python 3.10+, uv, Claude Code 2.1.295+ (or Antigravity / Pi) and a TypeSafe API key. |
| License | No licence file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`jev_guard/jev.py`](https://github.com/sport-viz/jev-guard/blob/f8899f4b612440418f34280bf15b13b67f79dc72/jev_guard/jev.py) at the pinned commit. |

## When to use

- Developers running coding agents in auto mode who want an extra, probability-based check before risky commands.
- Mismatch: a sandbox replacement; the guard only adds barriers and leaves your normal permission rules in place.

## How it works

`jev_guard/jev.py` wraps the official `typesafe-sdk` and calls `system_one` with the pinned `jev-1.13.0` model; the state is the truncated tool input, recent user prompts and facts code knows (path existence, git tracking). If Jev is unreachable the guard falls back to asking. A labelled eval set with cached Jev answers lets you re-tune thresholds offline. Integration evidence: [`jev_guard/jev.py`](https://github.com/sport-viz/jev-guard/blob/f8899f4b612440418f34280bf15b13b67f79dc72/jev_guard/jev.py).

## Get started

Install the hook, preview the settings change, then start in shadow mode.

```sh
git clone https://github.com/sport-viz/jev-guard && cd jev-guard
uv sync && scripts/install.sh
.venv/bin/python scripts/configure_settings.py --dry-run
export TYPESAFE_API_KEY=... JEV_GUARD_MODE=shadow
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Design notes: [github.com/sport-viz/jev-guard/blob/dev/PLAN.md](https://github.com/sport-viz/jev-guard/blob/dev/PLAN.md)
- Eval cases: [github.com/sport-viz/jev-guard/blob/dev/evals/cases.jsonl](https://github.com/sport-viz/jev-guard/blob/dev/evals/cases.jsonl)

## Limits and data handling

Truncated tool input and recent prompts go to TypeSafe on each screened call (the README estimates about $0.00003 per call). An optional summary step can call OpenAI or OpenRouter. No licence file, so no reuse rights are granted.

## Review and maintenance

Reviewed **2026-11-28** (Europe/Sofia) at [commit f8899f4b6124](https://github.com/sport-viz/jev-guard/tree/f8899f4b612440418f34280bf15b13b67f79dc72). Inspected the README, `jev_guard/jev.py`, `questions.py` and `pyproject.toml` at the pinned commit; no licence file present. Not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
