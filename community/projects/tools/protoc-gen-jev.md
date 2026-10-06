# protoc-gen-jev

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Experimental Buf (bufbuild) protoc plugin that turns Protobuf schemas annotated with questions, rubrics and thresholds into strongly typed Jev clients for Go, TypeScript and Python (or a language-agnostic `.jev.json` spec), mapping fields to noul, choice and score decisions.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/bufbuild/protoc-gen-jev) |
| Maintainer | [bufbuild](https://github.com/bufbuild). Independently curated. |
| Format | protoc / Buf plugin (`go install`) with Go, TypeScript and Python runtimes |
| Requirements | Buf CLI or protoc, Go to install the plugin, and the target-language runtime (`pkg/jev`, `@typesafe-ai/sdk`, or `typesafe-sdk`); `TYPESAFE_API_KEY` to call Jev. |
| License | [MIT](https://github.com/bufbuild/protoc-gen-jev/blob/e676487cb5a7e22cb8f64444253b83c001014819/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Share one schema of decisions across Go, TypeScript and Python services instead of hand-writing prompts and parsing JSON.
- Keep thresholds and rubric levels next to the field definitions so they are reviewed like any API change.
- Mismatch: experimental — schema options and generated APIs are under active development; pin generator and runtime to the same release.

## How it works

Annotate response fields with `jev.v1.field` options (instructions plus `noul { threshold }`, `score { levels }`, or enum/oneof choices). `protoc-gen-jev` generates a `Jev<Service>` client per service; calling it sends the request message as state to Jev and populates the typed response, with `jev.v1.Response` / `jev.v1.Meta` carrying model, usage, confidences and probability distributions. Working examples per language live in [`examples/`](https://github.com/bufbuild/protoc-gen-jev/tree/e676487cb5a7e22cb8f64444253b83c001014819/examples).

## Get started

Install the plugin, add the BSR dependency, and generate (calls to Jev happen when you invoke the generated client):

```sh
go install github.com/bufbuild/protoc-gen-jev@latest
# buf.yaml deps: - buf.build/bufbuild-experimental/protoc-gen-jev
# buf.gen.yaml: - local: protoc-gen-jev
#                 out: gen
#                 opt: [targets=go, paths=source_relative]
buf dep update && buf generate
```

Live commands contact TypeSafe (or the configured provider) and may incur charges.

## Examples and demos

- README Quickstart: an incident `TriageService` with a paging noul (0.85 threshold) and a 1–5 urgency score.
- Complete examples for Go, TypeScript, Python and JSON targets (release v0.0.3).

## Limits and data handling

Experimental (v0.0.x); APIs may change. Generated clients send request contents to TypeSafe. Listing is based on the public bufbuild repository; no affiliation or endorsement implied. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-06** (Europe/Sofia) at [commit e676487cb5a7](https://github.com/bufbuild/protoc-gen-jev/tree/e676487cb5a7e22cb8f64444253b83c001014819). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
