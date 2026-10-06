# goinfer

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Pure-Go, no-cgo local LLM inference (library and server) whose `POST /v1/systemone` answers TypeSafe's decisions wire shape so clients such as jevx work against it; it scores option labels with the served model or loads a trained decision head — TypeSafe's hosted model is not included.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/townsendmerino/goinfer) |
| Product homepage | [goinfer.dev](https://goinfer.dev) |
| Maintainer | [townsendmerino](https://github.com/townsendmerino). Independently curated. |
| Format | Go module and prebuilt binaries for macOS, Linux and Windows (Intel/ARM) |
| Requirements | A GGUF model (or the bundled 0.5B/1.5B single-file builds); optional trained decision head. No TypeSafe account. |
| License | [MIT](https://github.com/townsendmerino/goinfer/blob/d0b234316d5d6a692460f227ea82f0467e259214/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Test a Jev client (e.g. jevx) against a local, offline endpoint with the same request/response shape.
- Experiment with local decision heads and compare calibration to published Jev numbers.
- Mismatch: label scoring with a general chat model is well short of a trained head (upstream measures top-1 0.42 vs JEV-9B's published 0.92), so do not treat it as a Jev substitute without a head.

## How it works

By default `/v1/systemone` does one prefill per question and scores each option label with the served model (no decode). A trained decision head in the JEV layout can be loaded with `--model name=DIR,head=DIR` (see `docs/server.md`). The [jevx recipe](https://github.com/townsendmerino/goinfer/blob/d0b234316d5d6a692460f227ea82f0467e259214/docs/integrations/typesafe-jevx.md) and dated measurement records under `docs/measurements/` document the comparisons.

## Get started

Download a release binary (sha256 on the release) and point a Jev client at the local `/v1/systemone`:

```sh
# from https://github.com/townsendmerino/goinfer/releases/latest
./goinfer-serve-<os>-<arch> --help
# load a model, then POST http://localhost:<port>/v1/systemone with a TypeSafe-shaped body
# see docs/integrations/typesafe-jevx.md
```

Runs locally; no TypeSafe charges.

## Examples and demos

- `docs/measurements/decisions-d6a-2026-09-28.md` (Qwen3.5-9B label scoring vs JEV-9B) and Clef comparison records (maintainer-reported; not reproduced).
- jevx integration recipe.

## Limits and data handling

Independent project, not affiliated with TypeSafe; does not include or proxy hosted Jev. Quality depends on the model/head you load. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-06** (Europe/Sofia) at [commit d0b234316d5d](https://github.com/townsendmerino/goinfer/tree/d0b234316d5d6a692460f227ea82f0467e259214). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
