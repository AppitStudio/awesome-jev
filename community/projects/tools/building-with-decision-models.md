# Building with Decision Models

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Unofficial agent skill that teaches coding agents to design for decision models (TypeSafe Jev, Cloudflare Clef, pplx-decider, OpenAI Decisions, Databricks `ai_decide`, Ollama models and more): typed questions, calibrated confidence, per-provider reference files and a prior-art library of 450+ community projects sorted by pattern.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/aaddrick/building-with-decision-models) |
| Maintainer | [aaddrick](https://github.com/aaddrick). Independently curated. |
| Format | Agent skill packaged as a Claude Code plugin marketplace, Gemini extension and plain skill folder |
| Requirements | A supported coding agent (Claude Code, Codex, Gemini CLI, others via the skill folder); a provider key only if the agent then calls a model. |
| License | [MIT](https://github.com/aaddrick/building-with-decision-models/blob/7879fac8af8a5d6c15a0985f7ec72d8bdf0e6689/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Have a coding agent pick the right question type (Choice / Score / Noul) and confidence handling when adding Jev to code.
- Compare provider wire formats and switch between Jev, Clef or local deciders with the provider reference files.
- Mismatch: unofficial and not endorsed by TypeSafe or any provider; TypeSafe also publishes its own official skill (README explains the difference).

## How it works

The skill entry point [`SKILL.md`](https://github.com/aaddrick/building-with-decision-models/blob/7879fac8af8a5d6c15a0985f7ec72d8bdf0e6689/skills/building-with-decision-models/SKILL.md) loads when the agent works on decision-model code. Provider files such as [`providers/jev.md`](https://github.com/aaddrick/building-with-decision-models/blob/7879fac8af8a5d6c15a0985f7ec72d8bdf0e6689/skills/building-with-decision-models/providers/jev.md) cover each API; [`patterns.md`](https://github.com/aaddrick/building-with-decision-models/blob/7879fac8af8a5d6c15a0985f7ec72d8bdf0e6689/skills/building-with-decision-models/patterns.md) and the [prior-art index](https://github.com/aaddrick/building-with-decision-models/blob/7879fac8af8a5d6c15a0985f7ec72d8bdf0e6689/skills/building-with-decision-models/prior-art/INDEX.md) link community projects by shape (gates, judges, control loops and more).

## Get started

Install in Claude Code (README *Install*):

```sh
claude plugin marketplace add aaddrick/building-with-decision-models
claude plugin install building-with-decision-models@building-with-decision-models
```

The skill itself makes no model calls; code the agent writes may call paid providers.

## Examples and demos

- README *What is inside* and *The prior-art library*.
- Model switching guide: [`choosing-and-switching-models.md`](https://github.com/aaddrick/building-with-decision-models/blob/7879fac8af8a5d6c15a0985f7ec72d8bdf0e6689/skills/building-with-decision-models/choosing-and-switching-models.md).

## Limits and data handling

Documentation-only skill; accuracy notes are the author's compilation of community evidence. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-07** (Europe/Sofia) at [commit 7879fac8af8a](https://github.com/aaddrick/building-with-decision-models/tree/7879fac8af8a5d6c15a0985f7ec72d8bdf0e6689). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
