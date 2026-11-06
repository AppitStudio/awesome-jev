# open-decision (vendor-neutral decision runtime with a TypeSafe Jev provider)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Capability-aware, vendor-neutral decision runtime that can call TypeSafe Jev through `createTypeSafeProvider` (reads `TYPESAFE_API_KEY`) or local engines behind the same interface.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/gbesse/open-decision) |
| Maintainer | [gbesse](https://github.com/gbesse). Independently curated. |
| Format | TypeScript library (MIT) |
| Requirements | Node.js/TypeScript and `TYPESAFE_API_KEY` when using the TypeSafe provider. |
| License | [MIT](https://github.com/gbesse/open-decision/blob/3c4621cfebe11d8c815b5178d19a3ceb3e3b0448/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/index.ts`](https://github.com/gbesse/open-decision/blob/3c4621cfebe11d8c815b5178d19a3ceb3e3b0448/src/index.ts) at the pinned commit. |

## When to use

- Swap between Jev and local decision engines behind one API.
- Keep provider choice out of call sites.
- Mismatch: you still implement packs/policies on top.

## How it works

`createTypeSafeProvider` in `src/index.ts` reads `TYPESAFE_API_KEY` and posts to the TypeSafe endpoint; other providers implement the same `DecisionProvider` shape. Integration evidence: [`src/index.ts`](https://github.com/gbesse/open-decision/blob/3c4621cfebe11d8c815b5178d19a3ceb3e3b0448/src/index.ts).

## Get started

From the upstream README (not run on the review host):

```sh
export TYPESAFE_API_KEY=...
# import { createTypeSafeProvider } from "open-decision" (see README)
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/gbesse/open-decision/blob/3c4621cfebe11d8c815b5178d19a3ceb3e3b0448/README.md](https://github.com/gbesse/open-decision/blob/3c4621cfebe11d8c815b5178d19a3ceb3e3b0448/README.md)

## Limits and data handling

When the TypeSafe provider is selected, decision inputs go to TypeSafe on your key.

## Review and maintenance

Reviewed **2026-11-06** (Europe/Sofia) at [commit 3c4621cfebe1](https://github.com/gbesse/open-decision/tree/3c4621cfebe11d8c815b5178d19a3ceb3e3b0448). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
