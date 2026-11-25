# src-guard-jev by int-wc (mitmproxy egress guard for AI-driven penetration tests that uses Jev to block state-changing requests)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Outbound-traffic guardrail for authorised AI pentest agents (built for the Artex orchestrator): mitmproxy captures every request, a rule layer and Jev judge whether it modifies or deletes existing data or is an RCE exploit, dangerous actions get a 403, and the rest pass with an audit log and a monitoring dashboard. Docs are in Chinese.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/int-wc/src-guard-jev) |
| Maintainer | [int-wc](https://github.com/int-wc). Independently curated. |
| Format | Python (mitmproxy addon) with a web dashboard |
| Requirements | Python, mitmproxy (its CA installed in the agent's trust chain), a TypeSafe API key, and written authorisation for the target assets. |
| License | [MIT](https://github.com/int-wc/src-guard-jev/blob/76ae8074914c56a5ab499667a6892af8f388af71/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`core/guard.py`](https://github.com/int-wc/src-guard-jev/blob/76ae8074914c56a5ab499667a6892af8f388af71/core/guard.py) at the pinned commit. |

## When to use

- Reduce collateral damage when an AI agent tests systems you are authorised to test.
- Mismatch: as a substitute for authorisation or a guarantee; the README says it does not block 100%.

## How it works

`core/guard.py` sends the raw request to `https://api.typesafe.ai/v1/systemone` (default `jev-latest`, optionally via an egress proxy) and combines Jev's scores with the rule layer under `strict`, `dml` or `jev` policies. Integration evidence: [`core/guard.py`](https://github.com/int-wc/src-guard-jev/blob/76ae8074914c56a5ab499667a6892af8f388af71/core/guard.py).

## Get started

Install dependencies, list your authorised scopes, then start the guard and point the agent at it.

```sh
pip install -r requirements.txt
cp examples/scopes.example.json scopes.json
mitmdump -q --listen-port 9200 -s core/mitm_guard.py
export HTTP_PROXY=http://127.0.0.1:9200 HTTPS_PROXY=http://127.0.0.1:9200
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Architecture: [github.com/int-wc/src-guard-jev/blob/76ae8074914c56a5ab499667a6892af8f388af71/docs/ARCHITECTURE.md](https://github.com/int-wc/src-guard-jev/blob/76ae8074914c56a5ab499667a6892af8f388af71/docs/ARCHITECTURE.md)

## Limits and data handling

Raw requests to the targets, including any data they carry, are sent to TypeSafe. Code comments show the author relaxed RCE enforcement (Jev's RCE score is audit-only by default) and an optional DeepSeek or local stand-in for the Jev layer. The guard runs with `ssl_insecure` and the dashboard binds 0.0.0.0 by default; restrict it. Chinese-only docs.

## Review and maintenance

Reviewed **2026-11-25** (Europe/Sofia) at [commit 76ae8074914c](https://github.com/int-wc/src-guard-jev/tree/76ae8074914c56a5ab499667a6892af8f388af71). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
