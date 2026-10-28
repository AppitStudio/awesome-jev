# agent-factory (self-hosted company of AI agent seats that review and land code under scripted gates, with Jev routing)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Bun/TypeScript service with PostgreSQL that keeps your git repositories moving: agent seats review pull requests, triage issues, dispatch fixed jobs to disposable runner boxes and publish bounded results back to the forge, under hard scripted gates and a daily token budget kill switch. Roles name a capability tier rather than a model, and Jev picks the route.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/rodaddy/agent-factory) |
| Maintainer | [rodaddy](https://github.com/rodaddy). Independently curated. |
| Format | Bun/TypeScript service with PostgreSQL |
| Requirements | Bun, PostgreSQL, a Forgejo-style forge and model keys; a TypeSafe API key for Jev routing. |
| License | [MIT](https://github.com/rodaddy/agent-factory/blob/f032eb393980f9665fbd30e4e1c324cf8dc9d8ab/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jev/client.ts`](https://github.com/rodaddy/agent-factory/blob/f032eb393980f9665fbd30e4e1c324cf8dc9d8ab/src/jev/client.ts) at the pinned commit. |

## When to use

- Run an automated review and triage crew on your own forge.
- Mismatch: a large self-hosted system; start in `--shadow` mode.

## How it works

`src/jev/client.ts` is the single client for `https://api.typesafe.ai/v1/systemone` (pinned `jev-1.13.0`); `src/jev/model-route.ts` uses it to pick a model tier. Integration evidence: [`src/jev/client.ts`](https://github.com/rodaddy/agent-factory/blob/f032eb393980f9665fbd30e4e1c324cf8dc9d8ab/src/jev/client.ts).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/rodaddy/agent-factory.git && cd agent-factory
bun install && cp env.example .env
bun run src/index.ts doctor --config config/repos.yml
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/rodaddy/agent-factory#readme](https://github.com/rodaddy/agent-factory#readme)

## Limits and data handling

Task descriptions sent for routing go to TypeSafe. Code and state stay on your infrastructure.

## Review and maintenance

Reviewed **2026-10-28** (Europe/Sofia) at [commit f032eb393980](https://github.com/rodaddy/agent-factory/tree/f032eb393980f9665fbd30e4e1c324cf8dc9d8ab). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
