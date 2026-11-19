# Monid Social API for agents (pay-per-call social media data for agents, with Jev-powered viral UGC discovery)

[All projects](../README.md) · [Web apps](README.md#web-apps)

Monid is a pay-per-call tool registry for AI agents ("OpenRouter for agent tools"): one key gives an agent access to about 2,800 tools from 72 providers through a skill, a remote MCP server or a CLI. Its Social API bundles TikTok, Instagram, Reddit, YouTube, LinkedIn and ad-library data so an agent can track trends, creators, competitors and campaigns. Monid's launch post says the Social API is powered by Jev, and its landing page advertises "Jev-powered viral UGC discovery, end to end" (scan a niche, rank creators against their own baseline, then find a contact).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://monid.ai) |
| Tags | `Closed source` · `Paid` · `Commercial` |
| Product homepage | [monid.ai](https://monid.ai) |
| Pricing and access | Pay as you go with no subscription; the [Social API page](https://monid.ai/lp/social-media-api) lists per-call prices (for example $0.001 for a TikTok search or creator profile) and $1 of free credit to start. The free credit is a trial, not a free tier. Checked **2026-11-20**; sign-up was not tested. |
| Jev evidence | Vendor claim: Monid's [launch post](https://x.com/MonidHQ/status/2123543931438895491) (2026-11-19) introduces the "Social API for agents, powered by Jev", and the [Social API page](https://monid.ai/lp/social-media-api) describes "Jev-powered viral UGC discovery, end to end". Which steps call Jev was not stated, and the implementation was not inspected. |
| Disclosure | Closed source, commercial service. Jev use is the vendor's public claim, not independently observed API traffic. Monid's public GitHub repositories were checked earlier and showed no Jev code. Independently curated for Awesome Jev; no affiliation or commercial relationship with the vendor; no referral link. Inclusion is not an endorsement. Discovered via X ([post](https://x.com/MonidHQ/status/2123543931438895491)). |
| Maintainer | [Monid](https://monid.ai) ([@MonidHQ](https://x.com/MonidHQ)). |
| Format | Hosted API for agents, reachable as an agent skill (`monid.ai/SKILL.md`), a remote MCP server or a CLI. |
| Platform and availability | Web service; works with agents that load skills or MCP servers. |
| Jev's role | Vendor claim: Jev powers the viral UGC discovery workflow, such as judging which posts are outliers for their creator. Exact questions and thresholds are not documented publicly. |
| Requirements | A Monid account and API key; an agent that supports skills, MCP or a CLI. |
| License | Proprietary hosted service. |

## When to use

Use Monid if you want an agent to pull social media data (posts, creators, ads) across several networks with one key and per-call billing, and to find creators whose posts beat their usual reach. It is a commercial API, not a library. Mismatch: if you need to inspect or self-host the ranking logic, or must avoid third-party scraping providers.

## How it works

Your agent calls Monid's tools through the skill, MCP server or CLI. Monid routes each call to an upstream provider (its page names TikHub, AnyAPI, Apify, Apollo, Hunter and others) and bills the listed per-call price from your balance. For UGC discovery, Monid's page shows a workflow that scans a niche, compares each post with its creator's own baseline, skips non-outliers and looks up a contact; the vendor says this workflow is Jev-powered. No API calls were observed for this listing.

## Get started

This path follows Monid's public page; it was not executed (no sign-up).

1. Open the [Social API page](https://monid.ai/lp/social-media-api) and create an account to get the free starting credit.
2. Give your agent the skill line from the page (`set up https://monid.ai/SKILL.md`), or add the remote MCP server or CLI.
3. Ask the agent for a task such as ranking this month's posts in a niche by creator reach.

## Examples and demos

- [Launch post with a demo video](https://x.com/MonidHQ/status/2123543931438895491) (vendor material).
- [Social API landing page](https://monid.ai/lp/social-media-api) with sample calls and prices.

## Limits and data handling

Queries and results pass through Monid and its upstream data providers; check Monid's terms and each platform's rules before collecting personal data about creators. Prices are per call and can add up in agent loops. Jev's exact role and accuracy were not verified.

## Review and maintenance

Reviewed **2026-11-20** (Europe/Sofia) with AI assistance. Primary sources: [monid.ai](https://monid.ai) and the [Social API page](https://monid.ai/lp/social-media-api) (fetched 2026-11-20) and Monid's [launch post](https://x.com/MonidHQ/status/2123543931438895491) (2026-11-19). Catalog de-dupe found no existing Monid listing.
