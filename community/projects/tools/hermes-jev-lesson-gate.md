# hermes-jev-lesson-gate

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Hermes Agent plugin: TypeSafe Jev (OpenRouter Decisions) judges when memory/skill background review should run—replacing a fixed every-N-turns clock.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/VBS2004/hermes-jev-lesson-gate) |
| Maintainer | [VBS2004](https://github.com/VBS2004). Independently curated. |
| Format | Hermes plugin directory `jev_lesson_gate`. |
| Requirements | Hermes Agent with background-review hooks; OpenRouter access to `typesafe/jev-1.13`. |
| License | [MIT](https://github.com/VBS2004/hermes-jev-lesson-gate/blob/838bdd45326cb61ba945d4a0cae49a37c7060bc7/LICENSE). OpenRouter/TypeSafe usage may incur charges. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Upstream AUC figures are small/in-sample—not re-run here. Requires Hermes hook support noted upstream. Live Hermes/OpenRouter paths not run on the review host. |

## When to use

Use when Hermes background reviews should fire on lesson signals rather than turn counters. Prefer [hermes-jev-skills](hermes-jev-skills.md) for broader Jev skill routing.

## How it works

After each turn, asks Jev whether the user corrected the assistant, revealed a lasting fact, or the agent discovered a lasting method; returns review/skip directives per memory vs skills when Hermes allows judgment skips.

## Get started

```sh
git clone https://github.com/VBS2004/hermes-jev-lesson-gate.git
cd hermes-jev-lesson-gate
git checkout 838bdd45326cb61ba945d4a0cae49a37c7060bc7
# cp -r jev_lesson_gate ~/.hermes/plugins/  # per upstream
```

## Examples and demos

- Upstream measured AUC tables and cost note (~$0.00004/call, author-reported).

## Limits and data handling

Turn summaries/messages go to OpenRouter Decisions. Catalog checks did not install Hermes or run live judgments.

## Review and maintenance

Reviewed **2026-09-30** (Europe/Sofia) at [commit 838bdd4](https://github.com/VBS2004/hermes-jev-lesson-gate/tree/838bdd45326cb61ba945d4a0cae49a37c7060bc7). AI-assisted README and license inspection; install/live paths not executed.
