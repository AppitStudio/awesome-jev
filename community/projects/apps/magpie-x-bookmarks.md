# Magpie by Ian Poley (local archive of your X bookmarks and likes, sorted into topics with Jev and searchable by coding agents)

[All projects](../README.md) · [Web apps](README.md#web-apps)

Syncs your X bookmarks and likes to your machine every few hours, has Claude propose topic areas and Jev score each post against each topic, and serves a local web app for filtering, browsing linked repos and pages, and asking questions answered from your saved posts. A Claude skill lets coding agents search the archive.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ianpoley/magpie) |
| Tags | `Source available` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/ianpoley/magpie#readme) (source-built; no separate product site verified). |
| Pricing and access | Free source build run on your own macOS or Linux machine; a TypeSafe API key is required and Jev calls are billed to it; optional Claude Code calls count against your Claude plan. No license file, so reuse terms are not granted. Checked 2026-11-24. |
| Jev evidence | [`packages/engine/src/jev/tagger.ts`](https://github.com/ianpoley/magpie/blob/92dcd83f7dd59bcea50a9d2d45ae356abfe01f26/packages/engine/src/jev/tagger.ts) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Discovered via X ([post](https://x.com/ianpoley/status/2124951287934685217)). |
| Maintainer | [ianpoley](https://github.com/ianpoley). Independently curated. |
| Format | Bun / Node.js monorepo (Next.js web app, sync engine, Claude skill) |
| Platform and availability | Local web app on 127.0.0.1 with background services (LaunchAgents or systemd user units) on macOS or Linux. |
| Jev's role | Jev scores each saved post against each topic for tagging and helps select posts for Ask; Claude (optional) proposes the categories and writes Ask answers. |
| Requirements | macOS or Linux, git, Bun 1.3 and Node 26; an X account; a TypeSafe API key; Claude Code CLI optional. |
| License | No license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |

## When to use

- Turn a large pile of X bookmarks into a searchable, topic-sorted local archive.
- Mismatch: anyone unwilling to use X session cookies; see limits.

## How it works

`packages/engine/src/jev/` holds the client (official `TypeSafeClient` from the TypeSafe SDK), the tagging questions and the tagger; the web app's Ask flow in `apps/web/src/lib/ask.ts` also calls Jev. Integration evidence: [`packages/engine/src/jev/tagger.ts`](https://github.com/ianpoley/magpie/blob/92dcd83f7dd59bcea50a9d2d45ae356abfe01f26/packages/engine/src/jev/tagger.ts).

## Get started

Clone and run the interactive setup, which installs the services and asks for your X session and Jev key.

```sh
git clone https://github.com/ianpoley/magpie.git && cd magpie
bun run setup   # web app on http://127.0.0.1:3030
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/ianpoley/magpie/blob/92dcd83f7dd59bcea50a9d2d45ae356abfe01f26/README.md](https://github.com/ianpoley/magpie/blob/92dcd83f7dd59bcea50a9d2d45ae356abfe01f26/README.md)
- Concepts: [github.com/ianpoley/magpie/blob/92dcd83f7dd59bcea50a9d2d45ae356abfe01f26/CONCEPTS.md](https://github.com/ianpoley/magpie/blob/92dcd83f7dd59bcea50a9d2d45ae356abfe01f26/CONCEPTS.md)

## Limits and data handling

Sync uses your X browser session cookies (`auth_token`, `ct0`) through Birdclaw; the README warns this breaks X's terms and could get the account limited or suspended, and the cookies grant full account access. Post text is sent to TypeSafe and, if enabled, to Claude. The author calls it rough. No license file.

## Review and maintenance

Reviewed **2026-11-24** (Europe/Sofia) at [commit 92dcd83f7dd5](https://github.com/ianpoley/magpie/tree/92dcd83f7dd59bcea50a9d2d45ae356abfe01f26). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
