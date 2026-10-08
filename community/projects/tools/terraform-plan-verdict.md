# Terraform Plan Verdict

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

GitHub Action that turns a Terraform plan into a graded LOW / MEDIUM / HIGH / CRITICAL risk verdict across blast radius, destructiveness and security impact, surfaced as a job summary, sticky PR comment, labels and outputs; the default provider is deterministic rules, and the optional `systemone` provider asks Jev (`jev-latest`) for calibrated scores from a redacted plan summary.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/nandotorres/terraform-plan-verdict) |
| Maintainer | [nandotorres](https://github.com/nandotorres). Independently curated. |
| Format | GitHub Action (`uses: nandotorres/terraform-plan-verdict@v1`) |
| Requirements | A workflow producing `terraform show -json` output; `TYPESAFE_API_KEY` secret for `provider: systemone`. |
| License | The reviewed tree has **no LICENSE file** — listed as Source available; reuse terms are not granted until the maintainer adds a license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Replace a `destroy` grep with graded triage and a `fail-on` gate.
- Catch risky in-place changes (public access, encryption off, wide IAM).
- Mismatch: no LICENSE file in the reviewed tree.

## How it works

[`src/judge/rules.ts`](https://github.com/nandotorres/terraform-plan-verdict/blob/21420c4c008f9b01fc6c1d51ed444d8b0e2e2f6c/src/judge/rules.ts) computes deterministic facts; [`src/judge/systemone.ts`](https://github.com/nandotorres/terraform-plan-verdict/blob/21420c4c008f9b01fc6c1d51ed444d8b0e2e2f6c/src/judge/systemone.ts) sends a redacted summary (attribute values dropped) to Jev for scores; [`src/render.ts`](https://github.com/nandotorres/terraform-plan-verdict/blob/21420c4c008f9b01fc6c1d51ed444d8b0e2e2f6c/src/render.ts) writes the PR output.

## Get started

Add to a workflow (README *Examples*):

```sh
- uses: nandotorres/terraform-plan-verdict@v1
  with:
    plan-json: plan.json
    provider: systemone
    model: jev-latest
    api-key: ${{ secrets.TYPESAFE_API_KEY }}
```

`rules` is free; `systemone` bills your TypeSafe key per plan.

## Examples and demos

- Example plans: [`examples/README.md`](https://github.com/nandotorres/terraform-plan-verdict/blob/21420c4c008f9b01fc6c1d51ed444d8b0e2e2f6c/examples/README.md).

## Limits and data handling

Only a redacted plan summary is sent with AI providers. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-08** (Europe/Sofia) at [commit 21420c4c008f](https://github.com/nandotorres/terraform-plan-verdict/tree/21420c4c008f9b01fc6c1d51ed444d8b0e2e2f6c). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
