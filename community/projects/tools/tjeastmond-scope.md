# Scope (code context selector)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

CLI that selects the smallest useful code context for a software task: static analysis shortlists up to 30 candidate chunks, TypeSafe Jev judges the relevance of each through `@typesafe-ai/sdk`, and TypeScript adds supporting declarations to return traceable chunks.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/tjeastmond/scope) |
| Maintainer | [tjeastmond](https://github.com/tjeastmond). Independently curated. |
| Format | CLI (source build; `package.json` 0.0.0, not published at review) |
| Requirements | Bun for building, Node.js 24+ for the compiled CLI; `TYPESAFE_API_KEY`. |
| License | [Apache-2.0](https://github.com/tjeastmond/scope/blob/4d8f8fd49fae61f02c73e2a13cef4b5a8cac4c96/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Prepare focused context for an agent task such as “add retry handling to Stripe webhook processing”.
- Benchmark against the deterministic `--no-jev` baseline.
- Mismatch: early development; fails (non-zero exit) rather than falling back when Jev is unavailable.

## How it works

Static analysis discovers structure and builds a bounded shortlist; [`src/jev/provider.ts`](https://github.com/tjeastmond/scope/blob/4d8f8fd49fae61f02c73e2a13cef4b5a8cac4c96/src/jev/provider.ts) asks Jev whether each candidate is relevant and [`validate.ts`](https://github.com/tjeastmond/scope/blob/4d8f8fd49fae61f02c73e2a13cef4b5a8cac4c96/src/jev/validate.ts) rejects unusable answers. Ignored, dependency, binary and secret-named files are never read; credential-looking text is redacted best-effort before parsing.

## Get started

Build from source and run in a repository:

```sh
git clone https://github.com/tjeastmond/scope.git && cd scope
bun install && bun run build
export TYPESAFE_API_KEY=...
node dist/cli.js "Add retry handling to Stripe webhook processing" --repo /path/to/repo
```

Live commands contact TypeSafe (or the configured provider) and may incur charges.

## Examples and demos

- README *Credentials and data transmission* and exit-code table; [Jev SDK notes](https://github.com/tjeastmond/scope/blob/4d8f8fd49fae61f02c73e2a13cef4b5a8cac4c96/docs/jev-sdk-notes.md).
- `tests/jev-provider.test.ts` (offline) and opt-in `tests/live-jev.test.ts`.

## Limits and data handling

The task text and source of up to 30 shortlisted chunks (with paths and symbol names) are sent to TypeSafe. Redaction is best-effort. Early development. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-07** (Europe/Sofia) at [commit 4d8f8fd49fae](https://github.com/tjeastmond/scope/tree/4d8f8fd49fae61f02c73e2a13cef4b5a8cac4c96). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
