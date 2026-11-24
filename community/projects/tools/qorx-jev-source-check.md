# Qorx + Jev source check by bbrainfuckk (browser exercise and local runner where Jev picks which retrieved excerpt actually supports an answer)

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

A small exercise on retrieval for coding agents: two pinned FastAPI excerpts indexed by the Qorx CLI, and Jev chooses the excerpt that supports the answer or "Neither", with a companion Noul on whether the evidence is sufficient. Swap the file order, inspect the sources and download the exact request; a hosted browser version needs no key.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/bbrainfuckk/qorx-jev-source-check) |
| Maintainer | [bbrainfuckk](https://github.com/bbrainfuckk). Independently curated. |
| Format | Static web page plus a dependency-free Python runner |
| Requirements | Python 3.10+ for the runner; a TypeSafe API key only for the optional `--live` call. |
| License | [AGPL-3.0](https://github.com/bbrainfuckk/qorx-jev-source-check/blob/510be5f884615c03c39ee268c372358581b96de3/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`jev_check.py`](https://github.com/bbrainfuckk/qorx-jev-source-check/blob/510be5f884615c03c39ee268c372358581b96de3/jev_check.py) at the pinned commit. |

## When to use

- See how a companion Noul can catch retrieval that looks plausible but lacks the lines an answer needs.
- Mismatch: a retrieval library; this is a two-question teaching exercise.

## How it works

`jev_check.py` builds a Choice over the two excerpts plus a sufficiency Noul for `jev-1.14.0` and, only with `--live`, posts it to `api.typesafe.ai`; it validates the answer IDs and reports a supported candidate only above 0.8. Integration evidence: [`jev_check.py`](https://github.com/bbrainfuckk/qorx-jev-source-check/blob/510be5f884615c03c39ee268c372358581b96de3/jev_check.py).

## Get started

Try the hosted page, or preview the requests locally and run one live call with your key.

```sh
git clone https://github.com/bbrainfuckk/qorx-jev-source-check.git && cd qorx-jev-source-check
python jev_check.py --question positive
TYPESAFE_API_KEY=... python jev_check.py --question negative --live
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Hosted exercise: [qorx.idra-ai.com/labs/jev-source-check/](https://qorx.idra-ai.com/labs/jev-source-check/)
- README: [github.com/bbrainfuckk/qorx-jev-source-check/blob/510be5f884615c03c39ee268c372358581b96de3/README.md](https://github.com/bbrainfuckk/qorx-jev-source-check/blob/510be5f884615c03c39ee268c372358581b96de3/README.md)

## Limits and data handling

Only `--live` sends the excerpts and question to TypeSafe (up to two billable requests). The FastAPI excerpts keep FastAPI's own license (included). Code is AGPL-3.0.

## Review and maintenance

Reviewed **2026-11-24** (Europe/Sofia) at [commit 510be5f88461](https://github.com/bbrainfuckk/qorx-jev-source-check/tree/510be5f884615c03c39ee268c372358581b96de3). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
