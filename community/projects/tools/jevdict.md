# jevdict (typed decisions CLI)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

CLI that turns a described decision, such as ticket triage or whether a diff is risky, into typed Jev answers with probabilities that you can pluck in scripts or use as CI gates through exit codes.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Hashimlokasher/jevdict) |
| Maintainer | [Hashimlokasher](https://github.com/Hashimlokasher). Independently curated. |
| Format | CLI (TypeScript, Node.js 23.6+, zero runtime dependencies) |
| Requirements | Node.js 23.6+; a Command Code login (`cmd login`) or `JEVDICT_API_KEY`; TypeSafe's own API is also supported. |
| License | [MIT](https://github.com/Hashimlokasher/jevdict/blob/14200815857f931fe963428a0eca6a5a99d36e20/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/auth.ts`](https://github.com/Hashimlokasher/jevdict/blob/14200815857f931fe963428a0eca6a5a99d36e20/src/auth.ts) at the pinned commit. |

## When to use

- Gate CI on a decision such as `--fail-on 'answers.risk.score>=3'`.
- Script against typed answers with `--pluck` instead of grepping prose.
- Mismatch: needs a Command Code or TypeSafe credential; answers are only as good as the decision spec.

## How it works

Decision specs define a state and `choice`, `noul` or `score` questions; the CLI resolves credentials (`src/auth.ts`, Command Code by default or `https://api.typesafe.ai`), sends one call and prints answers with probabilities; `--dry-run` shows the exact payload. Integration evidence: [`src/auth.ts`](https://github.com/Hashimlokasher/jevdict/blob/14200815857f931fe963428a0eca6a5a99d36e20/src/auth.ts).

## Get started

From the upstream README (not run on the review host):

```sh
npm install -g jevdict
export JEVDICT_API_KEY=your-key
jevdict triage --var ticket="charged twice for the annual plan"
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Bundled decision specs: [github.com/Hashimlokasher/jevdict/tree/main/decisions](https://github.com/Hashimlokasher/jevdict/tree/main/decisions)
- CLI reference in the README: [github.com/Hashimlokasher/jevdict#readme](https://github.com/Hashimlokasher/jevdict#readme)

## Limits and data handling

The state you pass is sent to the chosen backend. Cost figures are the author's. Community project, not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-10-21** (Europe/Sofia) at [commit 14200815857f](https://github.com/Hashimlokasher/jevdict/tree/14200815857f931fe963428a0eca6a5a99d36e20). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
