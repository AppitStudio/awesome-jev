# jev-relayer (Claude Code and Codex hook that routes each prompt through Jev to pick inline, subagent or sibling session plus model and effort)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Hook for Claude Code and Codex that asks a cheap Jev classifier, before the expensive model starts, whether the turn should stay inline, go to a subagent, or open a sibling background session, and which model and reasoning effort to use. It never blocks a prompt; sibling handoffs wait for your approval.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/mxttbennett/jev-relayer) |
| Maintainer | [mxttbennett](https://github.com/mxttbennett). Independently curated. |
| Format | Node.js / TypeScript hook package (MIT; started from psadventure/jev-model-router) |
| Requirements | Claude Code or Codex with hooks enabled, Node.js, and a `TYPESAFE_API_KEY` for the classifier (falls back to heuristics when no classifier answers). |
| License | [MIT](https://github.com/mxttbennett/jev-relayer/blob/c642a10b95e29e7213f7bf471bdb1542c7466c33/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`bin/jev-relayer.mjs`](https://github.com/mxttbennett/jev-relayer/blob/c642a10b95e29e7213f7bf471bdb1542c7466c33/bin/jev-relayer.mjs) at the pinned commit. |

## When to use

- Cut cost on easy turns by sending renames and quick questions to a cheaper model.
- Keep the main session clean by fanning audit-style work to a subagent or approved sibling session.
- Mismatch: without a TypeSafe key it uses heuristics; sibling sessions still need your approval.

## How it works

`bin/jev-relayer.mjs` and the hook registration read `TYPESAFE_API_KEY` from the environment and post typed routing questions to Jev; the printed line shows the verdict, model and classifier confidence. Integration evidence: [`bin/jev-relayer.mjs`](https://github.com/mxttbennett/jev-relayer/blob/c642a10b95e29e7213f7bf471bdb1542c7466c33/bin/jev-relayer.mjs).

## Get started

From the upstream README (not run on the review host):

```sh
# see upstream README for Claude Code / Codex hook install
export TYPESAFE_API_KEY=...
# then enable the jev-relayer hook so each prompt is classified before the turn runs
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/mxttbennett/jev-relayer/blob/c642a10b95e29e7213f7bf471bdb1542c7466c33/README.md](https://github.com/mxttbennett/jev-relayer/blob/c642a10b95e29e7213f7bf471bdb1542c7466c33/README.md)

## Limits and data handling

Prompt text used for routing is sent to TypeSafe on your key. The classifier never blocks work; when it fails the hook falls back to heuristics.

## Review and maintenance

Reviewed **2026-11-06** (Europe/Sofia) at [commit c642a10b95e2](https://github.com/mxttbennett/jev-relayer/tree/c642a10b95e29e7213f7bf471bdb1542c7466c33). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
