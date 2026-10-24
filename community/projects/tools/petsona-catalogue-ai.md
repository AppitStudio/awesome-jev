# Petsona Catalogue AI (evidence-backed pet product tagging with Jev or Laya)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

AI slice of the Petsona Shopify app: product text, label OCR and manufacturer pages become evidence spans, code proposes values, and a decision model (Jev 1.13.0 or open-weight Laya) marks each one supported, contradicted, unknown or conflicting before a merchant reviews it.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/jeromtom/petsona-catalogue-ai) |
| Maintainer | [jeromtom](https://github.com/jeromtom). Independently curated. |
| Format | Node.js demo and library code (TypeScript) |
| Requirements | Node.js 22+; a TypeSafe key for Jev, or a Vercel AI Gateway key for Laya; runs offline without keys up to the model call. |
| License | [MIT](https://github.com/jeromtom/petsona-catalogue-ai/blob/358f7d21a79f80310275237ca97726d52f076257/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`demo/classify.ts`](https://github.com/jeromtom/petsona-catalogue-ai/blob/358f7d21a79f80310275237ca97726d52f076257/demo/classify.ts) at the pinned commit. |

## When to use

- Tag species, life stage and allergens with the source sentence attached.
- Keep a model from inventing ingredients by asking only closed questions.
- Mismatch: hackathon submission (AIBoomi, October 2026); the Shopify app itself is not in this repository.

## How it works

`demo/classify.ts` sends one atomic question per proposed value to `https://api.typesafe.ai/v1/systemone` (`jev-1.13.0`) or to Laya through Vercel AI Gateway, then validates the verdicts and records spend. Integration evidence: [`demo/classify.ts`](https://github.com/jeromtom/petsona-catalogue-ai/blob/358f7d21a79f80310275237ca97726d52f076257/demo/classify.ts).

## Get started

From the upstream README (not run on the review host):

```sh
npm install
npm test
npm run demo:all   # dry run, no credentials
TYPESAFE_API_KEY=... npm run demo -- demo/samples/ocean-fish-adult-cat-food.json
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Product site: [petsona.xyz](https://petsona.xyz)
- README: [github.com/jeromtom/petsona-catalogue-ai#readme](https://github.com/jeromtom/petsona-catalogue-ai#readme)

## Limits and data handling

Product text is sent to the chosen provider. The README notes the free Laya alias ends on 31 October 2026.

## Review and maintenance

Reviewed **2026-10-24** (Europe/Sofia) at [commit 358f7d21a79f](https://github.com/jeromtom/petsona-catalogue-ai/tree/358f7d21a79f80310275237ca97726d52f076257). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
