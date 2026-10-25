# Toru (recording infrastructure for coding agents, with optional Jev browser navigation)

[All projects](../README.md) · [Web apps](README.md#web-apps)

MCP recorder that lets Claude Code, Cursor, Codex and other agents record product demos, changelog GIFs and bug repros in your signed-in Chrome or on your Mac, renders them with your brand and checks each take; optional server-side Jev navigation picks browser operations and targets for a goal.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/alifoo/toru) |
| Tags | `Open source` · `Commercial` · `Freemium` · `BYOK` |
| Product homepage | [Product homepage](https://toru.tools) |
| Pricing and access | Hosted: Free (10 credits a month), Creator $19/month and Studio $49/month per [toru.tools/pricing](https://toru.tools/pricing); checkout after beta admission. Self-host under MIT. Checked 2026-10-25. |
| Jev evidence | [`apps/mcp/src/jev.ts`](https://github.com/alifoo/toru/blob/95c885a30eda5ee6e716626f6b632fef2c9e61e7/apps/mcp/src/jev.ts) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Commercial: the hosted service has paid plans; the source is MIT licensed. |
| Maintainer | [alifoo](https://github.com/alifoo). Independently curated. |
| Format | Hosted service and self-hostable MCP server (TypeScript) |
| Platform and availability | Hosted at toru.tools (limited public beta) with Toru for Chrome and Toru for Mac; source on GitHub. |
| Jev's role | Optional: with a TypeSafe key, Jev answers the operation and target questions for server-side navigation; manual MCP browser controls work without it, and Toru adds no model of its own otherwise. |
| Requirements | An MCP-capable agent; a toru.tools account, or a self-hosted instance; a TypeSafe key only for Jev navigation. |
| License | [MIT](https://github.com/alifoo/toru/blob/95c885a30eda5ee6e716626f6b632fef2c9e61e7/LICENSE) |

## When to use

- Have your coding agent record a launch clip or bug repro without screen-recording by hand.
- Let Jev drive routine browser steps cheaply within a per-session spend cap.
- Mismatch: hosted beta needs admission for paid plans; self-hosting runs the whole stack yourself.

## How it works

`apps/mcp/src/jev.ts` sends the operation and a target for each possible operation in one request to `https://api.typesafe.ai/v1/systemone` (pinned `jev-1.13.0`); `JEV_MAX_USD` (0.25 by default) caps estimated spend per browser session. Integration evidence: [`apps/mcp/src/jev.ts`](https://github.com/alifoo/toru/blob/95c885a30eda5ee6e716626f6b632fef2c9e61e7/apps/mcp/src/jev.ts).

## Get started

From the upstream README (not run on the review host):

```sh
# Hosted: connect https://toru.tools as a remote MCP server in your agent
# Self-host: see the README and set TYPESAFE_API_KEY for optional Jev navigation
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Docs: [toru.tools/docs](https://toru.tools/docs)
- Pricing: [toru.tools/pricing](https://toru.tools/pricing)
- README: [github.com/alifoo/toru#readme](https://github.com/alifoo/toru#readme)

## Limits and data handling

With Jev navigation on, page controls and the goal go to TypeSafe. Recordings run in your signed-in browser or Mac; passwords do not reach the agent or Toru per the README.

## Review and maintenance

Reviewed **2026-10-25** (Europe/Sofia) at [commit 95c885a30eda](https://github.com/alifoo/toru/tree/95c885a30eda5ee6e716626f6b632fef2c9e61e7). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
