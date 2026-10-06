# InspireJev

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

Browser-automation execution toolkit (Chinese and English docs) where the main agent plans and verifies while TypeSafe Jev picks Playwright actions from candidates actually observed on the page; GPT, Pi and MCP entries, with optional local `/v1/systemone` deciders in the 1.1 RC.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/q1325833367/inspire-jev) |
| Maintainer | [q1325833367](https://github.com/q1325833367). Independently curated. |
| Format | CLI + agent entries (GPT, Pi, MCP), installed from a release tarball |
| Requirements | Node.js 24+, Playwright Chromium, a TypeSafe API key (default cloud Jev); optional DeepSeek key for new text; optional local Laya/Kev/OpenJev servers. |
| License | [MIT](https://github.com/q1325833367/inspire-jev/blob/3c242e8e7a1726859bc84b1335db50729ba6b443/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Let a coding or chat agent run multi-step browsing on public sites without spending a large model on every click.
- Compare cloud Jev with local Jev-compatible deciders on the same browser tasks (1.1 RC).
- Mismatch: 1.0 scope is public, no-login sites; logins, CAPTCHAs and sensitive input stay with the user.

## How it works

`main agent → InspireJev core → TypeSafe/Jev action decision → Playwright → page evidence`: the core observes the DOM, offers Jev the candidate actions, executes the chosen one and re-observes; tasks verify completion conditions with checkpoints, resume and takeover. Default budget is 90 s / 40 actions per task. Local decider adapters live in [`integrations/local-jev/`](https://github.com/q1325833367/inspire-jev/tree/3c242e8e7a1726859bc84b1335db50729ba6b443/integrations/local-jev).

## Get started

Install the pinned release and Chromium, then configure keys interactively:

```sh
npm install --global https://github.com/q1325833367/inspire-jev/releases/download/v1.0.0/inspire-jev-1.0.0.tgz
npx playwright@1.63.0 install chromium
inspire-jev setup
inspire-jev install --entry gpt
inspire-jev doctor
```

Live commands contact TypeSafe (or the configured provider) and may incur charges.

## Examples and demos

- v1.0.0 [acceptance report](https://github.com/q1325833367/inspire-jev/releases/download/v1.0.0/acceptance-report.zh-CN.md) (upstream).
- Local-model comparison report under `docs/validation/` (upstream measurements).

## Limits and data handling

Page content and candidate actions are sent to TypeSafe (or a configured local server). No speed-up claim is made upstream; results were not reproduced. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-06** (Europe/Sofia) at [commit 3c242e8e7a17](https://github.com/q1325833367/inspire-jev/tree/3c242e8e7a1726859bc84b1335db50729ba6b443). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
