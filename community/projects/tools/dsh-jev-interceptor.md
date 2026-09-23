# dsh-jev-interceptor

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

DeepSeek Harness plugin: TypeSafe Jev risk-classifies tool calls (fail-closed / shadow→enforce) and can score session-reference messages instead of FIFO drop.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/AskTheWay/dsh-jev-interceptor) |
| Maintainer | [AskTheWay](https://github.com/AskTheWay). Independently curated. Not an endorsement. |
| Format | DeepSeek Harness (dsh) plugin. |
| Requirements | Node ≥ 20.3; dsh profile; TypeSafe or OpenRouter provider config. |
| License | [MIT](https://github.com/AskTheWay/dsh-jev-interceptor/blob/aaceff2bf92955a09230a8780fa12aa12eba9788/LICENSE). Provider usage may incur charges. |
| Disclosure | AI-assisted catalog review. Source inspected (README, LICENSE). Live dsh/Jev **not** run. Distinct from [dsh-jev](dsh-jev.md) / decide / verify / prune / kit listings. |

## When to use

Use it when DeepSeek Harness tool approvals need millisecond typed risk judgments and optional semantic session-reference retention. Prefer [dsh-jev](dsh-jev.md) when you only need an agent-callable `jev_ask` tool.

## How it works

Pre-execute hooks ask Jev about risk/irreversibility/task-fit/injection; actions are deny / ask / next() (never bare allow). Optional `jev-session-reference` scores messages for drop order. Shadow mode records decisions without enforcing. Telemetry via `/jev-stats`.

## Get started

```sh
dsh plugin --profile <name> add dsh-jev-interceptor
# configure cordis.patch.yml: mode shadow then enforce; provider typesafe|openrouter
```

Pin: [commit aaceff2](https://github.com/AskTheWay/dsh-jev-interceptor/tree/aaceff2bf92955a09230a8780fa12aa12eba9788).

## Examples and demos

- README shadow-mode `/jev-stats` sample.
- Upstream claims 63 tests including adversarial cases (not re-run here).

## Limits and data handling

Tool argument previews and message digests go to the configured Jev provider. Failures degrade to stock dsh. Latency/cost figures in the README are upstream-reported, not re-measured here.

## Review and maintenance

Reviewed **2026-09-23** at [commit aaceff2](https://github.com/AskTheWay/dsh-jev-interceptor/tree/aaceff2bf92955a09230a8780fa12aa12eba9788) (MIT). AI-assisted source review. No live TypeSafe spend.

Related: [dsh-jev](dsh-jev.md), [dsh-jev-kit](dsh-jev-kit.md), [dsh-jev-verify](dsh-jev-verify.md).
