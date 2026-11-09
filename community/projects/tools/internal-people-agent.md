# Internal People Agent (Workday MCP server with an optional TypeSafe Jev intent classifier)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Task-shaped Workday MCP server and Claude skill for employees' own benefits, equity and HR-policy questions with citations and an auditable decision chain; Jev can classify request intent and sensitivity.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/peopletechflow/internal-people-agent) |
| Maintainer | [peopletechflow](https://github.com/peopletechflow). Independently curated. |
| Format | MCP server (TypeScript, MIT) |
| Requirements | Node, an existing Workday MCP server (or fixture mode), and a TypeSafe key for the optional Jev classifier. |
| License | [MIT](https://github.com/peopletechflow/internal-people-agent/blob/5520899995217ce54556422d12a64b8f24162b47/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jev.ts`](https://github.com/peopletechflow/internal-people-agent/blob/5520899995217ce54556422d12a64b8f24162b47/src/jev.ts) at the pinned commit. |

## When to use

- Route HR questions to the right flow with typed intents.
- Record each request in an auditable chain.
- Mismatch: Jev is optional; real use needs a Workday MCP server.

## How it works

`src/jev.ts` uses `TypeSafeClient` (`jev-latest`) to ask an intent Choice plus any-fit and sensitive Nouls; Claude still writes every answer and Jev never decides permissions. Integration evidence: [`src/jev.ts`](https://github.com/peopletechflow/internal-people-agent/blob/5520899995217ce54556422d12a64b8f24162b47/src/jev.ts).

## Get started

Clone, install, and start in fixture mode, then add your TypeSafe key to enable the Jev classifier.

```sh
git clone https://github.com/peopletechflow/internal-people-agent.git && cd internal-people-agent
export TYPESAFE_API_KEY=...
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/peopletechflow/internal-people-agent/blob/5520899995217ce54556422d12a64b8f24162b47/README.md](https://github.com/peopletechflow/internal-people-agent/blob/5520899995217ce54556422d12a64b8f24162b47/README.md)

## Limits and data handling

Employee questions are sent to TypeSafe when the classifier is on.

## Review and maintenance

Reviewed **2026-11-10** (Europe/Sofia) at [commit 552089999521](https://github.com/peopletechflow/internal-people-agent/tree/5520899995217ce54556422d12a64b8f24162b47). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
