# Slop Mop

[All projects](../README.md) · [Browser extensions](README.md#browser-extensions)

Chrome Manifest V3 extension that judges LinkedIn post writing with TypeSafe Jev (11–12 typed questions), then folds or highlights suspected slop so you can inspect the score and overrule it. Not an AI detector.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/tomfrazier/slopmop) |
| Tags | `Open source` · `Free` · `BYOK` |
| Product homepage | [slopmop.lol](https://slopmop.lol) |
| Pricing and access | Hosted use via the maintainer's server is free with no signup; default daily cap is **250 checks per install per UTC day** (documented upstream). Self-host the MIT server with your own TypeSafe / AI Gateway key (`BYOK`); inference and hosting can incur charges. No paid app tier. Checked **2026-09-22**. |
| Jev evidence | [`slopmop-server/src/jev.ts`](https://github.com/tomfrazier/slopmop/blob/0c12eed4d95de8efb13621e7da10c544a8bbd99f/slopmop-server/src/jev.ts) builds a TypeSafe System One scorer; [`slopmop-server/src/routes/judge.ts`](https://github.com/tomfrazier/slopmop/blob/0c12eed4d95de8efb13621e7da10c544a8bbd99f/slopmop-server/src/routes/judge.ts) serves `POST /api/v1/judge`. Questions (nine Graphite-style tells, two counter-signs, optional AI-likelihood noul) are in [`slopmop-server/src/questions.ts`](https://github.com/tomfrazier/slopmop/blob/0c12eed4d95de8efb13621e7da10c544a8bbd99f/slopmop-server/src/questions.ts). |
| Disclosure | Self-submission via [issue #262](https://github.com/AppitStudio/awesome-jev/issues/262) / JevList by the maintainer. AI-assisted catalog review. Listing is not an endorsement. Source and offline vitest inspected; Chrome install, live LinkedIn browsing, and live Jev were not tested on the review host. Production tell weights on the maintainer's server may differ from equal-weight OSS defaults (disclosed upstream). |
| Maintainer | [Tom Frazier](https://github.com/tomfrazier) (`tomfrazier`). Self-submitted. |
| Format | Chromium Manifest V3 extension **0.1.0** plus Vercel Functions server (`slopmop-extension` / `slopmop-server`). |
| Platform and availability | Desktop Chromium / LinkedIn only. Load unpacked from a local build (`slopmop-extension/dist`); point at [slopmop.lol](https://slopmop.lol)'s backend or your own server. No Chrome Web Store listing verified. |
| Jev's role | Scores each post's text on typed Score/Noul writing questions; application code weights answers, applies engagement/threshold policy, and folds or highlights in the feed. Optional composer "mop" uses one daily check. |
| Requirements | Chromium; for self-host: Node toolchain, Vercel/Turso (or local server), and a TypeSafe or AI Gateway key. Hosted path needs only the built extension. |
| License | [MIT](https://github.com/tomfrazier/slopmop/blob/0c12eed4d95de8efb13621e7da10c544a8bbd99f/LICENSE). |

## When to use

Use it for personal LinkedIn browsing when you want reversible hide/highlight of posts that look like low-value writing patterns, with inspectable scores and local override votes. Prefer [JevSlop](jevslop.md) for note/article slop scoring outside LinkedIn, or [Polymorph](polymorph.md) for custom English feed rules on other sites. Do not treat judgments as authorship detection or as LinkedIn policy enforcement.

## How it works

1. The content script extracts post text (and engagement counts) on `linkedin.com` ahead of the viewport and asks the background worker to judge.
2. The worker posts to the Slop Mop server's `/api/v1/judge`. The server either returns a cached registry verdict or calls TypeSafe Jev via [`jev.ts`](https://github.com/tomfrazier/slopmop/blob/0c12eed4d95de8efb13621e7da10c544a8bbd99f/slopmop-server/src/jev.ts) / [`jevRequest.ts`](https://github.com/tomfrazier/slopmop/blob/0c12eed4d95de8efb13621e7da10c544a8bbd99f/slopmop-server/src/jevRequest.ts).
3. Weighted scores plus Mild/Moderate/Aggressive thresholds decide fold vs outline; the mop menu shows reasons and accepts No / Maybe / Probably votes (votes do not spend a check).

Ads are never scored. Author names and LinkedIn account identity are not sent; the server stores a text hash and scores by default, not the post body.

## Get started

Hosted (no account): build the extension pointed at the public product backend, or follow install steps on [slopmop.lol](https://slopmop.lol).

```sh
git clone https://github.com/tomfrazier/slopmop.git
cd slopmop
git checkout 0c12eed4d95de8efb13621e7da10c544a8bbd99f
cd slopmop-extension
npm ci
SLOPMOP_SERVER_URL=https://slopmop.lol npm run build
# Chrome → chrome://extensions → Developer mode → Load unpacked → slopmop-extension/dist
```

Self-host: run `slopmop-server` with your own TypeSafe/AI Gateway credentials, then build the extension with `SLOPMOP_SERVER_URL` set to that origin. Live judging sends post text to the server and on to Jev and can incur provider charges on a self-hosted key.

## Examples and demos

- Product site and upstream README screenshots / admin console notes.
- Offline **`npm test`** on the review host: extension **239 passed** (21 files); server **314 passed** (18 files). Live LinkedIn and live Jev were not run.

## Limits and data handling

Desktop Chromium and LinkedIn only; no mobile/Firefox/Safari path in the reviewed revision. Hosted installs share the maintainer's daily check cap and Jev budget. Self-host OSS defaults every tell to equal weight; production weights on the maintainer's server may differ. Post text leaves the browser for the configured server/Jev route. Judgments are probabilistic; stiff formal writing and humor can misfire (disclosed upstream).

## Review and maintenance

Reviewed on **2026-09-22** at [commit 0c12eed](https://github.com/tomfrazier/slopmop/tree/0c12eed4d95de8efb13621e7da10c544a8bbd99f): MIT, extension **0.1.0**. AI-assisted source review of README, LICENSE, `jev.ts`, `questions.ts`, and `routes/judge.ts`. Offline vitest as above. No Chrome load, no live LinkedIn, no live TypeSafe on the review host. Submission: [issue #262](https://github.com/AppitStudio/awesome-jev/issues/262).

Related: [JevSlop](jevslop.md), [Polymorph](polymorph.md), [Xtags](xtags.md), [Vibe Check for X](vibecheck.md).
