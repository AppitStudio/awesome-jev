# Jev Plays Chess by hs094 (play chess and Connect Four against Jev in the browser while Jev runs a Dino game)

[All projects](../README.md) · [Web apps](README.md#web-apps)

A browser game lab: you play White at chess or a Connect Four game against Jev, which picks from the legal moves the browser gives it, while Jev also plays a Chrome-Dino-style runner by choosing `jump` or `wait`. Games are saved locally in SQLite persisted through IndexedDB. Not related to the dmallory42 Jev plays chess ladder.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/hs094/Jev-Plays-Chess) |
| Tags | `Source available` · `Free` · `BYOK` |
| Product homepage | [Product homepage](https://jev-plays-chess.iamhardikat11.workers.dev) |
| Pricing and access | The live site is free to open; Jev moves need your own OpenCode API key with access to `jev-1.13-free`, or you can pick the keyless classifier.dev provider. Source has no license file, so reuse terms are not granted. Checked 2026-11-22. |
| Jev evidence | [`worker/index.ts`](https://github.com/hs094/Jev-Plays-Chess/blob/f0dd79ce9254488bc3aa2a5b60c94cf5070899a4/worker/index.ts) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [hs094](https://github.com/hs094). Independently curated. |
| Format | React + TypeScript web app + Cloudflare Worker |
| Platform and availability | Web (live Cloudflare Worker site, or run locally with Vite). |
| Jev's role | Picks each move as a choice among legal moves (the browser enforces the rules), and jump-or-wait for the runner. |
| Requirements | A browser; an OpenCode API key with `jev-1.13-free` access (stored encrypted in the browser), or the keyless classifier.dev option. Node.js 20+ to run it yourself. |
| License | No license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |

## When to use

- A playful way to see how a decision model chooses among legal options in real time.
- Mismatch: a strong chess opponent; Jev is not a chess engine and has no search.

## How it works

`worker/index.ts` proxies `/api/jev` to OpenCode Zen's `https://opencode.ai/zen/v1/systemone` with the key the browser supplies, so the browser avoids CORS; the classifier.dev provider receives the legal actions as labels instead. Integration evidence: [`worker/index.ts`](https://github.com/hs094/Jev-Plays-Chess/blob/f0dd79ce9254488bc3aa2a5b60c94cf5070899a4/worker/index.ts).

## Get started

Open the live site and pick a provider under "Under the hood", or run it locally with Vite.

```sh
git clone https://github.com/hs094/Jev-Plays-Chess && cd Jev-Plays-Chess
npm install
npm run dev
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Live site: [jev-plays-chess.iamhardikat11.workers.dev](https://jev-plays-chess.iamhardikat11.workers.dev)
- Demo screenshot: [github.com/hs094/Jev-Plays-Chess/blob/f0dd79ce9254488bc3aa2a5b60c94cf5070899a4/assets/demo.png](https://github.com/hs094/Jev-Plays-Chess/blob/f0dd79ce9254488bc3aa2a5b60c94cf5070899a4/assets/demo.png)

## Limits and data handling

The current position is sent to the chosen provider for each move; games stay in the browser. The OpenCode key is encrypted with a non-extractable Web Crypto key, which the author notes is not a complete security boundary. Whether classifier.dev runs Jev was not verified. No license file: reuse terms are not granted.

## Review and maintenance

Reviewed **2026-11-22** (Europe/Sofia) at [commit f0dd79ce9254](https://github.com/hs094/Jev-Plays-Chess/tree/f0dd79ce9254488bc3aa2a5b60c94cf5070899a4). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
