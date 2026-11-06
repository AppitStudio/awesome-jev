# NobleAgent (TypeScript chat-agent framework with an experimental Jev decider)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

TypeScript framework for front-of-house chat agents with a pluggable Decider interface; includes an experimental plain-HTTP TypeSafe Jev adapter marked experimental until the official SDK shape is confirmed.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/davolu/NobleAgent) |
| Maintainer | [davolu](https://github.com/davolu). Independently curated. |
| Format | TypeScript monorepo framework (MIT) |
| Requirements | Node.js/TypeScript and a TypeSafe key to use the experimental Jev decider. |
| License | [MIT](https://github.com/davolu/NobleAgent/blob/f5f2549824abd9441ff2752a7531dd6edcdde434/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`packages/decide/src/jev.ts`](https://github.com/davolu/NobleAgent/blob/f5f2549824abd9441ff2752a7531dd6edcdde434/packages/decide/src/jev.ts) at the pinned commit. |

## When to use

- Build a chat agent with an explicit decision/gate layer.
- Try Jev as one Decider behind the same interface.
- Mismatch: Jev adapter is experimental; verify against current TypeSafe docs before production.

## How it works

`packages/decide/src/jev.ts` `jevDecider` POSTs to `{TYPESAFE_BASE_URL||https://api.typesafe.ai/v1}` with Bearer `TYPESAFE_API_KEY` and implements the shared Decider interface. Integration evidence: [`packages/decide/src/jev.ts`](https://github.com/davolu/NobleAgent/blob/f5f2549824abd9441ff2752a7531dd6edcdde434/packages/decide/src/jev.ts).

## Get started

Clone, install workspace packages per README, set TYPESAFE_API_KEY, and wire `jevDecider` in an example agent.

```sh
git clone https://github.com/davolu/NobleAgent.git && cd NobleAgent
export TYPESAFE_API_KEY=...
npm install
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/davolu/NobleAgent/blob/f5f2549824abd9441ff2752a7531dd6edcdde434/README.md](https://github.com/davolu/NobleAgent/blob/f5f2549824abd9441ff2752a7531dd6edcdde434/README.md)

## Limits and data handling

Decision state and questions are sent to TypeSafe on your key. Adapter is labeled experimental in-repo.

## Review and maintenance

Reviewed **2026-11-06** (Europe/Sofia) at [commit f5f2549824ab](https://github.com/davolu/NobleAgent/tree/f5f2549824abd9441ff2752a7531dd6edcdde434). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
