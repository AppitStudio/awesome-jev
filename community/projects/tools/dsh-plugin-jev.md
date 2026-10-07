# dsh-plugin-jev

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

DeepSeek Harness (DSH) Web GUI plugin that gives the model a `jev_ask` tool for calibrated TypeSafe Jev judgments, exposes the same call to sibling plugins as a host service, adds an optional Jev command guard before tool execution, and shows per-chat usage in the browser.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/cyberofficial/dsh-plugin-jev) |
| Maintainer | [cyberofficial](https://github.com/cyberofficial). Independently curated. |
| Format | DSH plugin bundle installed with `dsh plugin --profile web install` |
| Requirements | DeepSeek Harness (web profile), pnpm, a TypeSafe API key entered in Settings → Plugins → Jev (TypeSafe). |
| License | README states MIT, but the reviewed tree has **no LICENSE file** — listed as Source available until a license file is added. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Give a DSH agent a tool for calibrated yes/no, choice and score judgments instead of guessing.
- Let other DSH plugins reuse Jev through `ctx.get('jev')` without a main-model round trip.
- Mismatch: the command guard is probabilistic — upstream warns it can block safe commands and allow dangerous ones.

## How it works

[`lib/tool.js`](https://github.com/cyberofficial/dsh-plugin-jev/blob/5ad07a705f21ead72bfd2b7a424c08c276d29fd3/lib/tool.js) registers `jev_ask` on the DSH tool plane with a system-prompt guidance section; [`lib/service.js`](https://github.com/cyberofficial/dsh-plugin-jev/blob/5ad07a705f21ead72bfd2b7a424c08c276d29fd3/lib/service.js) exposes the validated call to sibling plugins; [`lib/guard.js`](https://github.com/cyberofficial/dsh-plugin-jev/blob/5ad07a705f21ead72bfd2b7a424c08c276d29fd3/lib/guard.js) is a `tools/pre-execute` listener for the optional command guard; [`lib/usage.js`](https://github.com/cyberofficial/dsh-plugin-jev/blob/5ad07a705f21ead72bfd2b7a424c08c276d29fd3/lib/usage.js) tracks per-chat cost. Docs: [`docs/`](https://github.com/cyberofficial/dsh-plugin-jev/tree/5ad07a705f21ead72bfd2b7a424c08c276d29fd3/docs).

## Get started

Install into DSH (from the README):

```sh
git clone https://github.com/cyberofficial/dsh-plugin-jev.git
cd dsh-plugin-jev
dsh plugin --profile web install "link:$PWD"   # pnpm must be on PATH
```

Each `jev_ask` call or guarded command is a Jev request billed to your TypeSafe key.

## Examples and demos

- Tool reference: [`docs/03-jev-ask-tool.md`](https://github.com/cyberofficial/dsh-plugin-jev/blob/5ad07a705f21ead72bfd2b7a424c08c276d29fd3/docs/03-jev-ask-tool.md); command guard: [`docs/06-command-guard.md`](https://github.com/cyberofficial/dsh-plugin-jev/blob/5ad07a705f21ead72bfd2b7a424c08c276d29fd3/docs/06-command-guard.md).
- README *Usage and cost* and *Behavior and limits*.

## Limits and data handling

Questions and state chosen by the model go to TypeSafe. No LICENSE file despite the README's MIT statement. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-07** (Europe/Sofia) at [commit 5ad07a705f21](https://github.com/cyberofficial/dsh-plugin-jev/tree/5ad07a705f21ead72bfd2b7a424c08c276d29fd3). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
