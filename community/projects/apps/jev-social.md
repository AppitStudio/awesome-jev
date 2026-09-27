# Jev Social

[All projects](../README.md) · [Web apps](README.md#web-apps)

Local web UI and CLI that uses Jev through OpenRouter or an explicit loopback System One-compatible provider to choose read-only Instagram, TikTok, and LinkedIn research operations; the local `socai CLI` executes them in your Chrome and returns evidence for the next decision.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/socai-io/jev-social) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Product homepage](https://socai-io.github.io/jev-social/) |
| Pricing and access | No app purchase fee for the MIT source build. Requires Node 20+, an installed socai CLI, and either an OpenRouter key with Jev access (`OPENROUTER_API_KEY`) or a user-started TypeSafe-compatible server on the exact loopback `/v1/systemone` endpoint. Provider usage and any social-platform account rules are separate. Checked **2026-09-27**. |
| Jev evidence | [`src/classifier.js`](https://github.com/socai-io/jev-social/blob/0ea7be9d2ad4e19d1ae629d9b01bb670a90546b8/src/classifier.js) builds Choice questions for platform routes and later loop operations. [`src/decision-provider.js`](https://github.com/socai-io/jev-social/blob/0ea7be9d2ad4e19d1ae629d9b01bb670a90546b8/src/decision-provider.js) sends them to OpenRouter by default or to an explicit loopback System One-compatible endpoint. |
| Disclosure | Independently curated listing; not an endorsement. This factual update was submitted by a Jev Social maintainer with AI assistance. No live browser/social session or live Jev call was run for the update. |
| Maintainer | [socai-io](https://github.com/socai-io). This correction was submitted by project maintainer [IRONICBo](https://github.com/IRONICBo). |
| Format | Node.js local HTTP UI (`http://127.0.0.1:8766`) and CLI; package version **0.1.10** at reviewed commit `0ea7be9`, runnable from the tagged GitHub release with `npx` or from a source checkout. |
| Platform and availability | Local web app + CLI; loopback-only server. The reviewed commit is the `v0.1.10` release target and provides version-pinned `npx` startup, a versioned Agent Skill, and a source-checkout path. |
| Jev's role | Chooses platform route and each next read-only socai operation (search, open profile/post, comments, optional TikTok download, finish). socai owns browser automation; an LLM is not used to invent DOM coordinates or shell. |
| Requirements | Node ≥ 20; socai CLI; Chrome for socai; OpenRouter Jev access or an explicit loopback System One-compatible decision provider. |
| License | [MIT](https://github.com/socai-io/jev-social/blob/0ea7be9d2ad4e19d1ae629d9b01bb670a90546b8/LICENSE). |

## When to use

Use it for bounded, cited social research where Jev picks among concrete CLI operations discovered from prior results. Prefer [Jev Ultrafast](../tools/jev-ultrafast.md) or other browser agents when the task is general web navigation rather than Instagram/TikTok/LinkedIn via socai.

## How it works

1. Jev classifies the goal onto a supported platform workflow (`instagram_search` / `tiktok_search` / `linkedin_search` / `unsupported`).
2. In the loop, Jev chooses the next allowed operation from targets already captured (or explicit URLs); unsupported or low-confidence choices do not execute.
3. socai runs the selected command in real Chrome; summaries feed the next Choice set. Runs checkpoint completed operations and public evidence, while the UI prioritizes up to four previewable cards and retains the full evidence set for the report.

## Get started

```sh
# Node.js 20+ required. The default path contacts OpenRouter to validate
# a key entered at the prompt and stores it in ~/.jev-social/config.json.
# On macOS/Windows it can download and run the official socai installer.
npx github:socai-io/jev-social#v0.1.10 onboard

# Live (provider usage may be billable; reuses local Chrome):
npx github:socai-io/jev-social#v0.1.10
```

For local decisions, start a TypeSafe-compatible server such as Kev, set `JEV_SOCIAL_SYSTEM_ONE_URL` to its exact loopback `/v1/systemone` endpoint, and set `OPENROUTER_REPORT_MODEL=off` to keep report generation deterministic. This path does not require or receive an OpenRouter key. On Linux, install socai from source, set `SOCAI_BIN`, and use the source-checkout path documented in the [upstream README](https://github.com/socai-io/jev-social/tree/0ea7be9d2ad4e19d1ae629d9b01bb670a90546b8#run-it). This catalog update did not start the UI, drive social sites, or make a live decision-provider call.

## Examples and demos

- Historical routing-only prototype GIF under [`docs/`](https://github.com/socai-io/jev-social/tree/0ea7be9d2ad4e19d1ae629d9b01bb670a90546b8/docs); it predates the current per-operation Jev loop.
- Current operation table, CLI examples, recorded Instagram/TikTok evidence, and selectable research prompts in the [README](https://github.com/socai-io/jev-social/tree/0ea7be9d2ad4e19d1ae629d9b01bb670a90546b8#available-operations) and local UI.
- Fixed benchmark tasks, a privacy-safe row schema, and an exact-environment ten-run publication gate are documented in [`benchmark/README.md`](https://github.com/socai-io/jev-social/blob/0ea7be9d2ad4e19d1ae629d9b01bb670a90546b8/benchmark/README.md); v0.1.8 introduced the tooling, not a live speed result.
- Upstream GitHub Actions test workflow badge.

## Limits and data handling

With the default provider, goal text, operation options, and observed result summaries go to OpenRouter→Jev. With the local provider, the same bounded decision payload goes only to the explicitly configured loopback endpoint; an OpenRouter key is not forwarded. Report synthesis is a separate OpenRouter call by default when a key is configured, and `OPENROUTER_REPORT_MODEL=off` selects the deterministic source-linked report. Jev Social launches each socai child with an explicit environment allowlist that excludes OpenRouter, TypeSafe, socai-account, and session credentials; v0.1.10 also defaults `SOCAI_TELEMETRY` to `0`, with only the exact value `1` opting in. Browser cookies/sessions stay with socai/Chrome under your accounts—respect platform terms. Posting, liking, following, and messaging are out of scope. Login gates and step limits yield partial results rather than false success.

## Review and maintenance

Updated on **2026-09-27** against the `v0.1.10` release [commit 0ea7be9](https://github.com/socai-io/jev-social/tree/0ea7be9d2ad4e19d1ae629d9b01bb670a90546b8): package version **0.1.10**, MIT. The maintainer contributor inspected the README, security policy, license, provider resolver, Jev classifier/action loop, socai child-process environment, benchmark contract, checkpoint and preview paths, `package.json`, and release metadata, then ran `npm ci --ignore-scripts`, `npm run check`, and `npm test` (**199/199 offline tests passed**). These checks cover application control flow; the update did not launch the tagged app, drive a social site, make a live decision-provider call, or establish model accuracy or end-to-end speed.

Related: [Jev Ultrafast](../tools/jev-ultrafast.md), [Jev Browser (tontoko)](../tools/jev-browser-tontoko.md).
