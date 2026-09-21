# jev-sec-bench

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Blind security benchmarks for TypeSafe Jev (prompt-injection and vulnerable-code detection) built on jev-go, with a terminal dashboard over saved results.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Gaurav-Gosain/jev-sec-bench) |
| Maintainer | [Gaurav-Gosain](https://github.com/Gaurav-Gosain). Independently curated; this page is not an upstream submission or endorsement. |
| Format | Go CLI (`cmd/jev-sec-bench`, `cmd/jev-tui`) plus recorded `results/` JSON; depends on [jev-go](https://github.com/Gaurav-Gosain/jev-go). |
| Requirements | Go (module declares **1.27.1**); `TYPESAFE_API_KEY` to re-run benchmarks. Results JSON can be inspected offline. |
| License | [MIT](https://github.com/Gaurav-Gosain/jev-sec-bench/blob/fdb16b94d37535db9bad77f8ef0faa971bd7d69a/LICENSE). TypeSafe usage and Hugging Face corpora have separate terms/costs. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Offline Go package tests passed; live benchmark re-run against TypeSafe was **not** performed. Upstream accuracy/F1 figures are author-reported for a dated `jev-1.13.0` run—not catalog-remeasured. |

## When to use

Use it to study how Jev scores public prompt-injection and vulnerability-pair corpora, or to browse the included result files in the TUI. Prefer [is-malicious](is-malicious.md) or [jev-guard](jev-guard.md) for operational coding-agent scanning rather than offline corpora evaluation.

## How it works

Benchmark runners (via jev-go) send each sample as structured state to TypeSafe System One and record typed judgments. Metrics helpers and the Bubble Tea TUI read `results/`. Re-running downloads/uses public datasets and posts sample text to TypeSafe.

## Get started

```sh
export TYPESAFE_API_KEY=...
git clone https://github.com/Gaurav-Gosain/jev-sec-bench.git
cd jev-sec-bench
git checkout fdb16b94d37535db9bad77f8ef0faa971bd7d69a
go run ./cmd/jev-tui          # browse checked-in results offline
# go run ./cmd/jev-sec-bench -bench all   # live re-run (charges)
```

Pinned offline package tests:

```sh
go test ./...
```

## Examples and demos

- Checked-in `results/` (injection/code JSON) and README tables for a **2026-09-16** run on `jev-1.13.0`.
- Offline `go test ./...` on the review host: `internal/audit`, `internal/metrics`, and `internal/tui` **ok** (other packages have no test files). No live TypeSafe benchmark re-run.

## Limits and data handling

Live runs send corpus messages/code to TypeSafe and can be expensive at full scale. Treat README accuracy/ECE numbers as upstream snapshots for a specific model revision. Dataset licenses/terms apply separately.

## Review and maintenance

Reviewed on **2026-09-21** at [commit fdb16b9](https://github.com/Gaurav-Gosain/jev-sec-bench/tree/fdb16b94d37535db9bad77f8ef0faa971bd7d69a): MIT. AI-assisted source review of README, LICENSE, Go layout, and `results/`. **`go test ./...`**: audit/metrics/tui ok. No live TypeSafe re-benchmark.

Related: [is-malicious](is-malicious.md), [jev-guard](jev-guard.md), [Responsible AI Harness](responsible-ai-harness.md).
