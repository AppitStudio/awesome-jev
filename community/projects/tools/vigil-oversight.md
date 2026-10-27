# Vigil (decision ledger and circuit breaker for agents, with a Jev judge)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

TypeScript kernel that makes every agent decision interceptable, traceable and calibratable: an orchestrator loop with stop-loss, routing, quality gates, acceptance and escalation, each fork a kernel ruling recorded in an append-only hash-chained, Ed25519-signed ledger; the judge can be TypeSafe Jev or a local `/v1/systemone` server. Chinese-language docs.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/leo-bone/vigil) |
| Maintainer | [leo-bone](https://github.com/leo-bone). Independently curated. |
| Format | TypeScript library and CLI |
| Requirements | Node.js; a TypeSafe API key for the Jev judge, or a local System One-compatible server. |
| License | [MIT](https://github.com/leo-bone/vigil/blob/a934d92b1eb848c9e3b98e1ade28e47098e0b01b/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/judge/jev.ts`](https://github.com/leo-bone/vigil/blob/a934d92b1eb848c9e3b98e1ade28e47098e0b01b/src/judge/jev.ts) at the pinned commit. |

## When to use

- Add an auditable, signed decision record and circuit breaker around multi-agent work.
- Calibrate decision thresholds from recorded outcomes.
- Mismatch: early project; examples run against the bundled demos.

## How it works

`src/judge/jev.ts` adapts Jev (default `https://api.typesafe.ai/v1/systemone`, `jev-latest`) and any server that speaks the same dialect; the kernel applies policy to the probabilities. Integration evidence: [`src/judge/jev.ts`](https://github.com/leo-bone/vigil/blob/a934d92b1eb848c9e3b98e1ade28e47098e0b01b/src/judge/jev.ts).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/leo-bone/vigil && cd vigil
node examples/demo.ts
npm test
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README (Chinese): [github.com/leo-bone/vigil#readme](https://github.com/leo-bone/vigil#readme)

## Limits and data handling

Decision context goes to TypeSafe when the Jev judge is used. The ledger stays local.

## Review and maintenance

Reviewed **2026-10-27** (Europe/Sofia) at [commit a934d92b1eb8](https://github.com/leo-bone/vigil/tree/a934d92b1eb848c9e3b98e1ade28e47098e0b01b). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
