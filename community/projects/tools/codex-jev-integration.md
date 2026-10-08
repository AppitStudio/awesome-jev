# Codex Jev integration

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Standard-library Python MCP server for Codex CLI and App providing advisory role and resource selection with Jev: six tools (`jev_status`, `jev_route`, `jev_decide`, `jev_select_resources`, and two outcome reporters) send task goal, constraints and eligible candidates as `choice` questions to `jev-latest`, with deterministic review gates, local validation and confidence fallback; it never executes, launches, switches models or approves.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/monkey1sai/codex-jev-integration) |
| Maintainer | [monkey1sai](https://github.com/monkey1sai). Independently curated. |
| Format | MCP server (`python -B payload/jev/decision.py serve`) |
| Requirements | Python 3.12; Codex CLI/App; TypeSafe API key supplied by the caller environment. |
| License | [MIT](https://github.com/monkey1sai/codex-jev-integration/blob/2fa46c787ca99a273d1ada040520499cb3b6871d/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Give Codex a cheap second opinion on which role or resource to use.
- Mismatch: advisory only; reported outcomes are caller-reported, not verified.

## How it works

[`payload/jev/decision.py`](https://github.com/monkey1sai/codex-jev-integration/blob/2fa46c787ca99a273d1ada040520499cb3b6871d/payload/jev/decision.py) implements the tools and the single-attempt, no-redirect request to `/v1/systemone`; design notes in [`docs/codex-jev.md`](https://github.com/monkey1sai/codex-jev-integration/blob/2fa46c787ca99a273d1ada040520499cb3b6871d/docs/codex-jev.md).

## Get started

Register in Codex `config.toml` (README):

```sh
git clone https://github.com/monkey1sai/codex-jev-integration.git
# [mcp_servers.jev_decision]
# command = "python"
# args = ["-B", "<repo>/payload/jev/decision.py", "serve"]
```

Each provider decision is a Jev request on your key.

## Examples and demos

- Offline tests: [`tests/README.md`](https://github.com/monkey1sai/codex-jev-integration/blob/2fa46c787ca99a273d1ada040520499cb3b6871d/tests/README.md).

## Limits and data handling

Task context and candidates go to TypeSafe. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-08** (Europe/Sofia) at [commit 2fa46c787ca9](https://github.com/monkey1sai/codex-jev-integration/tree/2fa46c787ca99a273d1ada040520499cb3b6871d). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
