# layagrep (pipeline to train the open Laya model on jevgrep's code-relevance questions, using Jev as a teacher)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Training pipeline aimed at running jevgrep locally: it records every question jevgrep sends to Jev (and Jev's answer) on SWE-bench Verified tasks, gives each question only the code it is about, labels questions from the fix and test diffs, mixes 0.7 x the SWE-bench label with 0.3 x Jev's probability, and fine-tunes the open Laya System 1 model. Laya serves the same `/v1/systemone` protocol, so a good checkpoint could replace hosted Jev with no key. Only a small smoke run is reported so far.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/gak4u/layagrep) |
| Maintainer | [gak4u](https://github.com/gak4u). Independently curated. |
| Format | Python + TypeScript training pipeline |
| Requirements | Python venv with vendored Laya; Bun for the vendored jevgrep; a TypeSafe key for the recording step (about 0.1 to 2.6M input tokens per task per the README); Apple Silicon or a GPU for training. |
| License | [Apache-2.0](https://github.com/gak4u/layagrep/blob/bdbac773cbaa35c7b032ed02174f8a79d47670a4/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`harness/record.ts`](https://github.com/gak4u/layagrep/blob/bdbac773cbaa35c7b032ed02174f8a79d47670a4/harness/record.ts) at the pinned commit. |

## When to use

- Distil a hosted decision model's judgments for one tool into an open model you can run locally.
- Mismatch: research in progress; no trained checkpoint is published yet.

## How it works

`record.ts` runs jevgrep's real search with a custom `fetch` that saves each request to Jev with its answer, without modifying jevgrep; `pipeline/to_laya.py` builds the training mix and `pipeline/evaluate.py` reports AUC and agreement with Jev. Integration evidence: [`harness/record.ts`](https://github.com/gak4u/layagrep/blob/bdbac773cbaa35c7b032ed02174f8a79d47670a4/harness/record.ts).

## Get started

From the upstream README (not run on the review host):

```sh
git clone --recurse-submodules https://github.com/gak4u/layagrep
cd layagrep
(cd vendor/jevgrep && bun install --frozen-lockfile && bun scripts/parser-assets.mjs)
python -m venv .venv
.venv/bin/pip install -e vendor/laya -r requirements.txt
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Pipeline overview: [github.com/gak4u/layagrep/blob/bdbac773cbaa35c7b032ed02174f8a79d47670a4/README.md#how-it-works](https://github.com/gak4u/layagrep/blob/bdbac773cbaa35c7b032ed02174f8a79d47670a4/README.md#how-it-works)

## Limits and data handling

Recording sends repository code from SWE-bench tasks to TypeSafe and can cost many tokens. Results so far are a 6-task smoke run. Not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-10-30** (Europe/Sofia) at [commit bdbac773cbaa](https://github.com/gak4u/layagrep/tree/bdbac773cbaa35c7b032ed02174f8a79d47670a4). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
