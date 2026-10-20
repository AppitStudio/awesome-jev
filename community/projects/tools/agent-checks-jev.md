# Agent checks (routing, brief lint, plan and review gates)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Claude Code hooks and scripts that put Jev judgements around AI coding agents: route each turn on purpose, lint briefs before dispatch, block inline edits to files assigned to a worker, check cited sources in research reports, and ask whether returned work shows a check actually ran.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/jacob-mcclelland/agent-checks) |
| Maintainer | [jacob-mcclelland](https://github.com/jacob-mcclelland). Independently curated. |
| Format | Claude Code hooks and Python scripts (standard library only) |
| Requirements | Python 3.10+ and Git; Claude Code (the author dispatches workers with Codex CLI); a TypeSafe key for live checks. |
| License | [MIT](https://github.com/jacob-mcclelland/agent-checks/blob/d4e2735cd3c0343f721f22044270367d47bab562/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`jev/client.py`](https://github.com/jacob-mcclelland/agent-checks/blob/d4e2735cd3c0343f721f22044270367d47bab562/jev/client.py) at the pinned commit. |

## When to use

- Keep an orchestrating agent from claiming success it has not shown evidence for.
- Make delegation a decision with a logged override instead of a habit.
- Mismatch: guidance for a cooperating agent on one machine, not a security boundary; most checks fail open.

## How it works

Each hook builds narrow yes/no, choice or score questions (for example whether a brief identifies precisely what it is about, or whether the record shows a check ran and passed) and `jev/client.py` sends them to `https://api.typesafe.ai/v1/systemone` with a pinned model version. Code applies thresholds and role policy; the README treats the scores as ranks, not calibrated odds, and labels which thresholds are measured and which are guesses. Integration evidence: [`jev/client.py`](https://github.com/jacob-mcclelland/agent-checks/blob/d4e2735cd3c0343f721f22044270367d47bab562/jev/client.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/jacob-mcclelland/agent-checks.git && cd agent-checks
python tests/run_all.py            # offline tests, no key
cp routes.example.json routes.json  # map roles to models
export TYPESAFE_API_KEY=...
# merge examples/claude-settings.example.json hooks into your Claude Code settings
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- examples/claude-settings.example.json
- DESIGN-LOG.md (failures found while building the checks)

## Limits and data handling

Prompts, briefs, returned work records and fetched source pages are sent to TypeSafe for judgement. Used by one person on Windows, per the README.

## Review and maintenance

Reviewed **2026-10-20** (Europe/Sofia) at [commit d4e2735cd3c0](https://github.com/jacob-mcclelland/agent-checks/tree/d4e2735cd3c0343f721f22044270367d47bab562). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
