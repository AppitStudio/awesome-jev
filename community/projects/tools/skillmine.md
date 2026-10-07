# skillmine

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Mines coding-agent sessions (Claude Code, Codex CLI, Kimi CLI, OpenCode, Antigravity) for reusable knowledge: local embeddings cluster near-duplicate windows, TypeSafe Jev (or Laya / Haiku) gates whether a cluster taught something reusable, and a planner model writes skills or runbooks with provenance and one-command undo.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/flaviomartil/skillmine) |
| Maintainer | [flaviomartil](https://github.com/flaviomartil). Independently curated. |
| Format | Bun CLI (`skillmine`) and Claude Code plugin marketplace (`/plugin install skillmine@skillmine`) |
| Requirements | Bun; Ollama with `nomic-embed-text` for embeddings (or `--embed none`); a `TYPESAFE_API_KEY` for the `jev` classifier (or a local laya-server / `claude -p`); a planner CLI (Claude, Codex, Antigravity, Kimi or OpenCode) for real edits. |
| License | [MIT](https://github.com/flaviomartil/skillmine/blob/980245d29379e2e92414c490260971f3cfb7f5e9/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Capture gotchas and procedures a coding agent learned in past sessions as reusable skills.
- Run `mine --dry --classify jev --max-calls 40` to see which session clusters Jev flags before anything is written.
- Mismatch: early-stage (upstream status phase 4); the planner, not Jev, decides what is written.

## How it works

[`src/classify/jev.ts`](https://github.com/flaviomartil/skillmine/blob/980245d29379e2e92414c490260971f3cfb7f5e9/src/classify/jev.ts) sends cluster digests with the questions in [`questions.ts`](https://github.com/flaviomartil/skillmine/blob/980245d29379e2e92414c490260971f3cfb7f5e9/src/classify/questions.ts) to Jev. Clusters that pass go to the planner, whose typed edits are validated in [`src/apply/validate.ts`](https://github.com/flaviomartil/skillmine/blob/980245d29379e2e92414c490260971f3cfb7f5e9/src/apply/validate.ts), snapshotted and logged to a ledger before landing; `undo` reverts them.

## Get started

Dry-run with Jev as the classifier (README *Try it*):

```sh
git clone https://github.com/flaviomartil/skillmine && cd skillmine
bun install
ollama pull nomic-embed-text
export TYPESAFE_API_KEY=...
bun run src/cli.ts mine --days 3 --dry --classify jev --max-calls 40
```

Each classified cluster is one Jev request billed to your TypeSafe key (`--max-calls` caps them); planner runs use your coding agent's own billing.

## Examples and demos

- README *Try it* and *Mine for real* (dry run, ledger, undo).
- Design: [`SPEC.md`](https://github.com/flaviomartil/skillmine/blob/980245d29379e2e92414c490260971f3cfb7f5e9/SPEC.md).

## Limits and data handling

Session digests (from your local agent transcripts) go to TypeSafe when the `jev` classifier is used; embeddings run locally. Edits change files under `.agents/skills` and `~/.agents/skills`; backups and a ledger live in `~/.skillmine`. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-08** (Europe/Sofia) at [commit 980245d29379](https://github.com/flaviomartil/skillmine/tree/980245d29379e2e92414c490260971f3cfb7f5e9). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
