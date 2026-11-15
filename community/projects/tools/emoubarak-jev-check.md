# jev-check by emoubarak (agent skill that sends a Jev-driven browser agent through your staging app as a real account state and lets the database decide pass or fail)

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

Open-source agent skill for Claude Code, Codex, OpenClaw and other agents that read `SKILL.md`. It signs a throw-away account into your staging app in exactly the state you need (free, paid, lapsed, team member, stranger, anonymous), has the jev-ultrafast browser agent (Browser Use) follow a plain-English goal, and then reads your database to decide whether it really worked; the agent's "done" is only a claim. `jevcheck ask` answers one-off questions; `jevcheck audit` runs standing checks for plan gates, paywalls, roles and cross-account isolation.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/emoubarak/jev-check) |
| Maintainer | [emoubarak](https://github.com/emoubarak). Independently curated. |
| Format | Python CLI and agent skill (uv, MIT) |
| Requirements | Python 3.12+ with uv, Chrome, a staging app with test accounts and database access, `TYPESAFE_API_KEY`; an OpenAI-compatible key only for goals that need typing. |
| License | [MIT](https://github.com/emoubarak/jev-check/blob/c19da3cbf10ab2e12105b403947896d0decf5bf6/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`jevcheck/agent.py`](https://github.com/emoubarak/jev-check/blob/c19da3cbf10ab2e12105b403947896d0decf5bf6/jevcheck/agent.py) at the pinned commit. |

## When to use

- End-to-end checks of paywalls, roles and multi-tenant isolation on staging, verified against the database.
- Mismatch: production (refused by design) or CI gates; it needs a real browser and costs model calls.

## How it works

`jevcheck/agent.py` drives `jev_ultrafast.Agent` (pinned by commit in `pyproject.toml`) from a start URL toward the goal, where Jev makes the browser decisions; `jevcheck/cli.py` refuses to run without `TYPESAFE_API_KEY` and `.env.example` defaults to `jev-latest`. Integration evidence: [`jevcheck/agent.py`](https://github.com/emoubarak/jev-check/blob/c19da3cbf10ab2e12105b403947896d0decf5bf6/jevcheck/agent.py).

## Get started

Try the bundled demo app first, then install it as a skill and ask your agent to set it up for your app.

```sh
git clone https://github.com/emoubarak/jev-check ~/.claude/skills/jev-check
export TYPESAFE_API_KEY=...
uv run --project ~/.claude/skills/jev-check jevcheck init     # jevcheck.toml + hooks + checks
uv run --project ~/.claude/skills/jev-check jevcheck audit
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README (with demo GIF): [github.com/emoubarak/jev-check/blob/c19da3cbf10ab2e12105b403947896d0decf5bf6/README.md](https://github.com/emoubarak/jev-check/blob/c19da3cbf10ab2e12105b403947896d0decf5bf6/README.md)
- Skill instructions: [github.com/emoubarak/jev-check/blob/c19da3cbf10ab2e12105b403947896d0decf5bf6/SKILL.md](https://github.com/emoubarak/jev-check/blob/c19da3cbf10ab2e12105b403947896d0decf5bf6/SKILL.md)

## Limits and data handling

Page content seen by the agent goes to TypeSafe on your key; test accounts and database reads stay in your staging setup. Built on Browser Use's jev-ultrafast and browser-harness (MIT).

## Review and maintenance

Reviewed **2026-11-16** (Europe/Sofia) at [commit c19da3cbf10a](https://github.com/emoubarak/jev-check/tree/c19da3cbf10ab2e12105b403947896d0decf5bf6). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
