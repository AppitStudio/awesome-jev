# jevernetes

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Live Kubernetes log analysis in a terminal or localhost dashboard: surface events worth investigating, inspect surrounding context, and copy investigation prompts for coding agents—with optional TypeSafe Jev judgments or offline keyword rules.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/sunil-sadasivan/jevernetes) |
| Maintainer | [sunil-sadasivan](https://github.com/sunil-sadasivan). Independently curated; this page is not an upstream submission or endorsement. |
| Format | Python package (`python3 -m jevernetes`) with CLI, local dashboard (port **8792**), and read-only kubectl collection. |
| Requirements | Python ≥ 3.11; `kubectl` with permission to list pods and read logs. No mandatory Python runtime deps. Live Jev analysis needs `TYPESAFE_API_KEY`; `--offline` uses local keyword rules. |
| License | [Apache-2.0](https://github.com/sunil-sadasivan/jevernetes/blob/b0be7ebbf5d2215f8dd5930ad3984ebe06026fac/LICENSE). TypeSafe usage has separate costs. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Offline pytest mostly green (**82 passed**, **1 failed** on review host—see Review). Live cluster tail and live Jev not run. |

## When to use

Use it when operators need a read-only live tail that highlights important/needs-review events and can hand evidence to an agent. Prefer [Jev Logs](jevlogs.md) for OpenTelemetry scoring pipelines, or pure kubectl/observability stacks when you do not want Jev.

## How it works

[`jevernetes/jev.py`](https://github.com/sunil-sadasivan/jevernetes/blob/b0be7ebbf5d2215f8dd5930ad3984ebe06026fac/jevernetes/jev.py) posts redacted log text to `https://api.typesafe.ai/v1/systemone` (default model `jev-latest`) when not in offline mode. Collection uses existing kubeconfig and is described as read-only. The dashboard supports live tail, context fetch, copy-investigation-prompt, and acknowledge/expected review rules stored locally under `.runs/`. Cost budgets (`--max-cost`, `--max-batches`) are estimates and can be exceeded by in-flight work.

## Get started

```sh
git clone https://github.com/sunil-sadasivan/jevernetes.git
cd jevernetes
kubectl config current-context
# Offline first (no API key):
python3 -m jevernetes k8s -f --tail 0 --offline
# Dashboard:
python3 -m jevernetes dashboard
# Optional live Jev:
# export TYPESAFE_API_KEY=...
# python3 -m jevernetes k8s -f --tail 100 --max-cost 0.25
```

Pinned review checkout:

```sh
git checkout b0be7ebbf5d2215f8dd5930ad3984ebe06026fac
pip install -r requirements-dev.txt
pytest -q
```

## Examples and demos

- [`examples/mixed.log`](https://github.com/sunil-sadasivan/jevernetes/blob/b0be7ebbf5d2215f8dd5930ad3984ebe06026fac/examples/mixed.log) with `python3 -m jevernetes files examples/mixed.log --offline`.
- Upstream GIFs under [`docs/images/`](https://github.com/sunil-sadasivan/jevernetes/tree/b0be7ebbf5d2215f8dd5930ad3984ebe06026fac/docs/images) (not re-recorded here).
- This listing: pytest **82 passed**, **1 failed** (`tests/test_context_reviews.py::ReviewTests::test_rules_survive_reload_and_skip_live_ai_queue`). No live kubectl cluster or TypeSafe call.

## Limits and data handling

Jev mode sends redacted logs and source metadata to TypeSafe—redaction is best effort; use `--offline` when logs must stay local. Dashboard binds to localhost. Keep kubeconfigs, keys, logs, and reports out of git. Inspired by a log-sentinel experiment in `dabit3/jev-experiments` (separate licensing).

## Review and maintenance

Reviewed on **2026-09-21** at [commit b0be7eb](https://github.com/sunil-sadasivan/jevernetes/tree/b0be7ebbf5d2215f8dd5930ad3984ebe06026fac): Apache-2.0; AI-assisted source review of README, LICENSE, `jevernetes/jev.py`, CLI/dashboard modules; pytest as above. No live TypeSafe or cluster session.

Related: [Jev Logs](jevlogs.md), [demo-expanso-jev](demo-expanso-jev.md), [jevmetrics](jevmetrics.md).
