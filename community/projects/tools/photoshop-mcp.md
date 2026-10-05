# Photoshop MCP

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Unofficial MCP server for Adobe Photoshop (100+ tools and one-step recipes); its built-in chat UI can opt in to TypeSafe Jev intent routing so confident, safe single commands run without an LLM call.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/alisaitteke/photoshop-mcp) |
| Product homepage | [photoshop-mcp.com](https://photoshop-mcp.com) |
| Maintainer | [alisaitteke](https://github.com/alisaitteke). Independently curated. |
| Format | MCP server and standalone chat UI; Jev routing is experimental and opt-in |
| Requirements | Adobe Photoshop running on Windows or macOS and Node.js 18+. The chat UI needs an AI provider key or CLI account; Jev routing needs `TYPESAFE_API_KEY`. |
| License | [MIT](https://github.com/alisaitteke/photoshop-mcp/blob/1a8686853b33e56c970b50b4030fdb190f951c72/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Run quick edits such as undo, opacity, blend mode or background removal instantly from plain language, skipping the LLM when Jev is confident.
- Keep hard-to-undo operations (merge, flatten, delete) on the reviewed Action Plan path.
- Mismatch: using the MCP server from Cursor or Claude alone does not involve Jev; routing applies to the built-in chat UI.

## How it works

Before any LLM runs, the UI asks Jev to classify the message against the registered tools (each tool's 'Use when' line is a criterion) and to judge signals such as multi-step, specific and needs-a-look. Only a confident, known, non-risky command or a chain of up to four with resolved arguments runs instantly; free-text arguments, vague or visual requests and destructive steps go to the planner or agent loop. Thresholds live in `src/ui/intent/router.ts` ([standalone UI docs](https://github.com/alisaitteke/photoshop-mcp/blob/1a8686853b33e56c970b50b4030fdb190f951c72/docs/standalone-ui.md#jev-intent-routing-experimental-opt-in)).

## Get started

With Photoshop running, start the chat UI with a TypeSafe key (live Jev calls for each prompt):

```sh
TYPESAFE_API_KEY=... npx -p @alisaitteke/photoshop-mcp ui
```

With the key set, prompts are also sent to `api.typesafe.ai` and billed by TypeSafe; LLM-routed prompts use your AI provider. Some Photoshop features (for example generative fill) need an Adobe account.

## Examples and demos

- README *Try saying* prompts and the [standalone UI guide](https://github.com/alisaitteke/photoshop-mcp/blob/1a8686853b33e56c970b50b4030fdb190f951c72/docs/standalone-ui.md) (routes, chains, recipes, off switch).

## Limits and data handling

Experimental. Without the key the UI behaves as before and nothing is sent to TypeSafe. Not affiliated with or endorsed by Adobe; Photoshop is a separate paid product. Routing quality was not measured in this review.

## Review and maintenance

Reviewed **2026-10-05** (Europe/Sofia) at [commit 1a8686853b33](https://github.com/alisaitteke/photoshop-mcp/tree/1a8686853b33e56c970b50b4030fdb190f951c72). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
