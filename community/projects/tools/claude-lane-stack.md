# claude-lane-stack (one-person multi-agent coding factory with TypeSafe Jev routing and compaction)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Claude Code PM plus Codex/Qwen/Grok/Kimi lanes; TypeSafe Jev routes lane-spawned subagents to a model/effort and runs `/compact`, winnow and test filtering.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/VKirill/claude-lane-stack) |
| Maintainer | [VKirill](https://github.com/VKirill). Independently curated. |
| Format | Python/shell tooling for Claude Code (MIT) |
| Requirements | Claude Code, the lane CLIs you use, and a TypeSafe API key. |
| License | [MIT](https://github.com/VKirill/claude-lane-stack/blob/6acbe4a3030750e5d10bfe71233653dc1c99a333/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`bin/jev_decisions.py`](https://github.com/VKirill/claude-lane-stack/blob/6acbe4a3030750e5d10bfe71233653dc1c99a333/bin/jev_decisions.py) at the pinned commit. |

## When to use

- Route subagents to cheaper or stronger models per task.
- Compact long sessions with Jev decisions.
- Mismatch: opinionated one-person setup.

## How it works

`bin/jev_provider.py` wraps the System One API; `bin/jev_decisions.py` asks Jev which model a spawned subagent gets, and `jev_test_filter.py` trims test output. Only lane sessions call Jev. Integration evidence: [`bin/jev_decisions.py`](https://github.com/VKirill/claude-lane-stack/blob/6acbe4a3030750e5d10bfe71233653dc1c99a333/bin/jev_decisions.py).

## Get started

Install per README (hooks merge into Claude Code settings), then set `TYPESAFE_API_KEY`.

```sh
git clone https://github.com/VKirill/claude-lane-stack.git && cd claude-lane-stack
export TYPESAFE_API_KEY=...
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/VKirill/claude-lane-stack/blob/6acbe4a3030750e5d10bfe71233653dc1c99a333/README.md](https://github.com/VKirill/claude-lane-stack/blob/6acbe4a3030750e5d10bfe71233653dc1c99a333/README.md)

## Limits and data handling

Session snippets for routing/compaction go to TypeSafe on your key.

## Review and maintenance

Reviewed **2026-11-09** (Europe/Sofia) at [commit 6acbe4a30307](https://github.com/VKirill/claude-lane-stack/tree/6acbe4a3030750e5d10bfe71233653dc1c99a333). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
