# Browser-agent decision bench by Decido (Apache-2.0 replay benchmark that scores Jev Ultrafast's decision model on 1,500 recorded Mind2Web steps)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Benchmark for the model that picks a browser agent's next action in Jev Ultrafast: which operation and which element. It replays 1,500 human-recorded Multimodal-Mind2Web steps through the agent's own request builder and sends the identical request to each model behind a `/v1/systemone`-shaped endpoint. The published table has Jev 1.14 at 59.9% and Jev 1.13 at 54.4% step accuracy. Vendor disclosure: Decido publishes this benchmark and its own unreleased web-trained Decido-1 tops the table (78.6%), so read the comparison as a vendor result.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/decido-ai/browser-agent-decision-bench) |
| Maintainer | [decido-ai](https://github.com/decido-ai). Independently curated. |
| Format | Python benchmark scripts with a password-protected step set (Apache-2.0) |
| Requirements | Python and the pinned `jev-ultrafast` dependency; re-scoring the bundled results needs no key, and running Jev needs `TYPESAFE_API_KEY`. |
| License | [Apache-2.0](https://github.com/decido-ai/browser-agent-decision-bench/blob/696ae235ae071ff898e242876a50340b948dc167/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. The benchmark is published by Decido, which also builds the model that tops its table. |
| Jev evidence | [`decision_bench.py`](https://github.com/decido-ai/browser-agent-decision-bench/blob/696ae235ae071ff898e242876a50340b948dc167/decision_bench.py) at the pinned commit. |

## When to use

- Compare decision models for browser-agent steps on the same recorded cases, or check how Jev Ultrafast's model scores.
- Mismatch: a live task-success benchmark; it replays recorded steps offline with 50 candidate elements and has no wait, scroll or done labels.

## How it works

`decision_bench.py run` posts each step's request, built by `jev_ultrafast.model.choose()`, to any endpoint such as `https://api.typesafe.ai/v1/systemone`, and `score` and `compare` grade the answers with bootstrap confidence intervals. Integration evidence: [`decision_bench.py`](https://github.com/decido-ai/browser-agent-decision-bench/blob/696ae235ae071ff898e242876a50340b948dc167/decision_bench.py).

## Get started

Re-score the bundled results first (no key), then optionally run Jev yourself with your own key.

```sh
git clone https://github.com/decido-ai/browser-agent-decision-bench && cd browser-agent-decision-bench
pip install -r requirements.txt
python decision_bench.py score --steps data/steps-final.zip results/*.jsonl
export TYPESAFE_API_KEY=...   # only to run Jev yourself
python decision_bench.py run --steps data/steps-final.zip --url https://api.typesafe.ai/v1/systemone --api-key-env TYPESAFE_API_KEY --model jev-1.14.0 --out results/my-jev.jsonl
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/decido-ai/browser-agent-decision-bench/blob/696ae235ae071ff898e242876a50340b948dc167/README.md](https://github.com/decido-ai/browser-agent-decision-bench/blob/696ae235ae071ff898e242876a50340b948dc167/README.md)
- Jev Ultrafast: [github.com/browser-use/jev-ultrafast](https://github.com/browser-use/jev-ultrafast)

## Limits and data handling

Vendor-published numbers were not reproduced here. The step set is zipped with the Mind2Web password so it stays out of web crawls. Live runs send page snapshots to the endpoint you choose and cost money; Jev's training data is not public.

## Review and maintenance

Reviewed **2026-11-18** (Europe/Sofia) at [commit 696ae235ae07](https://github.com/decido-ai/browser-agent-decision-bench/tree/696ae235ae071ff898e242876a50340b948dc167). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
