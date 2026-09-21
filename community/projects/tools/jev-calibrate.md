# jev-calibrate

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Calibrate TypeSafe Jev questions against your own labelled examples: tune criteria, confirm on a held-out set, and get a per-question verdict (`gate`, `ranker`, `unusable`, …). Unofficial.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/smkrv/jev-calibrate) |
| Maintainer | [smkrv](https://github.com/smkrv). Independently curated; this page is not an upstream submission or endorsement. Unofficial—not affiliated with TypeSafe. |
| Format | TypeScript CLI / library published as npm **`jev-calibrate` 0.1.11** (zero runtime dependencies). |
| Requirements | Node.js 20+; live checks need `TYPESAFE_API_KEY` or `OPENROUTER_API_KEY`. |
| License | [MIT](https://github.com/smkrv/jev-calibrate/blob/28bc62065b95eb67709e669a0683e9a5f04f9414/LICENSE). Provider usage billed separately. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Offline `npm test`: **83 passed**. Live TypeSafe/OpenRouter calibration runs were not executed. |

## When to use

Use it when a hand-tuned Jev question looks good on a few examples but you need labelled evidence before treating answers as a gate. Prefer [jevlens](jevlens.md) for dataset eval dashboards/CI gates, [jeval](jeval.md) for provider-neutral calibration math, or [jev-align](jev-align.md) when you want GEPA optimization of AI Functions. Do not treat shipped example metrics as your production accuracy.

## How it works

You supply `questions.json` (System One question shapes plus operating points) and labelled `examples.jsonl`. The CLI talks to TypeSafe, OpenRouter, or any compatible `/v1/systemone` server, runs tune/holdout splits, and reports per-question verdicts such as `gate`, `gate-above-confidence`, `ranker`, `unusable`, or `too-few-examples`, with accuracy/AUC-style summaries and miss lists. Application code still owns thresholds and downstream actions.

## Get started

```sh
npm install -g jev-calibrate@0.1.11
# or inspect the reviewed tree:
git clone https://github.com/smkrv/jev-calibrate.git
cd jev-calibrate
git checkout 28bc62065b95eb67709e669a0683e9a5f04f9414
npm ci --ignore-scripts
npm test
```

Bundled support-ticket example (offline lint / live check when a key is set):

```sh
jev-calibrate lint  --dir examples/support-tickets
# live — sends labelled text to the provider and can incur charges:
# jev-calibrate check --dir examples/support-tickets --runs 3
```

`jev-calibrate init` writes starter files and never overwrites existing ones.

## Examples and demos

- README sample report for a `frustration` score question.
- Repository example under [`examples/support-tickets`](https://github.com/smkrv/jev-calibrate/tree/28bc62065b95eb67709e669a0683e9a5f04f9414/examples/support-tickets).
- Upstream CI badge on `main`.

## Limits and data handling

Labelled example text and question criteria leave the host on live checks. Verdicts depend on your labels, wording, and configured operating points—they are not audited model quality. Early software; treat published example numbers as illustrative for that fixture only.

## Review and maintenance

Reviewed on **2026-09-21** at [commit 28bc620](https://github.com/smkrv/jev-calibrate/tree/28bc62065b95eb67709e669a0683e9a5f04f9414): **0.1.11**, MIT. AI-assisted source review of README, `package.json`, license, and tests. Offline `npm test` → **83 passed**. Live provider calibration and npm global install paths were not run on the review host.

Related: [jevlens](jevlens.md), [jeval](jeval.md), [jev-align](jev-align.md).
