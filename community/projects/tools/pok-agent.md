# POK-Agent (Windows computer-use agent with an optional TypeSafe Jev System 1 router)

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

Windows 10/11 computer-use agent where a large model plans and a small fast model acts on screen (System 1: TypeSafe Jev or local Laya), with repeated tasks cached as muscle memory; installer, portable build and Telegram gateway.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Acekorneya/POK-Agent) |
| Maintainer | [Acekorneya](https://github.com/Acekorneya). Independently curated. |
| Format | Windows app + Rust CLI (Apache-2.0) |
| Requirements | Windows 10/11, a planner model (local LM Studio/Ollama or cloud key), and optionally a TypeSafe API key for the Jev router. |
| License | [Apache-2.0](https://github.com/Acekorneya/POK-Agent/blob/496e48d4fb3eeb396e0a60b7c8d783ce3544cab7/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`crates/pok-ai-core/src/session/decision_router.rs`](https://github.com/Acekorneya/POK-Agent/blob/496e48d4fb3eeb396e0a60b7c8d783ce3544cab7/crates/pok-ai-core/src/session/decision_router.rs) at the pinned commit. |

## When to use

- Let a planner model drive Windows apps while Jev handles fast action picks.
- Turn repeated desktop tasks into cached routines.
- Mismatch: Windows-only; builds are not code-signed; Jev router is optional.

## How it works

`crates/pok-ai-core/src/config.rs` defaults the System 1 endpoint to `https://api.typesafe.ai/v1/systemone`; `crates/pok-ai-core/src/session/decision_router.rs` routes fast on-screen action choices to it. Integration evidence: [`crates/pok-ai-core/src/session/decision_router.rs`](https://github.com/Acekorneya/POK-Agent/blob/496e48d4fb3eeb396e0a60b7c8d783ce3544cab7/crates/pok-ai-core/src/session/decision_router.rs).

## Get started

Download the Windows installer from Releases, or build from source, then pick a planner and optionally the JEV System 1 router in Settings → Model.

```sh
git clone https://github.com/Acekorneya/POK-Agent.git && cd POK-Agent
export TYPESAFE_API_KEY=...
cargo build --release
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/Acekorneya/POK-Agent/blob/496e48d4fb3eeb396e0a60b7c8d783ce3544cab7/README.md](https://github.com/Acekorneya/POK-Agent/blob/496e48d4fb3eeb396e0a60b7c8d783ce3544cab7/README.md)

## Limits and data handling

Screen context for System 1 decisions is sent to TypeSafe on your key when the Jev router is enabled; keys are stored in Windows Credential Manager.

## Review and maintenance

Reviewed **2026-11-08** (Europe/Sofia) at [commit 496e48d4fb3e](https://github.com/Acekorneya/POK-Agent/tree/496e48d4fb3eeb396e0a60b7c8d783ce3544cab7). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
