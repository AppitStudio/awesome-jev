# SPINACH Lab (knowledge-graph question answering with Jev-guided navigation)

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

Go reimplementation of the SPINACH knowledge-base question-answering research with an interactive graph editor, a step-by-step educational question journey and a lightweight SPARQL engine (SPARQLite); its experimental extension uses Jev as a navigation layer that ranks subgraphs before each model action, while OpenAI writes the answers. Live demo; English and Spanish docs.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/arturoeanton/go-r2-SPINACH) |
| Maintainer | [arturoeanton](https://github.com/arturoeanton). Independently curated. |
| Format | Go web app and SPARQL engine |
| Requirements | Go; OpenAI and TypeSafe API keys for question journeys (graph editing and manual SPARQL work without keys). |
| License | [MIT](https://github.com/arturoeanton/go-r2-SPINACH/blob/d7a90f6a4ead0210947cfa2c52e2763d5aafc42e/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`lab/internal/models/cloud.go`](https://github.com/arturoeanton/go-r2-SPINACH/blob/d7a90f6a4ead0210947cfa2c52e2763d5aafc42e/lab/internal/models/cloud.go) at the pinned commit. |

## When to use

- Learn how agentic KBQA walks a knowledge graph step by step.
- Mismatch: an experimental extension, not a measured improvement over the original system; Jev scores express navigation preference, not answer confidence.

## How it works

`lab/internal/models/cloud.go` configures the Jev connection (`JEV_BASE_URL`, default `https://api.typesafe.ai/v1`, `jev-latest`) used to rank candidate subgraphs. Integration evidence: [`lab/internal/models/cloud.go`](https://github.com/arturoeanton/go-r2-SPINACH/blob/d7a90f6a4ead0210947cfa2c52e2763d5aafc42e/lab/internal/models/cloud.go).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/arturoeanton/go-r2-SPINACH && cd go-r2-SPINACH
go run ./lab/cmd/spinach -db ./lab/data/spinach.db
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Live demo: [go-r2-spinach.vercel.app/](https://go-r2-spinach.vercel.app/)
- Validation report: [github.com/arturoeanton/go-r2-SPINACH/blob/main/docs/VALIDATION.md](https://github.com/arturoeanton/go-r2-SPINACH/blob/main/docs/VALIDATION.md)

## Limits and data handling

Question text and graph snippets go to OpenAI and TypeSafe during question journeys.

## Review and maintenance

Reviewed **2026-10-27** (Europe/Sofia) at [commit d7a90f6a4ead](https://github.com/arturoeanton/go-r2-SPINACH/tree/d7a90f6a4ead0210947cfa2c52e2763d5aafc42e). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
