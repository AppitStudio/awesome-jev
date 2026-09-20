# jev-pii-checker

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

CLI that scans text and files for PII with TypeSafe Jev presence/sensitivity judgments plus regex and segmentation layers, emitting JSON or tables and severity-aware exit codes.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/coo-quack/jev-pii-checker) |
| Maintainer | [coo-quack](https://github.com/coo-quack). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | TypeScript/Bun CLI **@coo-quack/jev-pii-checker 0.3.1** (npm / `bunx`). |
| Requirements | Node.js 20+ or Bun; live scans need `TYPESAFE_API_KEY`. |
| License | [MIT](https://github.com/coo-quack/jev-pii-checker/blob/84e1ba4a933851f5aa61e36879f36c40ba5e44bb/LICENSE). |

## When to use

Use it to gate text you were already sending to a model or pipeline for PII categories and sensitivity before export. Prefer a local-only guard when data must not leave the host ([sensitive-canary](https://github.com/coo-quack/sensitive-canary) is upstream’s pointer). Do not treat detections as legal compliance certifications.

## How it works

[`src/judge.ts`](https://github.com/coo-quack/jev-pii-checker/blob/84e1ba4a933851f5aa61e36879f36c40ba5e44bb/src/judge.ts) wraps `@typesafe-ai/sdk` `TypeSafeClient.systemOne` with Choice/Noul/Score questions. Gate, regex, and segmentation stages in `src/gate.ts` / `src/locate.ts` assemble spans; CLI exit codes reflect severity thresholds.

## Get started

```sh
bunx @coo-quack/jev-pii-checker --version
export TYPESAFE_API_KEY=…
echo 'Contact: k.sato@example.co.jp' | bunx @coo-quack/jev-pii-checker --json
```

Scanned text is sent to TypeSafe and can incur charges. This listing did not run live scans.

## Examples and demos

- [Documentation site](https://coo-quack.github.io/jev-pii-checker/) (getting started, categories, limitations).
- Offline unit tests under `tests/`; integration tests gated by `JEV_PII_INTEGRATION=1`.

## Limits and data handling

**All scanned content leaves the machine for TypeSafe** (see upstream SECURITY.md). Default output masks values; `--show-values` reveals them. Upstream measured accuracy claims were not reproduced here.

## Review and maintenance

Reviewed on **2026-09-20** at [commit 84e1ba4a](https://github.com/coo-quack/jev-pii-checker/tree/84e1ba4a933851f5aa61e36879f36c40ba5e44bb): **0.3.1**, MIT. AI-assisted source review of README, `judge.ts`, gate/locate modules, license, and docs. Bun tests and live TypeSafe calls were not executed on the review host.

Related: [SemDecide](semdecide.md), [toolgate](toolgate.md), [jev-prompt-sentry](jev-prompt-sentry.md).
