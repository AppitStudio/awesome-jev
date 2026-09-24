# jev-loop (King4s)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Decision-driven build loop: TypeSafe Jev decides; Claude Code or Hermes executes—as an MCP server plus skill. Distinct from lvzhaobo/jev-loop.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/King4s/jev-loop) |
| Maintainer | [King4s](https://github.com/King4s). Independently curated. |
| Format | Python MCP server + agent skill. |
| Requirements | Python; TypeSafe API key; Claude Code or Hermes. |
| License | [MIT](https://github.com/King4s/jev-loop/blob/10ca6fe7e4f0c88fa087ad04302760b660fc94fb/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live loop not run. Distinct from lvzhaobo/jev-loop. |

## When to use

Use when Jev should **own decisions** while a coding agent builds. Prefer [jev-macos-loop](jev-macos-loop.md) for native macOS GUI automation.

## How it works

MCP/skill surface asks Jev for typed decisions; Claude Code or Hermes performs the build steps (per README).

## Get started

```sh
git clone https://github.com/King4s/jev-loop.git
cd jev-loop
git checkout 10ca6fe7e4f0c88fa087ad04302760b660fc94fb
# install MCP/skill per README
```

## Examples and demos

- README MCP + skill overview.

## Limits and data handling

Task context reaches TypeSafe; agent tools may change the workspace—review decisions before destructive steps.

## Review and maintenance

Reviewed **2026-09-24** (Europe/Sofia) at [commit 10ca6fe](https://github.com/King4s/jev-loop/tree/10ca6fe7e4f0c88fa087ad04302760b660fc94fb). AI-assisted README inspection; live MCP not run.

Related: [jev-macos-loop](jev-macos-loop.md).
