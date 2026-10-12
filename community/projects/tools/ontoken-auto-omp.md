# ontoken-auto-omp

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Native OMP extension that routes each prompt to an OnToken model tier using TypeSafe Jev when a key is available, with heuristic fallback so turns still complete. Distinct from the listed ontoken-auto project.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/priaculun/ontoken-auto-omp) |
| Maintainer | [priaculun](https://github.com/priaculun). Independently curated. |
| Format | TypeScript · OMP extension |
| Requirements | OMP; optional `TYPESAFE_API_KEY`. |
| License | [MIT](https://github.com/priaculun/ontoken-auto-omp/blob/2c2c9889809fec13be58ea252fee086910f9527e/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |

## When to use

- Adaptive model routing inside OMP with a System One classifier.
- Mismatch: OMP-specific; not a standalone CLI.

## How it works

Classifier asks Jev for difficulty/slot; routing module selects fast/work/… models. Evidence: [`src/classifier.ts`](https://github.com/priaculun/ontoken-auto-omp/blob/2c2c9889809fec13be58ea252fee086910f9527e/src/classifier.ts).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/priaculun/ontoken-auto-omp.git
# install as OMP extension per README
```

## Limits and data handling

Provider-bound inputs may be billed by TypeSafe/OpenRouter when live. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-12** (Europe/Sofia) at [commit 2c2c9889809f](https://github.com/priaculun/ontoken-auto-omp/tree/2c2c9889809fec13be58ea252fee086910f9527e). Inspected the upstream README, LICENSE, and the Jev integration evidence linked above; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
