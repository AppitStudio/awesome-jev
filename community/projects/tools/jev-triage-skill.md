# jev-triage skill (Claude Code skill that sorts and scores large data with Jev instead of reading it)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Agent skill for Claude Code and other SKILL.md agents: instead of reading hundreds of log lines, tickets or files into context, the agent runs a standard-library script that asks Jev typed questions about each item and reads back only compact answers, with filters such as `category==bug` and `urgency>=2`.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/wordsbyvaclav-boop/jev-triage) |
| Maintainer | [wordsbyvaclav-boop](https://github.com/wordsbyvaclav-boop). Independently curated. |
| Format | Agent skill with a Python script (standard library only) |
| Requirements | Python 3.8+; a TypeSafe API key in `TYPESAFE_API_KEY` or a private env file. |
| License | [MIT](https://github.com/wordsbyvaclav-boop/jev-triage/blob/2a360acc6965ce5bf225b8776b9cf025f3a3a878/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`scripts/jev_ask.py`](https://github.com/wordsbyvaclav-boop/jev-triage/blob/2a360acc6965ce5bf225b8776b9cf025f3a3a878/scripts/jev_ask.py) at the pinned commit. |

## When to use

- Let a coding agent pick the 10 items that matter out of 300 without filling its context window.
- Reuse the example question files for issue triage and log filtering.
- Mismatch: every item is sent to TypeSafe; keep secrets out of the input.

## How it works

`scripts/jev_ask.py` posts each item as state with Choice, Noul and Score questions to `https://api.typesafe.ai/v1/systemone` (default `jev-latest`), retries transient errors and prints compact JSON lines plus token totals. Integration evidence: [`scripts/jev_ask.py`](https://github.com/wordsbyvaclav-boop/jev-triage/blob/2a360acc6965ce5bf225b8776b9cf025f3a3a878/scripts/jev_ask.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/wordsbyvaclav-boop/jev-triage ~/.claude/skills/jev-triage
export TYPESAFE_API_KEY=...
python ~/.claude/skills/jev-triage/scripts/jev_ask.py --items-file tickets.jsonl --questions-file examples/issue-triage.json --compact
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/wordsbyvaclav-boop/jev-triage#readme](https://github.com/wordsbyvaclav-boop/jev-triage#readme)

## Limits and data handling

The items you pass go to TypeSafe. The key is read from the environment or a file outside the repository and is not printed.

## Review and maintenance

Reviewed **2026-10-26** (Europe/Sofia) at [commit 2a360acc6965](https://github.com/wordsbyvaclav-boop/jev-triage/tree/2a360acc6965ce5bf225b8776b9cf025f3a3a878). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
