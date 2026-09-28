# jevlint (Ice-Hazymoon)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Semantic lint rules for the code-review questions a deterministic linter can't express—TypeSafe Jev yes/no with calibrated probabilities.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Ice-Hazymoon/jevlint) |
| Maintainer | [Ice-Hazymoon](https://github.com/Ice-Hazymoon). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | TypeScript npm CLI (`@hazymoon/jevlint`). |
| Requirements | Node.js 22+ or Bun; TypeScript peer; `TYPESAFE_API_KEY` or `AI_GATEWAY_API_KEY` for live lint. |
| License | [MIT](https://github.com/Ice-Hazymoon/jevlint/blob/4fc280339ac7e835d2d7413c2588047fb5383084/LICENSE). Provider usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source inspected; live provider paths not run on the review host. Distinct from [JevLint (huntedman)](jevlint.md) and [jev-lint (mizchi)](jev-lint.md). |

## When to use

Use when agents or CI need semantic, plain-English lint rules that syntax tools cannot express. Prefer huntedman/JevLint or mizchi/jev-lint if you already standardize on those CLIs.

## How it works

Rules are narrow yes/no questions (yes = violation). jevlint selects candidate code (chunk or ast-grep), asks TypeSafe Jev, and reports file/line/rule/probability like a conventional linter. Distinct from huntedman/JevLint (`@jevlint/cli`) and mizchi/jev-lint. Integration evidence: upstream README and source at the pinned commit below.

## Get started

```sh
git clone https://github.com/Ice-Hazymoon/jevlint.git
cd jevlint
git checkout 4fc280339ac7e835d2d7413c2588047fb5383084
# or: npm install --save-dev @hazymoon/jevlint typescript
# npx jevlint init && export TYPESAFE_API_KEY=... && npx jevlint test && npx jevlint
```

Pin revision `4fc280339ac7e835d2d7413c2588047fb5383084` when reproducing this review.

## Examples and demos

See the upstream README at the pinned commit. No separate live demo was executed on the review host.

## Limits and data handling

Live TypeSafe/AI Gateway calls not run on the review host. Use alongside ESLint for syntactic rules. Distinct from huntedman/JevLint and mizchi/jev-lint.

## Review and maintenance

Reviewed **2026-09-28** (Europe/Sofia) at [commit 4fc2803](https://github.com/Ice-Hazymoon/jevlint/tree/4fc280339ac7e835d2d7413c2588047fb5383084). AI-assisted README and LICENSE inspection; install/live paths not executed.
