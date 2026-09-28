# JEVals (duberblock)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Playground for evaluating System One and JEV-compatible models with fidelity, semantic judging, and independent verification.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/duberblock/JEVals) |
| Maintainer | [duberblock](https://github.com/duberblock). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Self-contained TypeScript playground (Principal / Investigation / Operation UIs). |
| Requirements | Node/Docker per upstream; TypeSafe and/or OpenAI-compatible keys for live provider runs. |
| License | [MIT](https://github.com/duberblock/JEVals/blob/3e2f9469ffdbe226720e141e80be262e252aa3b5/LICENSE). Provider usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source inspected; live provider paths not run on the review host. Distinct from [jevals](jevals.md) and [Jevals.com](jevals-com.md). |

## When to use

Use when comparing System One / JEV-compatible engines side-by-side with investigation traces. Prefer dayhaysoos/jevals for authoring local expected-answer cases.

## How it works

Validates SystemOneRequest payloads, runs emulator + JEV baseline + independent/judge providers, and compares per-question fidelity and divergence across three web screens. Distinct from dayhaysoos/jevals workbench and hosted Jevals.com. Integration evidence: upstream README and source at the pinned commit below.

## Get started

```sh
git clone https://github.com/duberblock/JEVals.git
cd JEVals
git checkout 3e2f9469ffdbe226720e141e80be262e252aa3b5
# follow upstream README / compose.yml for local apps
```

Pin revision `3e2f9469ffdbe226720e141e80be262e252aa3b5` when reproducing this review.

## Examples and demos

See the upstream README at the pinned commit. No separate live demo was executed on the review host.

## Limits and data handling

Live provider evaluations not run on the review host. Distinct from [jevals](jevals.md) (dayhaysoos) and [Jevals.com](jevals-com.md).

## Review and maintenance

Reviewed **2026-09-28** (Europe/Sofia) at [commit 3e2f946](https://github.com/duberblock/JEVals/tree/3e2f9469ffdbe226720e141e80be262e252aa3b5). AI-assisted README and LICENSE inspection; install/live paths not executed.
