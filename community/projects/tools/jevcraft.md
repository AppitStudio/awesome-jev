# jevcraft

[All projects](../README.md) · [Games and simulation](README.md#games-and-simulation)

Minecraft bot where code lists the actions it can really take and TypeSafe Jev picks one from that menu, with the project's own run statistics documented.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/mrubens/jevcraft) |
| Maintainer | [mrubens](https://github.com/mrubens). Independently curated. |
| Format | Mineflayer-style Minecraft bot (Node.js) |
| Requirements | Node.js, a Minecraft Java server you run, TypeSafe API key. |
| License | [MIT](https://github.com/mrubens/jevcraft/blob/f52eddfd35ee61a022faebf65a8c73cd3d16eb0f/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/typesafe.js`](https://github.com/mrubens/jevcraft/blob/f52eddfd35ee61a022faebf65a8c73cd3d16eb0f/src/typesafe.js) at the pinned commit. |

## When to use

- Study a long-running game agent where Jev only chooses among code-offered options.
- Learn from published failure notes and how they became tests.
- Mismatch: has not beaten the game; results are the maintainer's own counts.

## How it works

Code builds the option list (fight, retreat, take cover, eat, keep working, …) with descriptions; Jev returns a probability per option and code executes the choice. A hard rule in code protects chickens and pigs. Integration evidence: [`src/typesafe.js`](https://github.com/mrubens/jevcraft/blob/f52eddfd35ee61a022faebf65a8c73cd3d16eb0f/src/typesafe.js).

## Get started

From the upstream README (not run on the review host):

```sh
npm install
cp .env.example .env   # set MC_HOST, MC_PORT and your TypeSafe key
npm start
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Clips and status in the upstream README (e.g. 15 of 40 fresh worlds reached the Nether on 2026-09-28, as reported by the maintainer).
- Decision catalog: `docs/decisions.md`.

## Limits and data handling

Game state descriptions go to TypeSafe. Cost and speed figures are maintainer-reported, not reproduced here.

## Review and maintenance

Reviewed **2026-10-14** (Europe/Sofia) at [commit f52eddfd35ee](https://github.com/mrubens/jevcraft/tree/f52eddfd35ee61a022faebf65a8c73cd3d16eb0f). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
