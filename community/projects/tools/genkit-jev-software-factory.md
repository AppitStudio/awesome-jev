# Genkit software factory gated by Jev

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Go example of a software factory on Kubernetes: Gemini designs, plans and writes a Go module as Genkit flows run through senro, and Jev holds every gate, deciding whether the design is ready and whether to ship, rework or hand a human a brief.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/xavidop/genkit-k8s-flows-jev-software-factory) |
| Maintainer | [xavidop](https://github.com/xavidop). Independently curated. |
| Format | Example project (Go, Genkit, kind) |
| Requirements | Go 1.27+, Docker, kind, kubectl; `GEMINI_API_KEY` and `TYPESAFE_API_KEY`; optional senro CLI. |
| License | [MIT](https://github.com/xavidop/genkit-k8s-flows-jev-software-factory/blob/fe97042f612555c92f00bfe6f8faedff5339d2f5/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Discovered via X ([post](https://x.com/Xavidop/status/2112967386806575248)). |
| Jev evidence | [`flows.go`](https://github.com/xavidop/genkit-k8s-flows-jev-software-factory/blob/fe97042f612555c92f00bfe6f8faedff5339d2f5/flows.go) at the pinned commit. |

## When to use

- See Jev used as the decision layer of a multi-step code-generation pipeline.
- Stop vague requests early and hand a human a brief instead of shipping.
- Mismatch: a companion demo for an article, not a production pipeline.

## How it works

Each run ends with a record Jev produced (`design.json`, `review.json`) through Genkit's System One plugin (`typesafe/jev-latest`, see `flows.go`), and the coordinator state machine uses it to pick the next run. Integration evidence: [`flows.go`](https://github.com/xavidop/genkit-k8s-flows-jev-software-factory/blob/fe97042f612555c92f00bfe6f8faedff5339d2f5/flows.go).

## Get started

From the upstream README (not run on the review host):

```sh
scripts/cluster-up.sh
source scripts/cluster-env.sh
go run . -request requests/token-bucket.md
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Pipeline diagram and files table in the README: [github.com/xavidop/genkit-k8s-flows-jev-software-factory#readme](https://github.com/xavidop/genkit-k8s-flows-jev-software-factory#readme)
- Earlier ticket-routing example: [github.com/xavidop/genkit-k8s-flows-jev](https://github.com/xavidop/genkit-k8s-flows-jev)

## Limits and data handling

Requests and generated code go to Google (Gemini) and TypeSafe (Jev). Sample requests only.

## Review and maintenance

Reviewed **2026-10-22** (Europe/Sofia) at [commit fe97042f6125](https://github.com/xavidop/genkit-k8s-flows-jev-software-factory/tree/fe97042f612555c92f00bfe6f8faedff5339d2f5). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
