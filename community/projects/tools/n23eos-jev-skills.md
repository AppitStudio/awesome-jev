# Jev Skills (n23eos)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Fourteen installable Claude Code and Codex skills plus a CLI where TypeSafe Jev makes one bounded choice (skill, model, context file, first test, bug component or plan) and the coding agent does the work; distinct from the listed jev-skills plugin.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/n23eos/jev-skills) |
| Maintainer | [n23eos](https://github.com/n23eos). Independently curated. |
| Format | Agent skill pack with installer and doctor CLI |
| Requirements | uv, Git and curl (or the isolated Python install); Claude Code or Codex; `TYPESAFE_API_KEY` in the environment that starts the agent for live decisions. |
| License | [MIT](https://github.com/n23eos/jev-skills/blob/ff2d92b07091209c03d455d562f58c928b7b9e4e/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Several installed skills or next steps plausibly fit and choosing needs judgment.
- Pick which existing test to run first or which component to investigate first for a change.
- Mismatch: upstream says to skip it when the answer is obvious, a project rule decides, or the request is private; it does not claim better or cheaper outcomes.

## How it works

Each skill asks Jev one bounded Choice over candidates the agent supplies (installed skills, configured models, files, tests, components or plans) and hands the result back; the agent still verifies fit and performs the task. `jev-skills doctor` checks setup without contacting TypeSafe, and installation enables no automatic network calls ([README](https://github.com/n23eos/jev-skills/blob/ff2d92b07091209c03d455d562f58c928b7b9e4e/README.md)).

## Get started

Install the CLI and skills, check setup, then invoke one skill from the agent (one live Jev decision):

```sh
uv tool install 'git+https://github.com/n23eos/jev-skills.git'
jev-skills install --agent codex   # or --agent claude
jev-skills doctor --format human
export TYPESAFE_API_KEY=...
```

Live commands contact TypeSafe (or the configured provider) and may incur charges.

## Examples and demos

- README sample prompt for `$jev-test-prioritizer` / `/jev-test-prioritizer` and CLI examples; [Getting started](https://github.com/n23eos/jev-skills/blob/ff2d92b07091209c03d455d562f58c928b7b9e4e/docs/getting-started.md).

## Limits and data handling

Each live decision sends the supplied candidates and context to TypeSafe and is billed separately from your Codex/Claude subscription. Recommendations do not switch an existing conversation's model.

## Review and maintenance

Reviewed **2026-10-05** (Europe/Sofia) at [commit ff2d92b07091](https://github.com/n23eos/jev-skills/tree/ff2d92b07091209c03d455d562f58c928b7b9e4e). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
