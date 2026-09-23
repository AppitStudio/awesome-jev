# Juardrails

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Go guardrails management service for TypeSafe Jev: define Choice/Score/Noul policies in YAML or a UI, batch questions into one provider call, then apply explicit rules via REST/CLI—with namespaces, access control, and audit logging.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/abhaybhargav/juardrails) |
| Maintainer | [abhaybhargav](https://github.com/abhaybhargav). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Go server (`cmd/juardrails`) + CLI (`cmd/juard`) with embedded UI and docs site. |
| Requirements | Go **1.26+** (toolchain download supported). `TYPESAFE_API_KEY` for live evaluations. Bootstrap creates local admin credentials under `data/` and `~/.juardrails/`. |
| License | **Unspecified** — no repository root LICENSE / SPDX license metadata on the reviewed tip. Do not treat the source as a granted open-source license until upstream adds one. Docs: [abhaybhargav.github.io/juardrails](https://abhaybhargav.github.io/juardrails/). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Source inspected (README, `internal/guardrail/jev.go`, examples). Live server/Jev evaluations were **not** run on the review host. |

## When to use

Use it when you want a durable policy store and admin UI around Jev questions with audit trails, rather than one-off scripts. Prefer [daf-jev](daf-jev.md) for an embedded Python library, or agent-specific guards such as [jev-guard](jev-guard.md) / [opencode-jev-guard](opencode-jev-guard.md) for coding-agent preflight.

## How it works

Policies batch Jev questions; [`internal/guardrail/jev.go`](https://github.com/abhaybhargav/juardrails/blob/8c03b04efd32d3eb140adbacef9d44e0184db273/internal/guardrail/jev.go) talks to TypeSafe. The CLI can `apply` / `simulate` / `evaluate` YAML policies; simulation uses supplied answers locally and does not call Jev. Bootstrap provisions human and CLI service accounts with local credential files.

## Get started

```sh
git clone https://github.com/abhaybhargav/juardrails.git
cd juardrails
git checkout 8c03b04efd32d3eb140adbacef9d44e0184db273
go run ./cmd/juardrails bootstrap
go run ./cmd/juardrails
# Open http://127.0.0.1:8080
```

Pin for review: [commit 8c03b04](https://github.com/abhaybhargav/juardrails/tree/8c03b04efd32d3eb140adbacef9d44e0184db273). Live `evaluate` sends state to TypeSafe and may incur charges.

## Examples and demos

- `examples/support-safety.yaml` and simulation fixtures.
- Hosted docs: quickstart, CLI, Claude Code policy pack.

## Limits and data handling

License is unspecified at the reviewed tip—confirm redistribution rights before shipping binaries. Bootstrap credentials are written locally with restricted modes; treat them as secrets. Simulation is not a substitute for live model tests. No live TypeSafe spend in this listing.

## Review and maintenance

Reviewed on **2026-09-23** at [commit 8c03b04](https://github.com/abhaybhargav/juardrails/tree/8c03b04efd32d3eb140adbacef9d44e0184db273). AI-assisted source review. License gap recorded. No live Juardrails/Jev run.

Related: [daf-jev](daf-jev.md), [agent-chaperone](agent-chaperone.md), [opencode-jev-guard](opencode-jev-guard.md).
