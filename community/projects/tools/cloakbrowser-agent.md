# CloakBrowser-Agent

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

Stealth browser agent where TypeSafe Jev decides each step (~0.3 s) and CloakBrowser executes human-like actions (MCP, CLI, Python API)

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/CloakHQ/CloakBrowser-Agent) |
| Maintainer | [CloakHQ](https://github.com/CloakHQ). Independently curated. Related: [CloakBrowser](https://github.com/CloakHQ/CloakBrowser). |
| Format | Python · MCP server + CLI + library (MIT; see also LICENSE-jev-ultrafast note in tree). |
| Requirements | Python; TypeSafe API key; CloakBrowser runtime per upstream. |
| License | [MIT](https://github.com/CloakHQ/CloakBrowser-Agent/blob/2fa41ca83d2955e5bc8e3966830b5bf267973226/LICENSE). Provider/browser usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live browse/Jev not run on the review host. |

## When to use

Use when you want goal-driven browsing with Jev choosing clicks/fills and a stealth Chromium carrying them out.

## How it works

`browse(goal=…, url=…)` loops: observe → Jev decides action/target → CloakBrowser acts → markdown result. Available as MCP, CLI, or Python API.

## Get started

```sh
git clone https://github.com/CloakHQ/CloakBrowser-Agent.git
cd CloakBrowser-Agent
git checkout 2fa41ca83d2955e5bc8e3966830b5bf267973226
# follow upstream README for MCP/CLI install and keys
```

## Examples and demos

README trimmed Google Flights run with per-step Jev probabilities. No live browse on the review host.

## Limits and data handling

Page content and goals may be sent to TypeSafe when live. Stealth browsing has ethical/ToS implications — use responsibly.

## Review and maintenance

Reviewed **2026-09-29** (Europe/Sofia) at [commit 2fa41ca](https://github.com/CloakHQ/CloakBrowser-Agent/tree/2fa41ca83d2955e5bc8e3966830b5bf267973226). AI-assisted README + LICENSE inspection; live paths not executed.
