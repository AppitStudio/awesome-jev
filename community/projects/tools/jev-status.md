# jev-status

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Claude Code plugin that asks TypeSafe Jev two independent questions after every turn — is the task done / needs action / failed, and is the work development- or production-ready — and shows both answers with probabilities above the prompt plus a toast.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/PeterFujiyu/jev-status-marketplace) |
| Maintainer | [PeterFujiyu](https://github.com/PeterFujiyu). Independently curated. |
| Format | Claude Code plugin marketplace (`jev-status@peter-plugins`) |
| Requirements | Claude Code and a TypeSafe API key (plugin option in secure storage, or `TYPESAFE_API_KEY`). |
| License | The reviewed tree has **no LICENSE file** — listed as Source available; reuse terms are not granted until the maintainer adds a license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Get a quick second opinion on 'done' after each turn in terminal, desktop or VS Code.
- Mismatch: Jev sees only the latest turn, so ship answers lean on observed check states.

## How it works

[`plugins/jev-status/hooks/register.tsx`](https://github.com/PeterFujiyu/jev-status-marketplace/blob/dd985121b9354f2cd8467c1596920a7dac07052c/plugins/jev-status/hooks/register.tsx) sends excerpts of your message and Claude's final message, recent tool errors and four observed check states to `api.typesafe.ai/v1/systemone` after each completed turn and renders the band.

## Get started

Install from the marketplace (README *Install*):

```sh
claude plugin marketplace add PeterFujiyu/jev-status-marketplace
claude plugin install jev-status@peter-plugins
```

One Jev request per completed turn, billed to your TypeSafe key.

## Examples and demos

- README sample bands (`JEV task: ✔ done 97%`, `JEV ship: ▲ production 91%`).

## Limits and data handling

Message excerpts (up to 2,000/4,000 characters), tool error snippets and check states go to TypeSafe (README *What is sent*). No LICENSE file. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-07** (Europe/Sofia) at [commit dd985121b935](https://github.com/PeterFujiyu/jev-status-marketplace/tree/dd985121b9354f2cd8467c1596920a7dac07052c). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
