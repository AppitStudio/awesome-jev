# jev-test-impact

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Test impact analysis: Git diff and static dependency filtering produce candidates; TypeSafe Jev scores which Vitest/Jest files to run, with a static-only mode when no API key is present.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/holasoymalva/jev-test-impact) |
| Maintainer | [holasoymalva](https://github.com/holasoymalva). Independently curated. Distinct from [jev-test-filter](jev-test-filter.md). |
| Format | TypeScript npm package + GitHub Action (`action.yml`). |
| Requirements | Node package manager; optional `TYPESAFE_API_KEY` for Jev selection (`--static` skips network). |
| License | [MIT](https://github.com/holasoymalva/jev-test-impact/blob/f3bdc84c1e5f2b1852b042506cd857899baf2078/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live TypeSafe/CI paths not run on the review host. |

## When to use

Use to **shrink CI test sets** after a change without sending the whole suite. Prefer full-suite runs when impact analysis risk is unacceptable; use `--static` when offline.

## How it works

Diff → static dependency filter → optional Jev scoring of candidates → safety rules → run selected Vitest/Jest files.

## Get started

```sh
npm install -D jev-test-impact
TYPESAFE_API_KEY=... npx jev-test-impact
# or offline: jti --static
git clone https://github.com/holasoymalva/jev-test-impact.git
cd jev-test-impact
git checkout f3bdc84c1e5f2b1852b042506cd857899baf2078
```

## Examples and demos

- README sample console output; GitHub Action wiring via `action.yml`.

## Limits and data handling

With a key, candidate test metadata/paths may go to TypeSafe. Static mode keeps analysis local. Selection quality is not independently verified here.

## Review and maintenance

Reviewed **2026-09-26** (Europe/Sofia) at [commit f3bdc84](https://github.com/holasoymalva/jev-test-impact/tree/f3bdc84c1e5f2b1852b042506cd857899baf2078). AI-assisted README and LICENSE inspection; live Jev/CI not executed.
