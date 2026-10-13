# pi-magic8ball

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Advisory choice tool for the Pi coding agent: a neutral context builder collects state and TypeSafe Jev (or Cloudflare Clef) returns a choice distribution.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/neruok/pi-magic8ball) |
| Maintainer | [neruok](https://github.com/neruok). Independently curated. |
| Format | Pi extension (npm) |
| Requirements | Node.js 24+; Pi; TypeSafe or Cloudflare credentials. |
| License | [MIT](https://github.com/neruok/pi-magic8ball/blob/11102adf9d2617798e60928ebb531de1d99e0e1e/LICENSE) |
| Jev evidence | [`magic8ball.ts`](https://github.com/neruok/pi-magic8ball/blob/11102adf9d2617798e60928ebb531de1d99e0e1e/magic8ball.ts) at the pinned commit. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |

## When to use

- Get a probability-weighted second opinion between options inside a Pi session.
- Mismatch: advisory only; confidence measures concentration, not correctness.

## How it works

Private tools gather neutral state with a fixed schema; the extension sends options to the configured decision provider and reports the distribution. (Summarized from the upstream [README](https://github.com/neruok/pi-magic8ball/blob/11102adf9d2617798e60928ebb531de1d99e0e1e/README.md); not reproduced here.)

## Get started

From the upstream README (not run on the review host): install the package in Pi per the README and configure a Jev or Clef provider.

## Limits and data handling

Collected context goes to the configured provider and may incur charges. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-13** (Europe/Sofia) at [commit 11102adf9d26](https://github.com/neruok/pi-magic8ball/tree/11102adf9d2617798e60928ebb531de1d99e0e1e). Inspected the upstream README, LICENSE (where present), and the Jev integration evidence linked above; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
