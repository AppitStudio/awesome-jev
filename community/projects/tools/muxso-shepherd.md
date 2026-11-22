# Shepherd by muxso (platform that supervises AI coding agents, with Jev as the cheap verification judge)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

A self-hosted Rust platform that sits around Claude Code, Codex and opencode: you file a requirement, AI drafts a design you approve, work is split into a task DAG and claimed by executors on your own machines, and nothing reaches your main branch until it passes a verification gate. Setting a TypeSafe key routes that gate to Jev, which asks one yes/no question per acceptance criterion in a single call.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/muxso/Shepherd) |
| Maintainer | [muxso](https://github.com/muxso). Independently curated. |
| Format | Rust server + executor + web console (Docker Compose) |
| Requirements | Docker (the Compose file brings up server, executor, web, Postgres and Redis) or a Rust toolchain; an AI CLI on executor machines; `SHEPHERD_JEV_API_KEY` or `TYPESAFE_API_KEY` for the Jev judge, otherwise an LLM judge URL. |
| License | [GPL-2.0](https://github.com/muxso/Shepherd/blob/d728455f78b3680bee55856c1de25073de46a2ba/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`crates/server/src/jev.rs`](https://github.com/muxso/Shepherd/blob/d728455f78b3680bee55856c1de25073de46a2ba/crates/server/src/jev.rs) at the pinned commit. |

## When to use

- Teams that want a hard design gate and verification gate around AI coding agents, with a cheap typed judge for acceptance criteria.
- Mismatch: production use; the author labels v0.0.4 experimental, dogfooded internally, with no public benchmark.

## How it works

`crates/server/src/jev.rs` sends one `noul` per acceptance criterion about the deliverable to `https://api.typesafe.ai/v1/systemone` (`jev-latest` by default) and passes the gate only when every probability reaches the threshold (0.8 by default); `crates/server/src/judge.rs` prefers Jev over the LLM judge whenever a key is set. Integration evidence: [`crates/server/src/jev.rs`](https://github.com/muxso/Shepherd/blob/d728455f78b3680bee55856c1de25073de46a2ba/crates/server/src/jev.rs).

## Get started

Bring up the whole stack with Docker Compose and set the Jev key in the server environment; the usage guide covers from-source runs and executor setup.

```sh
git clone https://github.com/muxso/Shepherd && cd Shepherd
export TYPESAFE_API_KEY=...   # or SHEPHERD_JEV_API_KEY
docker compose -f deploy/docker/docker-compose.yml up --build
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Usage guide: [github.com/muxso/Shepherd/blob/d728455f78b3680bee55856c1de25073de46a2ba/docs/USAGE.md](https://github.com/muxso/Shepherd/blob/d728455f78b3680bee55856c1de25073de46a2ba/docs/USAGE.md)
- Executor install: [github.com/muxso/Shepherd/blob/d728455f78b3680bee55856c1de25073de46a2ba/docs/INSTALL.md](https://github.com/muxso/Shepherd/blob/d728455f78b3680bee55856c1de25073de46a2ba/docs/INSTALL.md)

## Limits and data handling

The deliverable view and acceptance criteria are sent to TypeSafe when the Jev judge is enabled. GPL-2.0: derivative works must stay under the same license. Executor binaries are unsigned. Docs are in English and Chinese.

## Review and maintenance

Reviewed **2026-11-22** (Europe/Sofia) at [commit d728455f78b3](https://github.com/muxso/Shepherd/tree/d728455f78b3680bee55856c1de25073de46a2ba). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
