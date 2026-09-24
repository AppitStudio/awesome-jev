# ajevt-browser

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

Bounded Jev System One browser tool for Pi, OpenCode V2, Amp, and MCP: one `ajevt_browser` call runs observe → decide → validate → act using Vercel `agent-browser`, with strict probability/risk checks.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/XYenon/ajevt-browser) |
| Maintainer | [XYenon](https://github.com/XYenon). Independently curated. |
| Format | TypeScript monorepo / npm (`ajevt-browser`, `ajevt-browser-mcp`). |
| Requirements | Node; global `agent-browser` + browser install; TypeSafe (or configured) Jev endpoint/key. |
| License | [AGPL-3.0](https://github.com/XYenon/ajevt-browser/blob/a20a6f172a14b13507487c9534d35951267751b5/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live browser/Jev not run. |

## When to use

Use it when an agent host should drive pages with **finite Jev-chosen operations** rather than free-form plans. Prefer [Jev Ultrafast](jev-ultrafast.md) / [Footwork](footwork.md) for other browser stacks.

## How it works

Hosts share [`src/jev.ts`](https://github.com/XYenon/ajevt-browser/blob/a20a6f172a14b13507487c9534d35951267751b5/src/jev.ts) transport: snapshot candidates, one System One request per step, validate confidence/risk, then `agent-browser` commands with verifiers. Secrets are redacted from Jev requests.

## Get started

```sh
npm install -g agent-browser && agent-browser install
git clone https://github.com/XYenon/ajevt-browser.git
cd ajevt-browser
git checkout a20a6f172a14b13507487c9534d35951267751b5
# Pi: pi install npm:ajevt-browser
# OpenCode: add "ajevt-browser" plugin; MCP: ajevt-browser-mcp package
```

## Examples and demos

- npm packages and README host install matrix.
- `test/jev.test.ts` (not executed on this review host).

## Limits and data handling

Page observations and typed values (non-secret) leave the host for Jev. AGPL-3.0 obligations apply to network service distribution—read the license. Password fields are not retyped when already filled.

## Review and maintenance

Reviewed **2026-09-24** (Europe/Sofia) at [commit a20a6f1](https://github.com/XYenon/ajevt-browser/tree/a20a6f172a14b13507487c9534d35951267751b5). AI-assisted README + `src/jev.ts` inspection. No live browser/TypeSafe run.

Related: [Footwork](footwork.md), [pi-Jev-browser](pi-jev-browser.md), [Jev Ultrafast](jev-ultrafast.md).
