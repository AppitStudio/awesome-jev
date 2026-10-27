# Dev Studio (one-click team of Claude Code sessions, with Jev routing every message between them)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Dock app that opens a team of Claude Code sessions (an Opus architect, a Sonnet main session and Haiku workers, each worker in its own copy of the project) plus a board showing Jev routing every message between them: who sent what, who got it and how sure the router was. Built on Herdr.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/rickndanger-ctrl/dev-studio) |
| Maintainer | [rickndanger-ctrl](https://github.com/rickndanger-ctrl). Independently curated. |
| Format | Shell and Python (macOS Dock app) |
| Requirements | macOS with Claude Code and Herdr; a TypeSafe API key for the router. |
| License | [MIT](https://github.com/rickndanger-ctrl/dev-studio/blob/c4ebef4c9a2990fdee057abaad5464cee15bd550/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`router/router.py`](https://github.com/rickndanger-ctrl/dev-studio/blob/c4ebef4c9a2990fdee057abaad5464cee15bd550/router/router.py) at the pinned commit. |

## When to use

- Run a small multi-agent Claude Code team and watch the routing.
- Mismatch: macOS; without a key the router falls back to plain rules.

## How it works

`router/router.py` asks Jev three questions about each `studio send` message at `https://api.typesafe.ai/v1/systemone` and applies confidence gates before delivering it. Integration evidence: [`router/router.py`](https://github.com/rickndanger-ctrl/dev-studio/blob/c4ebef4c9a2990fdee057abaad5464cee15bd550/router/router.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/rickndanger-ctrl/dev-studio && cd dev-studio
./install.sh
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/rickndanger-ctrl/dev-studio#readme](https://github.com/rickndanger-ctrl/dev-studio#readme)

## Limits and data handling

Inter-agent messages go to TypeSafe for routing. Code work runs in your own Claude Code sessions.

## Review and maintenance

Reviewed **2026-10-28** (Europe/Sofia) at [commit c4ebef4c9a29](https://github.com/rickndanger-ctrl/dev-studio/tree/c4ebef4c9a2990fdee057abaad5464cee15bd550). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
