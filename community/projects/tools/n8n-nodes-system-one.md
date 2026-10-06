# n8n-nodes-system-one

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

n8n community node for System One decision models across providers — TypeSafe Jev directly, Jev via OpenRouter (no TypeSafe account needed), Cloudflare Workers AI Clef, or any custom `/v1/systemone` endpoint — with typed questions and flat probability outputs for IF/Switch nodes.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/diegohh0411/n8n-nodes-system-one) |
| Maintainer | [diegohh0411](https://github.com/diegohh0411). Independently curated. |
| Format | n8n community node |
| Requirements | n8n with community nodes enabled; one credential: TypeSafe API key, OpenRouter key, Cloudflare account ID + Workers AI token, or a custom endpoint. |
| License | [MIT](https://github.com/diegohh0411/n8n-nodes-system-one/blob/67a2df92f956aef97086b1133feea1f6b6ed9cbc/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Route, classify or score workflow items with calibrated typed answers instead of an LLM node plus JSON parsing.
- Switch between hosted Jev, OpenRouter billing and Cloudflare Clef without rebuilding the workflow.
- Mismatch: other n8n Jev nodes are listed too; choose this one if you need multi-provider (Clef/custom) support.

## How it works

The node sends the chosen state (text or JSON) and a questions map — noul, choice, score, with JSON modes for structured questions — to the selected provider's System One endpoint and returns a Simplified flat object (e.g. `is_urgent`, `is_urgent_yes`, `team_confidence`, `team_probabilities`) or the raw response.

## Get started

Install the community node in n8n (version 0.2.4 on npm at review), add a credential, and configure questions (live provider calls per item):

```sh
# n8n → Settings → Community Nodes → Install
@diegohh0411/n8n-nodes-system-one
# Credential: TypeSafe API | OpenRouter (System One) API | Cloudflare Workers AI | Custom Endpoint
```

Live commands contact TypeSafe (or the configured provider) and may incur charges.

## Examples and demos

- README *Output* example with urgency, team and frustration answers.
- Provider table with endpoints and model IDs (`jev-latest`, `typesafe/jev-1.13`, `clef`, `clef-flash`).

## Limits and data handling

Workflow item content is sent to the selected provider. Model availability per provider is upstream's statement at the pinned commit. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-06** (Europe/Sofia) at [commit 67a2df92f956](https://github.com/diegohh0411/n8n-nodes-system-one/tree/67a2df92f956aef97086b1133feea1f6b6ed9cbc). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
