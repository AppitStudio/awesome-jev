# NEXUS (live command center inside Claude Code's terminal, with an optional observe-first Jev router)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Claude Code plugin that docks a dashboard beside the conversation showing the lead model, its subagents, advisor consultations, context and plan usage, and Jev's routing answers. Jev is optional and observe-only by default; after calibration it may retry a failed read or suggest a next file, only for read-only calls.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/muhzain05/Nexus) |
| Maintainer | [muhzain05](https://github.com/muhzain05). Independently curated. |
| Format | Claude Code plugin (TypeScript mod) |
| Requirements | Claude Code in fullscreen TUI; optional TypeSafe key (macOS Keychain or env). |
| License | [MIT](https://github.com/muhzain05/Nexus/blob/1983d623ff75b548c1eb1315a8b5913dfc2f2c29/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`mod/swarm-ui/hooks/jev.ts`](https://github.com/muhzain05/Nexus/blob/1983d623ff75b548c1eb1315a8b5913dfc2f2c29/mod/swarm-ui/hooks/jev.ts) at the pinned commit. |

## When to use

- See what Claude Code's subagents and advisor are doing as it happens.
- Mismatch: Jev covers only read-only Read/LSP calls.

## How it works

`mod/swarm-ui/hooks/jev.ts` is an observation-only client for `https://api.typesafe.ai/v1/systemone` (`jev-latest`) that asks choice questions about the lead's next step; only tool names, file basenames and error kinds are sent. Integration evidence: [`mod/swarm-ui/hooks/jev.ts`](https://github.com/muhzain05/Nexus/blob/1983d623ff75b548c1eb1315a8b5913dfc2f2c29/mod/swarm-ui/hooks/jev.ts).

## Get started

From the upstream README (not run on the review host):

```sh
claude plugin marketplace add muhzain05/Nexus
claude plugin install swarm-ui@claude-swarm --scope user
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Repository README: [github.com/muhzain05/Nexus#readme](https://github.com/muhzain05/Nexus#readme)

## Limits and data handling

With Jev on, tool names, file basenames and error kinds are sent to TypeSafe. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-02** (Europe/Sofia) at [commit 1983d623ff75](https://github.com/muhzain05/Nexus/tree/1983d623ff75b548c1eb1315a8b5913dfc2f2c29). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
