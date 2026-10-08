# barmkin-mod

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Claude Code mods security layer: secret redaction on every tool call, untrusted-content taint tracking with an injection screen and a Rule-of-Two egress gate, MCP server allowlists and post-write semgrep — with a Jev System One client that asks two noul questions per screened result (does it try to instruct the agent? does it contain credentials?) against an OpenRouter- or TypeSafe-style endpoint you configure, falling back to heuristics with a circuit breaker.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/samfrmr/barmkin-mod) |
| Maintainer | [samfrmr](https://github.com/samfrmr). Independently curated. |
| Format | Claude Code plugin (mods; Claude Code ≥ 2.1.287) |
| Requirements | Claude Code ≥ 2.1.287; optional `jev_base_url` + `jev_model` (pinned `jev-1.13`) and key; optional semgrep. |
| License | The reviewed tree has **no LICENSE file** — listed as Source available; reuse terms are not granted until the maintainer adds a license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Screen WebFetch/MCP/out-of-tree reads for prompt injection before the agent acts.
- Block egress after untrusted content has entered the session.
- Mismatch: no live Jev endpoint is required, but the screen is heuristic without one.

## How it works

`hooks/lib/system-one-client.ts` validates `POST {base_url}/v1/systemone` requests and responses; `hooks/lib/taint.ts` only ever tightens. After three consecutive classifier failures a 60-second breaker falls back to pattern screening. Manifest: [`.claude-plugin/plugin.json`](https://github.com/samfrmr/barmkin-mod/blob/61a97b3480df282241db01b45d4e97a8fe82c969/.claude-plugin/plugin.json).

## Get started

Validate and test the plugin from a checkout (README):

```sh
git clone https://github.com/samfrmr/barmkin-mod.git && cd barmkin-mod
claude plugin validate --strict .
claude plugin test
# set jev_base_url / jev_model in the plugin's user config
```

Two Jev questions per screened tool result when an endpoint is configured.

## Examples and demos

- README *Capabilities* table (10 capabilities).

## Limits and data handling

Screened content goes to your configured Jev endpoint. Independent of the barmkin project's gateway. No LICENSE file. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-08** (Europe/Sofia) at [commit 61a97b3480df](https://github.com/samfrmr/barmkin-mod/tree/61a97b3480df282241db01b45d4e97a8fe82c969). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
