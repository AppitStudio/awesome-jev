# jev-hooks by austpryb (nine Claude Code hooks backed by Jev)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Claude Code plugin with nine Jev-backed hooks: a Bash and an edit risk gate, compaction triage that keeps decisions, subagent report verification, loop detection, a stop self-check, subagent model routing, prompt routing and output narrowing. It fails open.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/austpryb/jev-hooks) |
| Maintainer | [austpryb](https://github.com/austpryb). Independently curated. |
| Format | Claude Code plugin (Python hooks) |
| Requirements | Claude Code; Python 3; a TypeSafe API key. |
| License | [MIT](https://github.com/austpryb/jev-hooks/blob/af2afd24776e654557b15a0aaacc485d52818dea/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`lib/jev.py`](https://github.com/austpryb/jev-hooks/blob/af2afd24776e654557b15a0aaacc485d52818dea/lib/jev.py) at the pinned commit. |

## When to use

- Gate risky shell commands and overwrites without a prompt for every read-only command.
- Check that a subagent's report matches what its tools actually did.
- Mismatch: Claude Code only; each hook adds a short Jev call.

## How it works

`lib/jev.py` posts typed yes/no, choice and score questions to `https://api.typesafe.ai/v1/systemone` (`jev-latest` by default, overridable with `JEV_HOOKS_MODEL`). Read-only commands and clean git states are settled in code without a call. Integration evidence: [`lib/jev.py`](https://github.com/austpryb/jev-hooks/blob/af2afd24776e654557b15a0aaacc485d52818dea/lib/jev.py).

## Get started

From the upstream README (not run on the review host):

```sh
export TYPESAFE_API_KEY=...
claude --plugin-dir /path/to/jev-hooks
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Hook table and live runs in the README: [github.com/austpryb/jev-hooks#readme](https://github.com/austpryb/jev-hooks#readme)

## Limits and data handling

Commands, prompts and parts of the transcript are sent to TypeSafe for the hooks you enable. `JEV_HOOKS_GATE_MODE=warn` makes the gates ask instead of deny.

## Review and maintenance

Reviewed **2026-10-24** (Europe/Sofia) at [commit af2afd24776e](https://github.com/austpryb/jev-hooks/tree/af2afd24776e654557b15a0aaacc485d52818dea). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
