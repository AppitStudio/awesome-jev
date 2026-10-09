# SystemOneClient

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Elixir client for System One decision models (TypeSafe Jev, Cloudflare Clef, OpenRouter decisions, self-hosted `/v1/systemone` servers) that returns full probability distributions for Choice, Score and Noul questions, with a test stub, retries honouring `Retry-After` and telemetry that does not leak state or keys.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/schainks/system_one_client) |
| Maintainer | [schainks](https://github.com/schainks). Independently curated. |
| Format | Elixir library (`{:system_one_client, "~> 0.1"}`) |
| Requirements | Elixir; a TypeSafe (or other provider) API key for live calls. |
| License | [Apache-2.0](https://github.com/schainks/system_one_client/blob/7e61f3ccabec2acfaf7a78146e5fa09a13633e30/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Route or gate in an Elixir app on top-k / threshold over Jev probabilities.
- Mismatch: not an official TypeSafe SDK; you own provider choice and keys.

## How it works

See the upstream [README](https://github.com/schainks/system_one_client/blob/7e61f3ccabec2acfaf7a78146e5fa09a13633e30/README.md) at the pinned commit for architecture and the Jev integration.

## Get started

From the README:

```elixir
# mix.exs
{:system_one_client, "~> 0.1"}
```

## Limits and data handling

State and questions go to the configured provider (TypeSafe for Jev). Not run on the review host.

## Review and maintenance

Reviewed **2026-10-09** (Europe/Sofia) at [commit 7e61f3ccabec](https://github.com/schainks/system_one_client/tree/7e61f3ccabec2acfaf7a78146e5fa09a13633e30). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
