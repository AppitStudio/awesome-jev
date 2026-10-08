# Qoresence

[All projects](../README.md) · [Windows apps](README.md#windows-apps)

Local-first Windows 'gaming streaming observatory' for PS5 + capture card + DualSense (Madden 27 / College Football): HDMI video, controller HID and game situation become one causal event bus surfaced through overlays, clips and a pull-only AgentGlass/MCP; with opt-in TypeSafe Jev, typed score-plausibility and ticket checks keep the board dark instead of painting an unconfirmed score — Jev never mints score digits.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ConWan30/Qoresence) |
| Tags | `Open source` · `Free` · `BYOK` |
| Product homepage | [conwan30.github.io/Qoresence](https://conwan30.github.io/Qoresence/) |
| Pricing and access | Free Windows starter package on [GitHub Releases](https://github.com/ConWan30/Qoresence/releases/latest) (v0.7.0, with SHA-256 file). Jev surfaces are off by default and need your own TypeSafe key (billed by TypeSafe). Checked 2026-10-08. |
| Jev evidence | [`qoresence/observability/jev_conductor.py`](https://github.com/ConWan30/Qoresence/blob/19c2df58275df92cb9e94b4d4b223c472c5ff869/qoresence/observability/jev_conductor.py) and [`jev_ledger.py`](https://github.com/ConWan30/Qoresence/blob/19c2df58275df92cb9e94b4d4b223c472c5ff869/qoresence/observability/jev_ledger.py) run judgment packs through the TypeSafe SDK/CLI and append to `logs/jev_ledger.jsonl`; upstream audit notes in [`docs/spike/JEV_INTEGRATION_REVIEW.md`](https://github.com/ConWan30/Qoresence/blob/19c2df58275df92cb9e94b4d4b223c472c5ff869/docs/spike/JEV_INTEGRATION_REVIEW.md). Source inspected at the pinned commit. |
| Disclosure | AI-assisted catalog review; no affiliation. Not commercial. Listing is not an endorsement. Live app not run on the review host. |
| Maintainer | [ConWan30](https://github.com/ConWan30). Independently curated. |
| Format | Windows desktop app (Python; installer script + launcher) |
| Platform and availability | Windows with a PS5, HDMI capture card and DualSense; pilot quality per upstream. |
| Jev's role | Optional typed gates on the observation plane (score plausibility, stale tickets, connector binds); Python code owns every compose decision. |
| Requirements | Windows, Python (installed by the starter package), capture hardware; optional `typesafe` CLI/SDK with `TYPESAFE_API_KEY` and `--jev` / `QORESENCE_JEV=1`. |
| License | [MIT](https://github.com/ConWan30/Qoresence/blob/19c2df58275df92cb9e94b4d4b223c472c5ff869/LICENSE). |

## When to use

- Run an honest score/situation overlay that goes dark rather than showing a wrong read.
- Expose game observations to a personal agent through a pull-only MCP.
- Mismatch: niche hardware setup; Jev is optional and off by default.

## How it works

The capture stack timestamps every event on one clock; ConfirmTicket and SEQGATE checks license digits before anything paints. With `--jev`, judgment packs ask Jev noul/choice/score questions and dual-write to the ledger; empty or unlocked answers produce blank tokens, never a guess.

## Get started

Install the Windows starter package (README *Download and install*):

```sh
.\Install-Qoresence.ps1   # from the extracted Qoresence-Windows.zip (PowerShell -ExecutionPolicy Bypass -File)
.\Start-Qoresence.bat
# optional: set TYPESAFE_API_KEY and start with --jev
```

Jev packs, when enabled, are billed to your TypeSafe key.

## Examples and demos

- [Windows installation guide](https://conwan30.github.io/Qoresence/install.html).
- [Launch post on X](https://x.com/Qoresence/status/2108026513203273827).

## Limits and data handling

Observation summaries sent to TypeSafe only when Jev is enabled; keys are never printed. Pilot software for specific titles. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-08** (Europe/Sofia) at [commit 19c2df58275d](https://github.com/ConWan30/Qoresence/tree/19c2df58275df92cb9e94b4d4b223c472c5ff869). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
