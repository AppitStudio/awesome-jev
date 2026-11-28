# system-one-router by Marco Mornati (OpenAI- and Anthropic-compatible Go gateway where Jev or a local decision model picks the LLM for each prompt)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Go gateway that speaks the OpenAI and Anthropic APIs. For every prompt a small System One decision model (TypeSafe Jev through OpenRouter, or a local Laya sidecar with the same Decisions API shape) classifies topic, complexity and risk, and the router sends the request to the cheapest configured LLM that is good enough, reporting the pick and reason in response headers. Ships a decision benchmark with a published report.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/mmornati/system-one-router) |
| Maintainer | [Marco Mornati](https://github.com/mmornati). Independently curated. |
| Format | Go service (OpenAI/Anthropic-compatible gateway) |
| Requirements | Go; an OpenRouter key for Jev and the answering models (or local sidecars for Laya and other decision models). |
| License | [Apache-2.0](https://github.com/mmornati/system-one-router/blob/f5cf448239669af3cc4b67290a257b0ba70fdc8e/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`internal/decision/decision.go`](https://github.com/mmornati/system-one-router/blob/f5cf448239669af3cc4b67290a257b0ba70fdc8e/internal/decision/decision.go) at the pinned commit. |

## When to use

- Developers who want a cheap classifier to choose between several LLMs per prompt, for Claude Code or any OpenAI client.
- Mismatch: single-model setups where nothing needs routing.

## How it works

`internal/decision/decision.go` sends `choice`, `noul` and `score` questions to the configured decision endpoint (`typesafe/jev-1.13` on OpenRouter in `config.yaml`, or a local sidecar), and the gateway maps the answers to a model from its routing table. Integration evidence: [`internal/decision/decision.go`](https://github.com/mmornati/system-one-router/blob/f5cf448239669af3cc4b67290a257b0ba70fdc8e/internal/decision/decision.go).

## Get started

Put your OpenRouter key in `.env`, start the gateway, and point an OpenAI or Anthropic client at it with model `auto`.

```sh
git clone https://github.com/mmornati/system-one-router && cd system-one-router
cp .env.example .env    # add your OpenRouter key
go run ./cmd/gateway    # listens on 127.0.0.1:8787
OPENAI_BASE_URL=http://127.0.0.1:8787/v1   # then use model "auto"
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Benchmark report: [mmornati.github.io/system-one-router/](https://mmornati.github.io/system-one-router/)
- Getting started: [github.com/mmornati/system-one-router/blob/main/docs/getting-started.md](https://github.com/mmornati/system-one-router/blob/main/docs/getting-started.md)

## Limits and data handling

Every prompt goes to the decision model (OpenRouter/TypeSafe unless you run a local sidecar) and then to the chosen LLM provider. Routing quality depends on your routing table; benchmark numbers are the author's own.

## Review and maintenance

Reviewed **2026-11-28** (Europe/Sofia) at [commit f5cf44823966](https://github.com/mmornati/system-one-router/tree/f5cf448239669af3cc4b67290a257b0ba70fdc8e). Inspected the README, LICENSE, `config.yaml` and `internal/decision/decision.go` at the pinned commit; nothing was built or run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
