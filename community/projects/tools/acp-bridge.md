# ACP Bridge

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Bridge that exposes local coding agents over the Agent Client Protocol, with a virtual `auto` agent where TypeSafe Jev picks the best-fit agent per task with a confidence gate.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/xiwan/acp-bridge) |
| Maintainer | [xiwan](https://github.com/xiwan). Independently curated. |
| Format | Python service |
| Requirements | Python; local agent CLIs; TypeSafe API key for `auto` routing. |
| License | [Apache-2.0](https://github.com/xiwan/acp-bridge/blob/e9a8192f5ad7ef4ebedb649a8645b5162b4971df/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jev_router.py`](https://github.com/xiwan/acp-bridge/blob/e9a8192f5ad7ef4ebedb649a8645b5162b4971df/src/jev_router.py) at the pinned commit. |

## When to use

- Send tasks to several coding agents through one bridge.
- Let Jev route tasks to an agent, falling back safely to a default when unsure.
- Mismatch: Jev routing is one feature of a larger bridge.

## How it works

Tasks sent to the virtual `auto` agent go to Jev as a choice question over configured agents; confident answers dispatch to that agent, otherwise a default agent is used. Integration evidence: [`src/jev_router.py`](https://github.com/xiwan/acp-bridge/blob/e9a8192f5ad7ef4ebedb649a8645b5162b4971df/src/jev_router.py).

## Get started

From the upstream README (not run on the review host):

```sh
curl -fsSL https://raw.githubusercontent.com/xiwan/acp-bridge/main/install.sh -o install.sh
less install.sh
bash install.sh
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Jev router docs: `docs/jev-router.md`.

## Limits and data handling

Task text is sent to TypeSafe for `auto` routing and billed to your key.

## Review and maintenance

Reviewed **2026-10-15** (Europe/Sofia) at [commit e9a8192f5ad7](https://github.com/xiwan/acp-bridge/tree/e9a8192f5ad7ef4ebedb649a8645b5162b4971df). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
