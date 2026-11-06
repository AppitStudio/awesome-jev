# AskAway Model (local gateway that delegates Claude Code, Desktop and Codex decisions to Jev)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Local service, hooks and MCP that send coding-agent permission and choice questions to TypeSafe Jev (or reselling gateways) and log every query. Independent plugin; not affiliated with TypeSafe.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/KeepGlide/askaway-model) |
| Maintainer | [KeepGlide](https://github.com/KeepGlide). Independently curated. |
| Format | Node.js local gateway + hooks/MCP (Apache-2.0) |
| Requirements | Node.js, Claude Code / Claude Desktop / Codex (or OpenCode) hooks as documented, and a TypeSafe or gateway key. |
| License | [Apache-2.0](https://github.com/KeepGlide/askaway-model/blob/5d57c0dc23ab806fc55212bb61f2e17b39a0d194/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`gateway/src/jev.ts`](https://github.com/KeepGlide/askaway-model/blob/5d57c0dc23ab806fc55212bb61f2e17b39a0d194/gateway/src/jev.ts) at the pinned commit. |

## When to use

- Delegate coding-agent yes/no and choice prompts to Jev with a local audit log.
- Swap TypeSafe direct vs gateway providers without changing agents.
- Mismatch: local gateway must stay running; not a hosted SaaS.

## How it works

`gateway/src/jev.ts` uses `@typesafe-ai/sdk` Questions against TypeSafe or gateway providers that accept the same System One body, resolving keys via `TYPESAFE_API_KEY` / provider env vars. Integration evidence: [`gateway/src/jev.ts`](https://github.com/KeepGlide/askaway-model/blob/5d57c0dc23ab806fc55212bb61f2e17b39a0d194/gateway/src/jev.ts).

## Get started

Follow the README to install the local gateway and agent hooks, then set a TypeSafe key (or gateway) and exercise one permission prompt.

```sh
git clone https://github.com/KeepGlide/askaway-model.git && cd askaway-model
export TYPESAFE_API_KEY=...
# follow README gateway + hook setup
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/KeepGlide/askaway-model/blob/5d57c0dc23ab806fc55212bb61f2e17b39a0d194/README.md](https://github.com/KeepGlide/askaway-model/blob/5d57c0dc23ab806fc55212bb61f2e17b39a0d194/README.md)

## Limits and data handling

Agent prompt text and choice sets are sent to the configured Jev provider on your key and logged locally. Independent project; JEV is a TypeSafe trademark.

## Review and maintenance

Reviewed **2026-11-06** (Europe/Sofia) at [commit 5d57c0dc23ab](https://github.com/KeepGlide/askaway-model/tree/5d57c0dc23ab806fc55212bb61f2e17b39a0d194). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
