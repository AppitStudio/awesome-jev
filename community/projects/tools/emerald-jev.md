# emerald-jev by aray03 (bot that plays Pokémon Emerald from New Game through the first gym, with Jev reading the screen)

[All projects](../README.md) · [Games and simulation](README.md#games-and-simulation)

Bot that plays Pokémon Emerald by itself in the BizHawk emulator, from New Game through the first gym (Roxanne in Rustboro), with later story goals toward the third gym still in progress. A Lua script reads game memory (map, position, battle state) and sends it with the screen frame to a local bridge server; the server asks Jev to read the screen and choose the next move, and the script presses the buttons. A dry-run mode logs memory while you play by hand.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/aray03/emerald-jev) |
| Maintainer | [aray03](https://github.com/aray03). Independently curated. |
| Format | Node.js bridge server and BizHawk Lua script (TypeScript; no license file) |
| Requirements | Linux with BizHawk 2.11.1 (Mono), Node.js, `TYPESAFE_API_KEY`, and your own Pokémon Emerald ROM. |
| License | No license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jev.ts`](https://github.com/aray03/emerald-jev/blob/348debbcb49749a2e771cafe6b7cba1568b8afad/src/jev.ts) at the pinned commit. |

## When to use

- Watch Jev play a long game from screen images and memory reads.
- Mismatch: speedrunning or a general game agent; its goals are scripted for Emerald.

## How it works

`src/jev.ts` uses the official `@typesafe-ai/sdk` `TypeSafeClient` to send the upscaled GBA frame and choice/noul questions (defined in `src/questions.ts`) to Jev, then returns the chosen move to the Lua script. Integration evidence: [`src/jev.ts`](https://github.com/aray03/emerald-jev/blob/348debbcb49749a2e771cafe6b7cba1568b8afad/src/jev.ts).

## Get started

Install BizHawk and the dependencies, add your key, start the bridge, then launch the emulator script.

```sh
git clone https://github.com/aray03/emerald-jev && cd emerald-jev
npm install
cp .env.example .env   # TYPESAFE_API_KEY=...
npm run dev            # bridge server on :3100
./play.sh              # in another terminal (ROM=... BIZHAWK=...)
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/aray03/emerald-jev/blob/348debbcb49749a2e771cafe6b7cba1568b8afad/README.md](https://github.com/aray03/emerald-jev/blob/348debbcb49749a2e771cafe6b7cba1568b8afad/README.md)

## Limits and data handling

Screen frames and game state go to TypeSafe on your key. You must supply your own ROM; none is included. No license file, so reuse terms are not granted.

## Review and maintenance

Reviewed **2026-11-17** (Europe/Sofia) at [commit 348debbcb497](https://github.com/aray03/emerald-jev/tree/348debbcb49749a2e771cafe6b7cba1568b8afad). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
