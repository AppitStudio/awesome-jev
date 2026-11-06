# decision-migrate (reviewable Dify classifier migrations onto TypeSafe Jev)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Helps migrate Dify question-classifier nodes onto TypeSafe Jev while preserving branches and capturing a baseline comparison. Targets the LangGenius TypeSafe provider id for `jev-1.13.0-only-for-question-classifier`.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/gbesse/decision-migrate) |
| Maintainer | [gbesse](https://github.com/gbesse). Independently curated. |
| Format | Node.js migration tooling (MIT) |
| Requirements | Node.js and access to the Dify export/workspace being migrated; TypeSafe key when running live comparisons. |
| License | [MIT](https://github.com/gbesse/decision-migrate/blob/38156f5bd9ce3196fb883c044171080bb6237e62/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/index.mjs`](https://github.com/gbesse/decision-migrate/blob/38156f5bd9ce3196fb883c044171080bb6237e62/src/index.mjs) at the pinned commit. |

## When to use

- Move Dify classifiers to Jev without losing branch structure.
- Compare baseline vs Jev on the same cases before cutover.
- Mismatch: Dify-specific; demo/synthetic mode available.

## How it works

`src/index.mjs` encodes the TypeSafe Jev target model provider string and migration rules; the server can run in synthetic demo mode. Integration evidence: [`src/index.mjs`](https://github.com/gbesse/decision-migrate/blob/38156f5bd9ce3196fb883c044171080bb6237e62/src/index.mjs).

## Get started

From the upstream README (not run on the review host):

```sh
# follow README to import a Dify export and produce a reviewable migration plan
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/gbesse/decision-migrate/blob/38156f5bd9ce3196fb883c044171080bb6237e62/README.md](https://github.com/gbesse/decision-migrate/blob/38156f5bd9ce3196fb883c044171080bb6237e62/README.md)

## Limits and data handling

Classifier prompts and sample cases used in live compare mode go to TypeSafe on your key.

## Review and maintenance

Reviewed **2026-11-06** (Europe/Sofia) at [commit 38156f5bd9ce](https://github.com/gbesse/decision-migrate/tree/38156f5bd9ce3196fb883c044171080bb6237e62). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
