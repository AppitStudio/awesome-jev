# System 1: Instinct (local CPU decision runtime that learns repeatable typed decisions from a few examples and can shadow a TypeSafe-compatible teacher before cutting over)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Python runtime for repeatable structured decisions (choice, boolean, multi-choice and score fields) answered on CPU in milliseconds from hashed lexical features and online-updated weights, with no pretrained weights. It abstains when unsure, learns from 3–10 examples per option or a teacher callable, compiles skills to `.s1m`, and includes a TypeSafe-compatible client whose `auto_cutover` mode can call hosted Jev and switch to the local skill once agreement is high enough.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/steph4n-gh/system1-instinct) |
| Maintainer | [steph4n-gh](https://github.com/steph4n-gh). Independently curated. |
| Format | Python package on PyPI, CLI, MCP/HTTP server and Docker image (Apache-2.0) |
| Requirements | Python 3.11+. Local mode needs no key; network teacher calls need explicit opt-in and a `TYPESAFE_API_KEY`. |
| License | [Apache-2.0](https://github.com/steph4n-gh/system1-instinct/blob/4107a4bc8403a18754fd60cb2ffe5cf32ef15683/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/system1/compat/typesafe.py`](https://github.com/steph4n-gh/system1-instinct/blob/4107a4bc8403a18754fd60cb2ffe5cf32ef15683/src/system1/compat/typesafe.py) at the pinned commit. |

## When to use

- Move high-volume, repeatable decisions off a paid API once a local skill agrees with it.
- Mismatch: open-ended judgments; at zero examples it abstains, and quality depends on your examples.

## How it works

`src/system1/compat/typesafe.py` defines `TypeSafeClient` with base URL `https://api.typesafe.ai/v1`, posting to `/systemone` only in passthrough or cutover modes with cloud access enabled; the default `mode='local'` with `zero_egress=True` makes no network calls. Integration evidence: [`src/system1/compat/typesafe.py`](https://github.com/steph4n-gh/system1-instinct/blob/4107a4bc8403a18754fd60cb2ffe5cf32ef15683/src/system1/compat/typesafe.py).

## Get started

Install from PyPI and follow the README example to define a schema and teach it.

```sh
python -m pip install system1-instinct
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/steph4n-gh/system1-instinct/blob/4107a4bc8403a18754fd60cb2ffe5cf32ef15683/README.md](https://github.com/steph4n-gh/system1-instinct/blob/4107a4bc8403a18754fd60cb2ffe5cf32ef15683/README.md)
- PyPI: [pypi.org/project/system1-instinct/](https://pypi.org/project/system1-instinct/)

## Limits and data handling

Local mode keeps data on the machine; passthrough or cutover modes send requests to TypeSafe on your key. The maintainer's replays use dataset labels or a keyword stub; live-LLM-teacher evaluation is listed as planned.

## Review and maintenance

Reviewed **2026-11-14** (Europe/Sofia) at [commit 4107a4bc8403](https://github.com/steph4n-gh/system1-instinct/tree/4107a4bc8403a18754fd60cb2ffe5cf32ef15683). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
