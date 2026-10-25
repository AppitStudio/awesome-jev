# cake-safety-judge (command-safety gate for the Cake agent, with an optional Jev fast-approval cascade)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Standalone Go gate for the Cake coding agent's `cake-gate/1` protocol: it judges each proposed shell command with an LLM rubric and strict verdict parsing, and in cascade mode a Jev probability of at least 0.85 approves clearly safe commands quickly while everything else falls back to the judge; offline fake and record providers for tests.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/travisennis/cake-safety-judge) |
| Maintainer | [travisennis](https://github.com/travisennis). Independently curated. |
| Format | Go binary (CLI and gate process) |
| Requirements | Go and just to build; an OpenAI-compatible judge model; `TYPESAFE_AI_API_KEY` for the optional Jev cascade. |
| License | [MIT](https://github.com/travisennis/cake-safety-judge/blob/3336ab735a215938df5868d58542b483f40ab244/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`internal/typesafe/typesafe.go`](https://github.com/travisennis/cake-safety-judge/blob/3336ab735a215938df5868d58542b483f40ab244/internal/typesafe/typesafe.go) at the pinned commit. |

## When to use

- Gate an agent's shell commands outside the agent process.
- Cut judge latency and cost for routine commands with a fixed Jev fast-approval cutoff.
- Mismatch: built for Cake's protocol and not yet Cake's default gate.

## How it works

`internal/typesafe/typesafe.go` sends the command, working directory and reason to `https://api.typesafe.ai/v1/systemone` (default `jev-1.13.0`) as an observation; `typesafe.mode` is `off` by default, `shadow` records only, and `cascade` treats a clean probability at or above the compiled 0.85 cutoff as approval. Integration evidence: [`internal/typesafe/typesafe.go`](https://github.com/travisennis/cake-safety-judge/blob/3336ab735a215938df5868d58542b483f40ab244/internal/typesafe/typesafe.go).

## Get started

From the upstream README (not run on the review host):

```sh
just build   # bin/cake-safety-judge
just test    # offline, no model calls
cake-safety-judge check --json --base-url https://api.example.test/v1 --model-name judge-model --api-key-env JUDGE_API_KEY -- 'git push --force'
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/travisennis/cake-safety-judge#readme](https://github.com/travisennis/cake-safety-judge#readme)
- Protocol: [github.com/travisennis/cake-safety-judge/blob/main/docs/protocol.md](https://github.com/travisennis/cake-safety-judge/blob/main/docs/protocol.md)

## Limits and data handling

Command text and context go to your judge model and, when enabled, to TypeSafe. A missing TypeSafe key disables the cascade instead of failing.

## Review and maintenance

Reviewed **2026-10-26** (Europe/Sofia) at [commit 3336ab735a21](https://github.com/travisennis/cake-safety-judge/tree/3336ab735a215938df5868d58542b483f40ab244). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
