# Jev Guess Who

[All projects](../README.md) · [Web apps](README.md#web-apps)

Server-authoritative Guess Who (human vs TypeSafe Jev) with 24 original SVG portraits, local practice without credentials, and analytics hooks.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/jevplays-games/jev-guess-who) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/jevplays-games/jev-guess-who#readme) |
| Pricing and access | Free source build; local practice without keys. Live Jev BYOK. Checked 2026-10-02. |
| Jev evidence | [Upstream README](https://github.com/jevplays-games/jev-guess-who/blob/5d1b4326d8aee7f61b5f03b8515b88ba64d14aad/README.md) documents human-vs-Jev gameplay and provider setup. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live install/UI paths not run on the Linux review host. |
| Maintainer | [jevplays-games](https://github.com/jevplays-games). Independently curated. |
| Format | JavaScript · Node web game (MIT) |
| Platform and availability | Web (Node server; Cloudflare Workers/D1 deploy files included) |
| Jev's role | Jev answers typed deduction questions; the server owns game state and legality. |
| Requirements | Node ≥22.13; TypeSafe/configured provider for live Jev. |
| License | [MIT](https://github.com/jevplays-games/jev-guess-who/blob/5d1b4326d8aee7f61b5f03b8515b88ba64d14aad/LICENSE). Provider usage may incur charges when live. |

## When to use

Use when the workflow matches the upstream README. Prefer other catalog apps when you need a different platform or a hosted-only product.

## How it works

Server-authoritative Guess Who (human vs TypeSafe Jev) with 24 original SVG portraits, local practice without credentials, and analytics hooks. Jev supplies typed judgments where configured; application code owns orchestration and side effects.

## Get started

```sh
git clone https://github.com/jevplays-games/jev-guess-who.git
cd jev-guess-who
git checkout 5d1b4326d8aee7f61b5f03b8515b88ba64d14aad
# follow upstream README for install/run
```

## Examples and demos

- Upstream README and any linked demos/screenshots.

## Limits and data handling

Live Jev may send task text to TypeSafe and may incur charges. Catalog checks did not execute install or live inference on the review host.

## Review and maintenance

Reviewed **2026-10-02** (Europe/Sofia) at [commit 5d1b4326d8ae](https://github.com/jevplays-games/jev-guess-who/tree/5d1b4326d8aee7f61b5f03b8515b88ba64d14aad). AI-assisted README and license inspection; live paths not executed.
