# jev-suite

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Four Java decision-quality apps on one shared Jev kernel: Jev answers structured score/choice/noul questions over sanitized evidence; deterministic code owns thresholds, vetoes, and routing.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/klauswg/jev-suite) |
| Maintainer | [klauswg](https://github.com/klauswg). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Maven multi-module **jev-suite 0.1.0** (JDK 17+): shared `jev-kit` plus apps (`jev-proof`, `jev-fit` shipped; `jev-fidelity` / `jev-rental` planned). |
| Requirements | JDK 17+, Maven. Live calibration needs `TYPESAFE_API_KEY`. `jev-proof` additionally needs [yt-dlp](https://github.com/yt-dlp/yt-dlp). |
| License | [MIT](https://github.com/klauswg/jev-suite/blob/b3ea52d05da2e2961411a958c90b156997041a9e/LICENSE). TypeSafe usage billed separately. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Source inspected (README, LICENSE, app table). Maven build and live calibration were **not** executed on the review host. Upstream calibration counts were not re-run. |

## When to use

Use it when you want Java examples of “Jev judges, code decides” for acceptance/fit-style evidence gates with fail-closed behavior and injection sanitization. Prefer TypeScript/Python harnesses when you need npm/PyPI packaging instead of Maven.

## How it works

Shared `jev-kit` provides a typed TypeSafe HTTP client, `NoulGate` three-way pass/fail/review, and `ExternalStringSanitizer`. Apps feed sanitized evidence into Jev and keep routing matrices in unit-tested Java. Upstream states calibration runners hard-fail without an API key unless `--allow-mock` watermarks output.

## Get started

```sh
git clone https://github.com/klauswg/jev-suite.git
cd jev-suite
git checkout b3ea52d05da2e2961411a958c90b156997041a9e
mvn package
```

Pin for review: [commit b3ea52d](https://github.com/klauswg/jev-suite/tree/b3ea52d05da2e2961411a958c90b156997041a9e).

## Examples and demos

- `jev-proof` — sponsored video brief delivery checks.
- `jev-fit` — candidate-vs-requirements shortfalls.
- Planned: `jev-fidelity`, `jev-rental` (PRD only at review tip).

## Limits and data handling

Model unreachable → review/escalate, never auto-pass (per upstream design). Live Jev sends evidence text to TypeSafe. This listing did not build or call Jev.

## Review and maintenance

Reviewed on **2026-09-23** at [commit b3ea52d](https://github.com/klauswg/jev-suite/tree/b3ea52d05da2e2961411a958c90b156997041a9e) (**0.1.0**, MIT). AI-assisted review of README and LICENSE. No live TypeSafe spend.

Related: [agent-evals](agent-evals.md), [daf-jev](daf-jev.md), [DecideKit](decidekit.md).
