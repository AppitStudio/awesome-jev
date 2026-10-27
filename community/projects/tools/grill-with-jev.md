# grill-with-jev (agent skill that grills a plan in rounds, with Jev deciding)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Agent skill from 1arley's skills collection: the host agent builds a design tree, asks each round of open questions with a recommended answer, and Jev, acting as the user's automated stand-in, decides through schema-validated answers; ends with a decision record of decisions, provenance, assumptions and open risks. Budget, round and session limits are enforced by the script.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/1arley/skills) |
| Maintainer | [1arley](https://github.com/1arley). Independently curated. |
| Format | Agent skill (TypeScript scripts) |
| Requirements | An agent that supports skills (via `npx skills`); a TypeSafe API key or another configured endpoint. |
| License | [MIT](https://github.com/1arley/skills/blob/3a44b6190f769fa2c308b8cfa59ea1b9315917f9/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`skills/productivity/grill-with-jev/scripts/ask-jev.ts`](https://github.com/1arley/skills/blob/3a44b6190f769fa2c308b8cfa59ea1b9315917f9/skills/productivity/grill-with-jev/scripts/ask-jev.ts) at the pinned commit. |

## When to use

- Pressure-test a plan quickly without answering every question yourself.
- Mismatch: explicit invocation only; each call may spend API credits; other skills in the collection are unrelated to Jev.

## How it works

`skills/productivity/grill-with-jev/scripts/ask-jev.ts` posts each round to `/v1/systemone` (default `https://api.typesafe.ai/v1`) and validates answers against the round schema. Integration evidence: [`skills/productivity/grill-with-jev/scripts/ask-jev.ts`](https://github.com/1arley/skills/blob/3a44b6190f769fa2c308b8cfa59ea1b9315917f9/skills/productivity/grill-with-jev/scripts/ask-jev.ts).

## Get started

From the upstream README (not run on the review host):

```sh
npx skills add 1arley/skills --skill grill-with-jev
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Skill: [github.com/1arley/skills/blob/master/skills/productivity/grill-with-jev/SKILL.md](https://github.com/1arley/skills/blob/master/skills/productivity/grill-with-jev/SKILL.md)

## Limits and data handling

Round questions and context go to the configured endpoint. Read the skill's security notes before setup.

## Review and maintenance

Reviewed **2026-10-27** (Europe/Sofia) at [commit 3a44b6190f76](https://github.com/1arley/skills/tree/3a44b6190f769fa2c308b8cfa59ea1b9315917f9). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
