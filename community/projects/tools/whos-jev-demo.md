# Who's Jev by Craig Hanenberg (seven TypeScript examples and a short deck that introduce Jev, from one yes/no to Jev hooks inside the pi coding agent)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

A Vue 3 lab and seven-slide deck for teaching Jev. Five examples call Jev from plain code (prompt-injection gate, support triage, ticket priority, bash-command gate, model routing); two run it inside the pi coding agent, as guardrail hooks the agent never sees and as a tool it chooses to call. Without a key the code examples run on an offline mock.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Craigels07/whos-jev-demo) |
| Maintainer | [Craigels07](https://github.com/Craigels07). Independently curated. |
| Format | TypeScript examples + Vue 3 lab and deck |
| Requirements | Node.js 22+ and `just`; a TypeSafe key for live runs; for the pi examples, pi and an Anthropic-compatible endpoint (the author uses a local proxy). |
| License | No license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`apps/whos-jev/src/core/client.ts`](https://github.com/Craigels07/whos-jev-demo/blob/228c36c86e88a6df81025a692bcffdf911d375a1/apps/whos-jev/src/core/client.ts) at the pinned commit. |

## When to use

- Present or learn Jev with runnable examples that ramp from a single Noul to agent guardrails.
- Mismatch: production code; these are teaching examples.

## How it works

`apps/whos-jev/src/core/client.ts` calls `https://api.typesafe.ai/v1/systemone`; the server switches to `JEV_BACKEND=mock` when no `TYPESAFE_API_KEY` is set. Integration evidence: [`apps/whos-jev/src/core/client.ts`](https://github.com/Craigels07/whos-jev-demo/blob/228c36c86e88a6df81025a692bcffdf911d375a1/apps/whos-jev/src/core/client.ts).

## Get started

Install the lab, add a key (or use the mock) and open it locally.

```sh
git clone https://github.com/Craigels07/whos-jev-demo && cd whos-jev-demo
cd apps/whos-jev/web && npm install && cd ../../..
cp .env.example .env   # TYPESAFE_API_KEY
just web               # http://127.0.0.1:4399
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Examples README: [github.com/Craigels07/whos-jev-demo/blob/228c36c86e88a6df81025a692bcffdf911d375a1/apps/whos-jev/README.md](https://github.com/Craigels07/whos-jev-demo/blob/228c36c86e88a6df81025a692bcffdf911d375a1/apps/whos-jev/README.md)

## Limits and data handling

Live examples send their state to TypeSafe; the pi examples also call Claude. No license file: reuse terms are not granted.

## Review and maintenance

Reviewed **2026-11-23** (Europe/Sofia) at [commit 228c36c86e88](https://github.com/Craigels07/whos-jev-demo/tree/228c36c86e88a6df81025a692bcffdf911d375a1). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
