# clangd-rerank (Korean-language research and VS Code extension that reorders clangd completions with a decision model, Jev or a small local Kev)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Preserved research repository on re-ordering the completion candidates clangd produces for C and C++ using a decision model. A three-stage pipeline has clangd produce up to 255 candidates, a LightGBM feature ranker keep the top K, and a decision model score them as a Choice question. The default path is a locally served fine-tuned Kev 0.8B model; a Jev backend through TypeSafe is a setting. It includes the models, training logs and comparison results, an LSP proxy and a VS Code extension, with self-hosted install steps. Documentation is in Korean.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Bartimaeus-han/clangd-rerank) |
| Maintainer | [Bartimaeus-han](https://github.com/Bartimaeus-han). Independently curated. |
| Format | Python LSP proxy, VS Code extension and model artifacts (Korean docs) |
| Requirements | clangd, Python, a VS Code install for the extension, and either a local Kev server (GPU) or a `TYPESAFE_API_KEY` for the Jev backend. |
| License | [MIT](https://github.com/Bartimaeus-han/clangd-rerank/blob/46e1591f29be43337361b2a8da0e0ddeb1cadde7/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`scripts/clangd_rerank_proxy.py`](https://github.com/Bartimaeus-han/clangd-rerank/blob/46e1591f29be43337361b2a8da0e0ddeb1cadde7/scripts/clangd_rerank_proxy.py) at the pinned commit. |

## When to use

- Study or reproduce reranking of code completions with a small typed decision model, with measured comparisons kept in the repo.
- Mismatch: it is research-grade, in Korean, and its default backend is a local fine-tuned Kev model rather than Jev.

## How it works

`scripts/clangd_rerank_proxy.py` posts the candidates as a Choice question to `<RERANK_BASE_URL>/v1/systemone` (the extension's README says the Jev backend sends the 40 lines before the cursor and the candidate names); with the base URL empty and `TYPESAFE_API_KEY` set it uses `https://api.typesafe.ai` and `jev-latest`, otherwise a local Kev server. Integration evidence: [`scripts/clangd_rerank_proxy.py`](https://github.com/Bartimaeus-han/clangd-rerank/blob/46e1591f29be43337361b2a8da0e0ddeb1cadde7/scripts/clangd_rerank_proxy.py).

## Get started

From the upstream README (not run on the review host):

```sh
# see INSTALL.md: start the local rerank server (or set TYPESAFE_API_KEY for Jev),
# then point VS Code's clangd.path at the proxy launcher
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Install guide (Korean): [github.com/Bartimaeus-han/clangd-rerank/blob/46e1591f29be43337361b2a8da0e0ddeb1cadde7/INSTALL.md](https://github.com/Bartimaeus-han/clangd-rerank/blob/46e1591f29be43337361b2a8da0e0ddeb1cadde7/INSTALL.md)
- README with the pipeline and model folders: [github.com/Bartimaeus-han/clangd-rerank#readme](https://github.com/Bartimaeus-han/clangd-rerank#readme)

## Limits and data handling

With the Jev backend, code near your cursor and candidate names go to TypeSafe on your key; the local Kev path stays on your machine. The repository states a 50 ms median serving round trip for its local model, which was not measured here. Documentation is in Korean. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-04** (Europe/Sofia) at [commit 46e1591f29be](https://github.com/Bartimaeus-han/clangd-rerank/tree/46e1591f29be43337361b2a8da0e0ddeb1cadde7). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
