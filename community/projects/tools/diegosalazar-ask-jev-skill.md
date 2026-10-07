# ask-jev-skill (DiegoSalazar)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Claude Code skill plus a dependency-free Bun `jev` CLI (`yes`, `pick`, `rate`, `rank`, `triage`) that lets Claude offload cheap, repetitive judgments to TypeSafe Jev — which files to read, whether command output means pass or fail, which skill fits, filtering and ranking — so raw content stays out of Claude's context.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/DiegoSalazar/ask-jev-skill) |
| Maintainer | [DiegoSalazar](https://github.com/DiegoSalazar). Independently curated. |
| Format | Bun CLI `jev` and Claude Code skill installed by symlink (`install.sh`) |
| Requirements | Bun, Claude Code and a `TYPESAFE_API_KEY`. |
| License | The reviewed tree has **no LICENSE file** — listed as Source available; reuse terms are not granted until the maintainer adds a license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Save Claude tokens on repetitive judgments such as test-output triage or file selection.
- Rank candidates by keyed references rather than array positions.
- Mismatch: no LICENSE file; small, early project. Distinct from the separately listed [ask-jev-skill](ask-jev-skill.md) Hermes skill.

## How it works

[`src/jev.ts`](https://github.com/DiegoSalazar/ask-jev-skill/blob/bb6b104aa816163dbb39bcbab78770bd83af4518/src/jev.ts) is the API client (retries on 429/529, secret redaction, confidence-to-action thresholds, keyed ranking); [`bin/jev.ts`](https://github.com/DiegoSalazar/ask-jev-skill/blob/bb6b104aa816163dbb39bcbab78770bd83af4518/bin/jev.ts) exposes the commands Claude calls as described in the skill.

## Get started

Install the skill and CLI (README *Install*):

```sh
git clone https://github.com/DiegoSalazar/ask-jev-skill && cd ask-jev-skill
./install.sh
export TYPESAFE_API_KEY=...
```

Each `jev` command is a Jev request billed to your TypeSafe key.

## Examples and demos

- README *Install* and *Develop*.

## Limits and data handling

Text passed to the CLI (after redaction) goes to TypeSafe. No LICENSE file. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-08** (Europe/Sofia) at [commit bb6b104aa816](https://github.com/DiegoSalazar/ask-jev-skill/tree/bb6b104aa816163dbb39bcbab78770bd83af4518). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
