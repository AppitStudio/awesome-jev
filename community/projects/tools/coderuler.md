# CodeRuler (policies-as-code checker for AI-written code, where AI rules ask Jev one decision about a selected scope)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Write your team's conventions as small TypeScript or JavaScript rule classes instead of Markdown that coding agents ignore, and check code, diffs or pull requests against them. Deterministic rules run as ordinary code; when a policy needs meaning or context, an `ai()` rule sends only the selected scope (for example one function) to a decision model and reports violations above a threshold. Includes a rule-writing skill for coding agents and per-rule model, threshold and token-price settings.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/alex-dbs/coderuler) |
| Maintainer | [alex-dbs](https://github.com/alex-dbs). Independently curated. |
| Format | Node.js CLI (npm `@alex-dbs/coderuler`, Apache-2.0) |
| Requirements | Node.js 24.15+ (or 26+), git for `check --diff` / `check --pr`, and `TYPESAFE_API_KEY` for AI rules (OpenAI is an alternative backend). |
| License | [Apache-2.0](https://github.com/alex-dbs/coderuler/blob/987377a0d472687dba9e12689703c577d9a2130d/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/adapter/decision/jev.ts`](https://github.com/alex-dbs/coderuler/blob/987377a0d472687dba9e12689703c577d9a2130d/src/adapter/decision/jev.ts) at the pinned commit. |

## When to use

- Enforce semantic conventions on agent-written code with predictable rules plus cheap Jev checks.
- Mismatch: teams that want no model calls; deterministic-only rules work without any key.

## How it works

`src/adapter/decision/jev.ts` posts AI-rule questions to `v1/systemone`; `src/infra/settings.ts` defaults to `https://api.typesafe.ai` and `jev-latest`, with an OpenAI adapter selectable instead. Integration evidence: [`src/adapter/decision/jev.ts`](https://github.com/alex-dbs/coderuler/blob/987377a0d472687dba9e12689703c577d9a2130d/src/adapter/decision/jev.ts).

## Get started

Install the CLI and the agent skill, write a rule under `.coderuler/`, then check your project.

```sh
npm install -g @alex-dbs/coderuler
coderuler skill install
export TYPESAFE_API_KEY=...
coderuler check
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/alex-dbs/coderuler/blob/987377a0d472687dba9e12689703c577d9a2130d/README.md](https://github.com/alex-dbs/coderuler/blob/987377a0d472687dba9e12689703c577d9a2130d/README.md)

## Limits and data handling

Only the code scope a rule selects is sent to TypeSafe (or OpenAI) on your key. Deterministic rules run locally. The maker's benchmark folder is its own measurement.

## Review and maintenance

Reviewed **2026-11-16** (Europe/Sofia) at [commit 987377a0d472](https://github.com/alex-dbs/coderuler/tree/987377a0d472687dba9e12689703c577d9a2130d). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
