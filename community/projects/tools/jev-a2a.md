# jev-a2a (Jev router for Paseo agents)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Personal-prototype router that sends work between coding agents running in Paseo sessions on several machines and keeps one record of what was asked, who took it and what came back; when a request names no recipient, TypeSafe Jev chooses the participant. Includes a web board and design docs; published as a worked example, not a product.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/skhlo/jev-a2a) |
| Maintainer | [skhlo](https://github.com/skhlo). Independently curated. |
| Format | Node 26 TypeScript service (`router` CLI + `serve`) with a Paseo plugin board |
| Requirements | Node 26, pnpm, a Paseo daemon with at least one agent; Tailscale Serve for the board's login header; a `TYPESAFE_API_KEY` only for requests without a recipient. |
| License | [MIT](https://github.com/skhlo/jev-a2a/blob/be778392e374f3c79fa541c1828c1de0fd09f41a/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Coordinate several agents on several hosts without re-typing context into each session.
- Study a documented design for agent-to-agent prompt delivery with ownership rules.
- Mismatch: upstream states no releases, no support, and contracts can change between commits.

## How it works

`router submit` records the request; without `--to`, [`router/src/jev.ts`](https://github.com/skhlo/jev-a2a/blob/be778392e374f3c79fa541c1828c1de0fd09f41a/router/src/jev.ts) asks Jev to choose among participants the sender may address, then [`paseo.ts`](https://github.com/skhlo/jev-a2a/blob/be778392e374f3c79fa541c1828c1de0fd09f41a/router/src/paseo.ts) delivers the prompt when the target session is idle. Design: [`docs/research/jev-router-spec.md`](https://github.com/skhlo/jev-a2a/blob/be778392e374f3c79fa541c1828c1de0fd09f41a/docs/research/jev-router-spec.md).

## Get started

Quick start on the router host (README):

```sh
git clone https://github.com/skhlo/jev-a2a && cd jev-a2a/router
pnpm install
mkdir -p ~/.config/jev-router && cp config.example.json ~/.config/jev-router/config.json
router submit "Is this machine current with merged main of the dotfiles baseline?"
```

Jev is called only for requests that name no recipient, billed to your TypeSafe key.

## Examples and demos

- README board GIF (sample record replay) and command table.
- Operating guide: [`docs/operating.md`](https://github.com/skhlo/jev-a2a/blob/be778392e374f3c79fa541c1828c1de0fd09f41a/docs/operating.md).

## Limits and data handling

Request text and participant descriptions go to TypeSafe for routing. Host tokens let agents on one host act as each other (README *Limits*). Not run on the review host.

## Review and maintenance

Reviewed **2026-10-07** (Europe/Sofia) at [commit be778392e374](https://github.com/skhlo/jev-a2a/tree/be778392e374f3c79fa541c1828c1de0fd09f41a). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
