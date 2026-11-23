# jev skill by Dan Kalivoda (agent skill that asks Jev how hard each subagent task is and picks the cheapest capable model)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Turns the main agent into an orchestrator: it splits a job into tasks, asks Jev to rate each one before handoff, and routes it to the cheapest model tier it trusts (Claude Haiku to Opus, or Codex models), optionally suggesting an installed skill. Failed attempts raise the tier, and settings can bias quality or cap cost per topic.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/danekkalivoda/jev-skill) |
| Maintainer | [danekkalivoda](https://github.com/danekkalivoda). Independently curated. |
| Format | Agent skill (`npx skills add`) with a Python router |
| Requirements | An agent that supports skills (Claude Code or Codex); `TYPESAFE_API_KEY`, or OpenRouter, or a local System One-compatible server. |
| License | No license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`skills/jev/route.py`](https://github.com/danekkalivoda/jev-skill/blob/81c58a2f7e7f7029edc14509dad27353c49b3560/skills/jev/route.py) at the pinned commit. |

## When to use

- Cut subagent spend by sending easy tasks to small models, with a Jev rating behind each choice.
- Mismatch: guaranteed quality; tier thresholds were calibrated by the author on Jev only.

## How it works

`skills/jev/route.py` posts to the provider in `skills/jev/models.json`: `https://api.typesafe.ai/v1/systemone` (`jev-1.13.0`) by default, OpenRouter (`typesafe/jev-1.13`), or a local server, with a fallback to TypeSafe if local fails. Integration evidence: [`skills/jev/route.py`](https://github.com/danekkalivoda/jev-skill/blob/81c58a2f7e7f7029edc14509dad27353c49b3560/skills/jev/route.py).

## Get started

Add the skill and set your key in your shell profile.

```sh
npx skills add danekkalivoda/jev-skill
export TYPESAFE_API_KEY=...
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Skill instructions: [github.com/danekkalivoda/jev-skill/blob/81c58a2f7e7f7029edc14509dad27353c49b3560/skills/jev/SKILL.md](https://github.com/danekkalivoda/jev-skill/blob/81c58a2f7e7f7029edc14509dad27353c49b3560/skills/jev/SKILL.md)

## Limits and data handling

Task briefs are sent to the configured provider. The local provider's tiers are uncalibrated. No license file: reuse terms are not granted.

## Review and maintenance

Reviewed **2026-11-23** (Europe/Sofia) at [commit 81c58a2f7e7f](https://github.com/danekkalivoda/jev-skill/tree/81c58a2f7e7f7029edc14509dad27353c49b3560). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
