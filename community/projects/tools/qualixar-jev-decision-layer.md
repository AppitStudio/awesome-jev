# Qualixar Jev Decision Layer

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Typed decisions for coding agents—execution stays with the agent; Jev answers bounded Choice/Score/Noul questions.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/qualixar/jev-decision-layer) |
| Maintainer | [qualixar](https://github.com/qualixar). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Python MCP decision layer with host adapters and offline selftest fixtures. |
| Requirements | Python; TypeSafe API key for live Jev; optional separately installed Laya-MLX for local route. |
| License | [MIT](https://github.com/qualixar/jev-decision-layer/blob/2f73135abd9dd0868933ff2f5b78d6f74e3a643d/LICENSE). Provider usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source inspected; live provider paths not run on the review host. |

## When to use

Use when coding agents need a calibrated typed decision plane with offline contract checks before spending on providers.

## How it works

Shared runtime + recipes + policy broker; thin adapters per host. Answers are gated locally with receipts; agent still executes. Integration evidence: upstream README and source at the pinned commit below.

## Get started

```sh
git clone https://github.com/qualixar/jev-decision-layer.git
cd jev-decision-layer
git checkout 2f73135abd9dd0868933ff2f5b78d6f74e3a643d
plugins/qualixar-jev-decision-layer/scripts/jev selftest
```

Pin revision `2f73135abd9dd0868933ff2f5b78d6f74e3a643d` when reproducing this review.

## Examples and demos

See the upstream README at the pinned commit. No separate live demo was executed on the review host.

## Limits and data handling

Independent of TypeSafe; thresholds marked demonstration/not calibrated unless measured. Live provider path not run on the review host.

## Review and maintenance

Reviewed **2026-09-27** (Europe/Sofia) at [commit 2f73135](https://github.com/qualixar/jev-decision-layer/tree/2f73135abd9dd0868933ff2f5b78d6f74e3a643d). AI-assisted README and LICENSE inspection; install/live paths not executed.
