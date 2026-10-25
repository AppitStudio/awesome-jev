# BOOLS (Breakout played live by Jev in the browser)

[All projects](../README.md) · [Web apps](README.md#web-apps)

Browser Breakout game where a System One decision model steers the paddle: while the ball falls the page sends its state and one Choice question over eight zones, and the paddle moves to the pick; on-screen stats show latency, accuracy by distance and per-zone probabilities.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/neovibrant/BOOLS) |
| Tags | `Open source` · `Free` · `BYOK` |
| Product homepage | [Product homepage](https://bools.iteratory.com) |
| Pricing and access | Open source (MIT); free to play. Decisions are billed to your own Requesty or provider key (about 400 input tokens each, a few per second). Checked 2026-10-25. |
| Jev evidence | [`public/index.html`](https://github.com/neovibrant/BOOLS/blob/c5ee4a06e0890e08ff6d35cc988b63839a78f776/public/index.html) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [neovibrant](https://github.com/neovibrant). Independently curated. |
| Format | Static web page (plain JavaScript) |
| Platform and availability | Web, at bools.iteratory.com; or run the single `public/index.html` locally. |
| Jev's role | Core: every paddle move comes from the model's answer; the game never predicts the ball itself. Default model `typesafe/jev-latest` through Requesty. |
| Requirements | A modern browser and a Requesty API key (or any OpenAI-compatible decision-model endpoint). |
| License | [MIT](https://github.com/neovibrant/BOOLS/blob/c5ee4a06e0890e08ff6d35cc988b63839a78f776/LICENSE) |

## When to use

- See how fast and how accurate Jev is when it has to answer several times a second.
- Compare decision models on the same live task with on-screen latency and accuracy stats.
- Mismatch: costs accrue quickly while playing; use a key with a spending limit.

## How it works

`public/index.html` posts the ball, paddle and field state with one Choice question to the configured endpoint (default `https://router.requesty.ai/v1`, model `typesafe/jev-latest`) and moves the paddle toward the chosen zone. Integration evidence: [`public/index.html`](https://github.com/neovibrant/BOOLS/blob/c5ee4a06e0890e08ff6d35cc988b63839a78f776/public/index.html).

## Get started

From the upstream README (not run on the review host): open the site, paste a Requesty key and press Play, or run it locally:

```sh
# https://bools.iteratory.com
npx wrangler dev   # or any static server for public/
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Play: [bools.iteratory.com](https://bools.iteratory.com)
- Design notes: [github.com/neovibrant/BOOLS/blob/main/instructions.md](https://github.com/neovibrant/BOOLS/blob/main/instructions.md)

## Limits and data handling

Game state goes to the API URL you enter. The key stays in the browser's localStorage and there is no backend.

## Review and maintenance

Reviewed **2026-10-25** (Europe/Sofia) at [commit c5ee4a06e089](https://github.com/neovibrant/BOOLS/tree/c5ee4a06e0890e08ff6d35cc988b63839a78f776). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
