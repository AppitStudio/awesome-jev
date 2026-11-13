# Superopen (local code graph, session memory and playbook harvest for Claude Code, Cursor and Codex, with an optional Jev harvest gate)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Harness around existing coding agents: a Tree-sitter code graph in SQLite that agents query instead of grepping, background session hooks, a ~350-token distilled index for the next session, and Harvest, which proposes playbook patches from sessions; with Jev harvest on, Jev decides which finished session deserves a candidate patch.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ishanjainn/superopen) |
| Maintainer | [ishanjainn](https://github.com/ishanjainn). Independently curated. |
| Format | Go CLI with web UI and agent plugins (Apache-2.0) |
| Requirements | The `so` binary (Homebrew, install script or release), a supported coding agent, and a TypeSafe key only when `SUPEROPEN_HARVEST_JEV=1`. |
| License | [Apache-2.0](https://github.com/ishanjainn/superopen/blob/9661f41f576f3a0692ceef20a87c9e0e70f9a29c/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`internal/harvest/jev.go`](https://github.com/ishanjainn/superopen/blob/9661f41f576f3a0692ceef20a87c9e0e70f9a29c/internal/harvest/jev.go) at the pinned commit. |

## When to use

- Reduce token waste across coding-agent sessions and capture recurring human corrections as playbook guidance.
- Mismatch: if you want Jev in the core loop; it is only an optional Harvest gate.

## How it works

`internal/harvest/jev.go` posts the latest finished session to `https://api.typesafe.ai/v1/systemone`; a candidate is stored only when Jev says promote, evidence is at least 2.5 of 4 and the correction probability is at least 0.80 (`docs/harvest.md`). Jev does not write the playbook diff. The code graph, sessions and distill run locally without Jev. Integration evidence: [`internal/harvest/jev.go`](https://github.com/ishanjainn/superopen/blob/9661f41f576f3a0692ceef20a87c9e0e70f9a29c/internal/harvest/jev.go).

## Get started

Install the `so` binary, set up your agent and repository, then enable Jev harvest with the environment variables below.

```sh
brew install ishanjainn/superopen/so
so install
so init
export SUPEROPEN_HARVEST_JEV=1 TYPESAFE_API_KEY=...
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/ishanjainn/superopen/blob/9661f41f576f3a0692ceef20a87c9e0e70f9a29c/README.md](https://github.com/ishanjainn/superopen/blob/9661f41f576f3a0692ceef20a87c9e0e70f9a29c/README.md)
- Harvest docs: [github.com/ishanjainn/superopen/blob/9661f41f576f3a0692ceef20a87c9e0e70f9a29c/docs/harvest.md](https://github.com/ishanjainn/superopen/blob/9661f41f576f3a0692ceef20a87c9e0e70f9a29c/docs/harvest.md)

## Limits and data handling

With Jev harvest on, the task and human correction from the latest session go to TypeSafe on your key.

## Review and maintenance

Reviewed **2026-11-13** (Europe/Sofia) at [commit 9661f41f576f](https://github.com/ishanjainn/superopen/tree/9661f41f576f3a0692ceef20a87c9e0e70f9a29c). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
