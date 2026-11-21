# Jevstice by Oleg Veschin (oh-my-pi extension where Jev records diagnostic verdicts on requirements, plans and finished work)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

An extension for the oh-my-pi (OMP) coding agent that sends the decisions it can see (requirements, plans, search candidates, acceptance claims, diffs, prose rules) to Jev as typed questions and records each verdict as a diagnostic, so you can leave cheaper models running and see afterwards what they missed. Thirteen `jev_*` tools plus `/jev` and `/jev-status`; verdicts never grant or block execution.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/veschin/jevstice) |
| Maintainer | [veschin](https://github.com/veschin). Independently curated. |
| Format | TypeScript OMP extension (Bun) |
| Requirements | Bun 1.1+, oh-my-pi, and a TypeSafe key (`TYPESAFE_API_KEY`, or a command in `TYPESAFE_API_KEY_COMMAND`). |
| License | [MIT](https://github.com/veschin/jevstice/blob/5708dfadb412b400b000e5afc2c40fb703e7426a/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Discovered via X ([post](https://x.com/veschindev/status/2123890069023097118)). |
| Jev evidence | [`src/judge.ts`](https://github.com/veschin/jevstice/blob/5708dfadb412b400b000e5afc2c40fb703e7426a/src/judge.ts) at the pinned commit. |

## When to use

- Add an independent, cheap Jev check on requirements, plans and acceptance claims while a cheaper coding model works unattended in oh-my-pi.
- Mismatch: you want a permission gate that blocks tool calls; Jevstice only records diagnostics by design.

## How it works

`src/judge.ts` defines the System One client (`jev-latest` via the TypeSafe API) that the tools use; the controller in `src/gates.ts` classifies each visible tool call with deterministic effect classifiers and records Jev's typed verdict. A missing or rejected key produces an unavailable judgment instead of stopping the host; `/jev-status` reports checks, outcomes and estimated spend. Integration evidence: [`src/judge.ts`](https://github.com/veschin/jevstice/blob/5708dfadb412b400b000e5afc2c40fb703e7426a/src/judge.ts).

## Get started

Clone the extension into OMP's extensions folder, provide the key and restart OMP.

```sh
git clone https://github.com/veschin/jevstice.git ~/.omp/agent/extensions/jevstice
export TYPESAFE_API_KEY=...
# restart omp; /jev-status shows checks and spend
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Project site: [veschin.github.io/jevstice/](https://veschin.github.io/jevstice/)
- README: [github.com/veschin/jevstice/blob/5708dfadb412b400b000e5afc2c40fb703e7426a/README.md](https://github.com/veschin/jevstice/blob/5708dfadb412b400b000e5afc2c40fb703e7426a/README.md)
- Launch thread on X: [x.com/veschindev/status/2123890069023097118](https://x.com/veschindev/status/2123890069023097118)

## Limits and data handling

Requirements, plans, diffs and the other submitted context are sent to TypeSafe for each check, with per-call cost. Fast-moving project (v2.3.1 at review); an earlier checkout was a replacement MVP.

## Review and maintenance

Reviewed **2026-11-21** (Europe/Sofia) at [commit 5708dfadb412](https://github.com/veschin/jevstice/tree/5708dfadb412b400b000e5afc2c40fb703e7426a). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
