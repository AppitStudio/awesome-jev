# jev-minecraft

[All projects](../README.md) · [Web apps](README.md#web-apps)

Runnable demo (Chinese docs) in an open-source Minecraft-compatible world: each step sends the bot's position, inventory, nearby blocks, task progress and available options to TypeSafe Jev, Jev picks the next action, Mineflayer executes it and the real world is checked; tasks range from collecting logs and building a pillar to a 90-block camp, and you can join the same world from a browser player page.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/BHD110/jev-minecraft) |
| Tags | `Open source` · `Free` · `BYOK` |
| Product homepage | [Repository README](https://github.com/BHD110/jev-minecraft#readme) (self-hosted local web app). |
| Pricing and access | Free source build; Jev decisions need your own TypeSafe API key (entered in the page, kept in server memory). Checked 2026-10-08. |
| Jev evidence | [`camp-game.mjs`](https://github.com/BHD110/jev-minecraft/blob/054291de3413bd4eb3c062ac9ee67c17c22ebdda/camp-game.mjs) / [`game.mjs`](https://github.com/BHD110/jev-minecraft/blob/054291de3413bd4eb3c062ac9ee67c17c22ebdda/game.mjs) send typed options to Jev; recorded run in [`evidence/camp-verified-run.json`](https://github.com/BHD110/jev-minecraft/blob/054291de3413bd4eb3c062ac9ee67c17c22ebdda/evidence/camp-verified-run.json) (author-recorded). Source inspected at the pinned commit. |
| Disclosure | AI-assisted catalog review; no affiliation. Not commercial. Listing is not an endorsement. Live app not run on the review host. |
| Maintainer | [BHD110](https://github.com/BHD110). Independently curated. |
| Format | Node web app (`pnpm start`, `http://127.0.0.1:5192/`) |
| Platform and availability | Node.js 22+ and pnpm 10 on macOS, Linux or Windows; any browser. |
| Jev's role | Chooses the bot's next gathering/building step from program-provided options. |
| Requirements | Node.js 22+, pnpm 10; TypeSafe API key. |
| License | [MIT](https://github.com/BHD110/jev-minecraft/blob/054291de3413bd4eb3c062ac9ee67c17c22ebdda/LICENSE). |

## When to use

- Watch typed Jev decisions drive a game bot with exportable request/response logs.
- Mismatch: blueprint and materials are fixed by the program; Jev chooses order, not design.

## How it works

The server builds the world state and legal options each step, asks Jev a choice question and executes via Mineflayer; the UI shows probabilities and results.

## Get started

Run locally (README):

```sh
git clone https://github.com/BHD110/jev-minecraft.git && cd jev-minecraft
npm install -g pnpm@10.32.1
pnpm install --frozen-lockfile
pnpm start
```

Each decision is a Jev request on your key (README camp run: 32 decisions — author-reported).

## Examples and demos

- Verified runs under [`evidence/`](https://github.com/BHD110/jev-minecraft/blob/054291de3413bd4eb3c062ac9ee67c17c22ebdda/evidence/verified-run.json).

## Limits and data handling

Game state goes to TypeSafe. Binds to 127.0.0.1 by default. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-08** (Europe/Sofia) at [commit 054291de3413](https://github.com/BHD110/jev-minecraft/tree/054291de3413bd4eb3c062ac9ee67c17c22ebdda). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
