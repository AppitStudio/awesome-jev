# mrouter (local and cloud model router)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Zero-dependency Python proxy that routes OpenAI-compatible requests across LM Studio models and priced cloud gateways, using Jev to classify each prompt by use case and forcing sensitive prompts onto local models.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/radioboxtv/mrouter) |
| Maintainer | [radioboxtv](https://github.com/radioboxtv). Independently curated. |
| Format | OpenAI-compatible proxy (Python 3.9+ stdlib) |
| Requirements | Python 3.9+; LM Studio and/or an OpenAI-compatible gateway; optional `TYPESAFE_API_KEY` (falls back to a local keyword classifier). |
| License | [MIT](https://github.com/radioboxtv/mrouter/blob/5e55fceb8cd6aa2df94542dcb43fe37d04dfd068/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`mrouter/categorize.py`](https://github.com/radioboxtv/mrouter/blob/5e55fceb8cd6aa2df94542dcb43fe37d04dfd068/mrouter/categorize.py) at the pinned commit. |

## When to use

- Point a client like Hermes Agent at model `auto` and let cost and capability pick the model.
- Keep sensitive prompts on your Mac by construction.
- Mismatch: built around Apple Silicon and LM Studio.

## How it works

For each request, `mrouter/categorize.py` asks Jev for use-case probabilities (chat, coding, sensitive, thinking); mrouter blends them into model scores for capability, speed, context and cost, and any prompt over the sensitive floor goes local only. Integration evidence: [`mrouter/categorize.py`](https://github.com/radioboxtv/mrouter/blob/5e55fceb8cd6aa2df94542dcb43fe37d04dfd068/mrouter/categorize.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/radioboxtv/mrouter && cd mrouter
cp config.example.json config.json
python3 -m mrouter scan
python3 -m mrouter serve
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- How routing works in the README: [github.com/radioboxtv/mrouter#readme](https://github.com/radioboxtv/mrouter#readme)

## Limits and data handling

Prompts are sent to TypeSafe for classification when a key is set; with the sensitive route, that classification call still sees the prompt.

## Review and maintenance

Reviewed **2026-10-21** (Europe/Sofia) at [commit 5e55fceb8cd6](https://github.com/radioboxtv/mrouter/tree/5e55fceb8cd6aa2df94542dcb43fe37d04dfd068). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
