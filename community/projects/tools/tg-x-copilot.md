# tg-x-copilot (Telegram to X drafting copilot)

[All projects](../README.md) · [Customer feedback and marketing](README.md#customer-feedback-and-marketing)

Telegram bot that turns forwarded posts into original X drafts: Jev triages each post with typed value, type and risk questions so confident low-value posts are skipped early, then an LLM rewrites the rest and you approve and post yourself.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/stackoracode/tg-x-copilot) |
| Maintainer | [stackoracode](https://github.com/stackoracode). Independently curated. |
| Format | Self-hosted Telegram bot (Python) |
| Requirements | Python; a Telegram bot; an OpenAI-compatible LLM proxy; optional TypeSafe key for Jev; Cloudflare R2 for media. |
| License | [MIT](https://github.com/stackoracode/tg-x-copilot/blob/4049db6a9fc37ea8ced1c7d91ebe8cf10ae6bac6/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/tg_x_copilot/clients/jev.py`](https://github.com/stackoracode/tg-x-copilot/blob/4049db6a9fc37ea8ced1c7d91ebe8cf10ae6bac6/src/tg_x_copilot/clients/jev.py) at the pinned commit. |

## When to use

- Filter a stream of forwarded content before spending LLM calls on it.
- Draft X posts with human approval on every one.
- Mismatch: Jev is optional; without it the main LLM decides.

## How it works

`clients/jev.py` sends the cleaned post to `POST /v1/systemone` (`jev-latest`) with score, choice and noul questions; confident skips end early and uncertain posts pass to the main LLM. Integration evidence: [`src/tg_x_copilot/clients/jev.py`](https://github.com/stackoracode/tg-x-copilot/blob/4049db6a9fc37ea8ced1c7d91ebe8cf10ae6bac6/src/tg_x_copilot/clients/jev.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/stackoracode/tg-x-copilot.git
cd tg-x-copilot
cp .env.example .env   # add your keys, then follow the README
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Pipeline and setup in the README: [github.com/stackoracode/tg-x-copilot#readme](https://github.com/stackoracode/tg-x-copilot#readme)

## Limits and data handling

Forwarded content goes to TypeSafe and your LLM provider. It never posts to X for you. Check rights before reusing others' content.

## Review and maintenance

Reviewed **2026-10-22** (Europe/Sofia) at [commit 4049db6a9fc3](https://github.com/stackoracode/tg-x-copilot/tree/4049db6a9fc37ea8ced1c7d91ebe8cf10ae6bac6). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
