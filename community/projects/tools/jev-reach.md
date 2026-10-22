# jev-reach (Jev walks the browser for chrome-devtools-mcp)

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

Drop-in chrome-devtools-mcp server with one extra `reach` tool: your agent states a goal once and Jev picks each click to walk the browser there, then the agent makes one devtools call on the same tab instead of one model turn per click.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/slothg/jev-reach) |
| Maintainer | [slothg](https://github.com/slothg). Independently curated. |
| Format | MCP server and Claude Code plugin (Node.js, npm `jev-reach`) |
| Requirements | Node 20.19+ or 22.12+; Chrome; a TypeSafe API key. |
| License | [MIT](https://github.com/slothg/jev-reach/blob/a301a87a5aa391e682e2e91465708f44062fe6fc/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jev.ts`](https://github.com/slothg/jev-reach/blob/a301a87a5aa391e682e2e91465708f44062fe6fc/src/jev.ts) at the pinned commit. |

## When to use

- Get past cookie banners, logins and menus before debugging a frontend bug.
- Cut context spent on page snapshots during navigation.
- Mismatch: replaces your chrome-devtools-mcp entry; running both gives two Chromes.

## How it works

For each step `reach` gives Jev a typed list of page elements and actions and `src/jev.ts` asks it to pick one (about 300 ms per step, `jev-latest` by default); the walk happens on the same page objects the stock devtools collectors listen to. Integration evidence: [`src/jev.ts`](https://github.com/slothg/jev-reach/blob/a301a87a5aa391e682e2e91465708f44062fe6fc/src/jev.ts).

## Get started

From the upstream README (not run on the review host):

```sh
claude mcp remove chrome-devtools
claude mcp add chrome-devtools -e TYPESAFE_API_KEY=your-key -- npx -y jev-reach --isolated
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Install options in the README: [github.com/slothg/jev-reach#readme](https://github.com/slothg/jev-reach#readme)

## Limits and data handling

Page element lists are sent to TypeSafe. The README's plugin marketplace path points at `rashedInt32/jev-reach`.

## Review and maintenance

Reviewed **2026-10-22** (Europe/Sofia) at [commit a301a87a5aa3](https://github.com/slothg/jev-reach/tree/a301a87a5aa391e682e2e91465708f44062fe6fc). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
