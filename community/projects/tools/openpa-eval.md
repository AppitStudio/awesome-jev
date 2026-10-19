# OpenPA Eval (prior authorization cascade)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

TypeScript workbench and MCP server that tests how much reasoning prior authorization needs on synthetic FHIR R4 records: rules first, then Jev typed decisions, then small and frontier LLMs, with every citation checked and uncertain cases sent to clinical review.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/dylanmarks/fhir-prior-auth-eval) |
| Maintainer | [dylanmarks](https://github.com/dylanmarks). Independently curated. |
| Format | Evaluation workbench + MCP server (TypeScript, Node 22) |
| Requirements | Node.js 22 and npm; the default demo runs offline without credentials; live runs need a Jev provider key (`JEV_MODEL=typesafe/jev-1.13`). |
| License | [MIT](https://github.com/dylanmarks/fhir-prior-auth-eval/blob/2ddac740c99d1573306507c0ee145a69958e8f3d/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Discovered via X ([post](https://x.com/dylanmarks/status/2112205087942783021)). |
| Jev evidence | [`packages/evaluators/src/jev/jev-evaluator.ts`](https://github.com/dylanmarks/fhir-prior-auth-eval/blob/2ddac740c99d1573306507c0ee145a69958e8f3d/packages/evaluators/src/jev/jev-evaluator.ts) at the pinned commit. |

## When to use

- Measure where a rules → Jev → LLM → human cascade saves cost without more confidently wrong answers.
- Explore evidence grounding, abstention and counterfactual tests on synthetic clinical records.
- Mismatch: public research prototype on synthetic data; not payer authorization or clinical advice.

## How it works

Each policy criterion first goes through integrity checks and deterministic rules. Unresolved criteria go to Jev as typed decisions in `packages/evaluators/src/jev/jev-evaluator.ts`; answers below the confidence threshold continue to a small generative model and then a frontier model. Every answer's citations are verified against the raw FHIR resources, and contradictions or invalid citations stop the cascade for clinical review. Integration evidence: [`packages/evaluators/src/jev/jev-evaluator.ts`](https://github.com/dylanmarks/fhir-prior-auth-eval/blob/2ddac740c99d1573306507c0ee145a69958e8f3d/packages/evaluators/src/jev/jev-evaluator.ts).

## Get started

From the upstream README: install with npm and run the offline benchmark, build and tests.

```sh
git clone https://github.com/dylanmarks/fhir-prior-auth-eval.git
cd fhir-prior-auth-eval
npm ci
npm run benchmark
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- [youtu.be/Xz5sfbvqN6c](https://youtu.be/Xz5sfbvqN6c)
- README model comparison and evidence workbench screenshots

## Limits and data handling

Synthetic records only; live provider behavior and the cost/quality claims are not validated, per the README. Live runs send record text to the configured providers.

## Review and maintenance

Reviewed **2026-10-20** (Europe/Sofia) at [commit 2ddac740c99d](https://github.com/dylanmarks/fhir-prior-auth-eval/tree/2ddac740c99d1573306507c0ee145a69958e8f3d). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
