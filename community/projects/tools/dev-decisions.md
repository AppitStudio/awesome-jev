# dev-decisions

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Verification and calibration layer for AI-aided development (v0.3.0): git hooks block secrets and classify diffs, an optional global ZCode hook blocks agent-run commits/pushes that fail the checks, and a CLI runs plan-contract gates and outcome grading — routing classification through a roster of decision models where TypeSafe Jev (`jev-1.13.0`) handles contract gates and fan-out next to GLiDE, local GLiNER2 and others.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/adelvillar1/dev-decisions) |
| Maintainer | [adelvillar1](https://github.com/adelvillar1). Independently curated. |
| Format | Python CLI with `install-hooks`, a ZCode hook and a live dashboard |
| Requirements | Python (uv), git; provider keys in `~/.config/dev-decisions/env` (`TYPESAFE_API_KEY` for Jev, `FASTINO_API_KEY` for GLiDE); optional local GLiNER2 venv for offline use. |
| License | [`LICENSE`](https://github.com/adelvillar1/dev-decisions/blob/6a2ff145fe86a13ef821072161d3a8ca183148eb/LICENSE) contains the Apache License 2.0 text (GitHub's detector reports it as unrecognised). |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Block secrets and risky diffs before they leave your machine, including agent-run pushes.
- Calibrate which decision model to trust per task from logged telemetry.
- Mismatch: macOS-centric paths and a multi-provider setup; Jev is one of several engines.

## How it works

Hooks call `scan-staged` and `classify-diff`; the router picks a provider chain from `~/.config/sys1/config.toml` (with Jev for Choice/Score/Noul contract gates) and every call emits latency, error and noul-rate telemetry into a JSONL log used for calibration feedback.

## Get started

Configure keys and install the hooks (README *Configuration*):

```sh
git clone https://github.com/adelvillar1/dev-decisions.git && cd dev-decisions
# ~/.config/dev-decisions/env (chmod 600): TYPESAFE_API_KEY=..., FASTINO_API_KEY=...
# then run the CLI's install-hooks in each repo (see README)
```

Decision calls bill the configured providers; the local GLiNER2 path is free.

## Examples and demos

- README *Architecture* and v0.3.0 notes (telemetry, dashboard, calibration feedback loop).

## Limits and data handling

Staged diffs and plan text go to the configured providers unless you use the local engine. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-08** (Europe/Sofia) at [commit 6a2ff145fe86](https://github.com/adelvillar1/dev-decisions/tree/6a2ff145fe86a13ef821072161d3a8ca183148eb). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
