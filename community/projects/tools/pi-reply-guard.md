# pi-reply-guard

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Pi extension that checks each agent reply against installed skills you choose: a classifier — Jev by default (`openrouter/typesafe/jev-1.13`) — returns the probability the reply adheres to each skill, and replies below your threshold are sent back for a rewrite (up to `maxRewrites`).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/amalavet/pi-reply-guard) |
| Maintainer | [amalavet](https://github.com/amalavet). Independently curated. |
| Format | Pi extension (`pi install npm:pi-reply-guard`) with a `/reply-guard` settings menu |
| Requirements | Pi; an OpenRouter key for the default Jev model (or another configured classifier). |
| License | [MIT](https://github.com/amalavet/pi-reply-guard/blob/c2ead37cd138609c0eb8f1c7998c503d477f5149/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Keep replies aligned with a style or policy skill without re-prompting by hand.
- Tune per-skill thresholds from the settings menu.
- Mismatch: each rewrite costs another main-model turn.

## How it works

[`extensions/jev.ts`](https://github.com/amalavet/pi-reply-guard/blob/c2ead37cd138609c0eb8f1c7998c503d477f5149/extensions/jev.ts) asks the classifier one adherence question per configured skill; settings live in `~/.pi/agent/reply-guard.json`.

## Get started

Install from npm or GitHub (README *Install*):

```sh
pi install npm:pi-reply-guard
# or: pi install git:github.com/amalavet/pi-reply-guard
# then run /reply-guard in Pi
```

One classifier call per reply × skill (billed by OpenRouter) plus any rewrite turns.

## Examples and demos

- npm package: [`pi-reply-guard`](https://www.npmjs.com/package/pi-reply-guard) (0.2.1).
- README demo video and *Configure*.

## Limits and data handling

Agent replies and skill text go to the classifier provider. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-08** (Europe/Sofia) at [commit c2ead37cd138](https://github.com/amalavet/pi-reply-guard/tree/c2ead37cd138609c0eb8f1c7998c503d477f5149). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
