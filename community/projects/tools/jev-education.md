# jev-education (open experiments with Jev in education: a learning-path map that diagnoses a student's first mistake)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Public experiments using Jev in education without real learner data. The main demo, a learning-path map for first-year junior-high maths, takes an equation and the student's working, has Jev choose the most likely first mistake, then offers a check question, review material or the next problem, and holds off when probabilities are low; it shows API latency, estimated cost and the raw request and response. Japanese-language docs.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/chaspy/jev-education) |
| Maintainer | [chaspy](https://github.com/chaspy). Independently curated. |
| Format | Cloudflare Workers apps (JavaScript) |
| Requirements | Node.js 22+ and a TypeSafe API key. |
| License | [MIT](https://github.com/chaspy/jev-education/blob/e10795557af6f25b2d21278799efb1014bc5e389/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`apps/learning-path/src/worker.mjs`](https://github.com/chaspy/jev-education/blob/e10795557af6f25b2d21278799efb1014bc5e389/apps/learning-path/src/worker.mjs) at the pinned commit. |

## When to use

- See how typed decisions can drive adaptive practice.
- Mismatch: Japanese UI and docs; demo data only.

## How it works

`apps/learning-path/src/worker.mjs` posts the problem and working to `https://api.typesafe.ai/v1/systemone` and records cost per call; an adaptive simulation logs its own Jev calls. Integration evidence: [`apps/learning-path/src/worker.mjs`](https://github.com/chaspy/jev-education/blob/e10795557af6f25b2d21278799efb1014bc5e389/apps/learning-path/src/worker.mjs).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/chaspy/jev-education && cd jev-education
npm ci
# put TYPESAFE_API_KEY=... in .env
npm run dev
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Live demo: [jev-education-learning-path.take-she12.workers.dev](https://jev-education-learning-path.take-she12.workers.dev)
- README (Japanese): [github.com/chaspy/jev-education#readme](https://github.com/chaspy/jev-education#readme)

## Limits and data handling

Entered problems and working go to TypeSafe. No real learner data is used.

## Review and maintenance

Reviewed **2026-10-28** (Europe/Sofia) at [commit e10795557af6](https://github.com/chaspy/jev-education/tree/e10795557af6f25b2d21278799efb1014bc5e389). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
