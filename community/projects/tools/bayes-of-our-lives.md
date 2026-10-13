# Bayes of Our Lives

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

One Embabel agent with three interchangeable decision services: TypeSafe Jev, OpenAI, and local code.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/jimador/bayes-of-our-lives) |
| Maintainer | [jimador](https://github.com/jimador). Independently curated. |
| Format | JVM / Embabel agent demo |
| Requirements | JVM; Embabel; TypeSafe API key when using the Jev decision service. |
| License | [MIT](https://github.com/jimador/bayes-of-our-lives/blob/cd87a8ab4841007c76f5f5aa4066fe79cd0e868c/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |
| Jev evidence | [`src/main/java/dev/jimador/bays/decision/BayesDecisionServices.java`](https://github.com/jimador/bayes-of-our-lives/blob/cd87a8ab4841007c76f5f5aa4066fe79cd0e868c/src/main/java/dev/jimador/bays/decision/BayesDecisionServices.java) at the pinned commit. |

## When to use

- Use when you need: One Embabel agent with three interchangeable decision services: TypeSafe Jev, Op…
- Mismatch: See upstream README for setup limits.

## How it works

See upstream integration at `src/main/java/dev/jimador/bays/decision/BayesDecisionServices.java`. (Summarized from the upstream README; not reproduced here.)

## Get started

From the upstream README (not run on the review host): follow setup, configure credentials, and run the documented entrypoint.

```sh
# see upstream README
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. Not run on the review host.

## Examples and demos

- Evidence path: src/main/java/dev/jimador/bays/decision/BayesDecisionServices.java.
- Upstream README.

## Limits and data handling

Inputs may go to TypeSafe or the configured provider when live. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-14** (Europe/Sofia) at [commit cd87a8ab4841](https://github.com/jimador/bayes-of-our-lives/tree/cd87a8ab4841007c76f5f5aa4066fe79cd0e868c). Inspected the upstream README, license status, and the Jev integration evidence linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
