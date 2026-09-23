# CUA-JEV (ZJU-REAL)

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

Open reference framework for Jev-powered computer use: task adapters propose legal actions; TypeSafe Jev chooses a concrete action and channel; code guards, executes, and verifies—distinct from [Cua jev-use](cua-jev-use.md) and [Jev Voice (CUA)](../apps/jev-cua.md).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ZJU-REAL/CUA-JEV) |
| Maintainer | [ZJU-REAL](https://github.com/ZJU-REAL). Independently curated. Not an endorsement. |
| Format | Python framework (`cua-jev`) + Windows-validated workflow examples + public webpage. |
| Requirements | TypeSafe key for live Jev; Windows for published desktop workflows (Edge/Excel/VS Code/Explorer). CI unit tests also cover Linux/macOS; desktop adapters for non-Windows are not validated. |
| License | [Apache-2.0](https://github.com/ZJU-REAL/CUA-JEV/blob/576d7db77baadaf0813e4cd263dd06669f0ed8e8/LICENSE). TypeSafe and optional planner models may incur charges. |
| Disclosure | AI-assisted catalog review. Source inspected (README, LICENSE, architecture). Live CUA/Jev **not** run. Timing tables are upstream pilots, not catalog benchmarks. |

## When to use

Use it when studying constrained computer-use loops where Jev picks among typed candidates across GUI and structured channels. Prefer [cua-jev-use](cua-jev-use.md) for the trycua Driver example, or [jev-cua](../apps/jev-cua.md) for the macOS voice Accessibility bar.

## How it works

Adapters observe state and enumerate `intent × channel` candidates; Jev `choice` selects an ID; `ActionGuard` checks freshness/scope before executors run; independent verifiers check resulting state. Hybrid vs GUI-only modes and open-task pilots are documented on the [project webpage](https://zjureal.com/CUA-JEV/).

## Get started

Clone [commit 576d7db](https://github.com/ZJU-REAL/CUA-JEV/tree/576d7db77baadaf0813e4cd263dd06669f0ed8e8) and follow upstream install/docs. Windows integrations (UI Automation, Excel COM) are required for the four published desktop workflows. Do not expect arbitrary-app generalization.

## Examples and demos

- [zjureal.com/CUA-JEV](https://zjureal.com/CUA-JEV/) videos and snapshot.json.
- Open-task twelve-decision browser→VS Code case study (upstream).

## Limits and data handling

Not a general agent: each workflow has task-specific adapters/verifiers. Screenshots/VLM paths are optional and not claimed for all demos. Application state and goals go to TypeSafe (and any planner gateway). No live spend here.

## Review and maintenance

Reviewed **2026-09-23** at [commit 576d7db](https://github.com/ZJU-REAL/CUA-JEV/tree/576d7db77baadaf0813e4cd263dd06669f0ed8e8) (Apache-2.0; GitHub SPDX may show NOASSERTION). AI-assisted source review. No live TypeSafe spend.

Related: [cua-jev-use](cua-jev-use.md), [typesafe-computer-use](typesafe-computer-use.md).
