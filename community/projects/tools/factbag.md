# Factbag (TypeScript library turning documents into evidence and rule-based conclusions with Jev)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Early-alpha TypeScript library: Jev reads passages and assesses claims, the results become sourced evidence in a knowledge base, and your rules derive true/false/conflicted/unknown conclusions.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/factbag/factbag) |
| Maintainer | [factbag](https://github.com/factbag). Independently curated. |
| Format | TypeScript monorepo / npm packages (Apache-2.0; alpha) |
| Requirements | Node/pnpm and a TypeSafe key for the Jev provider. |
| License | [Apache-2.0](https://github.com/factbag/factbag/blob/fe8e98f666058a3dc6238bae4db6ee349c239be8/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`providers/jev/src/index.ts`](https://github.com/factbag/factbag/blob/fe8e98f666058a3dc6238bae4db6ee349c239be8/providers/jev/src/index.ts) at the pinned commit. |

## When to use

- Derive explainable conclusions from documents.
- Inspect conflicting evidence back to source passages.
- Mismatch: early alpha; APIs will change.

## How it works

The `providers/jev` package depends on `@typesafe-ai/sdk` and asks Jev to assess predicates on corpus passages; `examples/jev` shows a demo with tests. Integration evidence: [`providers/jev/src/index.ts`](https://github.com/factbag/factbag/blob/fe8e98f666058a3dc6238bae4db6ee349c239be8/providers/jev/src/index.ts).

## Get started

Install the packages per the README, define claims, add documents and run the Jev provider with your key.

```sh
git clone https://github.com/factbag/factbag.git && cd factbag
export TYPESAFE_API_KEY=...
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/factbag/factbag/blob/fe8e98f666058a3dc6238bae4db6ee349c239be8/README.md](https://github.com/factbag/factbag/blob/fe8e98f666058a3dc6238bae4db6ee349c239be8/README.md)

## Limits and data handling

Document passages are sent to TypeSafe for assessment.

## Review and maintenance

Reviewed **2026-11-10** (Europe/Sofia) at [commit fe8e98f66605](https://github.com/factbag/factbag/tree/fe8e98f666058a3dc6238bae4db6ee349c239be8). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
