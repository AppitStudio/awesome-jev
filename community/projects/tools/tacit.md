# Tacit

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

Local-first browser context harness: reads the page and navigation trail on your machine and hands them to Claude Code, Cursor, or any MCP agent, with a TypeSafe Jev-backed DecisionEngine (`core/jev.ts` → `/v1/systemone`).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/wujiajunhahah/tacit) |
| Maintainer | [wujiajunhahah](https://github.com/wujiajunhahah). Independently curated. |
| Format | Bun/TypeScript local app + MCP tools |
| Requirements | Bun; optional TYPESAFE_API_KEY when using the Jev decision path. |
| License | [MIT](https://github.com/wujiajunhahah/tacit/blob/9c0c6643f1c102f1589ebd17c4e4f3c51c2f2eb0/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`core/jev.ts`](https://github.com/wujiajunhahah/tacit/blob/9c0c6643f1c102f1589ebd17c4e4f3c51c2f2eb0/core/jev.ts) at the pinned commit. |

## When to use

- Stop copy-pasting page context into coding agents.
- Want optional typed Jev decisions over local browser state.
- Mismatch: primary product is context capture; Jev is the DecisionEngine backend.

## How it works

`core/jev.ts` implements the DecisionEngine interface against `POST {baseUrl}/v1/systemone` with TypeSafe Jev. MCP tools expose page/ledger context to agents without leaving the machine by default. Integration evidence: [`core/jev.ts`](https://github.com/wujiajunhahah/tacit/blob/9c0c6643f1c102f1589ebd17c4e4f3c51c2f2eb0/core/jev.ts).

## Get started

Install with Bun per README, run the local harness, connect an MCP client.

```sh
git clone https://github.com/wujiajunhahah/tacit && cd tacit
# bun install && bun run per README
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README demo GIF
- core/jev.ts

## Limits and data handling

Jev path needs a key and sends selected state to TypeSafe. Local-first defaults still deserve a privacy review for your threat model.

## Review and maintenance

Reviewed **2026-10-18** (Europe/Sofia) at [commit 9c0c6643f1c1](https://github.com/wujiajunhahah/tacit/tree/9c0c6643f1c102f1589ebd17c4e4f3c51c2f2eb0). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
