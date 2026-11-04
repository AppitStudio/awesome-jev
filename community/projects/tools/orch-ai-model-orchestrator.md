# AI Model Orchestrator (local Go CLI where Jev, or an AI CLI, estimates which workflow stages a coding task needs)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Local Go CLI that takes one engineering task, decides which workflow stages it needs, and runs them by calling installed `claude`, `codex` or `gemini` CLIs in your git repository, with real test runs and run state on disk. A decision provider, the Jev API or one of the CLIs, only estimates probabilities such as task clarity, complexity and the need for research, investigation, development, testing or review; Go code applies thresholds and a deterministic state machine drives the stages. A mock Jev runs offline. License is PolyForm Noncommercial.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/kasorse/orch) |
| Maintainer | [kasorse](https://github.com/kasorse). Independently curated. |
| Format | Go CLI (PolyForm Noncommercial source) |
| Requirements | Go 1.26.1+, git, the AI CLIs you configure, bubblewrap for the default sandbox on Linux, and `JEV_API_KEY` for the real Jev provider. |
| License | [PolyForm Noncommercial 1.0.0](https://github.com/kasorse/orch/blob/302cf31496e222df352b3c19973f6d518a8ff00b/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`internal/decision/jev/client.go`](https://github.com/kasorse/orch/blob/302cf31496e222df352b3c19973f6d518a8ff00b/internal/decision/jev/client.go) at the pinned commit. |

## When to use

- Study a coding-agent workflow where a Jev classification picks stages and code, not a model, decides what happens next.
- Mismatch: the license is noncommercial source-available, the Claude CLI version range is narrow, and the Jev client was reviewed from source only.

## How it works

`internal/decision/jev/client.go` posts the task text and optional project context summaries to `{base_url}/v1/systemone` (default `https://api.typesafe.ai`, config model `jev-1.13.0`), keeping the wire format private to the package. Integration evidence: [`internal/decision/jev/client.go`](https://github.com/kasorse/orch/blob/302cf31496e222df352b3c19973f6d518a8ff00b/internal/decision/jev/client.go).

## Get started

From the upstream README (not run on the review host):

```sh
go build -o orchestrator ./cmd/orchestrator
# set decision.provider: jev and JEV_API_KEY in the config, or decision.jev.mock: true
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README with configuration and the section on what is sent to Jev: [github.com/kasorse/orch#readme](https://github.com/kasorse/orch#readme)

## Limits and data handling

With the real Jev provider, the task text and path, summary and rule context (never file contents beyond summaries, nor files on its deny list) go to TypeSafe on your key; the README notes zero data retention is enterprise-only. License terms forbid commercial use. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-04** (Europe/Sofia) at [commit 302cf31496e2](https://github.com/kasorse/orch/tree/302cf31496e222df352b3c19973f6d518a8ff00b). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
