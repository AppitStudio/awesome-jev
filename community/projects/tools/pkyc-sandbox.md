# Perpetual KYC (pKYC) Sandbox

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Compliance monitoring prototype where Jev acts as a fast gatekeeper on new registry filings, sanctions hits and adverse media: it checks same-entity, novelty and materiality, then discards noise, queues for an analyst, or triggers an LLM due-diligence report refresh.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/munronai/pkyc-sandbox) |
| Maintainer | [munronai](https://github.com/munronai). Independently curated. |
| Format | Python FastAPI server, MCP server over SSE and Streamlit dashboard (Modal deploy script included) |
| Requirements | Python 3.12+, uv; optional `TYPESAFE_API_KEY` for live Jev (a deterministic simulated mode is the default). |
| License | [Apache-2.0](https://github.com/munronai/pkyc-sandbox/blob/32fc1b766478e402f0904ca066e484cfc882e493/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`sandbox_server.py`](https://github.com/munronai/pkyc-sandbox/blob/32fc1b766478e402f0904ca066e484cfc882e493/sandbox_server.py) at the pinned commit. |

## When to use

- Prototype a System 1 / System 2 split for continuous KYC monitoring, so the expensive report model only runs on material changes.
- Test thresholds for discard, analyst review and auto-refresh against injected scenarios, or call it from an MCP client.
- Mismatch: a sandbox with sample entities and synthetic fallbacks, not a production compliance system or legal advice.

## How it works

`sandbox_server.py` builds a `/v1/systemone` payload with Noul, Choice and Score questions for each feed delta and, when the policy is switched to `live`, posts it to `https://api.typesafe.ai/v1/systemone`; otherwise a calibrated simulation answers. The score is routed by thresholds (below 0.50 discard, 0.50 to 0.88 review queue, 0.88 and above refresh). Integration evidence: [`sandbox_server.py`](https://github.com/munronai/pkyc-sandbox/blob/32fc1b766478e402f0904ca066e484cfc882e493/sandbox_server.py).

## Get started

From the upstream README (not run on the review host):

```sh
uv sync
# optional: TYPESAFE_API_KEY=... in .env, then switch Jev mode to live in the dashboard
uv run uvicorn sandbox_server:app --port 8000
uv run streamlit run sandbox_dashboard.py --server.port 8501
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Architecture diagram and a 3-step agent demo script in the README.
- MCP setup notes for Claude Desktop, Cursor and MCP Inspector.

## Limits and data handling

In live mode, feed deltas about the monitored entities go to TypeSafe on your key; the feeds themselves come from Companies House, OpenSanctions and GDELT. The repository commits `__pycache__` files; treat it as a demo.

## Review and maintenance

Reviewed **2026-10-17** (Europe/Sofia) at [commit 32fc1b766478](https://github.com/munronai/pkyc-sandbox/tree/32fc1b766478e402f0904ca066e484cfc882e493). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
