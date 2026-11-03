# opencode-jevcode (OpenCode plugin that adds a jevCode agent where Jev picks the coding model, skills, tool groups and conversation history for each prompt)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

OpenCode v2 plugin that adds a `jevCode` agent. For every prompt sent to it, Jev decides which coding model runs the turn, which skills are attached, which tool groups are sent and which parts of the conversation history are still relevant; OpenCode's own model still writes the code. If Jev is slow, down or not configured, the agent behaves like a plain one. Other agents are not changed.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/AleksandrBagdasarov/opencode-jevcode) |
| Maintainer | [AleksandrBagdasarov](https://github.com/AleksandrBagdasarov). Independently curated. |
| Format | OpenCode plugin (TypeScript, npm) |
| Requirements | OpenCode 2.x (tested on 2.2.5) and a TypeSafe or OpenRouter key, or an OpenCode-native decision model. |
| License | [MIT](https://github.com/AleksandrBagdasarov/opencode-jevcode/blob/3f8539ae73d6c98a66301417a1a85999e89f4b59/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jev/transports/typesafe.ts`](https://github.com/AleksandrBagdasarov/opencode-jevcode/blob/3f8539ae73d6c98a66301417a1a85999e89f4b59/src/jev/transports/typesafe.ts) at the pinned commit. |

## When to use

- Let a cheap, fast decision call choose the model, skills and tools for each coding prompt instead of sending everything every time.
- Mismatch: routing assumes English prompts, at most 12 candidate models, and the project is at v0.1.

## How it works

`src/jev/transports/typesafe.ts` posts to `https://api.typesafe.ai/v1/systemone` (default `jev-latest`; an OpenRouter transport also exists); every answer is checked against a closed set of model keys, skill ids, tool group names and history unit ids, and any failure or timeout falls back to keeping the current model with all tools and messages. Integration evidence: [`src/jev/transports/typesafe.ts`](https://github.com/AleksandrBagdasarov/opencode-jevcode/blob/3f8539ae73d6c98a66301417a1a85999e89f4b59/src/jev/transports/typesafe.ts).

## Get started

From the upstream README (not run on the review host):

```sh
opencode plugin add opencode-jevcode
# then set TYPESAFE_API_KEY (or OPENROUTER_API_KEY) and add a `models` allowlist in opencode.jsonc
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README with the options, tool groups and fail-open rules: [github.com/AleksandrBagdasarov/opencode-jevcode#readme](https://github.com/AleksandrBagdasarov/opencode-jevcode#readme)

## Limits and data handling

Per request your prompt (cut to about 3,000 characters), candidate model profiles, skill and tool-group descriptions and, when pruning, a compact conversation state go to TypeSafe or OpenRouter on your key. The README says the plugin is at v0.1, tested only on OpenCode 2.2.5, with English-only routing quality. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-04** (Europe/Sofia) at [commit 3f8539ae73d6](https://github.com/AleksandrBagdasarov/opencode-jevcode/tree/3f8539ae73d6c98a66301417a1a85999e89f4b59). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
