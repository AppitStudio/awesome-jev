# Uncle Gerd's Graveyard of Dead Side Projects by Jens Martsch (pixel-art graveyard of your stale GitHub repos where Jev judges revival odds)

[All projects](../README.md) · [Web apps](README.md#web-apps)

A personal agent on a Fly.io Sprite that finds your GitHub repos with no push in a year and turns them into tombstones in a walkable pixel-art graveyard or museum. Jev judges revival odds, whether it's worth it, and Uncle Gerd's mood; an LLM writes his lines; Claude Code can try to revive a project on its own Sprite. Built for Hacksgiving 2026.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/jmartsch/uncle-gerds-graveyard-of-dead-side-projects) |
| Tags | `Source available` · `Free` · `BYOK` |
| Product homepage | [Product homepage](https://ugm-museum-3nrx.sprites.app) |
| Pricing and access | Free to visit the hosted museum and to run from source; self-hosting uses your own Fly.io Sprites, GitHub, TypeSafe, Ollama Cloud and Anthropic accounts. Checked 2026-11-24. |
| Jev evidence | [`lib/jev.js`](https://github.com/jmartsch/uncle-gerds-graveyard-of-dead-side-projects/blob/e4c4c06ae5d2a114f5429f6b41c3302c85f23acd/lib/jev.js) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [jmartsch](https://github.com/jmartsch). Independently curated. |
| Format | Node.js web app (Phaser front end) |
| Platform and availability | Hosted web app on Fly.io Sprites; local demo with `npm run dev`. |
| Jev's role | Jev answers typed questions per repo (revivable and worth-it Nouls, a mood Choice) that drive the plaque tone and which projects get revival attempts. |
| Requirements | Node.js; for real scans a GitHub token and optionally TypeSafe and Ollama keys; deployment needs Fly.io Sprites connectors. |
| License | No license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |

## When to use

- A fun way to review abandoned side projects, with Jev deciding which are worth reviving.
- Mismatch: a serious portfolio audit tool.

## How it works

`lib/jev.js` posts repo state and questions to TypeSafe's `/v1/systemone` through the Sprites gateway connector (or `https://api.typesafe.ai` directly when run locally). Integration evidence: [`lib/jev.js`](https://github.com/jmartsch/uncle-gerds-graveyard-of-dead-side-projects/blob/e4c4c06ae5d2a114f5429f6b41c3302c85f23acd/lib/jev.js).

## Get started

Visit the hosted museum and type a GitHub username, or run the local demo.

```sh
git clone https://github.com/jmartsch/uncle-gerds-graveyard-of-dead-side-projects.git && cd uncle-gerds-graveyard-of-dead-side-projects
npm install
npm run dev   # http://localhost:8080
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Hosted museum: [ugm-museum-3nrx.sprites.app](https://ugm-museum-3nrx.sprites.app)
- Hacksgiving 2026: [fly.io/hacksgiving/](https://fly.io/hacksgiving/)

## Limits and data handling

Public repo READMEs, commits and issues are sent to TypeSafe and Ollama; revivals run Claude Code on new Sprites. No license file, so no reuse terms are granted.

## Review and maintenance

Reviewed **2026-11-24** (Europe/Sofia) at [commit e4c4c06ae5d2](https://github.com/jmartsch/uncle-gerds-graveyard-of-dead-side-projects/tree/e4c4c06ae5d2a114f5429f6b41c3302c85f23acd). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
