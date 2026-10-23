# jev-router (Claude Code model and effort suggestions by Jev)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Claude Code mod that adds a Route with Jev button: before you send a draft, Jev scores it and a card suggests which Claude model and effort level fit, with notes when a safety rule or low confidence changed the pick. It never changes settings or sends anything.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/pbswimmer3/claude-jev-router) |
| Maintainer | [pbswimmer3](https://github.com/pbswimmer3). Independently curated. |
| Format | Claude Code plugin (TypeScript hooks) |
| Requirements | Claude Code; a key for a Jev-shaped decisions API (Merge Gateway by default, or TypeSafe direct). |
| License | [Apache-2.0](https://github.com/pbswimmer3/claude-jev-router/blob/9276123fb5b924e9f1aaf17c6db8c3d5f0faf1c7/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`hooks/jev.ts`](https://github.com/pbswimmer3/claude-jev-router/blob/9276123fb5b924e9f1aaf17c6db8c3d5f0faf1c7/hooks/jev.ts) at the pinned commit. |

## When to use

- Pick a cheaper model for simple drafts and a stronger one for hard or risky work.
- See why a suggestion was stepped up instead of trusting a silent router.
- Mismatch: suggestions only; you still set the model in the picker yourself.

## How it works

`hooks/jev.ts` sends the draft to a Jev-shaped decisions endpoint (default model `typesafe/jev-1.13`) and parses the model and effort answers; `hooks/route.ts` applies confidence and risk rules before showing the card. Integration evidence: [`hooks/jev.ts`](https://github.com/pbswimmer3/claude-jev-router/blob/9276123fb5b924e9f1aaf17c6db8c3d5f0faf1c7/hooks/jev.ts).

## Get started

From the upstream README (not run on the review host):

```sh
claude plugin marketplace add pbswimmer3/claude-jev-router
claude plugin install jev-router@claude-jev-router --scope user
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Card meanings and keys in the README: [github.com/pbswimmer3/claude-jev-router#readme](https://github.com/pbswimmer3/claude-jev-router#readme)

## Limits and data handling

Draft text is sent to the configured gateway or TypeSafe when you press the button. Separate project from the catalog's other claude-jev-router listing.

## Review and maintenance

Reviewed **2026-10-23** (Europe/Sofia) at [commit 9276123fb5b9](https://github.com/pbswimmer3/claude-jev-router/tree/9276123fb5b924e9f1aaf17c6db8c3d5f0faf1c7). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
