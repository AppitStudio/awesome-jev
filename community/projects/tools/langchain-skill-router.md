# Skill Router (LangChain)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Drop-in replacement for the deepagents `SkillsMiddleware` that picks which `SKILL.md` skills to load each turn with a pluggable judge; the included `JevJudge` adapter uses TypeSafe Jev.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/deyna256/langchain-skill-router) |
| Product homepage | [pypi.org](https://pypi.org/project/langchain-skill-router/) |
| Maintainer | [deyna256](https://github.com/deyna256). Independently curated. |
| Format | Python middleware library for LangChain deepagents |
| Requirements | Python, LangChain deepagents, `pip install "langchain-skill-router[jev]"`, `TYPESAFE_API_KEY` plus your agent model provider's key. |
| License | [MIT](https://github.com/deyna256/langchain-skill-router/blob/22de948a9159cb4463e38a6e754711195d133c61/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Keep a large skill catalog out of every prompt and load the right skill on each turn.
- Swap in your own judge (self-hosted model or rules) behind the same routing core.
- Mismatch: small catalogs that fit comfortably in context gain little.

## How it works

Each turn the judge ranks catalog skills (catalogs larger than Jev's per-call limits, 32k tokens / 255 options, are split and re-ranked), then reads the start of top candidates' `SKILL.md` to verify fit; a confident ranking skips the second call. `on_decision=` receives probabilities, stage and timing for logs ([README](https://github.com/deyna256/langchain-skill-router/blob/22de948a9159cb4463e38a6e754711195d133c61/README.md)).

## Get started

Install with the Jev adapter and pass `JevJudge()` to the middleware (live Jev calls per turn):

```sh
pip install "langchain-skill-router[jev]"
export TYPESAFE_API_KEY=...
# from langchain_skill_router.providers.jev import JevJudge
# skill_router = SkillRouterMiddleware(backend=backend, sources=["/skills/"], judge=JevJudge())
```

Live commands contact TypeSafe (or the configured provider) and may incur charges.

## Examples and demos

- README benchmark on a 236-skill catalog (55 conversations × 5 turns): maintainer-reported 113.0k → 25.8k input tokens per turn and 88% → 90% correct answers. Not reproduced here.

## Limits and data handling

User turns and skill descriptions go to TypeSafe and are billed per decision. Independent project; benchmark figures are upstream-reported.

## Review and maintenance

Reviewed **2026-10-05** (Europe/Sofia) at [commit 22de948a9159](https://github.com/deyna256/langchain-skill-router/tree/22de948a9159cb4463e38a6e754711195d133c61). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
