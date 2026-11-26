# Jev na prática by INEMA TDS (free Portuguese course on Jev: 3 tracks, 12 modules, 36 lessons and 12 labs)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Free, self-paced course in Portuguese on using Jev: where it fits, the three question types, confidence and error, cost, support and transcripts, documents and evidence, agents, browser and sensitive applications, integration, quality measurement and operations, ending in a final project. Modules 1–8 need no code; 9–12 use JSON, the terminal and Python. Lessons are in Markdown and an HTML course site, with Spanish and English material in progress.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/inematds/jev-curso) |
| Maintainer | [Nei Maldaner / INEMA TDS](https://github.com/inematds). Independently curated. |
| Format | Course (Markdown lessons + static HTML site) |
| Requirements | A browser; for the technical modules, Python and a TypeSafe or OpenRouter key to run the companion lab for real. |
| License | [MIT](https://github.com/inematds/jev-curso/blob/ffcc5184a21080cf796f0aa4ae79324ba4ebe4bf/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`aulas/modulo-09.md`](https://github.com/inematds/jev-curso/blob/ffcc5184a21080cf796f0aa4ae79324ba4ebe4bf/aulas/modulo-09.md) at the pinned commit. |

## When to use

- Portuguese-speaking product, ops or engineering teams who want a structured introduction to Jev before building.
- Mismatch: up-to-date pricing or model limits; the course's prices were checked on 2026-09-18, so confirm in TypeSafe's docs.

## How it works

Lessons such as `aulas/modulo-09.md` (integration) walk through calling Jev from the companion Jev Decision Lab, directly or via OpenRouter's Decisions API (`~typesafe/jev-latest`), and keeping the decision separate from the action. Integration evidence: [`aulas/modulo-09.md`](https://github.com/inematds/jev-curso/blob/ffcc5184a21080cf796f0aa4ae79324ba4ebe4bf/aulas/modulo-09.md).

## Get started

Open the HTML course or read the Markdown lessons in order.

```sh
https://inematds.github.io/jev-curso/
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Course site: [inematds.github.io/jev-curso/](https://inematds.github.io/jev-curso/)
- Final project: [github.com/inematds/jev-curso/blob/ffcc5184a21080cf796f0aa4ae79324ba4ebe4bf/materiais/projeto-final.md](https://github.com/inematds/jev-curso/blob/ffcc5184a21080cf796f0aa4ae79324ba4ebe4bf/materiais/projeto-final.md)

## Limits and data handling

Independent educational course, not TypeSafe material. Clinical, legal and financial cases are fictional; simulations in the labs do not prove Jev's performance (the course says so). Pricing in the exercises dates from 2026-09-18.

## Review and maintenance

Reviewed **2026-11-26** (Europe/Sofia) at [commit ffcc5184a210](https://github.com/inematds/jev-curso/tree/ffcc5184a21080cf796f0aa4ae79324ba4ebe4bf). Inspected the README, LICENSE and lesson files at the pinned commit; the course site was not reviewed lesson by lesson. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
