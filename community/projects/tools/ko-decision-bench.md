# ko-decision-bench

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Reproducible Korean benchmark for Jev and System One-style decision models: same questions, prompts and metrics across 7 KLUE, KoBEST, KorNLI and UnSmile tasks, with accuracy, Brier, ECE and latency, and a `/v1/systemone` adapter.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/phykn/ko-decision-bench) |
| Maintainer | [phykn](https://github.com/phykn). Independently curated. |
| Format | Python benchmark |
| Requirements | Python; local model runtimes or a `/v1/systemone` endpoint (such as TypeSafe) to test. |
| License | [Apache-2.0](https://github.com/phykn/ko-decision-bench/blob/c8b80fd824b985e2f6d9204baf7605211073848f/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/kodb/adapters.py`](https://github.com/phykn/ko-decision-bench/blob/c8b80fd824b985e2f6d9204baf7605211073848f/src/kodb/adapters.py) at the pinned commit. |

## When to use

- Compare decision models on Korean tasks with one method.
- Check calibration, not only accuracy.
- Mismatch: published table covers open models; run it yourself for hosted Jev numbers.

## How it works

Each task is asked as typed questions with fixed prompts and splits, and each model returns a probability per option. `src/kodb/adapters.py` includes an HTTP adapter that posts to `{url}/v1/systemone`, so Jev and compatible servers run through the same harness. Results flag possible training-data overlap. Integration evidence: [`src/kodb/adapters.py`](https://github.com/phykn/ko-decision-bench/blob/c8b80fd824b985e2f6d9204baf7605211073848f/src/kodb/adapters.py).

## Get started

From the upstream README: install, pick an adapter, run the tasks, and read the generated tables.

```sh
git clone https://github.com/phykn/ko-decision-bench && cd ko-decision-bench
# see README for adapters and run commands
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README results table (8 models, 7 tasks)
- README.ko.md

## Limits and data handling

Benchmark texts go to the endpoint you test. Overlap markers mean some scores may be inflated.

## Review and maintenance

Reviewed **2026-10-19** (Europe/Sofia) at [commit c8b80fd824b9](https://github.com/phykn/ko-decision-bench/tree/c8b80fd824b985e2f6d9204baf7605211073848f). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
