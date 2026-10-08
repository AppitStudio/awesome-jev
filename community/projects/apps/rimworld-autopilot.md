# RimWorld Autopilot

[All projects](../README.md) · [Windows apps](README.md#windows-apps)

Experimental autonomous colony manager for RimWorld 1.6 on Windows: Laya — the open, Jev-compatible System One decision model — runs locally, reads the map through a bundled RIMAPI mod, picks what matters next and issues real in-game orders (food, building, work, trade, caravans, raids), with a desktop app to watch its reasoning and change priorities.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Georgy-hook/rimworld-autopilot) |
| Tags | `Open source` · `Free` |
| Product homepage | [Repository README](https://github.com/Georgy-hook/rimworld-autopilot#readme) · [latest release](https://github.com/Georgy-hook/rimworld-autopilot/releases/latest) (Windows installer). |
| Pricing and access | Free Windows installer on GitHub Releases; runs Laya locally (no API key). Requires a RimWorld 1.6 copy and Harmony. Checked 2026-10-08. |
| Jev evidence | Uses Laya, an open Jev-compatible decision model, not hosted Jev: [`laya_decisions.py`](https://github.com/Georgy-hook/rimworld-autopilot/blob/004e9334ca1f8eec1965f1ab97a8374700520be3/laya_decisions.py) and [`docs/LAYA_ARCHITECTURE.md`](https://github.com/Georgy-hook/rimworld-autopilot/blob/004e9334ca1f8eec1965f1ab97a8374700520be3/docs/LAYA_ARCHITECTURE.md). Source inspected at the pinned commit. |
| Disclosure | AI-assisted catalog review; no affiliation. Not commercial. Listing is not an endorsement. Live app not run on the review host. |
| Maintainer | [Georgy-hook](https://github.com/Georgy-hook). Independently curated. |
| Format | Windows installer + Python app + bundled RIMAPI mod |
| Platform and availability | 64-bit Windows 10 (1809+) / 11; RimWorld 1.6 with Harmony; Python 3.10–3.12; NVIDIA GPU recommended (CPU mode available). |
| Jev's role | Laya (Jev-compatible) chooses the colony's next priorities and orders from typed options. |
| Requirements | Windows, RimWorld 1.6, Harmony, Python 3.10–3.12; first setup downloads Laya model files. |
| License | [GPL-3.0](https://github.com/Georgy-hook/rimworld-autopilot/blob/004e9334ca1f8eec1965f1ab97a8374700520be3/LICENSE). |

## When to use

- Watch a local decision model run a RimWorld colony and inspect what it considered.
- Example of a Jev-style typed decision loop driving a complex game fully offline.
- Mismatch: experimental; Windows only; uses Laya rather than hosted Jev.

## How it works

The desktop app polls game state through RIMAPI, builds typed questions for colony needs and lets Laya choose; chosen orders are sent back into the game.

## Get started

Run the Windows installer (README *Quick install*), or set up from source:

```sh
git clone https://github.com/Georgy-hook/rimworld-autopilot.git && cd rimworld-autopilot
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

No API charges; inference is local.

## Examples and demos

- Release notes: [`RELEASE_NOTES.md`](https://github.com/Georgy-hook/rimworld-autopilot/blob/004e9334ca1f8eec1965f1ab97a8374700520be3/RELEASE_NOTES.md).
- Playtest report: [`PLAYTEST_REPORT.md`](https://github.com/Georgy-hook/rimworld-autopilot/blob/004e9334ca1f8eec1965f1ab97a8374700520be3/PLAYTEST_REPORT.md).

## Limits and data handling

Runs locally; game state stays on the machine. Experimental automation can make poor colony choices. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-08** (Europe/Sofia) at [commit 004e9334ca1f](https://github.com/Georgy-hook/rimworld-autopilot/tree/004e9334ca1f8eec1965f1ab97a8374700520be3). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
