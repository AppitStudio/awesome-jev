# jev-guard by Ashish Dhillon (Claude Code PreToolUse hook where Jev decides whether a Bash command needs your confirmation)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Claude Code `PreToolUse` hook for Bash: local rules deny obvious disasters and skip obviously read-only commands, and everything else goes to Jev with two questions (is it read-only, reversible or destructive, and does it touch credentials). Destructive, low-confidence or likely-secret commands get a confirmation prompt; the hook never auto-approves.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ashishdhillon/jev-guard) |
| Maintainer | [Ashish Dhillon](https://github.com/ashishdhillon). Independently curated. |
| Format | Python package and CLI (stdlib only) |
| Requirements | Python 3.9+, Claude Code, and a TypeSafe API key in `TYPESAFE_API_KEY` (not needed for `--offline`). |
| License | [MIT](https://github.com/ashishdhillon/jev-guard/blob/d44111c8a35f2a5ad02f92606d9a9e15ecae83d2/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jev_guard/client.py`](https://github.com/ashishdhillon/jev-guard/blob/d44111c8a35f2a5ad02f92606d9a9e15ecae83d2/src/jev_guard/client.py) at the pinned commit. |

## When to use

- Claude Code users who want a second opinion before risky shell commands without writing a long allowlist.
- Mismatch: a security boundary; it only adds prompts or denies, and normal Claude Code permissions still decide the rest.

## How it works

`src/jev_guard/client.py` posts the command to `https://api.typesafe.ai/v1/systemone` (default `jev-latest`, overridable with `JEV_GUARD_MODEL`) with a `choice` risk question and a `noul` secrets question; `hook.py` turns them into Claude Code's ask/deny output at `JEV_GUARD_THRESHOLD` (0.8). If Jev is unreachable it falls back to normal permissions, or to ask with `JEV_GUARD_FAIL=ask`. Integration evidence: [`src/jev_guard/client.py`](https://github.com/ashishdhillon/jev-guard/blob/d44111c8a35f2a5ad02f92606d9a9e15ecae83d2/src/jev_guard/client.py).

## Get started

Install from GitHub, set the key, print the settings snippet and add it to `~/.claude/settings.json`; try commands with `check` first.

```sh
pip install git+https://github.com/ashishdhillon/jev-guard
export TYPESAFE_API_KEY=...
jev-guard install                     # prints the settings.json snippet
jev-guard check "git reset --hard HEAD~5"
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Settings example: [github.com/ashishdhillon/jev-guard/tree/d44111c8a35f2a5ad02f92606d9a9e15ecae83d2/examples](https://github.com/ashishdhillon/jev-guard/tree/d44111c8a35f2a5ad02f92606d9a9e15ecae83d2/examples)

## Limits and data handling

Commands that reach Jev are sent to TypeSafe; commands handled by local rules are not, and `--offline` keeps everything local. Only Bash tool calls are checked. The author says thresholds should be calibrated on your own commands and that Jev's accuracy figures are vendor-reported. Not published on PyPI; install from GitHub.

## Review and maintenance

Reviewed **2026-11-26** (Europe/Sofia) at [commit d44111c8a35f](https://github.com/ashishdhillon/jev-guard/tree/d44111c8a35f2a5ad02f92606d9a9e15ecae83d2). Inspected the README, LICENSE, `src/jev_guard/client.py` and `hook.py` at the pinned commit; the hook was not installed or run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
