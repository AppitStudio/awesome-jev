# craft-cli

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Unofficial local-first CLI and TypeScript library for Craft Docs, with an agent skills library stored in Craft; `craft lib pick --jev` can use TypeSafe Jev to choose which skills fit a request.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/pa1ar/craft-cli) |
| Maintainer | [pa1ar](https://github.com/pa1ar). Independently curated. |
| Format | Bun single-binary CLI + TypeScript library |
| Requirements | Bun; Craft Docs account/API access; optional `JEV_API_KEY` or `TYPESAFE_API_KEY` for Jev skill picking. |
| License | [MIT](https://github.com/pa1ar/craft-cli/blob/f6ac032f3247f272a2c3aeaeaffa29a6ea11a7ad/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Discovered via X ([post](https://x.com/pa1ar/status/2111851998945374588)). |
| Jev evidence | [`src/lib/skill-picker.ts`](https://github.com/pa1ar/craft-cli/blob/f6ac032f3247f272a2c3aeaeaffa29a6ea11a7ad/src/lib/skill-picker.ts) at the pinned commit. |

## When to use

- Keep agent skills in a Craft collection and load only the relevant ones per request.
- Want an optional Jev selector with keyword fallback and a token budget.
- Mismatch: Craft Docs users only; Jev is optional, not the core of the CLI.

## How it works

`src/lib/skill-picker.ts` selects skills by keywords or, with `--jev`, sends skill metadata and the request to TypeSafe Jev to pick matches, falling back to keywords when asked. `craft lib hook` wires the picker into Codex or Claude Code sessions. The repo also publishes Jev retrieval experiments under `experiments/jev-retrieval`. Integration evidence: [`src/lib/skill-picker.ts`](https://github.com/pa1ar/craft-cli/blob/f6ac032f3247f272a2c3aeaeaffa29a6ea11a7ad/src/lib/skill-picker.ts).

## Get started

From the upstream README: install from the latest stable release (the README includes an agent-run install prompt), authenticate with Craft, then set up a skills library and pick with `--jev`.

```sh
# after installing per README
craft lib setup --document ID --collection ID
craft lib pick "request" --published --max-output 5 --jev --json
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- docs/jev-retrieval-experiments-2026-09-27.md
- docs/benchmarks/2026-09-27-jev-retrieval.json

## Limits and data handling

With `--jev`, skill metadata and your request go to TypeSafe. Not affiliated with Craft Docs. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-19** (Europe/Sofia) at [commit f6ac032f3247](https://github.com/pa1ar/craft-cli/tree/f6ac032f3247f272a2c3aeaeaffa29a6ea11a7ad). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
