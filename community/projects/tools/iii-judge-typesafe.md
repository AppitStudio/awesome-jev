# judge-typesafe (iii worker that gives the iii engine's judge hub typed Jev answers)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Rust worker in the iii-hq/workers collection that provides TypeSafe Jev to the iii engine's `judge` hub. It turns JSON state and Noul, Choice or Score questions into typed, validated answers, shares credentials and HTTP capacity across callers, and supports model listing and cancellation. Callers use `judge::evaluate`; the iii ADE's setup wizard can add it as an optional Judge step with the API key stored in the `secrets` worker.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/iii-hq/workers/tree/main/judge-typesafe) |
| Maintainer | [iii-hq](https://github.com/iii-hq). Independently curated. |
| Format | Rust worker for the iii engine (installed with `iii call compose::add`) |
| Requirements | The iii engine (iii/v0.26.0 verified by the repository's CI) and a `TYPESAFE_API_KEY`. |
| License | [Apache-2.0](https://github.com/iii-hq/workers/blob/4c6b2abb8f55947efc5f799d5c99757555cd39de/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/client.rs`](https://github.com/iii-hq/workers/blob/4c6b2abb8f55947efc5f799d5c99757555cd39de/judge-typesafe/src/client.rs) at the pinned commit. |

## When to use

- Give iii workers and agents a shared, typed yes/no, choice or score judgment service backed by Jev.
- Mismatch: it needs the iii engine, and Jev is one of several judge providers (Clef, Laya, OpenAI and others sit beside it).

## How it works

`src/client.rs` posts evaluations to `https://api.typesafe.ai/v1/systemone` (default model `jev-latest`) with retries, shared HTTP capacity and caller-owned cancellation, and returns validated typed answers to `judge::evaluate`. Integration evidence: [`src/client.rs`](https://github.com/iii-hq/workers/blob/4c6b2abb8f55947efc5f799d5c99757555cd39de/judge-typesafe/src/client.rs).

## Get started

From the upstream README (not run on the review host):

```sh
iii call compose::add worker=judge-typesafe
# set the API key in Console > Settings > Workers > Judge TypeSafe, or TYPESAFE_API_KEY in the service environment
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Worker README with a quickstart ticket-urgency evaluation: [github.com/iii-hq/workers/blob/4c6b2abb8f55947efc5f799d5c99757555cd39de/judge-typesafe/README.md](https://github.com/iii-hq/workers/blob/4c6b2abb8f55947efc5f799d5c99757555cd39de/judge-typesafe/README.md)

## Limits and data handling

State you evaluate goes to TypeSafe on your key. The listing covers only the `judge-typesafe` directory of a large multi-worker repository; other workers were not reviewed. Not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-04** (Europe/Sofia) at [commit 4c6b2abb8f55](https://github.com/iii-hq/workers/tree/4c6b2abb8f55947efc5f799d5c99757555cd39de/judge-typesafe). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
