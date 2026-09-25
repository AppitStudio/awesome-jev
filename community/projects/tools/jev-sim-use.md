# jev-sim-use

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

Fast iOS Simulator / Android navigator on top of sim-use: TypeSafe Jev picks the next on-screen action each step instead of a full agent turn per tap.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Ryu0118/jev-sim-use) |
| Maintainer | [Ryu0118](https://github.com/Ryu0118). Independently curated. |
| Format | CLI installer wrapping sim-use + Jev decision loop (Swift toolchain upstream). |
| Requirements | macOS 15+; sim-use 0.14.0+ (`brew install lycorp-jp/tap/sim-use`); TypeSafe API key; iOS Simulator or Android device. |
| License | [MIT](https://github.com/Ryu0118/jev-sim-use/blob/09fba40b1c9966f5c3e58186f9a84a6e5e30b992/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live provider paths were not exercised on the review host. |

## When to use

Use to **drive mobile UI goals** (“Turn on Dark Mode”) with one Jev call per step, handing back to the agent only when stuck.

## How it works

Reads visible labels/values, asks Jev whether the goal is reached and which action is next, and only types values you pass with `-t name=value`.

## Get started

```sh
brew tap lycorp-jp/tap && brew install lycorp-jp/tap/sim-use
curl -fsSL https://raw.githubusercontent.com/Ryu0118/jev-sim-use/main/install.sh | bash
# pin reviewed tip when building from source:
# git clone https://github.com/Ryu0118/jev-sim-use.git && cd jev-sim-use && git checkout 09fba40b1c9966f5c3e58186f9a84a6e5e30b992
```

## Examples and demos

- README feature list and install variants (`VERSION=`, `FORCE=1`).

## Limits and data handling

Screen labels and values are sent to TypeSafe each step. Requires Apple Silicon/macOS simulator stack; Android path depends on sim-use support.

## Review and maintenance

Reviewed **2026-09-25** (Europe/Sofia) at [commit 09fba40](https://github.com/Ryu0118/jev-sim-use/tree/09fba40b1c9966f5c3e58186f9a84a6e5e30b992). AI-assisted README and LICENSE inspection; live TypeSafe/provider integration paths not run.

Related: [CUA-JEV (ZJU-REAL)](cua-jev-zju.md), [typesafe-computer-use](typesafe-computer-use.md).
