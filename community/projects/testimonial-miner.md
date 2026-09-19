# Testimonial miner

[All projects](../README.md) · [Customer feedback and marketing](../README.md#customer-feedback-and-marketing)

Find useful customer praise in a Gmail inbox and collect the sender's actual words for review, grouped by product.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/AppitStudio/testimonial-miner) |
| Maintainer | [AppIt Studio](https://github.com/AppitStudio), which also maintains Awesome Jev; self-submission. |
| Format | Python CLI with a local review dashboard. |
| Requirements | Python 3.12+, uv; a TypeSafe key for inference and Google app passwords for Gmail access. |
| License | [MIT](https://github.com/AppitStudio/testimonial-miner/blob/main/LICENSE). |

## When to use

- You receive product feedback by email and want a reviewable shortlist of possible testimonials.
- You manage several products and need candidate quotes grouped by app.
- You want to study a complete Jev workflow that selects source sentences and reapplies policy without repeating inference.

It does not write promotional quotes or decide whether you have permission to publish private correspondence.

## How it works

Code filters mail headers, removes quoted replies, and splits the sender's message into sentences. Jev judges message type, app, praise quality, and individual sentences. Code assembles selected sentences in order and records candidates, borderline results, and review metadata. The [configuration](https://github.com/AppitStudio/testimonial-miner/blob/0852a28f6961935afe440b1d698ce22412a4a7ec/testimonial_miner/config.py) holds the policy thresholds and model setting.

## Get started

Clone it separately from Awesome Jev and run the offline tests first:

```sh
git clone https://github.com/AppitStudio/testimonial-miner.git
cd testimonial-miner
uv sync --frozen
uv run python -m unittest discover -s tests -v
```

The tests use fake mail and model responses and need no `.env`. For real use, follow the upstream [setup instructions](https://github.com/AppitStudio/testimonial-miner#setup): configure a private `API_KEY` (the loader also accepts `TYPESAFE_API_KEY`), mailbox credentials, and your own product names in `apps.json`. Check Google account eligibility and organization restrictions in those instructions. Pin `TYPESAFE_MODEL` when evaluating a policy.

After configuration, preview a bounded selection:

```sh
uv run python -m testimonial_miner scan --limit 10 --dry-run
```

This reads Gmail but makes no model calls; it is not an offline command. The current loader still requires a configured TypeSafe key. Once you intend to send those messages to TypeSafe, remove `--dry-run` to judge them. `--limit` bounds selected messages per mailbox, not total HTTP attempts across accounts and SDK retries.

After a scan, open the local review dashboard:

```sh
uv run python -m testimonial_miner web
```

Visit `http://127.0.0.1:8765` to inspect quotes and their context. The [CLI implementation](https://github.com/AppitStudio/testimonial-miner/blob/0852a28f6961935afe440b1d698ce22412a4a7ec/testimonial_miner/cli.py) also provides list, stats, and `redecide` commands.

## Examples and demos

- [Synthetic email fixtures](https://github.com/AppitStudio/testimonial-miner/tree/main/fixtures) — inspect realistic inputs without supplying your inbox.
- [Fixture test and live-run instructions](https://github.com/AppitStudio/testimonial-miner#tests) — distinguish mocked tests from optional billed inference.
- [Dashboard walkthrough](https://github.com/AppitStudio/testimonial-miner#local-review-dashboard) — search, filter, and inspect stored candidates.
- [Policy tuning](https://github.com/AppitStudio/testimonial-miner#decisions-and-tuning) — apply different thresholds to saved judgments with `redecide`.

## Limits and data handling

Gmail access is read-only. Judged messages send sender identity, subject, cleaned text, and the app catalog to TypeSafe; model calls may incur charges. Local data files contain message content and should stay private. Long messages are truncated, and thresholds need evaluation on your own mail. Review the original context and obtain appropriate permission before publishing a quote. See the project's [data flow](https://github.com/AppitStudio/testimonial-miner#where-your-data-goes).

## Review and maintenance

Documentation and selected source were inspected on 2026-09-19 at [0852a28](https://github.com/AppitStudio/testimonial-miner/tree/0852a28f6961935afe440b1d698ce22412a4a7ec). [Submission PR #5](https://github.com/AppitStudio/awesome-jev/pull/5) records the submitter's 26 offline tests and bounded live fixture check; these were not rerun for this page. The [project CI](https://github.com/AppitStudio/testimonial-miner/actions/runs/35393194082) and [catalog validation](../../docs/validation.md#community-project-checks) give the review scope. No independent workload-accuracy evaluation is claimed.

Related: [span selection](../../examples/span-selection/README.md) for a smaller source-selection example; [quality rubric](../../examples/quality-rubric/README.md) for combining independent judgments.
