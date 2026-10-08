# defrag

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Research tool for telling a coding agent's user when compacting is safe — at the quiet point between tasks, not when the context is nearly full: it extracts checkpoints from real sessions, lets you label them, and replays them against judges with TypeSafe Jev as the first production judge (plus OpenAI Decisions, rules, a threshold proxy or a local model) to measure which one to ship.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/jaylamping/defrag) |
| Maintainer | [jaylamping](https://github.com/jaylamping). Independently curated. |
| Format | Local evaluation CLI (`node src/cli.js extract / review / predict`) |
| Requirements | Node.js 24+; session data from OpenCode (SQLite) or other supported agents; `TYPESAFE_API_KEY` for the Jev judge with explicit per-run outbound-data consent. |
| License | [MIT](https://github.com/jaylamping/defrag/blob/8061e26e53e40da7b8c18f7099fa49e122ffb5e6/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Build a labeled set of compaction checkpoints from your own agent history.
- Compare Jev with OpenAI Decisions or rules before trusting any default.
- Mismatch: status upstream — no live IDE adapters yet and no judge accuracy measured.

## How it works

[`src/jev.js`](https://github.com/jaylamping/defrag/blob/8061e26e53e40da7b8c18f7099fa49e122ffb5e6/src/jev.js) posts each checkpoint to `https://api.typesafe.ai/v1/systemone` (`jev-latest`) and returns a decision against a floor; outputs are written privately (0600) under ignored `eval/` directories and never overwritten.

## Get started

Run the checks and extract checkpoints (README):

```sh
git clone https://github.com/jaylamping/defrag.git && cd defrag
npm run check
node src/cli.js extract --db ~/.local/share/opencode/opencode.db --out eval/data/checkpoints.jsonl
```

Hosted judges (Jev, OpenAI Decisions) are billed by their providers and only run after explicit consent.

## Examples and demos

- README *1. Extract checkpoints*, *2. Review and label*, *3. Run predictions*.

## Limits and data handling

Checkpoint text from your sessions goes to TypeSafe only when you consent per run. Early research; no accuracy claims. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-08** (Europe/Sofia) at [commit 8061e26e53e4](https://github.com/jaylamping/defrag/tree/8061e26e53e40da7b8c18f7099fa49e122ffb5e6). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
