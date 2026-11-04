# Go AI SDK TypeSafe provider (evaluation provider for Jev inside a multi-provider Go AI SDK)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Go port of the AI SDK that supports 49 providers behind one API. Its TypeSafe AI provider implements only the experimental `ai.ExperimentalEvaluate` call: you pass a state and boolean, choice or score questions, and it returns typed answers from a Jev model; text, embedding, image and speech models return errors by design. Documentation lives in a provider guide page.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/digitallysavvy/go-ai) |
| Maintainer | [digitallysavvy](https://github.com/digitallysavvy). Independently curated. |
| Format | Go module (provider package inside go-ai) |
| Requirements | Go and a `TYPESAFE_AI_API_KEY`. |
| License | [Apache-2.0](https://github.com/digitallysavvy/go-ai/blob/31da6def299cba541a124382cd9647d0826947dd/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`pkg/providers/typesafeai/evaluation_model.go`](https://github.com/digitallysavvy/go-ai/blob/31da6def299cba541a124382cd9647d0826947dd/pkg/providers/typesafeai/evaluation_model.go) at the pinned commit. |

## When to use

- Add typed Jev judgments to a Go service already built on the Go AI SDK.
- Mismatch: the TypeSafe provider covers evaluation only, and the evaluate API is marked experimental.

## How it works

`evaluation_model.go` posts to `{baseURL}/systemone` (default `https://api.typesafe.ai/v1`), sending boolean questions as TypeSafe's native noul type, and maps the wire response back to typed results; tests pin `jev-1.13.0`. Integration evidence: [`pkg/providers/typesafeai/evaluation_model.go`](https://github.com/digitallysavvy/go-ai/blob/31da6def299cba541a124382cd9647d0826947dd/pkg/providers/typesafeai/evaluation_model.go).

## Get started

From the upstream README (not run on the review host):

```sh
export TYPESAFE_AI_API_KEY=...
# Go: provider := typesafeai.New(typesafeai.Config{APIKey: os.Getenv("TYPESAFE_AI_API_KEY")})
# evalModel, _ := provider.EvaluationModel("jev-latest")
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Provider guide with setup and an evaluation example: [github.com/digitallysavvy/go-ai/blob/31da6def299cba541a124382cd9647d0826947dd/docs/05-providers/46-typesafeai.mdx](https://github.com/digitallysavvy/go-ai/blob/31da6def299cba541a124382cd9647d0826947dd/docs/05-providers/46-typesafeai.mdx)

## Limits and data handling

Questions and state go to TypeSafe on your key. The repository is a general SDK, so most of it is unrelated to Jev; the Jev code is limited to one provider package. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-04** (Europe/Sofia) at [commit 31da6def299c](https://github.com/digitallysavvy/go-ai/tree/31da6def299cba541a124382cd9647d0826947dd). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
