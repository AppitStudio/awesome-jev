# THE SWARM

[All projects](../README.md) · [Web apps](README.md#web-apps)

WebGL swarm of 1,000 light particles whose strategy (flee, attack, protect, split, regroup) is chosen live by TypeSafe Jev every 1.5 seconds or on events, while local rules move each particle.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/machine1986/the-swarm) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/machine1986/the-swarm#readme) (source-built; no separate product site verified). |
| Pricing and access | Free source build; you supply your own TypeSafe/provider keys and any hosting costs. Checked 2026-10-15. |
| Jev evidence | [`server/src/services/JevService.ts`](https://github.com/machine1986/the-swarm/blob/1df20db862e0aeeacad1b42a8ed7ffee23a5677b/server/src/services/JevService.ts) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [machine1986](https://github.com/machine1986). Independently curated. |
| Format | Web app (TypeScript, PixiJS v8, Vite, Node server) |
| Platform and availability | Web (local source build) |
| Jev's role | Jev picks the swarm's strategy in real time. |
| Requirements | Node.js 22.18+; TypeSafe API key optional (runs without one). |
| License | [Apache-2.0](https://github.com/machine1986/the-swarm/blob/1df20db862e0aeeacad1b42a8ed7ffee23a5677b/LICENSE) |

## When to use

- Watch a decision model steer a strategy layer over simple local rules.
- Use as a reference for server-side Jev calls in a realtime visual demo.
- Mismatch: German-language README; a demo, not a game with goals.

## How it works

The server sends the swarm's situation to Jev with typed questions and applies the chosen strategy; the 60 FPS particle simulation runs locally in the browser. Integration evidence: [`server/src/services/JevService.ts`](https://github.com/machine1986/the-swarm/blob/1df20db862e0aeeacad1b42a8ed7ffee23a5677b/server/src/services/JevService.ts).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/machine1986/the-swarm.git && cd the-swarm
npm install
cp .env.example .env   # TYPESAFE_API_KEY (optional)
npm run dev
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Performance notes in the upstream README.

## Limits and data handling

Swarm state goes to TypeSafe from the server on your key; no personal data is involved.

## Review and maintenance

Reviewed **2026-10-15** (Europe/Sofia) at [commit 1df20db862e0](https://github.com/machine1986/the-swarm/tree/1df20db862e0aeeacad1b42a8ed7ffee23a5677b). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
