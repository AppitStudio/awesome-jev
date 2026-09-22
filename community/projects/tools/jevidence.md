# Jevidence

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

An educational Python sandbox for turning typed Jev judgments into advisory issue-routing decisions with a separate, testable policy.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/peakevergreen/jevidence) |
| Maintainer | [Peak Evergreen](https://github.com/peakevergreen); submitted on behalf of the project owner. |
| Format | Python CLI and reference sandbox; Makefile and Docker targets. |
| Requirements | Python 3.10+ for the dependency-free offline demo. Optional hosted inference needs `typesafe-sdk==0.7.1`, a TypeSafe account, and `TYPESAFE_API_KEY`. |
| Jev's role | Optional live judgments about issue category, reproduction steps, and observation specificity; the default demo uses synthetic fixtures. |
| Compatibility | Hosted model pinned to `jev-1.13.0`; an optional adapter connects to an existing Kev server. |
| Access and costs | Free source build. Hosted TypeSafe requests are billable and require explicit opt-in; Kev needs a separately configured server and its compute resources. |
| License | [MIT](https://github.com/peakevergreen/jevidence/blob/main/LICENSE). |
| Disclosure | Self-submission for Peak Evergreen's project, which accompanies its consulting site's developer article. Prepared and checked with Codex; no TypeSafe affiliation or endorsement is claimed. |

## When to use

Use it to learn where model judgment ends and application policy begins, compare a fallback with a specialist queue, or test threshold and failure behavior before adding a provider call. It is a small worked example rather than a ticketing integration or model-quality benchmark.

## How it works

The [question definitions](https://github.com/peakevergreen/jevidence/blob/main/jevidence/questions.py) ask three independent questions about an issue: a Choice for the investigation area, a Noul for explicit reproduction steps, and a Score for observation specificity. The Score is recorded, not converted into priority or a routing gate.

The [policy](https://github.com/peakevergreen/jevidence/blob/main/jevidence/policy.py) accepts only known routes, checks Choice confidence, and separately checks the reproduction probability for runtime reports. Unknown or weak routes return general triage; insufficient reproduction evidence sends a runtime report to reproduction review. Thresholds are teaching values, not calibrated recommendations.

The [runner](https://github.com/peakevergreen/jevidence/blob/main/jevidence/runner.py) reports unavailable judgments separately from model votes, preserves the current queue on failure, and prints an advisory record with `applied: false`. It never assigns an issue. Live SDK retries are disabled in this sandbox.

## Get started

Run these commands with Python 3.10+ from a shell. After cloning, the fixture commands require no package installation, account, API key, or network:

```sh
git clone https://github.com/peakevergreen/jevidence.git
cd jevidence
python3 -m jevidence demo
python3 -m jevidence demo --route-floor 0.7
python3 -m jevidence evaluate
python3 -m unittest discover -s tests -v
```

The default constructed `runtime` judgment has confidence `0.72`, below the `0.8` route threshold, so it proposes `general-triage`. Lowering that threshold to `0.7` changes the proposal to `runtime-investigation`; its separate reproduction check also passes. Neither command applies an action.

For optional inference, follow the upstream [live setup](https://github.com/peakevergreen/jevidence#make-one-live-request). A live hosted request sends the issue's allowlisted ID, title, and body plus the question definitions to TypeSafe and may incur charges. Set the key privately in the environment. The [Kev guide](https://github.com/peakevergreen/jevidence/blob/main/docs/kev.md) instead connects to an existing server; Jevidence does not duplicate Kev's playground or establish equivalent model behavior.

## Examples and demos

- [50-second captioned demo](https://github.com/peakevergreen/jevidence/raw/refs/heads/main/assets/jevidence-demo.mp4) and [transcript](https://github.com/peakevergreen/jevidence/blob/main/docs/demo.md): real CLI output from synthetic fixtures, showing a threshold change, policy replay, and offline tests. No live model calls.
- [Constructed cases](https://github.com/peakevergreen/jevidence/blob/main/jevidence/data/cases.json): eight judgments covering specialist routes, fallbacks, and thresholds.
- [Companion developer article](https://peakevergreen.com/blog/jev-for-developers/): typed decisions, application boundaries, and evaluation patterns.

## Limits and data handling

Fixture agreement tests the code, not Jev accuracy or confidence calibration. The example does not ingest a live issue tracker or carry out its proposed assignments. Real deployments still need representative labeled data, access checks, persistence, and an action boundary.

Offline commands use bundled synthetic records. Live mode sends only the validated issue fields to the selected backend, but those fields can still contain sensitive text supplied by the operator. The Kev backend uses a separate placeholder key rather than forwarding `TYPESAFE_API_KEY`; a custom Kev server is another data recipient. JSON output includes the issue ID and judgment, so consider its handling before redirecting it to logs. The code does not make the model's judgments an authorization mechanism.

## Review and maintenance

Reviewed with Codex on September 22, 2026 at upstream commit [`097f783`](https://github.com/peakevergreen/jevidence/tree/097f7837c01225d9a7b12b2a01ace4be68059f5e). Inspected the license, README, CLI, question definitions, validation, policy, runner, and tests.

Executed the default demo, the `--route-floor 0.7` variation, and the evaluation command: the two proposals matched the explanation above, and all eight constructed cases matched their expected queues at the default thresholds. Python 3.12.14 ran 15 passing offline tests; five optional SDK transport tests were skipped because the SDK was not installed. The demo's code revision predates only the documentation and media addition in this reviewed commit.

No hosted Jev call, running Kev server, Docker build, or model-quality evaluation was performed for this submission. Optional SDK transport tests were inspected but not executed. The owner requested submission; no separate human code review is asserted. Maintainers decide whether to include the project.
