# Agentic Failure Attribution (what agent traces do and don't tell you, with Jev step judgments)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Study on τ-bench banking (20 models, 7,760 conversations, 97 tasks) testing the signals trace-QA tools rely on against real outcomes; Jev judged each step and every user message (17,160 calls), and the finding is that task difficulty predicts failure better than anything in the trace, retrieval matters within a task, and user pushback is not an early warning. Includes a trace dashboard.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Sudarsh3301/trace-analysis) |
| Maintainer | [Sudarsh3301](https://github.com/Sudarsh3301). Independently curated. |
| Format | Python analysis with a Next.js trace dashboard |
| Requirements | Python and Node.js; a TypeSafe API key to rerun the Jev judgments. |
| License | [MIT](https://github.com/Sudarsh3301/trace-analysis/blob/7c08fd6fa6ea9925082df48e6b8ac4ac25ec0e02/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`analysis/jev.py`](https://github.com/Sudarsh3301/trace-analysis/blob/7c08fd6fa6ea9925082df48e6b8ac4ac25ec0e02/analysis/jev.py) at the pinned commit. |

## When to use

- Check whether trace-based failure predictors beat a simple per-task baseline.
- Reuse the Jev step-judgment code for your own agent traces.
- Mismatch: one benchmark domain; numbers are the author's.

## How it works

`analysis/jev.py` uses the TypeSafe Python SDK with Choice and Noul questions, pinned to `jev-1.14.0`, with results cached by request hash; `lib/jev/client.ts` does the same for the dashboard. Integration evidence: [`analysis/jev.py`](https://github.com/Sudarsh3301/trace-analysis/blob/7c08fd6fa6ea9925082df48e6b8ac4ac25ec0e02/analysis/jev.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/Sudarsh3301/trace-analysis && cd trace-analysis
# see the README for the analysis steps and the dashboard
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README with findings: [github.com/Sudarsh3301/trace-analysis#readme](https://github.com/Sudarsh3301/trace-analysis#readme)

## Limits and data handling

Conversation text from the public benchmark goes to TypeSafe when rerun. Findings are associations reported by the author, not verified here.

## Review and maintenance

Reviewed **2026-10-27** (Europe/Sofia) at [commit 7c08fd6fa6ea](https://github.com/Sudarsh3301/trace-analysis/tree/7c08fd6fa6ea9925082df48e6b8ac4ac25ec0e02). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
