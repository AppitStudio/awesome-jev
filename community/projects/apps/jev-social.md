# Jev Social

[All projects](../README.md) · [Web apps](README.md#web-apps)

Local web UI and CLI that uses TypeSafe Jev (via OpenRouter) to choose read-only Instagram, TikTok, and LinkedIn research operations; [socai](https://github.com/socai-io/socai) executes them in your Chrome and returns evidence for the next decision.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/socai-io/jev-social) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Product homepage](https://socai-io.github.io/jev-social/) |
| Pricing and access | No app purchase fee for the MIT source build. Requires Node 20+, installed socai CLI, and an OpenRouter key with Jev access (`OPENROUTER_API_KEY`). Provider usage and any social-platform account rules are separate. Checked **2026-09-20**. |
| Jev evidence | [`src/classifier.js`](https://github.com/socai-io/jev-social/blob/c06651eba85267fed7ec5edeeb8ad7b84b9c7d81/src/classifier.js) posts Choice questions to OpenRouter `https://openrouter.ai/api/alpha/decisions` (default model `~typesafe/jev-latest`) to pick platform routes and later loop operations. |
| Disclosure | Independently curated listing; not an upstream submission or endorsement. AI-assisted source review; live browser/social sessions and live Jev calls were not run. |
| Maintainer | [socai-io](https://github.com/socai-io). Contributor affiliation/commercial relationships were not supplied. |
| Format | Node.js **jev-social 0.1.0** local HTTP UI (`http://127.0.0.1:8766`) and CLI (`npm start -- search …`). |
| Platform and availability | Source-built local web app + CLI; loopback-only server. Release stage early (0.1.0). |
| Jev's role | Chooses platform route and each next read-only socai operation (search, open profile/post, comments, optional TikTok download, finish). socai owns browser automation; an LLM is not used to invent DOM coordinates or shell. |
| Requirements | Node ≥ 20; socai CLI; `OPENROUTER_API_KEY`; Chrome for socai. |
| License | [MIT](https://github.com/socai-io/jev-social/blob/c06651eba85267fed7ec5edeeb8ad7b84b9c7d81/LICENSE). |

## When to use

Use it for bounded, cited social research where Jev picks among concrete CLI operations discovered from prior results. Prefer [Jev Ultrafast](../tools/jev-ultrafast.md) or other browser agents when the task is general web navigation rather than Instagram/TikTok/LinkedIn via socai.

## How it works

1. Jev classifies the goal onto a supported platform workflow (`instagram_search` / `tiktok_search` / `linkedin_search` / `unsupported`).
2. In the loop, Jev chooses the next allowed operation from targets already captured (or explicit URLs); unsupported or low-confidence choices do not execute.
3. socai runs the selected command in real Chrome; summaries feed the next Choice set. Runs store choices, confidence, commands, and evidence for reports.

## Get started

```sh
# install socai per upstream, then:
git clone https://github.com/socai-io/jev-social.git
cd jev-social
git checkout c06651eba85267fed7ec5edeeb8ad7b84b9c7d81
npm install
cp .env.example .env   # OPENROUTER_API_KEY=…
npm test               # offline node:test
# Live (billable + browser): npm start
```

This listing did not start the UI, drive social sites, or call OpenRouter/Jev.

## Examples and demos

- Docs GIF and platform notes under [`docs/`](https://github.com/socai-io/jev-social/tree/c06651eba85267fed7ec5edeeb8ad7b84b9c7d81/docs).
- CLI examples in the README (`npm start -- search "…" --platform auto --limit 4`).
- Upstream GitHub Actions test workflow badge.

## Limits and data handling

Goal text, operation options, and observed result summaries go to OpenRouter→Jev. Browser cookies/sessions stay with socai/Chrome under your accounts—respect platform terms. Posting, liking, following, and messaging are out of scope. Login gates and step limits yield partial results rather than false success.

## Review and maintenance

Reviewed on **2026-09-20** at [commit c06651e](https://github.com/socai-io/jev-social/tree/c06651eba85267fed7ec5edeeb8ad7b84b9c7d81): **0.1.0**, MIT. AI-assisted review of README, `classifier.js`, and `package.json`. `npm test` / live runs not executed on the review host.

Related: [Jev Ultrafast](../tools/jev-ultrafast.md), [Jev Browser (tontoko)](../tools/jev-browser-tontoko.md).
