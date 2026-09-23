# jev-guard (klauswg)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Real-time risk triage gateway for exchange deposits/withdrawals: TypeSafe Jev answers risk/pattern/freeze questions; Java code owns hard rules, thresholds, and final actions. Distinct from [leepokai/jev-guard](jev-guard.md) and [CMaintz/jev-guard](cmaintz-jev-guard.md).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/klauswg/jev-guard) |
| Maintainer | [klauswg](https://github.com/klauswg). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Java 17+ Spring Boot demo service (`com.jevguard`) with mock and live TypeSafe clients. |
| Requirements | JDK 17+, Maven; optional `TYPESAFE_API_KEY` for live mode. Mock mode runs the full pipeline offline. |
| License | [MIT](https://github.com/klauswg/jev-guard/blob/067a17073f0a7fd5f5fc18508bf9aec49ce46ac2/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Source inspected (README, LICENSE, Java layout). Live TypeSafe calibration and Spring Boot run were **not** executed on the review host. Upstream n=100 calibration is synthetic/author-labeled—not a real AML detection rate. |

## When to use

Use it as a **reference architecture** for Jev-as-triage + deterministic adjudication on irreversible money flows. Prefer coding-agent [jev-guard](jev-guard.md) / [cmaintz-jev-guard](cmaintz-jev-guard.md) for tool-call firewalls—not this finance demo.

## How it works

FeatureBuilder digests a 24h window → HardRuleEngine may veto without a model call → StateRenderer builds sanitized English state → Jev answers risk_level / pattern / should_freeze / observation-only route → GateLogic composes AUTO_PASS / MANUAL_REVIEW / FREEZE. Failures degrade to manual review, never auto-pass. JSONL audit masks addresses.

## Get started

```sh
git clone https://github.com/klauswg/jev-guard.git
cd jev-guard
git checkout 067a17073f0a7fd5f5fc18508bf9aec49ce46ac2
mvn spring-boot:run
# second terminal: ./demo.sh   # mock fixtures, no API key
```

## Examples and demos

- `./demo.sh` / `demo.ps1` simulated events; `GET /v1/metrics`, `GET /v1/decisions`.
- `docs/calibration-report.md`, `eval/labeled-samples.jsonl` (author-reported).

## Limits and data handling

Demo binds localhost; blacklist is sample data, not a live sanctions feed; in-memory profiles reset on restart. Live mode sends transfer feature text to TypeSafe. Not production-ready without your auth and data sources. This listing did not call live Jev.

## Review and maintenance

Reviewed on **2026-09-23** at [commit 067a170](https://github.com/klauswg/jev-guard/tree/067a17073f0a7fd5f5fc18508bf9aec49ce46ac2) (MIT). AI-assisted source review of README, LICENSE, package layout. No live TypeSafe spend.

Related: [jev-guard](jev-guard.md), [cmaintz-jev-guard](cmaintz-jev-guard.md), [jev-java](jev-java.md).
