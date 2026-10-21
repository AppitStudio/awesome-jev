# minifactory

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Small pluggable software factory where declarative YAML workflows of plugin steps fence AI agents in with budgets and real gates; its default router asks Jev which workflow fits a plain-language request.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/juan-campuzano/minifactory) |
| Maintainer | [juan-campuzano](https://github.com/juan-campuzano). Independently curated. |
| Format | CLI and Python package |
| Requirements | Python with uv or pipx; `TYPESAFE_API_KEY` for the default Jev router (`--router keyword` works offline); an LLM backend such as Bedrock for real runs. |
| License | [MIT](https://github.com/juan-campuzano/minifactory/blob/1884a03e7dc5f5a2f38f43601db62b31a8af56cf/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/minifactory/plugins/builtin/routers.py`](https://github.com/juan-campuzano/minifactory/blob/1884a03e7dc5f5a2f38f43601db62b31a8af56cf/src/minifactory/plugins/builtin/routers.py) at the pinned commit. |

## When to use

- Run repeatable agent workflows with compiler, test and diff-size gates.
- Let `minifactory ask` pick the workflow and draft its input from a sentence.
- Mismatch: alpha; the shipped example uses canned LLM replies.

## How it works

`minifactory ask` sends your request and the routable workflows to Jev (`https://api.typesafe.ai/v1/systemone`, see `src/minifactory/plugins/builtin/routers.py`) and the caller's policy decides what to do with the confidence before anything runs. Integration evidence: [`src/minifactory/plugins/builtin/routers.py`](https://github.com/juan-campuzano/minifactory/blob/1884a03e7dc5f5a2f38f43601db62b31a8af56cf/src/minifactory/plugins/builtin/routers.py).

## Get started

From the upstream README (not run on the review host):

```sh
uv tool install minifactory
minifactory init my-factory && cd my-factory
minifactory workflows copy flutter-app-factory
minifactory run flutter-app-factory
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Limitations and architecture in the README: [github.com/juan-campuzano/minifactory#readme](https://github.com/juan-campuzano/minifactory#readme)

## Limits and data handling

Requests are sent to TypeSafe for routing when the Jev router is used.

## Review and maintenance

Reviewed **2026-10-21** (Europe/Sofia) at [commit 1884a03e7dc5](https://github.com/juan-campuzano/minifactory/tree/1884a03e7dc5f5a2f38f43601db62b31a8af56cf). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
