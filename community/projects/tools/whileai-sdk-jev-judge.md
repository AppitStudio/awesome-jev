# whileai (agent post-training SDK with TypeSafe Jev as a judge backend)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Python SDK for evals, simulations and GRPO/SFT/DPO post-training of agents; its `typesafe:<model>` judge-only spec lets Jev grade outputs with typed, calibrated answers.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/whilehq/whileai-sdk) |
| Maintainer | [whilehq](https://github.com/whilehq). Independently curated. |
| Format | Python package on PyPI (`whileai`, Apache-2.0) |
| Requirements | Python with `uv add whileai`, plus `TYPESAFE_API_KEY` (or `WHILEAI_TYPESAFE_API_KEY`) for the Jev judge. |
| License | [Apache-2.0](https://github.com/whilehq/whileai-sdk/blob/c3d9a845f7f869defdb68bd07fab801611fe940b/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`whileai/simulations/generate/typesafe_backend.py`](https://github.com/whilehq/whileai-sdk/blob/c3d9a845f7f869defdb68bd07fab801611fe940b/whileai/simulations/generate/typesafe_backend.py) at the pinned commit. |

## When to use

- Use Jev as a calibrated judge inside an agent eval or training loop.
- Compare judges against human labels before trusting them.
- Mismatch: Jev is one optional judge among several; the SDK's main README does not mention it.

## How it works

`typesafe_backend.py` posts `{state, model, questions}` to `/v1/systemone` (`jev-latest` default, `TYPESAFE_BASE_URL` for a gateway); the docs show `data.grade(llm_spec="typesafe:jev-latest")`. Jev is a judge-only spec, not a generator. Integration evidence: [`whileai/simulations/generate/typesafe_backend.py`](https://github.com/whilehq/whileai-sdk/blob/c3d9a845f7f869defdb68bd07fab801611fe940b/whileai/simulations/generate/typesafe_backend.py).

## Get started

Install the package, set `TYPESAFE_API_KEY`, and pass `llm_spec="typesafe:jev-latest"` to grading as in `docs/reference/overview.md`.

```sh
uv add whileai
export TYPESAFE_API_KEY=...
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Judge spec reference: [github.com/whilehq/whileai-sdk/blob/c3d9a845f7f869defdb68bd07fab801611fe940b/docs/reference/overview.md](https://github.com/whilehq/whileai-sdk/blob/c3d9a845f7f869defdb68bd07fab801611fe940b/docs/reference/overview.md)

## Limits and data handling

Graded transcripts go to TypeSafe on your key when the typesafe judge is selected.

## Review and maintenance

Reviewed **2026-11-10** (Europe/Sofia) at [commit c3d9a845f7f8](https://github.com/whilehq/whileai-sdk/tree/c3d9a845f7f869defdb68bd07fab801611fe940b). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
