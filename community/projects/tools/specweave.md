# SpecWeave (intent-first spec CLI for coding agents with an opt-in Jev layer for routing, failure triage and shell-command and text screening)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Spec-driven development CLI that hands work between Claude, Codex, Grok and other agents. An optional, off-by-default Jev integration delegates closed-set decisions (routing, failure classification, task model tier, shell-command safety, text screening, headless browsing) to a decision model through OpenRouter, TypeSafe or OpenAI Decisions, with `specweave jev setup` and `doctor` commands, usage tracking, redaction and a documented 26-input benchmark.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/anton-abyzov/specweave) |
| Maintainer | [anton-abyzov](https://github.com/anton-abyzov). Independently curated. |
| Format | npm CLI (`specweave`, TypeScript) with skills and docs site |
| Requirements | Node.js 20.12+; Jev needs `OPENROUTER_API_KEY`, `TYPESAFE_API_KEY` or `JEV_API_KEY` and an explicit opt-in. |
| License | [MIT](https://github.com/anton-abyzov/specweave/blob/812848c27ca03c5507ddf8a24c128bc38ad8c633/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/core/jev/client.ts`](https://github.com/anton-abyzov/specweave/blob/812848c27ca03c5507ddf8a24c128bc38ad8c633/src/core/jev/client.ts) at the pinned commit. |

## When to use

- Move closed-set decisions in an agent workflow from a frontier-model turn to a typed decision model.
- Study an opt-in design with key-name-only reporting and a kill switch (`SPECWEAVE_JEV=0`).
- Mismatch: Jev is optional inside a much larger toolkit; the benchmark is on synthetic, author-labelled messages.

## How it works

`src/core/jev/` holds the client, config, redaction, usage and `decide` modules; `specweave jev` commands configure and test it and the docs guide states the one test: every possible answer must be writable before the call. Integration evidence: [`src/core/jev/client.ts`](https://github.com/anton-abyzov/specweave/blob/812848c27ca03c5507ddf8a24c128bc38ad8c633/src/core/jev/client.ts).

## Get started

From the upstream README (not run on the review host):

```sh
npm install -g specweave
specweave jev setup
specweave jev doctor
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Jev (System One) guide: [github.com/anton-abyzov/specweave/blob/812848c27ca03c5507ddf8a24c128bc38ad8c633/docs-site/docs/guides/jev-system-one.md](https://github.com/anton-abyzov/specweave/blob/812848c27ca03c5507ddf8a24c128bc38ad8c633/docs-site/docs/guides/jev-system-one.md)

## Limits and data handling

Jev is off by default and is a paid external call; the benchmark figures are the author's own, on synthetic inputs.

## Review and maintenance

Reviewed **2026-11-05** (Europe/Sofia) at [commit 812848c27ca0](https://github.com/anton-abyzov/specweave/tree/812848c27ca03c5507ddf8a24c128bc38ad8c633). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
