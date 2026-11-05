# Agent AFK (local coding agent you can walk away from, with optional Jev as the what-if verification judge)

[All projects](../README.md) · [Command-line apps](README.md#command-line-apps)

Local coding-agent harness (`afk`) that builds a feature, verifies its own work and texts you when done. Optional Jev integration: configure Jev as an MCP judge so `afk whatif --judge auto` grades verification episodes with calibrated probabilities instead of the same-family model.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/griffinwork40/agent-afk) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Product homepage](https://agentafk.com) |
| Pricing and access | Free source build / npm package; bring your own model and optional TypeSafe keys. Checked 2026-11-06. |
| Jev evidence | [`src/whatif/judge/jev.ts`](https://github.com/griffinwork40/agent-afk/blob/84f7c6293265ce6f2973eab65d09264bee84b2b2/src/whatif/judge/jev.ts) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [griffinwork40](https://github.com/griffinwork40). Independently curated. |
| Format | Node.js CLI (`agent-afk` on npm, Apache-2.0) |
| Platform and availability | CLI on macOS/Linux/Windows (Node). Product site agentafk.com. |
| Jev's role | Optional external judge for what-if verification episodes (`--judge auto` prefers Jev when configured; falls back to Claude). |
| Requirements | Node.js 22.22+/24.15+/26+ (23.x and 25.x excluded), provider credentials via `afk login`, and optional Jev MCP config in `~/.afk/config/mcp.json` for the what-if judge. |
| License | [Apache-2.0](https://github.com/griffinwork40/agent-afk/blob/84f7c6293265ce6f2973eab65d09264bee84b2b2/LICENSE) |

## When to use

- Run a coding agent unattended with receipts of every step.
- Grade verification episodes with a cross-family Jev judge.
- Mismatch: Jev is optional and only used in the what-if judge path when MCP-configured.

## How it works

`src/whatif/judge/jev.ts` and `jev-connect.ts` talk to a Jev MCP server; tests pin verbatim Jev 1.13.0 responses. Without Jev configured, what-if falls back to Claude. Integration evidence: [`src/whatif/judge/jev.ts`](https://github.com/griffinwork40/agent-afk/blob/84f7c6293265ce6f2973eab65d09264bee84b2b2/src/whatif/judge/jev.ts).

## Get started

From the upstream README (not run on the review host):

```sh
npm install -g agent-afk
afk login && afk doctor
# optional: configure Jev MCP in ~/.afk/config/mcp.json then:
afk whatif --judge auto --append "Always ask before using tools." --verify
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/griffinwork40/agent-afk/blob/84f7c6293265ce6f2973eab65d09264bee84b2b2/README.md](https://github.com/griffinwork40/agent-afk/blob/84f7c6293265ce6f2973eab65d09264bee84b2b2/README.md)
- Jev judge: [github.com/griffinwork40/agent-afk/blob/84f7c6293265ce6f2973eab65d09264bee84b2b2/src/whatif/judge/jev.ts](https://github.com/griffinwork40/agent-afk/blob/84f7c6293265ce6f2973eab65d09264bee84b2b2/src/whatif/judge/jev.ts)

## Limits and data handling

When Jev is configured, verification episode data is sent to TypeSafe on your key. Default agent work uses your chosen coding-model provider.

## Review and maintenance

Reviewed **2026-11-06** (Europe/Sofia) at [commit 84f7c6293265](https://github.com/griffinwork40/agent-afk/tree/84f7c6293265ce6f2973eab65d09264bee84b2b2). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
