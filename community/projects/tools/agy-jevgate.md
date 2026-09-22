# agy-jevgate

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Fail-closed Antigravity (`agy`) `PreToolUse` hook for `run_command`: exact read-only fast-pass, a short static destructive guard, then TypeSafe Jev risk scoring—errors and missing keys deny.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/catpotd/agy-jevgate) |
| Maintainer | [catpotd](https://github.com/catpotd). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Antigravity / Gemini plugin (`hooks.json`, `plugin.json`) with stdlib Python hook scripts and unittest suite. |
| Requirements | Python 3.9+; Antigravity CLI with `PreToolUse` hooks; POSIX `fcntl` locking. TypeSafe key via macOS Keychain setup or `apiKeyCommand` in config. Windows not supported by the locking path. |
| License | [MIT](https://github.com/catpotd/agy-jevgate/blob/0200c35c8162f24f898acebb1a478d21703dbe34/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not endorsement. Offline unittest inspected; live TypeSafe and Antigravity sessions not run on the review host. |

## When to use

Use it when Antigravity shell tool calls should be **denied by default** unless they are exact read-only fast-passes or Jev scores them below a configured risk threshold. Prefer [claude-code-jev](claude-code-jev.md) or [stop-rules](stop-rules.md) for Claude Code / multi-agent stop hooks, or [agent-chaperone](agent-chaperone.md) for a broader MCP tool firewall. This is not a sandbox and does not cover tools other than the configured `run_command` hook.

## How it works

[`scripts/jev_gate.py`](https://github.com/catpotd/agy-jevgate/blob/0200c35c8162f24f898acebb1a478d21703dbe34/scripts/jev_gate.py) posts risk questions to `https://api.typesafe.ai/v1/systemone`. Exact prior denials (command + `conversationId`) are sticky; static patterns catch common destructive forms; remaining commands need a successful low-risk Jev answer. Missing credentials, bad input, Jev errors, and unreadable denial state all produce `deny`.

## Get started

```sh
git clone https://github.com/catpotd/agy-jevgate.git
cd agy-jevgate
git checkout 0200c35c8162f24f898acebb1a478d21703dbe34
python3 -m unittest discover -s tests -v
# Install per upstream README into ~/.gemini/config/plugins or .agents/plugins
# Then configure Keychain (macOS) or apiKeyCommand; live hooks need Antigravity + TypeSafe
```

Live hooks send command strings to TypeSafe and may incur charges. This listing did not call live APIs or run Antigravity.

## Examples and demos

- Offline on the review host: `python3 -m unittest discover -s tests -v` → **11 passed**.
- Upstream documents `agy plugin validate .` when the Antigravity CLI is installed; that command was not available on the review host.

## Limits and data handling

Not a complete authorization system: a changed command or new `conversationId` is re-evaluated. The static guard is intentionally short. Denied commands are recorded under `~/.config/agy-jevgate/denied_commands.json` and do not expire. There is no chat-based override path.

## Review and maintenance

Reviewed on **2026-09-22** at [commit 0200c35](https://github.com/catpotd/agy-jevgate/tree/0200c35c8162f24f898acebb1a478d21703dbe34): MIT. AI-assisted source review of README, LICENSE, `scripts/jev_gate.py`, hooks manifest. Offline unittest **11 passed**. No live TypeSafe or Antigravity run on the review host.

Related: [claude-code-jev](claude-code-jev.md), [agent-chaperone](agent-chaperone.md), [stop-rules](stop-rules.md), [pi-typesafe-bash-guard](pi-typesafe-bash-guard.md).
