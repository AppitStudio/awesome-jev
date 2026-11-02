# jevellan-harness-skills (Claude Code skills that turn a session into a coordinator, with Jev choosing model, effort and provider per step)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Seventeen skills and plain Node scripts that turn a Claude Code session into a coordinator: requests become tasks, Jev picks the model, effort and provider for every step, each step runs as its own `claude -p` or `codex exec` session, results land through a guarded script, and an append-only ledger lets any session pick up. Installed by copying `skills/` and merging three hooks.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/gongiskhan/jevellan-harness-skills) |
| Maintainer | [gongiskhan](https://github.com/gongiskhan). Independently curated. |
| Format | Claude Code skills + Node scripts |
| Requirements | Node 22.13+, git, Claude Code (optionally Codex CLI), a TypeSafe key file. |
| License | [MIT](https://github.com/gongiskhan/jevellan-harness-skills/blob/155b2d5e7f7988b070c85d00cca4b29e7a167dda/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`skills/jevellan-router/scripts/jev.mjs`](https://github.com/gongiskhan/jevellan-harness-skills/blob/155b2d5e7f7988b070c85d00cca4b29e7a167dda/skills/jevellan-router/scripts/jev.mjs) at the pinned commit. |

## When to use

- Coordinate multi-step coding work across runtimes with a per-step model choice.
- Mismatch: needs your own provider accounts and tokens configured on disk.

## How it works

`skills/jevellan-router/scripts/jev.mjs` posts to TypeSafe `/v1/systemone` with a Bearer key read from the configured key file, retries on 429 and validates answers before the router uses them. Integration evidence: [`skills/jevellan-router/scripts/jev.mjs`](https://github.com/gongiskhan/jevellan-harness-skills/blob/155b2d5e7f7988b070c85d00cca4b29e7a167dda/skills/jevellan-router/scripts/jev.mjs).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/gongiskhan/jevellan-harness-skills
cp -r jevellan-harness-skills/skills/* your-project/.claude/skills/
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Example provider config: [github.com/gongiskhan/jevellan-harness-skills/blob/main/providers.example.json](https://github.com/gongiskhan/jevellan-harness-skills/blob/main/providers.example.json)

## Limits and data handling

Task descriptions are sent to TypeSafe for routing. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-02** (Europe/Sofia) at [commit 155b2d5e7f79](https://github.com/gongiskhan/jevellan-harness-skills/tree/155b2d5e7f7988b070c85d00cca4b29e7a167dda). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
