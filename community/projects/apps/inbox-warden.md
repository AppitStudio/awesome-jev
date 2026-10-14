# Inbox Warden

[All projects](../README.md) · [Web apps](README.md#web-apps)

Self-hosted agent that labels and cleans Gmail / Google Workspace inboxes with company-specific labels, using Jev as the first pass into existing labels and Claude for the rest.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/IshanVats-6/inbox-warden) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/IshanVats-6/inbox-warden#readme) (source-built; no separate product site verified). |
| Pricing and access | Free source build; you supply your own TypeSafe/provider keys and any hosting costs. Checked 2026-10-15. |
| Jev evidence | [`warden/classifier.py`](https://github.com/IshanVats-6/inbox-warden/blob/ec843a55f8e324d95390f51a9496008274bab590/warden/classifier.py) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [IshanVats-6](https://github.com/IshanVats-6). Independently curated. |
| Format | Self-hosted Python web app (Docker) |
| Platform and availability | Self-hosted (Docker) |
| Jev's role | Jev assigns each email to an existing label as the first pass; Claude handles the remainder. |
| Requirements | Docker, Google OAuth setup, TypeSafe API key; Anthropic key for the second pass. |
| License | [MIT](https://github.com/IshanVats-6/inbox-warden/blob/ec843a55f8e324d95390f51a9496008274bab590/LICENSE) |

## When to use

- Sort several company mailboxes into labels that fit each business and archive noise.
- Flag the few emails waiting on you.
- Mismatch: requires your own Google Cloud OAuth app and hosting.

## How it works

Jev classifies each message into existing labels first; low-confidence or new-label cases go to Claude. Code applies labels and archiving with safety settings described upstream. Integration evidence: [`warden/classifier.py`](https://github.com/IshanVats-6/inbox-warden/blob/ec843a55f8e324d95390f51a9496008274bab590/warden/classifier.py).

## Get started

From the upstream README (not run on the review host):

```sh
curl -fsSL https://raw.githubusercontent.com/IshanVats-6/inbox-warden/main/install.sh -o install.sh
less install.sh
bash install.sh
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Google setup: `docs/google-setup.md`.

## Limits and data handling

Email content is sent to TypeSafe (and Anthropic for the second pass) and billed to your keys; mailbox access uses your OAuth app.

## Review and maintenance

Reviewed **2026-10-15** (Europe/Sofia) at [commit ec843a55f8e3](https://github.com/IshanVats-6/inbox-warden/tree/ec843a55f8e324d95390f51a9496008274bab590). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
