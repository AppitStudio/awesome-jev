# chinese-workflow-decision-bench

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Reusable Feishu-style workplace message classification benchmark: 64 frozen synthetic Chinese scenarios, Choice and four-Noul workflows, published Jev vs Laya results, and pluggable classifier adapters. Not affiliated with Feishu.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Adkid-Zephyr/chinese-workflow-decision-bench) |
| Maintainer | [Adkid-Zephyr](https://github.com/Adkid-Zephyr). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Python 3.11 benchmark harness (`bench.py`, `evaluate.py`, adapters, frozen `data/`). |
| Requirements | Python 3.11+ for recorded backends; stdlib-only adapter runner for plumbing checks. Live Jev runs need `TYPESAFE_API_KEY`. Laya path needs a local multilingual checkpoint. |
| License | [MIT](https://github.com/Adkid-Zephyr/chinese-workflow-decision-bench/blob/b694dc6dbcba12c5bcf8d51b60ec48ff6ab87d57/LICENSE). TypeSafe usage billed separately for live Jev. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Upstream results are AI-assisted synthetic diagnostics, not a general leaderboard or independent blind annotation. Offline unittest green here; live Jev/Laya not re-run. |

## When to use

Use it when comparing typed classifiers on Chinese workplace ownership/urgency/noise triage with frozen prompts and labels. Prefer [jev-sec-bench](jev-sec-bench.md) for prompt-injection/vulnerable-code security corpora, or [jev-agent-failure-benchmark](jev-agent-failure-benchmark.md) for Who&When-style agent traces.

## How it works

`bench.py --backend jev` posts frozen Choice / four-Noul System One requests to `https://api.typesafe.ai/v1/systemone` with model `jev-1.13.0`, validates answer schemas, and writes raw JSONL plus metadata (keys never saved). Quality uses the first repeat only (denominator 64); latency aggregates successful timed calls. Adapters can be evaluated offline via `evaluate.py` without labels leaking into requests.

## Get started

```sh
git clone https://github.com/Adkid-Zephyr/chinese-workflow-decision-bench.git
cd chinese-workflow-decision-bench
git checkout b694dc6dbcba12c5bcf8d51b60ec48ff6ab87d57
python3 -m unittest discover -s tests -v
python evaluate.py --adapter adapters.constant:create --kind baseline \
  --model-id constant-noise --output /tmp/constant-noise
# live Jev (charges): TYPESAFE_API_KEY=... python bench.py --backend jev --output results/my-jev
```

Do not rerun `freeze.py` or relabel v1 cases when reproducing published scores.

## Examples and demos

- Published scorecards and `results/v1/jev/` raw records (vendor-recorded).
- Constant baseline adapter for plumbing (expected 16/64).

## Limits and data handling

Cases are synthetic and AI-assisted; not private chat dumps. Cloud Jev latency includes network; local Laya is a different hardware path—upstream warns against same-hardware architecture claims. Live calls send message state to TypeSafe.

## Review and maintenance

Reviewed on **2026-09-21** at [commit b694dc6](https://github.com/Adkid-Zephyr/chinese-workflow-decision-bench/tree/b694dc6dbcba12c5bcf8d51b60ec48ff6ab87d57): MIT. AI-assisted source review of README/README.en.md, LICENSE, `bench.py` Jev client, adapters, and frozen data hashes. Offline `python3 -m unittest discover -s tests -v`: **12 passed**. No live TypeSafe or Laya runs.

Related: [jev-sec-bench](jev-sec-bench.md), [jev-agent-failure-benchmark](jev-agent-failure-benchmark.md), [jevals](jevals.md).
