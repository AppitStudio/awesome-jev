# libsemop

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

C++17 port of semantic-operators built on libtypesafe: write a typed semantic judgment once (Boolean, Choice, Score, enum), run it on TypeSafe Jev or another System One provider, and get "don't know" instead of a guess below a confidence threshold; filtering, reranking, cascades and benchmarks included.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/jasonduncan/libsemop) |
| Maintainer | [jasonduncan](https://github.com/jasonduncan). Independently curated. |
| Format | CMake library (`libsemop::semop`, `libsemop::typesafe`) with examples; 0.1.0 not yet released |
| Requirements | CMake ≥ 3.24, a C++17 compiler, libcurl and libtypesafe ≥ 0.1 (fetched if missing); `TYPESAFE_API_KEY` for live calls. |
| License | [MIT](https://github.com/jasonduncan/libsemop/blob/3502e73093ff5b980278748be6fc61db7b248bb8/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Add Jev classification, filtering or reranking to a C++ program without exceptions.
- Escalate only unsure answers to a stronger provider with `Cascade`.
- Mismatch: pre-release (0.1.0 unreleased); API may change.

## How it works

[`include/semop/typesafe.hpp`](https://github.com/jasonduncan/libsemop/blob/3502e73093ff5b980278748be6fc61db7b248bb8/include/semop/typesafe.hpp) implements the Jev provider on libtypesafe; operators and flows in [`semop.hpp`](https://github.com/jasonduncan/libsemop/blob/3502e73093ff5b980278748be6fc61db7b248bb8/include/semop/semop.hpp) map answers to typed values or 'don't know'. Upstream reports the live suite passing against jev-1.13.0 and requests byte-identical to the Python library.

## Get started

Build and run the offline tests (README *Build and use*):

```sh
git clone https://github.com/jasonduncan/libsemop && cd libsemop
cmake -S . -B build && cmake --build build
ctest --test-dir build -LE live
```

Offline tests make no requests; the opt-in live suite (`LIBSEMOP_LIVE=1`) and your own calls are billed by TypeSafe.

## Examples and demos

- Examples: [`examples/`](https://github.com/jasonduncan/libsemop/tree/3502e73093ff5b980278748be6fc61db7b248bb8/examples) (`hello.cpp`, `triage.cpp`, `rerank.cpp`, `filter.cpp`, `ask.cpp`).
- Design notes: [`docs/DESIGN.md`](https://github.com/jasonduncan/libsemop/blob/3502e73093ff5b980278748be6fc61db7b248bb8/docs/DESIGN.md).

## Limits and data handling

Text you classify goes to TypeSafe. Not affiliated with TypeSafe (upstream). Not built on the review host.

## Review and maintenance

Reviewed **2026-10-08** (Europe/Sofia) at [commit 3502e73093ff](https://github.com/jasonduncan/libsemop/tree/3502e73093ff5b980278748be6fc61db7b248bb8). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
