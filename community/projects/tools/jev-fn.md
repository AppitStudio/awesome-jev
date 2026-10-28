# jev-fn (call Jev as an ordinary Python function that returns a probability)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Small Python wrapper around the official TypeSafe SDK that exposes Jev as one callable: `if jev("Is this customer angry?") > 0.9: flag_for_human_review()`. Set one environment variable (TypeSafe or OpenRouter) and use it in if-statements, loops and pipelines; sync and async clients, model choice through `configure()`.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/abhimanyuHatesToCode/jev-fn) |
| Maintainer | [abhimanyuHatesToCode](https://github.com/abhimanyuHatesToCode). Independently curated. |
| Format | Python package (PyPI `jev-fn`) |
| Requirements | Python and a TypeSafe or OpenRouter API key. |
| License | [MIT](https://github.com/abhimanyuHatesToCode/jev-fn/blob/6e05292cbdc2b3d713ef9ddff7387fbca6eb3820/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. The LICENSE file is MIT text but its copyright line still contains unresolved merge-conflict markers (GitHub shows NOASSERTION). Discovered via X ([post](https://x.com/abhimanyuisbusy/status/2115336754513494389)). |
| Jev evidence | [`src/jev_fn/core.py`](https://github.com/abhimanyuHatesToCode/jev-fn/blob/6e05292cbdc2b3d713ef9ddff7387fbca6eb3820/src/jev_fn/core.py) at the pinned commit. |

## When to use

- Drop yes/no semantic checks into ordinary Python code.
- Mismatch: Noul questions only; use the SDK directly for Choice and Score.

## How it works

`src/jev_fn/core.py` wraps `TypeSafeClient` and `AsyncTypeSafeClient` from `typesafe_sdk` and sends each call as a Noul question (`jev-latest` by default). Integration evidence: [`src/jev_fn/core.py`](https://github.com/abhimanyuHatesToCode/jev-fn/blob/6e05292cbdc2b3d713ef9ddff7387fbca6eb3820/src/jev_fn/core.py).

## Get started

From the upstream README (not run on the review host):

```sh
pip install jev-fn
export TYPESAFE_API_KEY=...   # or OPENROUTER_API_KEY
python -c 'from jev_fn import jev; print(jev("Is this customer angry?", context="I want my money back NOW"))'
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- PyPI: [pypi.org/project/jev-fn/](https://pypi.org/project/jev-fn/)
- README: [github.com/abhimanyuHatesToCode/jev-fn#readme](https://github.com/abhimanyuHatesToCode/jev-fn#readme)

## Limits and data handling

Each call sends its text to TypeSafe or OpenRouter, whichever key is set.

## Review and maintenance

Reviewed **2026-10-28** (Europe/Sofia) at [commit 6e05292cbdc2](https://github.com/abhimanyuHatesToCode/jev-fn/tree/6e05292cbdc2b3d713ef9ddff7387fbca6eb3820). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
