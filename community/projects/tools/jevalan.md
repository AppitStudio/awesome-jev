# jevalan (local decision hub that agents ask before acting, with Jev and other System One backends)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Local Rust daemon that agents such as Claude Code (through a PreToolUse hook), Crush or scripts ask whether to do something. It passes `/v1/systemone` requests through to TypeSafe, OpenRouter, Ollama or local models, runs declarative flows (rules, noul, choice, score, batch) and a capability registry, and streams events over WebSocket. It never performs the effect itself. Alpha release candidate.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/jevalan/jevalan) |
| Maintainer | [jevalan](https://github.com/jevalan). Independently curated. |
| Format | Rust daemon |
| Requirements | Rust toolchain to build; a TypeSafe or OpenRouter key, or a local System One model. |
| License | [Apache-2.0 or MIT](https://github.com/jevalan/jevalan/blob/082179b708d4788764b6ef6eaef0427f19b6a38c/LICENSE-APACHE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`config.example.yaml`](https://github.com/jevalan/jevalan/blob/082179b708d4788764b6ef6eaef0427f19b6a38c/config.example.yaml) at the pinned commit. |

## When to use

- Centralize allow/ask/deny decisions for several local agents.
- Mismatch: alpha (0.1.0-alpha.1, unpublished).

## How it works

`config.example.yaml` defines the TypeSafe backend (`https://api.typesafe.ai`, `TYPESAFE_API_KEY`), and flows such as `config/flows/agent-guard.yaml` ask `jev-latest`; `src/crates/jevalan-daemon/src/flows.rs` runs them. Integration evidence: [`config.example.yaml`](https://github.com/jevalan/jevalan/blob/082179b708d4788764b6ef6eaef0427f19b6a38c/config.example.yaml).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/jevalan/jevalan && cd jevalan
cp config.example.yaml config.yaml   # set your backend keys
# build and run per the README
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/jevalan/jevalan#readme](https://github.com/jevalan/jevalan#readme)

## Limits and data handling

Requests go to whichever backend each flow names; local models keep them on your machine.

## Review and maintenance

Reviewed **2026-10-29** (Europe/Sofia) at [commit 082179b708d4](https://github.com/jevalan/jevalan/tree/082179b708d4788764b6ef6eaef0427f19b6a38c). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
