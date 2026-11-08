# chatsnack (Python ChatGPT library with a Jev sampler backend)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Long-running Python library for rapid OpenAI chat development; its sampler supports TypeSafe Jev (including Jev 1.14 vision) with `params.provider: typesafe`.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Mattie/chatsnack) |
| Maintainer | [Mattie](https://github.com/Mattie). Independently curated. |
| Format | Python library (MIT) |
| Requirements | Python, `pip install chatsnack`, and a TypeSafe API key for the Jev backend. |
| License | [MIT](https://github.com/Mattie/chatsnack/blob/6d9402e552153fa5489c62cca7062436d3474f40/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`chatsnack/sampler/models.py`](https://github.com/Mattie/chatsnack/blob/6d9402e552153fa5489c62cca7062436d3474f40/chatsnack/sampler/models.py) at the pinned commit. |

## When to use

- Sample typed answers from Jev inside chatsnack workflows.
- Mix chat and decision calls in one library.
- Mismatch: provider must be set explicitly since 0.10.

## How it works

`chatsnack/sampler/models.py` translates questions into Jev vocabulary and routes Jev model names to the TypeSafe backend; see the 0.10 migration notes. Integration evidence: [`chatsnack/sampler/models.py`](https://github.com/Mattie/chatsnack/blob/6d9402e552153fa5489c62cca7062436d3474f40/chatsnack/sampler/models.py).

## Get started

Install chatsnack and set `params.provider: typesafe` for sampler calls.

```sh
git clone https://github.com/Mattie/chatsnack.git && cd chatsnack
export TYPESAFE_API_KEY=...
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Sampler web example: [github.com/Mattie/chatsnack/tree/6d9402e552153fa5489c62cca7062436d3474f40/examples/sampler-web](https://github.com/Mattie/chatsnack/tree/6d9402e552153fa5489c62cca7062436d3474f40/examples/sampler-web)

## Limits and data handling

Sampler inputs are sent to TypeSafe on your key.

## Review and maintenance

Reviewed **2026-11-09** (Europe/Sofia) at [commit 6d9402e55215](https://github.com/Mattie/chatsnack/tree/6d9402e552153fa5489c62cca7062436d3474f40). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
