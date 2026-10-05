# changelog-bot

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

AI changelog CLI and GitHub Action with an experimental `--why-engine jev`: Jev checks each PR-description candidate for an explicit reason that applies to the change, and the strongest accepted text is quoted without paraphrase.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/nyaomaru/changelog-bot) |
| Maintainer | [nyaomaru](https://github.com/nyaomaru). Independently curated. |
| Format | CLI, composite GitHub Action and reusable workflow |
| Requirements | Node.js with pnpm/npx; an LLM provider key for the changelog itself; `TYPESAFE_API_KEY` for the Jev WHY engine (`TYPESAFE_MODEL` optional, default `jev-latest`). |
| License | [MIT](https://github.com/nyaomaru/changelog-bot/blob/51b204554ae09fdbe58be0fb531a6b77c0cd56c7/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Add a "why" to each changelog entry without letting a model invent rationale.
- Evaluate Jev against an LLM provider on your own labelled WHY corpus (`pnpm eval:why`).
- Mismatch: Jev selects, it does not write; the changelog text still comes from the LLM provider (or none with `--no-ai`).

## How it works

For each change, Jev answers two questions per PR-description candidate: does it explicitly state a reason, and does that reason apply to this change. A candidate is accepted only when both probabilities are at least 0.50; the lower one maps to low/medium/high confidence (default bar medium, 0.60). Retryable 429/529 responses back off up to 30 s, and missing credentials skip WHY extraction with a diagnostic ([README](https://github.com/nyaomaru/changelog-bot/blob/51b204554ae09fdbe58be0fb531a6b77c0cd56c7/README.md#experiment-with-typesafe-jev-for-why-selection)).

## Get started

Dry-run a release with the Jev WHY engine (live TypeSafe calls):

```sh
export TYPESAFE_API_KEY=...
pnpm dlx @nyaomaru/changelog-bot \
  --release-tag HEAD --release-name 1.2.3 \
  --why --why-engine jev --dry-run
```

Live commands contact TypeSafe (or the configured provider) and may incur charges.

## Examples and demos

- README *Evaluate Jev WHY selection*: `pnpm eval:why` prints precision, recall, F1 and source preservation for Jev and one LLM provider on the labelled corpus.

## Limits and data handling

Experimental upstream; thresholds may change. PR descriptions are sent to TypeSafe. No evaluation results are claimed here; not run on the review host.

## Review and maintenance

Reviewed **2026-10-06** (Europe/Sofia) at [commit 51b204554ae0](https://github.com/nyaomaru/changelog-bot/tree/51b204554ae09fdbe58be0fb531a6b77c0cd56c7). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
