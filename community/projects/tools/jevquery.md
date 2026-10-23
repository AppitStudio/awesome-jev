# JevQuery (sentences to typed query plans for Drizzle and Prisma)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

TypeScript library that turns a sentence such as "orders over 100 dollars, biggest first" into a typed query plan (table, filters, columns, order, limit) by having Jev pick each part from your schema. Drizzle, Prisma or plain SQL builders run it; no model writes SQL.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/saembit/jevquery) |
| Maintainer | [saembit](https://github.com/saembit). Independently curated. |
| Format | TypeScript library |
| Requirements | Node.js; a TypeSafe API key; Drizzle, Prisma or your own SQL builder. |
| License | [MIT](https://github.com/saembit/jevquery/blob/2f56dc67dfa65d910503a02ba57ef03fb40f0759/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/deciders.ts`](https://github.com/saembit/jevquery/blob/2f56dc67dfa65d910503a02ba57ef03fb40f0759/src/deciders.ts) at the pinned commit. |

## When to use

- Add natural-language filters to an admin panel or internal tool without letting a model write SQL.
- Validate the plan with any Standard Schema validator before it runs.
- Mismatch: plans limited to what your schema description offers; no joins invented by a model.

## How it works

`typesafeDecider` in `src/deciders.ts` posts choice questions to `https://api.typesafe.ai/v1/systemone` (`jev-latest` by default). `plan()` builds the query from the chosen options. Integration evidence: [`src/deciders.ts`](https://github.com/saembit/jevquery/blob/2f56dc67dfa65d910503a02ba57ef03fb40f0759/src/deciders.ts).

## Get started

The README shows `npm install jevquery`, but no npm release was found on 2026-10-24. From source (not run on the review host):

```sh
git clone https://github.com/saembit/jevquery
cd jevquery && npm install
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Drizzle, Prisma and tRPC examples in the README: [github.com/saembit/jevquery#readme](https://github.com/saembit/jevquery#readme)

## Limits and data handling

The sentence and your schema descriptions are sent to TypeSafe. Not affiliated with TypeSafe, Drizzle or Prisma.

## Review and maintenance

Reviewed **2026-10-24** (Europe/Sofia) at [commit 2f56dc67dfa6](https://github.com/saembit/jevquery/tree/2f56dc67dfa65d910503a02ba57ef03fb40f0759). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
