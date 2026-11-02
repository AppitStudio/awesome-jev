# The Living Handbook (living article for beginner vibe coders where Jev screens reader edits before a person publishes)

[All projects](../README.md) · [Web apps](README.md#web-apps)

Russian and English article for beginner vibe coders, with an MCP server their agents can read. Readers select text and suggest edits; Jev judges each suggestion, an optional writer model rewrites it, a second Jev check reviews the result, and the author publishes by hand.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Bb-soil/the-living-handbook) |
| Tags | `Open source` · `Free` |
| Product homepage | [Product homepage](https://the-living-handbook.fit-hake-0747.chatgpt.site/) |
| Pricing and access | Free live demo (sign-in needed to suggest edits); free source build under MIT with your own OpenRouter key. Checked 2026-11-03. |
| Jev evidence | [`worker/ai.js`](https://github.com/Bb-soil/the-living-handbook/blob/6391fcfea6a9c3db729e3d8c3e3e424395e8294d/worker/ai.js) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [Bb-soil](https://github.com/Bb-soil). Independently curated. |
| Format | Web app + read-only MCP server (Cloudflare Worker + D1) |
| Platform and availability | Web (live demo); self-host as a Worker. |
| Jev's role | Judges each reader suggestion and re-checks the rewritten candidate. |
| Requirements | A browser for the live demo; Node.js 22.14+ to run locally; `OPENROUTER_API_KEY` for Jev on OpenRouter's Decisions API to self-host. |
| License | [MIT](https://github.com/Bb-soil/the-living-handbook/blob/6391fcfea6a9c3db729e3d8c3e3e424395e8294d/LICENSE) |

## When to use

- Take reader suggestions on a living document while keeping a person in charge of every publication.
- Mismatch: Jev thresholds are provisional and the live demo runs on a platform-specific host.

## How it works

`worker/ai.js` sends each suggestion with its section context to OpenRouter's Decisions API (`typesafe/jev-1.14` by default) and uses the answers to admit, reject or route it; an optional Claude Haiku writer rewrites admitted ones and Jev checks the candidate again. Integration evidence: [`worker/ai.js`](https://github.com/Bb-soil/the-living-handbook/blob/6391fcfea6a9c3db729e3d8c3e3e424395e8294d/worker/ai.js).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/Bb-soil/the-living-handbook.git
cd the-living-handbook
npm ci
npm run check
npm run preview
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Live demo: [the-living-handbook.fit-hake-0747.chatgpt.site/](https://the-living-handbook.fit-hake-0747.chatgpt.site/)
- English article: [github.com/Bb-soil/the-living-handbook/blob/main/content/ARTICLE.en.md](https://github.com/Bb-soil/the-living-handbook/blob/main/content/ARTICLE.en.md)

## Limits and data handling

Selected text, the suggestion and article context go to OpenRouter (Jev) and, if enabled, the writer model; the live demo needs ChatGPT sign-in to suggest. Article content is CC BY 4.0, code MIT. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-03** (Europe/Sofia) at [commit 6391fcfea6a9](https://github.com/Bb-soil/the-living-handbook/tree/6391fcfea6a9c3db729e3d8c3e3e424395e8294d). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
