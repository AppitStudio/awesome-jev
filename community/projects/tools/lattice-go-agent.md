# go-agent by Protocol-Lattice (Go agent framework with TypeSafe Jev tool decisions)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Go framework for AI agents (pluggable LLM providers, memory, guardrails, UTCP tools, multi-agent coordination) with a tool-decision layer that defaults to TypeSafe Jev via OpenRouter's decisions API.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Protocol-Lattice/go-agent) |
| Maintainer | [Protocol-Lattice](https://github.com/Protocol-Lattice). Independently curated. |
| Format | Go module (Apache-2.0) |
| Requirements | Go and an OpenRouter key for Jev tool decisions. |
| License | [Apache-2.0](https://github.com/Protocol-Lattice/go-agent/blob/ebf73f2b10e26b41266d49535c95303821c2590d/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`tool_decision.go`](https://github.com/Protocol-Lattice/go-agent/blob/ebf73f2b10e26b41266d49535c95303821c2590d/tool_decision.go) at the pinned commit. |

## When to use

- Let a Go agent pick tools with a fast typed decision.
- Keep the LLM for generation only.
- Mismatch: Jev is one option in a general framework.

## How it works

`tool_decision.go` defaults to `typesafe/jev-1.13` at `https://openrouter.ai/api/alpha/decisions` to choose tools before invoking them. Integration evidence: [`tool_decision.go`](https://github.com/Protocol-Lattice/go-agent/blob/ebf73f2b10e26b41266d49535c95303821c2590d/tool_decision.go).

## Get started

Add the module with `go get` and enable the Jev tool decider per README.

```sh
git clone https://github.com/Protocol-Lattice/go-agent.git && cd go-agent
export OPENROUTER_API_KEY=...
go test ./...
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/Protocol-Lattice/go-agent/blob/ebf73f2b10e26b41266d49535c95303821c2590d/README.md](https://github.com/Protocol-Lattice/go-agent/blob/ebf73f2b10e26b41266d49535c95303821c2590d/README.md)

## Limits and data handling

Tool-choice context is sent to OpenRouter/TypeSafe on your key.

## Review and maintenance

Reviewed **2026-11-08** (Europe/Sofia) at [commit ebf73f2b10e2](https://github.com/Protocol-Lattice/go-agent/tree/ebf73f2b10e26b41266d49535c95303821c2590d). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
