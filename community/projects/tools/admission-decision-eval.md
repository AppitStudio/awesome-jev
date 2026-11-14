# admission-decision-eval (reproducible comparison of Jev and other decision models on admitting an agent's knowledge-base writes)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

One dependency-free script and 85 labeled synthetic cases testing whether an AI agent's write to a knowledge base can be admitted automatically or needs human review. It compares Jev 1.14.0 with Clef, Perplexity Decider, Microsoft and Gemini Decision 1 and GPT-6 Luna on recall, routine admit rate, order sensitivity and latency, against gates set before the runs.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/nicia-ai/admission-decision-eval) |
| Maintainer | [nicia-ai](https://github.com/nicia-ai). Independently curated. |
| Format | Node.js evaluation script with cases, results and run history (Apache-2.0) |
| Requirements | Node.js and a key per backend you run (TypeSafe for Jev; others optional). |
| License | [Apache-2.0](https://github.com/nicia-ai/admission-decision-eval/blob/90c84f7fbaaf6725b4649104246e156812bb14cd/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`run.mjs`](https://github.com/nicia-ai/admission-decision-eval/blob/90c84f7fbaaf6725b4649104246e156812bb14cd/run.mjs) at the pinned commit. |

## When to use

- Choose a decision model for gating agent writes into shared memory or a knowledge base.
- Mismatch: treating 85 synthetic cases as proof for your own data; rerun on your cases.

## How it works

`run.mjs` defines the TypeSafe backend as `https://api.typesafe.ai/v1/systemone` with `jev-1.14.0` (and `jev-preview`), runs original and reversed record orders at six in flight and one at a time, and scores each pass against fixed gates (recall ≥ 0.95, routine admit ≥ 0.85, p95 ≤ 2500 ms, no failed calls). Integration evidence: [`run.mjs`](https://github.com/nicia-ai/admission-decision-eval/blob/90c84f7fbaaf6725b4649104246e156812bb14cd/run.mjs).

## Get started

Clone and run the default backends, or pick them with `--backends`.

```sh
git clone https://github.com/nicia-ai/admission-decision-eval && cd admission-decision-eval
TYPESAFE_API_KEY=... node run.mjs --backends jev --passes 3
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README with results tables: [github.com/nicia-ai/admission-decision-eval/blob/90c84f7fbaaf6725b4649104246e156812bb14cd/README.md](https://github.com/nicia-ai/admission-decision-eval/blob/90c84f7fbaaf6725b4649104246e156812bb14cd/README.md)

## Limits and data handling

Synthetic cases go to each backend you enable. Evaluation dates differ between rows (Jev measured 2026-11-11), so latency rows are not a same-day comparison.

## Review and maintenance

Reviewed **2026-11-14** (Europe/Sofia) at [commit 90c84f7fbaaf](https://github.com/nicia-ai/admission-decision-eval/tree/90c84f7fbaaf6725b4649104246e156812bb14cd). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
