# Tiny Bouncer

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Screens shell commands that LLM agents request in the OpenCode V2 harness: each command goes to TypeSafe Jev (default) for a judgment, and code thresholds turn the probabilities into allow, deny or the normal interactive prompt; it fails safe to asking and never grants permission your config denies.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/radupopescu/tiny-bouncer) |
| Maintainer | [radupopescu](https://github.com/radupopescu). Independently curated. |
| Format | Go CLI (`tinybouncer`, stdlib only) spawned by an OpenCode permission plugin |
| Requirements | Go ≥ 1.23 to build, OpenCode V2, and `TINY_BOUNCER_JEV_API_KEY` or `TYPESAFE_API_KEY`. |
| License | The reviewed tree has **no LICENSE file** — listed as Source available; reuse terms are not granted until the maintainer adds a license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Auto-approve clearly safe agent shell commands and block clearly dangerous ones.
- Evaluate the classifier on your own command set with `tinybouncer eval`.
- Mismatch: v0.1.0; upstream notes a manual smoke test still pending.

## How it works

The plugin batches shell commands per permission event and runs `tinybouncer check`; [`internal/backend/jev/client.go`](https://github.com/radupopescu/tiny-bouncer/blob/941306837209517b3bc8dcabb7095323efbd29d0/internal/backend/jev/client.go) calls Jev and [`route.go`](https://github.com/radupopescu/tiny-bouncer/blob/941306837209517b3bc8dcabb7095323efbd29d0/internal/backend/jev/route.go) applies thresholds calibrated on [`data/evalset.json`](https://github.com/radupopescu/tiny-bouncer/blob/941306837209517b3bc8dcabb7095323efbd29d0/data/evalset.json) (upstream gate: no false negatives). Design is in [`doc/architecture.md`](https://github.com/radupopescu/tiny-bouncer/blob/941306837209517b3bc8dcabb7095323efbd29d0/doc/architecture.md).

## Get started

Build and wire into OpenCode (README):

```sh
git clone https://github.com/radupopescu/tiny-bouncer && cd tiny-bouncer
make build   # bin/tinybouncer
export TYPESAFE_API_KEY=...
# then add the plugin to opencode.jsonc as shown in the README
```

Each permission event sends one Jev request (optional cache), billed by TypeSafe.

## Examples and demos

- README *How it works*.
- [Implementation plan](https://github.com/radupopescu/tiny-bouncer/blob/941306837209517b3bc8dcabb7095323efbd29d0/doc/plan.md).

## Limits and data handling

Proposed shell commands go to TypeSafe. No LICENSE file. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-08** (Europe/Sofia) at [commit 941306837209](https://github.com/radupopescu/tiny-bouncer/tree/941306837209517b3bc8dcabb7095323efbd29d0). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
