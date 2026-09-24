# mobai-ci

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Run MobAI mobile UI tests (`.mob` and Maestro flows) in CI; plain-text `.mobflow` steps are classified and acted on the device by TypeSafe Jev.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/MobAI-App/mobai-ci) |
| Maintainer | [MobAI-App](https://github.com/MobAI-App) / Interlap. Independently curated; this entry is not an upstream submission or endorsement. |
| Format | CLI · GitHub Action (`MobAI-App/mobai-ci@v1`) plus curl install script. |
| Requirements | macOS or Linux runner for local sim/emu/USB; `MOBAI_TYPESAFE_KEY` (or `--jev-key`) for `.mobflow` workflows; optional MobAI account key for Pro cloud/BYOD. Offline flow validation needs no device or key. |
| License | Repository files (action, `install.sh`, examples, docs): [MIT](https://github.com/MobAI-App/mobai-ci/blob/f551408608e57dec92693883c17189de9923c329/LICENSE). Published `mobai-ci` binaries: closed source, free for local use under [LICENSE-BINARY.md](https://github.com/MobAI-App/mobai-ci/blob/f551408608e57dec92693883c17189de9923c329/LICENSE-BINARY.md). |
| Access and costs | Local simulator, emulator, and USB paths are free (no MobAI account). Cloud device farms and BYOD are Pro. `.mobflow` Jev steps use your TypeSafe key (BYOK) and run on local devices only; TypeSafe inference is billed to that key. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Public README, licenses, Action metadata, and examples inspected. No live Jev call, device boot, or Pro cloud run was performed. |

## When to use

- Drive `.mob` or Maestro UI flows on a GitHub-hosted iOS simulator or Android emulator and keep JUnit plus failure screenshots/UI trees as artifacts.
- Write regression checks as plain-text `.mobflow` lines so Jev classifies each sentence as act, assert, or sign-in from the live screen.
- Prefer classical selector-based `.mob`/Maestro when you do not want a TypeSafe key, or when cloud/BYOD farms are required (workflows are local-device only).

## How it works

`mobai-ci test` runs flows against an already-booted or attached device and emits JUnit. For `.mobflow`, the README states that before each step runs, Jev reads the sentence and classifies it; checks are judged from the screen and never acted on. Code owns install, device selection, sharding, reports, and exit codes. Selector-based `.mob` / Maestro flows do not require Jev.

Evidence: [README — Workflows: tests as plain text](https://github.com/MobAI-App/mobai-ci/blob/f551408608e57dec92693883c17189de9923c329/README.md#L83-L123) and [`examples/github-actions-workflows.yml`](https://github.com/MobAI-App/mobai-ci/blob/f551408608e57dec92693883c17189de9923c329/examples/github-actions-workflows.yml).

## Get started

Install via the Action or the install script (pin a release when you can):

```yaml
- uses: MobAI-App/mobai-ci@v1
  with:
    boot-sim: true   # macOS: UDID in $MOBAI_SIM_UDID
```

```sh
curl -fsSL https://mobai.run/ci/install.sh | sh
mobai-ci validate ./flows   # parse only; no device or TypeSafe key
```

Live `.mobflow` on a local device (billed to your TypeSafe key; needs a booted device and app build):

```sh
export MOBAI_TYPESAFE_KEY=...   # or pass --jev-key
mobai-ci test ./flows --app "$APP_PATH" --device "$MOBAI_SIM_UDID" --wait-device 4m --output reports
```

Upstream how-tos cover emulator, USB signing, cloud, and BYOD; those paths were not executed in this review.

## Examples and demos

- [`examples/github-actions-workflows.yml`](https://github.com/MobAI-App/mobai-ci/blob/f551408608e57dec92693883c17189de9923c329/examples/github-actions-workflows.yml) — `.mobflow` on a macOS simulator (needs `MOBAI_TYPESAFE_KEY`).
- [`examples/github-actions-simulator.yml`](https://github.com/MobAI-App/mobai-ci/blob/f551408608e57dec92693883c17189de9923c329/examples/github-actions-simulator.yml) / [`emulator.yml`](https://github.com/MobAI-App/mobai-ci/blob/f551408608e57dec92693883c17189de9923c329/examples/github-actions-emulator.yml) — free local runners without Jev.
- Cloud and BYOD examples are Pro and were not run here.

## Limits and data handling

- Binary is closed source; only the Action wrapper, install script, examples, and docs are MIT source in the repo.
- `.mobflow` sends screen-derived step decisions through TypeSafe under your key; secrets named `MOBAI_SECRET_*` may be typed on-device for sign-in steps and are documented as scrubbed from logs/reports/UI trees (screenshots can still show unmasked fields).
- Cloud/BYOD need a MobAI Pro key and provider credentials; workflows do not run on those paths per upstream docs.
- This listing does not measure flake rates, cost per step, or model quality.

## Review and maintenance

Reviewed on **2026-09-24** at commit [`f551408`](https://github.com/MobAI-App/mobai-ci/tree/f551408608e57dec92693883c17189de9923c329): public README, MIT + binary licenses, `action.yml`, and examples. AI-assisted source review. **No live Jev call, simulator/emulator boot, USB device, or Pro cloud/BYOD run.** Catalog checks only validate Awesome Jev navigation, not upstream runtime behavior.

Related: [jev-ci-selector](jev-ci-selector.md), [jev-test-filter](jev-test-filter.md), [Mobile Jev](mobile-jev.md), [Midscene JEV Runner](midscene-jev-runner.md).
