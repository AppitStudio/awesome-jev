# Waterline by noah-thing (checks a link in a sealed browser before it goes on stream, with Jev confirming or clearing what the rules flag)

[All projects](../README.md) · [Web apps](README.md#web-apps)

Paste a link and Waterline opens it in a sealed headless Chromium, presses Play, mashes keys and fast-forwards timers, then reads every script and image it loads. Six depths of checks look for look-alike or brand-new domains, ClickFix commands, crypto miners, IP loggers, data-stealing webhooks and adult content (an on-device NSFW image model included). Rules find candidates; Jev gives a second opinion on each borderline frame, image and code match, and DeepSeek optionally reads the most suspicious script. Made for streamers who get sent games and links live.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/noah-thing/waterline) |
| Tags | `Open source` · `Free` · `BYOK` |
| Product homepage | [Product homepage](https://waterline.cc) |
| Pricing and access | Hosted site: paste a link and check it, with no sign-up or price shown (rate-limited). Self-hosting is a free MIT build where you pay for your own TypeSafe/DeepSeek calls. Checked 2026-11-17. |
| Jev evidence | [`engine/judge.mjs`](https://github.com/noah-thing/waterline/blob/634e7a47a30a4bb4da7f4a10ccc08b5d3e07e359/engine/judge.mjs) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Discovered via X ([post](https://x.com/fsconfig/status/2122423837015015481)). |
| Maintainer | [noah-thing](https://github.com/noah-thing). Independently curated. |
| Format | Web app (Node.js, Playwright; hosted at waterline.cc, MIT) |
| Platform and availability | Web (hosted at waterline.cc on Vercel); self-hostable Node.js server |
| Jev's role | Jev is the second opinion on every borderline frame, image and code match the rules flag, keeping false positives down. |
| Requirements | For self-hosting: Node 20+, Playwright's headless Chromium, `TYPESAFE_API_KEY` (recommended), optional DeepSeek and Google Safe Browsing keys. |
| License | [MIT](https://github.com/noah-thing/waterline/blob/634e7a47a30a4bb4da7f4a10ccc08b5d3e07e359/LICENSE) |

## When to use

- Check a game or link someone sent you before opening it on a live stream.
- Mismatch: a full malware sandbox or antivirus; it is a quick pre-stream check.

## How it works

`engine/judge.mjs` posts typed questions (with images when needed) to `https://api.typesafe.ai/v1/systemone` with `jev-latest` and uses the answers to confirm or clear flagged frames, images and code. Integration evidence: [`engine/judge.mjs`](https://github.com/noah-thing/waterline/blob/634e7a47a30a4bb4da7f4a10ccc08b5d3e07e359/engine/judge.mjs).

## Get started

Use the hosted site, or run it yourself with your keys.

```sh
git clone https://github.com/noah-thing/waterline && cd waterline
npm install && npx playwright install chromium-headless-shell
cp .env.example .env   # TYPESAFE_API_KEY=...
node server.mjs        # http://localhost:4321
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Live site: [waterline.cc](https://waterline.cc)
- README: [github.com/noah-thing/waterline/blob/634e7a47a30a4bb4da7f4a10ccc08b5d3e07e359/README.md](https://github.com/noah-thing/waterline/blob/634e7a47a30a4bb4da7f4a10ccc08b5d3e07e359/README.md)

## Limits and data handling

The hosted site visits submitted links on the maker's server and sends flagged frames, images and code to TypeSafe (and DeepSeek if set). Without keys it still runs the browser, rules and on-device image model. Detection quality is not independently measured.

## Review and maintenance

Reviewed **2026-11-17** (Europe/Sofia) at [commit 634e7a47a30a](https://github.com/noah-thing/waterline/tree/634e7a47a30a4bb4da7f4a10ccc08b5d3e07e359). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
