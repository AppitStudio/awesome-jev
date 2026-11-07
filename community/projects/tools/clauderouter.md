# ClaudeRouter (Claude Code mod with optional TypeSafe Jev model-tier engine)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Claude Code mod that picks haiku/sonnet/opus and reasoning effort per request with a live status band; an optional Jev engine lets TypeSafe Jev choose the tier.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/visualife/ClaudeRouter) |
| Maintainer | [visualife](https://github.com/visualife). Independently curated. |
| Format | Claude Code hooks mod (TypeScript; no SPDX license file on the reviewed commit) |
| Requirements | Claude Code and, for the Jev engine, a TypeSafe API key. |
| License | NONE on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`hooks/jev.ts`](https://github.com/visualife/ClaudeRouter/blob/fdeabb59dfd0be055b3fde3f8d37a9f89bd114c6/hooks/jev.ts) at the pinned commit. |

## When to use

- Cut Claude Code cost by routing requests to the right tier.
- Compare heuristic vs Jev routing.
- Mismatch: Jev engine is optional; no OSI license on the reviewed commit.

## How it works

`hooks/jev.ts` posts to `https://api.typesafe.ai/v1/systemone` when `/clauderouter engine jev` is selected; default routing is local heuristics. Integration evidence: [`hooks/jev.ts`](https://github.com/visualife/ClaudeRouter/blob/fdeabb59dfd0be055b3fde3f8d37a9f89bd114c6/hooks/jev.ts).

## Get started

Install the hooks per README, then run `/clauderouter engine jev` with TYPESAFE_API_KEY set.

```sh
git clone https://github.com/visualife/ClaudeRouter.git && cd ClaudeRouter
export TYPESAFE_API_KEY=...
/clauderouter engine jev
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/visualife/ClaudeRouter/blob/fdeabb59dfd0be055b3fde3f8d37a9f89bd114c6/README.md](https://github.com/visualife/ClaudeRouter/blob/fdeabb59dfd0be055b3fde3f8d37a9f89bd114c6/README.md)

## Limits and data handling

Prompt summaries are sent to TypeSafe when the Jev engine is on.

## Review and maintenance

Reviewed **2026-11-08** (Europe/Sofia) at [commit fdeabb59dfd0](https://github.com/visualife/ClaudeRouter/tree/fdeabb59dfd0be055b3fde3f8d37a9f89bd114c6). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
