# jev-qualiscope-action (turn a Qualiscope signal into an explicit human-reviewed action level with Jev)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

CLI/action that maps a Qualiscope quality signal into an explicit action level using TypeSafe Jev (`jev-1.13.0`), so humans still review what to do next instead of auto-merging on a score.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/gbesse/jev-qualiscope-action) |
| Maintainer | [gbesse](https://github.com/gbesse). Independently curated. |
| Format | Node.js CLI / GitHub Action-friendly tool (MIT) |
| Requirements | Node.js and `TYPESAFE_API_KEY`. |
| License | [MIT](https://github.com/gbesse/jev-qualiscope-action/blob/c43ef6b6035a4a0c6c770a30cd79b3718fc202a5/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jev.mjs`](https://github.com/gbesse/jev-qualiscope-action/blob/c43ef6b6035a4a0c6c770a30cd79b3718fc202a5/src/jev.mjs) at the pinned commit. |

## When to use

- Convert Qualiscope signals into reviewable action levels.
- Keep humans in the loop on merge/release decisions.
- Mismatch: Qualiscope-specific input shape.

## How it works

`src/jev.mjs` creates a Jev client pinned to `jev-1.13.0` against `https://api.typesafe.ai/v1/systemone` using `TYPESAFE_API_KEY`. Integration evidence: [`src/jev.mjs`](https://github.com/gbesse/jev-qualiscope-action/blob/c43ef6b6035a4a0c6c770a30cd79b3718fc202a5/src/jev.mjs).

## Get started

From the upstream README (not run on the review host):

```sh
export TYPESAFE_API_KEY=...
node bin/jev-qualiscope-action.mjs --help
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/gbesse/jev-qualiscope-action/blob/c43ef6b6035a4a0c6c770a30cd79b3718fc202a5/README.md](https://github.com/gbesse/jev-qualiscope-action/blob/c43ef6b6035a4a0c6c770a30cd79b3718fc202a5/README.md)

## Limits and data handling

Qualiscope payloads are sent to TypeSafe on your key. Outputs are advisory action levels.

## Review and maintenance

Reviewed **2026-11-06** (Europe/Sofia) at [commit c43ef6b6035a](https://github.com/gbesse/jev-qualiscope-action/tree/c43ef6b6035a4a0c6c770a30cd79b3718fc202a5). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
