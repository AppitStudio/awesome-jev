# IDU Cross-CLI (agent router and quality harness with TypeSafe Jev arbitration)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Spanish-language harness that delegates tasks to real AI coding CLIs (Claude Code, OpenCode, Codex, Pi, Kimi, Qwen and more), audits every change, and arbitrates autonomous decisions with local Kev, TypeSafe Jev or a deterministic fallback.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Wladimirfn/IDU-PI) |
| Maintainer | [Wladimirfn](https://github.com/Wladimirfn). Independently curated. |
| Format | TypeScript CLI + MCP server (no SPDX license file on the reviewed commit) |
| Requirements | Node.js, the coding CLIs you want to delegate to, and optionally a TypeSafe API key. |
| License | NONE on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/arbitration.ts`](https://github.com/Wladimirfn/IDU-PI/blob/a6d8bc4dec96bb0b9a08a7631cefafaa996e8584/src/arbitration.ts) at the pinned commit. |

## When to use

- Route coding tasks across several real agent CLIs with resumable sessions.
- Gate autonomous decisions with a typed arbiter and a durable decision ledger.
- Mismatch: README is in Spanish; no OSI license on the reviewed commit.

## How it works

`src/arbitration.ts` defaults to `https://api.typesafe.ai/v1/systemone` with `jev-latest` for the cloud tier of `idu_arbitrate`, between a local GPU model and a zero-cost Risk-First fallback. Integration evidence: [`src/arbitration.ts`](https://github.com/Wladimirfn/IDU-PI/blob/a6d8bc4dec96bb0b9a08a7631cefafaa996e8584/src/arbitration.ts).

## Get started

Clone, install dependencies, copy `.env.example`, and register the MCP server per README.

```sh
git clone https://github.com/Wladimirfn/IDU-PI.git && cd IDU-PI
export TYPESAFE_API_KEY=...
npm install && npm test
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/Wladimirfn/IDU-PI/blob/a6d8bc4dec96bb0b9a08a7631cefafaa996e8584/README.md](https://github.com/Wladimirfn/IDU-PI/blob/a6d8bc4dec96bb0b9a08a7631cefafaa996e8584/README.md)

## Limits and data handling

When the TypeSafe tier is enabled, decision context is sent to TypeSafe on your key; the local and deterministic tiers stay on your machine.

## Review and maintenance

Reviewed **2026-11-08** (Europe/Sofia) at [commit a6d8bc4dec96](https://github.com/Wladimirfn/IDU-PI/tree/a6d8bc4dec96bb0b9a08a7631cefafaa996e8584). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
