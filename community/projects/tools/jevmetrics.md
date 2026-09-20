# jevmetrics

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Experimental OpenTelemetry Collector metrics processor that asks TypeSafe Jev whether unfamiliar metric instruments are worth retaining, then applies deterministic keep/reduce policy from cached assessments.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ishantanu/jevmetrics) |
| Maintainer | [ishantanu](https://github.com/ishantanu) (Shantanu Deshpande). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Go OpenTelemetry Collector processor (`jevmetrics` / `otelprocessor`) with example Collector configs; version **0.1.0-dev** (alpha). |
| Requirements | Go **1.23+** (README also notes 1.26+ for some build paths); OpenTelemetry Collector Builder; `TYPESAFE_API_KEY` (or configured API key) for live inference. Offline unit tests use mocked HTTP. |
| License | [Apache-2.0](https://github.com/ishantanu/jevmetrics/blob/ca8d73aaa3985071a9859a1b51f338f359cb9730/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source and offline Go tests inspected; live TypeSafe inference and full Collector deployments were not run. |

## When to use

Use it when new services dump unclassified metrics into a Collector pipeline and you want semantic assessment of instrument metadata (name, description, unit, attributes) before primary storage. Prefer ordinary OTel filter processors when you already have explicit keep/drop rules. Prefer [Jev Logs](jevlogs.md) for log triage rather than metrics retention.

## How it works

For unprotected metrics without a fresh cache entry, the processor summarizes metadata, keeps the current batch, and queues an asynchronous `POST https://api.typesafe.ai/v1/systemone` call (default model `jev-latest`) with four questions (`relevance`, `redundancy`, `keep` noul; `action` choice). Validated answers are cached; subsequent batches apply annotate or reduce policy from the keep-score without another call. Explicit protection rules override inference. See [`otelprocessor/jev.go`](https://github.com/ishantanu/jevmetrics/blob/ca8d73aaa3985071a9859a1b51f338f359cb9730/otelprocessor/jev.go) and [`internal/evaluator/jev.go`](https://github.com/ishantanu/jevmetrics/blob/ca8d73aaa3985071a9859a1b51f338f359cb9730/internal/evaluator/jev.go).

## Get started

```sh
git clone https://github.com/ishantanu/jevmetrics.git
cd jevmetrics
git checkout ca8d73aaa3985071a9859a1b51f338f359cb9730
# unit tests (no live key):
go test ./internal/...
(cd otelprocessor && go test ./...)
```

Build and run a custom Collector with the processor via the repository Makefile / `BUILD_NOTES.md` and `examples/otelcol/config.yaml`. Live inference sends metric metadata to TypeSafe and can incur charges; this listing did not run a live Collector against TypeSafe.

## Examples and demos

- README architecture and question table.
- `examples/otelcol/config.yaml` sample Collector config.
- Offline Go tests under `internal/evaluator` and `otelprocessor` (mocked `/v1/systemone`).

## Limits and data handling

Status is **alpha**. Filtering effectiveness and cost savings need evaluation on your telemetry. Metric metadata and attribute keys leave the host when inference runs. Cached assessments can stale; protection rules and thresholds remain operator-owned. Upstream retention/cost claims were not independently measured.

## Review and maintenance

Reviewed on **2026-09-20** at [commit ca8d73a](https://github.com/ishantanu/jevmetrics/tree/ca8d73aaa3985071a9859a1b51f338f359cb9730): **0.1.0-dev**, Apache-2.0. AI-assisted source review of README, LICENSE, evaluator/processor Jev clients, and config examples. Ran `go test ./internal/...` and `go test` in `otelprocessor/` (pass). No live TypeSafe calls.

Related: [Jev Logs](jevlogs.md), [typesafe-cli](typesafe-cli.md).
