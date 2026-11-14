# Jev demos collection (honeyychawla) (five local Jev apps — ad blocker, Domino's cart chat, emoji search, Gmail/YouTube inbox and X feed classifier — with setup guides and one-shot build prompts)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

One repository bundling five finished local demos, each with its source package, a shareable ZIP, a setup guide and a one-shot prompt for rebuilding it with a coding agent: Jev Shield (hides display ads), a Domino's cart builder driven by chat, Emote (emoji search), Jev Inbox (sorts Gmail and YouTube comments) and Sift (decides which X posts to open). Most call Jev through OpenRouter.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/honeyychawla/jev) |
| Maintainer | [honeyychawla](https://github.com/honeyychawla). Independently curated. |
| Format | Collection of local web apps and browser extensions (JavaScript/TypeScript) |
| Requirements | Node.js for the apps, Chrome for the extensions, and an OpenRouter key; Jev Inbox also needs your own Google OAuth client. |
| License | No license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`use-cases/pizza-ordering/decisions.mjs`](https://github.com/honeyychawla/jev/blob/70a9755918ba90ac26195d4c04d3cc525c40b198/use-cases/pizza-ordering/decisions.mjs) at the pinned commit. |

## When to use

- Start from a working small Jev app and its build prompt instead of a blank project.
- Mismatch: maintained products; these are demo snapshots (14 November 2026).

## How it works

Each demo calls Jev through OpenRouter, e.g. `use-cases/pizza-ordering/decisions.mjs` posts to `https://openrouter.ai/api/alpha/decisions` and `use-cases/x-feed-classifier/lib/provider.js` uses OpenRouter's `/api/v1/systemone`; the inbox defaults to `typesafe/jev-1.14`. Integration evidence: [`use-cases/pizza-ordering/decisions.mjs`](https://github.com/honeyychawla/jev/blob/70a9755918ba90ac26195d4c04d3cc525c40b198/use-cases/pizza-ordering/decisions.mjs).

## Get started

Pick a demo in the README table, then follow that demo's setup guide (or use its ZIP).

```sh
git clone https://github.com/honeyychawla/jev && cd jev
# open use-cases/<demo>/README.md and follow its setup guide
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/honeyychawla/jev/blob/70a9755918ba90ac26195d4c04d3cc525c40b198/README.md](https://github.com/honeyychawla/jev/blob/70a9755918ba90ac26195d4c04d3cc525c40b198/README.md)
- Emote (standalone repo): [github.com/honeyychawla/emote-emoji-search](https://github.com/honeyychawla/emote-emoji-search)
- Jev Inbox (standalone repo): [github.com/honeyychawla/jev-inbox](https://github.com/honeyychawla/jev-inbox)

## Limits and data handling

Each demo sends its inputs (page elements, chat messages, emails and comments, X posts) to OpenRouter on your key. The Domino's demo builds a cart; check it before any real order. No license file, so reuse terms are not granted.

## Review and maintenance

Reviewed **2026-11-15** (Europe/Sofia) at [commit 70a9755918ba](https://github.com/honeyychawla/jev/tree/70a9755918ba90ac26195d4c04d3cc525c40b198). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
