# jev4j

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Java 17+ library (Maven Central) for TypeSafe/OpenRouter Jev: noul/choice/score in ordinary `if`/`switch`, multi-question records, Spring Boot 4 starter, and offline fixtures.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/maxsumrall/jev4j) |
| Maintainer | [maxsumrall](https://github.com/maxsumrall). Independently curated. Not an endorsement. |
| Format | Java library **jev4j-core 0.1.0** (+ Spring starter). |
| Requirements | Java 17+; TypeSafe or OpenRouter API key for live calls. |
| License | [MIT](https://github.com/maxsumrall/jev4j/blob/98bdb5269e146d02038ad4a87b22efc772b6705d/LICENSE). Provider usage may incur charges. |
| Disclosure | AI-assisted catalog review. Source inspected (README, LICENSE). Live Jev **not** run. Early API may change per README. |

## When to use

Use it when Java application code should branch on typed Jev answers with enum-mapped choices and acceptance thresholds. Prefer [jev4k](jev4k.md) / [Klassify](klassify.md) for Kotlin.

## How it works

`JevEvaluator` evaluates questions against text or structured state; helpers expose `test`/`evaluate` and multi-question mapping into records. Offline `question.answer(...)` fixtures support tests without network.

## Get started

Add Maven Central `io.github.maxsumrall.jev4j:jev4j-core:0.1.0` (see upstream README). Pin review source at [commit 98bdb52](https://github.com/maxsumrall/jev4j/tree/98bdb5269e146d02038ad4a87b22efc772b6705d).

## Examples and demos

- README Java snippets for refund/team/mood examples.
- CI and OpenRouter component workflows (not re-run here).

## Limits and data handling

Each live evaluation is a provider request. Apply thresholds before acting. Early-development API warning applies.

## Review and maintenance

Reviewed **2026-09-23** at [commit 98bdb52](https://github.com/maxsumrall/jev4j/tree/98bdb5269e146d02038ad4a87b22efc772b6705d) (MIT, 0.1.0). AI-assisted source review. No live TypeSafe spend.

Related: [jev4k](jev4k.md), [go-jev](go-jev.md), [jevapi](https://github.com/JawzoD3TH/JevApi).
