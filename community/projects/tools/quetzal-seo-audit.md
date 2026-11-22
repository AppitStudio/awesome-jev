# Quetzal SEO & AI-Search Audit Skill by Sergio Verdugo (agent skill for SEO and AI-search audits, with Jev as the decision layer)

[All projects](../README.md) · [Customer feedback and marketing](README.md#customer-feedback-and-marketing)

An agent skill for Claude Code, Antigravity and Cursor that runs a classic SEO and AI-search (AEO/GEO) audit of a website in ten phases: a no-JS crawl, performance, AI-answer visibility across ChatGPT, Perplexity, Gemini and Claude, the sources cited in lost answers, demand, SERP shape, trends and competitors. It writes a client-branded HTML report plus `findings.json`, and refuses findings that lack quoted evidence.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Svrubio7/quetzal-seo-audit-skill) |
| Maintainer | [Svrubio7](https://github.com/Svrubio7). Independently curated. |
| Format | Agent skill + 11 zero-dependency Node scripts |
| Requirements | Node 18+; an OpenRouter key for the AI-answer probes and Jev (or a TypeSafe key with `JEV_URL`); optional free Google PageSpeed and Search Console access. Every missing key is recorded in the report instead of guessed. |
| License | [MIT](https://github.com/Svrubio7/quetzal-seo-audit-skill/blob/6db3cee2e18dc349d178de785068573dad4d0e70/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`tools/lib/jev.mjs`](https://github.com/Svrubio7/quetzal-seo-audit-skill/blob/6db3cee2e18dc349d178de785068573dad4d0e70/tools/lib/jev.mjs) at the pinned commit. |

## When to use

- Audit a site for both Google and AI-answer visibility, with evidence attached to every finding.
- Mismatch: a hosted SEO dashboard; this runs locally through your coding agent.

## How it works

`tools/lib/jev.mjs` is the single Jev client: it batches every question about one state into one request to OpenRouter's decisions endpoint (`typesafe/jev-1.13`) or to `https://api.typesafe.ai/v1/systemone` with a TypeSafe key, with bounded concurrency, retries and metered cost. `tools/jev-seo.mjs` uses it for intent tagging, query-to-page mapping, cannibalisation and reading AI answers. Integration evidence: [`tools/lib/jev.mjs`](https://github.com/Svrubio7/quetzal-seo-audit-skill/blob/6db3cee2e18dc349d178de785068573dad4d0e70/tools/lib/jev.mjs).

## Get started

Clone the skill into your agent's skills folder, add keys to `.env.local` in the directory you audit from, then ask the agent to run the audit.

```sh
git clone https://github.com/Svrubio7/quetzal-seo-audit-skill.git ~/.claude/skills/seo-audit
cp ~/.claude/skills/seo-audit/.env.example .env.local   # add OPENROUTER_API_KEY etc.
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- When and how Jev is used: [github.com/Svrubio7/quetzal-seo-audit-skill/blob/6db3cee2e18dc349d178de785068573dad4d0e70/references/jev.md](https://github.com/Svrubio7/quetzal-seo-audit-skill/blob/6db3cee2e18dc349d178de785068573dad4d0e70/references/jev.md)
- Skill definition: [github.com/Svrubio7/quetzal-seo-audit-skill/blob/6db3cee2e18dc349d178de785068573dad4d0e70/SKILL.md](https://github.com/Svrubio7/quetzal-seo-audit-skill/blob/6db3cee2e18dc349d178de785068573dad4d0e70/SKILL.md)

## Limits and data handling

The headline numbers (14× impressions, ~1,100 Jev decisions for $0.12) are the author's own results on their own domain. Crawled pages, prompts and AI answers go to OpenRouter and the model providers it calls. The author's company also sells a paid run-and-implement service; the skill itself is MIT.

## Review and maintenance

Reviewed **2026-11-23** (Europe/Sofia) at [commit 6db3cee2e18d](https://github.com/Svrubio7/quetzal-seo-audit-skill/tree/6db3cee2e18dc349d178de785068573dad4d0e70). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
