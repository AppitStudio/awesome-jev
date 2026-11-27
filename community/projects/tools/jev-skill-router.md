# JEV Skill Router by Luana-tex (Portuguese-language CLI and Codex skill where Jev picks which Agent Skills fit a task and drops overlapping ones)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Finds the Agent Skills installed for a project and for your user, then asks Jev which ones help with a given task. Candidates above a relevance threshold are picked in order, and remaining skills whose contribution is already covered are dropped, so the agent gets a short list instead of every skill. Also ships as an optional Codex skill. README and messages are in Portuguese.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Luana-tex/jev-skill-router) |
| Maintainer | [Luana-tex](https://github.com/Luana-tex). Independently curated. |
| Format | Node.js CLI (TypeScript) + Codex skill |
| Requirements | Node.js 22.12+ and a TypeSafe API key for `select` (listing skills needs no key). |
| License | [MIT](https://github.com/Luana-tex/jev-skill-router/blob/dc8f63d8b6c02bcd74e8aa18e104ea1db63d19ea/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/decision/jev.ts`](https://github.com/Luana-tex/jev-skill-router/blob/dc8f63d8b6c02bcd74e8aa18e104ea1db63d19ea/src/decision/jev.ts) at the pinned commit. |

## When to use

- Codex or Agent Skills users with many installed skills who want only the relevant few loaded.
- Mismatch: non-Portuguese readers may find the docs hard; the CLI recommends skills and does not load them.

## How it works

`src/decision/jev.ts` posts one `noul` question per candidate skill to `https://api.typesafe.ai/v1/systemone` (model `jev-latest`) for relevance, then redundancy questions against already chosen skills; thresholds default to 0.7 and 0.8 and can be changed, as can the criteria text. Integration evidence: [`src/decision/jev.ts`](https://github.com/Luana-tex/jev-skill-router/blob/dc8f63d8b6c02bcd74e8aa18e104ea1db63d19ea/src/decision/jev.ts).

## Get started

Build from source, list the skills it finds, then ask it to select for a task.

```sh
git clone https://github.com/Luana-tex/jev-skill-router && cd jev-skill-router
npm ci && npm run build
node dist/cli.js list
node --env-file=.env dist/cli.js select "Revisar componentes React" --max-skills 3
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Codex skill: [github.com/Luana-tex/jev-skill-router/tree/main/codex/jev-skill-router](https://github.com/Luana-tex/jev-skill-router/tree/main/codex/jev-skill-router)
- Roadmap: [github.com/Luana-tex/jev-skill-router/blob/main/ROADMAP.md](https://github.com/Luana-tex/jev-skill-router/blob/main/ROADMAP.md)

## Limits and data handling

The task text and each candidate skill's name and description go to TypeSafe; skill files are read as data and never run. Single-commit project at review time.

## Review and maintenance

Reviewed **2026-11-27** (Europe/Sofia) at [commit dc8f63d8b6c0](https://github.com/Luana-tex/jev-skill-router/tree/dc8f63d8b6c02bcd74e8aa18e104ea1db63d19ea). Inspected the README, LICENSE and `src/decision/jev.ts` at the pinned commit; nothing was installed or run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
