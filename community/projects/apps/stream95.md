# stream95 (Windows 95-style live-stream overlay whose chat is moderated by rules and Jev before it shows)

[All projects](../README.md) · [Web apps](README.md#web-apps)

Live-stream overlay for old-school programming channels built with React95: eight ready OBS scenes, chat that passes local rules and then Jev before it appears on screen, an LLM fallback when Jev is unsure, a Clippy that answers chat questions and optional text-to-speech. Portuguese-language docs.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/frederico-kluser/stream95) |
| Tags | `Open source` · `Free source build` |
| Product homepage | [Repository README](https://github.com/frederico-kluser/stream95#readme) (source-built; no separate product site verified). |
| Pricing and access | Open source (MIT); free source build. Jev and LLM calls are billed to your own OpenRouter key. Checked 2026-10-28. |
| Jev evidence | [`apps/server/src/env.ts`](https://github.com/frederico-kluser/stream95/blob/b940a1be1bec0a5e410e73a91e3fd997a8f56d72/apps/server/src/env.ts) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [frederico-kluser](https://github.com/frederico-kluser). Independently curated. |
| Format | Local Node.js server with browser-source scenes |
| Platform and availability | Runs locally; scenes load in OBS as browser sources. |
| Jev's role | Chat moderation: Jev decides whether each message is shown, held for a human, or flagged. |
| Requirements | Node.js and OBS; an OpenRouter key for Jev and the fallback LLM. |
| License | [MIT](https://github.com/frederico-kluser/stream95/blob/b940a1be1bec0a5e410e73a91e3fd997a8f56d72/LICENSE) |

## When to use

- Moderate a live chat before it reaches the overlay.
- Mismatch: Portuguese docs; the moderation benchmark is 8 messages.

## How it works

The server reads `JEV_MODEL` (default `typesafe/jev-1.14`, `apps/server/src/env.ts`) and asks Jev through OpenRouter's Decisions API about each message; if Jev is unsure or down, the LLM decides. Integration evidence: [`apps/server/src/env.ts`](https://github.com/frederico-kluser/stream95/blob/b940a1be1bec0a5e410e73a91e3fd997a8f56d72/apps/server/src/env.ts).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/frederico-kluser/stream95 && cd stream95
npm install
npm run build
npm start   # http://localhost:1995
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README (Portuguese): [github.com/frederico-kluser/stream95#readme](https://github.com/frederico-kluser/stream95#readme)

## Limits and data handling

Chat messages go to OpenRouter and TypeSafe for moderation.

## Review and maintenance

Reviewed **2026-10-28** (Europe/Sofia) at [commit b940a1be1bec](https://github.com/frederico-kluser/stream95/tree/b940a1be1bec0a5e410e73a91e3fd997a8f56d72). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
