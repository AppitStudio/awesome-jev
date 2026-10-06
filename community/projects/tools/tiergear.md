# tiergear

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Claude Code plugin and CLI where a decision model judge — TypeSafe Jev by default, or local Laya/Kev — picks a tier (trivial → max) for each typed prompt and maps it to a model and reasoning effort, with floors, ceilings and cache-aware switching.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/jang2162/tiergear) |
| Maintainer | [jang2162](https://github.com/jang2162). Independently curated. |
| Format | Claude Code plugin (marketplace) + optional CLI (npm `tiergear`, 0.1.0 at review) |
| Requirements | Claude Code 2.1.289+; `TYPESAFE_API_KEY` for the default Jev judge (or a local Laya/Kev server); Node 20+ for the CLI. |
| License | [MIT](https://github.com/jang2162/tiergear/blob/b69cc20d548b9c939c2795a792451e2ab8c58b98/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Auto-route Claude Code prompts to a model/effort tier with a status band to override or turn routing off.
- Launch Orca workers or sessions with `--min-tier` / `--max-tier` bounds.
- Mismatch: model or effort changes invalidate the prompt cache; the judge adds latency to each judged prompt.

## How it works

Hooks send only user-typed prompts to the judge ([`src/core/judges/systemone.ts`](https://github.com/jang2162/tiergear/blob/b69cc20d548b9c939c2795a792451e2ab8c58b98/src/core/judges/systemone.ts)), which returns a tier; tables map it to model and effort. Raising needs confidence 0.5, lowering 0.85 on two consecutive turns; manual `/model` or `/effort` pauses routing; a slow or failed judge leaves the turn untouched.

## Get started

Inside a Claude Code session:

```sh
/plugin marketplace add jang2162/tiergear
/plugin install tiergear@tiergear
# set TYPESAFE_API_KEY for the default jev judge, then start a new session
```

Each judged prompt is a Jev request billed by TypeSafe; Claude usage is billed as usual.

## Examples and demos

- README status band, tier tables and *Which prompts are judged* sections.
- `tiergear stats` / `tiergear status` CLI for routing history.

## Limits and data handling

With the Jev judge, prompts (start/end if long), recent exchanges truncated to 400–1500 characters and session counters are sent to TypeSafe (upstream *Data sent to the judge*); Laya/Kev stay local. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-07** (Europe/Sofia) at [commit b69cc20d548b](https://github.com/jang2162/tiergear/tree/b69cc20d548b9c939c2795a792451e2ab8c58b98). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
