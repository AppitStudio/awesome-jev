# System 1 Fraud Interceptor (demo racing Jev against Gemini on synthetic card transactions; Spanish)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Personal experiment (Spanish README) inspired by Kahneman's fast and slow thinking: a web demo sends each synthetic transaction in parallel to Jev for a typed fraud decision with confidence and to Gemini Flash Lite for a decision plus written report, and shows latency, cost and agreement side by side. The author states it is not a benchmark.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ordepas/system1-fraud-interceptor-demo) |
| Maintainer | [ordepas](https://github.com/ordepas). Independently curated. |
| Format | Web demo (React + Node server) |
| Requirements | Node.js; your own TypeSafe and Gemini keys. |
| License | [MIT](https://github.com/ordepas/system1-fraud-interceptor-demo/blob/a018fb3d491caa58c38e7dccbec4b544bd54cb17/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`server.ts`](https://github.com/ordepas/system1-fraud-interceptor-demo/blob/a018fb3d491caa58c38e7dccbec4b544bd54cb17/server.ts) at the pinned commit. |

## When to use

- Show fast typed decisions next to an LLM audit on the same input.
- Mismatch: synthetic data and a personal demo, not a benchmark.

## How it works

`server.ts` builds the System One request (POST `https://api.typesafe.ai/v1/systemone`) with choice questions for each transaction and returns the choice, probability and latency; `eval/eval_demo.mjs` runs a batch comparison. Integration evidence: [`server.ts`](https://github.com/ordepas/system1-fraud-interceptor-demo/blob/a018fb3d491caa58c38e7dccbec4b544bd54cb17/server.ts).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/ordepas/system1-fraud-interceptor-demo.git && cd system1-fraud-interceptor-demo
npm install
npm run dev
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Batch eval script: [github.com/ordepas/system1-fraud-interceptor-demo/blob/main/eval/eval_demo.mjs](https://github.com/ordepas/system1-fraud-interceptor-demo/blob/main/eval/eval_demo.mjs)

## Limits and data handling

Only synthetic transactions are sent to TypeSafe and Google. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-02** (Europe/Sofia) at [commit a018fb3d491c](https://github.com/ordepas/system1-fraud-interceptor-demo/tree/a018fb3d491caa58c38e7dccbec4b544bd54cb17). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
