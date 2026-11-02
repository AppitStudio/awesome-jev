# Quorum (terminal room where agent CLIs work a problem together, with Jev gating and checking diagrams)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Go and TypeScript TUI that seats official agent CLIs (Claude Code, Codex, Gemini, Opencode, Kimi Code and more) in one channel or a round-based council with a Chair, digests and a consensus board. Jev is opt-in: it decides whether a reply would benefit from an animated diagram, skipping the generator call when not, and then checks the finished diagram is faithful to the reply.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Jbudone/quorum) |
| Maintainer | [Jbudone](https://github.com/Jbudone). Independently curated. |
| Format | TUI (Go + Bubble Tea) with a TypeScript engine |
| Requirements | Node.js with pnpm, Go, the agent CLIs you want; optional OpenRouter key for Jev. |
| License | [MIT](https://github.com/Jbudone/quorum/blob/32d5c53bf2911c67bdb35d70416a62ea3b8cdf63/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`engine/src/jev.ts`](https://github.com/Jbudone/quorum/blob/32d5c53bf2911c67bdb35d70416a62ea3b8cdf63/engine/src/jev.ts) at the pinned commit. |

## When to use

- Run several coding agents on one hard problem and watch them converge.
- Mismatch: Jev only gates and verifies diagrams; it does not steer the council.

## How it works

`engine/src/jev.ts` calls `typesafe/jev-1.13` through OpenRouter's decisions endpoint with noul and score questions; a low faithfulness score means the diagram is not shown. Integration evidence: [`engine/src/jev.ts`](https://github.com/Jbudone/quorum/blob/32d5c53bf2911c67bdb35d70416a62ea3b8cdf63/engine/src/jev.ts).

## Get started

From the upstream README (not run on the review host):

```sh
cd quorum && pnpm install
./quorum --mock   # scripted agents, no tokens
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Repository README: [github.com/Jbudone/quorum#readme](https://github.com/Jbudone/quorum#readme)

## Limits and data handling

With Jev on, reply text is sent to OpenRouter/TypeSafe. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-02** (Europe/Sofia) at [commit 32d5c53bf291](https://github.com/Jbudone/quorum/tree/32d5c53bf2911c67bdb35d70416a62ea3b8cdf63). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
