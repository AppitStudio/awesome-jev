# Jev × LexGLUE (reproducible zero-shot benchmark of Jev on all seven LexGLUE legal tasks)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Benchmark that freezes the official LexGLUE evaluation sets, sends each example to Jev as typed choice or per-label yes/no questions through OpenRouter, checkpoints every request and reports micro/macro-F1, usage and cost. The README compares Jev 1.13 with a frontier chat model, open System One models and a fine-tuned BERT baseline on the full 23,607-example test split.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/chepyle/jev-test) |
| Maintainer | [chepyle](https://github.com/chepyle). Independently curated. |
| Format | Python benchmark (uv CLI `jev-bench`) |
| Requirements | Python with uv; an OpenRouter key for live runs (Modal for the self-served baselines). |
| License | [Apache-2.0](https://github.com/chepyle/jev-test/blob/3b793ad446096b834d0cbe31184b775594cdc240/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jev_test/client.py`](https://github.com/chepyle/jev-test/blob/3b793ad446096b834d0cbe31184b775594cdc240/src/jev_test/client.py) at the pinned commit. |

## When to use

- Check how Jev does on legal text classification against other approaches.
- Mismatch: author-reported numbers; live reruns cost money.

## How it works

`src/jev_test/client.py` calls OpenRouter's `/api/v1/systemone` endpoint; single-label tasks become one choice question and multi-label tasks one noul question per label, with no chat completions or text parsing. Integration evidence: [`src/jev_test/client.py`](https://github.com/chepyle/jev-test/blob/3b793ad446096b834d0cbe31184b775594cdc240/src/jev_test/client.py).

## Get started

From the upstream README (not run on the review host):

```sh
uv sync --locked
uv run jev-bench prepare --tasks all --limit 10 --output data/quick
uv run jev-bench run --data data/quick --output results/preview --dry-run
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Results table in the README: [github.com/chepyle/jev-test#results](https://github.com/chepyle/jev-test#results)

## Limits and data handling

Benchmark examples are public LexGLUE data sent to OpenRouter. Figures are the author's. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-02** (Europe/Sofia) at [commit 3b793ad44609](https://github.com/chepyle/jev-test/tree/3b793ad446096b834d0cbe31184b775594cdc240). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
