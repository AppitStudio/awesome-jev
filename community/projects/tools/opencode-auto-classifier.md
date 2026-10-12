# opencode-auto-classifier

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

OpenCode plugin that sends each shell command, file read, and edit to TypeSafe Jev for typed classifications, then folds those answers into permission decisions (via OpenCode Zen).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/schemaitat/opencode-auto-classifier) |
| Maintainer | [schemaitat](https://github.com/schemaitat). Independently curated. |
| Format | TypeScript · OpenCode plugin |
| Requirements | OpenCode; TypeSafe/OpenCode Zen access for Jev. |
| License | [MIT](https://github.com/schemaitat/opencode-auto-classifier/blob/db56990fc1e2aa5df4e509d56de826ba2edaf1ca/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |

## When to use

- Add a System One check before risky agent tool calls in OpenCode.
- Mismatch: Classification quality depends on question design; fails open/closed per config.

## How it works

Before tools run, resources are classified with typed Jev questions; results inform allow/deny. Client: [`jev.ts`](https://github.com/schemaitat/opencode-auto-classifier/blob/db56990fc1e2aa5df4e509d56de826ba2edaf1ca/jev.ts).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/schemaitat/opencode-auto-classifier.git
# follow README plugin install
```

## Limits and data handling

Command/path text may be sent to Jev; billed. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-12** (Europe/Sofia) at [commit db56990fc1e2](https://github.com/schemaitat/opencode-auto-classifier/tree/db56990fc1e2aa5df4e509d56de826ba2edaf1ca). Inspected the upstream README, LICENSE, and the Jev integration file linked above; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
