# Jev Decision Gateway (kartikanand73)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Governed decision-model gateway: TypeSafe Jev vs GPT-6 Sol vs rules on synthetic withdrawals.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/kartikanand73/jev-decision-gateway) |
| Maintainer | [kartikanand73](https://github.com/kartikanand73). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Architecture PoC + benchmark harness with audit log. |
| Requirements | Python; OpenRouter/TypeSafe and/or OpenAI credentials for live scorer arms. |
| License | [MIT](https://github.com/kartikanand73/jev-decision-gateway/blob/870962323337e2b3e08c43a996f1b258baf39322/LICENSE). Provider usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source inspected; live provider paths not run on the review host. Distinct from kuldeepsinh19/jev-decision-gateway. |

## When to use

Use when studying a pattern where Jev scores and code owns the irreversible decision.

## How it works

Hard rules filter first; Jev (or LLM/rules) scores eligible withdrawals; deterministic HMAC-signed policy decides; simulated executor accepts only signed decisions. Distinct from kuldeepsinh19/jev-decision-gateway. Integration evidence: upstream README and source at the pinned commit below.

## Get started

```sh
git clone https://github.com/kartikanand73/jev-decision-gateway.git
cd jev-decision-gateway
git checkout 870962323337e2b3e08c43a996f1b258baf39322
# follow upstream README for bench/demo; configure credentials as documented
```

Pin revision `870962323337e2b3e08c43a996f1b258baf39322` when reproducing this review.

## Examples and demos

See the upstream README at the pinned commit. No separate live demo was executed on the review host.

## Limits and data handling

Synthetic withdrawals / PoC. Upstream bench numbers are author-reported. Live paths not run on the review host. Distinct from kuldeepsinh19/jev-decision-gateway.

## Review and maintenance

Reviewed **2026-09-28** (Europe/Sofia) at [commit 8709623](https://github.com/kartikanand73/jev-decision-gateway/tree/870962323337e2b3e08c43a996f1b258baf39322). AI-assisted README and LICENSE inspection; install/live paths not executed.
