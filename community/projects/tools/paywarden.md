# PayWarden (payment firewall between an AI accounts-payable agent and PayPal, with Jev choosing payee and amount)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

PayPal AI Hackathon project: an accounts-payable agent reads invoices and job-done messages and proposes PayPal Payouts or Invoices without holding PayPal credentials, and a policy layer applies injection defence, payee and amount provenance, spend mandates, sanctions and structuring checks before executing, asking one or two humans with TOTP, or blocking. Jev picks the payee and total only from values that literally appear in the document and flags manipulation; Claude or an offline fallback can replace it. Every step goes to a hash-chained audit log.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/natrajexplore/paywarden) |
| Maintainer | [natrajexplore](https://github.com/natrajexplore). Independently curated. |
| Format | FastAPI service + MCP server (PayPal sandbox) |
| Requirements | Python 3 and the requirements; PayPal sandbox credentials; a TypeSafe key (Jev is the preferred engine). |
| License | [MIT](https://github.com/natrajexplore/paywarden/blob/1a53fb5101d46dccb28daf96aff40e2838eb5bc7/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`app/agent.py`](https://github.com/natrajexplore/paywarden/blob/1a53fb5101d46dccb28daf96aff40e2838eb5bc7/app/agent.py) at the pinned commit. |

## When to use

- Prototype guardrails for agents that can move money, with typed model signals feeding fixed policy rules.
- Mismatch: built and tested against the PayPal sandbox for a hackathon; not a production payments product.

## How it works

`agent.py` extracts candidate emails and amounts from the redacted document and asks Jev through the TypeSafe SDK to choose payee and total among them and to score manipulation; thresholds (for example manipulation probability 0.80 for deny) live in policy code. Integration evidence: [`app/agent.py`](https://github.com/natrajexplore/paywarden/blob/1a53fb5101d46dccb28daf96aff40e2838eb5bc7/app/agent.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/natrajexplore/paywarden.git
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Policy and AI-signal table: [github.com/natrajexplore/paywarden/blob/1a53fb5101d46dccb28daf96aff40e2838eb5bc7/README.md](https://github.com/natrajexplore/paywarden/blob/1a53fb5101d46dccb28daf96aff40e2838eb5bc7/README.md)

## Limits and data handling

Redacted invoice text is sent to TypeSafe (or Anthropic). Sandbox only; payment decisions should not rely on it without your own review. Not affiliated with PayPal or TypeSafe.

## Review and maintenance

Reviewed **2026-10-30** (Europe/Sofia) at [commit 1a53fb5101d4](https://github.com/natrajexplore/paywarden/tree/1a53fb5101d46dccb28daf96aff40e2838eb5bc7). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
