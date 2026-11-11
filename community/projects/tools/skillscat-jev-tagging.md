# SkillsCat (agent-skill directory with Jev fallback classification and security tags)

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

Open platform behind skills.cat for discovering and installing AI agent skills; its classification and security-analysis workers can fall back to Jev for category and risk tagging.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/SkillsCat/skillscat) |
| Maintainer | [SkillsCat](https://github.com/SkillsCat). Independently curated. |
| Format | Cloudflare Workers web platform (TypeScript, AGPL-3.0) |
| Requirements | Cloudflare Workers to self-host, OpenRouter keys, and an optional `TYPESAFE_API_KEY` secret on the two workers. |
| License | [AGPL-3.0](https://github.com/SkillsCat/skillscat/blob/d555ed361855bcba7da4a72bed2ca4ba27cf1ca1/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`apps/web/workers/shared/ai/typesafe.ts`](https://github.com/SkillsCat/skillscat/blob/d555ed361855bcba7da4a72bed2ca4ba27cf1ca1/apps/web/workers/shared/ai/typesafe.ts) at the pinned commit. |

## When to use

- See Jev as a fallback classifier in a multi-model pipeline.
- Self-host a skills directory.
- Mismatch: AGPL-3.0; Jev is optional and only a fallback.

## How it works

`apps/web/workers/shared/ai/typesafe.ts` calls `/v1/systemone` via `fetch`; per `docs/typesafe.md` (Chinese), free OpenRouter models run first and Jev noul/score questions are tried when they fail, before a paid model and keywords. Integration evidence: [`apps/web/workers/shared/ai/typesafe.ts`](https://github.com/SkillsCat/skillscat/blob/d555ed361855bcba7da4a72bed2ca4ba27cf1ca1/apps/web/workers/shared/ai/typesafe.ts).

## Get started

Self-host per the README and set `TYPESAFE_API_KEY` on the classification and security-analysis workers.

```sh
git clone https://github.com/SkillsCat/skillscat.git
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- TypeSafe integration notes: [github.com/SkillsCat/skillscat/blob/d555ed361855bcba7da4a72bed2ca4ba27cf1ca1/docs/typesafe.md](https://github.com/SkillsCat/skillscat/blob/d555ed361855bcba7da4a72bed2ca4ba27cf1ca1/docs/typesafe.md)

## Limits and data handling

Skill text goes to TypeSafe only when the fallback runs and a key is set.

## Review and maintenance

Reviewed **2026-11-11** (Europe/Sofia) at [commit d555ed361855](https://github.com/SkillsCat/skillscat/tree/d555ed361855bcba7da4a72bed2ca4ba27cf1ca1). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
