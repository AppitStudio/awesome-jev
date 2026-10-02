# jev-decision-kit (kdcadmin)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Local skill/plugin cabinet: an on-device Jev head selects which skills to preface before the chat model speaks.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/kdcadmin/jev-decision-kit) |
| Maintainer | [kdcadmin](https://github.com/kdcadmin). Independently curated. |
| Format | Python · local skill/plugin selector (MIT) |
| Requirements | See upstream README; TypeSafe or local decision backends as documented. |
| License | [`MIT`](https://github.com/kdcadmin/jev-decision-kit/blob/62a1b0b81ec9199bead06e3609678ba9fb11b614/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Local Jev head; disclose not TypeSafe-hosted. Live install/inference not run on the review host. |

## When to use

Use when the workflow matches the upstream README. Prefer other catalog entries when you need a different stack or a hosted-only product.

## How it works

Local skill/plugin cabinet: an on-device Jev head selects which skills to preface before the chat model speaks. Jev (or a disclosed local/open System One substitute) supplies typed judgments where configured; ordinary application code owns orchestration, I/O, and side effects. See upstream for schemas and failure handling.

## Get started

```sh
git clone https://github.com/kdcadmin/jev-decision-kit.git
cd jev-decision-kit
git checkout 62a1b0b81ec9199bead06e3609678ba9fb11b614
# follow upstream README for install/run
```

## Examples and demos

- Upstream README and any linked demos/benchmarks.
- Jev evidence: README + `models/jev/head.json` / `host/jev.py` local decision scoring; not TypeSafe-hosted. ([upstream evidence](https://github.com/kdcadmin/jev-decision-kit/blob/62a1b0b81ec9199bead06e3609678ba9fb11b614/host/jev.py)).

## Limits and data handling

Live Jev may send task text to TypeSafe or another provider and may incur charges. Catalog checks did not execute install or live inference on the review host.

## Review and maintenance

Reviewed **2026-10-03** (Europe/Sofia) at [commit 62a1b0b81ec9](https://github.com/kdcadmin/jev-decision-kit/tree/62a1b0b81ec9199bead06e3609678ba9fb11b614). AI-assisted README and license inspection; install/live paths not executed.
