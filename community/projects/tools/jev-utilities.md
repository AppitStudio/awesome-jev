# jev-utilities by jadeforrest (TypeScript helpers and a CLI for categorizing data with Jev, flagging low-confidence items for a person)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Small TypeScript package that makes a categorization job a two-file affair: a categories file with the question and label descriptions, and an input file of items. The `jev-categorize` CLI (and library) sends each item to Jev as a Choice question with bounded concurrency and retries, and anything below the confidence threshold comes back with `label: null`, Jev's best guess as a suggestion and `needsReview: true` instead of a guess. Includes a dry-run mode and dotenv support.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/jadeforrest/jev-utilities) |
| Maintainer | [jadeforrest](https://github.com/jadeforrest). Independently curated. |
| Format | TypeScript library + CLI (`jev-categorize`, MIT) |
| Requirements | Node.js and `TYPESAFE_API_KEY` (or `--env-file`). |
| License | [MIT](https://github.com/jadeforrest/jev-utilities/blob/d1a472def43eb965053d15616b5e0011534e4a9c/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/client.ts`](https://github.com/jadeforrest/jev-utilities/blob/d1a472def43eb965053d15616b5e0011534e4a9c/src/client.ts) at the pinned commit. |

## When to use

- Sort support requests, transactions or notes into your own labels with a review queue for unsure items.
- Mismatch: open-ended extraction; it answers one Choice question per item.

## How it works

`src/client.ts` posts to `https://api.typesafe.ai/v1/systemone` with retry and response validation; `src/categorize.ts` builds the Choice question from your categories and applies the confidence threshold. Integration evidence: [`src/client.ts`](https://github.com/jadeforrest/jev-utilities/blob/d1a472def43eb965053d15616b5e0011534e4a9c/src/client.ts).

## Get started

Install, then run the CLI on a categories file and an input file.

```sh
git clone https://github.com/jadeforrest/jev-utilities && cd jev-utilities
./install.sh     # builds and links ~/.local/bin/jev-categorize
export TYPESAFE_API_KEY=...
jev-categorize --categories cats.json --input items.json --min-confidence 0.6 --output results.json
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/jadeforrest/jev-utilities/blob/d1a472def43eb965053d15616b5e0011534e4a9c/README.md](https://github.com/jadeforrest/jev-utilities/blob/d1a472def43eb965053d15616b5e0011534e4a9c/README.md)

## Limits and data handling

Items go to TypeSafe on your key. Built as the shared client for the author's own projects; small and young.

## Review and maintenance

Reviewed **2026-11-17** (Europe/Sofia) at [commit d1a472def43e](https://github.com/jadeforrest/jev-utilities/tree/d1a472def43eb965053d15616b5e0011534e4a9c). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
