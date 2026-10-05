# Edward

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Supervisor for unattended coding agents (CI, overnight runs) that wraps any subprocess with deterministic rules and an optional advisory scorer; `EDWARD_SCORER_BACKEND=jev` batches all probes into one TypeSafe Jev call per check.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/VeridicalTech/Edward) |
| Product homepage | [pypi.org](https://pypi.org/project/edward-guard/) |
| Maintainer | [VeridicalTech](https://github.com/VeridicalTech). Independently curated. |
| Format | CLI supervisor/wrapper with audit log |
| Requirements | Python 3.11+ and `pipx install edward-guard`. Jev backend: `EDWARD_SCORER_BACKEND=jev` and `TYPESAFE_API_KEY`; other backends are a LAN scorer endpoint or an offline heuristic. |
| License | [MIT](https://github.com/VeridicalTech/Edward/blob/5e101e515003c1063768f9bbdc92e8304bf68e44/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Supervise unattended agents in CI or scheduled batches and stop silent failure loops before they burn budget.
- Swap the judgment backend between a local model and Jev without changing the rule layer.
- Mismatch: interactive sessions where a human watches every step get less from it.

## How it works

Deterministic code owns everything irreversible (blocklists, write scopes, budget caps). With the `jev` backend, one call receives the cross-turn state (error trends, write streaks, budget) and returns calibrated judgments on whether to continue, pause or escalate; Jev's confidence gates routing, never actions, and a circuit breaker falls back to rules ([`edward/backends.py`](https://github.com/VeridicalTech/Edward/blob/5e101e515003c1063768f9bbdc92e8304bf68e44/edward/backends.py)).

## Get started

Install, run the offline demo, then wrap an agent with the Jev backend (live Jev calls):

```sh
pipx install edward-guard
edward demo --live-scorer --offline   # no GPU, no API key
export EDWARD_SCORER_BACKEND=jev TYPESAFE_API_KEY=...
edward wrap -- pi "fix the flaky test"
```

Live commands contact TypeSafe (or the configured provider) and may incur charges.

## Examples and demos

- README StepShield holdout table (maintainer-reported): Jev 1.13 backend recall 59.3%, clean FPR 10.2%, EIR₃ 0.91, vs a local 4B scorer at 58.3% / 17.6% / 0.78 and the paper's GPT-4.1-mini judge at 95.4% recall; see `BENCHMARK.md` upstream. Not reproduced here.
- `edward demo` runs six failure scenarios against the frozen rule set offline.

## Limits and data handling

The scorer is advisory; agent event state goes to TypeSafe with the Jev backend and is billed. Benchmarks are maintainer-reported. A team cloud console is listed as planned on the roadmap; not evaluated.

## Review and maintenance

Reviewed **2026-10-05** (Europe/Sofia) at [commit 5e101e515003](https://github.com/VeridicalTech/Edward/tree/5e101e515003c1063768f9bbdc92e8304bf68e44). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
