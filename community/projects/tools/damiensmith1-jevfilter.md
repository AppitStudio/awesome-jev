# jevfilter

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

Python library/PyPI: filter or classify text with plain-English rules via TypeSafe Jev (choose/check/rate).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/damiensmith1/jevfilter) |
| Maintainer | [damiensmith1](https://github.com/damiensmith1). Independently curated. |
| Format | Python library (PyPI `jevfilter`). |
| Requirements | Python 3.10+; TYPESAFE_API_KEY; optional yaml extra. |
| License | [MIT](https://github.com/damiensmith1/jevfilter/blob/ea832c3a013cdce296934eaff732f5665e9abbc0/LICENSE). TypeSafe usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live TypeSafe/provider paths not run on the review host. |

## When to use

Use for **stateless plain-English filters** over content. Prefer heavier RAG/rerank tools when you need retrieval stacks.

## How it works

Wraps TypeSafe Jev Choice/Noul/Score helpers (`choose`, `check`, `rate`) with no local storage—caller persists results.

## Get started

```sh
git clone https://github.com/damiensmith1/jevfilter.git
cd jevfilter
git checkout ea832c3a013cdce296934eaff732f5665e9abbc0
# pip install "jevfilter[yaml]"; export TYPESAFE_API_KEY=...
```

## Examples and demos

- Upstream README quickstart and examples at the pinned commit.
- Separate interactive demos only where the upstream README links them; none were executed on the review host.

## Limits and data handling

Live Jev/TypeSafe (or other provider) calls send the judged text/state to that provider and may incur charges. Offline/demo paths stay local when documented upstream. Catalog checks did not run live integrations.

## Review and maintenance

Reviewed **2026-09-26** (Europe/Sofia) at [commit ea832c3](https://github.com/damiensmith1/jevfilter/tree/ea832c3a013cdce296934eaff732f5665e9abbc0). AI-assisted README and license inspection; install/live paths not executed.
