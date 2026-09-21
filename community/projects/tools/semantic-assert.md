# semantic-assert

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Assert plain-English claims about captured UI or text state with a probabilistic judge—defaulting to TypeSafe Jev—so thresholds live in test code instead of brittle exact-string matchers.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/mondaychen/semantic-assert) |
| Maintainer | [mondaychen](https://github.com/mondaychen). Independently curated; this page is not an upstream submission or endorsement. |
| Format | TypeScript monorepo packages: `semantic-assert`, `semantic-assert-typesafe`, `semantic-assert-ai-sdk`, `semantic-assert-playwright` (Node 22+; pnpm). |
| Requirements | Node.js 22+; TypeSafe key for the typesafe provider (or Vercel AI Gateway via the AI SDK adapter). Playwright peer `>=1.50` for the Playwright package. |
| License | [Apache-2.0](https://github.com/mondaychen/semantic-assert/blob/a4d1f709ba6fef11fcbddc57f426489ca95c92b6/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Offline core package tests **35 passed**; typesafe package tests **20 passed** after `pnpm build`. No live TypeSafe or Playwright browser run. |

## When to use

Use it when UI/copy assertions should track product intent (“the alert explains recovery”) rather than exact strings. Keep counting, arithmetic, and exact IDs in ordinary asserts. Prefer [SemDecide](semdecide.md) for Unix pipeline exit codes; prefer raw SDK scripts for one-off checks.

## How it works

The core package batches related claims, applies thresholds in code, and returns per-claim probabilities. `semantic-assert-typesafe` posts typed questions to TypeSafe Jev. The Playwright adapter captures page regions, supports matchers/fixtures, redaction, and usage reporting. A deterministic fake provider supports offline unit tests.

## Get started

```sh
pnpm add semantic-assert semantic-assert-typesafe
```

Follow upstream [quick start](https://mengdi.dev/semantic-assert/getting-started.html). From this repo (offline):

```sh
git clone https://github.com/mondaychen/semantic-assert.git
cd semantic-assert
git checkout a4d1f709ba6fef11fcbddc57f426489ca95c92b6
pnpm install --frozen-lockfile
pnpm --filter semantic-assert test
pnpm build && pnpm --filter semantic-assert-typesafe test
```

Live judgments send captured state to the configured provider and may incur charges.

## Examples and demos

- Docs site examples for HTML alerts and generated support replies.
- Core + typesafe Vitest suites (run offline in this review).
- Optional Playwright integration tests (not run here).

## Limits and data handling

Captured page/text state goes to the provider—redact secrets. Model judgments are probabilistic; calibrate thresholds on your own examples. Polling is opt-in. Listing does not establish production flakiness characteristics.

## Review and maintenance

Reviewed on **2026-09-21** at [commit a4d1f70](https://github.com/mondaychen/semantic-assert/tree/a4d1f709ba6fef11fcbddc57f426489ca95c92b6): Apache-2.0. AI-assisted review of README, packages, and LICENSE. Offline: `semantic-assert` **35 passed**; `semantic-assert-typesafe` **20 passed**. No live TypeSafe.

Related: [SemDecide](semdecide.md), [Sniff Test](snifftest.md), [jeval](jeval.md).
