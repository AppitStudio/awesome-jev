# effortless

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Claude Code mod that picks the reasoning effort for every prompt with a judge — Jev (TypeSafe key, about 0.25 s), Haiku on your Claude login, or your own OpenAI-compatible model — and shows a prompt-cache countdown with one-click Compact.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/HeyCubit/effortless) |
| Maintainer | [HeyCubit](https://github.com/HeyCubit). Independently curated. |
| Format | Claude Code plugin (marketplace install) |
| Requirements | Claude Code; optional `TYPESAFE_API_KEY` for the Jev judge (default `auto` uses Jev when a key is set, Haiku otherwise). |
| License | [MIT](https://github.com/HeyCubit/effortless/blob/15b9661f2bec5a711c7969abbf6f14d3a62a4f4f/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Save effort/latency on simple Claude Code prompts while keeping high effort for complex jobs.
- Compare Jev and Haiku as prompt-difficulty judges with the bundled labelled cases.
- Mismatch: changing effort yourself turns Auto off; without a key it uses Haiku, not Jev.

## How it works

A prompt hook ([`hooks/register.tsx`](https://github.com/HeyCubit/effortless/blob/15b9661f2bec5a711c7969abbf6f14d3a62a4f4f/hooks/register.tsx)) sends the prompt to the selected judge and sets the effort level before the turn; the status line shows the chosen level and the time until the prompt cache goes cold.

## Get started

Install from the plugin marketplace inside Claude Code:

```sh
/plugin marketplace add HeyCubit/effortless
/plugin install effortless@effortless
# restart Claude Code; pick Jev (key), Haiku or your own AI in the setup
```

The Jev judge sends each prompt to TypeSafe (billed to your key); Haiku uses your Claude plan.

## Examples and demos

- `bench/judge-cases.json` labelled cases and the README *How often the judge is right* section (upstream numbers).

## Limits and data handling

Judge accuracy figures are upstream; not reproduced. Prompts are sent to the chosen judge. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-06** (Europe/Sofia) at [commit 15b9661f2bec](https://github.com/HeyCubit/effortless/tree/15b9661f2bec5a711c7969abbf6f14d3a62a4f4f). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
