# golla-jev (Claude Code plugin that finds the pick-one moments in your work and designs a workflow that hands them to Jev)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Claude Code plugin that takes a description of your work, finds the steps that are really a choice between fixed options, and returns a workflow design that gives those choices to Jev, arithmetic and lookups to code, wording to templates and photo or audio reading to a multimodal model, with draft Jev question JSON and a test plan.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/fivetaku/golla-jev) |
| Maintainer | [fivetaku](https://github.com/fivetaku). Independently curated. |
| Format | Claude Code plugin with a bundled Python benchmark template (MIT) |
| Requirements | Claude Code; a TypeSafe key (`TYPESAFE_API_KEY`) only to run the drafted questions or the bundled benchmark. Design output alone needs no key. |
| License | [MIT](https://github.com/fivetaku/golla-jev/blob/4b7f0a1a76d88bb2a6ead62abcd6997312edfaa1/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`skills/golla-jev/bench/run.py`](https://github.com/fivetaku/golla-jev/blob/4b7f0a1a76d88bb2a6ead62abcd6997312edfaa1/skills/golla-jev/bench/run.py) at the pinned commit. |

## When to use

- Find where Jev could take over routine choices in office work (expense categories, mail triage, contract clauses) before writing any code.
- Get a concrete question design and a threshold test plan you can run on your own sample.
- Mismatch: a ready-made automation; the plugin produces designs and drafts, not a running workflow.

## How it works

The skill in `skills/golla-jev/` produces a step table, Jev question drafts with an example state, an output preview tagging each field by who fills it, and a dev/holdout threshold procedure. The bundled benchmark (`skills/golla-jev/bench/run.py`) sends items to `https://api.typesafe.ai/v1/systemone` with `jev-latest`; the author reports 96.3% on a 108-item Korean office benchmark with jev-1.14.0 and notes that the auto-handle threshold should be re-picked when the model changes. These are author-reported figures. Integration evidence: [`skills/golla-jev/bench/run.py`](https://github.com/fivetaku/golla-jev/blob/4b7f0a1a76d88bb2a6ead62abcd6997312edfaa1/skills/golla-jev/bench/run.py).

## Get started

Add the gptaku plugin marketplace in Claude Code, install the plugin, restart, then describe a task with `/golla-jev`.

```sh
/plugin marketplace add https://github.com/fivetaku/gptaku_plugins.git
/plugin install golla-jev
/golla-jev I want to automate our team's receipt reimbursements
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README with example designs: [github.com/fivetaku/golla-jev/blob/4b7f0a1a76d88bb2a6ead62abcd6997312edfaa1/README.md](https://github.com/fivetaku/golla-jev/blob/4b7f0a1a76d88bb2a6ead62abcd6997312edfaa1/README.md)
- Example design (receipts to expense report): [github.com/fivetaku/golla-jev/blob/4b7f0a1a76d88bb2a6ead62abcd6997312edfaa1/examples/01-expense-report.md](https://github.com/fivetaku/golla-jev/blob/4b7f0a1a76d88bb2a6ead62abcd6997312edfaa1/examples/01-expense-report.md)

## Limits and data handling

Task descriptions go to Claude Code's model; only benchmark or question runs send items to TypeSafe on your key. Bundled benchmark items are hand-written, not customer data.

## Review and maintenance

Reviewed **2026-11-13** (Europe/Sofia) at [commit 4b7f0a1a76d8](https://github.com/fivetaku/golla-jev/tree/4b7f0a1a76d88bb2a6ead62abcd6997312edfaa1). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
