# jev-sigma-bench by nwang783 (preliminary test of Jev against 1,732 Sigma rules on Windows event logs)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Experiment on whether Jev can stand in for Sigma rules when spotting attacks in Windows event logs: 426 attack events from SigmaHQ regression data and 33,354 benign events from a clean lab baseline, with label-revealing lab artifacts removed. Jev was asked three kinds of yes/no question: generic (is this malicious?), described (does it show the behaviour in this rule's title and description?) and filter (Sigma fired; is it real?). With no rule it found about as many unseen attacks as the rest of the rule set at the same false-positive rate; given a rule's two-sentence description it caught the matching attack for 89% of 405 rules at 0.5% benign firing; as an alert filter it was weak. 36,934 requests cost $0.98.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/nwang783/jev-sigma-bench) |
| Maintainer | [nwang783](https://github.com/nwang783). Independently curated. |
| Format | Python research code with results and charts (MIT) |
| Requirements | Python with uv, the setup script's public datasets, and an OpenRouter key for `typesafe/jev-1.14`. |
| License | [MIT](https://github.com/nwang783/jev-sigma-bench/blob/d4c53b31a797a37725ef571d735d5df98225d1a6/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`bench/jev.py`](https://github.com/nwang783/jev-sigma-bench/blob/d4c53b31a797a37725ef571d735d5df98225d1a6/bench/jev.py) at the pinned commit. |

## When to use

- See how a plain-language Jev question compares with Sigma rules for Windows attack detection.
- Mismatch: production detection; the author calls it preliminary and the false-positive rates lower bounds.

## How it works

`bench/jev.py` posts the yes/no questions to OpenRouter's decisions endpoint with `typesafe/jev-1.14` (overridable with `JEV_MODEL`), caches answers and enforces a cost limit. Integration evidence: [`bench/jev.py`](https://github.com/nwang783/jev-sigma-bench/blob/d4c53b31a797a37725ef571d735d5df98225d1a6/bench/jev.py).

## Get started

Fetch the data, then run the Sigma and Jev arms and the summary.

```sh
git clone https://github.com/nwang783/jev-sigma-bench && cd jev-sigma-bench
./setup.sh && uv venv && uv pip install pyyaml evtx httpx matplotlib
uv run python -m bench.build_baseline && uv run python -m bench.sigma_arm
uv run python -m bench.jev_arm && uv run python -m bench.summary
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/nwang783/jev-sigma-bench/blob/d4c53b31a797a37725ef571d735d5df98225d1a6/README.md](https://github.com/nwang783/jev-sigma-bench/blob/d4c53b31a797a37725ef571d735d5df98225d1a6/README.md)

## Limits and data handling

Event data goes to OpenRouter/TypeSafe on your key. Benign data is from clean lab machines and the rewritten commands were never executed, per the author's caveats.

## Review and maintenance

Reviewed **2026-11-17** (Europe/Sofia) at [commit d4c53b31a797](https://github.com/nwang783/jev-sigma-bench/tree/d4c53b31a797a37725ef571d735d5df98225d1a6). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
