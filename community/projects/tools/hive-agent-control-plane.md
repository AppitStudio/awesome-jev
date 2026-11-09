# Hive (self-hosted AI-agent control plane whose router can shadow-classify prompts with Jev)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Self-hosted suite controller (`hive.sh`) that installs identity, model gateway, memory and other agent products from a signed manifest; hive-router has an optional Jev shadow decision model.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ChefTaco/hive) |
| Maintainer | [ChefTaco](https://github.com/ChefTaco). Independently curated. |
| Format | Bash suite controller + Docker services (Apache-2.0) |
| Requirements | Bash, jq, openssl, Docker Compose, and optionally `HIVE_TYPESAFE_AI_KEY` or an OpenRouter key for the shadow model. |
| License | [Apache-2.0](https://github.com/ChefTaco/hive/blob/a1c129e15252e8338be123356251edaaa42e4c9d/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`services/hive-router/src/routing/typesafe.ts`](https://github.com/ChefTaco/hive/blob/a1c129e15252e8338be123356251edaaa42e4c9d/services/hive-router/src/routing/typesafe.ts) at the pinned commit. |

## When to use

- Self-host an agent platform with one controller.
- Compare Jev routing classifications in shadow mode.
- Mismatch: Jev is an optional shadow signal.

## How it works

`routing/typesafe.ts` posts to `https://api.typesafe.ai/v1/systemone` with `jev-latest` (OpenRouter `~typesafe/jev-latest` as fallback) and records the shadow classification on routing decisions. Integration evidence: [`services/hive-router/src/routing/typesafe.ts`](https://github.com/ChefTaco/hive/blob/a1c129e15252e8338be123356251edaaa42e4c9d/services/hive-router/src/routing/typesafe.ts).

## Get started

Install with `hive.sh` per the project site, then set the hive-router TypeSafe variables to enable the shadow model.

```sh
git clone https://github.com/ChefTaco/hive.git && cd hive
./hive.sh plan
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/ChefTaco/hive/blob/a1c129e15252e8338be123356251edaaa42e4c9d/README.md](https://github.com/ChefTaco/hive/blob/a1c129e15252e8338be123356251edaaa42e4c9d/README.md)

## Limits and data handling

Prompts are sent to TypeSafe/OpenRouter when the shadow model is enabled.

## Review and maintenance

Reviewed **2026-11-10** (Europe/Sofia) at [commit a1c129e15252](https://github.com/ChefTaco/hive/tree/a1c129e15252e8338be123356251edaaa42e4c9d). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
