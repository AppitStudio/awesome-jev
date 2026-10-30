# jev-claude-gate (Claude Code hooks that ask Jev to vet session rules, tool calls, tool output and task completion)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Four Claude Code hooks backed by Jev: a SessionStart check of CLAUDE.md, AGENTS.md and rules files for planted instructions, a PreToolUse gate that scores each command or edit on several risk questions before it runs, a PostToolUse scan of fetched pages and files for indirect prompt injection, and a Stop check for agents that claim to be done while hiding errors. The gate sees the tool name, arguments and recent workspace state, not the agent's reasoning. README in Chinese.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/JingYao152/jev-claude-gate) |
| Maintainer | [JingYao152](https://github.com/JingYao152). Independently curated. |
| Format | Python hook scripts and a JSON config |
| Requirements | Claude Code, Python 3, and a Jev endpoint (TypeSafe directly, OpenRouter-style ID, or a local gateway). |
| License | [MIT](https://github.com/JingYao152/jev-claude-gate/blob/ea3494c73d0a8139606c17b78d53adb7a8642e25/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`hooks/jev_common.py`](https://github.com/JingYao152/jev-claude-gate/blob/ea3494c73d0a8139606c17b78d53adb7a8642e25/hooks/jev_common.py) at the pinned commit. |

## When to use

- Add a fast second opinion before Claude Code runs shell commands or edits files.
- Mismatch: thresholds and hook behaviour are the author's defaults; review them before relying on the gate.

## How it works

`hooks/jev_common.py` builds one `/v1/systemone` request per check with `typesafe/jev-latest` and the configured endpoint; `hooks/jev-gate.py` turns the answers into allow, ask or deny. Integration evidence: [`hooks/jev_common.py`](https://github.com/JingYao152/jev-claude-gate/blob/ea3494c73d0a8139606c17b78d53adb7a8642e25/hooks/jev_common.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/JingYao152/jev-claude-gate.git && cd jev-claude-gate
mkdir -p ~/.claude/hooks
cp hooks/*.py ~/.claude/hooks/
cp config/jev-gate.example.json ~/.claude/hooks/jev-gate.json
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README with the hook design: [github.com/JingYao152/jev-claude-gate#readme](https://github.com/JingYao152/jev-claude-gate#readme)

## Limits and data handling

Tool names, arguments, file snippets and fetched content are sent to the configured Jev endpoint. The example config points at a local gateway on 127.0.0.1:3425; change it to TypeSafe or your own proxy.

## Review and maintenance

Reviewed **2026-10-30** (Europe/Sofia) at [commit ea3494c73d0a](https://github.com/JingYao152/jev-claude-gate/tree/ea3494c73d0a8139606c17b78d53adb7a8642e25). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
