# system-one for Hermes Agent by salismt (one tool for TypeSafe Jev and other System One decision models, with spend caps)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Hermes Agent plugin that puts System One decision models behind one `system_one` tool, so the provider is a setting: TypeSafe Jev, Liquid d1.2, Upstage Solar Decide, Microsoft-Decision-1, or open models such as Laya and Tev1 in Ollama. Before sending it checks each request against the model's known question types and limits and refuses ones that cannot work, enforces total, daily and per-call USD caps from a local SQLite ledger, and `/system-one` shows the provider, price, spend and which keys are set. Jev is one of several providers.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/salismt/hermes-system-one) |
| Maintainer | [salismt](https://github.com/salismt). Independently curated. |
| Format | Hermes Agent plugin (Python standard library, MIT) |
| Requirements | Hermes 0.23+; a key for the hosted provider you pick (`TYPESAFE_API_KEY` for Jev) or a local Ollama for open models. |
| License | [MIT](https://github.com/salismt/hermes-system-one/blob/9a48299c73db92e7cb175b23af24dc4315afd49a/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`system_one/providers.py`](https://github.com/salismt/hermes-system-one/blob/9a48299c73db92e7cb175b23af24dc4315afd49a/system_one/providers.py) at the pinned commit. |

## When to use

- Give a Hermes agent typed decisions and switch between Jev and other decision models without code changes.
- Mismatch: text generation; decision models only answer typed questions.

## How it works

`system_one/providers.py` registers the `jev` provider at `https://api.typesafe.ai` with `TYPESAFE_API_KEY`, next to the other hosted and local System One providers; requests use `POST /v1/systemone`. Integration evidence: [`system_one/providers.py`](https://github.com/salismt/hermes-system-one/blob/9a48299c73db92e7cb175b23af24dc4315afd49a/system_one/providers.py).

## Get started

Install and enable the plugin, then pick a provider and add its key.

```sh
hermes plugins install salismt/hermes-system-one
hermes plugins enable system-one
export TYPESAFE_API_KEY=...   # for provider jev
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/salismt/hermes-system-one/blob/9a48299c73db92e7cb175b23af24dc4315afd49a/README.md](https://github.com/salismt/hermes-system-one/blob/9a48299c73db92e7cb175b23af24dc4315afd49a/README.md)

## Limits and data handling

Questions and state go to the provider you pick on your key (or stay local with Ollama). Spend caps are checked against the plugin's own ledger, not the provider's billing. The README's speed and price figures are single measurements, as it says.

## Review and maintenance

Reviewed **2026-11-17** (Europe/Sofia) at [commit 9a48299c73db](https://github.com/salismt/hermes-system-one/tree/9a48299c73db92e7cb175b23af24dc4315afd49a). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
