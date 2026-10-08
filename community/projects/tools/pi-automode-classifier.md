# pi-automode-classifier

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Auto mode for the Pi coding agent: built-in rules decide most tool calls, then a classifier model — hosted Jev (e.g. `openrouter` `typesafe/jev-1.13` through Pi's model registry) or local Kev / Laya on CPU via llama.cpp's `/v1/systemone` — scores unknown shell commands, and risky ones get a confirm prompt or are blocked.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/deepu105/pi-automode-classifier) |
| Maintainer | [deepu105](https://github.com/deepu105). Independently curated. |
| Format | Pi extension (`pi install npm:pi-automode-classifier`) |
| Requirements | Pi; either a Pi-registered decision model (Jev via TypeSafe/OpenRouter) or a llama.cpp server (Oct 2 2026+ build) with Kev-0.8B or Laya. |
| License | [MIT](https://github.com/deepu105/pi-automode-classifier/blob/5287bd10a35340d4ee2da3aef3756576f751f9e0/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Let Pi run safe commands unattended while risky ones still ask you.
- Keep classification fully offline with Kev or Laya on CPU.
- Mismatch: the author's 50-command bench found hosted Jev much better than local models (author-reported).

## How it works

[`index.ts`](https://github.com/deepu105/pi-automode-classifier/blob/5287bd10a35340d4ee2da3aef3756576f751f9e0/index.ts) applies [`rules.ts`](https://github.com/deepu105/pi-automode-classifier/blob/5287bd10a35340d4ee2da3aef3756576f751f9e0/rules.ts) first and asks the classifier the configured questions for unknown commands, comparing the probability with `askAbove`; [`bench.mjs`](https://github.com/deepu105/pi-automode-classifier/blob/5287bd10a35340d4ee2da3aef3756576f751f9e0/bench.mjs) replays [`bench-cases.json`](https://github.com/deepu105/pi-automode-classifier/blob/5287bd10a35340d4ee2da3aef3756576f751f9e0/bench-cases.json).

## Get started

Install into Pi (README *Install*):

```sh
pi install npm:pi-automode-classifier
# or
pi install git:github.com/deepu105/pi-automode-classifier
```

Hosted Jev calls bill your provider; local Kev/Laya is free.

## Examples and demos

- npm package: [`pi-automode-classifier`](https://www.npmjs.com/package/pi-automode-classifier) (0.1.0).
- README sample configs for Kev-0.8B, Laya and hosted Jev.

## Limits and data handling

With hosted Jev, commands are sent to the provider; local mode keeps them on the machine. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-08** (Europe/Sofia) at [commit 5287bd10a353](https://github.com/deepu105/pi-automode-classifier/tree/5287bd10a35340d4ee2da3aef3756576f751f9e0). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
