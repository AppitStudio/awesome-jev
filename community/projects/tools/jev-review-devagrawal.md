# Jev Review (Dev Agrawal)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Explore a staged code-review CLI that screens JavaScript and TypeScript changes or a codebase, selects supporting evidence, and displays structured findings in a local dashboard.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/devagrawal09/jev-review) |
| Maintainer | [Dev Agrawal](https://github.com/devagrawal09). Independent community project. |
| Format | Experimental TypeScript CLI and local report dashboard. |
| Requirements | Node.js 24+, npm, Git, a Git repository to review, and a TypeSafe account/key in `TYPESAFE_API_KEY`. |
| Jev's role | Noul risk screening, Choice evidence/mechanism/reviewer selection, and Score priority/severity through `@typesafe-ai/sdk` `^0.6.0`. No explicit model version is pinned. |
| License | [MIT](https://github.com/devagrawal09/jev-review/blob/31f89602797fb7bea007f8a480bf368bf564954e/LICENSE). |
| Access and costs | Source checkout; review commands call TypeSafe and can incur inference charges. The dashboard reads local reports. |

## When to use

- Study how several narrow typed judgments can form a code-review workflow.
- Screen a local JavaScript/TypeScript diff or package for concerns to investigate manually.
- Inspect a risk matrix and evidence locations alongside your normal review process.

This is a separate project from the [Jev Review MCP server](jev-review.md). Its distinct contribution is a Git-aware staged CLI with diff and codebase modes. Findings are review prompts, not proof of defects or a merge gate.

## How it works

The [change adapter](https://github.com/devagrawal09/jev-review/blob/31f89602797fb7bea007f8a480bf368bf564954e/src/adapters/git.ts) reads changes against `HEAD` plus non-ignored untracked source files. Changed tests provide context. Codebase mode reads tracked and non-ignored untracked JavaScript/TypeScript files; it screens 160-line regions with up to four related, abbreviated test files.

The [judgments](https://github.com/devagrawal09/jev-review/blob/31f89602797fb7bea007f8a480bf368bf564954e/src/review/judgments.ts) screen correctness, security, reliability, compatibility, and test gaps. Application code ranks signals, profiles up to five files, and follows up at most eight signals at or above `0.7`. Follow-up calls choose evidence, classify a mechanism, score severity, and sometimes select a reviewer role.

Evidence selections below confidence `0.55`, `noMatch`, unknown evidence IDs, and `noIssue` mechanisms produce no finding. Severity thresholds determine the report's `comment` or `request_changes` label; these labels do not publish GitHub reviews. The report preserves selected values and confidence fields, but not complete raw API responses. See the [workflow and policy](https://github.com/devagrawal09/jev-review/tree/31f89602797fb7bea007f8a480bf368bf564954e/src/review) and [official API reference](https://docs.typesafe.ai/api).

## Get started

The following is the inspected upstream source-checkout path; installation and live review were not run during this catalog review:

```sh
git clone https://github.com/devagrawal09/jev-review.git
cd jev-review
npm install --ignore-scripts
cp .env.example .env
```

Set `TYPESAFE_API_KEY` privately in `.env`. Choose a small, non-sensitive scope first: review commands transmit source/diff content and test context to TypeSafe and have no offline mode.

```sh
# Live: inspect current changes within a Git repository.
npm run review:changes:save -- /path/to/git/repository

# Local: display the saved report.
npm run dashboard
```

Open `http://127.0.0.1:4317`. Successful reviews save `reviews/latest.json` in the tool checkout; `REVIEW_FILE` can override the path. The dashboard binds to loopback and serves a fixed asset list plus the saved report.

For a complete source scan, explicitly choose the separate live command:

```sh
npm run review:codebase:save -- /path/to/git/repository-or-package
```

The non-`:save` variants print JSON. A scope with no eligible source files raises an error. See the [upstream command table](https://github.com/devagrawal09/jev-review#commands).

## Examples and demos

- The [README screenshot](https://github.com/devagrawal09/jev-review/blob/31f89602797fb7bea007f8a480bf368bf564954e/docs/dashboard.png) illustrates the dashboard; it is upstream demonstration material, not this review's output.
- [Codebase judgments](https://github.com/devagrawal09/jev-review/blob/31f89602797fb7bea007f8a480bf368bf564954e/src/review/codebase-judgments.ts) show source-region selection and test-context filtering.
- No separate offline fixture demo or behavioral test suite was found. The documented usage commands require live credentials.

## Limits and data handling

Only JavaScript/TypeScript source extensions are selected. Change mode excludes deleted files and compares the current working tree against `HEAD`, rather than reviewing an arbitrary PR base. Codebase test matching uses path heuristics and truncated snippets; cross-file behavior and missing context can be overlooked.

Screening has no project-wide file/request budget; the eight-follow-up cap does not cap initial screening. Large files can create multiple screening calls, while later profiling and evidence selection can still include full files. API payload limits and costs therefore need consideration before scanning a large repository.

Service failures abort the review; save mode reports failure and leaves the previous report unchanged. There is no application-level partial-results recovery. Confidence for mechanism, severity, and owner is recorded without the evidence-selection confidence gate, and review thresholds have not been validated here.

Source, paths, patches, and test context go to TypeSafe. Saved reports contain scope paths and judgments; keep them private when reviewing proprietary work. The source extension filter is not secret redaction. No compiler, static analyzer, or runtime test execution confirms findings.

## Review and maintenance

Reviewed on **2026-09-19** at commit [`31f89602797fb7bea007f8a480bf368bf564954e`](https://github.com/devagrawal09/jev-review/commit/31f89602797fb7bea007f8a480bf368bf564954e).

Inspected the README, MIT license, package scripts, Git/source discovery, both judgment implementations, policy/orchestration, report storage, CLI failure handling, dashboard server, and dependency checker. A credential-free `node --check src/dashboard/public/app.js` passed using Node.js 22.19.0; this syntax check does not establish compatibility with the required Node.js 24 runtime. Dependencies were not installed, and the upstream type/dependency checks, dashboard, and live API path were not executed. No accuracy or performance evaluation was performed.

AI-assisted catalog review; contributor affiliation/commercial relationships were not supplied. Listing is not an endorsement.
