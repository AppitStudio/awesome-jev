# System One routing for Apache APISIX

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Adds a `system_one` load-balancing algorithm to Apache APISIX's ai-proxy-multi plugin: a System One model (Jev, Clef) ranks the configured LLM instances for each prompt and the request goes to the highest-ranked healthy one.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/surak/semantic-routing-llm-plugin) |
| Maintainer | [surak](https://github.com/surak). Independently curated. |
| Format | Apache APISIX plugin overlay and patch (Lua), Docker Compose example |
| Requirements | Apache APISIX with ai-proxy-multi, Docker for the example, a System One endpoint key (TypeSafe, OpenRouter or Blablador). |
| License | [Apache-2.0](https://github.com/surak/semantic-routing-llm-plugin/blob/e6831e807106cd36376be376a91fee2c5534012e/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`overlay/apisix/plugins/ai-proxy/system-one.lua`](https://github.com/surak/semantic-routing-llm-plugin/blob/e6831e807106cd36376be376a91fee2c5534012e/overlay/apisix/plugins/ai-proxy/system-one.lua) at the pinned commit. |

## When to use

- Route coding, math and general prompts to different LLMs with one readable sentence per instance instead of example embeddings.
- Fall back to the next-ranked instance on 429 or 5xx errors.
- Mismatch: adds one decision call to every request; the example uses Blablador rather than TypeSafe by default.

## How it works

For each request the balancer asks one choice question, "which of these instances should answer this prompt?", with each instance's description as an option, posts it to the configured `/v1/systemone` endpoint, and picks the most probable healthy instance above the threshold, otherwise the fallback. Integration evidence: [`overlay/apisix/plugins/ai-proxy/system-one.lua`](https://github.com/surak/semantic-routing-llm-plugin/blob/e6831e807106cd36376be376a91fee2c5534012e/overlay/apisix/plugins/ai-proxy/system-one.lua).

## Get started

From the upstream README (not run on the review host):

```sh
cd examples/blablador
export BLABLADOR_API_KEY=...
docker compose up -d
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Documentation site: [surak.github.io/semantic-routing-llm-plugin/](https://surak.github.io/semantic-routing-llm-plugin/)
- Live routing table from 2026-10-16 in the README.

## Limits and data handling

Each prompt is sent to the System One endpoint you configure, on your key, before it reaches the chosen LLM.

## Review and maintenance

Reviewed **2026-10-17** (Europe/Sofia) at [commit e6831e807106](https://github.com/surak/semantic-routing-llm-plugin/tree/e6831e807106cd36376be376a91fee2c5534012e). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
