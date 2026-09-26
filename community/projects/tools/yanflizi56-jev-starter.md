# Jev Starter

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Browser console to configure TypeSafe Jev Noul/Choice/Score questions, test live, and export Python/JS/cURL (or example JSON).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/YanfLIZi56/jev-starter) |
| Maintainer | [YanfLIZi56](https://github.com/YanfLIZi56). Independently curated. |
| Format | Vue browser starter/console for Jev question design. |
| Requirements | Node/Vite per upstream; TypeSafe API key for live test calls. |
| License | [MIT](https://github.com/YanfLIZi56/jev-starter/blob/84dc781856ae27a1fe95097e65be82f722796bcc/LICENSE). TypeSafe usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live TypeSafe/provider paths not run on the review host. |

## When to use

Use when designing **typed Jev questions** before wiring them into app code. Prefer SDK docs alone when you already know the question shapes.

## How it works

Browser UI builds Noul/Choice/Score payloads, submits live evaluate calls, and exports Python/JavaScript/cURL or shareable example JSON.

## Get started

```sh
git clone https://github.com/YanfLIZi56/jev-starter.git
cd jev-starter
git checkout 84dc781856ae27a1fe95097e65be82f722796bcc
# Follow README for local Vite console; live tests need TypeSafe key
```

## Examples and demos

- Upstream README quickstart and examples at the pinned commit.
- Separate interactive demos only where the upstream README links them; none were executed on the review host.

## Limits and data handling

Live Jev/TypeSafe (or other provider) calls send the judged text/state to that provider and may incur charges. Offline/demo paths stay local when documented upstream. Catalog checks did not run live integrations.

## Review and maintenance

Reviewed **2026-09-26** (Europe/Sofia) at [commit 84dc781](https://github.com/YanfLIZi56/jev-starter/tree/84dc781856ae27a1fe95097e65be82f722796bcc). AI-assisted README and license inspection; install/live paths not executed.
