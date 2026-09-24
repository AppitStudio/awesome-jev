# Jev Social

[All projects](../README.md) · [Web apps](README.md#web-apps)

Local web UI and CLI that uses TypeSafe Jev (via OpenRouter) to choose read-only Instagram, TikTok, and LinkedIn research operations; [socai](https://github.com/socai-io/socai) executes them in your Chrome and returns evidence for the next decision.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/socai-io/jev-social) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Product homepage](https://socai-io.github.io/jev-social/) |
| Pricing and access | No app purchase fee for the MIT source build. Requires Node 20+, installed socai CLI, and an OpenRouter key with Jev access (`OPENROUTER_API_KEY`). Provider usage and any social-platform account rules are separate. Checked **2026-09-24**. |
| Jev evidence | [`src/classifier.js`](https://github.com/socai-io/jev-social/blob/51830b34906673e796754b70f8e878d166822a9b/src/classifier.js) posts Choice questions to OpenRouter `https://openrouter.ai/api/alpha/decisions` (default model `~typesafe/jev-latest`) to pick platform routes and later loop operations. |
| Disclosure | Independently curated listing; not an endorsement. This factual update was submitted by a Jev Social maintainer with AI assistance. No live browser/social session or live Jev call was run for the update. |
| Maintainer | [socai-io](https://github.com/socai-io). This correction was submitted by project maintainer [IRONICBo](https://github.com/IRONICBo). |
| Format | Node.js local HTTP UI (`http://127.0.0.1:8766`) and CLI; package version **0.1.5** at reviewed commit `51830b3`, runnable from the tagged GitHub release with `npx` or from a source checkout. |
| Platform and availability | Local web app + CLI; loopback-only server. The reviewed commit is the `v0.1.5` release target and provides version-pinned `npx` startup plus a source-checkout path. |
| Jev's role | Chooses platform route and each next read-only socai operation (search, open profile/post, comments, optional TikTok download, finish). socai owns browser automation; an LLM is not used to invent DOM coordinates or shell. |
| Requirements | Node ≥ 20; socai CLI; `OPENROUTER_API_KEY`; Chrome for socai. |
| License | [MIT](https://github.com/socai-io/jev-social/blob/51830b34906673e796754b70f8e878d166822a9b/LICENSE). |

## When to use

Use it for bounded, cited social research where Jev picks among concrete CLI operations discovered from prior results. Prefer [Jev Ultrafast](../tools/jev-ultrafast.md) or other browser agents when the task is general web navigation rather than Instagram/TikTok/LinkedIn via socai.

## How it works

1. Jev classifies the goal onto a supported platform workflow (`instagram_search` / `tiktok_search` / `linkedin_search` / `unsupported`).
2. In the loop, Jev chooses the next allowed operation from targets already captured (or explicit URLs); unsupported or low-confidence choices do not execute.
3. socai runs the selected command in real Chrome; summaries feed the next Choice set. Runs checkpoint completed operations and public evidence, while the UI prioritizes up to four previewable cards and retains the full evidence set for the report.

## Get started

```sh
# Node.js 20+ required. This contacts OpenRouter to validate the key and
# stores a key entered at the prompt in ~/.jev-social/config.json.
# On macOS/Windows it can download and run the official socai installer.
npx github:socai-io/jev-social#v0.1.5 onboard

# Live (provider usage may be billable; reuses local Chrome):
npx github:socai-io/jev-social#v0.1.5
```

On Linux, install socai from source, set `SOCAI_BIN`, and use the source-checkout path documented in the [upstream README](https://github.com/socai-io/jev-social/tree/51830b34906673e796754b70f8e878d166822a9b#run-it). This catalog update did not run onboarding, start the UI, drive social sites, or call OpenRouter/Jev.

## Examples and demos

- Historical routing-only prototype GIF under [`docs/`](https://github.com/socai-io/jev-social/tree/51830b34906673e796754b70f8e878d166822a9b/docs); it predates the current per-operation Jev loop.
- Current operation table, CLI examples, recorded Instagram/TikTok evidence, and selectable research prompts in the [README](https://github.com/socai-io/jev-social/tree/51830b34906673e796754b70f8e878d166822a9b#available-operations) and local UI.
- Upstream GitHub Actions test workflow badge.

## Limits and data handling

Goal text, operation options, and observed result summaries go to OpenRouter→Jev. Browser cookies/sessions stay with socai/Chrome under your accounts—respect platform terms. Posting, liking, following, and messaging are out of scope. Login gates and step limits yield partial results rather than false success.

## Review and maintenance

Updated on **2026-09-24** against the `v0.1.5` release [commit 51830b3](https://github.com/socai-io/jev-social/tree/51830b34906673e796754b70f8e878d166822a9b): package version **0.1.5**, MIT. The maintainer contributor inspected the README, license, Jev classifier/action loop, checkpoint and preview paths, `package.json`, and release metadata, then ran `npm ci --ignore-scripts`, `npm run check`, and `npm test` (**87/87 offline tests passed**). These checks cover application control flow; the update did not run the app through `npx`, drive a social site, make a live Jev call, or establish model accuracy or end-to-end speed.

Related: [Jev Ultrafast](../tools/jev-ultrafast.md), [Jev Browser (tontoko)](../tools/jev-browser-tontoko.md).
