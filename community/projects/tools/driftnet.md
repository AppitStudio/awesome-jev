# driftnet (drop links in chat and get them sorted, explained and searchable, with Jev as the judge)

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

Self-hosted link catcher: drop links into LINE, Slack, Discord or Telegram, send them with a Chrome button, or hand them to an agent; driftnet follows each one to the actual tool or repo, writes a short explanation in your language and puts it on a searchable page that agents can also read over MCP. Jev judges each item's category, kind, worth and whether it looks like prompt injection.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/KevinChu1110/driftnet) |
| Maintainer | [KevinChu1110](https://github.com/KevinChu1110). Independently curated. |
| Format | TypeScript service with web page, chat bots, Chrome extension and MCP server |
| Requirements | Node.js and pnpm; any LLM (or none); a TypeSafe API key enables the Jev judge. |
| License | [MIT](https://github.com/KevinChu1110/driftnet/blob/6917e18204a30f21595f3a755563c3e25ba581fd/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`packages/core/src/judge/jev.ts`](https://github.com/KevinChu1110/driftnet/blob/6917e18204a30f21595f3a755563c3e25ba581fd/packages/core/src/judge/jev.ts) at the pinned commit. |

## When to use

- Turn a pile of saved AI-tool links into a browsable, explained catalogue.
- Mismatch: below a 0.4 confidence the LLM classifies instead of Jev.

## How it works

`packages/core/src/judge/jev.ts` posts each digested link to `https://api.typesafe.ai/v1/systemone` (`jev-latest`, override with `TYPESAFE_ENDPOINT`); any failure falls back to the LLM. Integration evidence: [`packages/core/src/judge/jev.ts`](https://github.com/KevinChu1110/driftnet/blob/6917e18204a30f21595f3a755563c3e25ba581fd/packages/core/src/judge/jev.ts).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/KevinChu1110/driftnet && cd driftnet
pnpm install
pnpm start   # http://localhost:8787
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/KevinChu1110/driftnet#readme](https://github.com/KevinChu1110/driftnet#readme)

## Limits and data handling

Link digests go to TypeSafe when the judge is on (`DRIFTNET_JUDGE=off` disables it). The catalogue stays on your computer.

## Review and maintenance

Reviewed **2026-10-28** (Europe/Sofia) at [commit 6917e18204a3](https://github.com/KevinChu1110/driftnet/tree/6917e18204a30f21595f3a755563c3e25ba581fd). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
