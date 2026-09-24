# macos-computer-use-kit

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

Accessibility-first macOS computer-use kit (stdio MCP, CLI, pi package, DeepSeek Harness plugin): agents act on `#ref` AX targets with background input and verification; optional TypeSafe Jev semantic guards judge targets/inputs before irreversible actions.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Sur-Cai/macos-computer-use-kit) |
| Maintainer | [Sur-Cai](https://github.com/Sur-Cai). Independently curated. |
| Format | Python PyPI package + npm pi/DSH adapters. |
| Requirements | macOS 12+; Python; Accessibility permissions; optional TypeSafe key when enabling Jev guards. |
| License | [MIT](https://github.com/Sur-Cai/macos-computer-use-kit/blob/97f8c52a3ae0968ee5f1af8248be8359b3a5e9a8/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live macOS automation not run on the Linux review host. Jev is optional. |

## When to use

Use for **AX-ref** macOS control with verified actions. Prefer [typesafe-computer-use](typesafe-computer-use.md) / [jev-macos-loop](jev-macos-loop.md) for other native macOS Jev loops.

## How it works

Snapshots return stable `#ref` elements; clicks/keys post to the target process without moving the user cursor; results separate `action_sent` from `verified`. Optional Jev guards add calibrated semantic checks before risky steps (decisions stay in code).

## Get started

```sh
pip install macos-computer-use-kit
# or
git clone https://github.com/Sur-Cai/macos-computer-use-kit.git
cd macos-computer-use-kit
git checkout 97f8c52a3ae0968ee5f1af8248be8359b3a5e9a8
# follow README for MCP client config; enable Jev guards only if desired
```

## Examples and demos

- PyPI / pi / DSH package badges and CI workflow.
- README bilingual EN/ZH.

## Limits and data handling

Requires Accessibility permission. UI text may reach Jev when guards are on. Linux review host could not exercise macOS AX.

## Review and maintenance

Reviewed **2026-09-24** (Europe/Sofia) at [commit 97f8c52](https://github.com/Sur-Cai/macos-computer-use-kit/tree/97f8c52a3ae0968ee5f1af8248be8359b3a5e9a8). AI-assisted README and source inspection; live provider calls not run on the review host.

Related: [typesafe-computer-use](typesafe-computer-use.md), [jev-macos-loop](jev-macos-loop.md), [agent-desktop](agent-desktop.md).
