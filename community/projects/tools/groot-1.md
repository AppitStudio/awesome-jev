# Groot 1 (open typed-decision model in the System One format)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Open 149M-parameter typed-decision model that answers System One choice, score and noul questions with full probability distributions over states of up to 64k tokens, with a pure Bend implementation of its forward pass; the author reports it beating Jev on their 2,000-question test split.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/leofmarciano/groot) |
| Maintainer | [leofmarciano](https://github.com/leofmarciano). Independently curated. |
| Format | Python package (PyTorch) with Hugging Face weights and an optional HTTP server |
| Requirements | Python 3.10+, PyTorch 2.4+; about 569 MiB for the checkpoint. |
| License | [Apache-2.0](https://github.com/leofmarciano/groot/blob/371e82157a0c79320d053ea7ab8c39ad8ad37a6b/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Discovered via X ([post](https://x.com/leomarciano/status/2113275095812559353)). |
| Jev evidence | [`groot1/schema.py`](https://github.com/leofmarciano/groot/blob/371e82157a0c79320d053ea7ab8c39ad8ad37a6b/groot1/schema.py) at the pinned commit. |

## When to use

- Run System One-style decisions locally with open weights.
- Compare calibration and long-context behavior against hosted Jev.
- Mismatch: benchmark claims are the author's own; verify on your task.

## How it works

`groot1/schema.py` implements the System One request format (`choice`, `score`, `noul`) so the same questions you send to Jev can be answered by the local model; the optional server exposes it over HTTP. Integration evidence: [`groot1/schema.py`](https://github.com/leofmarciano/groot/blob/371e82157a0c79320d053ea7ab8c39ad8ad37a6b/groot1/schema.py).

## Get started

From the upstream README (not run on the review host):

```sh
python -m pip install huggingface_hub
python -c "from huggingface_hub import snapshot_download; snapshot_download('marcyano/Groot-1-S', local_dir='Groot-1-S')"
python -m pip install -e ./Groot-1-S
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Weights: [huggingface.co/marcyano/Groot-1-S](https://huggingface.co/marcyano/Groot-1-S)
- Article on X: [x.com/leomarciano/status/2113275095812559353](https://x.com/leomarciano/status/2113275095812559353)

## Limits and data handling

Independent model, not a TypeSafe product; runs locally, so nothing is sent to TypeSafe.

## Review and maintenance

Reviewed **2026-10-23** (Europe/Sofia) at [commit 371e82157a0c](https://github.com/leofmarciano/groot/tree/371e82157a0c79320d053ea7ab8c39ad8ad37a6b). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
