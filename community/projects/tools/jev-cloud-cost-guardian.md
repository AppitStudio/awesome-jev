# jev-cloud-cost-guardian

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

GitHub Action FinOps gate: normalize cloud cost evidence, ask TypeSafe Jev for a typed `approve` / `warn` / `block` / `manual-review` decision, then apply deterministic rails that never hide cost lines or mutate infrastructure.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/JevForge/jev-cloud-cost-guardian) |
| Maintainer | [JevForge](https://github.com/JevForge). Independently curated. |
| Format | TypeScript GitHub Action (`action.yml`) with collectors and tests. |
| Requirements | GitHub Actions; `AI_GATEWAY_API_KEY`, `TYPESAFE_API_KEY`, or `JEV_CUSTOM_API_KEY`. |
| License | [MIT](https://github.com/JevForge/jev-cloud-cost-guardian/blob/6b599c3f9cdcf3294fc2d2ae27008765fdf7382f/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live Actions/Jev not run. |

## When to use

Use it when infra PRs need a **budget-aware merge signal** without letting a model apply Terraform/kubectl. Prefer classical cost bots when you only need numeric threshold checks without Jev.

## How it works

Collectors normalize estimates/plans/bills; [`src/core/jev/`](https://github.com/JevForge/jev-cloud-cost-guardian/tree/6b599c3f9cdcf3294fc2d2ae27008765fdf7382f/src/core/jev) calls Jev (`experimental_evaluate`); policy may tighten but not loosen `block` / `manual-review`.

## Get started

```sh
git clone https://github.com/JevForge/jev-cloud-cost-guardian.git
cd jev-cloud-cost-guardian
git checkout 6b599c3f9cdcf3294fc2d2ae27008765fdf7382f
npm ci
npm test
# Wire Action per README with secrets.AI_GATEWAY_API_KEY
```

## Examples and demos

- README Action snippet; `examples/estimates.yml` and `examples/pr-gate.yml`.

## Limits and data handling

Cost evidence (after redaction) is sent to the configured Jev provider. The Action does not apply cloud mutations. This listing did not run live CI.

## Review and maintenance

Reviewed **2026-09-24** (Europe/Sofia) at [commit 6b599c3](https://github.com/JevForge/jev-cloud-cost-guardian/tree/6b599c3f9cdcf3294fc2d2ae27008765fdf7382f). AI-assisted README + Action/`src/core/jev` inspection. Offline tests not re-run here.

Related: [jev-ci-selector](jev-ci-selector.md), [Moongate](moongate.md), [Metis](metis.md).
