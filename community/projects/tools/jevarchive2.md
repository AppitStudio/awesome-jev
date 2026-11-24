# JevArchive 2 by happydesk213124 (RisuAI long-term memory plugin that keeps original chat fragments and lets Jev pick what to recall)

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

Korean RisuAI plugin for long role-play chats. It stores conversation fragments word for word with date and character tags, and uses Jev plus embeddings (no summarising LLM) to tag events, people, promises and secrets and to choose which memories go into each reply. Includes character and relationship views.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/happydesk213124/JevArchive2) |
| Maintainer | [happydesk213124](https://github.com/happydesk213124). Independently curated. |
| Format | RisuAI plugin (single JavaScript file) |
| Requirements | RisuAI and an OpenRouter key (recommended, for Jev and embeddings) or a TypeSafe key plus an embeddings provider. |
| License | No license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`jevarchive.js`](https://github.com/happydesk213124/JevArchive2/blob/16be0c45dddec54d07213ec20744fd8629fa7858/jevarchive.js) at the pinned commit. |

## When to use

- Keep long RisuAI chats consistent about who did what, when, without a summary model rewriting memories.
- Mismatch: non-Korean readers (docs and UI are Korean) or apps other than RisuAI.

## How it works

`jevarchive.js` offers OpenRouter (`typesafe/jev-1.14` at `https://openrouter.ai/api/v1/systemone`) or TypeSafe's `https://api.typesafe.ai/v1/systemone`; Jev only selects names, words or sentences that appear in the message and leaves fields empty otherwise. Integration evidence: [`jevarchive.js`](https://github.com/happydesk213124/JevArchive2/blob/16be0c45dddec54d07213ec20744fd8629fa7858/jevarchive.js).

## Get started

Download `jevarchive.js`, add it under RisuAI's plugin settings, and follow the in-app setup; turn off RisuAI's own memory to avoid double recall.

```sh
curl -LO https://raw.githubusercontent.com/happydesk213124/JevArchive2/16be0c45dddec54d07213ec20744fd8629fa7858/jevarchive.js
# RisuAI → Settings → Plugins → Add plugin → choose jevarchive.js
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README (Korean): [github.com/happydesk213124/JevArchive2/blob/16be0c45dddec54d07213ec20744fd8629fa7858/README.md](https://github.com/happydesk213124/JevArchive2/blob/16be0c45dddec54d07213ec20744fd8629fa7858/README.md)
- 1.x repository: [github.com/happydesk213124/JevArchive](https://github.com/happydesk213124/JevArchive)

## Limits and data handling

Chat fragments are sent to OpenRouter or TypeSafe and your embeddings provider, billed to your keys. Version 2.0 replaces the 1.x JevArchive repo. No license file, so no reuse terms are granted.

## Review and maintenance

Reviewed **2026-11-24** (Europe/Sofia) at [commit 16be0c45ddde](https://github.com/happydesk213124/JevArchive2/tree/16be0c45dddec54d07213ec20744fd8629fa7858). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
