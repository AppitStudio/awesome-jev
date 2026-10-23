# Switchbite (agent and model pool recommendations by Jev)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Rust library and native MCP stdio server from BiteFoundry that recommends which worker (agent, model, or harness and settings combination) from your pool should take a task, or holds explicitly; it also validates task DAGs and normalizes outcome feedback, with Jev as the online judge.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/BiteFoundry/switchbite) |
| Maintainer | [BiteFoundry](https://github.com/BiteFoundry). Independently curated. |
| Format | Rust MCP server and library (Windows x64 release binary) |
| Requirements | Windows x64 for the release build (Linux and macOS not release-validated); an MCP client such as Claude Code, Codex or Cursor; a TypeSafe API key for online decisions. |
| License | [MIT](https://github.com/BiteFoundry/switchbite/blob/878530478ea948efcdba0ed5e67831ffe0810ad7/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/http.rs`](https://github.com/BiteFoundry/switchbite/blob/878530478ea948efcdba0ed5e67831ffe0810ad7/src/http.rs) at the pinned commit. |

## When to use

- Let an orchestrator ask which agent or model should take the next task.
- Replay decisions offline and validate plans without a key.
- Mismatch: proposes only; your host owns execution, authorization and state.

## How it works

`src/http.rs` posts each assignment question to `https://api.typesafe.ai/v1/systemone` with `jev-1.14.0` using `TYPESAFE_API_KEY` from the MCP child process; `--offline` disables online judging. Integration evidence: [`src/http.rs`](https://github.com/BiteFoundry/switchbite/blob/878530478ea948efcdba0ed5e67831ffe0810ad7/src/http.rs).

## Get started

From the upstream README (not run on the review host):

```sh
.\bin\switchbite.exe --version
.\bin\switchbite.exe config --client claude
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Model pools and orchestrators: [github.com/BiteFoundry/switchbite/blob/main/docs/model-pools.md](https://github.com/BiteFoundry/switchbite/blob/main/docs/model-pools.md)
- API details: [github.com/BiteFoundry/switchbite/blob/main/docs/api.md](https://github.com/BiteFoundry/switchbite/blob/main/docs/api.md)

## Limits and data handling

Task and candidate descriptions are sent to TypeSafe in online mode. First public preview (v0.3.0).

## Review and maintenance

Reviewed **2026-10-23** (Europe/Sofia) at [commit 878530478ea9](https://github.com/BiteFoundry/switchbite/tree/878530478ea948efcdba0ed5e67831ffe0810ad7). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
