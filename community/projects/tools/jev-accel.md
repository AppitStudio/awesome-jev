# JEV_accel

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Traditional-Chinese Python package, CLI and MCP server that speeds up embedded bench work on a TI F280049C board with a RIGOL MSO5104 oscilloscope and Code Composer Studio: deterministic L0 rules answer first, TypeSafe Jev (`typesafe-sdk` Choice/Noul) is called only for ambiguous cases such as prioritising multiple violations, and the agent gets measurement state, a verdict and ready-to-send SCPI or next commands in one tool call.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/poyen-tseng/jev-accel) |
| Maintainer | [poyen-tseng](https://github.com/poyen-tseng). Independently curated. |
| Format | Python package with CLI (`python -m jev_accel …`) and MCP servers (Windows) |
| Requirements | Windows, Python 3.11, TI CCS, RIGOL MSO5104 over the network; optional `TYPESAFE_API_KEY` (falls back to L0 rules). |
| License | The reviewed tree has **no LICENSE file** — listed as Source available; reuse terms are not granted until the maintainer adds a license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Let Cursor/Claude Code verify scope captures and flash state without screenshot guessing.
- Template for rule-first, Jev-second hardware tooling.
- Mismatch: tied to one specific board/scope setup; Chinese-only docs.

## How it works

Rules in `src/jev_accel/rules/*` run first (~0 ms); [`src/jev_accel/jev.py`](https://github.com/poyen-tseng/jev-accel/blob/00c95b4d1fdc1ba6f0d5513a9f5588a86ea2006c/src/jev_accel/jev.py) asks Jev only when rules are inconclusive; [`mcp_server.py`](https://github.com/poyen-tseng/jev-accel/blob/00c95b4d1fdc1ba6f0d5513a9f5588a86ea2006c/src/jev_accel/mcp_server.py) exposes `jev_check_frame`, `jev_autoframe` and CCS tools. Replay accuracy/latency in [`JEV_PERFORMANCE.md`](https://github.com/poyen-tseng/jev-accel/blob/00c95b4d1fdc1ba6f0d5513a9f5588a86ea2006c/JEV_PERFORMANCE.md).

## Get started

Create a venv and install (README):

```sh
py -3.11 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -e ".[dev]"
setx TYPESAFE_API_KEY "<key>"
.\.venv\Scripts\python.exe -m jev_accel ping-jev
```

Jev calls (only for ambiguous cases) billed to your TypeSafe key.

## Examples and demos

- README replay results (2026-10-07, `jev-1.13.0`).

## Limits and data handling

Measurement summaries go to TypeSafe when Jev is called. No LICENSE file. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-08** (Europe/Sofia) at [commit 00c95b4d1fdc](https://github.com/poyen-tseng/jev-accel/tree/00c95b4d1fdc1ba6f0d5513a9f5588a86ea2006c). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
