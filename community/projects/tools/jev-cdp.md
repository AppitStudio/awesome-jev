# jev-cdp (Jev-powered bridge that drives Chrome through the Chrome DevTools Protocol)

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

Small TypeScript bridge that steers a visible Chrome tab over CDP: Jev picks the next browser action from typed questions while page readiness and element facts stay in code. Built for Bun.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/kbitgood/jev-cdp) |
| Maintainer | [kbitgood](https://github.com/kbitgood). Independently curated. |
| Format | Bun / TypeScript CLI (MIT) |
| Requirements | Bun, a running Chrome with remote debugging, and a `TYPESAFE_API_KEY` (`TYPESAFE_MODEL` defaults to `jev-latest`). |
| License | [MIT](https://github.com/kbitgood/jev-cdp/blob/43e8afb67247b03b615df34b4da81aa170699124/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/model.ts`](https://github.com/kbitgood/jev-cdp/blob/43e8afb67247b03b615df34b4da81aa170699124/src/model.ts) at the pinned commit. |

## When to use

- Drive a real Chrome tab with one typed Jev judgment per step.
- Keep geometry and readiness checks in code and pass them to Jev as facts.
- Mismatch: Chrome CDP only; not a headless multi-browser framework.

## How it works

`src/model.ts` posts to `https://api.typesafe.ai/v1/systemone` with your TypeSafe key and model; the agent loop in `src/agent.ts` applies the chosen CDP action. Integration evidence: [`src/model.ts`](https://github.com/kbitgood/jev-cdp/blob/43e8afb67247b03b615df34b4da81aa170699124/src/model.ts).

## Get started

From the upstream README (not run on the review host):

```sh
export TYPESAFE_API_KEY=...
bun install
# follow README to attach to Chrome CDP and run a task
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/kbitgood/jev-cdp/blob/43e8afb67247b03b615df34b4da81aa170699124/README.md](https://github.com/kbitgood/jev-cdp/blob/43e8afb67247b03b615df34b4da81aa170699124/README.md)

## Limits and data handling

Page text, element lists and optional screenshots from the tab you drive are sent to TypeSafe on your key.

## Review and maintenance

Reviewed **2026-11-06** (Europe/Sofia) at [commit 43e8afb67247](https://github.com/kbitgood/jev-cdp/tree/43e8afb67247b03b615df34b4da81aa170699124). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
