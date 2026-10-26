# omp-maestro (oh-my-pi setup in one command, with a Jev Router choosing models)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

One-command oh-my-pi setup with curated public plugins and skills, three switchable model ensembles and the author's own Jev Router extension, which asks Jev which model should take each request so that, in the author's words, Claude thinks, GPT codes and Jev decides who plays.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/hsmoviich/omp-maestro) |
| Maintainer | [hsmoviich](https://github.com/hsmoviich). Independently curated. |
| Format | oh-my-pi setup script and extension (Node.js, npm `omp-maestro`) |
| Requirements | oh-my-pi; npx or bunx; a TypeSafe API key for the Jev Router, plus keys for the models in your ensemble. |
| License | [MIT](https://github.com/hsmoviich/omp-maestro/blob/07f21292555b4912f535c7804a93578a43f0125a/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`extensions/jev-router.ts`](https://github.com/hsmoviich/omp-maestro/blob/07f21292555b4912f535c7804a93578a43f0125a/extensions/jev-router.ts) at the pinned commit. |

## When to use

- Set up a working oh-my-pi environment quickly.
- Route requests between models with Jev instead of fixed rules.
- Mismatch: an opinionated personal setup; ensembles assume access to the listed models.

## How it works

`extensions/jev-router.ts` uses `@typesafe-ai/sdk` with `jev-latest` to ask which configured model fits the request and switches to it. Integration evidence: [`extensions/jev-router.ts`](https://github.com/hsmoviich/omp-maestro/blob/07f21292555b4912f535c7804a93578a43f0125a/extensions/jev-router.ts).

## Get started

From the upstream README (not run on the review host):

```sh
npx omp-maestro
export TYPESAFE_API_KEY=...   # or add it to ~/.omp/agent/.env
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- npm: [www.npmjs.com/package/omp-maestro](https://www.npmjs.com/package/omp-maestro)
- README: [github.com/hsmoviich/omp-maestro#readme](https://github.com/hsmoviich/omp-maestro#readme)

## Limits and data handling

Request summaries go to TypeSafe for routing; the chosen model's provider receives the request itself.

## Review and maintenance

Reviewed **2026-10-26** (Europe/Sofia) at [commit 07f21292555b](https://github.com/hsmoviich/omp-maestro/tree/07f21292555b4912f535c7804a93578a43f0125a). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
