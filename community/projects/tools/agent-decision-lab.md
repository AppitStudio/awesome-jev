# Agent Decision Lab (100 Java agent recipes with an optional TypeSafe Jev HTTP adapter)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Educational Java preview: 100 bounded review/routing recipes on one guardrail runtime, with synthetic fixtures and an optional live adapter that calls TypeSafe Jev over HTTP. Offline mode does not call a model.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Sandeep-BA/agent-decision-lab) |
| Maintainer | [Sandeep-BA](https://github.com/Sandeep-BA). Independently curated. |
| Format | Java 17+ / Maven recipes (MIT) |
| Requirements | Java 17+, Maven 3.9+, and a TypeSafe key only when enabling the live adapter. |
| License | [MIT](https://github.com/Sandeep-BA/agent-decision-lab/blob/8cbd4a0a33ee195910ada3e3ffda208bedecb7b0/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/main/java/com/belgavi/agents/JevClient.java`](https://github.com/Sandeep-BA/agent-decision-lab/blob/8cbd4a0a33ee195910ada3e3ffda208bedecb7b0/src/main/java/com/belgavi/agents/JevClient.java) at the pinned commit. |

## When to use

- Study typed decision guardrails in Java with runnable fixtures.
- Optionally call live Jev for the same recipes.
- Mismatch: educational preview, not 100 deployed apps; no business-effect tools.

## How it works

`JevClient.java` calls the documented TypeSafe HTTP System One API with `TYPESAFE_API_KEY`; recipes share one runtime and synthetic fixtures for offline verify. Integration evidence: [`src/main/java/com/belgavi/agents/JevClient.java`](https://github.com/Sandeep-BA/agent-decision-lab/blob/8cbd4a0a33ee195910ada3e3ffda208bedecb7b0/src/main/java/com/belgavi/agents/JevClient.java).

## Get started

Clone, run `mvn verify` offline, then set TYPESAFE_API_KEY only if you enable the live adapter paths in the README.

```sh
git clone https://github.com/Sandeep-BA/agent-decision-lab.git && cd agent-decision-lab
mvn verify
# export TYPESAFE_API_KEY=... for live adapter
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/Sandeep-BA/agent-decision-lab/blob/8cbd4a0a33ee195910ada3e3ffda208bedecb7b0/README.md](https://github.com/Sandeep-BA/agent-decision-lab/blob/8cbd4a0a33ee195910ada3e3ffda208bedecb7b0/README.md)

## Limits and data handling

When live, recipe state and questions are sent to TypeSafe on your key. No paid provider call was made during initial upstream validation.

## Review and maintenance

Reviewed **2026-11-06** (Europe/Sofia) at [commit 8cbd4a0a33ee](https://github.com/Sandeep-BA/agent-decision-lab/tree/8cbd4a0a33ee195910ada3e3ffda208bedecb7b0). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
