# playwright-jev

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Semantic Playwright assertions powered by Jev with three-valued, fail-closed verdicts.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/criguex/playwright-jev) |
| Maintainer | [criguex](https://github.com/criguex). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | TypeScript Playwright Test extension/reporter. |
| Requirements | Node ≥ 20; Playwright Test ≥ 1.45; `TYPESAFE_API_KEY` for live assertions (fixtures for replay). |
| License | [MIT](https://github.com/criguex/playwright-jev/blob/d3503d42af1622f876ae8cb3474b9631680ae8a0/LICENSE). Provider usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source inspected; live provider paths not run on the review host. |

## When to use

Use when acceptance criteria care about meaning under copy changes. Prefer locator string asserts for exact UI contracts.

## How it works

Each assertion sends page text as state with typed questions; ambiguity and transport failures mark unverified (never pass). Integration evidence: upstream README and source at the pinned commit below.

## Get started

```sh
git clone https://github.com/criguex/playwright-jev.git
cd playwright-jev
git checkout d3503d42af1622f876ae8cb3474b9631680ae8a0
# install per upstream README; export TYPESAFE_API_KEY=…
```

Pin revision `d3503d42af1622f876ae8cb3474b9631680ae8a0` when reproducing this review.

## Examples and demos

See the upstream README at the pinned commit. No separate live demo was executed on the review host.

## Limits and data handling

Sends page text to TypeSafe on live runs. Distinct from arthurfiorette/jev-playwright recipes. Live assertions not run on the review host.

## Review and maintenance

Reviewed **2026-09-27** (Europe/Sofia) at [commit d3503d4](https://github.com/criguex/playwright-jev/tree/d3503d42af1622f876ae8cb3474b9631680ae8a0). AI-assisted README and LICENSE inspection; install/live paths not executed.
