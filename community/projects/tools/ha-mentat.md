# Mentat by Trevor Jones (Home Assistant integration that asks Jev typed questions about your house)

[All projects](../README.md) · [Home automation](README.md#home-automation)

A Home Assistant custom integration: write a question about your home in plain language and a System One model (Jev, Cloudflare Clef or a local server) answers with a typed value, a probability, one option from a set, or a level on your scale, that automations can act on. It can include a rolling window of state changes and events and tracks token use and estimated cost.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/tdjones/ha-mentat) |
| Maintainer | [tdjones](https://github.com/tdjones). Independently curated. |
| Format | Home Assistant custom integration (HACS) |
| Requirements | Home Assistant, HACS (custom repository), and a TypeSafe API key for Jev (or Cloudflare Workers AI / a local Clef server). |
| License | [MIT](https://github.com/tdjones/ha-mentat/blob/225b0cc351b96e13f8067610cd26ad71325a3544/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`custom_components/mentat/providers.py`](https://github.com/tdjones/ha-mentat/blob/225b0cc351b96e13f8067610cd26ad71325a3544/custom_components/mentat/providers.py) at the pinned commit. |

## When to use

- Turn fuzzy household questions (is anyone home, did the dishwasher finish, is this doorbell visitor a delivery) into typed values for Home Assistant automations.
- Mismatch: safety-critical automations (locks, alarms) without a deterministic fallback.

## How it works

`custom_components/mentat/providers.py` defines the providers; the TypeSafe one uses the published `/v1/systemone` API at `https://api.typesafe.ai` and sends camera images as named assets that the state refers to. Readings and the event window go in the state, and the typed answer becomes a Home Assistant value for automations. Integration evidence: [`custom_components/mentat/providers.py`](https://github.com/tdjones/ha-mentat/blob/225b0cc351b96e13f8067610cd26ad71325a3544/custom_components/mentat/providers.py).

## Get started

Add the GitHub mirror to HACS as a custom repository, install Mentat, then add the integration with your provider and key.

```sh
# HACS -> menu -> Custom repositories
#   https://github.com/tdjones/ha-mentat  (category: Integration)
# install Mentat, restart Home Assistant, then
# Settings -> Devices & services -> Add integration -> Mentat
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- GitLab home: [gitlab.com/tdjones8081/ha-mentat](https://gitlab.com/tdjones8081/ha-mentat)
- README: [github.com/tdjones/ha-mentat/blob/225b0cc351b96e13f8067610cd26ad71325a3544/README.md](https://github.com/tdjones/ha-mentat/blob/225b0cc351b96e13f8067610cd26ad71325a3544/README.md)

## Limits and data handling

Entity states, event logs and any camera images you include are sent to the chosen hosted provider on every evaluation, with per-call cost; a local Clef server keeps data at home. Developed on GitLab (gitlab.com/tdjones8081/ha-mentat) and mirrored to GitHub for HACS.

## Review and maintenance

Reviewed **2026-11-21** (Europe/Sofia) at [commit 225b0cc351b9](https://github.com/tdjones/ha-mentat/tree/225b0cc351b96e13f8067610cd26ad71325a3544). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
