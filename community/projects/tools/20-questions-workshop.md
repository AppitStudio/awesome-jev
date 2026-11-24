# 20 Questions with Jev by Rhys Lindmark (hands-on workshop: build a 20 Questions player with Jev and race it against DeepSeek and Sonnet)

[All projects](../README.md) · [Games and simulation](README.md#games-and-simulation)

Leveled workshop teaching "Jev makes one judgment, code does the rest": each turn Jev picks the next yes/no question, while answering, crossing off candidates and guessing are plain code. Uses a fixed 100-noun × 35-question answer table that Jev filled once, and recorded races so it runs without keys.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Rhys-Lindmark/20-questions-workshop) |
| Maintainer | [Rhys Lindmark](https://github.com/Rhys-Lindmark). Independently curated. |
| Format | Node.js workshop (no dependencies) with a terminal race and a local web page |
| Requirements | Git and Node.js 22 or newer; a TypeSafe key to run Jev live (and an OpenRouter key to race the LLMs live). |
| License | [MIT](https://github.com/Rhys-Lindmark/20-questions-workshop/blob/70c20a8a31f1aff7468a0f9c9c1b958d2a4a16d9/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/lanes.js`](https://github.com/Rhys-Lindmark/20-questions-workshop/blob/70c20a8a31f1aff7468a0f9c9c1b958d2a4a16d9/src/lanes.js) at the pinned commit. |

## When to use

- Teach or learn how to split a task into one Jev judgment plus deterministic code.
- Mismatch: a production template; it is a teaching game.

## How it works

`src/lanes.js` posts the game state and a choice question to `https://api.typesafe.ai/v1/systemone`; LLM lanes go through OpenRouter for comparison. Integration evidence: [`src/lanes.js`](https://github.com/Rhys-Lindmark/20-questions-workshop/blob/70c20a8a31f1aff7468a0f9c9c1b958d2a4a16d9/src/lanes.js).

## Get started

Clone, run the doctor, then race on recorded answers before adding keys.

```sh
git clone https://github.com/Rhys-Lindmark/20-questions-workshop.git && cd 20-questions-workshop
npm run doctor
npm run play -- frog
npm run app   # http://localhost:3420
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Workshop levels and README: [github.com/Rhys-Lindmark/20-questions-workshop/blob/70c20a8a31f1aff7468a0f9c9c1b958d2a4a16d9/README.md](https://github.com/Rhys-Lindmark/20-questions-workshop/blob/70c20a8a31f1aff7468a0f9c9c1b958d2a4a16d9/README.md)

## Limits and data handling

Race results are the author's; 6% of the answer table was pinned by hand. Live mode sends game state to TypeSafe and OpenRouter.

## Review and maintenance

Reviewed **2026-11-25** (Europe/Sofia) at [commit 70c20a8a31f1](https://github.com/Rhys-Lindmark/20-questions-workshop/tree/70c20a8a31f1aff7468a0f9c9c1b958d2a4a16d9). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
