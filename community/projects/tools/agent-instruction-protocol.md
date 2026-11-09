# AIP — Agent Instruction Protocol (governed agent workflows whose decision steps resolve with TypeSafe Jev)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Open protocol and Python runtime for governed, step-by-step agent procedures built on Agent Skills; decision steps are resolved by a TypeSafe System One model when a key is configured.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/zach-blumenfeld/aip) |
| Maintainer | [zach-blumenfeld](https://github.com/zach-blumenfeld). Independently curated. |
| Format | Python CLI/SDK + server (Apache-2.0) |
| Requirements | Python/uv, `uv tool install agent-instruction-protocol`, and optionally a `TYPESAFE_API_KEY` for decision steps. |
| License | [Apache-2.0](https://github.com/zach-blumenfeld/aip/blob/7e63f2fd80acaa3138236b683de5d8b4b834ce35/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/aip/client/resolver.py`](https://github.com/zach-blumenfeld/aip/blob/7e63f2fd80acaa3138236b683de5d8b4b834ce35/src/aip/client/resolver.py) at the pinned commit. |

## When to use

- Run auditable agent procedures with typed decision steps.
- Let small agents follow distilled domain workflows.
- Mismatch: Jev is optional; decisions can be manual.

## How it works

`resolver.py` uses `typesafe_sdk` (`TypeSafeClient`, `Noul`, `Choice`, `Score`) to answer decision steps with confidences against the author's thresholds; without a key, decisions fall back to manual resolution. Integration evidence: [`src/aip/client/resolver.py`](https://github.com/zach-blumenfeld/aip/blob/7e63f2fd80acaa3138236b683de5d8b4b834ce35/src/aip/client/resolver.py).

## Get started

Install the CLI, then run `aip config --decision-model ...` or export `TYPESAFE_API_KEY` before running a procedure.

```sh
uv tool install "agent-instruction-protocol[server]"
export TYPESAFE_API_KEY=...
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Running docs: [github.com/zach-blumenfeld/aip/blob/7e63f2fd80acaa3138236b683de5d8b4b834ce35/docs/running.md](https://github.com/zach-blumenfeld/aip/blob/7e63f2fd80acaa3138236b683de5d8b4b834ce35/docs/running.md)

## Limits and data handling

Step state for decision questions is sent to TypeSafe from the client machine.

## Review and maintenance

Reviewed **2026-11-09** (Europe/Sofia) at [commit 7e63f2fd80ac](https://github.com/zach-blumenfeld/aip/tree/7e63f2fd80acaa3138236b683de5d8b4b834ce35). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
