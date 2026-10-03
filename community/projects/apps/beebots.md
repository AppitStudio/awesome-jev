# beebots

[All projects](../README.md) · [Web apps](README.md#web-apps)

Three AI trading bees on OKX perpetual futures race on paper by default: TypeSafe Jev makes every trade decision; plain code owns the risk layer and orders. OpenAI is used only to design bee personas and portraits.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/imikerussell/beebots) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/imikerussell/beebots#readme) |
| Pricing and access | Free source build; no app purchase fee verified. TypeSafe and OpenAI usage billed separately; optional third-party VPS hosting may charge. Checked 2026-10-03. Not financial advice. |
| Jev evidence | [Upstream README](https://github.com/imikerussell/beebots/blob/6d3fe0d4f72dd25676c2f5caac0b83dff05031fb/README.md) states every decision comes from Jev and requires a key from console.typesafe.ai/keys; OpenAI is for bee design/portraits only. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Not financial advice; paper trading by default. Catalog listing links the GitHub source only (no affiliate deploy links). Live install/UI paths not run on the Linux review host. |
| Maintainer | [imikerussell](https://github.com/imikerussell). Independently curated. |
| Format | Docker Compose dashboard + paper-trading engine (MIT) |
| Platform and availability | Self-hosted Docker dashboard (paper trading by default) |
| Jev's role | Jev decides every trade action for each bee; application code executes risk checks and simulated or exchange orders. OpenAI is not used for trade decisions. |
| Requirements | Docker Compose; TYPESAFE/Jev API key; OpenAI key for bee design; optional OKX credentials only if leaving paper mode. |
| License | [MIT](https://github.com/imikerussell/beebots/blob/6d3fe0d4f72dd25676c2f5caac0b83dff05031fb/LICENSE). Provider usage may incur charges when live. |

## When to use

Use when the workflow matches the upstream README. Prefer other catalog apps when you need a different platform or a hosted-only product.

## How it works

Three AI trading bees on OKX perpetual futures race on paper by default: TypeSafe Jev makes every trade decision; plain code owns the risk layer and orders. OpenAI is used only to design bee personas and portraits. Jev supplies typed judgments where configured; application code owns orchestration and side effects.

## Get started

```sh
git clone https://github.com/imikerussell/beebots.git
cd beebots
git checkout 6d3fe0d4f72dd25676c2f5caac0b83dff05031fb
# follow upstream README for install/run
```

## Examples and demos

- Upstream README and any linked demos/screenshots.

## Limits and data handling

Live Jev may send task text to TypeSafe and may incur charges. Catalog checks did not execute install or live inference on the review host.

## Review and maintenance

Reviewed **2026-10-03** (Europe/Sofia) at [commit 6d3fe0d4f72d](https://github.com/imikerussell/beebots/tree/6d3fe0d4f72dd25676c2f5caac0b83dff05031fb). AI-assisted README and license inspection; live paths not executed.
