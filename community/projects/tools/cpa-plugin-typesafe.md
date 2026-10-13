# cpa-plugin-typesafe

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

CLIProxyAPI plugin that adds a native TypeSafe/Jev typed API path with OpenAI-compatible chat and private settings.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/EcoRayDev/cpa-plugin-typesafe) |
| Maintainer | [EcoRayDev](https://github.com/EcoRayDev). Independently curated. |
| Format | Go plugin for CLIProxyAPI |
| Requirements | CLIProxyAPI; TypeSafe credentials per plugin settings. |
| License | [MIT](https://github.com/EcoRayDev/cpa-plugin-typesafe/blob/c58bd6001b914319a6f4c7ce6df0b6ba2ed372c2/LICENSE) |
| Jev evidence | [`internal/typesafe/plugin.go`](https://github.com/EcoRayDev/cpa-plugin-typesafe/blob/c58bd6001b914319a6f4c7ce6df0b6ba2ed372c2/internal/typesafe/plugin.go) at the pinned commit. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |

## When to use

- Front TypeSafe Jev through CLIProxyAPI with typed routes and optional OpenAI-shaped chat.
- Mismatch: Requires the CLIProxyAPI host; not a standalone SDK.

## How it works

The plugin registers TypeSafe resources and routes typed System One traffic (and chat compatibility) through CLIProxyAPI management. (Summarized from the upstream [README](https://github.com/EcoRayDev/cpa-plugin-typesafe/blob/c58bd6001b914319a6f4c7ce6df0b6ba2ed372c2/README.md); not reproduced here.)

## Get started

From the upstream README (not run on the review host): build/install the plugin into CLIProxyAPI and configure TypeSafe credentials in private settings.

## Limits and data handling

Prompts and typed questions go to TypeSafe with your key. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-13** (Europe/Sofia) at [commit c58bd6001b91](https://github.com/EcoRayDev/cpa-plugin-typesafe/tree/c58bd6001b914319a6f4c7ce6df0b6ba2ed372c2). Inspected the upstream README, LICENSE, and the Jev integration evidence linked above; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
