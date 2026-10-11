# jev CLI (vilinski)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

jev is a Rust CLI for System One decision models that sends state plus typed questions and prints typed answers as JSON, across TypeSafe Jev, Cloudflare Clef, Clef on local Ollama and OpenAI log-probabilities.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/vilinski/jev) |
| Maintainer | [vilinski](https://github.com/vilinski). Independently curated. |
| Format | Rust CLI |
| Requirements | Rust toolchain or a release binary; a TypeSafe key for Jev (other providers optional). |
| License | [Apache-2.0 OR MIT](https://github.com/vilinski/jev/blob/504d52dcc8c42421c5da713cd5aa55c8be0bd998/LICENSE-APACHE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |

## When to use

- Call Jev from shell scripts and pipelines with JSON output and the API key kept out of the caller.
- Mismatch: multi-provider; non-Jev providers behave differently.

## How it works

The CLI normalizes one request shape (model, state, questions) across providers and returns the same answers format, with optional OpenTelemetry tracing. (Summarized from the upstream [README](https://github.com/vilinski/jev/blob/504d52dcc8c42421c5da713cd5aa55c8be0bd998/README.md); not reproduced here.)

## Get started

From the upstream README (not run on the review host): Install the binary as described in the README and run it with `--provider typesafe` and your question file.

## Limits and data handling

State is sent to the selected provider. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-12** (Europe/Sofia) at [commit 504d52dcc8c4](https://github.com/vilinski/jev/tree/504d52dcc8c42421c5da713cd5aa55c8be0bd998). Inspected the upstream README and LICENSE status at the pinned commit; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
