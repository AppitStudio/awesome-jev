# fast-resume-scoring

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Score how well a resume fits a job in under a second with TypeSafe Jev and see which requirements it covers (reported one request, ~0.4 s).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/dphbfs/fast-resume-scoring) |
| Maintainer | [dphbfs](https://github.com/dphbfs). Independently curated. |
| Format | Go service/CLI |
| Requirements | Go; TypeSafe key. |
| License | [Apache-2.0](https://github.com/dphbfs/fast-resume-scoring/blob/107d7f49aec893a8b6a690eaba45f544c37c8fc2/LICENSE) |
| Jev evidence | [`internal/adapter/jev/client.go`](https://github.com/dphbfs/fast-resume-scoring/blob/107d7f49aec893a8b6a690eaba45f544c37c8fc2/internal/adapter/jev/client.go) at the pinned commit. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |

## When to use

- Quick first-pass fit scoring with per-requirement evidence.
- Mismatch: screening aid only; keep humans in hiring decisions and check local rules on automated screening.

## How it works

Requirements become typed questions in one Jev request; a validate/replay adapter supports offline testing. (Summarized from the upstream [README](https://github.com/dphbfs/fast-resume-scoring/blob/107d7f49aec893a8b6a690eaba45f544c37c8fc2/README.md); not reproduced here.)

## Get started

From the upstream README (not run on the review host): build per the README and point it at a resume and job description.

## Limits and data handling

Resume and job text go to TypeSafe. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-13** (Europe/Sofia) at [commit 107d7f49aec8](https://github.com/dphbfs/fast-resume-scoring/tree/107d7f49aec893a8b6a690eaba45f544c37c8fc2). Inspected the upstream README, LICENSE, and the Jev integration evidence linked above; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
