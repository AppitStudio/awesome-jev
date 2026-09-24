# jev-qa (moonshot-partners)

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

TypeScript CLI for Jev-driven parallel browser QA: acceptance, adversarial, and smoke verification of web changes with structured decision loops rather than free-form LLM browsing.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/moonshot-partners/jev-qa) |
| Maintainer | [moonshot-partners](https://github.com/moonshot-partners). Independently curated. |
| Format | TypeScript CLI (`bin/` + `src/`). |
| Requirements | Node.js; browser automation deps per package.json; TypeSafe/Jev provider access. |
| License | [MIT](https://github.com/moonshot-partners/jev-qa/blob/b88928d480e50cb4b0d0711f1c57b1391b6ed870/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live QA runs not executed. |

## When to use

Use to **gate** web changes with typed Jev browser checks. Prefer [jev-browse (cooper667)](cooper667-jev-browse.md) for Claude Code Playwright checklists.

## How it works

CLI orchestrates parallel browser scenarios; Jev selects verification actions/assertions from structured observations (per README architecture).

## Get started

```sh
git clone https://github.com/moonshot-partners/jev-qa.git
cd jev-qa
git checkout b88928d480e50cb4b0d0711f1c57b1391b6ed870
npm ci
# run CLI per README / package.json bin
```

## Examples and demos

- `test/` suite (not re-run here).
- README scenario taxonomy.

## Limits and data handling

Page content reaches the Jev provider. Adversarial checks may stress target sites—use staging.

## Review and maintenance

Reviewed **2026-09-24** (Europe/Sofia) at [commit b88928d](https://github.com/moonshot-partners/jev-qa/tree/b88928d480e50cb4b0d0711f1c57b1391b6ed870). AI-assisted README and source inspection; live provider calls not run on the review host.

Related: [cooper667-jev-browse](cooper667-jev-browse.md), [Jev Browser (tontoko)](jev-browser-tontoko.md).
