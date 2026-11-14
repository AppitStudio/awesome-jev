# Jev LLM Gateway (cost-aware three-tier LLM gateway study, with Jev's typed choice and success questions as one router)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Reproducible study of serving small, medium and frontier chat tiers behind one OpenAI-style endpoint: `model=auto` routes each prompt, and Jev is one router option (typed tier choice and success questions), compared against a prompted small model, fixed and random baselines. Includes a frozen 2,500-prompt benchmark (GSM8K, MMLU, MBPP), optional verifier cascades and caching, Docker Compose monitoring and an experiment ledger that reports what is still unmeasured.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Arwin-K/jev-llm-gateway) |
| Maintainer | [Arwin-K](https://github.com/Arwin-K). Independently curated. |
| Format | Python gateway and evaluation package with uv, Docker Compose and kind profiles (MIT) |
| Requirements | Python with uv, Ollama with Qwen 2.5 models for the local tiers, and a TypeSafe key plus configured caps for the Jev router. |
| License | [MIT](https://github.com/Arwin-K/jev-llm-gateway/blob/1bcffb0e63efcc6e7a668385e27d2769b49c3e29/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jev_gateway/routing/jev_client.py`](https://github.com/Arwin-K/jev-llm-gateway/blob/1bcffb0e63efcc6e7a668385e27d2769b49c3e29/src/jev_gateway/routing/jev_client.py) at the pinned commit. |

## When to use

- Study how much answer quality a router keeps while sending prompts to cheaper models.
- Mismatch: a production gateway; sustained real load and trained fallbacks are documented as pending.

## How it works

`src/jev_gateway/routing/jev_client.py` posts `{model, state, questions}` to `https://api.typesafe.ai` (contract checked against `openapi.json` on 2026-10-29) and refuses to run unless model, key, sourced rates and positive spend caps are all configured. Integration evidence: [`src/jev_gateway/routing/jev_client.py`](https://github.com/Arwin-K/jev-llm-gateway/blob/1bcffb0e63efcc6e7a668385e27d2769b49c3e29/src/jev_gateway/routing/jev_client.py).

## Get started

Check the setup, start the gateway and send an explicit-tier request.

```sh
git clone https://github.com/Arwin-K/jev-llm-gateway && cd jev-llm-gateway
uv run jev doctor
uv run jev serve
uv run jev smoke --tier small
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/Arwin-K/jev-llm-gateway/blob/1bcffb0e63efcc6e7a668385e27d2769b49c3e29/README.md](https://github.com/Arwin-K/jev-llm-gateway/blob/1bcffb0e63efcc6e7a668385e27d2769b49c3e29/README.md)
- Feature status: [github.com/Arwin-K/jev-llm-gateway/blob/1bcffb0e63efcc6e7a668385e27d2769b49c3e29/docs/FEATURE_STATUS.md](https://github.com/Arwin-K/jev-llm-gateway/blob/1bcffb0e63efcc6e7a668385e27d2769b49c3e29/docs/FEATURE_STATUS.md)

## Limits and data handling

With the Jev router on, prompts go to TypeSafe on your key under configured caps; local tiers run on Ollama. The author marks several features as implemented but not yet measured.

## Review and maintenance

Reviewed **2026-11-14** (Europe/Sofia) at [commit 1bcffb0e63ef](https://github.com/Arwin-K/jev-llm-gateway/tree/1bcffb0e63efcc6e7a668385e27d2769b49c3e29). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
