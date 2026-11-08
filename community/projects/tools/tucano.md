# Tucano (desktop team of AI agents with an optional TypeSafe Jev channel router)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Free, open-source desktop app where named coding agents work in chat channels with per-tool permissions and approvals; Jev can act as the router that picks which agent answers.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/eduwxyz/tucano) |
| Maintainer | [eduwxyz](https://github.com/eduwxyz). Independently curated. |
| Format | Electron desktop app (Apache-2.0) |
| Requirements | Tucano desktop build, local agent CLIs (Claude Code, Codex, etc.), and a TypeSafe key for the Jev router. |
| License | [Apache-2.0](https://github.com/eduwxyz/tucano/blob/b71464654925b035fd743fa8d2261e8db0620ac3/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/core/jev.ts`](https://github.com/eduwxyz/tucano/blob/b71464654925b035fd743fa8d2261e8db0620ac3/src/core/jev.ts) at the pinned commit. |

## When to use

- Route channel messages to the right agent without @mentions.
- Keep agents, memory and approvals local.
- Mismatch: router is optional; default router does not call TypeSafe.

## How it works

`src/core/jev.ts` posts to `https://api.typesafe.ai/v1/systemone` with a typed choice among channel handles; selecting `jev` as Router in Settings enables it. Also used for optional browser click targeting. Integration evidence: [`src/core/jev.ts`](https://github.com/eduwxyz/tucano/blob/b71464654925b035fd743fa8d2261e8db0620ac3/src/core/jev.ts).

## Get started

Install from tucano.sh or source, then set Router to Jev in Settings and paste your TypeSafe key.

```sh
git clone https://github.com/eduwxyz/tucano.git && cd tucano
export TYPESAFE_API_KEY=...
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/eduwxyz/tucano/blob/b71464654925b035fd743fa8d2261e8db0620ac3/README.md](https://github.com/eduwxyz/tucano/blob/b71464654925b035fd743fa8d2261e8db0620ac3/README.md)

## Limits and data handling

Message text and agent handles go to TypeSafe when the Jev router is selected.

## Review and maintenance

Reviewed **2026-11-09** (Europe/Sofia) at [commit b71464654925](https://github.com/eduwxyz/tucano/tree/b71464654925b035fd743fa8d2261e8db0620ac3). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
