# forge (continuous engineering loop)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Claude Code plugin that applies the autoresearch ratchet (one change, one commit, one measurement, keep or reset) inside a team-style process — spec, mapped scope, clarifying questions, tests beyond the happy path and human sign-off — with small tasks run through a test-driven harness and large ones driven to a measurable goal by an orchestrator, parallel subagents and a deterministic judge; Claude does the work while Jev makes cheap judgments such as triage, model routing and failure labelling.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/sudikama/forge) |
| Maintainer | [sudikama](https://github.com/sudikama). Independently curated. |
| Format | Claude Code plugin (`forge@forge-local`) |
| Requirements | Claude Code 2.1.280+, Node 20+, git; a Jev lane (TypeSafe key gives calibrated confidence; other lanes configurable). |
| License | [MIT](https://github.com/sudikama/forge/blob/f006565617e88a50e28ec89af73213ccca58111b/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Run unattended improvement loops with explicit sign-off gates.
- Mismatch: heavy process for tiny edits.

## How it works

[`lib/triage.mjs`](https://github.com/sudikama/forge/blob/f006565617e88a50e28ec89af73213ccca58111b/lib/triage.mjs) and [`lib/route.mjs`](https://github.com/sudikama/forge/blob/f006565617e88a50e28ec89af73213ccca58111b/lib/route.mjs) ask Jev via [`lib/jev.mjs`](https://github.com/sudikama/forge/blob/f006565617e88a50e28ec89af73213ccca58111b/lib/jev.mjs) with lane failover in [`lib/lanes.mjs`](https://github.com/sudikama/forge/blob/f006565617e88a50e28ec89af73213ccca58111b/lib/lanes.mjs); [`lib/judge.mjs`](https://github.com/sudikama/forge/blob/f006565617e88a50e28ec89af73213ccca58111b/lib/judge.mjs) is the deterministic judge.

## Get started

Install as a local plugin (README):

```sh
claude plugin marketplace add sudikama/forge
claude plugin install forge@forge-local
```

Claude usage plus Jev lane usage per your configured keys.

## Examples and demos

- Templates: [`templates/spec.md`](https://github.com/sudikama/forge/blob/f006565617e88a50e28ec89af73213ccca58111b/templates/spec.md).

## Limits and data handling

Task text goes to the configured Jev lane provider. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-08** (Europe/Sofia) at [commit f006565617e8](https://github.com/sudikama/forge/tree/f006565617e88a50e28ec89af73213ccca58111b). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
