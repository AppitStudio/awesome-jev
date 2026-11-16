# Sortroom by mhoenes (self-hosted IMAP mail sorter where a decision model such as Jev files new mail into your own folders)

[All projects](../README.md) · [Web apps](README.md#web-apps)

One Docker container with a web admin UI that sorts any IMAP inbox (Gmail, Outlook/Microsoft 365, others). A classification model reads each new mail and picks one of your categories, so it can never invent a folder: twelve built-in English or German categories you can edit, uncertain mail left in the inbox under To review, stars for bills, appointments and security alerts, expiry tracking for time-limited offers, free sender rules, an unsubscribe helper and several mailboxes with their own schedules. The model is any service that speaks the TypeSafe API; the default is Jev through OpenRouter's decisions API.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/mhoenes/sortroom) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/mhoenes/sortroom#readme) (source-built; no separate product site verified). |
| Pricing and access | Free AGPL-3.0 source build and container. You pay your model provider (the README estimates about $0.00002 per mail on OpenRouter's default) and run your own host. Checked 2026-11-17. |
| Jev evidence | [`email_sorter/classifier.py`](https://github.com/mhoenes/sortroom/blob/55da574a47a13444e7e08f1733f40fc904a29d62/email_sorter/classifier.py) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [mhoenes](https://github.com/mhoenes). Independently curated. |
| Format | Self-hosted web app (Python, Docker, AGPL-3.0) |
| Platform and availability | Self-hosted web app in one Docker container (amd64/arm64: home server, NAS, Raspberry Pi) |
| Jev's role | Jev (the default model, via OpenRouter) picks one of your categories for each new mail; low-confidence mail waits for review. |
| Requirements | Docker (amd64 or arm64), an IMAP mailbox, and an OpenRouter key (default) or a TypeSafe-API endpoint and key. |
| License | [AGPL-3.0](https://github.com/mhoenes/sortroom/blob/55da574a47a13444e7e08f1733f40fc904a29d62/LICENSE) |

## When to use

- Keep a personal or small-team inbox filed into your own folders without a text-generating model.
- Mismatch: Gmail-only label workflows or shared helpdesks; it works on IMAP folders.

## How it works

`email_sorter/classifier.py` sends each mail to an endpoint that speaks the TypeSafe API; `config/config.toml` defaults to OpenRouter's decisions endpoint with `typesafe/jev-1.13`, and TypeSafe itself or a self-hosted clone can be set instead. Integration evidence: [`email_sorter/classifier.py`](https://github.com/mhoenes/sortroom/blob/55da574a47a13444e7e08f1733f40fc904a29d62/email_sorter/classifier.py).

## Get started

Download the compose file, set the admin password and start the container.

```sh
curl -fsSLO https://raw.githubusercontent.com/mhoenes/sortroom/main/docker-compose.yml
# create .env with ADMIN_PASSWORD=...; set TZ in docker-compose.yml
docker compose up -d   # open http://<docker-host>:8765
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/mhoenes/sortroom/blob/55da574a47a13444e7e08f1733f40fc904a29d62/README.md](https://github.com/mhoenes/sortroom/blob/55da574a47a13444e7e08f1733f40fc904a29d62/README.md)
- Wiki: [github.com/mhoenes/sortroom/wiki](https://github.com/mhoenes/sortroom/wiki)

## Limits and data handling

For each mail it sends sender, recipients, date, subject, attachment names and up to 3,000 characters of cleaned text to the configured provider. Beta before 1.0; updates can need manual steps.

## Review and maintenance

Reviewed **2026-11-17** (Europe/Sofia) at [commit 55da574a47a1](https://github.com/mhoenes/sortroom/tree/55da574a47a13444e7e08f1733f40fc904a29d62). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
