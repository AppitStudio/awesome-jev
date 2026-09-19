# Skillbox

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Self-host a versioned skill library for coding agents and optionally use Jev to recommend authorized skills for a task.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/kitze/skillbox) |
| Maintainer | [Kitze](https://github.com/kitze) and contributors. |
| Format | Developer skill library with a web editor, MCP server, HTTP API and CLI. |
| Stack | TypeScript, React, Bun, Hono and PostgreSQL. |
| Jev's role | Optional relevance scoring over task text and authorized skill descriptions; permissions, revisions, ranking and fallback remain in application code. |
| Requirements | Docker Engine/Desktop, Compose v2 and Bash on Linux, macOS or WSL; a provider account/key for Jev. Local development uses Bun and PostgreSQL 16+. |
| Access and costs | MIT source build without a purchase requirement; self-hosting and optional TypeSafe, OpenRouter or Vercel AI Gateway inference costs are separate. No hosted account is required. |
| License | [MIT](https://github.com/kitze/skillbox/blob/486c2a3caf36aca9cff5a43b7b2c59988f7509a2/LICENSE). |

## When to use

Use Skillbox when several coding agents need a shared skill catalog with immutable
revisions, client-specific grants and a task-aware discovery interface. Its Jev
integration also provides a reference for separating semantic relevance from
access control and falling back explicitly when model evaluation fails.

The reviewed release is a single-owner service. It starts with an empty library;
it is not a hosted marketplace or a preloaded collection of reviewed skills.

## How it works

The [recommender](https://github.com/kitze/skillbox/blob/486c2a3caf36aca9cff5a43b7b2c59988f7509a2/src/server/recommendations.ts)
constructs one score question per authorized, active leaf skill, using the task
and skill descriptions as evidence. Code accepts scores from 0 to 4, returns
scores at least 3, sorts ties by skill ID and attaches local immutable revisions.
The rubric is uncalibrated: a score is not a probability or a guarantee of fit.

The direct TypeSafe route uses `POST /v1/systemone` with `jev-latest`. Alternatives
are OpenRouter's `/api/alpha/decisions` with `typesafe/jev-1.13`, or Vercel AI
Gateway's evaluation endpoint with `typesafe-ai/jev`. These are the contracts in
the inspected source; provider access and live compatibility were not tested.

The complete authorized catalog is considered up to 200 skills and 120,000
serialized characters. Larger catalogs fall back instead of silently ranking a
subset. OpenRouter requests are additionally batched. Grants and catalog
revisions are rechecked after evaluation, including cached results.

## Get started

The following is the upstream source-build path, inspected but not executed.
Building downloads dependencies/images; it does not configure a paid provider.

```sh
git clone https://github.com/kitze/skillbox.git
cd skillbox
bash scripts/skillbox.sh setup
bash scripts/skillbox.sh start
```

Open `http://127.0.0.1:4791` and sign in using the generated
`SKILLBOX_ADMIN_TOKEN` in your private local `.env`. Create or import a skill,
create a profile with the required grants, then create a scoped client key.
Follow [self-hosting](https://github.com/kitze/skillbox/blob/486c2a3caf36aca9cff5a43b7b2c59988f7509a2/docs/self-hosting.md)
for HTTPS, backup and upgrades.

To enable live recommendations, open **Settings → Jev recommendations**, choose
a provider and save that provider's key. A recommendation then sends task text
and authorized skill IDs/descriptions to that provider and can incur charges.
Without a saved key, the same interface returns deterministic search fallback.

Configure the CLI using the protected client configuration described in the
[upstream instructions](https://github.com/kitze/skillbox#agents-and-cli), then run
with Node or Bun:

```sh
node cli/skillbox.mjs list
node cli/skillbox.mjs recommend "Fix choppy scrolling in an Expo app"
```

Results identify the recommendation method and selected skill revisions. Through
MCP, use `recommend_skills({task, limit?, offset?})`, then load selected skills
at the returned revisions. Recommendations do not execute skill code.

## Examples and demos

- The [README usage examples](https://github.com/kitze/skillbox#agents-and-cli) cover CLI and MCP configuration; no separate hosted demo was verified.
- [Recommendation tests](https://github.com/kitze/skillbox/blob/486c2a3caf36aca9cff5a43b7b2c59988f7509a2/tests/recommendations.test.ts) use synthetic scores and mocked provider responses to exercise ranking, cache isolation, authorization rechecks, validation and fallback.
- The [benchmark script](https://github.com/kitze/skillbox/blob/486c2a3caf36aca9cff5a43b7b2c59988f7509a2/scripts/benchmark-recommendations.ts) is a separate, explicitly live developer experiment; its synthetic sample does not establish production model quality.

## Limits and data handling

Failures, missing keys, invalid answers, capacity limits and an eight-second
deadline return lexical search with `method=search`, null relevance/no-match
fields and a fallback reason. There are no automatic retries. Semantic no-match
is reserved for a completed evaluation with no score reaching the threshold.
Returned confidence/probability fields are validated when present but do not
control ranking; the application retains scores rather than full raw responses.

Skills, revisions and settings reside in PostgreSQL. Provider keys are encrypted
server-side using key material derived from the owner token; changing that token
requires the documented credential-rotation procedure. The process-local score
cache has a five-minute lifetime. Imported skill content still needs review;
package validation and recommendations do not establish that instructions are safe.

## Review and maintenance

Reviewed on **2026-09-19** at commit
[`486c2a3caf36aca9cff5a43b7b2c59988f7509a2`](https://github.com/kitze/skillbox/commit/486c2a3caf36aca9cff5a43b7b2c59988f7509a2).
Inspected README/setup instructions, package metadata, MIT license, Compose and
launcher configuration, recommendation/provider code and representative mocked
tests. This was source inspection only: no installation, Docker run, upstream
test suite, provider request or recommendation-quality evaluation was performed.
Catalog checks are tracked separately in [validation scope](../../../docs/validation.md#community-project-checks).

AI-assisted catalog review; contributor affiliation/commercial relationships
were not supplied. Listing is not an endorsement.
