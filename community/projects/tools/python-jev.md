# python-jev (unofficial typed Python SDK for Jev)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Unofficial typed Python SDK for Jev: write each question once as a class, get choices and levels back as members of your own enums, ask all questions in one request, and pass text, Pydantic objects or JSON as state, with sync and async clients typed for pyright and mypy.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/VianneyMI/python-jev) |
| Maintainer | [VianneyMI](https://github.com/VianneyMI). Independently curated. |
| Format | Python library on PyPI (MIT) |
| Requirements | Python 3.11+, `pip install python-jev` (imports as `jev`; conflicts with the separate `jev` package on PyPI), and `TYPESAFE_API_KEY`. |
| License | [MIT](https://github.com/VianneyMI/python-jev/blob/a0c876e79fcf85016e3a4907362dd0e9037460f7/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jev/_client.py`](https://github.com/VianneyMI/python-jev/blob/a0c876e79fcf85016e3a4907362dd0e9037460f7/src/jev/_client.py) at the pinned commit. |

## When to use

- Get typed answers in Python apps instead of parsing raw JSON.
- Ask several Jev questions about one state in a single call.
- Mismatch: unofficial; same import name as another PyPI package.

## How it works

`src/jev/_client.py` posts to `https://api.typesafe.ai/v1/systemone` and maps the answers back onto the declared question classes; a script checks the client against TypeSafe's published OpenAPI spec for drift. Integration evidence: [`src/jev/_client.py`](https://github.com/VianneyMI/python-jev/blob/a0c876e79fcf85016e3a4907362dd0e9037460f7/src/jev/_client.py).

## Get started

Install from PyPI, set your key and declare your questions as classes.

```sh
pip install python-jev
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/VianneyMI/python-jev/blob/a0c876e79fcf85016e3a4907362dd0e9037460f7/README.md](https://github.com/VianneyMI/python-jev/blob/a0c876e79fcf85016e3a4907362dd0e9037460f7/README.md)
- PyPI: [pypi.org/project/python-jev/](https://pypi.org/project/python-jev/)

## Limits and data handling

States you evaluate are sent to TypeSafe on your key.

## Review and maintenance

Reviewed **2026-11-12** (Europe/Sofia) at [commit a0c876e79fcf](https://github.com/VianneyMI/python-jev/tree/a0c876e79fcf85016e3a4907362dd0e9037460f7). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
