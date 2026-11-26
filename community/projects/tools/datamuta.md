# Datamuta by Don Johnson (experimental Rust database migration runtime where Jev can suggest a column mapping that a person then approves)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Experimental Rust runtime for database migrations: it captures a typed snapshot, validates an explicit transformation, seals data into bounded partitions, publishes an exactly approved plan, resumes from native commit evidence and verifies stored values. Jev is optional: `suggest-mapping` enumerates the structurally valid column mappings and asks Jev to pick one, with a review option, before the usual hash-approved plan.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/copyleftdev/datamuta) |
| Maintainer | [Don Johnson](https://github.com/copyleftdev) (copyleftdev). Independently curated. |
| Format | Rust CLI and crates (experimental, 0.1.0) |
| Requirements | Rust 1.99+, disposable or backed-up source and target databases (a synthetic PostgreSQL example is included); a TypeSafe key in `DATAMUTA_JEV_API_KEY` only for `suggest-mapping ask`. |
| License | [MIT OR Apache-2.0](https://github.com/copyleftdev/datamuta/blob/d50d033a2f42cbc3c6ce1cd1c416038ea895b98f/LICENSE-MIT) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Discovered via X ([post](https://x.com/sudo_1337/status/2125767724098089199)). |
| Jev evidence | [`crates/datamuta-stream/src/suggest.rs`](https://github.com/copyleftdev/datamuta/blob/d50d033a2f42cbc3c6ce1cd1c416038ea895b98f/crates/datamuta-stream/src/suggest.rs) at the pinned commit. |

## When to use

- Exploring an auditable migration flow where a decision model proposes a mapping but never gets authority over the plan.
- Mismatch: production migrations; the project is experimental, unaudited and says not to point it at production data.

## How it works

`crates/datamuta-stream/src/suggest.rs` builds a Jev Choice request over at most 16 candidate mappings, posts it once (no retries) to `https://api.typesafe.ai/v1/systemone` over HTTPS, saves request and reply, and admits an answer only at probability ≥ 0.90 and margin ≥ 0.20; otherwise it exits 3 and lists the candidates. The author reports validation against live jev-1.14.0. Integration evidence: [`crates/datamuta-stream/src/suggest.rs`](https://github.com/copyleftdev/datamuta/blob/d50d033a2f42cbc3c6ce1cd1c416038ea895b98f/crates/datamuta-stream/src/suggest.rs).

## Get started

Build from source and follow the PostgreSQL example; for a Jev suggestion, set the key and run `suggest-mapping ask`.

```sh
git clone https://github.com/copyleftdev/datamuta
cd datamuta
# build and follow examples/postgres/README.md
export DATAMUTA_JEV_API_KEY=...   # never stored by Datamuta
datamuta-stream suggest-mapping ask --source-endpoint src.json --source-table billing --target-endpoint tgt.json --target-table invoices --evidence evidence.json --request-out request.json --response-out response.json --mapping-out mapping.json --provenance-out mapping.provenance.json
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Project site: [copyleftdev.github.io/datamuta/](https://copyleftdev.github.io/datamuta/)
- Operations guide (mapping suggestion): [github.com/copyleftdev/datamuta/blob/d50d033a2f42cbc3c6ce1cd1c416038ea895b98f/docs/book/operations.md](https://github.com/copyleftdev/datamuta/blob/d50d033a2f42cbc3c6ce1cd1c416038ea895b98f/docs/book/operations.md)

## Limits and data handling

Experimental and unaudited; use disposable databases. Field names and human-written field meanings are sent to TypeSafe when you use `ask`; an accepted mapping is only a draft that still needs `configure`, `inspect` and exact plan-hash approval. Mapping search is bounded (equal field counts, at most 8 fields).

## Review and maintenance

Reviewed **2026-11-26** (Europe/Sofia) at [commit d50d033a2f42](https://github.com/copyleftdev/datamuta/tree/d50d033a2f42cbc3c6ce1cd1c416038ea895b98f). Inspected the README, both licence files, `docs/book/operations.md` and `crates/datamuta-stream/src/suggest.rs` at the pinned commit; nothing was built or run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
