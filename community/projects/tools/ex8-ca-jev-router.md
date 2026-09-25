# jev-router (Ex8-ca)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Hermes plugin: TypeSafe Jev (via OpenRouter) routes skills with `jev_route` / `jev_classify`, plus a session-start pre-route that injects top skills into the user message without breaking prompt cache.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Ex8-ca/jev-router) |
| Maintainer | [Ex8-ca](https://github.com/Ex8-ca). Independently curated. |
| Format | Hermes agent plugin (Python tools + `pre_llm_call` hook). |
| Requirements | Hermes agent environment; OpenRouter access to TypeSafe Jev Decisions API; API key as documented. |
| License | [MIT](https://github.com/Ex8-ca/jev-router/blob/db95b19616d069826fdd0e4f4b174eaf2ecbec05/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live provider paths were not exercised on the review host. |

## When to use

Use inside **Hermes** when you need typed skill routing and one cache-safe Jev pre-route per session (not Claude/Codex router proxies).

## How it works

On first turn, Jev ranks skills, `skill_view()` loads bodies, and a stable context block is replayed later. Fail-open on missing key/network. Keyword pre-filter when skills exceed Jev’s 255-cap.

## Get started

```sh
git clone https://github.com/Ex8-ca/jev-router.git
cd jev-router
git checkout db95b19616d069826fdd0e4f4b174eaf2ecbec05
# Install as a Hermes plugin per upstream README; configure OpenRouter/TypeSafe credentials
```

## Examples and demos

- README tools: `jev_route`, `jev_classify`, session-start hook rationale.

## Limits and data handling

Conversation state and skill names go to OpenRouter/TypeSafe. Distinct from gargpratyush/jev-router and other coding-CLI routers.

## Review and maintenance

Reviewed **2026-09-25** (Europe/Sofia) at [commit db95b19](https://github.com/Ex8-ca/jev-router/tree/db95b19616d069826fdd0e4f4b174eaf2ecbec05). AI-assisted README and LICENSE inspection; live TypeSafe/provider integration paths not run.

Related: [jev-router (gargpratyush)](jev-router.md), [codex-jev-router](codex-jev-router.md).
