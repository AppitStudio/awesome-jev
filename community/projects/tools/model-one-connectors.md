# Jev custom connector for Power Platform (Power Automate and Copilot Studio)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Open-source Power Platform custom connectors for TypeSafe Jev and Microsoft-Decision-1: define yes/no, choice and score questions in the designer and use the typed answers as dynamic content in Power Automate flows and Copilot Studio agents.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/markus-tobler/model-one-connectors) |
| Maintainer | [markus-tobler](https://github.com/markus-tobler). Independently curated. |
| Format | Power Platform managed solution (custom connector) |
| Requirements | A Power Platform environment that allows custom connectors; a TypeSafe API key. |
| License | [MIT](https://github.com/markus-tobler/model-one-connectors/blob/f78daa5f7452195d39a7016684265e791ac9accd/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`solutions/JevCustomConnector/src/Connectors/mto_jevv1connector_customcodeblobcontent.csx`](https://github.com/markus-tobler/model-one-connectors/blob/f78daa5f7452195d39a7016684265e791ac9accd/solutions/JevCustomConnector/src/Connectors/mto_jevv1connector_customcodeblobcontent.csx) at the pinned commit. |

## When to use

- Route support requests or qualify form responses in low-code flows.
- Use thresholds on Jev probabilities in conditions and approvals.
- Mismatch: Power Platform licensing for custom connectors applies.

## How it works

The connector's custom code (`.csx`) calls `/v1/systemone` on TypeSafe's API with `jev-latest` by default and lets you pick a model per action; a second connector targets Microsoft-Decision-1 in your own Foundry resource. Integration evidence: [`solutions/JevCustomConnector/src/Connectors/mto_jevv1connector_customcodeblobcontent.csx`](https://github.com/markus-tobler/model-one-connectors/blob/f78daa5f7452195d39a7016684265e791ac9accd/solutions/JevCustomConnector/src/Connectors/mto_jevv1connector_customcodeblobcontent.csx).

## Get started

From the upstream README (not run on the review host): download the managed `JevCustomConnector` solution from the latest release, import it into your environment, then create a connection with your TypeSafe key.

```sh
# Power Platform: Solutions > Import solution > JevCustomConnector_managed.zip
# then add the action "Evaluate with Jev" to a flow
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Releases: [github.com/markus-tobler/model-one-connectors/releases/latest](https://github.com/markus-tobler/model-one-connectors/releases/latest)
- Usage guide: [github.com/markus-tobler/model-one-connectors/blob/main/docs/usage.md](https://github.com/markus-tobler/model-one-connectors/blob/main/docs/usage.md)

## Limits and data handling

Flow data you evaluate is sent to TypeSafe. Not affiliated with Microsoft or TypeSafe.

## Review and maintenance

Reviewed **2026-10-24** (Europe/Sofia) at [commit f78daa5f7452](https://github.com/markus-tobler/model-one-connectors/tree/f78daa5f7452195d39a7016684265e791ac9accd). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
