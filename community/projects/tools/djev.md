# djev by Prakash Kagitha (Deterministic Jev: self-hosted Jev-compatible decisions that repeat bit for bit)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Self-hosted server for the Jev `POST /v1/systemone` API whose answers repeat exactly for the same request bytes, across load, restarts and a second GPU of the same model. Built on openjev-sglang, a Qwen3.5-9B decision LoRA (Bespoke Nimble) and SGLang's deterministic mode plus patches. On TypeSafe's consistency and guardrail cookbooks it compares against hosted Jev 1.13: zero answer flips between identical calls, with lower accuracy than hosted Jev on some jailbreaks.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/prakashkagitha/djev) |
| Maintainer | [Prakash Kagitha](https://github.com/prakashkagitha) (prakashkagitha). Independently curated. |
| Format | Python server + SGLang patches + replay tests and benchmarks |
| Requirements | An NVIDIA H100-class GPU, SGLang 0.5.19, openjev-sglang and the Bespoke Nimble LoRA merged into Qwen3.5-9B. |
| License | [MIT](https://github.com/prakashkagitha/djev/blob/88a067b5aff53ca6e34fd0fc59dd53612bab495d/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`server/detjev/serve.py`](https://github.com/prakashkagitha/djev/blob/88a067b5aff53ca6e34fd0fc59dd53612bab495d/server/detjev/serve.py) at the pinned commit. |

## When to use

- Teams who need replayable, auditable decisions for guardrails or tests and can self-host a GPU.
- Mismatch: matching hosted Jev accuracy; the README notes misses that hosted Jev catches.

## How it works

`server/detjev/serve.py` fronts the openjev-sglang API at `/v1/systemone` with an optional exact memo keyed by request bytes and key-order canonicalisation. The hosted-Jev comparison runs called TypeSafe's API with the author's key; the server itself does not call TypeSafe. Integration evidence: [`server/detjev/serve.py`](https://github.com/prakashkagitha/djev/blob/88a067b5aff53ca6e34fd0fc59dd53612bab495d/server/detjev/serve.py).

## Get started

Follow the quick start to build the engine and API, then run the benchmarks.

```sh
git clone https://github.com/prakashkagitha/djev && cd djev
# install SGLang 0.5.19 + patches and merge the Nimble LoRA (see README)
scripts/serve_bg.sh djev models/nimble-9b-merged 1 30020
scripts/api_up.sh djev
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Evidence: [github.com/prakashkagitha/djev/blob/main/docs/EVIDENCE.md](https://github.com/prakashkagitha/djev/blob/main/docs/EVIDENCE.md)
- Results: [github.com/prakashkagitha/djev#results](https://github.com/prakashkagitha/djev#results)

## Limits and data handling

Determinism holds for a fixed model, engine version, flags and GPU model; cross-GPU-model agreement is untested. Results were measured against `jev-1.13.0` on 2026-09-28. Upstream models and datasets keep their own terms.

## Review and maintenance

Reviewed **2026-11-28** (Europe/Sofia) at [commit 88a067b5aff5](https://github.com/prakashkagitha/djev/tree/88a067b5aff53ca6e34fd0fc59dd53612bab495d). Inspected the README, LICENSE and `server/detjev/serve.py` at the pinned commit; nothing was installed or run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
