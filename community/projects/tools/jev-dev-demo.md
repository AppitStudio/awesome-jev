# jev-dev-demo (LIDR)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Spanish-language teaching repo with three runnable demos of 'Jev decides, the LLM reasons': Jira triage that classifies, prioritises and assigns each ticket with a confidence and escalates ambiguous ones, a pre-flight scan that flags existing bugs in the functions a ticket touches, and an LLM router that sends each PR to a large, small or no model (upstream reports 50–75% lower cost); every demo has a `--mock` mode.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/LIDR-academy/jev-dev-demo) |
| Maintainer | [LIDR-academy](https://github.com/LIDR-academy). Independently curated. |
| Format | npm scripts (`batch`, `scan`, `review`, `compare`, `costs`) with mock mode |
| Requirements | Node 22.18+; Jev and LLM keys in `.env` (or `--mock`); a Jira project for demo 1; a fork of the referenced repo for demo 2. |
| License | The reviewed tree has **no LICENSE file** — listed as Source available; reuse terms are not granted until the maintainer adds a license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Teach or present the state → typed question → probability → code decides pattern.
- Rehearse without keys using `--mock`.
- Mismatch: demo code and Spanish docs; no LICENSE file.

## How it works

[`shared/jev.ts`](https://github.com/LIDR-academy/jev-dev-demo/blob/b366263e17282e25596d790f446db6925cce3ffd/shared/jev.ts) implements the `POST /v1/systemone` contract against `https://api.typesafe.ai` (override with `JEV_BASE_URL`); thresholds turn probabilities into actions and 14 tests cover thresholds and LLM-answer parsing.

## Get started

Clone and run the demos in mock mode first (README):

```sh
git clone https://github.com/LIDR-academy/jev-dev-demo.git && cd jev-dev-demo
cp .env.example .env
npm test
npm run batch -- --mock
npm run review -- --mode=jev --mock && npm run compare
```

Live runs bill Jev (TypeSafe) and the configured LLM; `npm run costs` reports each run.

## Examples and demos

- Presenter script: [`docs/Guion-demo-Jev.pdf`](https://github.com/LIDR-academy/jev-dev-demo/blob/b366263e17282e25596d790f446db6925cce3ffd/docs/Guion-demo-Jev.pdf).

## Limits and data handling

Ticket and code excerpts go to TypeSafe and the LLM in live mode. Cost savings are upstream-reported. No LICENSE file — Source available. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-08** (Europe/Sofia) at [commit b366263e1728](https://github.com/LIDR-academy/jev-dev-demo/tree/b366263e17282e25596d790f446db6925cce3ffd). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
