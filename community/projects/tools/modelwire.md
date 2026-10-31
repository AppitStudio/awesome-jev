# modelwire (async Python clients for the OpenAI Responses, Anthropic Messages and System One APIs)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Small async Python library with clients for the OpenAI Responses, Anthropic Messages and TypeSafe System One APIs behind one retry and error model, plus servers compatible with them for testing. `SystemOne(...).ask(model, state, questions)` returns typed answers from Jev.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/eyayaw/modelwire) |
| Maintainer | [eyayaw](https://github.com/eyayaw). Independently curated. |
| Format | Python package (Git install) |
| Requirements | Python 3.15+ per the README; a TypeSafe key. |
| License | [MIT](https://github.com/eyayaw/modelwire/blob/f8661ed15d57532068b4444789c2932488403777/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/modelwire/__init__.py`](https://github.com/eyayaw/modelwire/blob/f8661ed15d57532068b4444789c2932488403777/src/modelwire/__init__.py) at the pinned commit. |

## When to use

- Call Jev and generative models from the same async codebase.
- Mismatch: early v0.1.0 with a single dependency (httpx2).

## How it works

`src/modelwire/__init__.py` defines `SystemOne` with base URL `https://api.typesafe.ai/v1`, request-id capture and retries on 5xx/529, following TypeSafe's published OpenAPI schema. Integration evidence: [`src/modelwire/__init__.py`](https://github.com/eyayaw/modelwire/blob/f8661ed15d57532068b4444789c2932488403777/src/modelwire/__init__.py).

## Get started

From the upstream README (not run on the review host):

```sh
uv add "modelwire @ git+https://github.com/eyayaw/modelwire@v0.1.0"
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/eyayaw/modelwire#readme](https://github.com/eyayaw/modelwire#readme)

## Limits and data handling

Requests go to the API you call. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-01** (Europe/Sofia) at [commit f8661ed15d57](https://github.com/eyayaw/modelwire/tree/f8661ed15d57532068b4444789c2932488403777). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
