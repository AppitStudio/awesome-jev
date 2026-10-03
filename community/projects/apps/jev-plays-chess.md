# Jev plays chess

[All projects](../README.md) · [Web apps](README.md#web-apps)

Public chess ladder where TypeSafe Jev picks each move as a Choice over legal moves annotated with local facts (no lookahead); Maia-3 is the opponent; Stockfish eval bar is display-only.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/dmallory42/jev-plays-chess) |
| Tags | `Open source` · `Free` · `BYOK` |
| Product homepage | [jev-plays-chess.view.fast](https://jev-plays-chess.view.fast/) |
| Pricing and access | Hosted spectator site free for visitors (operator pays Jev). Self-host is free source build with BYOK TypeSafe. Checked 2026-10-04. |
| Jev evidence | [Upstream README](https://github.com/dmallory42/jev-plays-chess/blob/1356f2fc96f7425e9a37168ca06a3aa85ea6574f/README.md) documents facts.ts → jev.ts Choice flow and Maia-3 opponent. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. GPL-2.0-or-later; deployed combination with maia3-ts is AGPL-3.0 as upstream notes. Distinct from [Jev Chess](https://github.com/choxos/jevchess) (OpenRouter/Stockfish/you opponents). Live install/UI paths not run on the Linux review host. |
| Maintainer | [dmallory42](https://github.com/dmallory42). Independently curated. |
| Format | Web viewer + API: Jev vs Maia-3 Elo ladder (GPL-2.0-or-later) |
| Platform and availability | Hosted viewer + self-host Node/Docker adapters |
| Jev's role | Each turn Jev answers one Choice over legal moves with factual annotations; code owns pacing, Elo updates, and Maia play. Stockfish never reaches Jev. |
| Requirements | Node 22.13+ for self-host; TYPESAFE_API_KEY for live Jev (or --fake-jev for offline). |
| License | [GPL-2.0](https://github.com/dmallory42/jev-plays-chess/blob/1356f2fc96f7425e9a37168ca06a3aa85ea6574f/LICENSE). Provider usage may incur charges when live. |

## When to use

Use to watch or self-host Jev vs human-like Maia-3 on an Elo ladder. Prefer jevchess when you want interactive play vs LLMs/Stockfish/you.

## How it works

Public chess ladder where TypeSafe Jev picks each move as a Choice over legal moves annotated with local facts (no lookahead); Maia-3 is the opponent; Stockfish eval bar is display-only. Jev supplies typed judgments where configured; application code owns orchestration and side effects.

## Get started

```sh
git clone https://github.com/dmallory42/jev-plays-chess.git
cd jev-plays-chess
git checkout 1356f2fc96f7425e9a37168ca06a3aa85ea6574f
# follow upstream README for install/run
```

## Examples and demos

- Upstream README and any linked demos/screenshots.

## Limits and data handling

Live Jev may send task text to TypeSafe and may incur charges. Catalog checks did not execute install or live inference on the review host.

## Review and maintenance

Reviewed **2026-10-04** (Europe/Sofia) at [commit 1356f2fc96f7](https://github.com/dmallory42/jev-plays-chess/tree/1356f2fc96f7425e9a37168ca06a3aa85ea6574f). AI-assisted README and license inspection; live paths not executed.
