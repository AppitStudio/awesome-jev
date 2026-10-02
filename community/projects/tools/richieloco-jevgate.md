# JevGate (RichieLoco)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Pure-MQL5 MetaTrader 5 module that vetoes EA trades using TypeSafe Jev calibrated judgments (≠ Claude Code jevgate).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/RichieLoco/JevGate) |
| Maintainer | [RichieLoco](https://github.com/RichieLoco). Independently curated. |
| Format | MQL5 · MetaTrader 5 include (MIT) |
| Requirements | See upstream README; TypeSafe or local decision backends as documented. |
| License | [`MIT`](https://github.com/RichieLoco/JevGate/blob/d0a7b1697a0628756eca6a3ccee74e463cecf4c1/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement.  Live install/inference not run on the review host. |

## When to use

Use when the workflow matches the upstream README. Prefer other catalog entries when you need a different stack or a hosted-only product.

## How it works

Pure-MQL5 MetaTrader 5 module that vetoes EA trades using TypeSafe Jev calibrated judgments (≠ Claude Code jevgate). Jev (or a disclosed local/open System One substitute) supplies typed judgments where configured; ordinary application code owns orchestration, I/O, and side effects. See upstream for schemas and failure handling.

## Get started

```sh
git clone https://github.com/RichieLoco/JevGate.git
cd JevGate
git checkout d0a7b1697a0628756eca6a3ccee74e463cecf4c1
# follow upstream README for install/run
```

## Examples and demos

- Upstream README and any linked demos/benchmarks.
- Jev evidence: MQL5/Include/JevGate/JevGate.mqh + example EA call TypeSafe Jev. ([upstream evidence](https://github.com/RichieLoco/JevGate/blob/d0a7b1697a0628756eca6a3ccee74e463cecf4c1/MQL5/Include/JevGate/JevGate.mqh)).

## Limits and data handling

Live Jev may send task text to TypeSafe or another provider and may incur charges. Catalog checks did not execute install or live inference on the review host.

## Review and maintenance

Reviewed **2026-10-03** (Europe/Sofia) at [commit d0a7b1697a06](https://github.com/RichieLoco/JevGate/tree/d0a7b1697a0628756eca6a3ccee74e463cecf4c1). AI-assisted README and license inspection; install/live paths not executed.
