# Jev builds by Eventum (index of measured Jev builds, each compared against another way of doing the same job)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Eventum, a TypeSafe technology partner, indexes its Jev build log here: five builds so far (PDF table-of-contents search, contract-clause filtering, payment-fraud alert sorting, a signal benchmark beside chat models and a knowledge-drift judge), each with what Jev judges, the result, the Jev version and date tested, and links to the builder's own code and write-up.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/EventumAI/jev-builds) |
| Maintainer | [EventumAI](https://github.com/EventumAI). Independently curated. |
| Format | Markdown index and write-ups (one build's material in the repo) |
| Requirements | None to read. To rerun a build, follow its own repository and a TypeSafe key. |
| License | No license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`knowledge-drift-judge/JEV-DRIFT-CASCADE.md`](https://github.com/EventumAI/jev-builds/blob/0e3eabb2d26559a35125ebf359f41b0715299312/knowledge-drift-judge/JEV-DRIFT-CASCADE.md) at the pinned commit. |

## When to use

- Find worked, measured examples of Jev on one narrow decision, with honest comparisons and limits.
- Mismatch: a library or runnable tool; this repo is an index.

## How it works

The README summarises each build and links to its code repository and Eventum's build page; `knowledge-drift-judge/JEV-DRIFT-CASCADE.md` holds the one write-up published in this repo, with its threshold sweep. Integration evidence: [`knowledge-drift-judge/JEV-DRIFT-CASCADE.md`](https://github.com/EventumAI/jev-builds/blob/0e3eabb2d26559a35125ebf359f41b0715299312/knowledge-drift-judge/JEV-DRIFT-CASCADE.md).

## Get started

Read the README, then open a build's own repository to run it.

```sh
git clone https://github.com/EventumAI/jev-builds.git
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Eventum's build log: [www.eventum.ai/jev-builds](https://www.eventum.ai/jev-builds)
- RVC remote-job labels benchmark data (one of the builds): [github.com/maketeamake/rvc-work-arrangement-benchmark](https://github.com/maketeamake/rvc-work-arrangement-benchmark)
- Related listing by Eventum: [jevlist.ai/projects/jev-video-lab](https://jevlist.ai/projects/jev-video-lab)

## Limits and data handling

Every figure is the builder's own measurement. Eventum is a TypeSafe partner, so treat it as a vendor-adjacent source. Linked builds carry their own licenses (some MIT or Apache-2.0); this index repo has no license file, so no reuse terms are granted for it.

## Review and maintenance

Reviewed **2026-11-24** (Europe/Sofia) at [commit 0e3eabb2d265](https://github.com/EventumAI/jev-builds/tree/0e3eabb2d26559a35125ebf359f41b0715299312). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
