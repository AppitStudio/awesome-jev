# Jevidence by Peak Evergreen (Python sandbox that turns Jev judgments into testable issue-routing policies you can replay offline)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Teaching sandbox for the pattern "let Jev judge, let your code decide". An issue goes to Jev for a choice (investigation area), a yes/no (explicit reproduction steps) and a 0 to 2 score (observation specificity); allowlists and thresholds in your own code then pick a queue and hints, and a failure keeps the existing queue. Offline `demo`, `evaluate`, `replay` and `calibrate` commands re-run stored judgments with different thresholds without calling a model, including a calibration and stability comparison across decision models. Companion to a Peak Evergreen blog post; built with Codex and independent of TypeSafe.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/peakevergreen/jevidence) |
| Maintainer | [peakevergreen](https://github.com/peakevergreen). Independently curated. |
| Format | Python 3.10+ command-line sandbox, standard library only (MIT) |
| Requirements | Python 3.10+. Offline commands need no packages, key or network; live judgments need `TYPESAFE_API_KEY`. |
| License | [MIT](https://github.com/peakevergreen/jevidence/blob/339f17d174354c287ec1827d4c76a32ee39aa461/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`jevidence/runner.py`](https://github.com/peakevergreen/jevidence/blob/339f17d174354c287ec1827d4c76a32ee39aa461/jevidence/runner.py) at the pinned commit. |

## When to use

- Learn how to wrap a decision model's answer in thresholds and a safe fallback, and test the policy on stored judgments.
- Mismatch: a production triage service; it is a teaching sandbox with synthetic examples.

## How it works

`jevidence/runner.py` posts the issue and typed questions (`jevidence/questions.py`, model `jev-1.13.0`) to `https://api.typesafe.ai`; `jevidence/policy.py` applies the thresholds and `replay.py` re-scores stored judgments. Integration evidence: [`jevidence/runner.py`](https://github.com/peakevergreen/jevidence/blob/339f17d174354c287ec1827d4c76a32ee39aa461/jevidence/runner.py).

## Get started

Clone it and run the offline demo; set a TypeSafe key only if you want live judgments.

```sh
git clone https://github.com/peakevergreen/jevidence.git && cd jevidence
python3 -m jevidence demo
python3 -m jevidence demo --route-floor 0.7
python3 -m jevidence evaluate
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Demo transcript: [github.com/peakevergreen/jevidence/blob/339f17d174354c287ec1827d4c76a32ee39aa461/docs/demo.md](https://github.com/peakevergreen/jevidence/blob/339f17d174354c287ec1827d4c76a32ee39aa461/docs/demo.md)
- Replay guide: [github.com/peakevergreen/jevidence/blob/339f17d174354c287ec1827d4c76a32ee39aa461/docs/replay.md](https://github.com/peakevergreen/jevidence/blob/339f17d174354c287ec1827d4c76a32ee39aa461/docs/replay.md)

## Limits and data handling

Bundled examples are synthetic and `replay` and `calibrate` never contact a model; live calls send issue text to TypeSafe on your key. Results shown are illustrative, not measurements of Jev.

## Review and maintenance

Reviewed **2026-11-18** (Europe/Sofia) at [commit 339f17d17435](https://github.com/peakevergreen/jevidence/tree/339f17d174354c287ec1827d4c76a32ee39aa461). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
