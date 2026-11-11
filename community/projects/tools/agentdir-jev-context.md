# agentdir (local agent mailstore with opt-in Jev context filtering)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Local-first, Maildir-inspired work mailstore for software agents; an opt-in reranker sends the task and up to 20 local candidate passages to Jev to filter and rank context for `work start` and `context build`.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/jstxn/agentdir) |
| Maintainer | [jstxn](https://github.com/jstxn). Independently curated. |
| Format | Python CLI (MIT) |
| Requirements | Python, and `TYPESAFE_API_KEY` (or `JEV_API_KEY`) after `agentdir memory reranker configure jev`. |
| License | [MIT](https://github.com/jstxn/agentdir/blob/c5d37787b17136b983b1a267ca6fbc1e454f30ad/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/agentdir/jev.py`](https://github.com/jstxn/agentdir/blob/c5d37787b17136b983b1a267ca6fbc1e454f30ad/src/agentdir/jev.py) at the pinned commit. |

## When to use

- Filter local agent memory down to task-relevant context with a typed check.
- Mismatch: off by default; small project.

## How it works

`src/agentdir/jev.py` scores candidates with `jev-1.13.0` against a fixed rubric (threshold 0.7, 20 candidates, 3 s timeout) and redacts text first; `scripts/eval_jev.py` evaluates it. Integration evidence: [`src/agentdir/jev.py`](https://github.com/jstxn/agentdir/blob/c5d37787b17136b983b1a267ca6fbc1e454f30ad/src/agentdir/jev.py).

## Get started

Opt in per store, then start work as usual; configure `none` to go back to local-only selection.

```sh
agentdir memory reranker configure jev
agentdir work start "make database migrations safe to roll back"
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/jstxn/agentdir/blob/c5d37787b17136b983b1a267ca6fbc1e454f30ad/README.md](https://github.com/jstxn/agentdir/blob/c5d37787b17136b983b1a267ca6fbc1e454f30ad/README.md)

## Limits and data handling

The task (up to 2048 bytes) and up to 20 redacted passages (1024 bytes each) go to TypeSafe when enabled.

## Review and maintenance

Reviewed **2026-11-11** (Europe/Sofia) at [commit c5d37787b171](https://github.com/jstxn/agentdir/tree/c5d37787b17136b983b1a267ca6fbc1e454f30ad). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
