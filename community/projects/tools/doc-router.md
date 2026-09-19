# doc-router

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Route mixed PDF documents between local text extraction and hosted OCR, with optional Jev judgments about which pages need OCR.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/misbahsy/doc-router) |
| Maintainer | [misbahsy](https://github.com/misbahsy). Catalog-curated entry, not a submission by the upstream creator; no upstream affiliation or commercial relationship was provided for this listing. Inclusion is not an endorsement. |
| Format | Rust library and CLI, a Jev adapter, a benchmark harness, and Python bindings through PyO3. |
| Requirements | Rust 1.88+ for a source build. Local heuristic classification needs no account. Jev needs a TypeSafe account and `TYPESAFE_API_KEY` (or `JEV_API_KEY`); OCR execution needs a compatible LiteLLM gateway/provider and its access configuration. |
| Access and costs | Public source build with no app purchase fee; hosted Jev, OCR, and gateway hosting may incur separate charges. Source access does not establish free inference. |
| Jev's role | Optional per-page OCR judgment using extracted text and structural evidence. Default model: `jev-latest`; configurable through `TYPESAFE_MODEL`. The default judge is a local heuristic. |
| License | [MIT](https://github.com/misbahsy/doc-router/blob/8977d2ba1fd672fbbc85f01e630a2d5de6a406aa/LICENSE). |

## When to use

Use this as a developer integration when PDFs mix ordinary text pages with scans, broken text encodings, or unreliable existing OCR layers. It provides a way to inspect routing decisions before connecting an OCR service, or to add page-level routing to an existing document pipeline.

The Rust core exposes the routing and extraction workflow; the CLI supplies the hosted integrations. [Python bindings](https://github.com/misbahsy/doc-router/blob/8977d2ba1fd672fbbc85f01e630a2d5de6a406aa/crates/doc-router-py/README.md) offer another integration path with separate installation requirements. This is a source-built developer tool, not a hosted document application.

## How it works

```text
PDF → structural inspection and text evidence → page judge
    → local extraction / OCR provider → page-ordered result
```

The [Jev request builder](https://github.com/misbahsy/doc-router/blob/8977d2ba1fd672fbbc85f01e630a2d5de6a406aa/crates/doc-router-jev/src/wire.rs) asks one [Noul](https://docs.typesafe.ai/primitives/noul) question per page: does this page need OCR because its text is absent or does not faithfully represent its content? Each question identifies the page in its instructions. State includes structural flags and up to 2,000 characters of extracted text per page, with truncation labeled. Jev does not inspect a rendered page image in this integration.

Requests group up to 50 pages, with an additional soft serialized-size limit. Answers are matched by page keys. [Application code](https://github.com/misbahsy/doc-router/blob/8977d2ba1fd672fbbc85f01e630a2d5de6a406aa/crates/doc-router-jev/src/judge.rs) applies a default probability threshold of `0.5`; there is no default abstention interval. The `jev_gated` mode calls Jev only for documents that meet the implementation's structural ambiguity rules.

The core library handles routing, local extraction, and merging without owning an HTTP client. The [CLI host](https://github.com/misbahsy/doc-router/blob/8977d2ba1fd672fbbc85f01e630a2d5de6a406aa/crates/doc-router-cli/src/host.rs) calls a LiteLLM-compatible `/v1/ocr` endpoint. Jev judges routing; the configured OCR provider performs OCR.

## Get started

**Setup downloads source and Rust dependencies; it makes no inference requests.** Use a separate working directory:

```sh
git clone https://github.com/misbahsy/doc-router.git
cd doc-router
git checkout 8977d2ba1fd672fbbc85f01e630a2d5de6a406aa
cargo build --locked -p doc-router-cli
```

**Offline synthetic example**, from that checkout:

```sh
cargo run --locked -q -p doc-router-cli -- classify tests/fixtures/mixed.pdf
```

Expected: a four-page mixed document with zero-based pages `[1,3]` selected for OCR. The default heuristic makes no provider calls. This classifies the fixture; it does not perform OCR.

**Optional live Jev check:** privately configure `TYPESAFE_API_KEY` in the process environment, then explicitly select Jev:

```sh
cargo run --locked -q -p doc-router-cli -- classify --judge jev tests/fixtures/mixed.pdf
```

This submits the four-page synthetic fixture's text evidence in one Jev request and may incur TypeSafe charges. It does not contact an OCR provider. The result is a model judgment, not a fixed expected output; this live command was not executed during the catalog review.

For actual OCR, follow the upstream [CLI execution guide](https://github.com/misbahsy/doc-router/blob/8977d2ba1fd672fbbc85f01e630a2d5de6a406aa/docs/GUIDE.md). Supply `--base-url`, the provider's model, and any required gateway key such as `LITELLM_API_KEY`. Review the upload and fallback behavior below before using private PDFs. Use `--split-subset` when the provider needs a physically reduced PDF rather than a page-selection field.

## Examples and demos

- [Synthetic fixtures](https://github.com/misbahsy/doc-router/tree/8977d2ba1fd672fbbc85f01e630a2d5de6a406aa/tests/fixtures): small text, scanned, and mixed PDFs for local classification and extraction checks.
- [Jev adapter tests](https://github.com/misbahsy/doc-router/blob/8977d2ba1fd672fbbc85f01e630a2d5de6a406aa/crates/doc-router-jev/tests/http.rs): local mock HTTP examples covering request shape, chunking, missing answers, failures, and the circuit breaker.
- [Corpus and evaluation instructions](https://github.com/misbahsy/doc-router/blob/8977d2ba1fd672fbbc85f01e630a2d5de6a406aa/tests/corpus/README.md): generated fixtures and adversarial PDFs with page-level labels. Live judges require keys and incur usage costs.

No separate hosted demo was verified. The fixture command above is the reviewed starting path.

## Limits and data handling

**Page selection does not necessarily restrict uploaded bytes.** The default OCR host uploads the full PDF with a `pages` field. `--split-subset` sends a reduced PDF for a subset request. If an execution leg fails, the [runner](https://github.com/misbahsy/doc-router/blob/8977d2ba1fd672fbbc85f01e630a2d5de6a406aa/crates/doc-router/src/run.rs) can retry the whole document once through the OCR host, including after a subset attempt. Account for that data transfer and additional cost.

Live Jev calls send extracted text snippets and structural metadata to TypeSafe, or the configured `TYPESAFE_BASE_URL`. OCR calls send document content to the configured gateway and its provider. Local heuristic classification requires neither transfer.

Explicitly selecting Jev without a key produces an error. The reviewed README's statement about missing-key fallback does not match the CLI implementation and tests. With a configured judge, API/timeout/protocol failures in the CLI fall back to the heuristic with labeled reasons; the benchmark constructs a strict judge to avoid attributing heuristic results to Jev. A circuit breaker limits repeated failures. Missing or malformed answers trigger failure handling, while finite out-of-range probabilities are clamped to `[0,1]`.

The default `0.5` threshold and text-only evidence can miss pages needing OCR. Evaluate on representative documents and verify extracted content before relying on it. The corpus documentation also describes a watermark case where the local extractor returns empty content despite a usable text layer; correct routing alone does not guarantee complete extraction.

Upstream reports live benchmark results on a generated corpus, including missed OCR pages. Those figures are not independent validation or a general speed, cost, or accuracy guarantee. No performance claims from that corpus are adopted by this listing.

## Review and maintenance

Reviewed on **2026-09-19** at [commit 8977d2b](https://github.com/misbahsy/doc-router/tree/8977d2ba1fd672fbbc85f01e630a2d5de6a406aa), workspace version 0.1.0. AI-assisted source review covered the license, setup instructions, Jev request/response handling, routing, OCR host, fallback behavior, tests, and corpus documentation. The wire format was compared with the current [TypeSafe API reference](https://docs.typesafe.ai/api) and Noul documentation.

`cargo test --locked -p doc-router -p doc-router-jev -p doc-router-cli` passed **193 tests, including doctests**, with no provider credentials. Tests used synthetic fixtures and local mocks. The built CLI classified the mixed fixture as four pages with `[1,3]` needing OCR; explicitly selecting Jev without a key returned the unavailable-judge error. Python bindings, live Jev/OCR calls, deployment, and model quality were not tested. These checks establish the inspected code behavior, not reliability on real document collections.

Related: [Routing and classification patterns](../../../README.md#routing-and-classification) and the [routing evaluation runner](../../../evaluations/README.md).
