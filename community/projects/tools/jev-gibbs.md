# Jev in Large Language Gibbs

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Replication of the TruthfulQA consistent-reasoning experiment from Large Language Gibbs (arXiv 2606.19264) with Jev supplying per-claim conditionals, plus controls, GSM8K, knights-and-knaves, entity resolution and kinship tests of where Gibbs helps.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/eumemic/jev-gibbs) |
| Maintainer | [eumemic](https://github.com/eumemic). Independently curated. |
| Format | Python research scripts with raw results and logs |
| Requirements | Python 3, a TypeSafe API key; RunPod and a GPU only for the paper-model comparison. |
| License | [MIT](https://github.com/eumemic/jev-gibbs/blob/347ba11eb35e22590ccdc161c36f19fb27361414/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`jev_gibbs.py`](https://github.com/eumemic/jev-gibbs/blob/347ba11eb35e22590ccdc161c36f19fb27361414/jev_gibbs.py) at the pinned commit. |

## When to use

- Read a careful replication of a structured-inference method using Jev as the conditional model.
- Reuse the scripts and logged results to test Gibbs-style consistency on your own claims.
- Mismatch: research code, not a library; full runs make many paid calls.

## How it works

`jev_gibbs.py` posts claim questions to `https://api.typesafe.ai/v1/systemone` (`jev-latest`, which resolved to jev-1.13.0 in the runs) in zero-shot, probe, context and Gibbs modes; analysis scripts compare seeds and count answer switches. Raw outputs are committed under `results/` and `logs/`. Integration evidence: [`jev_gibbs.py`](https://github.com/eumemic/jev-gibbs/blob/347ba11eb35e22590ccdc161c36f19fb27361414/jev_gibbs.py).

## Get started

From the upstream README (not run on the review host):

```sh
export TYPESAFE_API_KEY=...
python3 jev_gibbs.py zeroshot
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Result tables and per-experiment write-ups in the README.
- Paper: [arxiv.org/abs/2606.19264](https://arxiv.org/abs/2606.19264)

## Limits and data handling

Benchmark text goes to TypeSafe on your key. The RunPod comparison creates and deletes a paid GPU pod.

## Review and maintenance

Reviewed **2026-10-17** (Europe/Sofia) at [commit 347ba11eb35e](https://github.com/eumemic/jev-gibbs/tree/347ba11eb35e22590ccdc161c36f19fb27361414). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
