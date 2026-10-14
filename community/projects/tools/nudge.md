# Nudge

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Typed, replayable, budget-aware language for LLM agents that compiles to Python/TypeScript and includes `decide` blocks targeting `/v1/systemone` Jev-family servers.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/NekomyaDev/nudge) |
| Maintainer | [NekomyaDev](https://github.com/NekomyaDev). Independently curated. |
| Format | Programming language + compiler (Rust) with runtimes |
| Requirements | Rust toolchain or installer; TypeSafe Jev or a Jev-compatible server for real decisions. |
| License | [Apache-2.0](https://github.com/NekomyaDev/nudge/blob/27cb6ba961de735b1b3f28e29d42803c198ea22b/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`runtime/nudge_runtime.ts`](https://github.com/NekomyaDev/nudge/blob/27cb6ba961de735b1b3f28e29d42803c198ea22b/runtime/nudge_runtime.ts) at the pinned commit. |

## When to use

- Write agent workflows with batched typed decisions, deadlines and replay.
- Mismatch: Jev is one decision backend; the language covers far more than Jev.

## How it works

`decide { choose / yes/no / score }` compiles to batched System One requests; the runtime speaks the `/v1/systemone` wire contract shared by TypeSafe Jev and Laya. Integration evidence: [`runtime/nudge_runtime.ts`](https://github.com/NekomyaDev/nudge/blob/27cb6ba961de735b1b3f28e29d42803c198ea22b/runtime/nudge_runtime.ts).

## Get started

From the upstream README (not run on the review host):

```sh
# see README install options (install.command / install.bat / cargo)
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Example: `examples/triage-agent/triage-agent.ndg`.
- Benchmarks: `benches/`.

## Limits and data handling

Decision inputs go to the configured server.

## Review and maintenance

Reviewed **2026-10-14** (Europe/Sofia) at [commit 27cb6ba961de](https://github.com/NekomyaDev/nudge/tree/27cb6ba961de735b1b3f28e29d42803c198ea22b). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
