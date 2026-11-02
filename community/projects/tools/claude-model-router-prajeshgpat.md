# claude-model-router by prajeshgpat (local proxy that picks the cheapest sufficient Claude model per turn from Jev's answers)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Runs Claude Code through a loopback proxy: on each new user turn Jev answers typed questions about the request, a truth table in code turns the answers into a model tier, and the request goes on to Anthropic. Your Claude Code login, tools and sessions work as usual; if Jev fails, it keeps the current tier.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/prajeshgpat/claude-model-router) |
| Maintainer | [prajeshgpat](https://github.com/prajeshgpat). Independently curated. |
| Format | Node.js proxy and installer (no npm dependencies) |
| Requirements | macOS or Linux, Node 20.12+, Claude Code, `TYPESAFE_API_KEY`. |
| License | [MIT](https://github.com/prajeshgpat/claude-model-router/blob/7c47aa0c1b22afad45dcc4bbae9248c2df2a7dd9/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/infra/jev-client.mjs`](https://github.com/prajeshgpat/claude-model-router/blob/7c47aa0c1b22afad45dcc4bbae9248c2df2a7dd9/src/infra/jev-client.mjs) at the pinned commit. |

## When to use

- Cut Claude Code cost by routing easy turns to smaller models.
- Mismatch: adds a shell alias and proxy; picking a model in /model bypasses routing.

## How it works

`src/infra/jev-client.mjs` posts once per new turn to `https://api.typesafe.ai/v1/systemone` (`jev-latest`) and returns null on any failure, which the policy treats as no judgment. Integration evidence: [`src/infra/jev-client.mjs`](https://github.com/prajeshgpat/claude-model-router/blob/7c47aa0c1b22afad45dcc4bbae9248c2df2a7dd9/src/infra/jev-client.mjs).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/prajeshgpat/claude-model-router && cd claude-model-router
node bin/install.mjs
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Repository README: [github.com/prajeshgpat/claude-model-router#readme](https://github.com/prajeshgpat/claude-model-router#readme)

## Limits and data handling

The new user turn is sent to TypeSafe once per turn. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-02** (Europe/Sofia) at [commit 7c47aa0c1b22](https://github.com/prajeshgpat/claude-model-router/tree/7c47aa0c1b22afad45dcc4bbae9248c2df2a7dd9). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
