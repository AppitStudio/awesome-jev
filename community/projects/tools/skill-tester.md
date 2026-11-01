# skill-tester (eval harness for agent skills with headless agent runs, Jev judge packs and blind human review)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Eval harness for agent skills: it generates outputs with headless coding agents (Claude Code, Cursor's agent), grades them with code checks and Jev judge packs, keeps runs and reports, and offers blind human review in a local web app. Jev is the judge for every pack.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/milesroxas/skill-tester) |
| Maintainer | [milesroxas](https://github.com/milesroxas). Independently curated. |
| Format | CLI (`pnpm st`) + local web app (TypeScript) |
| Requirements | Node.js with pnpm; Claude Code or Cursor CLI for generation; a TypeSafe key for grading. |
| License | [MIT](https://github.com/milesroxas/skill-tester/blob/c12ef5b1cbf38c8dfa42571ae984428c9a232c9c/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`server/jev.ts`](https://github.com/milesroxas/skill-tester/blob/c12ef5b1cbf38c8dfa42571ae984428c9a232c9c/server/jev.ts) at the pinned commit. |

## When to use

- Compare versions of a SKILL.md on fixed cases with repeatable judged scores.
- Mismatch: without a TypeSafe key every judged layer is null.

## How it works

`server/jev.ts` and `judges/shared/questions.ts` build Jev questions (noul, score, image) with `@typesafe-ai/sdk`; judge packs under `judges/` grade Markdown, HTML or screenshots and store raw Jev answers next to thresholds. Integration evidence: [`server/jev.ts`](https://github.com/milesroxas/skill-tester/blob/c12ef5b1cbf38c8dfa42571ae984428c9a232c9c/server/jev.ts).

## Get started

From the upstream README (not run on the review host):

```sh
pnpm install
cp .env.example .env   # set TYPESAFE_API_KEY
pnpm st run <skill-dir> --engine claude --model sonnet
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/milesroxas/skill-tester#readme](https://github.com/milesroxas/skill-tester#readme)

## Limits and data handling

Generated artifacts are sent to TypeSafe for grading. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-01** (Europe/Sofia) at [commit c12ef5b1cbf3](https://github.com/milesroxas/skill-tester/tree/c12ef5b1cbf38c8dfa42571ae984428c9a232c9c). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
