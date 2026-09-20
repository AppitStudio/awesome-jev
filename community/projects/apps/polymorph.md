# Polymorph

[All projects](../README.md) · [Browser extensions](README.md#browser-extensions)

Chrome extension that collapses posts matching English rules you wrote, replacing them with your own images or GIFs. TypeSafe Jev (via OpenRouter Decisions, `typesafe/jev-1.13`) is the judge; nothing is deleted—Show original restores the post.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/moomooskycow/polymorph) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Project homepage](https://github.com/moomooskycow/polymorph#polymorph) |
| Pricing and access | [Build and load unpacked](https://github.com/moomooskycow/polymorph#load); no app purchase fee. Bring an OpenRouter API key; each judged post can incur provider charges. Not on the Chrome Web Store. Reviewed 2026-09-20. |
| Jev evidence | [`src/jev/client.ts`](https://github.com/moomooskycow/polymorph/blob/3290af04a0aadca0c8841bd27cdaeb92e8c837fa/src/jev/client.ts) and [`src/defaults.ts`](https://github.com/moomooskycow/polymorph/blob/3290af04a0aadca0c8841bd27cdaeb92e8c837fa/src/defaults.ts) POST Choice questions to `https://openrouter.ai/api/alpha/decisions` with model `typesafe/jev-1.13`; gate thresholds in code. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source inspected; Chrome installation and live feed judging were not tested. |
| Maintainer | [moomooskycow](https://github.com/moomooskycow). Independently curated. |
| Format | TypeScript Manifest V3 Chrome extension (**0.3.0**), Vite build, Vitest suite. |
| Platform and availability | Source-built Chromium extension (Developer mode → Load unpacked → `dist/`). Default allowlist: X, Reddit, Hacker News, YouTube. |
| Jev's role | Judges whether a post's visible text matches an enabled English rule; extension UI hides/replaces matches. Fail-open on errors. |
| Requirements | Chromium; Node/pnpm to build; OpenRouter API key in extension Options. |
| License | [MIT](https://github.com/moomooskycow/polymorph/blob/3290af04a0aadca0c8841bd27cdaeb92e8c837fa/LICENSE). |

## When to use

Use it as a personal filter that turns matching posts into your media while keeping one-click restore. Prefer [Unclutter](unclutter.md) for broader page-clutter hide rules, or [TypeSafe Fun AdBlocker](typesafe-adblock.md) for experimental ad-shaped DOM judgments. Example rules ship **off**.

## How it works

1. Content script observes allowlisted feeds and extracts visible post text (capped; no author ids/HTML/cookies in the default state builder).
2. Background worker calls OpenRouter Decisions with `typesafe/jev-1.13` Choice questions per enabled rule ([`src/jev/`](https://github.com/moomooskycow/polymorph/tree/3290af04a0aadca0c8841bd27cdaeb92e8c837fa/src/jev)).
3. On a match above gate probability/confidence, the extension swaps in a replacement card (your IndexedDB media library or a compact collapse card). Failures leave the post visible.

## Get started

```sh
git clone https://github.com/moomooskycow/polymorph.git
cd polymorph
git checkout 3290af04a0aadca0c8841bd27cdaeb92e8c837fa
pnpm install
pnpm build
pnpm test
```

Chrome → `chrome://extensions` → Developer mode → Load unpacked → `dist/`. Options: paste OpenRouter key, enable a rule, optional media. Live judging sends post text to OpenRouter and can incur charges. This listing did not load the extension in Chrome or call live Decisions.

## Examples and demos

- Three example rules in Options (disabled by default).
- Offline Vitest coverage under `src/jev/*.test.ts` and `pnpm test`.

## Limits and data handling

Visible post text (bounded) goes to OpenRouter for Jev judgments; the key stays in `chrome.storage.local` and is used only against `openrouter.ai` per upstream. Replacement media stays in IndexedDB locally. Not a store-listed product; personal daily-driver framing. Upstream accuracy claims were not reproduced here.

## Review and maintenance

Reviewed on **2026-09-20** at [commit 3290af0](https://github.com/moomooskycow/polymorph/tree/3290af04a0aadca0c8841bd27cdaeb92e8c837fa): **0.3.0**, MIT. AI-assisted source review of README, `src/defaults.ts`, `src/jev/client.ts`, package metadata, and license. `pnpm test` / Chrome load / live OpenRouter were not executed on the review host.

Related: [Unclutter](unclutter.md), [TypeSafe Fun AdBlocker](typesafe-adblock.md), [Xtags](xtags.md).
