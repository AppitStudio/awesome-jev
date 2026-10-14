# OMP Jev Auto Mode

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Experimental Jev tool-call guard for Oh My Pi adapted from pi-jev-auto-mode, defaulting to ask on uncertainty and blocking escalations without a UI.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/suzuuuuu09/omp-jev-auto-mode) |
| Maintainer | [suzuuuuu09](https://github.com/suzuuuuu09). Independently curated. |
| Format | OMP extension (TypeScript) |
| Requirements | Oh My Pi, TypeSafe API key. |
| License | [MIT](https://github.com/suzuuuuu09/omp-jev-auto-mode/blob/313e5e994b739249a803061d275c01afe8c9a84c/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jev/transport.ts`](https://github.com/suzuuuuu09/omp-jev-auto-mode/blob/313e5e994b739249a803061d275c01afe8c9a84c/src/jev/transport.ts) at the pinned commit. |

## When to use

- Add a classification gate before OMP runs write or exec tool calls.
- Mismatch: experimental, not tested end-to-end; not a filesystem sandbox.

## How it works

Read-only operations take a fast path; others are judged by Jev, with `uncertain: ask`. Code protects `.omp`/`.herdr` paths and blocks `eval` while enabled. Integration evidence: [`src/jev/transport.ts`](https://github.com/suzuuuuu09/omp-jev-auto-mode/blob/313e5e994b739249a803061d275c01afe8c9a84c/src/jev/transport.ts).

## Get started

From the upstream README (not run on the review host):

```sh
bun install
bun run check
omp --no-extensions -e $(pwd)/index.ts   # isolated test session
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Config: `jev-auto-mode.json`.
- Tests: `test/`.

## Limits and data handling

Tool-call details go to TypeSafe.

## Review and maintenance

Reviewed **2026-10-14** (Europe/Sofia) at [commit 313e5e994b73](https://github.com/suzuuuuu09/omp-jev-auto-mode/tree/313e5e994b739249a803061d275c01afe8c9a84c). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
