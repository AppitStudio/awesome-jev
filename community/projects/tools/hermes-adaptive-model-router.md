# hermes-adaptive-model-router

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Shadow-first adaptive model router plugin for Hermes Agent: a redacted, current-turn routing dossier goes to TypeSafe Jev, which chooses between a fast model and a high-capability model; decisions are logged content-free while the gateway's configured model still runs.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/INEEDBUG/hermes-adaptive-model-router) |
| Maintainer | [INEEDBUG](https://github.com/INEEDBUG). Independently curated. |
| Format | Hermes Agent plugin with install script and offline test suites |
| Requirements | Hermes Agent (tested with v0.21.5) plus a small upstream integration patch; `TYPESAFE_API_KEY` for live shadow decisions. |
| License | [MIT](https://github.com/INEEDBUG/hermes-adaptive-model-router/blob/884a279d42920c06549b39cb096abad530446ac1/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Measure whether a cheaper model would have sufficed per turn, without changing production routing.
- Copy a privacy design for routing: redaction, human-turn-only provenance gates, kill switch, content-free telemetry.
- Mismatch: automatic provider switching is designed but not enabled; this is shadow evidence only.

## How it works

A `pre_api_request` hook builds a sanitized Routing Dossier (redacted, truncated, current human turn only) and asks Jev for a route decision with probabilities ([`router/client.py`](https://github.com/INEEDBUG/hermes-adaptive-model-router/blob/884a279d42920c06549b39cb096abad530446ac1/router/client.py), [`router/dossier.py`](https://github.com/INEEDBUG/hermes-adaptive-model-router/blob/884a279d42920c06549b39cb096abad530446ac1/router/dossier.py)). The decision and outcome are written to JSONL telemetry; the turn still runs on the gateway's configured model. Turns without `turn_origin == "user"` are rejected before any dossier is built.

## Get started

Run the offline suites first, then install in dry-run mode:

```sh
git clone https://github.com/INEEDBUG/hermes-adaptive-model-router.git
cd hermes-adaptive-model-router
python3 tests/test_router.py          # offline: no credential, no network
./tools/install_plugin.sh --hermes-home "$HERMES_HOME" --dry-run
```

Live commands contact TypeSafe (or the configured provider) and may incur charges.

## Examples and demos

- Mermaid architecture diagrams in the README (shadow path and the designed one-turn override).
- `tools/check_turn_origin_patch.py` to detect a missing provenance patch after a Hermes upgrade.

## Limits and data handling

Redaction is pattern-based, not DLP (upstream statement). Auto mode has no completed concurrency test; route availability is configured, not discovered. Redacted dossiers are sent to TypeSafe. Independent plugin, not affiliated with Nous Research. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-06** (Europe/Sofia) at [commit 884a279d4292](https://github.com/INEEDBUG/hermes-adaptive-model-router/tree/884a279d42920c06549b39cb096abad530446ac1). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
