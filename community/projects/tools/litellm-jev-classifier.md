# LiteLLM Jev classifier (route gateway requests by complexity with Jev)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

LiteLLM, the open-source gateway that calls 100+ LLM APIs in OpenAI format, can use Jev as the classifier in its complexity router: one typed choice call grades each incoming request into a tier, and the proxy sends it to the models you mapped to that tier.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/BerriAI/litellm) |
| Maintainer | [BerriAI](https://github.com/BerriAI). Independently curated. |
| Format | Python SDK and proxy server (option in the complexity router) |
| Requirements | Python and LiteLLM (SDK or proxy); a TypeSafe API key for the Jev classifier. |
| License | [MIT (outside `enterprise/`)](https://github.com/BerriAI/litellm/blob/ada3614eb425b08224265dd3182361b68dfeed63/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`litellm/router_strategy/complexity_router/jev_classifier.py`](https://github.com/BerriAI/litellm/blob/ada3614eb425b08224265dd3182361b68dfeed63/litellm/router_strategy/complexity_router/jev_classifier.py) at the pinned commit. |

## When to use

- You already run LiteLLM and want a calibrated request grader instead of the default rule-based scorer.
- Send simple prompts to cheap models and hard ones to reasoning models with one setting.
- Mismatch: a router option inside a large gateway, not a standalone Jev client.

## How it works

With `classifier_type: "jev"`, `jev_classifier.py` posts one `tier` choice question (from `non_reasoning` up to `reasoning`) to `{api_base}/v1/systemone`. The config validator only sends `TYPESAFE_API_KEY` to TypeSafe's own base URL, and failures fall back to the configured default tier. Integration evidence: [`litellm/router_strategy/complexity_router/jev_classifier.py`](https://github.com/BerriAI/litellm/blob/ada3614eb425b08224265dd3182361b68dfeed63/litellm/router_strategy/complexity_router/jev_classifier.py).

## Get started

Outline based on the LiteLLM source and docs (not run on the review host):

```sh
pip install 'litellm[proxy]'
export TYPESAFE_API_KEY=...
# set classifier_type: "jev" in the complexity router config
litellm --config config.yaml
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- LiteLLM docs: [docs.litellm.ai/docs/](https://docs.litellm.ai/docs/)
- Deepgram write-up covering the Jev classifier: [deepgram.com/learn/audio-decision-composition-five-open-source-jev-projects](https://deepgram.com/learn/audio-decision-composition-five-open-source-jev-projects)

## Limits and data handling

Each graded request's content is sent to TypeSafe when the Jev classifier is on. The `enterprise/` directory uses a separate commercial license; the classifier code reviewed here is in the MIT part.

## Review and maintenance

Reviewed **2026-10-24** (Europe/Sofia) at [commit ada3614eb425](https://github.com/BerriAI/litellm/tree/ada3614eb425b08224265dd3182361b68dfeed63). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
