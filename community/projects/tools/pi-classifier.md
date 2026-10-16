# pi-classifier

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Pi coding-agent extension for typed, probabilistic decisions across TypeSafe Jev, OpenAI Decisions, Perplexity Decisions, Cloudflare Clef and other SystemOne-compatible gateways, with one configured model and one provider request per decision.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/abhishek944/pi-classifier) |
| Maintainer | [abhishek944](https://github.com/abhishek944). Independently curated. |
| Format | Pi extension (Git install, TypeScript) |
| Requirements | Node.js 22.19+, Pi 1.2+, a provider key such as `TYPESAFE_API_KEY`. |
| License | [Apache-2.0](https://github.com/abhishek944/pi-classifier/blob/25c850679f946c0f8579014dedae5ecc2c8be5cc/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/config.ts`](https://github.com/abhishek944/pi-classifier/blob/25c850679f946c0f8579014dedae5ecc2c8be5cc/src/config.ts) at the pinned commit. |

## When to use

- Ask a typed question from inside a Pi session and get a probability, not prose.
- Switch the decision provider in config without changing your prompts.
- Mismatch: no fallback routes, retries or permission auto-approval by design.

## How it works

Config maps each provider to a route; the `typesafe-api` route accepts `jev-latest`, `jev-1.13.0`, `jev-preview` or `jev-1.14.0` with `TYPESAFE_API_KEY`, and Jev is also reachable through OpenRouter or Cloudflare. Experimental Jev image and Box answers need opt-in. Integration evidence: [`src/config.ts`](https://github.com/abhishek944/pi-classifier/blob/25c850679f946c0f8579014dedae5ecc2c8be5cc/src/config.ts).

## Get started

From the upstream README (not run on the review host):

```sh
pi install git:github.com/abhishek944/pi-classifier@v0.1.0
export TYPESAFE_API_KEY=...
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Provider and model table in the README.

## Limits and data handling

Decision state (and any images you attach) goes to the configured provider on your key.

## Review and maintenance

Reviewed **2026-10-17** (Europe/Sofia) at [commit 25c850679f94](https://github.com/abhishek944/pi-classifier/tree/25c850679f946c0f8579014dedae5ecc2c8be5cc). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
