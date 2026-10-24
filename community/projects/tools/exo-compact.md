# exo-compact (fast Claude Code compaction, with an optional Jev rule check)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Claude Code plugin (beta) that compacts in about a second instead of a minute, quotes your rules word for word and keeps the whole session searchable on disk; an optional Jev rule check, off by default, asks TypeSafe's Jev which of your task's rules each reply breaks.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/MarcinSufa/exo-compact) |
| Maintainer | [MarcinSufa](https://github.com/MarcinSufa). Independently curated. |
| Format | Claude Code plugin (TypeScript) |
| Requirements | Claude Code 2.1.278+ and Node.js 22.15+; a TypeSafe API key only for the optional rule check. |
| License | [MIT](https://github.com/MarcinSufa/exo-compact/blob/833e95760eeae6116ee59f5fa42a6a2aa43f89d2/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`plugin/compact/host/jev-client.ts`](https://github.com/MarcinSufa/exo-compact/blob/833e95760eeae6116ee59f5fa42a6a2aa43f89d2/plugin/compact/host/jev-client.ts) at the pinned commit. |

## When to use

- Keep one Claude Code session working for days without losing rules or task state.
- Add a cheap rule check on replies when you set a TypeSafe key.
- Mismatch: compaction itself makes no model call; Jev is only used for the opt-in rule check.

## How it works

`plugin/compact/host/jev-client.ts` posts rule-check questions to `https://api.typesafe.ai/v1/systemone` (`jev-latest` by default); `EXO_JEV_URL` can point at a Jev-compatible server of your own (experimental). Integration evidence: [`plugin/compact/host/jev-client.ts`](https://github.com/MarcinSufa/exo-compact/blob/833e95760eeae6116ee59f5fa42a6a2aa43f89d2/plugin/compact/host/jev-client.ts).

## Get started

From the upstream README (not run on the review host):

```sh
/plugin marketplace add MarcinSufa/exo-compact
/plugin install exo-compact@exo-compact
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README with A/B results: [github.com/MarcinSufa/exo-compact#readme](https://github.com/MarcinSufa/exo-compact#readme)
- Install guide: [github.com/MarcinSufa/exo-compact/blob/main/docs/install.md](https://github.com/MarcinSufa/exo-compact/blob/main/docs/install.md)

## Limits and data handling

With the rule check on, replies and rules go to TypeSafe. The capture store stays on your machine with keys redacted. Results are the author's own.

## Review and maintenance

Reviewed **2026-10-25** (Europe/Sofia) at [commit 833e95760eea](https://github.com/MarcinSufa/exo-compact/tree/833e95760eeae6116ee59f5fa42a6a2aa43f89d2). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
