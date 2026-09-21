# jevgo

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Unofficial Go client for TypeSafe System One (`jev`): send `state` plus typed Noul/Choice/Score questions and get calibrated answers in one call.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/devbackend/jevgo) |
| Maintainer | [devbackend](https://github.com/devbackend). Independently curated; this page is not an upstream submission or endorsement. Independent/unofficial—not maintained by TypeSafe. |
| Format | Go module (`github.com/devbackend/jevgo`); stdlib HTTP client (testify in tests only). |
| Requirements | Go 1.24+; `TYPESAFE_API_KEY` (optional `TYPESAFE_BASE_URL`, `TYPESAFE_DEFAULT_MODEL`). |
| License | [MIT](https://github.com/devbackend/jevgo/blob/849768d0830528e08fbd572c692a667f4d1854a9/LICENSE). TypeSafe inference billed separately. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Offline `go test ./...` **ok** (~25 cases with httptest). Live TypeSafe calls not run. |

## When to use

Use it when a Go service needs typed System One judgments without pulling a heavier SDK stack. Prefer the [official Python](https://github.com/typesafe-ai/typesafe-sdk-python) / [JavaScript](https://github.com/typesafe-ai/typesafe-sdk-js) SDKs for first-party support, or [semgate](semgate.md) when you want Go HTTP middleware rather than a client library.

## How it works

[`systemone.go`](https://github.com/devbackend/jevgo/blob/849768d0830528e08fbd572c692a667f4d1854a9/systemone.go) posts to `/v1/systemone`. [`questions.go`](https://github.com/devbackend/jevgo/blob/849768d0830528e08fbd572c692a667f4d1854a9/questions.go) builds Noul/Choice/Score constructors; [`answers.go`](https://github.com/devbackend/jevgo/blob/849768d0830528e08fbd572c692a667f4d1854a9/answers.go) decodes typed answers (unknown primitives become `UnknownAnswer`). [`client.go`](https://github.com/devbackend/jevgo/blob/849768d0830528e08fbd572c692a667f4d1854a9/client.go) handles retries, timeouts, and `x-typesafe-request-id`. State and question text leave the host on live calls.

## Get started

```sh
go get github.com/devbackend/jevgo@849768d0830528e08fbd572c692a667f4d1854a9
# or
git clone https://github.com/devbackend/jevgo.git
cd jevgo
git checkout 849768d0830528e08fbd572c692a667f4d1854a9
go test ./...
```

`jevgo.New()` reads `TYPESAFE_API_KEY`. Live calls are billed by TypeSafe.

## Examples and demos

- README quick-start snippet (Noul/Choice/Score).
- This listing: `go test ./...` → **ok** (httptest request/response, validation, retries). No live TypeSafe call.

## Limits and data handling

`state`, instructions, and criteria are sent to TypeSafe when a key is set. Missing keys fail client construction. Not affiliated with TypeSafe. Latency/cost marketing was not measured here.

## Review and maintenance

Reviewed on **2026-09-21** at [commit 849768d](https://github.com/devbackend/jevgo/tree/849768d0830528e08fbd572c692a667f4d1854a9): MIT; AI-assisted source review of README, LICENSE, and Go packages; offline tests passed. No live TypeSafe call.

Related: [semgate](semgate.md), [jev-java](jev-java.md), [TypeSafe.AI (.NET SDK)](typesafe-sdk-csharp.md).
