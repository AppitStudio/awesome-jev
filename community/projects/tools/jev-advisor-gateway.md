# jev-advisor-gateway

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Local gateway that routes coding-agent tool decisions through Jev and can attach a read-only advisor (GPT or Claude) without giving the advisor write authority.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/1arley/jev-advisor-gateway) |
| Maintainer | [1arley](https://github.com/1arley). Independently curated. |
| Format | Node.js local gateway scripts |
| Requirements | Node.js; TYPESAFE_API_KEY for Jev; optional OpenAI/Anthropic keys for advisors. |
| License | [MIT](https://github.com/1arley/jev-advisor-gateway/blob/8d130b5c62687b358c8fff996494f124c53a6a13/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`bin/clients.mjs`](https://github.com/1arley/jev-advisor-gateway/blob/8d130b5c62687b358c8fff996494f124c53a6a13/bin/clients.mjs) at the pinned commit. |

## When to use

- Put Jev in front of coding-agent tool approvals locally.
- Want an optional read-only LLM advisor beside typed Jev gates.
- Mismatch: local gateway; not a hosted product.

## How it works

`bin/clients.mjs` separates TYPESAFE_API_KEY (Jev authorization) from advisor keys and routes tool decisions through the System One client paths documented in the README. Integration evidence: [`bin/clients.mjs`](https://github.com/1arley/jev-advisor-gateway/blob/8d130b5c62687b358c8fff996494f124c53a6a13/bin/clients.mjs).

## Get started

Clone, configure keys in env, and point your agent's tool traffic at the local gateway.

```sh
git clone https://github.com/1arley/jev-advisor-gateway && cd jev-advisor-gateway
# configure TYPESAFE_API_KEY; see README
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README gateway overview
- bin/clients.mjs key separation notes

## Limits and data handling

Local trust boundary only as strong as how you wire the agent. Advisor models see prompts you forward.

## Review and maintenance

Reviewed **2026-10-18** (Europe/Sofia) at [commit 8d130b5c6268](https://github.com/1arley/jev-advisor-gateway/tree/8d130b5c62687b358c8fff996494f124c53a6a13). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
