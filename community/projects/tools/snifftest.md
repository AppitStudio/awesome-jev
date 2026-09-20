# Sniff Test

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Prose linter for Markdown and plain text: free local countable (regex) rules plus optional TypeSafe Jev judgment rules when you confirm sending paragraphs. It flags lines; it does not rewrite your draft.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/DanRWilloughby/snifftest) |
| Maintainer | [DanRWilloughby](https://github.com/DanRWilloughby). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Node/Bun CLI **snifftest 0.1.0** (`snifftest check`, `snifftest serve`); optional Claude Code plugin and GitHub Action. |
| Requirements | Node.js ≥ 20 (upstream builds with Bun); `TYPESAFE_API_KEY` only for judgment rules (not needed for `--dry-run` countable rules). |
| License | [MIT](https://github.com/DanRWilloughby/snifftest/blob/240653e2b082c114c38fed50a42e7eb311e21219/LICENSE). TypeSafe usage has separate costs. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source inspected; offline `bun test` run. Live TypeSafe judgment rules were not run. |

## When to use

Use it when you want house-style AI-writing tells caught locally first, with optional Jev only after an explicit yes. Prefer [jev-lint](jev-lint.md) / [JevLint](jevlint.md) for code semantic linting, or [PageGrade](../apps/pagegrade.md) for on-page writing grades. Do not treat flags as proof of authorship.

## How it works

Countable rules run on-device with regexes and send nothing. Judgment rules (see [`src/jev.ts`](https://github.com/DanRWilloughby/snifftest/blob/240653e2b082c114c38fed50a42e7eb311e21219/src/jev.ts)) send one paragraph at a time to TypeSafe Jev and receive one probability per rule after interactive confirmation. Exit codes: `0` clean, `1` flags, `2` tool failure, `3` judgment rules needed confirmation and did not get it. `snifftest serve` opens a local nose-mascot UI for interactive typing.

## Get started

```sh
git clone https://github.com/DanRWilloughby/snifftest.git
cd snifftest
git checkout 240653e2b082c114c38fed50a42e7eb311e21219
bun test
# Countable only: npm install --global snifftest && snifftest check --dry-run draft.md
# Judgment rules: TYPESAFE_API_KEY=… snifftest check draft.md  # confirms before send
```

This listing did not call TypeSafe or install the global CLI.

## Examples and demos

- Corpus and seeds under `examples/`.
- Bench artifacts under `bench/` (upstream-reported; not re-run).
- Offline `bun test` on the review host (see Review).

## Limits and data handling

With judgment rules enabled, paragraph text leaves the host to TypeSafe after confirmation. Countable `--dry-run` stays local. The tool does not rewrite text. House rules are yours to maintain; upstream defaults are starting points.

## Review and maintenance

Reviewed on **2026-09-20** at [commit 240653e](https://github.com/DanRWilloughby/snifftest/tree/240653e2b082c114c38fed50a42e7eb311e21219): **snifftest 0.1.0**, MIT. AI-assisted source review of README, LICENSE, and `src/jev.ts`. Ran `bun test`: **647 passed**, **1 skipped**. Live TypeSafe judgment path not executed.

Related: [jev-lint](jev-lint.md), [JevLint](jevlint.md), [patdown](patdown.md), [PageGrade](../apps/pagegrade.md).
