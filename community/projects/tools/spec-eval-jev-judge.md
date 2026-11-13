# spec-eval (grades a chat model against the OpenAI Model Spec's own examples, with Jev as the judge on OpenRouter)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Turns about 180 example conversations from the OpenAI Model Spec (marked GOOD, OK or BAD) into 186 test items, asks the model under test each one, and has Jev grade every answer against the spec section and reference answers through OpenRouter's Decisions API.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/pwhiting/spec-eval) |
| Maintainer | [pwhiting](https://github.com/pwhiting). Independently curated. |
| Format | Python script with extracted test set (uv; no license file) |
| Requirements | uv and an OpenRouter key with access to the model under test and to Jev. |
| License | No license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`spec_eval.py`](https://github.com/pwhiting/spec-eval/blob/1508188629780a74afc52b079e885ac68a0ce1ce/spec_eval.py) at the pinned commit. |

## When to use

- Check how a model follows the OpenAI Model Spec with a cheap probabilistic judge.
- Mismatch: a validated grader; Jev's agreement with human graders is not measured here.

## How it works

`spec_eval.py` sends each judgment to `https://openrouter.ai/api/alpha/decisions` with the default judge `typesafe/jev-1.14`; the model under test defaults to `openai/gpt-6-luna` via OpenRouter chat. `extract_spec.py` rebuilds the item set from the published spec. Integration evidence: [`spec_eval.py`](https://github.com/pwhiting/spec-eval/blob/1508188629780a74afc52b079e885ac68a0ce1ce/spec_eval.py).

## Get started

Clone, export your OpenRouter key, and run a five-item smoke test.

```sh
git clone https://github.com/pwhiting/spec-eval && cd spec-eval
export OPENROUTER_API_KEY=...
uv run spec_eval.py --limit 5
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/pwhiting/spec-eval/blob/1508188629780a74afc52b079e885ac68a0ce1ce/README.md](https://github.com/pwhiting/spec-eval/blob/1508188629780a74afc52b079e885ac68a0ce1ce/README.md)

## Limits and data handling

Spec prompts and the tested model's answers go to OpenRouter on your key.

## Review and maintenance

Reviewed **2026-11-13** (Europe/Sofia) at [commit 150818862978](https://github.com/pwhiting/spec-eval/tree/1508188629780a74afc52b079e885ac68a0ce1ce). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
