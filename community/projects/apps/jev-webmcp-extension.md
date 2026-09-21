# Jev × WebMCP

[All projects](../README.md) · [Browser extensions](README.md#browser-extensions)

Chrome side panel that uses TypeSafe Jev (System One) to select and populate WebMCP tool calls from keystrokes on the current page. Converts the page's tool schemas into Jev questions; shows confidence and latency; confirms non-readOnly or consequential tools.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/sdras/jev-webmcp-extension) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Project homepage](https://github.com/sdras/jev-webmcp-extension#jev--webmcp-chrome-extension) |
| Pricing and access | [Load unpacked from source](https://github.com/sdras/jev-webmcp-extension#set-it-up); no app purchase fee and no Chrome Web Store listing verified. Bring a TypeSafe API key from [console.typesafe.ai/keys](https://console.typesafe.ai/keys) (stored in `chrome.storage.local`). Inference usage can incur charges. Reviewed 2026-09-22. |
| Jev evidence | [`src/jev.js`](https://github.com/sdras/jev-webmcp-extension/blob/1ec3afb6cebf116d811a3c8a073414edaf5cb67c/src/jev.js) posts `{state, model, questions}` to `https://api.typesafe.ai/v1/systemone` with default `jev-latest`. [`src/core/questions.js`](https://github.com/sdras/jev-webmcp-extension/blob/1ec3afb6cebf116d811a3c8a073414edaf5cb67c/src/core/questions.js) turns WebMCP tool schemas into Choice/Score/Noul questions; [`src/core/decode.js`](https://github.com/sdras/jev-webmcp-extension/blob/1ec3afb6cebf116d811a3c8a073414edaf5cb67c/src/core/decode.js) and [`src/core/policy.js`](https://github.com/sdras/jev-webmcp-extension/blob/1ec3afb6cebf116d811a3c8a073414edaf5cb67c/src/core/policy.js) decode answers and gate auto-run vs confirmation. |
| Disclosure | AI-assisted catalog review; no affiliation or commercial relationship with the maintainer was supplied. Community project, not affiliated with TypeSafe. Listing is not an endorsement. Source and offline `npm test` inspected; Chrome install, WebMCP enablement, and live TypeSafe calls were not tested on the review host. |
| Maintainer | [Sarah Drasner / sdras](https://github.com/sdras) ([@sarah_edo](https://x.com/sarah_edo)). Independently curated. |
| Format | Manifest V3 Chrome side-panel extension **0.1.0** (plain JS modules; no build step). |
| Platform and availability | Chrome **149+** with WebMCP (origin trial or `chrome://flags/#enable-webmcp-testing`). Developer mode → Load unpacked on the repo folder. Not verified on the Chrome Web Store. |
| Jev's role | Selects which page WebMCP tool fits the user's utterance and fills typed arguments from schemas; application code bridges to the page, applies readOnly/consequential confirmation policy, and screens tool manifests. Jev does not generate free-form tool-calling prose. |
| Requirements | Chrome 149+ with WebMCP; TypeSafe API key in extension settings; optional host permission per enabled site. |
| License | [Apache-2.0](https://github.com/sdras/jev-webmcp-extension/blob/1ec3afb6cebf116d811a3c8a073414edaf5cb67c/LICENSE) (vendored `lz-string` remains MIT). |

## When to use

Use it when a page already exposes WebMCP tools and you want typed selection of the tool and arguments from natural language in a side panel, with per-site access and confirmation for state-changing calls. Prefer [Jev for Chrome](jev-for-chrome.md) when you need Jev to drive ordinary DOM clicks and typing without WebMCP. Prefer [Tab Bouncer](tab-bouncer.md) for bulk tab triage rather than in-page tool execution. Do not treat confidence percentages or demo latencies as audited production SLOs.

## How it works

1. The side panel discovers WebMCP tools on the enabled site via a main-world bridge (`pageListTools` / `pageCallTool` in [`src/platform/chrome.js`](https://github.com/sdras/jev-webmcp-extension/blob/1ec3afb6cebf116d811a3c8a073414edaf5cb67c/src/platform/chrome.js)).
2. [`src/core/questions.js`](https://github.com/sdras/jev-webmcp-extension/blob/1ec3afb6cebf116d811a3c8a073414edaf5cb67c/src/core/questions.js) maps tool lists and parameter schemas into parallel Jev questions (routing Choice, enums, booleans, spans of the user's words, and optional “is it stated?” Nouls).
3. [`src/jev.js`](https://github.com/sdras/jev-webmcp-extension/blob/1ec3afb6cebf116d811a3c8a073414edaf5cb67c/src/jev.js) calls TypeSafe System One; the panel shows predicted calls, confidence, and latency as you type.
4. [`src/core/policy.js`](https://github.com/sdras/jev-webmcp-extension/blob/1ec3afb6cebf116d811a3c8a073414edaf5cb67c/src/core/policy.js) allows automatic run only for confident `readOnlyHint` tools unless disabled; consequential or destructive annotations always need a second confirmation. Manifest screening flags agent-directed tool descriptions.

## Get started

```sh
git clone https://github.com/sdras/jev-webmcp-extension.git
cd jev-webmcp-extension
git checkout 1ec3afb6cebf116d811a3c8a073414edaf5cb67c
# Chrome 149+ → chrome://flags/#enable-webmcp-testing (or origin trial)
# chrome://extensions → Developer mode → Load unpacked → this folder
# Side panel settings → paste TypeSafe key → Enable on (site)
```

There is no build step. Live keystrokes and tool execution send utterances and tool schemas to TypeSafe and can incur charges; this listing did not load the extension or call the live API.

## Examples and demos

- Upstream walkthrough against the [Basketful live demo](https://shopping-webmcp-demo.netlify.app/) or local [shopping-cart-webmcp](https://github.com/sdras/shopping-cart-webmcp) (`npm run dev`) — not executed on the review host.
- Offline: `npm test` (schema → questions → decode → policy; no network). Optional `npm run harness` (mock model) and `npm run eval` (live API; needs `TYPESAFE_API_KEY`).

## Limits and data handling

Chrome 149+ and WebMCP are required. Per-site optional host permissions; keys stay in `chrome.storage.local`. User utterances and page-provided tool descriptions/schemas go to TypeSafe; tool results stay in the panel and are not fed back into model requests. Page schemas remain untrusted inputs. Array arguments currently populate only the first element. Prediction quality depends on question wording; live latency/accuracy claims were not reproduced here.

## Review and maintenance

Reviewed on **2026-09-22** (Europe/Sofia) at [commit 1ec3afb6](https://github.com/sdras/jev-webmcp-extension/tree/1ec3afb6cebf116d811a3c8a073414edaf5cb67c): **0.1.0**, Apache-2.0. AI-assisted source review of README, LICENSE, `manifest.json`, `src/jev.js`, `src/core/*`, and `package.json`. Offline `npm test`: **16 passed** on the review host (Node.js 22). Chrome install, WebMCP flag/origin trial, Basketful demo, and live TypeSafe/`npm run eval` were not run.

Related: [Jev for Chrome](jev-for-chrome.md), [Tab Bouncer](tab-bouncer.md), [Smart Paste](smart-paste.md).
