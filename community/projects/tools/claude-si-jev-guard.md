# jev-guard for Claude Code (PostToolUse hook where Jev scans web, MCP and network results for prompt injection before Claude reads them)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Claude Code plugin in the `claude-si` marketplace: after WebFetch, WebSearch, any `mcp__*` tool, or a Bash network command against a non-loopback host, the hook sends the result in chunks to Jev and replaces flagged output with a withheld notice. Clean verdicts below 0.6 confidence are also withheld, and without a key results are delivered but marked unvetted.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/u007/claude-si) |
| Maintainer | [u007](https://github.com/u007). Independently curated. |
| Format | Claude Code plugin (Python hook) in a personal plugin marketplace (no license file) |
| Requirements | Claude Code and a TypeSafe key in `TYPESAFE_API_KEY`, exported in the shell that launches Claude Code. |
| License | No license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`jev-guard/scripts/content_guard.py`](https://github.com/u007/claude-si/blob/b0604ffb21ef58d49568ce3353fa65c0f98e3814/jev-guard/scripts/content_guard.py) at the pinned commit. |

## When to use

- Put a prompt-injection check between untrusted web or MCP content and a Claude Code session.
- Mismatch: a complete security boundary; the author notes it is not yet verified end to end on a clean machine.

## How it works

`jev-guard/scripts/content_guard.py` posts to `https://api.typesafe.ai/v1/systemone` with `jev-latest`, scanning up to 32 chunks of 6,000 characters; it is a port of the author's ocode content guard. Local Bash and Read output is never scanned. Integration evidence: [`jev-guard/scripts/content_guard.py`](https://github.com/u007/claude-si/blob/b0604ffb21ef58d49568ce3353fa65c0f98e3814/jev-guard/scripts/content_guard.py).

## Get started

Add the marketplace, install the plugin and export your key.

```sh
claude plugin marketplace add https://github.com/u007/claude-plugins
claude plugin install jev-guard@claude-si
export TYPESAFE_API_KEY=...
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Plugin README: [github.com/u007/claude-si/blob/b0604ffb21ef58d49568ce3353fa65c0f98e3814/jev-guard/README.md](https://github.com/u007/claude-si/blob/b0604ffb21ef58d49568ce3353fa65c0f98e3814/jev-guard/README.md)
- Marketplace README: [github.com/u007/claude-si/blob/b0604ffb21ef58d49568ce3353fa65c0f98e3814/README.md](https://github.com/u007/claude-si/blob/b0604ffb21ef58d49568ce3353fa65c0f98e3814/README.md)

## Limits and data handling

Fetched web, search, MCP and network-command results go to TypeSafe on your key. Very large results are truncated to the scanned prefix.

## Review and maintenance

Reviewed **2026-11-14** (Europe/Sofia) at [commit b0604ffb21ef](https://github.com/u007/claude-si/tree/b0604ffb21ef58d49568ce3353fa65c0f98e3814). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
