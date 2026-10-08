# gutfeel

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Usability testing for MCP servers: a participant that doesn't deliberate — TypeSafe Jev by default — walks your tools on realistic, hint-free missions, and gutfeel draws the tree of every path (right tool, wrong turn, dead end, error, loop) with the description sentence behind each failure; pre-alpha, with `gutfeel live` runnable today.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/huayaney-exe/gutfeel) |
| Maintainer | [huayaney-exe](https://github.com/huayaney-exe). Independently curated. |
| Format | `gutfeel live` localhost viewer (`bun packages/live/server.ts`); the `npx gutfeel` CLI is planned |
| Requirements | Bun; `TYPESAFE_API_KEY` (direct) or `OPENROUTER_API_KEY` for Jev; a run folder (`surface.json`, `missions.json`, `protocol.json`); a sandbox MCP environment. |
| License | [MIT](https://github.com/huayaney-exe/gutfeel/blob/8165ca6bf59e70745b97489e25087aa430197fd5/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Find tool descriptions that send agents down the wrong path before users hit them.
- Replay a recorded run for a demo without a key.
- Mismatch: live walks really call your tools — never point it at production.

## How it works

[`packages/live/engine.ts`](https://github.com/huayaney-exe/gutfeel/blob/8165ca6bf59e70745b97489e25087aa430197fd5/packages/live/engine.ts) renders what the participant sees and asks Jev (TypeSafe `jev-latest` or OpenRouter `~typesafe/jev-latest`) to pick the next tool; [`walk.ts`](https://github.com/huayaney-exe/gutfeel/blob/8165ca6bf59e70745b97489e25087aa430197fd5/packages/live/walk.ts) executes and judges each step. The design for the full pipeline is in [`docs/DESIGN.md`](https://github.com/huayaney-exe/gutfeel/blob/8165ca6bf59e70745b97489e25087aa430197fd5/docs/DESIGN.md).

## Get started

Run the live viewer against a run folder (packages/live README):

```sh
git clone https://github.com/huayaney-exe/gutfeel.git && cd gutfeel
TYPESAFE_API_KEY=... bun packages/live/server.ts --dir <run folder> --open
# no key: replays events.jsonl from the folder
```

Live walks make Jev calls billed by TypeSafe or OpenRouter.

## Examples and demos

- [`packages/live/README.md`](https://github.com/huayaney-exe/gutfeel/blob/8165ca6bf59e70745b97489e25087aa430197fd5/packages/live/README.md).
- README *The tree* and *Findings you can act on* (target interface).

## Limits and data handling

Tool descriptions, missions and tool results go to the Jev provider; live mode executes real tool calls. Most of the README describes the planned CLI, not yet runnable. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-08** (Europe/Sofia) at [commit 8165ca6bf59e](https://github.com/huayaney-exe/gutfeel/tree/8165ca6bf59e70745b97489e25087aa430197fd5). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
