# askif

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

TypeScript toolkit for typed branching on Jev answers — `ask.if(…).elseif()`, `ask.switch`, `ask.score` and `.unsure()` bands — with a provider-neutral `Backend` contract, a mock backend for tests, and `@askif/jev` as the TypeSafe Jev bundle.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/asakaxgit/askif) |
| Product homepage | [www.npmjs.com](https://www.npmjs.com/package/@askif/jev) |
| Maintainer | [asakaxgit](https://github.com/asakaxgit). Independently curated. |
| Format | TypeScript library (npm `askif` 0.2.0, `@askif/jev` 0.1.2 at review) |
| Requirements | Node.js 22+ on a server (the TypeSafe SDK refuses to run in a browser); `TYPESAFE_API_KEY`. |
| License | [MIT](https://github.com/asakaxgit/askif/blob/12953a5b3c1929024db1ae43ba392e1ae6d5ad0d/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Branch application logic on a yes/no or pick-one Jev answer with an explicit threshold and an unsure path.
- Batch several questions and unit-test the chains offline with the mock backend.
- Mismatch: server-side only; unofficial, not affiliated with TypeSafe.

## How it works

The core chain logic and `Backend` contract live in [`packages/askif/src/core.ts`](https://github.com/asakaxgit/askif/blob/12953a5b3c1929024db1ae43ba392e1ae6d5ad0d/packages/askif/src/core.ts); [`packages/jev`](https://github.com/asakaxgit/askif/tree/12953a5b3c1929024db1ae43ba392e1ae6d5ad0d/packages/jev) wires the TypeSafe SDK. Defaults: threshold 0.5, configurable `minConfidence` and per-call overrides.

## Get started

Install and ask:

```sh
npm install askif @askif/jev
export TYPESAFE_API_KEY=...
# import { ask } from "@askif/jev";
# await ask.if(state, "is spam", onSpam, { threshold: 0.9 });
```

Live commands contact TypeSafe (or the configured provider) and may incur charges.

## Examples and demos

- Offline [`packages/askif/examples`](https://github.com/asakaxgit/askif/tree/12953a5b3c1929024db1ae43ba392e1ae6d5ad0d/packages/askif/examples) (mock backend) and live [`packages/jev/examples`](https://github.com/asakaxgit/askif/tree/12953a5b3c1929024db1ae43ba392e1ae6d5ad0d/packages/jev/examples).
- README *Writing good questions* and *Errors* sections.

## Limits and data handling

State is sent to TypeSafe on live calls. Early (0.x). Not run on the review host.

## Review and maintenance

Reviewed **2026-10-07** (Europe/Sofia) at [commit 12953a5b3c19](https://github.com/asakaxgit/askif/tree/12953a5b3c1929024db1ae43ba392e1ae6d5ad0d). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
