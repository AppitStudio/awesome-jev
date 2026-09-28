# jev (taifoon-io)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Grade an AI agent job with TypeSafe Jev: fact checks in code, four closed questions, receipt with probabilities, optional on-chain records (`@taifoon/jev`)

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/taifoon-io/jev) |
| Maintainer | [taifoon-io](https://github.com/taifoon-io). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | TypeScript npm package (`@taifoon/jev`). |
| Requirements | Node; `TYPESAFE_API_KEY` (BYOK); optional on-chain recording per README. |
| License | [MIT](https://github.com/taifoon-io/jev/blob/e9d97f7fd0d35ddd07a16ef9872aa69a1cdb6749/LICENSE). Provider usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source inspected; live provider paths not run on the review host. |

## When to use

Use when buyers/sellers need a recomputable complete/reject/needs-review grade for agent work. Prefer simpler evaluate wrappers if you do not need receipts or on-chain hooks.

## How it works

Code extracts facts; Jev answers four bounded questions; code maps answers to a grade and receipt. Distinct from other bare `/jev` repos. Integration evidence: upstream README at the pinned commit.

## Get started

```sh
git clone https://github.com/taifoon-io/jev.git
cd jev
git checkout e9d97f7fd0d35ddd07a16ef9872aa69a1cdb6749
```

Pin revision `e9d97f7fd0d35ddd07a16ef9872aa69a1cdb6749` when reproducing this review.

## Examples and demos

See the upstream README at the pinned commit. No separate live demo was executed on the review host.

## Limits and data handling

Live TypeSafe/provider calls and install paths were not executed on the review host. Treat upstream benchmarks and measured claims as author-reported unless independently reproduced.

## Review and maintenance

Reviewed **2026-09-28** (Europe/Sofia) at [commit e9d97f7](https://github.com/taifoon-io/jev/tree/e9d97f7fd0d35ddd07a16ef9872aa69a1cdb6749). AI-assisted README and LICENSE inspection; install/live paths not executed.
