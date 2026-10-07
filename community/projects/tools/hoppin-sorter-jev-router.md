# jev-router (Hoppin-Sorter)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Before each prompt, asks TypeSafe Jev what the task is (difficulty, subject, output kind) and which of your skills fits; code then picks the Claude or OpenAI model and optional effort with a quality/cost focus slider. Ships as a Claude Code plugin, a TypeScript/Python router library, a Codex CLI launcher and an optional macOS menu-bar widget. Distinct from the separately listed jev-router.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Hoppin-Sorter/jev-router) |
| Maintainer | [Hoppin-Sorter](https://github.com/Hoppin-Sorter). Independently curated. |
| Format | Claude Code plugin (function hooks), router library (`lib/jev-router.ts`, `lib/jev_router.py`), Codex launcher, macOS widget |
| Requirements | Your own TypeSafe API key; Claude Code (tested upstream on 2.1.293) or your own app on the Claude/OpenAI API. |
| License | [MIT](https://github.com/Hoppin-Sorter/jev-router/blob/7b7b8497830dd0be512e130a3fa6b6f7315cf587/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Stop top-tier models handling trivial edits in Claude Code.
- Nudge the agent towards a matching skill when Jev sees a clear fit.
- Mismatch: early access (depends on Claude Code's function-hooks API); see also the other [jev-router](jev-router.md) listing.

## How it works

[`lib/jev-router.ts`](https://github.com/Hoppin-Sorter/jev-router/blob/7b7b8497830dd0be512e130a3fa6b6f7315cf587/lib/jev-router.ts) sends one Jev request per prompt with task and skill questions; code maps the answers to a model and effort. [`hooks/register.tsx`](https://github.com/Hoppin-Sorter/jev-router/blob/7b7b8497830dd0be512e130a3fa6b6f7315cf587/hooks/register.tsx) wires it into Claude Code; [`eval/`](https://github.com/Hoppin-Sorter/jev-router/tree/7b7b8497830dd0be512e130a3fa6b6f7315cf587/eval) holds a prompt set and runner.

## Get started

Install the Claude Code plugin (README), then add your TypeSafe key as described there:

```sh
claude plugin marketplace add Hoppin-Sorter/jev-router
claude plugin install jev-router@jev-router
```

One Jev request per prompt (upstream: about 0.3 s and a fraction of a cent), billed to your TypeSafe key.

## Examples and demos

- README routing examples and *Which one do I use?* table.
- Eval prompts: [`eval/prompts.jsonl`](https://github.com/Hoppin-Sorter/jev-router/blob/7b7b8497830dd0be512e130a3fa6b6f7315cf587/eval/prompts.jsonl).

## Limits and data handling

Each prompt's text goes to TypeSafe. Model names and settings are upstream choices. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-08** (Europe/Sofia) at [commit 7b7b8497830d](https://github.com/Hoppin-Sorter/jev-router/tree/7b7b8497830dd0be512e130a3fa6b6f7315cf587). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
