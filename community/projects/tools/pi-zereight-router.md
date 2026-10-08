# pi-zereight-router

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Jev-backed virtual model for Pi: each user message is classified by Jev (`openrouter/typesafe/jev-1.13`) as planning, research, codebase explore, review, implementation or other and routed to a fixed Cursor-provider model and effort, with a mid-turn handoff to the implementation model after the first file edit and a local phase decision log.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/zereight/pi-zereight-router) |
| Maintainer | [zereight](https://github.com/zereight). Independently curated. |
| Format | Pi extension (`pi install git:github.com/zereight/pi-zereight-router`) |
| Requirements | Pi with pi-cursor-sdk models in your catalog (`cursor/claude-sonnet-5-5@300k`, `cursor/claude-haiku-5-5@300k`, `cursor/grok-4.6`, `cursor/composer-2.5`) and `OPENROUTER_API_KEY` for Jev. |
| License | [MIT](https://github.com/zereight/pi-zereight-router/blob/1e416d7ea852ad0bb190ddbdf7459ee7930e6dbf/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Spend planning and review on the models suited to them automatically.
- Audit routing choices in the phase decision log.
- Mismatch: tied to the author's Cursor-provider model set; adapt the policy for others.

## How it works

[`extensions/cursor-router.ts`](https://github.com/zereight/pi-zereight-router/blob/1e416d7ea852ad0bb190ddbdf7459ee7930e6dbf/extensions/cursor-router.ts) asks Jev for the phase and applies [`route-policy.ts`](https://github.com/zereight/pi-zereight-router/blob/1e416d7ea852ad0bb190ddbdf7459ee7930e6dbf/extensions/route-policy.ts); retries stay on the same physical model and [`phase-decision-log.ts`](https://github.com/zereight/pi-zereight-router/blob/1e416d7ea852ad0bb190ddbdf7459ee7930e6dbf/extensions/phase-decision-log.ts) records each decision. If Jev fails, new messages default to planning.

## Get started

Install in Pi (README *Install*):

```sh
pi install git:github.com/zereight/pi-zereight-router
# or for one session: pi -e git:github.com/zereight/pi-zereight-router
```

One Jev classification per message (OpenRouter) plus the routed models' usage.

## Examples and demos

- README *Routing* table and *Cache measurement (routing)*.

## Limits and data handling

User messages go to OpenRouter for classification. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-08** (Europe/Sofia) at [commit 1e416d7ea852](https://github.com/zereight/pi-zereight-router/tree/1e416d7ea852ad0bb190ddbdf7459ee7930e6dbf). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
