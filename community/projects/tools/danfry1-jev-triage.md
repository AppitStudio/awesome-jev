# jev-triage by danfry1 (GitHub Action that labels, deduplicates and spam-checks issues with Jev)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

GitHub Action that triages each new issue in one Jev request: labels chosen only from the repository's existing labels, duplicate detection against recent open issues and spam detection with optional auto-close, each gated by a calibrated probability.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/danfry1/jev-triage) |
| Maintainer | [danfry1](https://github.com/danfry1). Independently curated. |
| Format | GitHub Action (TypeScript) |
| Requirements | A GitHub repository with Actions and issues: write permission; a TypeSafe API key as a secret. |
| License | [MIT](https://github.com/danfry1/jev-triage/blob/80909247299acf0857b233062f0666036a4aeb46/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/triage.ts`](https://github.com/danfry1/jev-triage/blob/80909247299acf0857b233062f0666036a4aeb46/src/triage.ts) at the pinned commit. |

## When to use

- Label incoming issues automatically without letting a model invent labels.
- Flag likely duplicates and spam with a threshold you choose.
- Mismatch: starts in dry-run mode and only comments until you set dry-run to false.

## How it works

`src/triage.ts` uses `@typesafe-ai/sdk` (`jev-latest` by default) to send the issue title, body and author association with one question per candidate label plus spam and duplicate questions in a single request. Integration evidence: [`src/triage.ts`](https://github.com/danfry1/jev-triage/blob/80909247299acf0857b233062f0666036a4aeb46/src/triage.ts).

## Get started

From the upstream README (not run on the review host):

```sh
# .github/workflows/triage.yml
- uses: danfry1/jev-triage@v0
  with:
    api-key: ${{ secrets.TYPESAFE_API_KEY }}
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Example workflow: [github.com/danfry1/jev-triage/blob/main/examples/triage.yml](https://github.com/danfry1/jev-triage/blob/main/examples/triage.yml)
- README: [github.com/danfry1/jev-triage#readme](https://github.com/danfry1/jev-triage#readme)

## Limits and data handling

Issue text and recent issue titles are sent to TypeSafe.

## Review and maintenance

Reviewed **2026-10-25** (Europe/Sofia) at [commit 80909247299a](https://github.com/danfry1/jev-triage/tree/80909247299acf0857b233062f0666036a4aeb46). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
