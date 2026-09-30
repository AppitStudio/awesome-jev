# Jev NetHack

[All projects](../README.md) · [Games and simulation](README.md#games-and-simulation)

TypeSafe Jev plays NetHack 5.0: code lists legal moves, Jev picks one—no LLM in the loop—with a live dashboard and optional Hardfought play.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/statico/jev-nethack) |
| Maintainer | [statico](https://github.com/statico). Independently curated. |
| Format | Python server + NetHack 5.0 build + web dashboard; MIT. |
| Requirements | Python 3; Node.js (dashboard build); NetHack build script; `JEV_API_KEY` (TypeSafe). |
| License | [MIT](https://github.com/statico/jev-nethack/blob/cb56e9f880e44942fa94be4602eed53512a72f96/LICENSE). TypeSafe usage may incur charges; default spend limit `$5` via `JEV_BUDGET_USD`. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Upstream notes AI-written code. Live NetHack/TypeSafe paths not run on the review host. |

## When to use

Use as a game demo of closed-set System One choices under NetHack state. Prefer lighter sims (2048, Zork) when you lack a NetHack build.

## How it works

Code reads the terminal screen, enumerates legal options, asks Jev a `choice`, and a motor executes keystrokes. Dashboard shows probabilities, spend, and history; Hardfought mode optional.

## Get started

```sh
git clone https://github.com/statico/jev-nethack.git
cd jev-nethack
git checkout cb56e9f880e44942fa94be4602eed53512a72f96
# follow upstream: scripts/build-nethack.sh, venv, web build, JEV_API_KEY, python -m jev.server
```

## Examples and demos

- Upstream README screenshots and Hardfought instructions.
- Decision logs under `runs/<id>/decisions.jsonl` when run.

## Limits and data handling

Live Jev sends game-option text to TypeSafe and may incur charges. Catalog checks did not build NetHack or run live play.

## Review and maintenance

Reviewed **2026-09-30** (Europe/Sofia) at [commit cb56e9f](https://github.com/statico/jev-nethack/tree/cb56e9f880e44942fa94be4602eed53512a72f96). AI-assisted README and license inspection; install/live paths not executed.
