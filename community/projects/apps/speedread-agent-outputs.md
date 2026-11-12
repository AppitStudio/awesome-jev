# SpeedRead (macOS app that highlights the decisions and actions in AI coding agent outputs, using Jev)

[All projects](../README.md) · [macOS apps](README.md#macos-apps)

macOS app for reading long Claude Code or Codex reports: paste the output and Jev classifies each line, block or sentence as decision, action or info, so you can jump between what needs you and delete the rest.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/TomySpagnoletti/speed-reading-app) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/TomySpagnoletti/speed-reading-app#readme) (source-built; no separate product site verified). |
| Pricing and access | Free MIT source build; requires your own OpenRouter key, billed per Jev call by OpenRouter (the app logs cost locally). Checked 2026-11-13. |
| Jev evidence | [`src/jev.ts`](https://github.com/TomySpagnoletti/speed-reading-app/blob/351b6190930389e19966d868d3e79159eeb82008/src/jev.ts) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [TomySpagnoletti](https://github.com/TomySpagnoletti). Independently curated. |
| Format | Tauri desktop app (TypeScript + Rust, MIT) |
| Platform and availability | macOS (source build with Tauri; no signed release verified) |
| Jev's role | Jev classifies every segment of the pasted text as decision, action or info; the colour intensity follows Jev's probability. |
| Requirements | macOS with Node.js 24+, Rust and Xcode Command Line Tools to build; an OpenRouter API key in `~/.speedread/.env`. |
| License | [MIT](https://github.com/TomySpagnoletti/speed-reading-app/blob/351b6190930389e19966d868d3e79159eeb82008/LICENSE) |

## When to use

- Skim agent reports and keep only the sentences that need a decision or action from you.
- Mismatch: Windows/Linux or a prebuilt download; the README targets macOS source builds.

## How it works

`src/jev.ts` turns each segment into a three-option Jev choice question (model `typesafe/jev-1.13`) with the whole numbered message as context, batching up to 25 segments per call; the Rust side posts them to OpenRouter's decisions endpoint (`https://openrouter.ai/api/alpha/decisions`) so the key never reaches the web view. A local ledger logs each call's cost. Integration evidence: [`src/jev.ts`](https://github.com/TomySpagnoletti/speed-reading-app/blob/351b6190930389e19966d868d3e79159eeb82008/src/jev.ts).

## Get started

Put your OpenRouter key in `~/.speedread/.env`, clone, install and run in dev mode, or build and copy the app to /Applications.

```sh
mkdir -p ~/.speedread && echo "OPENROUTER_API_KEY=your-key" > ~/.speedread/.env
git clone https://github.com/TomySpagnoletti/speed-reading-app.git && cd speed-reading-app
npm install && npm run tauri dev
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README and screenshot: [github.com/TomySpagnoletti/speed-reading-app/blob/351b6190930389e19966d868d3e79159eeb82008/README.md](https://github.com/TomySpagnoletti/speed-reading-app/blob/351b6190930389e19966d868d3e79159eeb82008/README.md)

## Limits and data handling

Pasted text is sent to OpenRouter and TypeSafe for classification; text, notes and the call ledger stay in `~/.speedread/` on your Mac.

## Review and maintenance

Reviewed **2026-11-13** (Europe/Sofia) at [commit 351b61909303](https://github.com/TomySpagnoletti/speed-reading-app/tree/351b6190930389e19966d868d3e79159eeb82008). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
