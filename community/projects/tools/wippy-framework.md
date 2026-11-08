# Wippy framework (LLM module with a TypeSafe Jev typed-evaluation driver)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Wippy's open framework (Lua modules) whose LLM layer includes a TypeSafe driver for typed evaluation with Jev, alongside other providers.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/wippyai/framework) |
| Maintainer | [wippyai](https://github.com/wippyai). Independently curated. |
| Format | Lua framework modules (MPL-2.0) |
| Requirements | The Wippy runtime and a TypeSafe API key. |
| License | [MPL-2.0](https://github.com/wippyai/framework/blob/99044bd523ffa861add597698158120c4f9eda90/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/llm/src/typesafe/client.lua`](https://github.com/wippyai/framework/blob/99044bd523ffa861add597698158120c4f9eda90/src/llm/src/typesafe/client.lua) at the pinned commit. |

## When to use

- Run typed Jev evaluations inside Wippy apps.
- Swap Jev in next to other LLM providers.
- Mismatch: requires the Wippy runtime.

## How it works

`src/llm/src/typesafe/client.lua` uses `TYPESAFE_BASE_URL` (default `https://api.typesafe.ai/v1`) for typed evaluation; the changelog notes the TypeSafe/Jev driver (#124). Integration evidence: [`src/llm/src/typesafe/client.lua`](https://github.com/wippyai/framework/blob/99044bd523ffa861add597698158120c4f9eda90/src/llm/src/typesafe/client.lua).

## Get started

Use the framework's LLM module in a Wippy app and configure the TypeSafe provider per docs.

```sh
git clone https://github.com/wippyai/framework.git && cd framework
export TYPESAFE_API_KEY=...
ls src/llm/src/typesafe
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/wippyai/framework/blob/99044bd523ffa861add597698158120c4f9eda90/README.md](https://github.com/wippyai/framework/blob/99044bd523ffa861add597698158120c4f9eda90/README.md)

## Limits and data handling

Evaluation inputs are sent to TypeSafe on your key.

## Review and maintenance

Reviewed **2026-11-08** (Europe/Sofia) at [commit 99044bd523ff](https://github.com/wippyai/framework/tree/99044bd523ffa861add597698158120c4f9eda90). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
