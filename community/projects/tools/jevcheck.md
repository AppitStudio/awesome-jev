# jevcheck

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Semantic linting: deterministic AST/text selection finds candidates, Jev answers one bounded yes/no question, then policy decides shadow vs owned enforcement—via `@mhingston5/jev-cli` provider selection.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/mhingston/jevcheck) |
| Maintainer | [mhingston](https://github.com/mhingston). Independently curated. |
| Format | Node.js CLI (`@mhingston5/jevcheck`) |
| Requirements | Node.js 20+; optional provider credentials for live semantic checks (`inspect` works without a key). |
| License | [MIT](https://github.com/mhingston/jevcheck/blob/c0cfd51ad811a0adb2ae9f5e9749b2cb024218ef/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/cli.ts`](https://github.com/mhingston/jevcheck/blob/c0cfd51ad811a0adb2ae9f5e9749b2cb024218ef/src/cli.ts) at the pinned commit. |

## When to use

- Turn repeated code-review judgments into testable semantic lint rules.
- Need inspect-without-key previews before enabling live Jev checks.
- Mismatch: rules are only as good as the invariants you encode.

## How it works

Deterministic selectors build a bounded request; `@mhingston5/jev-cli` selects a Jev-capable provider for the yes/no; policy maps answers to advisory or blocking outcomes. `inspect` shows the exact request without calling a model. Integration evidence: [`src/cli.ts`](https://github.com/mhingston/jevcheck/blob/c0cfd51ad811a0adb2ae9f5e9749b2cb024218ef/src/cli.ts).

## Get started

npm install --save-dev @mhingston5/jevcheck and add a `jevcheck.config.json`, or clone and run the queue-ack walkthrough.

```sh
git clone https://github.com/mhingston/jevcheck && cd jevcheck
npm ci && npm run build
node dist/cli.js inspect examples/queue-ack/src/handler.ts --config examples/queue-ack/jevcheck.config.json --verbose
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- examples/queue-ack walkthrough
- docs/concepts.md rule-authoring guidance

## Limits and data handling

Evidence path is README/`jev-cli` integration rather than an in-tree TypeSafe URL string. Live checks send candidate snippets to the configured provider.

## Review and maintenance

Reviewed **2026-10-18** (Europe/Sofia) at [commit c0cfd51ad811](https://github.com/mhingston/jevcheck/tree/c0cfd51ad811a0adb2ae9f5e9749b2cb024218ef). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
